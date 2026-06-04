# Metaphor Analysis Skill — Examples

## Example Input

```text
The city was a broken mirror, reflecting every dream I had lost.
```

## Expected Output

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

## Notes

The output is structurally valid because it contains the required fields.

It still requires human review because the interpretation may be incomplete, culturally thin, or too confident.
