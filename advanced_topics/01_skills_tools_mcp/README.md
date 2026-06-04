# Advanced Lesson 1 — Skills, Tools, MCP, and Python Helpers

## From Reusable Humanities Methods to Tool-Connected Research Workflows

This lesson introduces the architecture of advanced LLM-based humanities research.

The goal is not to install a full MCP system immediately.

The goal is **architectural literacy**: students should be able to distinguish a humanities method, a reusable skill, an executable tool, a connector, a workflow, and an agent.

---

## Learning Goals

By the end of this lesson, students should be able to explain:

```text
Skill = method package
Tool = executable action
MCP = connection protocol
Agent = coordinator over time
Python helper = repeatable validation or processing step
```

More precisely:

```text
A skill tells the model HOW to perform a method.
A tool lets the model DO an action.
MCP exposes tools and data sources through a common protocol.
An agent coordinates skills, tools, memory, retrieval, and evaluation over time.
```

Core slogan:

```text
Skills package methods.
Tools execute actions.
MCP connects tools.
Agents coordinate skills and tools over time.
Fine-tuning internalizes behavior.
```

---

## Why This Lesson Comes First

The advanced course begins with skills, tools, and MCP because students need architectural literacy before they use RAG, evaluation harnesses, fine-tuning, or research platforms.

The goal is to understand the difference between:

- a humanities method
- a reusable skill
- an executable tool
- a connector
- a workflow
- an agent

Without this distinction, students may confuse a good prompt with a reusable method, or tool use with methodological validity.

---

## 1. Skill, Tool, MCP, Agent

### Skill

A **skill** is a reusable method package.

It tells the model **how to perform a method**.

A skill may contain:

```text
SKILL.md
examples.md
rubric.md
output_schema.json
failure_modes.md
scripts/
templates/
```

Humanities examples:

```text
metaphor_analysis_skill
close_reading_skill
translation_comparison_skill
discourse_analysis_skill
voice_annotation_skill
cultural_reference_detection_skill
```

### Tool

A **tool** is an executable action.

It lets the model do something:

```text
search files
query Zotero
read PDFs
run Python
transcribe audio
translate text
export CSV
validate JSON
```

### MCP

**MCP**, or Model Context Protocol, is a connection protocol for exposing tools and data sources to LLM applications.

Think of it as:

```text
API layer for LLM tools
```

An MCP server can connect an AI assistant to external systems such as:

```text
Zotero
Obsidian
filesystem
GitHub
PDF libraries
databases
translation services
transcription services
search systems
```

### Agent

An **agent** coordinates:

```text
skills
tools
memory
retrieval
evaluation
stopping conditions
```

over time.

In this course, agents are not magic autonomous researchers. They are systems or workflows that coordinate methods, tools, and checks.

---

## 2. Why Discuss MCP Without Installing It?

Because the first goal is conceptual literacy.

Students should learn to recognize:

```text
Skill = method
Tool = action
MCP = connector
Agent = coordinator
```

Even without installing MCP, they can understand how a future humanities assistant might connect to Zotero, Obsidian, PDFs, transcription, translation, or a local corpus.

This is like teaching what an API is before asking students to build one.

---

## 3. Where to Find MCP Servers and Tools

Students should know how to inspect the MCP ecosystem without necessarily installing anything.

Useful discovery points include:

```text
Official MCP Registry
GitHub MCP Registry / MCP-related GitHub repositories
Awesome MCP Servers lists
MCP.so
Composio toolkits
GitHub search
```

When inspecting an MCP server, ask:

1. What system does it connect to?
2. What tools or actions does it expose?
3. What data does it access?
4. Can it modify files or only read them?
5. Does it require credentials?
6. What humanities task could it support?
7. What are the risks?

---

## 4. Humanities-Relevant MCP Categories

For humanities research, the most useful MCP categories are research-context tools:

```text
Zotero / bibliography
Obsidian / markdown notes
filesystem / local corpus
GitHub / research repository
PDF reading and extraction
semantic search / embeddings
translation APIs
speech-to-text / audio transcription
audio annotation
web search / web archives
spreadsheet / CSV tools
```

The point is not that students must install all of these.

The point is that they should be able to ask:

```text
What data does this tool access?
What action does it expose?
What humanities task could it support?
What are the risks?
```

---

## 5. Worked Example: Metaphor Analysis Skill

This example shows how a humanities method can become a reusable skill.

The skill analyzes metaphor in short texts and includes a small Python checker.

Folder:

```text
metaphor_analysis_skill_example/
├── SKILL.md
├── examples.md
├── rubric.md
├── output_schema.json
└── scripts/
    └── check_output.py
```

### Example Input

```text
The city was a broken mirror, reflecting every dream I had lost.
```

### Expected Output

```json
{
  "passage": "The city was a broken mirror",
  "device": "metaphor",
  "evidence": "The city was a broken mirror",
  "source_domain": "broken mirror",
  "target_domain": "city",
  "affect": "loss, fragmentation",
  "interpretation": "The city is represented as damaged and reflective of lost hopes.",
  "alternative_reading": "The mirror may also suggest self-recognition.",
  "confidence": 5
}
```

---

## 6. Python Inside a Skill

A skill can include code.

The skill explains the method.

The Python script performs a repeatable subtask.

In this example, Python does not interpret the metaphor. It checks whether an annotation contains the required fields.

This teaches students that computation can support humanities interpretation without replacing judgment.

### What the checker does

The checker verifies that an annotation includes required fields such as:

```text
passage
device
evidence
source_domain
target_domain
interpretation
confidence
```

Students can run:

```bash
python scripts/check_output.py
```

or:

```bash
python scripts/check_output.py my_annotation.json
```

This creates the progression:

```text
manual skill
→ skill with helper script
→ tool-callable script
→ MCP-connected tool
→ agent workflow
```

---

## 7. Lab 1A — Inspect One MCP Server

Use:

```text
mcp_tool_review_template.md
```

Choose one MCP server or tool category.

Search for one of:

```text
Zotero
Obsidian
filesystem
GitHub
PDF
transcription
translation
semantic search
spreadsheet
```

Record:

1. name
2. source or link
3. what it connects to
4. what tools or actions it exposes
5. what data it accesses
6. possible humanities use case
7. risks or limitations
8. whether you would use it in a research workflow

Save as:

```text
mcp_tool_review.md
```

---

## 8. Lab 1B — Build One Skill with a Python Helper

Create:

```text
skills/my_humanities_skill/
├── SKILL.md
├── examples.md
├── rubric.md
├── output_schema.json
└── scripts/
    └── check_output.py
```

Choose one humanities method:

```text
metaphor analysis
close reading
rhetorical device annotation
discourse analysis
translation comparison
cultural reference detection
narrative structure analysis
voice annotation
```

Your Python checker should not perform the whole interpretation. It should check whether the output follows the required structure.

### Architecture Reflection

Answer:

1. What part is the skill?
2. What part is the tool?
3. What part could become MCP-accessible?
4. What would an agent coordinate?
5. What remains human judgment?

---

## 9. Advanced MCP Connection Section

Because MCP is not covered again later in the course, this lesson includes an optional advanced section:

```text
advanced_mcp_connection_section.md
```

That section explains how a local script, such as:

```text
scripts/check_output.py
```

could become an MCP-accessible tool.

The goal is not full production deployment. The goal is to understand the connection architecture:

```text
LLM application / MCP host
        ↓
MCP client
        ↓
MCP server
        ↓
local tool or data source
        ↓
result returned to model
```

---

## 10. MCP Safety and Research Ethics

MCP tools can access files, libraries, APIs, and local systems. That makes them powerful, but also risky.

Before using an MCP server, ask:

1. What data does it access?
2. Can it modify files?
3. Can it run commands?
4. Does it send data outside the machine?
5. Does it require credentials?
6. Is the server maintained and trustworthy?
7. Could prompt injection cause unsafe tool use?
8. Is private or copyrighted material being exposed?

For humanities students, the practical rule is:

```text
Do not connect private archives, student data, unpublished manuscripts, copyrighted PDFs, or personal notes to unknown MCP servers without review.
```

---

## Final Reflection

Write a short reflection:

1. What is the difference between a skill and a tool?
2. What does MCP add?
3. Why might a humanities researcher want Python inside a skill?
4. What would an agent coordinate in this example?
5. What should remain human-reviewed?
