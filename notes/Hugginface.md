# Hugging Face — Primer

## What it is

Hugging Face is an ecosystem for finding, running, and fine-tuning ML models — think of it as "the Hub" (a GitHub-like repository of models/datasets/apps) plus a set of Python libraries that make using that content easy.

## Core pieces

**The Hub** hosts three things:
- **Models** — pretrained weights, filterable by task/framework/license
- **Datasets** — shared, versioned data, loadable with one line of code
- **Spaces** — live demo apps (usually Gradio/Streamlit) to try a model in-browser

**The libraries** are what you import in Python:
- `transformers` — download a model from the Hub and run inference or fine-tune it
- `datasets` — load/stream/process datasets without manual downloads
- `tokenizers` — fast text-to-token conversion (used under the hood by `transformers`)
- `accelerate` / `PEFT` — scale training across GPUs; fine-tune large models cheaply (e.g. LoRA)

**Deployment:**
- **Inference Endpoints** — Hugging Face hosts your model behind an API (paid)
- **Spaces deployment** — you host a small interactive app yourself (free tier available)

## How this fits into this repo

Hugging Face is a **different layer** than the Anthropic API-based agent work this repo is centered on:

| | Anthropic API | Hugging Face |
|---|---|---|
| What you get | One strong model, via API | Thousands of open models, run yourself |
| Main use here | The "brain" for agents (tool use, reasoning loop) | Local/open-source models, embeddings, fine-tuning, evals |
| Where it runs | Anthropic's servers | Your machine / Spaces / Inference Endpoints |

They're complementary, not competing. The agent-building path (Phases 1–7 in `notes/roadmap.md`) doesn't require Hugging Face at all — but it becomes useful once agents are working and you want to extend them.

## Concrete places Hugging Face could show up later in this repo

- **`tools/`** — a tool that uses a small local Hugging Face model (e.g. a local embedding model for search, a local classifier) instead of calling an external API for a specific task
- **`agents/`** — an agent variant that swaps the Anthropic model for an open-source model pulled from the Hub, to compare behavior/cost/latency
- **`evals/`** — using Hugging Face `datasets` to pull a benchmark dataset to test agent or tool accuracy against
- **`notebooks/`** — quick experiments: load a small model with `transformers`, run inference, see how it behaves, before deciding if it's worth wiring into a real agent/tool

## Suggested first hands-on exercise (not yet done)

Pull a small model with `transformers` and run inference locally, e.g. a sentiment classifier or a small text-generation model, just to get a feel for the library — no agent involved yet.

## Status

📝 Primer only — no Hugging Face code in this repo yet. This is background knowledge for when/if a future agent or tool needs a local/open-source model.