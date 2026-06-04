# Advanced Course Instructional Videos and Recorded Workshops

## Purpose

This page collects instructional videos and recorded workshops that support the advanced course:

```text
Skills / Tools / MCP
→ RAG and Context Engineering
→ Loop Patterns and Agent Orchestration
→ Research Harnesses and Evaluation
→ Annotation Assets and Model Adaptation
→ Humanities Research Platforms
```

Videos are grouped by lesson.

Use them selectively.

Many videos are technical. For humanities students, pair videos with the course's manual exercises so students understand the method before seeing the framework.

---

# Recommended Use

## For students

Use:

- short conceptual videos
- demos that clarify the workflow
- selected workshop talks

Avoid requiring long technical coding videos unless the class has a programming component.

## For instructors

Use:

- longer workshops
- framework demos
- technical implementation videos
- evaluation and harness videos

---

# Lesson 1 — Skills, Tools, MCP, and Python Helpers

## Recommended

### Model Context Protocol (MCP), clearly explained

YouTube:  
https://www.youtube.com/watch?v=7j_NE6Pjv-E

Use for:  
Conceptual introduction to MCP as a standard way for LLMs to connect to tools and external services.

Teaching note:  
Pair this with the Lesson 1 distinction:

```text
Skill = method
Tool = action
MCP = connector
Agent = coordinator
```

---

## Optional Technical

### MCP in 26 Minutes

YouTube:  
https://www.youtube.com/watch?v=kOhLoixrJXo

Use for:  
Students or instructors who want a more implementation-oriented MCP overview.

---

### Model Context Protocol (MCP) Explained in 20 Minutes

YouTube:  
https://www.youtube.com/watch?v=N3vHJcHBS-w

Use for:  
Optional technical demonstration of MCP architecture and building a custom MCP server.

---

### Model Context Protocol (MCP) Explained in 17 Minutes

YouTube:  
https://www.youtube.com/watch?v=G5KyIzV-254

Use for:  
Short technical overview of MCP as a standardized connection layer.

---

# Lesson 2 — RAG and Context Engineering

## Recommended

### TypeScript RAG Tutorial for Beginners with LlamaIndex

YouTube:  
https://www.youtube.com/watch?v=af_HSgYvPcY

Use for:  
Showing students the practical mechanics of RAG: documents, indexing, retrieval, and generated answers.

Teaching note:  
This video is technical, so pair it with the course's manual RAG and keyword RAG exercises.

---

## Instructor Background / Optional Technical

### Advanced RAG Techniques with LlamaIndex

YouTube:  
https://www.youtube.com/watch?v=gDQYUaVvH6k

Use for:  
Instructor background or technical students interested in production RAG issues.

---

### LlamaIndex Introduction / RAG System

YouTube:  
https://www.youtube.com/watch?v=IQ0dCl93M3w

Use for:  
Overview of LlamaIndex and RAG concepts.

---

### Building Agentic RAG with LlamaIndex

YouTube:  
https://www.youtube.com/watch?v=KE7iHWzyc3A

Use for:  
Optional bridge between Lesson 2 RAG and Lesson 3 agent workflows.

---

# Lesson 3 — Loop Patterns, Multi-Turn Reasoning, and Agent Orchestration

## Recommended / Current Research

### NeurIPS 2025 Workshop on Multi-Turn Interactions in Large Language Models

Workshop site:  
https://workshop-multi-turn-interaction.github.io/

OpenReview venue:  
https://openreview.net/group?id=NeurIPS.cc/2025/Workshop/MTI-LLM

SlidesLive video collection:  
https://slideslive.com/neurips-2025/workshop-workshop-on-multiturn-interactions-in-large-language-models

Use for:  
Current research framing of multi-turn interaction.

Teaching note:  
This is better used as instructor background or selected student viewing. It supports the idea that multi-turn interaction is not just longer chat; it involves task progress, memory, evaluation, consistency, and adaptation.

---

## Optional Technical

### Building Effective Agents with LangGraph

YouTube:  
https://www.youtube.com/watch?v=aHCDrAbH_go

Use for:  
Students who want to see how loops and agent workflows can be implemented in a graph framework.

---

# Lesson 4 — Research Harnesses and Evaluation Harnesses

## Recommended

### Promptfoo: How to Test Your LLM? Very Easy!

YouTube:  
https://www.youtube.com/watch?v=VKyJYgz8IiQ

Use for:  
A practical view of evaluation harnesses: prompts, test cases, multiple models, and comparisons.

Teaching note:  
Connect this video to the Lesson 4 distinction:

```text
Loop = improves one output.
Harness = tests or operationalizes a method.
```

---

## Optional Technical

### Promptfoo and LLM Testing Videos

Promptfoo YouTube search / channel resources:  
https://www.youtube.com/results?search_query=promptfoo+llm+evaluation+tutorial

Use for:  
Finding updated Promptfoo demos if the specific video becomes outdated.

---

# Lesson 5 — Annotation Assets and Model Adaptation

## Optional Technical

### LoRA and QLoRA Explained / Fine-Tuning Tutorials

YouTube search:  
https://www.youtube.com/results?search_query=LoRA+QLoRA+fine+tuning+LLM+tutorial

Use for:  
Optional technical extension for students who want to understand model adaptation.

Teaching note:  
Do not make fine-tuning videos required unless students have the technical background.

The required Lesson 5 deliverable should remain:

```text
model adaptation dossier
```

not actual model training.

---

### Fine-Tuning LLMs with Hugging Face / QLoRA

YouTube search:  
https://www.youtube.com/results?search_query=Hugging+Face+QLoRA+fine+tuning+tutorial

Use for:  
Technical students who want to see LoRA / QLoRA workflows.

---

# Lesson 6 — Humanities Research Platform

## Recommended Instructor Use

There is no single perfect video for the final humanities platform capstone.

Instead, combine:

```text
MCP overview
RAG tutorial
Multi-turn workshop talk
Promptfoo evaluation tutorial
Fine-tuning optional video
```

and ask students to present how their own platform integrates:

```text
skill
RAG
loop
research harness
annotation assets
model adaptation decision
```

---

# Suggested Required Video Set

If students should watch only a small number of videos, use:

1. **Model Context Protocol (MCP), clearly explained**  
   https://www.youtube.com/watch?v=7j_NE6Pjv-E

2. **TypeScript RAG Tutorial for Beginners with LlamaIndex**  
   https://www.youtube.com/watch?v=af_HSgYvPcY

3. **Selected talk from NeurIPS 2025 Workshop on Multi-Turn Interactions in LLMs**  
   https://slideslive.com/neurips-2025/workshop-workshop-on-multiturn-interactions-in-large-language-models

4. **Promptfoo: How to Test Your LLM? Very Easy!**  
   https://www.youtube.com/watch?v=VKyJYgz8IiQ

5. **Optional: LoRA / QLoRA fine-tuning tutorial**  
   https://www.youtube.com/results?search_query=LoRA+QLoRA+fine+tuning+LLM+tutorial

---

# Suggested Instructor Viewing Set

For instructors preparing the advanced course:

1. NeurIPS 2025 Multi-Turn Workshop video collection  
   https://slideslive.com/neurips-2025/workshop-workshop-on-multiturn-interactions-in-large-language-models

2. MCP overview video  
   https://www.youtube.com/watch?v=7j_NE6Pjv-E

3. Advanced RAG Techniques with LlamaIndex  
   https://www.youtube.com/watch?v=gDQYUaVvH6k

4. Building Effective Agents with LangGraph  
   https://www.youtube.com/watch?v=aHCDrAbH_go

5. Promptfoo evaluation tutorial  
   https://www.youtube.com/watch?v=VKyJYgz8IiQ

---

# Notes on Video Stability

Video links change more often than papers or documentation.

For that reason:

- keep videos in this separate page
- avoid embedding them deeply inside lesson files
- review links before teaching each offering
- replace broken links with updated searches or official channels

---

# Optional Future Improvement

For a polished course site, each lesson could include a short section:

```markdown
## Optional Videos

See:
../../instructor_notes/advanced_course_videos.md
```

But for now, this page can remain a central video index.
