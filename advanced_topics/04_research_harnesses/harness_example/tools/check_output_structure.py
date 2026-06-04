# check_output_structure.py

import json
from pathlib import Path

OUTPUT_DIR = Path("outputs")

REQUIRED_FIELDS = [
    "text_id",
    "passage",
    "device",
    "evidence",
    "source_domain",
    "target_domain",
    "interpretation",
    "confidence",
    "uncertainty_note"
]

def check_file(path):
    data = json.loads(path.read_text(encoding="utf-8"))
    missing = [
        field for field in REQUIRED_FIELDS
        if field not in data or data[field] in [None, ""]
    ]
    return {
        "file": str(path),
        "valid_structure": len(missing) == 0,
        "missing_fields": missing
    }

def main():
    files = sorted(OUTPUT_DIR.glob("*.json"))

    if not files:
        print("No JSON files found in outputs/.")
        print("Save model outputs as .json files before running this checker.")
        return

    for path in files:
        result = check_file(path)
        print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
