import json
from datetime import datetime, timezone
from pathlib import Path

from harness_demo.config import TRACE_DIR


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def write_trace(trace: dict) -> Path:
    TRACE_DIR.mkdir(parents=True, exist_ok=True)
    path = TRACE_DIR / f"{trace['run_id']}.json"
    path.write_text(json.dumps(trace, indent=2), encoding="utf-8")
    index_path = TRACE_DIR / "index.jsonl"
    with index_path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(trace) + "\n")
    return path
