from pathlib import Path


def run_baseline(issue_path: str) -> dict:
    issue_id = Path(issue_path).stem
    return {
        "mode": "baseline",
        "issue_id": issue_id,
        "summary": "Attempted fix with minimal workflow constraints.",
        "files_read": ["app/math_demo.py", "tests/test_math_demo.py"],
        "files_changed": ["app/math_demo.py"],
    }
