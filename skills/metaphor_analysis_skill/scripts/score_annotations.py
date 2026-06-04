"""Simple scoring helper for metaphor analysis annotations."""

def score_annotation(annotation):
    score = 0
    required = ["passage", "device", "evidence", "source_domain", "target_domain", "interpretation", "confidence"]
    for field in required:
        if annotation.get(field):
            score += 1
    return score

if __name__ == "__main__":
    example = {
        "passage": "The city was a broken mirror",
        "device": "metaphor",
        "evidence": "The city was a broken mirror",
        "source_domain": "broken mirror",
        "target_domain": "city",
        "interpretation": "The city is framed as fragmented and reflective.",
        "confidence": 5
    }
    print(score_annotation(example))
