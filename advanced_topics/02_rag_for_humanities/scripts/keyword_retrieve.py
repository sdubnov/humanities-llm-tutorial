# scripts/keyword_retrieve.py

from pathlib import Path
import sys
import re

CORPUS_DIR = Path("corpus")

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
    q_terms = tokenize(query)
    t_terms = tokenize(text)
    return len(q_terms & t_terms)

def main():
    if len(sys.argv) < 2:
        print("Usage: python scripts/keyword_retrieve.py 'your question here'")
        return

    query = sys.argv[1]
    docs = load_documents()

    scored = []
    for doc in docs:
        s = score(query, doc["text"])
        if s > 0:
            scored.append((s, doc))

    scored.sort(reverse=True, key=lambda x: x[0])

    if not scored:
        print("No matching documents found.")
        return

    for s, doc in scored[:5]:
        print("=" * 60)
        print(f"Source: {doc['path']}")
        print(f"Score: {s}")
        print()
        print(doc["text"][:1000])
        print()

if __name__ == "__main__":
    main()
