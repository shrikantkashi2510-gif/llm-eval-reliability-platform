# System Architecture

## Overview
This platform evaluates LLM behavior by replaying or sampling prompts,
scoring responses, and detecting regressions before production impact.

## High-Level Flow
1. An application calls an LLM
2. Prompts and responses are sampled or replayed
3. The evaluation runner executes metrics
4. Scores are written to versioned reports
5. Reports are compared across runs to detect regressions

## Core Components
- **Eval Runner**: Orchestrates evaluation runs
- **Metrics Engine**: Computes faithfulness and relevance scores
- **Golden Datasets**: Define expected model behavior
- **Eval Reports**: Machine-readable evaluation outputs

## Design Principles
- Stateless execution
- Model-agnostic design
- Cheap enough to run frequently
- Identical logic in local and hosted modes
