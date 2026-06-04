# validate_annotations.py

import json
from pathlib import Path

DATA_PATH = Path("model_adaptation_dossier/annotations.jsonl")

REQUIRED_FIELDS = [
    "text_id",
    "passage",
    "device",
    "evidence",
    "source_domain",
    "target_domain",
    "interpretation",
    "confidence",
    "uncertainty_note",
    "review_status"
]

def validate(item):
    missing = [field for field in REQUIRED_FIELDS if not item.get(field)]
    confidence = item.get("confidence")
    confidence_valid = isinstance(confidence, int) and 1 <= confidence <= 5
    return {
        "text_id": item.get("text_id"),
        "missing_fields": missing,
        "confidence_valid": confidence_valid,
        "valid": len(missing) == 0 and confidence_valid
    }

def main():
    if not DATA_PATH.exists():
        print(f"Missing file: {DATA_PATH}")
        return

    rows = []
    for line in DATA_PATH.read_text(encoding="utf-8").splitlines():
        if line.strip():
            rows.append(json.loads(line))

    if not rows:
        print("No annotations found.")
        return

    for row in rows:
        print(json.dumps(validate(row), indent=2))

if __name__ == "__main__":
    main()
