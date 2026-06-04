# Metaphor Analysis Research Harness

This folder contains a small working example of a humanities research harness.

The harness operationalizes a metaphor-analysis method.

It contains:

```text
research_policy.md
allowed_sources.md
guides/
prompts/
tools/
test_texts/
outputs/
scores.csv
harness_report_template.md
```

## How to Run the Example

1. Read `research_policy.md`.
2. Read `allowed_sources.md`.
3. Read the guides in `guides/`.
4. Open a test text in `test_texts/`.
5. Use `prompts/analyst_prompt.md` to generate an annotation.
6. Save the annotation as a JSON file in `outputs/`.
7. Run:

```bash
python tools/check_output_structure.py
```

8. Fill in `scores.csv`.
9. Complete `harness_report_template.md`.

## What This Demonstrates

The model does not operate alone.

The harness defines:

```text
allowed sources
method rules
output schema
evaluation criteria
review requirements
archive structure
```
