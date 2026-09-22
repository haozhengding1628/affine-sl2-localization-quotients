"""Bounded Windows transport for the unmodified Danus verification/write gate."""
from __future__ import annotations

import argparse
import concurrent.futures
import datetime as dt
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parent.parent
UPSTREAM = ROOT / "work" / "danus-src"
sys.path.insert(0, str(UPSTREAM))

ISSUE = {"type": "object", "properties": {
    "location": {"type": "string"}, "issue": {"type": "string"}},
    "required": ["location", "issue"], "additionalProperties": False}
VERDICT_SCHEMA = {"type": "object", "properties": {
    "verification_report": {"type": "object", "properties": {
        "summary": {"type": "string"},
        "critical_errors": {"type": "array", "items": ISSUE},
        "gaps": {"type": "array", "items": ISSUE}},
        "required": ["summary", "critical_errors", "gaps"], "additionalProperties": False},
    "verdict": {"type": "string", "enum": ["correct", "wrong"]},
    "repair_hints": {"type": "string"}},
    "required": ["verification_report", "verdict", "repair_hints"], "additionalProperties": False}
PROPOSAL_SCHEMA = {"type": "object", "properties": {
    "statement": {"type": "string"}, "proof": {"type": "string"},
    "scope_notes": {"type": "string"}},
    "required": ["statement", "proof", "scope_notes"], "additionalProperties": False}


def save_json(path, obj):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def validate_verdict(value):
    if not isinstance(value, dict) or set(value) != set(VERDICT_SCHEMA["required"]):
        raise ValueError("malformed verifier envelope")
    report = value["verification_report"]
    if not isinstance(report, dict) or set(report) != {"summary", "critical_errors", "gaps"}:
        raise ValueError("malformed report")
    if not isinstance(report["summary"], str) or not report["summary"].strip():
        raise ValueError("empty verifier summary")
    for field in ("critical_errors", "gaps"):
        if not isinstance(report[field], list):
            raise ValueError("issues must be lists")
        for issue in report[field]:
            if not isinstance(issue, dict) or set(issue) != {"location", "issue"}:
                raise ValueError("malformed issue")
            if not all(isinstance(x, str) and x.strip() for x in issue.values()):
                raise ValueError("empty issue")
    verdict, hints = value["verdict"], value["repair_hints"]
    clean = not report["critical_errors"] and not report["gaps"]
    if verdict not in ("correct", "wrong") or (verdict == "correct") != clean:
        raise ValueError("inconsistent verifier verdict; fail closed")
    if not isinstance(hints, str) or (verdict == "wrong") != bool(hints.strip()):
        raise ValueError("inconsistent repair hints")
    return value


def native_model_call(run_dir, label, prompt, schema):
    """Read-only model; only the supervisor/CLI captures the final output."""
    run_dir.mkdir(parents=True, exist_ok=True)
    schema_path = run_dir / f"{label}.schema.json"
    output_path = run_dir / f"{label}.json"
    save_json(schema_path, schema)
    (run_dir / f"{label}.prompt.txt").write_text(prompt, encoding="utf-8")
    executable = shutil.which("codex")
    if not executable:
        raise RuntimeError("codex CLI missing; no installation attempted")
    command = [executable, "exec", "--ignore-user-config", "--ephemeral",
               "--skip-git-repo-check", "--sandbox", "read-only",
               "-c", 'approval_policy="never"',
               "-c", 'model_reasoning_effort="high"',
               "-C", str(run_dir), "--color", "never", "--json",
               "--output-schema", str(schema_path),
               "--output-last-message", str(output_path), "-"]
    save_json(run_dir / f"{label}.command.json", command)
    env = dict(os.environ)
    # Existing authentication stays in place; do not copy/read credential stores.
    env["PYTHONUTF8"] = "1"
    with (run_dir / f"{label}.events.jsonl").open("w", encoding="utf-8") as out, \
         (run_dir / f"{label}.stderr.txt").open("w", encoding="utf-8") as err:
        result = subprocess.run(command, input=prompt, encoding="utf-8",
                                stdout=out, stderr=err, env=env,
                                timeout=900, check=False,
                                creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0))
    if result.returncode != 0:
        raise RuntimeError(f"{label}: codex exited {result.returncode}; see {run_dir}")
    if not output_path.is_file():
        raise RuntimeError(f"{label}: no output; not an accepted proof")
    return json.loads(output_path.read_text(encoding="utf-8"))


def verifier_contract():
    paths = [UPSTREAM / "agents/contracts/verifier.md"]
    paths += [UPSTREAM / "agents/skills/verify" / name / "SKILL.md" for name in (
        "verify-sequential-statements", "check-referenced-statements", "synthesize-verification-report")]
    return "\n\n".join(p.read_text(encoding="utf-8") for p in paths)


def worker_prompt(job, feedback="", previous=None):
    task = (ROOT / "danus_trial" / f"{job}.md").read_text(encoding="utf-8")
    return ("You are a bounded Danus mathematical proof worker, not the verifier. "
            "Construct a self-contained candidate for independent verification. "
            "Do not write files, launch agents, access credentials, or claim acceptance. "
            "Return only the requested JSON. Reason directly; do not call tools unless essential. "
            "Prove what is true and explicitly limit what is not established.\n\n" + task +
            ("\n\nPrevious candidate (unverified):\n" + json.dumps(previous, ensure_ascii=False)
             + "\n\nIndependent verifier feedback to repair:\n" + feedback if previous else ""))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--job", choices=["boundary", "derivation", "all"], default="all")
    parser.add_argument("--attempts", type=int, choices=[1, 2], default=2)
    args = parser.parse_args()
    stamp = dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    run = ROOT / "work/danus-runs" / stamp
    run.mkdir(parents=True, exist_ok=False)
    project = run / "project"
    project.mkdir()
    jobs = ["boundary", "derivation"] if args.job == "all" else [args.job]
    os.environ["DANUS_PROJECT_DIR"] = str(project)
    os.environ["DANUS_PROBLEM_ID"] = "affine-boundary-and-derivation"
    os.environ["DANUS_ROLE"] = "worker"
    os.environ["VERIFIER_RESULTS_DIR"] = str(run / "verification")
    from danus.gateway import server as gateway
    from danus.verify import service
    manifest = {"upstream_commit": "7a51336e53cd1d558d0e766a61eb0fed46ebb05b",
                "mode": "bounded-native-windows-inprocess-transport", "formal_proof": False,
                "run": str(run), "jobs": jobs, "attempts_per_job": args.attempts,
                "paid_consult": "off", "model": "existing CLI default", "outcomes": {}}
    save_json(run / "manifest.json", manifest)
    print(json.dumps({"event": "run_started", "run": str(run)}), flush=True)

    def cold_verify(run_id, statement, proof):
        prompt = ("This is a bounded native-Windows transport adaptation. Follow the attached "
                  "upstream Danus verification contract and skills for mathematical acceptance. "
                  "TRANSPORT OVERRIDE ONLY: do not write files or run agents; return the final "
                  "verification JSON, which the supervisor persists unchanged. No write to the "
                  "fact graph. The input is self-contained and PBW is an allowed foundational "
                  "theorem; if it instead relies on inaccessible external paper results, do not "
                  "pretend to have checked those. Check all shift signs and quantifiers.\n\n" +
                  verifier_contract() + "\n\nRun_id: " + run_id +
                  "\n\nStatement:\n" + statement + "\n\nProof:\n" + proof)
        print(json.dumps({"event": "verifier_started", "run_id": run_id}), flush=True)
        payload = native_model_call(run / "verification" / run_id, "verifier", prompt, VERDICT_SCHEMA)
        validate_verdict(payload)
        print(json.dumps({"event": "verifier_finished", "run_id": run_id,
                          "verdict": payload["verdict"]}), flush=True)
        return payload

    # Adapt transport, not the prechecks or the acceptance/write path.
    service.run_codex_verification = cold_verify
    gateway._verify = lambda statement, proof: service.verify(
        service.VerifyRequest(statement=statement, proof=proof))

    proposals = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
        futures = {pool.submit(native_model_call, run / job / "attempt1", "worker",
                               worker_prompt(job), PROPOSAL_SCHEMA): job for job in jobs}
        for future in concurrent.futures.as_completed(futures):
            job = futures[future]
            try:
                proposals[job] = future.result()
                print(json.dumps({"event": "worker_finished", "job": job}), flush=True)
            except Exception as error:
                manifest["outcomes"][job] = {"status": "transport_error", "error": str(error)}
                save_json(run / "manifest.json", manifest)
                print(json.dumps({"event": "worker_error", "job": job, "error": str(error)}), flush=True)

    for job, proposal in proposals.items():
        for attempt in range(1, args.attempts + 1):
            if not all(isinstance(proposal.get(k), str) and proposal[k].strip()
                       for k in ("statement", "proof")):
                manifest["outcomes"][job] = {"status": "invalid_proposal"}
                break
            os.environ["DANUS_AUTHOR"] = f"native-worker-{job}"
            result = gateway.fact_submit(statement=proposal["statement"], proof=proposal["proof"],
                                         intuition=proposal.get("scope_notes", ""))
            save_json(run / job / f"attempt{attempt}" / "submission.json", result)
            accepted = bool(result.get("accepted") and result.get("fact_id"))
            manifest["outcomes"][job] = {"status": "accepted" if accepted else "not_accepted",
                                        "attempt": attempt, "submission": result}
            save_json(run / "manifest.json", manifest)
            print(json.dumps({"event": "submission", "job": job, "attempt": attempt,
                              "accepted": accepted, "fact_id": result.get("fact_id")}), flush=True)
            if accepted or result.get("verdict") == "error" or attempt == args.attempts:
                break
            proposal = native_model_call(run / job / f"attempt{attempt+1}", "worker",
                                        worker_prompt(job, json.dumps(result, ensure_ascii=False), proposal),
                                        PROPOSAL_SCHEMA)
    save_json(run / "manifest.json", manifest)
    print(json.dumps({"event": "run_finished", "manifest": str(run / "manifest.json")}), flush=True)
    return 0 if all(x.get("status") == "accepted" for x in manifest["outcomes"].values()) else 2


if __name__ == "__main__":
    sys.exit(main())
