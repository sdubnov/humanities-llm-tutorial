# Instructor Notes

## Recommended use

This project works best after students have already practiced structured prompting, taxonomies, multi-turn revision, and role-based agents.

It can be taught as:

- a two-session project;
- a one-week lab;
- a bridge assignment before the advanced course;
- a mini-capstone for the introductory course.

## Timing

### 15 minutes — Framing

Discuss why “vibe” is not merely subjective atmosphere but a shorthand for recurring patterns of structure, affect, form, and readerly pressure.

### 25 minutes — Agent review

Have students inspect `agents_config.json`. Ask:

- What does each agent see?
- What does each agent ignore?
- Which words are too vague?
- Which boundaries prevent the agent from becoming a generic summarizer?

### 40 minutes — Prompting lab

Students run one shared text through all three agents and compare outputs.

### 30 minutes — Matrix construction

Students enter scores and justifications into the CSV.

### 20 minutes — Python report

Students run:

```bash
python run_analysis.py
```

or:

```bash
python run_analysis.py my_matrix.csv --output my_report.txt
```

### 30 minutes — Critique discussion

Discuss which scores are useful, which are misleading, and which cluster labels need revision.

## Important teaching cautions

Do not let students treat the matrix as objective measurement. The matrix is a structured provocation.

Emphasize that the most important part of the project is the reliability warning. If students cannot name the limitation of a score, they have not understood the method.

## Possible extensions

- Add a fourth agent for pastiche, race/gender, translation, genre, or historical mediation.
- Compare two models using the same prompt.
- Replace summaries with short passages.
- Have students produce human benchmark scores before consulting the model.
- Ask students to revise cluster labels after seeing the generated report.
