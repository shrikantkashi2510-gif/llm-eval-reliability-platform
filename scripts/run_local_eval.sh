#!/bin/bash

echo "Running local LLM evaluation..."

python evals/runners/run_eval.py

echo "Evaluation finished. Check evals/reports/sample_report.json"
