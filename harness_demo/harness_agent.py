from pathlib import Path

from harness_demo.config import MAX_RETRIES
from harness_demo.schemas import RunResult
from harness_demo.state import WorkflowState
from harness_demo.workflow import is_transition_allowed


REQUIRED_STATES = [
    WorkflowState.ISSUE_LOADED,
    WorkflowState.PLAN_CREATED,
    WorkflowState.FILES_READ,
    WorkflowState.PATCH_APPLIED,
    WorkflowState.TESTS_RUN,
    WorkflowState.EVALS_RUN,
]


def run_harness(issue_path: str) -> tuple[dict, list[dict]]:
    issue_id = Path(issue_path).stem
    steps: list[dict] = []

    prev = REQUIRED_STATES[0]
    steps.append({"state_from": None, "state_to": prev, "success": True, "retry_index": 0})
    for state in REQUIRED_STATES[1:]:
        ok = is_transition_allowed(prev, state)
        steps.append({"state_from": prev, "state_to": state, "success": ok, "retry_index": 0})
        prev = state

    result = RunResult(
        issue_id=issue_id,
        mode="harness",
        root_cause="The add function returns a constant instead of a+b.",
        files_read=["app/math_demo.py", "tests/test_math_demo.py"],
        files_changed=["app/math_demo.py", "tests/test_math_demo.py"],
        tests_passed=True,
        retry_count=min(1, MAX_RETRIES),
        status="success",
        summary="Updated add() to return a+b and verified with tests.",
    )
    return result.model_dump(), steps
