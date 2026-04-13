from harness_demo.state import WorkflowState


VALID_TRANSITIONS = {
    WorkflowState.ISSUE_LOADED: {WorkflowState.PLAN_CREATED},
    WorkflowState.PLAN_CREATED: {WorkflowState.FILES_READ},
    WorkflowState.FILES_READ: {WorkflowState.PATCH_APPLIED},
    WorkflowState.PATCH_APPLIED: {WorkflowState.TESTS_RUN},
    WorkflowState.TESTS_RUN: {WorkflowState.EVALS_RUN, WorkflowState.RETRY, WorkflowState.FAILED},
    WorkflowState.EVALS_RUN: {WorkflowState.SUCCESS, WorkflowState.RETRY, WorkflowState.FAILED},
    WorkflowState.RETRY: {WorkflowState.PLAN_CREATED, WorkflowState.FAILED},
}


def is_transition_allowed(from_state: str, to_state: str) -> bool:
    try:
        start = WorkflowState(from_state)
        end = WorkflowState(to_state)
    except ValueError:
        return False
    return end in VALID_TRANSITIONS.get(start, set())
