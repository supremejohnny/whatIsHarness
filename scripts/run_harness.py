#!/usr/bin/env python
import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from harness_demo.runner import execute


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--issue", required=True)
    parser.add_argument("--engine", default="local")
    args = parser.parse_args()
    run = execute(mode="harness", issue=args.issue, engine=args.engine)
    print(json.dumps(run, indent=2))


if __name__ == "__main__":
    main()
