# INI-006 — Objection Handling

## Objection 1: "The AI Center team will train the model themselves"
**Response:** "The long-term goal should absolutely be an AI Center team that trains and maintains the sovereign LLM independently. We propose a methodology transfer model: we deliver the 7B base model and training pipeline in Year 1, co-publish with NUU, and transfer the entire training codebase to the AI Center team. From Year 2, the AI Center owns the model. UAE TII did not outsource Falcon forever — they built the team through the first training cycle."

## Objection 2: "Why not use GPT-4 or Gemini?"
**Response:** "State use cases — courts, tax authority, health system — require that citizen data never leaves the sovereign boundary. GPT-4 and Gemini are foreign APIs with servers outside Uzbekistan. УП-2025-189 explicitly mandates sovereign AI capability. The sovereign LLM runs entirely on UzCloud; no query from a court or clinic ever reaches a foreign server."

## Objection 3: "Training data quality is poor for Uzbek"
**Response:** "Uzbek corpus quality is the core technical challenge — and our approach addresses it specifically. We start with a Russian-foundation model (large, high-quality corpus) and apply Uzbek instruction tuning on a curated subset. NUU AI Cluster co-curates the Uzbek corpus with us, providing academic standards for quality filtering. The benchmark we co-publish documents exactly what Uzbek coverage we have achieved and on which tasks — honest, independently verifiable."

## Objection 4: "GPU hardware export controls make this risky"
**Response:** "We have designed for this from the start. Phase 1 uses a hybrid architecture: NVIDIA H100-class GPUs for training where available, with a Huawei Ascend fallback track designed in from Day 1. The model weights, once trained, run efficiently on inference hardware that is export-control-clean. We are not dependent on a single hardware vendor."

## Objection 5: "What happens if the model is biased or generates inappropriate content?"
**Response:** "We include three mitigation layers: (1) instruction tuning with explicit government-domain content policy; (2) output filtering layer before API delivery; (3) an AI ethics evaluation framework co-authored with MIT Media Lab (Bobur Yakubov) and NUU, covering bias testing in Uzbek and Russian contexts. The bias evaluation protocol is published openly — the AI Center and MoDT can run it themselves."
