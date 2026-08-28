# agents/

This folder holds actual agent implementations — the working code, not just experiments.

Each agent gets its **own subfolder**, e.g.:

```
agents/
├── single_tool_agent/
│   ├── README.md
│   ├── agent.py
│   └── ...
├── multi_tool_agent/
└── stateful_agent/
```

## Guidelines for each agent subfolder

- A short `README.md` explaining:
  - What the agent does
  - What tool(s) it uses
  - How to run it
  - Any known limitations
- A clear entry point (e.g. `agent.py` or `run.py`)
- Keep agent logic separate from tool definitions — tools live in `tools/` and get imported in here, not redefined.

## Current status

🚧 Empty — first agent (single-tool, Anthropic API) coming in Phase 3 of the learning plan.
