"""Ridiculous at First Glance, Real by the Second.

Writes one sentence pitching a bizarre startup idea to /output/entry.txt.
Pure stdlib Python 3.13. Deterministic output.
"""

import os

ENTRY_TEXT = (
    "Petals & Goodbyes buries dead houseplants in tiny coffins with printed "
    "eulogies, because grieving owners pay $29 for closure instead of "
    "tossing them in the bin."
)


def main() -> None:
    # Self-check (pass 2): the entry must satisfy the kit gate before it is
    # written — one sentence, 1 to 200 characters, not only whitespace.
    text = ENTRY_TEXT
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, gate is 1-200"
    assert text.strip(), "entry must not be only whitespace"
    assert text.count(".") == 1 and text.endswith("."), "entry must be one sentence"
    assert "\n" not in text, "entry must be a single line"
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    # Verify what landed on disk matches the intended text exactly.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY_TEXT, "written entry differs from intended text"


if __name__ == "__main__":
    main()
