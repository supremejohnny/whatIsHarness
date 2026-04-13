# Repository working rules

## Goal
This repository demonstrates harness engineering by comparing baseline and harnessed agent runs.

## Code style
- prefer simple, readable Python
- keep files small
- avoid unnecessary abstractions
- favor explicit state transitions over magic behavior

## Demo contract
- keep the app intentionally tiny
- the educational value is in the harness, not in app complexity
- preserve side-by-side comparability between baseline and harness modes

## Required outputs
- local trace artifacts
- local eval artifacts
- run summaries
- comparison summaries

## Do not
- do not add Docker in v1
- do not add databases in v1
- do not add external observability vendors in v1
- do not hide workflow behavior behind opaque wrappers

## Success criteria
- users can run baseline and harness locally
- users can compare results from artifacts
- README explains every step clearly
