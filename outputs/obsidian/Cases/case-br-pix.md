---
type: "global_case"
id: "case-br-pix"
country_origin: "Brazil"
sector: "Finance & Fiscal"
year_initiated: 2020
uz_transferability_score: 8
kg_transferability_score: 8
verification: "VERIFIED"
---

# Brazil Pix Instant Payment System

**Origin**: Brazil  •  **Year**: 2020  •  **Sector**: Finance & Fiscal

## Problem solved

Brazil's payment system was oligopolistic — Mastercard and Visa controlled 80%+ of card payments with high merchant fees (2-3%). Bank transfers (TED/DOC) were expensive ($2-5 per transaction) and had limited hours. Pix created a 24/7/365 instant payment system operated by Brazil's central bank (BCB) with zero consumer fees and capped merchant fees, breaking the card duopoly.

## Architecture

BCB (Banco Central do Brasil) operated Pix switch: real-time clearing for transactions under BRL 200k. Payment key types: CPF (national ID), CNPJ (business ID), phone number, email, random key. Any bank or fintech with BCB licence mandated to offer Pix. QR code standard (static + dynamic) for merchant payments. Schedule: created November 2020, grew to largest instant payment system in Western Hemisphere by 2022. Anti-fraud: central fraud score for each transaction, MED (special mechanism for return) for fraud recovery. Integration: BCB publishes open API standard; 700+ institutions connected.

## UZ transferability (8/10)

UZ Central Bank operated instant payment layer — Pix architecture is directly applicable. The central design decision (central bank operates the switch, all licensed institutions MUST connect) is the political economy challenge in UZ where state-owned banks have legacy payment infrastructure interests. Key: UZ CBU should study Pix's mandatory participation rule. Budget: $10-20M for UZ instant payment switch. World Bank financial sector TA is available.

## KG transferability (8/10)

KG digital som (CBDC) design should incorporate Pix-equivalent instant payment rails from inception. NBKR can use Pix architecture for the interoperability layer between digital som wallets and existing bank accounts. Brazil has 200M population vs KG 6.5M — but the payment switch architecture scales down cleanly. Budget: $5-10M. IMF technical assistance to NBKR is available for CBDC design.
