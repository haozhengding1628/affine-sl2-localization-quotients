# Bounded Windows adaptation of Danus

This experiment uses upstream `frenzymath/Danus`, release `v0.1.0-codex`, commit
`7a51336e53cd1d558d0e766a61eb0fed46ebb05b` (Apache-2.0).
The source checkout is `../work/danus-src`; it is not modified.

This is NOT a full Linux deployment or a Lean/Coq formalization. It keeps the
upstream deterministic prechecks, verify-service entry point, worker submission
gate, content-addressed fact graph and verification traces. A bounded native
Windows supervisor replaces the Linux daemon/process transport. Worker proposals
are passed unchanged to `gateway.fact_submit`; only a cold-start verifier's
accepted proposals enter the graph. The supervisor supplies no positive verdicts.

Safety differences from upstream:

- Existing Codex authentication only; no credential files are copied or printed.
- `--ignore-user-config`, `--ephemeral`, `--sandbox read-only` for each model run.
- No upstream bootstrap, shell daemon, global plugin/config edit, paid strategy
  consult, publication, background monitoring, or sandbox bypass.
- Workers return a JSON proposal; the supervisor writes only run artifacts.
- Verifiers return JSON through CLI output capture, not model filesystem writes.
- In-process calls replace localhost HTTP/MCP for this bounded trial.
- Verifier output is additionally checked for consistency: no acceptance with
  errors/gaps, malformed fields, or missing output. Transport errors are not proofs.
- At most two worker attempts per claim; one independent verifier per attempt.

Run with the project-local virtual environment:

    work/danus-venv/Scripts/python.exe danus_trial/run_trial.py

Use `--job boundary` or `--job derivation` to select a single research question.
The run manifest, proposals, verdicts, logs and genuine Danus facts are saved under
`work/danus-runs/`. These are research drafts and LLM audits, not formal certificates.

Offline transport/core/precheck/service tests (2026-09-08): 67 passed, with two
dependency deprecation warnings. Test-only canned verdicts are confined to pytest
temporary directories, never to the research project. These tests check software
contracts, not the mathematical theorems.

The original user's questions and a precise mathematical scope are recorded in
`boundary.md` and `derivation.md`. Existing notes are hypotheses to audit, not
automatically accepted facts. PBW is the only foundational theorem allowed without
restating a full proof; all localization and induction claims must be justified.
