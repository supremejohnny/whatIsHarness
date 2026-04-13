import json
from pathlib import Path

from harness_demo.config import EVAL_DIR


def evaluate(run: dict) -> dict:
    checks = run.get("checks", {})
    functional = bool(checks.get("functional_correctness"))
    anti_hardcode = bool(checks.get("anti_hardcode_passed"))
    pytest_passed = bool(checks.get("pytest_passed"))
    schema_valid = bool(checks.get("schema_valid"))
    workflow_compliant = bool(checks.get("workflow_compliant"))
    overall = all([functional, anti_hardcode, pytest_passed, schema_valid, workflow_compliant])
    result = {
        "run_id": run["run_id"],
        "issue_id": run["issue_id"],
        "mode": run["mode"],
        "functional_correctness": functional,
        "anti_hardcode_passed": anti_hardcode,
        "pytest_passed": pytest_passed,
        "schema_valid": schema_valid,
        "workflow_compliant": workflow_compliant,
        "recovery_success": run.get("recovery_success"),
        "overall_score": 1.0 if overall else 0.0,
    }
    EVAL_DIR.mkdir(parents=True, exist_ok=True)
    (EVAL_DIR / f"{run['run_id']}.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
    return result
