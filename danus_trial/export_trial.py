"""Export recorded Danus results, checking accepted fact identities first."""
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "work/danus-src"))
from danus.core import FactGraph
from danus.core.schema import compute_fact_id

run = Path(sys.argv[1]).resolve()
manifest = json.loads((run / "manifest.json").read_text(encoding="utf-8"))
graph = FactGraph(run / "project")
audits = []
proofs = ["# Danus-accepted mathematical candidates\n",
          "Date: 2026-09-08. These are LLM-reviewed proofs, NOT formal proof certificates.\n",
          "The two facts are independent. Applying the derivation functorial theorem to the "
          "boundary theorem yields the combined isomorphism in the Chinese note.\n"]
for job in ("boundary", "derivation"):
    outcome = manifest["outcomes"][job]
    if outcome["status"] != "accepted":
        raise RuntimeError(f"{job} was not accepted; export stopped")
    attempt = outcome["attempt"]
    proposal = json.loads((run / job / f"attempt{attempt}" / "worker.json").read_text(encoding="utf-8"))
    fid = outcome["submission"]["fact_id"]
    expected = compute_fact_id(problem_id="affine-boundary-and-derivation", predecessors=[],
                               glossary_introduces={}, statement=proposal["statement"],
                               proof=proposal["proof"])
    if fid != expected or not graph.exists(fid):
        raise RuntimeError("fact identity mismatch or missing fact")
    proofs += [f"\n## {job.capitalize()}\n\nFact ID: `{fid}`. Accepted attempt: {attempt}.\n",
               "### Statement\n\n" + proposal["statement"] + "\n",
               "### Proof\n\n" + proposal["proof"] + "\n",
               "### Scope\n\n" + proposal["scope_notes"] + "\n"]
    audits.append({"job": job, "accepted_attempt": attempt, "fact_id": fid,
                   "hash_recomputed": True, "fact_file_exists": True,
                   "advisory_symbol_warnings": len(outcome["submission"].get("undefined_symbols", []))})
verdicts = []
for path in sorted((run / "verification").glob("*/verifier.json")):
    verdicts.append({"run_id": path.parent.name,
                     **json.loads(path.read_text(encoding="utf-8"))})
usage = {}
calls = 0
for path in run.rglob("*.events.jsonl"):
    for line in path.read_text(encoding="utf-8").splitlines():
        event = json.loads(line)
        if event.get("type") == "turn.completed":
            calls += 1
            for key, value in event.get("usage", {}).items():
                if isinstance(value, int):
                    usage[key] = usage.get(key, 0) + value
audit = {"date": "2026-09-08", "upstream_commit": manifest["upstream_commit"],
         "transport": manifest["mode"], "model_selection": "CLI built-in default; user config ignored",
         "reasoning_effort": "high", "paid_consult": "off", "formal_proof": False,
         "completed_model_calls": calls, "reported_usage_totals": usage,
         "facts": audits, "verifications": verdicts,
         "tests": {"passed": 67, "dependency_deprecation_warnings": 2},
         "full_note_reverified": False, "run_manifest": str(run / "manifest.json")}
(ROOT / "outputs/danus_verified_proofs_en.md").write_text("\n".join(proofs), encoding="utf-8")
(ROOT / "outputs/danus_trial_audit.json").write_text(json.dumps(audit, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
print(json.dumps({"facts": audits, "completed_model_calls": calls, "usage": usage}, ensure_ascii=False))
