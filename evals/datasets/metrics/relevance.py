def relevance_score(response: str, expected: str) -> float:
    response_tokens = set(response.lower().split())
    expected_tokens = set(expected.lower().split())
    overlap = response_tokens.intersection(expected_tokens)
    return round(min(1.0, len(overlap) / 10), 2)
