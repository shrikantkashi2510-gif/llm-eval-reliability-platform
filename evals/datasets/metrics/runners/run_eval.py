import json
from evals.metrics.faithfulness import faithfulness_score
from evals.metrics.relevance import relevance_score

DATASET_PATH = "evals/datasets/golden_set.json"
REPORT_PATH = "evals/reports/sample_report.json"

with open(DATASET_PATH) as f:
    dataset = json.load(f)

results = []

for item in dataset:
    # Mock response for now (replace with real LLM call later)
    mock_response = "LLMs may hallucinate and create compliance risks."

    result = {
        "id": item["id"],
        "faithfulness": faithfulness_score(mock_response),
        "relevance": relevance_score(
            mock_response,
            item["expected_behavior"]
        )
    }

    results.append(result)

with open(REPORT_PATH, "w") as f:
    json.dump(results, f, indent=2)

print("Evaluation completed. Report generated.")
