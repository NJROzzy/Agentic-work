# tools/

This folder holds **reusable tool/function definitions** that agents can call — the "hands" of the agents living in `agents/`.

A "tool" here means:
1. A plain Python function that does something real (fetch weather, do math, read a file, hit an API, etc.)
2. A matching tool **schema/definition** describing that function to the model (name, description, input parameters) so it can be passed to the Anthropic API's `tools` parameter.

## Suggested layout

```
tools/
├── weather.py       # get_weather() + its tool schema
├── calculator.py    # calculate() + its tool schema
└── __init__.py
```

## Guidelines

- One tool (or a small tightly-related group) per file
- Keep tool functions pure/simple where possible — easier to test and reason about
- Tool schemas should stay next to the function they describe, so they never drift out of sync
- Tools should be **imported into agents**, not duplicated inside agent code

## Current status

🚧 Empty — first tool (likely a simple weather or calculator function) coming alongside the Phase 3 single-tool agent.
