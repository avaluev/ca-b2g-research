---
type: "global_case"
id: "case-ru-gosuslugi-chatbot"
country_origin: "Russia"
sector: "Cross-cutting"
year_initiated: 2019
uz_transferability_score: 7
kg_transferability_score: 7
verification: "VERIFIED"
---

# Russia Gosuslugi AI Chatbot and Voice Bot

**Origin**: Russia  •  **Year**: 2019  •  **Sector**: Cross-cutting

## Problem solved

Russia's Gosuslugi portal received 150M+ support queries/year overwhelming 20,000+ operators. An AI chatbot + voice bot (IVR) was needed to automate routine queries (service status, document requirements, account issues) and reduce human agent load while maintaining Russian-language quality.

## Architecture

Mintsifry chatbot platform: NLP model (Sber AI FRED-T5 base + fine-tuning on Gosuslugi query corpus), 3-channel deployment (web chat, mobile chat, telephone IVR). Integration with Gosuslugi backend: chatbot can query real-time service status, document requirements, and account information via API. ESIA authentication for personalised responses. Voice bot: ASR (Yandex SpeechKit) + TTS (Yandex TTS) for telephone channel. Fallback: seamless escalation to human agent with conversation context passed.

## UZ transferability (7/10)

Russian-language chatbot for EPIGU is immediately deployable using Sber AI or Yandex models (if geopolitical risk acceptable) or open-source alternatives (mGPT, ruBERT). The architecture pattern — NLU + intent detection + EPIGU API queries + fallback to human — is standard. Key: UZ needs Uzbek-language extension alongside Russian. Budget: $2-4M for UZ EPIGU chatbot deploying Bürokratt or this architecture. NOTE: Yandex/Sber dependency creates political risk for EU/World Bank co-funded projects.

## KG transferability (7/10)

KG Tunduk citizen-facing chatbot in Russian + Kyrgyz. Sber AI/Yandex components acceptable for Russian layer if KG political risk assessment permits. Open-source alternative (multilingual BERT, mT5) recommended to avoid Russian vendor dependency. Budget: $1.5-3M for KG Tunduk chatbot.
