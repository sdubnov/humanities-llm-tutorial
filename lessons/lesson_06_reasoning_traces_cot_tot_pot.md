# Lesson 6 — Reasoning Traces: CoT, ToT, and PoT

## Goal

Learn how to make interpretive reasoning explicit, inspectable, and revisable by comparing linear reasoning, branching reasoning, and procedural reasoning.

This lesson introduces three reasoning formats:

- **CoT**: Chain-of-Thought-style interpretive trace
- **ToT**: Tree-of-Thought-style branching interpretation
- **PoT**: Program-of-Thought-style procedural analysis

In this course, these are not treated as access to the model's private reasoning. They are treated as **external scholarly artifacts** that can be inspected, challenged, revised, and reused.

---

## Why this lesson comes before agents

Before assigning roles such as Analyst, Skeptic, Editor, or Archivist, students need to understand what kind of reasoning those roles should produce.

Without explicit reasoning traces, agent roles can become theatrical:

```text
Analyst says something.
Skeptic disagrees.
Editor rewrites.
```

With reasoning traces, role-based agents become methodological:

```text
Analyst proposes evidence-to-claim reasoning.
Skeptic tests unsupported steps.
Editor revises the interpretation.
Archivist records the reasoning trace and changes.
```

---

## Key distinction

A normal LLM answer gives a result.

A reasoning trace records a path.

```text
answer = final interpretation
reasoning trace = evidence → interpretive move → uncertainty → claim
```

The purpose is not to make the model sound more confident. The purpose is to make the method more visible.

---

## Part 1 — Direct Interpretation

Choose a short text:

- poem
- lyric
- speech excerpt
- biblical passage
- historical document
- short theoretical passage

Prompt:

```text
Interpret the following text. Focus on metaphor, imagery, and possible cultural meaning.

Text:
[paste text here]
```

Save the output:

```text
outputs/direct_interpretation_001.md
```

Reflection questions:

- What claims did the model make?
- Did it cite evidence?
- Did it distinguish evidence from interpretation?
- Did it mention uncertainty?

---

## Part 2 — CoT-Style Interpretive Trace

CoT usually means step-by-step reasoning. In this course, we adapt it as a visible interpretive trace.

Use this prompt:

```text
Analyze the following text using a visible interpretive reasoning trace.

Do not only give a final interpretation.

For each major claim, provide:

1. textual evidence
2. the interpretive move from evidence to meaning
3. an uncertainty or ambiguity note
4. a final claim

Use this structure:

Evidence:
Interpretive move:
Uncertainty:
Claim:

Text:
[paste text here]
```

Save the output:

```text
outputs/cot_interpretive_trace_001.md
```

What to look for:

- Does each claim have evidence?
- Are the interpretive moves plausible?
- Does the model admit ambiguity?
- Are any claims unsupported?

---

## Part 3 — ToT-Style Branching Interpretation

ToT means exploring multiple possible paths rather than one linear chain.

In humanities research, this is useful because a text can support competing interpretations.

Use this prompt:

```text
Analyze the following text using a Tree-of-Thought-style interpretive search.

Generate three competing interpretations.

For each branch, provide:

1. interpretation title
2. main claim
3. supporting evidence
4. weaknesses or risks
5. decision: continue, revise, or prune

After comparing the branches, synthesize a final interpretation that preserves the strongest evidence and acknowledges ambiguity.

Text:
[paste text here]
```

Save the output:

```text
outputs/tot_interpretive_search_001.md
```

What to look for:

- Are the branches genuinely different?
- Does each branch use evidence?
- Does the model fairly evaluate weaknesses?
- Does it prune too quickly?
- Does the synthesis preserve ambiguity?

---

## Part 4 — PoT-Style Procedural Analysis

PoT usually means Program-of-Thought prompting, where reasoning is expressed as code or as an explicit procedure.

In this course, PoT means turning an interpretive method into a structured, repeatable procedure.

Use this prompt:

```text
Turn the analysis of this text into a reusable procedure.

Create a procedure that could be applied to other texts.

The procedure should include:

1. input
2. preprocessing or segmentation
3. categories to identify
4. evidence fields to collect
5. confidence or uncertainty fields
6. output format
7. failure modes

Then apply the procedure briefly to the text.

Text:
[paste text here]
```

Save the output:

```text
outputs/pot_procedure_001.md
```

Optional structured output format:

```json
{
  "text_id": "",
  "passage": "",
  "device": "",
  "evidence": "",
  "interpretive_move": "",
  "possible_meaning": "",
  "confidence": "",
  "uncertainty_note": ""
}
```

What to look for:

- Is the procedure reusable?
- Does it force evidence collection?
- Does it preserve ambiguity?
- Does it over-formalize interpretation?

---

## Part 5 — Compare the Four Methods

Create a comparison file:

```text
evaluations/reasoning_comparison_001.md
```

Use this structure:

```markdown
# Reasoning Comparison

## Text analyzed

## Direct interpretation
Strengths:
Weaknesses:

## CoT-style interpretive trace
Strengths:
Weaknesses:

## ToT-style branching interpretation
Strengths:
Weaknesses:

## PoT-style procedural analysis
Strengths:
Weaknesses:

## Best use case for each method

## What changed in my understanding?

## What would I reuse in a future research workflow?
```

---

## Discussion

Questions for class discussion:

- When did reasoning traces improve interpretation?
- When did they create false confidence?
- Which method was best for ambiguity?
- Which method was best for reproducibility?
- Which method was best for building a reusable workflow?
- What kinds of humanities questions should not be forced into a procedure?

---

## Common failure modes

Watch for:

- fabricated evidence
- unsupported reasoning chains
- excessive confidence
- shallow branching
- branches that are only rewordings of each other
- premature pruning of valid interpretations
- procedures that flatten literary ambiguity
- output formats that look rigorous but hide weak interpretation

---

## Deliverables

Submit:

```text
outputs/direct_interpretation_001.md
outputs/cot_interpretive_trace_001.md
outputs/tot_interpretive_search_001.md
outputs/pot_procedure_001.md
evaluations/reasoning_comparison_001.md
```

Optional:

```text
templates/custom_reasoning_trace_template.md
```

---

## Instructor note

Students may ask whether CoT reveals the model's real private reasoning. For this course, avoid framing it that way. The course treats reasoning traces as **requested explanations and structured scholarly artifacts**, not as guaranteed access to internal model cognition.
