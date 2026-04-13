#!/usr/bin/env python
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from harness_demo.runner import execute


if __name__ == "__main__":
    issue = "issues/fixtures/001_basic_bug.md"
    execute("baseline", issue)
    execute("harness", issue)
