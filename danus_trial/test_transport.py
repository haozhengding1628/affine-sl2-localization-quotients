"""Offline adapter checks; fake verdicts stay exclusively in pytest temp dirs."""
import copy
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent))
from run_trial import validate_verdict
from danus.gateway import server as gateway
from danus.verify import service
from danus.core import FactGraph

CLEAN = {"verification_report": {"summary": "offline test only", "critical_errors": [], "gaps": []},
         "verdict": "correct", "repair_hints": ""}
STATEMENT = "For every integer n, adding zero leaves n unchanged."
PROOF = "Zero is the additive identity in the group of integers, hence n plus zero is n for every integer n."


def test_consistent_clean():
    assert validate_verdict(copy.deepcopy(CLEAN))["verdict"] == "correct"


@pytest.mark.parametrize("mutation", [
    lambda x: x.update(verdict="maybe"),
    lambda x: x.update(repair_hints="hidden gap"),
    lambda x: x["verification_report"]["gaps"].append({"location": "1", "issue": "missing proof"}),
    lambda x: x["verification_report"].update(critical_errors=None),
    lambda x: x["verification_report"].update(summary=""),
    lambda x: x.update(verdict="wrong", repair_hints="fix it"),
])
def test_inconsistent_verdict_fails_closed(mutation):
    value = copy.deepcopy(CLEAN)
    mutation(value)
    with pytest.raises(ValueError):
        validate_verdict(value)


def test_reject_does_not_write_fact(tmp_path, monkeypatch):
    monkeypatch.setenv("DANUS_PROJECT_DIR", str(tmp_path))
    reject = copy.deepcopy(CLEAN)
    reject["verdict"] = "wrong"
    reject["repair_hints"] = "supply a missing argument"
    reject["verification_report"]["gaps"] = [{"location": "test", "issue": "missing argument"}]
    monkeypatch.setattr(gateway, "_verify", lambda s, p: validate_verdict(reject))
    answer = gateway.fact_submit(STATEMENT, PROOF)
    assert answer["accepted"] is False
    assert FactGraph(tmp_path).list() == []


def test_transport_failure_does_not_write_fact(tmp_path, monkeypatch):
    monkeypatch.setenv("DANUS_PROJECT_DIR", str(tmp_path))
    def broken(s, p):
        raise RuntimeError("offline simulated transport failure")
    monkeypatch.setattr(gateway, "_verify", broken)
    answer = gateway.fact_submit(STATEMENT, PROOF)
    assert answer["verdict"] == "error"
    assert FactGraph(tmp_path).list() == []


def test_only_validated_acceptance_enters_temp_graph(tmp_path, monkeypatch):
    monkeypatch.setenv("DANUS_PROJECT_DIR", str(tmp_path))
    monkeypatch.setattr(gateway, "_verify", lambda s, p: validate_verdict(copy.deepcopy(CLEAN)))
    answer = gateway.fact_submit(STATEMENT, PROOF)
    assert answer["accepted"] is True
    assert FactGraph(tmp_path).list() == [answer["fact_id"]]


def test_precheck_prevents_model_call(monkeypatch):
    def forbidden(**kwargs):
        raise AssertionError("a vacuous proof must not reach the model")
    monkeypatch.setattr(service, "run_codex_verification", forbidden)
    with pytest.raises(Exception) as caught:
        service.verify(service.VerifyRequest(statement=STATEMENT, proof="QED"))
    assert getattr(caught.value, "status_code", None) == 400


def test_localization_polynomial_shift_regression():
    # Finite coefficient-independent evaluations: a regression check, not a proof.
    for n in range(-3, 4):
        for m in range(1, 5):
            for t in range(-2, 3):
                for r in range(5):
                    # F^-m P(d) = P(d+mn) F^-m; inverse uses d-mn.
                    assert ((t + m*n) - m*n)**r == t**r
                    # [d,F^-m] = -mn F^-m in the shifted polynomial model.
                    assert t*(t+m*n)**r - (t+m*n)**(r+1) == -m*n*(t+m*n)**r
