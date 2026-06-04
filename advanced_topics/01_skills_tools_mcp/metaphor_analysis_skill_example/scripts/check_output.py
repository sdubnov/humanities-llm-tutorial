# scripts/check_output.py

import json
import sys
from pathlib import Path

required_fields = [
    "passage",
    "device",
    "evidence",
    "source_domain",
    "target_domain",
    "interpretation",
    "confidence"
]

def check_output(annotation):
    missing = [
        field for field in required_fields
        if field not in annotation or not annotation[field]
    ]

    return {
        "valid": len(missing) == 0,
        "missing_fields": missing
    }

def main():
    if len(sys.argv) > 1:
        path = Path(sys.argv[1])
        annotation = json.loads(path.read_text(encoding="utf-8"))
    else:
        annotation = {
            "passage": "The city was a broken mirror",
            "device": "metaphor",
            "evidence": "The city was a broken mirror",
            "source_domain": "broken mirror",
            "target_domain": "city",
            "interpretation": "The city is represented as damaged and reflective of lost hopes.",
            "confidence": 5
        }

    result = check_output(annotation)
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
