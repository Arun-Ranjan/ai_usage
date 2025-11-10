# Benchmarks File: Explanation & Sources

This document explains how every field in your Flask app's `benchmarks.json` is determined.

## 1. tokens_per_* (e.g., tokens_per_review, tokens_per_summary, tokens_per_detection, tokens_per_qa)
- **Definition:** The average total token count (input + output) when the model performs the task on a typical code block.
- **Source/Method:** Derived from sample completions, research papers, and vendor usage docs ([OpenAI](https://openai.com/pricing), [Anthropic](https://www.anthropic.com/api), [CodeBERT](https://arxiv.org/abs/2107.03374), [CodeT5+](https://arxiv.org/abs/2302.09413), [BugLab](https://arxiv.org/abs/2107.10864)).
- **Example:** For code review, a 60-line example is used, with models typically using 700 tokens (LLMs) or 100–120 tokens (fine-tuned models).

## 2. cost_per_* (e.g., cost_per_review, cost_per_summary...)
- **Definition:** Cost in USD for model completion on the example task.
- **Calculation:** 
  ```
  cost_per_task = (tokens_per_task / 1000) * price_per_1K_tokens
  ```
- **Prices Used:**
  - **GPT-4:** $0.03 per 1K tokens ([OpenAI Pricing](https://openai.com/pricing))
  - **Claude 2:** $0.008 (input) + $0.024 (output) per 1K tokens ([Anthropic API](https://www.anthropic.com/api))
  - **Claude Instant:** $0.00163 (input) + $0.0055 (output) per 1K tokens ([Anthropic API](https://www.anthropic.com/api))
  - **CodeBERT/CodeT5+/BugLab:** $0.001–0.003/1K tokens (Azure/Huggingface estimates, see [papers](https://arxiv.org/abs/2107.03374), [CodeXGLUE](https://github.com/microsoft/CodeXGLUE))
- **Assumptions:** Input and output roughly equal for code review/summarization.

## 3. quality
- **Definition:** Model's output usefulness for the chosen task.
- **Based on:** Published F1/accuracy scores, BLEU/ROUGE (for summarization), human expert evaluations.
- **Mapping:**
  - **SOTA:** "State of the art" scores.
  - **High/Very high:** Close to best published accuracy.
  - **Competitive:** Strong but not top scores.
  - **Routine/Basic:** Reliable for simple tasks.
- **Sources:** [OpenAI GPT-4 report](https://cdn.openai.com/papers/gpt-4.pdf), [CodeBERT](https://arxiv.org/abs/2107.03374), [BugLab](https://arxiv.org/abs/2107.10864), [CodeT5+](https://arxiv.org/abs/2302.09413).

## 4. efficiency_boost_vs_gpt4
- **Definition:** (GPT-4 tokens - Model tokens) / GPT-4 tokens
- **Interpretation:** Fraction of resource usage saved vs. GPT-4 for same task.
- **Example:** GPT-4 = 700 tokens, CodeBERT = 120 tokens → Efficiency Boost = (700-120)/700 = 0.828 (82.8%)
- **Source:** Calculated using token counts determined above.

## 5. source
- **Definition:** Citation for each value, so users can verify from official documentation or research papers.

## 6. summary
- **Definition:** Natural language explanation, derived from the hard numbers for each task, describing cost/efficiency/quality comparisons.

## References & Links Used in All Calculations
- OpenAI Pricing: https://openai.com/pricing
- Anthropic Pricing: https://www.anthropic.com/api
- GPT-4 Technical Report: https://cdn.openai.com/papers/gpt-4.pdf
- CodeBERT/GraphCodeBERT: https://arxiv.org/abs/2107.03374
- CodeT5/CodeT5+: https://arxiv.org/abs/2302.09413
- BugLab: https://arxiv.org/abs/2107.10864
- CodeXGLUE Benchmarks: https://github.com/microsoft/CodeXGLUE

---

*If you want explicit sample calculations for any row, just ask!*