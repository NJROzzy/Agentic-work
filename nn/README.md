# nn/

This folder is a **from-scratch neural networks** learning track — plain Python, no frameworks (no PyTorch/TensorFlow) — built to understand what's actually happening under the hood before ever relying on a library to do it.

This is a separate track from the agentic AI work in `agents/`, `tools/`, etc. — a complementary skill, not a replacement.

## Why from scratch

Frameworks like PyTorch are great once you understand what they're abstracting away. Building a neural net by hand first — the math, the forward pass, the backward pass — makes everything you do later in a framework make sense instead of feeling like magic.

## Planned progression

- [ ] A single neuron (weights, bias, activation function)
- [ ] A single layer of neurons (forward pass)
- [ ] Loss function (measuring how wrong the output is)
- [ ] Backpropagation (how the network learns — gradients, updating weights)
- [ ] A minimal multi-layer network trained on a toy problem (e.g. XOR)
- [ ] (Optional, later) Comparing the from-scratch version to the same thing in PyTorch, to see the abstraction

## Suggested layout

```
nn/
├── README.md
├── 01_single_neuron.py
├── 02_forward_pass.py
├── 03_loss_function.py
├── 04_backpropagation.py
└── 05_train_xor.py
```

## Guidelines

- Each file builds on the previous one — don't skip ahead
- Prefer clarity over cleverness — no need for optimized/vectorized code yet; readable loops are fine at this stage
- Comment the *why*, not just the *what* — especially for the math

## Status

🚧 Just started. First file: a single neuron.