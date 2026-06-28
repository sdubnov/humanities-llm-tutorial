#!/usr/bin/env python3
"""Run a simple vibe-matrix analysis for the Postmodern Vibe Agentic Matrixing project.

Usage:
    python run_analysis.py
    python run_analysis.py sample_matrix.csv
    python run_analysis.py path/to/your_matrix.csv --output report.txt

This script is intentionally simple. It is designed for humanities students who are
learning how interpretive matrices can be made explicit and debatable.
"""

from __future__ import annotations

import argparse
import csv
from pathlib import Path
from statistics import mean
from typing import Dict, Iterable, List

REQUIRED_SCORE_FIELDS = [
    "ontological_multiplicity",
    "paranoia_affective_density",
    "media_structural_friction",
]


def to_int(value: str, field: str, title: str) -> int:
    try:
        score = int(value)
    except (TypeError, ValueError):
        raise ValueError(f"Invalid score for {title!r} in field {field!r}: {value!r}")
    if score < 1 or score > 10:
        raise ValueError(f"Score out of range for {title!r} in field {field!r}: {score}")
    return score


def load_matrix(path: Path) -> List[Dict[str, str]]:
    if not path.exists():
        raise FileNotFoundError(f"Could not find matrix file: {path}")
    with path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    if not rows:
        raise ValueError("The matrix is empty.")
    missing = [field for field in REQUIRED_SCORE_FIELDS if field not in reader.fieldnames]
    if missing:
        raise ValueError(f"Missing required score fields: {', '.join(missing)}")
    return rows


def assign_cluster(scores: Dict[str, int]) -> str:
    ontology = scores["ontological_multiplicity"]
    affect = scores["paranoia_affective_density"]
    media = scores["media_structural_friction"]

    if media >= 8 and ontology >= 7:
        return "Ergodic / Media Monsters"
    if affect >= 8 and ontology <= 5:
        return "Paranoid Realists"
    if ontology >= 8 and media <= 6:
        return "Chrono-Fractured Empaths"
    if affect >= 8 and media >= 8:
        return "Overload Systems"
    return "Hybrid / Unsettled Postmodern Form"


def build_report(rows: Iterable[Dict[str, str]]) -> str:
    rows = list(rows)
    report: List[str] = []
    report.append("POSTMODERN VIBE AGENTIC MATRIX REPORT")
    report.append("=" * 44)
    report.append("")

    all_scores = {field: [] for field in REQUIRED_SCORE_FIELDS}

    for row in rows:
        title = row.get("title", "Untitled")
        author = row.get("author", "Unknown")
        scores = {
            field: to_int(row.get(field, ""), field, title)
            for field in REQUIRED_SCORE_FIELDS
        }
        for field, value in scores.items():
            all_scores[field].append(value)

        cluster = assign_cluster(scores)
        report.append(f"{title} — {author}")
        report.append("-" * (len(title) + len(author) + 3))
        report.append(f"Ontological multiplicity:     {scores['ontological_multiplicity']}/10")
        report.append(f"Paranoia / affective density: {scores['paranoia_affective_density']}/10")
        report.append(f"Media / structural friction:  {scores['media_structural_friction']}/10")
        report.append(f"Assigned cluster: {cluster}")
        warning = row.get("reliability_warning", "").strip()
        if warning:
            report.append(f"Reliability warning: {warning}")
        report.append("")

    report.append("CLASS-LEVEL SUMMARY")
    report.append("-" * 19)
    for field, values in all_scores.items():
        report.append(f"Average {field}: {mean(values):.2f}")

    report.append("")
    report.append("REFLECTION PROMPTS")
    report.append("-" * 18)
    report.append("1. Which cluster assignment felt most persuasive, and why?")
    report.append("2. Which score looked falsely precise?")
    report.append("3. Where did the agents rely on reputation rather than evidence?")
    report.append("4. Which agent role would you add, remove, or rewrite?")
    report.append("5. How would the results change if the input were full passages rather than summaries?")

    return "\n".join(report)


def main() -> None:
    parser = argparse.ArgumentParser(description="Run a simple vibe-matrix report.")
    parser.add_argument(
        "matrix",
        nargs="?",
        default="sample_matrix.csv",
        help="Path to a completed CSV matrix. Defaults to sample_matrix.csv.",
    )
    parser.add_argument(
        "--output",
        "-o",
        help="Optional path for saving the report as a text file.",
    )
    args = parser.parse_args()

    matrix_path = Path(args.matrix)
    if not matrix_path.is_absolute():
        matrix_path = Path(__file__).parent / matrix_path

    rows = load_matrix(matrix_path)
    report = build_report(rows)
    print(report)

    if args.output:
        output_path = Path(args.output)
        output_path.write_text(report, encoding="utf-8")
        print(f"\nSaved report to: {output_path}")


if __name__ == "__main__":
    main()
