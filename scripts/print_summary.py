#!/usr/bin/env python
import json
from pathlib import Path

for f in sorted(Path("artifacts/comparisons").glob("*.json")):
    data = json.loads(f.read_text(encoding="utf-8"))
    print(f"{f.name}: {data['conclusion']}")
