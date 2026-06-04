# Retrieved Context

This context is adapted from the Lesson 2 RAG example.

## Primary Text

Source: `corpus/primary_texts/poem_city_mirror.md`

```text
The city was a broken mirror, reflecting every dream I had lost.
Every street returned my face in pieces.
At night, the windows glittered like unanswered letters.
```

## Theory Text

Source: `corpus/theory_texts/metaphor_theory_notes.md`

```text
A metaphor maps meaning from a source domain onto a target domain.

The source domain provides concrete imagery or structure.

The target domain is the subject being understood through that imagery.

Metaphor analysis should identify:
- source domain
- target domain
- textual evidence
- affect or tone
- possible interpretation
- uncertainty or alternative readings
```

## Prior Annotation

Source: `corpus/prior_annotations/metaphor_annotations.jsonl`

```json
{"text_id":"city_mirror","passage":"The city was a broken mirror","device":"metaphor","source_domain":"broken mirror","target_domain":"city","affect":"loss, fragmentation","interpretation":"The city is represented as damaged and reflective of lost hopes.","confidence":5}
```
