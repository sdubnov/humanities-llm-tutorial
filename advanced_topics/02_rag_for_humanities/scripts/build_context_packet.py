# scripts/build_context_packet.py

from pathlib import Path
import sys
import re

CORPUS_DIR = Path("corpus")
OUTPUT_DIR = Path("outputs")
OUTPUT_DIR.mkdir(exist_ok=True)

def tokenize(text):
    return set(re.findall(r"\b\w+\b", text.lower()))

def load_documents():
    docs = []
    for path in CORPUS_DIR.rglob("*"):
        if path.is_file() and path.suffix in [".md", ".txt", ".jsonl"]:
            text = path.read_text(encoding="utf-8")
            docs.append({
                "path": str(path),
                "text": text
            })
    return docs

def score(query, text):
    return len(tokenize(query) & tokenize(text))

def main():
    if len(sys.argv) < 2:
        print("Usage: python scripts/build_context_packet.py 'your question here'")
        return

    query = sys.argv[1]
    docs = load_documents()

    scored = [
        (score(query, doc["text"]), doc)
        for doc in docs
    ]
    scored = [(s, d) for s, d in scored if s > 0]
    scored.sort(reverse=True, key=lambda x: x[0])

    top = scored[:4]

    if not top:
        print("No matching documents found. Try a different query.")
        return

    lines = []
    lines.append("# RAG Context Packet")
    lines.append("")
    lines.append("## Research Question")
    lines.append("")
    lines.append(query)
    lines.append("")
    lines.append("## Retrieved Context")
    lines.append("")

    for i, (s, doc) in enumerate(top, start=1):
        lines.append(f"### Passage {i}")
        lines.append("")
        lines.append(f"Source: `{doc['path']}`")
        lines.append("")
        lines.append(f"Retrieval score: {s}")
        lines.append("")
        lines.append("```text")
        lines.append(doc["text"][:1200])
        lines.append("```")
        lines.append("")

    lines.append("## Prompt")
    lines.append("")
    lines.append("Answer the research question using only the retrieved context above.")
    lines.append("")
    lines.append("Requirements:")
    lines.append("- cite the source path for each claim")
    lines.append("- distinguish textual evidence from interpretation")
    lines.append("- state uncertainty")
    lines.append("- do not use outside information")
    lines.append("")

    output_path = OUTPUT_DIR / "rag_context_packet.md"
    output_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {output_path}")

if __name__ == "__main__":
    main()
