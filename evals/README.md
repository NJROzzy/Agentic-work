# evals/

This folder holds **evaluation and test scripts** for agent behavior — how do you know an agent is actually working, not just "seems fine"?

## What goes here

- Simple test cases: given input X, does the agent take the right action / call the right tool / reach the right answer?
- Scripts that run an agent against a set of known scenarios and report pass/fail
- Notes on observed failure modes and edge cases

## Suggested layout

```
evals/
├── single_tool_agent_evals.py
├── cases/
│   └── weather_cases.json    # example inputs + expected behavior
└── results/                    # optional: logged outputs over time
```

## Guidelines

- Keep eval cases simple and readable — plain input/expected-output pairs where possible
- Prefer many small cases over one big complex one
- Re-run evals whenever an agent or its tools change, to catch regressions

## Current status

🚧 Empty — evals will start once the first agent (Phase 3) exists to test against.
