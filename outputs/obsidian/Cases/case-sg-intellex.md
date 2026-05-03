---
type: "global_case"
id: "case-sg-intellex"
country_origin: "Singapore"
sector: "Justice & Rule of Law"
year_initiated: 2017
uz_transferability_score: 7
kg_transferability_score: 6
verification: "L2_VERIFIED"
---

# Singapore INTELLLEX Legal AI / SAL Ventures

**Origin**: Singapore  •  **Year**: 2017  •  **Sector**: Justice & Rule of Law

## Problem solved

Singapore lawyers and legal aid workers faced the task of manually searching 500,000+ Singapore court decisions plus Commonwealth case law for relevant precedents. Legal research was a significant cost barrier for smaller firms and for the State Courts (community justice). The Singapore Academy of Law (SAL) funded development of AI-assisted legal research tools to democratise access to case law.

## Architecture

INTELLLEX platform: semantic search over Singapore Law Watch case database plus Commonwealth Legal Information Institute data. NLP pipeline: case classification (by area of law), legal proposition extraction, citation network analysis. Judgement summaries auto-generated using extractive + abstractive summarisation. Integration with Singapore Statutes Online. Later expanded to include LawNet (SAL's official legal database). Cloud-hosted (AWS Singapore Region). Annual subscription model for law firms; subsidised access for legal aid bureaus.

## UZ transferability (7/10)

UZ has a digitised court decision database (sud.uz) and the mandate for AI in courts (УП-140). INTELLLEX architecture — semantic search + case summarisation — is the Phase 1 tool that can be built on UZ court decisions corpus. Russian-language NLP capability exists (Yandex, Sber). Key adaptation: Uzbek legal system is Russian-language + Uzbek procedural code. Cost: $1-3M initial tool is affordable. Legal aid application (free access for low-income citizens) is politically valuable.

## KG transferability (6/10)

KG has court decisions database (cbd.minjust.gov.kg publishes legal acts; court decisions less systematically published). Phase 1 for KG: improve publication completeness of court decisions, then build search tool. Russian-language NLP applies. Legal aid application especially relevant given KG's limited legal aid infrastructure. Cost: $1-2M including corpus digitisation.
