# Falcon-7B Instruct: Local Model Reproduction

This repository contains a successful local reproduction of the **Falcon-7B-Instruct** model, optimized for efficient inference using the **MLX** framework. 

## Objective
The goal was to reproduce the inference capabilities of a 7-billion parameter model in a local, resource-constrained environment. By leveraging 4-bit quantization and the Metal-optimized MLX framework, this implementation achieves real-time text generation without external API dependencies.

## Model Source & Lineage
- **Base Model:** [tiiuae/falcon-7b-instruct](https://huggingface.co/tiiuae/falcon-7b-instruct)
- **Developer:** Technology Innovation Institute (TII)
- **Architecture:** Causal decoder-only transformer featuring:
  - **Multi-Query Attention:** Shared keys and values across heads to minimize memory bandwidth.
  - **RefinedWeb Training:** Built on 1,500B tokens of high-quality web data.
  - **Rotary Positional Embeddings (RoPE):** For enhanced long-range context handling.

## Reproduction Benchmarks
The implementation was validated with the following metrics:
- **Quantization:** 4-bit weight compression.
- **Generation Speed:** ~6.25 tokens per second.
- **Prompt Processing:** ~4.65 tokens per second.
- **Memory Efficiency:** Peak active RAM usage stayed under 5GB, demonstrating high stability for local deployment.

## Setup & Execution

 **Environment Initialization:**
   ```bash
   python3 -m venv falcon7b
   source falcon7b/bin/activate
   pip install mlx-lm psutil