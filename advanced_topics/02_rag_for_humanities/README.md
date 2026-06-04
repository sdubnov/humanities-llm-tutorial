# Advanced Lesson 2 — RAG and Context Engineering for Humanities

## Goal

Learn how Retrieval-Augmented Generation, or RAG, works in practice for humanities research.

This lesson answers concrete questions:

```text
Where are the documents?
How are they searched?
What gets retrieved?
What gets pasted or passed into the model?
How is the answer grounded?
How do we evaluate whether retrieval helped?
```

The central teaching point:

```text
RAG is not the answer.
RAG is the process of deciding what evidence the model is allowed to use.
```

---

## Learning Goals

By the end of this lesson, students should be able to:

1. explain the difference between a corpus, a retrieval step, a context packet, and a model answer
2. build a manual RAG context packet
3. run a simple keyword retrieval script over a local corpus
4. generate a context packet from retrieved passages
5. ask an LLM to answer using only retrieved context
6. evaluate whether the answer is grounded in the retrieved evidence
7. explain how vector RAG and MCP-connected RAG extend the basic method

---

## What RAG Actually Does

A basic RAG workflow looks like this:

```text
research question
→ retrieve relevant documents or passages
→ insert retrieved context into the prompt
→ ask the model to answer using that context
→ check whether the answer is grounded
```

More mechanically:

```text
Corpus folder
→ document loading
→ chunking or passage selection
→ retrieval
→ context packet
→ prompt
→ grounded answer
→ citation / evidence check
```

Or step by step:

```text
1. Put documents somewhere.
2. Split them into passages or chunks.
3. Store passage text plus metadata.
4. Ask a question.
5. Search for relevant passages.
6. Insert those passages into the LLM prompt.
7. Ask the LLM to answer only from those passages.
8. Evaluate whether the answer used the retrieved evidence correctly.
```

---

## RAG Is a Method, Not One Tool

There is no single tool called “RAG.”

RAG can be done with:

```text
manual copy/paste context packets
Python keyword search
Python + embeddings
LlamaIndex
LangChain
Chroma
Qdrant
Weaviate
Elasticsearch / OpenSearch
Zotero MCP
Obsidian MCP
filesystem MCP
custom MCP vector-search server
```

In this lesson, we use:

```text
Level 1: Manual RAG
Level 2: Local keyword RAG
Level 3: Conceptual vector RAG
Optional: MCP-connected RAG
```

Manual and keyword RAG come first because students need to understand what retrieval is doing before hiding it behind a framework.

---

## Where Are the Documents?

For this lesson, the documents are local files in the course folder:

```text
advanced_topics/02_rag_context_engineering/corpus/
```

The folder contains:

```text
corpus/
├── primary_texts/
│   ├── poem_city_mirror.md
│   ├── speech_freedom_excerpt.md
│   └── biblical_exodus_excerpt.md
├── theory_texts/
│   ├── metaphor_theory_notes.md
│   └── liberty_theory_notes.md
└── prior_annotations/
    └── metaphor_annotations.jsonl
```

The documents are deliberately small so students can inspect them directly.

---

## The Miniature Corpus

### Primary texts

The primary texts include:

- a short poem-like passage about a city as a broken mirror
- a short speech excerpt about freedom
- a short Exodus-inspired passage about leaving bondage

### Theory texts

The theory texts include:

- notes on metaphor analysis
- notes on negative and positive liberty

### Prior annotations

The prior annotation file contains a previous metaphor annotation in JSONL format.

This lets students see that RAG can retrieve not only source texts, but also theory notes, taxonomies, and prior research artifacts.

---

## Level 1 — Manual RAG

Manual RAG means students retrieve context by reading and selecting passages themselves.

### Research question

```text
How does the broken mirror metaphor express loss or fragmentation?
```

### Manual retrieval

Students inspect the corpus and select relevant passages.

Example selected context:

```text
Source: corpus/primary_texts/poem_city_mirror.md

The city was a broken mirror, reflecting every dream I had lost.
Every street returned my face in pieces.
```

```text
Source: corpus/theory_texts/metaphor_theory_notes.md

A metaphor maps meaning from a source domain onto a target domain.
The source domain provides concrete imagery or structure.
The target domain is the subject being understood through that imagery.
```

### Context packet

Students paste selected passages into a structured packet.

Use:

```text
templates/context_packet_template.md
```

### Grounded prompt

```text
Answer the research question using only the retrieved context below.

Research question:
How does the broken mirror metaphor express loss or fragmentation?

Retrieved context:
[paste context packet]

Requirements:
- cite the source file for each claim
- distinguish textual evidence from interpretation
- state uncertainty
- do not use outside information
```

---

## Level 2 — Keyword RAG with Python

Keyword RAG uses a script to search the local corpus.

The script does not understand meaning deeply. It scores documents by keyword overlap with the question.

This is simple but useful for teaching the mechanics of retrieval.

### Script 1

```text
scripts/keyword_retrieve.py
```

Run:

```bash
cd advanced_topics/02_rag_context_engineering
python scripts/keyword_retrieve.py "How does the broken mirror metaphor express loss?"
```

The script prints the top matching corpus files and excerpts.

### Script 2

```text
scripts/build_context_packet.py
```

Run:

```bash
cd advanced_topics/02_rag_context_engineering
python scripts/build_context_packet.py "How does the broken mirror metaphor express loss?"
```

The script writes:

```text
outputs/rag_context_packet.md
```

Students then paste `outputs/rag_context_packet.md` into an LLM and ask for a grounded answer.

---

## What the LLM Actually Sees

The LLM does not magically know the corpus.

In this lesson, the LLM sees only what the student pastes into the prompt.

That means the context packet is crucial.

A good RAG prompt includes:

```text
research question
retrieved passages
source paths
instructions
citation requirements
uncertainty requirements
```

A weak RAG prompt includes only:

```text
answer this question
```

without showing what evidence the answer should use.

---

## Level 3 — Vector RAG

Vector RAG uses embeddings to retrieve semantically similar chunks.

The workflow is:

```text
Documents are split into chunks.
Each chunk is converted into an embedding.
Embeddings are stored in a vector database.
The question is also embedded.
The system retrieves chunks whose vectors are closest to the question vector.
Retrieved chunks are inserted into the prompt.
The LLM answers using those chunks.
```

Tools that can support this include:

```text
LlamaIndex
LangChain
Chroma
Qdrant
Weaviate
FAISS
```

For humanities students, the important idea is:

```text
Keyword RAG retrieves matching words.
Vector RAG retrieves related meanings.
```

But vector RAG can also retrieve irrelevant passages if the embedding similarity does not match the interpretive question.

So vector retrieval still needs human evaluation.

---

## MCP-Connected RAG

MCP does not replace RAG.

```text
RAG = method for grounding generation in retrieved context.
MCP = protocol for connecting an LLM app to tools or data sources.
```

MCP can support RAG by exposing retrieval tools such as:

```text
search_local_corpus
read_pdf_text
search_zotero_library
search_obsidian_notes
query_vector_index
retrieve_prior_annotations
```

An MCP-connected RAG workflow might look like:

```text
research question
→ agent calls search_local_corpus
→ agent calls search_theory_notes
→ retrieved passages become context
→ model answers with citations
→ evaluator checks grounding
→ model revises answer
```

In this lesson we do not require MCP installation.

The goal is to understand how local retrieval could later become tool-connected retrieval.

---

## Lab — Build and Evaluate a Mini RAG Workflow

### Part A — Inspect the corpus

Open:

```text
corpus/
```

Identify:

1. primary texts
2. theory texts
3. prior annotations

Answer:

```text
What kind of evidence does each folder contain?
```

### Part B — Manual retrieval

Choose a research question:

```text
How does the broken mirror metaphor express loss or fragmentation?
```

or:

```text
How does the freedom speech distinguish external constraint from inner capacity?
```

Manually select three useful passages.

Save your manual packet as:

```text
outputs/manual_context_packet.md
```

Use:

```text
templates/context_packet_template.md
```

### Part C — Keyword retrieval

Run:

```bash
python scripts/keyword_retrieve.py "How does the broken mirror metaphor express loss?"
```

Compare the retrieved passages with your manual choices.

### Part D — Build a context packet automatically

Run:

```bash
python scripts/build_context_packet.py "How does the broken mirror metaphor express loss?"
```

This writes:

```text
outputs/rag_context_packet.md
```

### Part E — Ask the LLM

Paste the context packet into an LLM.

Ask:

```text
Answer the research question using only the retrieved context.
Cite the source path for every claim.
Distinguish evidence from interpretation.
State uncertainty.
```

Save the answer as:

```text
outputs/rag_answer.md
```

### Part F — Evaluate the answer

Use:

```text
templates/rag_evaluation_template.md
```

Save:

```text
outputs/rag_evaluation.md
```

### Part G — Reflection

Answer:

1. What did manual retrieval find that keyword retrieval missed?
2. What did keyword retrieval find that you missed?
3. Did the model use the retrieved context accurately?
4. Did the model invent anything outside the packet?
5. What would vector RAG improve?
6. What would MCP add?
7. What still requires human judgment?

---

## Common Failure Modes

RAG can fail in several ways:

```text
wrong documents retrieved
right document but wrong passage
too much irrelevant context
missing theory context
missing primary-text evidence
model ignores retrieved evidence
model invents outside information
model cites source paths without support
retrieval narrows interpretation too much
```

For humanities, a key risk is that RAG can make an answer look grounded even when the retrieved passages are poorly chosen.

---

## Evaluation Criteria

A good RAG answer should:

- answer the research question
- cite retrieved source paths
- use exact textual evidence
- distinguish evidence from interpretation
- acknowledge uncertainty
- avoid outside claims
- explain how retrieved theory informs interpretation
- avoid flattening ambiguity

---

## Deliverables

Submit:

```text
outputs/manual_context_packet.md
outputs/rag_context_packet.md
outputs/rag_answer.md
outputs/rag_evaluation.md
```

Also submit a short reflection:

```text
outputs/rag_reflection.md
```

---

## Final Takeaway

RAG is not simply “adding search.”

For humanities research, RAG is a form of context control.

It asks:

```text
What evidence should the model be allowed to use?
What theory should frame the interpretation?
What prior annotations should be remembered?
What sources should be excluded?
How do we know the answer is grounded?
```
