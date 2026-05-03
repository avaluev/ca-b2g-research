# INI-007 — Objection Handling

## Objection 1: "Huawei is our preferred partner — they already operate our govcloud"
**Response:** "Our architecture is designed to integrate with the Huawei govcloud layer, not replace it. We use Huawei Ascend as the fallback/secondary compute tier within the same cluster, enabling the UZ government to have NVIDIA performance for frontier model training and Huawei continuity for existing workloads. No disruption to existing Huawei DSR infrastructure."

## Objection 2: "NVIDIA H100 export controls — can you actually deliver?"
**Response:** "We have mapped four supply-chain paths: (1) direct NVIDIA through authorized Central Asia partner; (2) via GCC tech zone (UAE/KSA, which has NVIDIA export access); (3) Huawei Ascend 910B as primary if H100 clearance delayed; (4) hybrid: start Ascend in Month 1, add H100 when cleared. The INI-006 LLM training timeline is set accordingly — no single-supplier blocking."

## Objection 3: "We want full government ownership of the hardware"
**Response:** "Agreed — we design for full government ownership. We deliver the hardware + orchestration software, transfer all operational documentation, and train the UzCloud team to manage independently. Year 2 onwards the AI Center operates the cluster without vendor dependency. Our ongoing relationship is advisory and upgrade, not lock-in maintenance."

## Objection 4: "NUU co-hosting creates governance conflicts"
**Response:** "Standard multi-tenant SLA: government workloads have priority; NUU academic workloads fill unused capacity. The SLA defines clear preemption rules. This is the same model Singapore PAIR uses for government + research tenant mix. We handle the SLA drafting as part of the pilot phase."
