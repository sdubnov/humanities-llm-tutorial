# Instructor Notes and Teaching Guide

## Course Philosophy

The course teaches students to move from casual AI chatting toward structured, reproducible humanities research workflows. Prompts, summaries, rules, evaluations, taxonomies, and reasoning traces are treated as scholarly artifacts.

Core progression:

```text
chatting → prompting → files → rules → taxonomies → multi-turn analysis → explicit reasoning traces → role-based agents → research workflows
```

This progression moves students from casual interaction with LLMs toward reproducible humanities research methods.

“Explicit reasoning traces” refers to visible evidence-to-claim reasoning, branching interpretation, and procedural analysis. “Role-based agents” refers to structured research roles such as Theorist, Analyst, Skeptic, Comparativist, Archivist, and Editor, rather than fully autonomous software agents.

The course emphasizes:

- methodological transparency
- reproducibility
- controlled interpretation
- critical evaluation
- externalized cognition
- reasoning transparency

rather than heavy software engineering.

A central goal of the course is to help students distinguish between an LLM answer and an LLM-assisted method. For this reason, the course introduces reasoning traces before agent roles. Chain-of-Thought, Tree-of-Thought, and Program-of-Thought are taught not as magic ways to make the model smarter, but as ways of externalizing scholarly reasoning: linear interpretation, branching comparison, and procedural analysis. This prepares students to understand agents, tools, RAG, skills, and evaluation harnesses in a later advanced course.

---

## Lesson 0 — First Contact with LLMs

Purpose: Introduce the difference between casual chat, structured prompting, and reusable workflows.

Students learn:

- prompt structure changes outputs
- reusable formats matter
- interpretation can become procedural

Discussion topics:

- What changed between explanation and analysis?
- Why are tables/checklists more reusable?
- Is the model “understanding” metaphor?

Evaluation: Students should document:

- prompt differences
- useful outputs
- vague outputs
- possible improvements

---

## Lesson 1 — Build the Research Environment

Purpose: Teach students to externalize research memory into files.

Key concepts:

- session memory
- markdown notebooks
- reproducibility
- project organization

Important distinction:

```text
research memory ≠ chat history
```

Discussion topics:

- Why save prompts separately?
- Why use markdown?
- Why does the LLM not remember everything?
- How does external memory support reproducibility?

Evaluation: Students should:

- create project structure
- save prompts/outputs correctly
- understand the role of each folder

---

## Lesson 2 — Prompting as Method

Purpose: Transform humanities interpretation into a controlled protocol.

Students learn:

- role prompting
- evidence requirements
- uncertainty handling
- output formatting
- prompt revision

Instructor emphasis: The goal is not “getting the right answer.” The goal is creating a controlled interpretive method.

Evaluation criteria:

- clarity of prompt
- evidence usage
- uncertainty awareness
- prompt revision quality
- critique of model output

---

## Lesson 3 — Sessions, CLI Tools, Memory, and Commands

Purpose: Introduce hidden memory, restartability, compression, and reproducibility.

Students compare:

1. continuing the same chat
2. restarting from a markdown summary
3. starting a fresh session

Discussion topics:

- context windows
- hidden summarization
- external memory
- reproducibility
- what changes after a restart?

Important learning goal: Students experience the difference between conversational continuity and portable research state.

Evaluation: Students should:

- summarize sessions clearly
- identify what carries over
- explain instability or information loss

---

## Lesson 4 — Humanities Concepts, Taxonomy, and Ontology

Purpose: Move from free interpretation toward explicit categories.

Students learn:

- taxonomy construction
- ontology relationships
- operationalization of literary concepts
- ambiguity handling

Discussion topics:

- Can interpretation become partially formalized?
- What is lost in formalization?
- Are categories culturally dependent?
- What makes a category usable across multiple texts?

Common failure modes:

- overgeneralization
- invented categories
- flattening ambiguity
- unsupported cultural claims

Evaluation: Students should:

- define categories clearly
- use inclusion/exclusion criteria
- identify ambiguous cases
- revise vague concepts

---

## Lesson 5 — Multi-Turn Interaction and In-Context Learning

Purpose: Introduce iterative refinement and temporary specialization through context.

Students learn:

- in-context learning
- example-based adaptation
- critique loops
- taxonomy revision
- prompt iteration
- session documentation

Instructor clarification: This lesson may include critique and revision, but it should not be described as a full CoT/ToT/PoT lesson. Reasoning traces are introduced explicitly in Lesson 6.

Discussion topics:

- When does the model begin to appear expert?
- Is this real expertise?
- What disappears after restart?
- What is preserved when examples are saved externally?

Evaluation: Students should:

- revise prompts iteratively
- critique outputs
- compare versions
- document improvements

---

## Lesson 6 — Reasoning Traces: CoT, ToT, and PoT

Purpose: Teach students how to make interpretive reasoning explicit, inspectable, and revisable before moving into role-based agents or automated workflows.

Students learn:

- Chain-of-Thought-style interpretive reasoning
- Tree-of-Thought-style branching interpretation
- Program-of-Thought-style procedural analysis
- evidence-to-claim reasoning
- uncertainty tracking
- comparison between direct prompting and structured reasoning

Important distinction: Reasoning traces are not treated as access to the model’s private mind. They are treated as external scholarly artifacts: visible explanations, procedures, branches, and revision paths that can be inspected, challenged, and improved.

Instructor emphasis: The goal is not to make the model “think like a human.” The goal is to help students externalize interpretive method.

CoT in this course means a linear interpretive trace:

```text
evidence → interpretive move → uncertainty → claim
```

ToT means branching interpretive search:

```text
possible reading A
possible reading B
possible reading C
→ compare evidence
→ identify weaknesses
→ prune or revise
→ synthesize
```

PoT means turning interpretation into a procedure:

```text
input text
→ segment passages
→ identify devices
→ classify evidence
→ assign confidence
→ export structured notes
```

Discussion topics:

- What is the difference between an answer and a reasoning trace?
- When does step-by-step reasoning clarify interpretation?
- When does it create false confidence?
- How can multiple competing interpretations be compared fairly?
- What kinds of humanities tasks can become procedures?
- What is lost when interpretation becomes procedural?

Common failure modes:

- unsupported reasoning chains
- overconfident explanations
- fabricated evidence
- premature pruning of valid interpretations
- treating the model’s explanation as proof
- confusing procedural structure with truth

Practical exercise: Students compare four outputs on the same text:

1. direct interpretation
2. CoT-style stepwise interpretation
3. ToT-style competing interpretations
4. PoT-style structured procedure or annotation schema

Evaluation: Students should:

- distinguish evidence from interpretation
- identify unsupported reasoning steps
- compare competing interpretive branches
- explain where structured reasoning improved or weakened the analysis
- produce a reusable reasoning protocol

---

## Lesson 7 — Agent Roles for Interpretive Analysis

Purpose: Introduce role-based agents as pedagogical workflows that build on the reasoning traces developed in Lesson 6.

Roles include:

- Theorist
- Analyst
- Skeptic
- Comparativist
- Editor
- Archivist

Important clarification: These are pedagogical agents, not orchestration systems. Agents should not be introduced before students understand reasoning traces. Otherwise, role-based workflows can become theatrical rather than methodological. The Analyst, Skeptic, Comparativist, Editor, and Archivist roles should each operate on explicit evidence, reasoning steps, and uncertainty notes.

Discussion topics:

- Why separate critique from interpretation?
- Why is skepticism useful?
- What happens when all roles collapse into one prompt?
- How does a Skeptic role improve a reasoning trace?
- How does an Archivist role make the workflow reproducible?

Evaluation: Students should:

- compare role outputs
- identify improvements from critique
- explain role specialization
- preserve reasoning traces and revisions in project files

---

## Final Project

Purpose: Integrate all course components into a reproducible humanities workflow.

Students combine:

- theory text
- taxonomy
- prompting
- multi-turn interaction
- reasoning traces
- role-based critique
- evaluation
- revision
- session documentation

Primary grading criteria:

- methodological clarity
- reproducibility
- taxonomy quality
- reasoning transparency
- critique quality
- awareness of limitations
- revision process

The project should not be graded solely on whether the literary interpretation is “correct.” The focus is the quality of the workflow and methodological reasoning.

Suggested final project folder structure:

```text
final_project/
├── research_question.md
├── source_texts/
├── theory_notes/
├── taxonomy.md
├── prompts/
├── outputs/
├── reasoning_traces/
├── agent_critiques/
├── revisions/
├── evaluation.md
└── final_reflection.md
```

Suggested final reflection questions:

- What changed between the first answer and the final workflow?
- Which prompt decisions mattered most?
- Where did reasoning traces clarify the interpretation?
- Where did they create false confidence?
- How did role-based critique improve the work?
- What would need to change for this to become a reusable research method?
