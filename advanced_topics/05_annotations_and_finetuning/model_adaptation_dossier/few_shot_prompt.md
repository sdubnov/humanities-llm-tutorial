# Few-Shot Prompt for Metaphor Annotation

You annotate metaphors in humanities texts.

Return JSON with:

- text_id
- passage
- device
- evidence
- source_domain
- target_domain
- affect
- interpretation
- alternative_reading
- confidence
- uncertainty_note
- review_status

Rules:

- Use exact evidence.
- Distinguish evidence from interpretation.
- Preserve ambiguity.
- Do not invent historical, cultural, or biographical context.

## Example 1

Input:

```text
The city was a broken mirror, reflecting every dream I had lost.
```

Output:

```json
{
  "text_id": "city_mirror",
  "passage": "The city was a broken mirror, reflecting every dream I had lost.",
  "device": "metaphor",
  "evidence": "The city was a broken mirror",
  "source_domain": "broken mirror",
  "target_domain": "city",
  "affect": "loss, fragmentation",
  "interpretation": "The city is represented as damaged and reflective of lost hopes.",
  "alternative_reading": "The mirror may also suggest self-recognition or distorted memory.",
  "confidence": 4,
  "uncertainty_note": "The metaphor supports loss and fragmentation, but the balance between city, memory, and self-image remains uncertain.",
  "review_status": "human_reviewed"
}
```
