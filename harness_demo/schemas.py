from dataclasses import asdict, dataclass


@dataclass
class RunResult:
    issue_id: str
    mode: str
    root_cause: str
    files_read: list[str]
    files_changed: list[str]
    tests_passed: bool
    retry_count: int
    status: str
    summary: str

    def model_dump(self) -> dict:
        return asdict(self)
