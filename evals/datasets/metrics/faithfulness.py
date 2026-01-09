def faithfulness_score(response: str) -> float:
    """
    Simple heuristic for faithfulness.
    Replace with stronger methods later.
    """
    risky_terms = ["hallucinate", "fabricate", "unknown"]
    hits = sum(1 for term in risky_terms if term in response.lower())
    return round(min(1.0, hits / 3), 2)
