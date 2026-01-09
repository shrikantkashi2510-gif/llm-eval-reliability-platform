# Evaluation Framework

This folder contains the core evaluation logic for detecting
LLM regressions, hallucinations, and reliability issues.

## Design Principles
- Deterministic where possible
- Cheap to run frequently
- Focused on real production failures
- Model-agnostic

## Structure
- `datasets/` → Golden evaluation inputs
- `metrics/` → Individual scoring functions
- `runners/` → Evaluation orchestration
- `reports/` → Machine-readable results
