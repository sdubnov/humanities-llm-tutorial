# Humanities LLM Research Methods

A practical low-code / minimal-code course on using Large Language Models (LLMs) for humanities, interpretive, and qualitative research.

Created by Shlomo Dubnov  
sdubnov@ucsd.edu

This repository contains two connected course sequences:

1. **Introductory Course — Humanities LLM Research Methods**  
   A first course on prompting, files, memory, taxonomies, reasoning traces, role-based agents, and reproducible humanities workflows.

2. **Advanced Course — Humanities LLM Research Platforms**  
   A continuation that moves from LLM-assisted interpretation toward skills, tools, RAG, loop orchestration, research harnesses, annotation assets, model-adaptation decisions, and full humanities research platforms.

---

## Course Philosophy

The course treats the following as scholarly research artifacts:

- prompts
- rules
- annotations
- evaluations
- session summaries
- taxonomies
- reasoning traces
- context packets
- loop traces
- research harnesses
- model-adaptation memos

The emphasis is on:

- methodological transparency
- reproducibility
- critical interpretation
- controlled experimentation
- visible evidence-to-claim reasoning
- accountable human-AI scholarship

rather than software engineering for its own sake.

---

## Repository Structure

```text
humanities-llm-tutorial/
├── lessons/                 # Introductory course lessons
├── advanced_topics/          # Advanced course modules
├── projects/                 # Introductory capstone/project materials
├── advanced_projects/        # Advanced project materials, if used
├── templates/                # Reusable templates
├── skills/                   # Example skills, including metaphor analysis
├── examples/                 # Example texts and outputs
├── setup/                    # Setup scripts and environment notes
├── sources/                  # Source lists and BibTeX bibliography
└── instructor_notes/         # Teaching guides, course design notes, videos, references
```

---

# Introductory Course

## Core Progression

The introductory course follows this progression:

```text
chatting
→ prompting
→ files
→ rules
→ taxonomies
→ multi-turn analysis
→ explicit reasoning traces
→ role-based agents
→ research workflows
```

This progression moves students from casual interaction with LLMs toward reproducible humanities research methods.

“Explicit reasoning traces” refers to visible evidence-to-claim reasoning, branching interpretation, and procedural analysis.

“Role-based agents” refers to structured research roles such as Theorist, Analyst, Skeptic, Comparativist, Editor, and Archivist, rather than fully autonomous software agents.

## Introductory Lessons

### [Lesson 0 — First Contact with LLMs](lessons/lesson_00_first_contact.md)

Students explore LLM systems such as ChatGPT, Claude, Gemini, OpenAI Playground, and Hugging Face Spaces. They compare casual prompting with structured prompting and create their first session note.

### [Lesson 1 — Environment Setup](lessons/lesson_01_environment_setup.md)

Students set up a local repository, use markdown files, learn session memory, and understand why research memory should be externalized.

### [Lesson 2 — Prompting as Method](lessons/lesson_02_prompting_as_method.md)

Students transform humanities questions into procedural prompts, compare zero-shot and structured prompting, iteratively revise prompts, and evaluate outputs critically.

### [Lesson 3 — Sessions, CLI, Memory, and Commands](lessons/lesson_03_sessions_cli_memory_commands.md)

Students compare continuing the same session, restarting from markdown summaries, and starting fresh sessions. Topics include context windows, hidden compression, reproducibility, restartability, and external memory.

### [Lesson 4 — Humanities Concepts, Taxonomy, and Ontology](lessons/lesson_04_humanities_concepts_taxonomy_ontology.md)

Students extract analytical concepts from theory texts, build taxonomies and ontologies, operationalize literary concepts, and apply categories to poems and lyrics.

### [Lesson 5 — Multi-Turn Interaction and In-Context Learning](lessons/lesson_05_multi_turn_interaction_and_icl.md)

Students learn multi-turn interaction, in-context learning, teacher-annotated examples, critique loops, prompt iteration, and taxonomy revision.

### [Lesson 6 — Reasoning Traces: CoT, ToT, and PoT](lessons/lesson_06_reasoning_traces_cot_tot_pot.md)

Students learn how to make interpretive reasoning explicit, inspectable, and revisable through Chain-of-Thought-style interpretive traces, Tree-of-Thought-style branching interpretation, and Program-of-Thought-style procedural analysis.

### [Lesson 7 — Agent Roles for Interpretive Analysis](lessons/lesson_07_agent_roles_for_interpretive_analysis.md)

Students explore role-based agents such as Theorist, Analyst, Skeptic, Comparativist, Editor, and Archivist. Agent roles are introduced after reasoning traces so that each role works with explicit evidence, reasoning steps, and uncertainty notes.

---

## Introductory Capstone

The introductory capstone integrates:

```text
theory
→ taxonomy
→ prompting
→ multi-turn analysis
→ reasoning traces
→ role-based critique
→ evaluation
→ revision
```

Students submit a reproducible humanities LLM workflow, including saved prompts, outputs, reasoning traces, critiques, revisions, and a final methodological reflection.

See:

- [projects/](projects/)
- [templates/](templates/)

---

# Advanced Course

## Advanced Course Goal

The advanced course extends the introductory course from LLM-assisted interpretation to humanities research platforms.

The central goal is to move from:

```text
LLM assistant
```

to:

```text
humanities research platform
```

A humanities research platform makes interpretation:

- explicit
- grounded
- testable
- revisable
- archivable
- human-reviewable

## Advanced Progression

```text
skills and tools
→ RAG and context engineering
→ loop orchestration
→ research harnesses
→ annotation assets and model adaptation
→ humanities research platform
```

Core slogan:

```text
Skills package methods.
Tools execute actions.
MCP connects tools.
RAG controls context.
Loops make revision accountable.
Harnesses operationalize research policy.
Annotations preserve reusable examples.
Fine-tuning internalizes behavior only when justified.
Platforms assemble the system.
```

## Advanced Modules

### [Advanced Lesson 1 — Skills, Tools, MCP, and Python Helpers](advanced_topics/01_skills_tools_mcp/)

Students learn the difference between skills, tools, MCP, Python helpers, and agents. They inspect MCP/tool ecosystems and build a metaphor-analysis skill with a small Python checker.

### [Advanced Lesson 2 — RAG and Context Engineering for Humanities](advanced_topics/02_rag_for_humanities/)

Students learn how RAG works in practice: where documents live, how retrieval works, what the model sees, how context packets are built, and how grounded answers are evaluated.

### [Advanced Lesson 3 — Loop Patterns, Multi-Turn Reasoning, and Agent Orchestration](advanced_topics/03_loop_patterns/)

Students learn how CoT, ToT, multi-turn interaction, loops, agents, orchestration, and termination criteria relate. They run a practical Analyst → Skeptic → Editor → Evaluator → Archivist loop.

### [Advanced Lesson 4 — Research Harnesses and Evaluation Harnesses](advanced_topics/04_research_harnesses/)

Students learn that a harness is not only an evaluation table. A research harness is an operational wrapper around an LLM-assisted method, including policies, allowed sources, tools, checks, guardrails, human review points, and archives.

### [Advanced Lesson 5 — Annotation Assets and Model Adaptation](advanced_topics/05_annotations_and_finetuning/)

Students learn how annotations can support few-shot prompting, skills, RAG memory, evaluation harnesses, fine-tuning, distillation, and LoRA/adapters. The required task is a model-adaptation dossier, not actual model training.

### [Advanced Lesson 6 — Capstone: Building a Humanities Research Platform](advanced_topics/06_humanities_research_platform/)

Students assemble the advanced course into a platform that includes research policy, corpus, theory library, skill, RAG context packet, loop trace, research harness, annotation assets, model-adaptation memo, and final report.

---

## Advanced Capstone

The advanced capstone architecture is:

```text
Research question
→ corpus and theory library
→ skill
→ RAG/context engineering
→ loop/orchestration
→ research harness
→ annotation assets
→ model adaptation decision
→ final interpretive report
```

Students are not required to build a production app or fine-tune a model.

A successful advanced project demonstrates:

- methodological clarity
- source grounding
- reproducibility
- explicit uncertainty
- evidence-based interpretation
- appropriate use of tools
- thoughtful evaluation
- human review
- honest limitation statements

See:

- [advanced_topics/06_humanities_research_platform/](advanced_topics/06_humanities_research_platform/)
- [advanced_projects/](advanced_projects/)

---

# Instructor Notes and Teaching Resources

The `instructor_notes/` folder contains teaching guides for both the introductory and advanced sequences.

Key files:

- [Introductory Instructor Guide](instructor_notes/instructor_notes_and_teaching_guide.md)
- [Advanced Course Design / Instructor Notes](instructor_notes/advanced_course_design.md)
- [Advanced Course References](instructor_notes/advanced_course_references.md)
- [Introductory Course Videos](instructor_notes/introductory_course_videos.md)
- [Advanced Course Videos](instructor_notes/advanced_course_videos.md)

These files include:

- pedagogical rationale
- suggested pacing
- lesson-by-lesson teaching notes
- student learning checkpoints
- assessment strategy
- capstone evaluation criteria
- suggested videos
- references and bibliography

---

# References and Sources

The `sources/` folder contains course-wide source materials and bibliographies.

Important files include:

- [Multi-turn and CLI sources](sources/multiturn_and_cli_sources.md)
- [Advanced Course Bibliography](sources/advanced_course_bibliography.bib)

The readable advanced-course reference guide is in:

- [instructor_notes/advanced_course_references.md](instructor_notes/advanced_course_references.md)

---

# Videos

Video references are collected separately because video links change more often than papers or documentation.

- [Introductory Course Videos](instructor_notes/introductory_course_videos.md)
- [Advanced Course Videos](instructor_notes/advanced_course_videos.md)

---

# Included Materials

The repository includes:

- introductory lessons
- advanced modules
- templates
- setup scripts
- instructor notes
- video reference pages
- source references
- BibTeX bibliography
- example skills
- tiny example texts
- introductory capstone materials
- advanced platform capstone materials

---

# Suggested Use

## For students

Start with:

```text
lessons/
```

Then, after completing the introductory sequence, continue to:

```text
advanced_topics/
```

## For instructors

Start with:

```text
instructor_notes/instructor_notes_and_teaching_guide.md
instructor_notes/advanced_course_design.md
```

Then review:

```text
instructor_notes/introductory_course_videos.md
instructor_notes/advanced_course_videos.md
instructor_notes/advanced_course_references.md
```

## For project work

Use:

```text
projects/
advanced_projects/
templates/
advanced_topics/06_humanities_research_platform/
```

---

# Final Course Vision

The introductory course teaches students to use LLMs as structured research partners.

The advanced course teaches students to design accountable research environments around LLMs.

The desired transformation is:

```text
from answer generation
to method design

from chat transcript
to research platform

from automation enthusiasm
to accountable human-AI scholarship
```
