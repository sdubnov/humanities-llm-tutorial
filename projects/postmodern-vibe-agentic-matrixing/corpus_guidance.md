# Corpus Guidance for Postmodern Vibe Agentic Matrixing

## What this file is

`input_corpus.csv` is the missing upstream input for the project. It contains short, copyright-safe instructor paraphrases of five postmodern novels used in the sample matrix.

The intended workflow is:

```text
input_corpus.csv
    ↓
agents_config.json + analysis_prompt.md
    ↓
student or instructor runs LLM agents manually
    ↓
student_matrix.csv or sample_matrix.csv
    ↓
run_analysis.py
    ↓
sample_report.txt or instructor_test_report.txt
```

## Why summaries are included instead of excerpts

The selected novels are modern copyrighted works. For a public GitHub repository, do not include long excerpts from the novels.

Summaries are safe and useful for demonstrating the project workflow, but they bias the agents toward plot, reputation, and known literary categories. They are weaker for style analysis.

## Should students use original text?

Yes, when the learning goal is style-sensitive analysis.

Use summary input when asking:

- What is the book's premise?
- What broad postmodern features are visible?
- How do agents behave when given compressed secondary descriptions?

Use original excerpts when asking:

- How does syntax affect affective scoring?
- How do typography, footnotes, and layout affect media-friction scoring?
- Does the model respond differently to textual surface than to reputation?

## Recommended classroom practice

For the public repo, keep only `input_corpus.csv`.

For a live class, instructors may provide short excerpts through the course LMS, library reserve, or legally accessed student editions. Students can then replace the `input_text` field with a brief passage and compare the matrix scores against the summary-based run.

## Suggested student experiment

Run the same book twice:

1. Once using the summary row from `input_corpus.csv`.
2. Once using a legally accessed short excerpt.

Then answer:

- Which agent changed its score the most?
- Did the excerpt increase or decrease Media/Structural Friction?
- Did the summary cause the model to rely on known reputation?
- Did the excerpt reveal style features absent from the summary?
