# Accuracy Notes — Falcon-7B-Instruct (MLX, 4-bit)

This document records basic accuracy observations for **Falcon-7B-Instruct** running locally using the MLX framework with 4-bit quantization.

All responses were generated using a **maximum token limit of 80** to intentionally constrain verbosity and observe how the model behaves under tight generation limits.

---

## Evaluation Setup

- **Model:** Falcon-7B-Instruct (4-bit, MLX)
- **Inference Device:** CPU (Apple Silicon)
- **Max New Tokens:** 80
- **Sampling:** Enabled (temperature ≈ 0.7)
- **Prompt Style:** Direct, single-turn factual questions
- **No external tools or retrieval used**

---

## Accuracy Summary

- Total questions evaluated: 8  
- Correct answers: 5  
- Partially correct answers: 1  
- Incorrect or hallucinated answers: 2  

- **Strict accuracy:** ~62.5%  
- **Lenient accuracy (including partial answers):** ~75%

---

## Observed Strengths

- Performs well on:
  - Basic mathematics and numerical reasoning
  - Scientific definitions (physics, biology)
  - Logical sequence completion
- Responses are generally coherent and well-structured even at low token limits

---

## Observed Failure Modes

- **Named-entity confusion:**  
  Pop-culture and fictional character questions often resulted in incorrect associations or mixed entities.
  
- **Hallucinated extensions:**  
  Even when the core answer was correct, the model sometimes fabricated additional factual details.

- **Task drift under constraint:**  
  With a max token limit of 80, some responses appeared truncated or prematurely diverted, impacting factual completeness.

---

## Why Inaccuracies Could Have Occurred

The observed inaccuracies can likely be attributed to:

- **Small model size (7B parameters):**  
  Limited factual recall compared to larger models.

- **Aggressive token limitation:**  
  Tight token budgets reduce the model’s ability to self-correct or qualify answers.

- **Quantization effects (4-bit):**  
  While memory-efficient, quantization can slightly degrade factual precision.

- **No retrieval or grounding:**  
  The model relies purely on internal weights without external verification.

---

## Conclusion

Falcon-7B-Instruct demonstrates solid reasoning and scientific understanding for a locally deployed 7B model, but shows clear limitations in factual recall and named-entity accuracy—especially under constrained token generation.

These results are expected for a lightweight, fully offline inference setup and provide a useful baseline for future experimentation.

---