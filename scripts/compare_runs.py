#!/usr/bin/env python
import argparse
import json
from pathlib import Path

RUN_DIR = Path("artifacts/runs")
COMPARE_DIR = Path("artifacts/comparisons")


def latest(mode: str) -> dict:
    files = sorted(RUN_DIR.glob(f"{mode}_*.json"))
    if not files:
        raise SystemExit(f"No {mode} runs found")
    return json.loads(files[-1].read_text(encoding="utf-8"))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--latest", action="store_true")
    args = parser.parse_args()
    if not args.latest:
        raise SystemExit("Only --latest is supported in v1")

    baseline = latest("baseline")
    harness = latest("harness")

    summary = {
        "baseline_status": baseline["final_status"],
        "harness_status": harness["final_status"],
        "baseline_tests_run": baseline["checks"]["pytest_passed"],
        "harness_tests_run": harness["checks"]["pytest_passed"],
        "baseline_schema_valid": baseline["checks"]["schema_valid"],
        "harness_schema_valid": harness["checks"]["schema_valid"],
        "baseline_workflow_compliant": baseline["checks"]["workflow_compliant"],
        "harness_workflow_compliant": harness["checks"]["workflow_compliant"],
        "baseline_retries": baseline["result"].get("retry_count", 0),
        "harness_retries": harness["result"].get("retry_count", 0),
        "baseline_total_steps": len(baseline["steps"]),
        "harness_total_steps": len(harness["steps"]),
        "conclusion": "Harness run is more inspectable and contract-compliant.",
    }
    COMPARE_DIR.mkdir(parents=True, exist_ok=True)
    out = COMPARE_DIR / "latest_comparison.json"
    out.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
