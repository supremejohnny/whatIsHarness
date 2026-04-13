# Harness Demo

A tiny public repo that makes harness engineering visible.

This repo shows the difference between:
- a baseline agent that tries to fix a bug with minimal structure
- a harnessed agent that follows a controlled workflow with tracing, evals, retries, and output contracts

## What this repo demonstrates

The goal is not to show that an agent can fix a tiny bug.
The goal is to show that reliability comes from the harness around the agent.

You will see:
- how baseline runs can look correct but still be weak
- how harness runs become inspectable, repeatable, and easier to trust
- how traces show what happened
- how evals show whether the run should be trusted

## Demo issues

This repo includes three demo issues:
1. basic bug fix
2. anti-hardcode bug fix
3. bug fix with test + schema + workflow requirements

## Repo modes

### baseline
Free-form execution with minimal constraints.

### harness
Controlled execution with:
- workflow states
- local tracing
- local evals
- output schema
- retry rules
- workflow validation

## Do I need external tools?

### To inspect the demo only
No external tools are required.

### To run local tests and replay sample runs
You need:
- Git
- Python 3.11+
- pytest

### To run the OpenAI-enhanced version
You need:
- OPENAI_API_KEY
- openai
- openai-agents

### Optional
If you want Codex CLI to help maintain this repo locally, install Codex CLI and sign in with ChatGPT or an API key.

## v1 intentionally does **not** require
- Docker
- a database
- Slack API
- browser automation
- Langfuse / LangSmith

## Quickstart

### 1. Clone the repo
```bash
git clone <your-repo-url>
cd harness-demo
```

### 2. Create a virtual environment

macOS/Linux:
```bash
python -m venv .venv
source .venv/bin/activate
```

Windows PowerShell:
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Windows CMD:
```bat
python -m venv .venv
.\.venv\Scripts\activate.bat
```

### 3. Install dependencies

```bash
pip install -e .[dev]
```

If editable install fails with a setuptools package discovery error, ensure you are using the latest `pyproject.toml` in this repo (it explicitly includes only `app` and `harness_demo` packages).

### 4. Run tests

```bash
pytest
```

### 5. Run the baseline demo

```bash
python scripts/run_baseline.py --issue issues/fixtures/001_basic_bug.md
```

### 6. Run the harness demo

```bash
python scripts/run_harness.py --issue issues/fixtures/001_basic_bug.md
```

### 7. Compare the runs

```bash
python scripts/compare_runs.py --latest
```

## What gets generated

Each run writes artifacts to:

- `artifacts/traces/`
- `artifacts/evals/`
- `artifacts/runs/`
- `artifacts/comparisons/`

## OpenAI-enhanced mode (optional)

When enabled, the harness runner can use OpenAI as an execution engine while still writing local artifacts.

```bash
export OPENAI_API_KEY=your_key_here
pip install -e .[openai]
python scripts/run_harness.py --issue issues/fixtures/001_basic_bug.md --engine openai
```

## Roadmap

See `docs/roadmap.md`.

## License

MIT
