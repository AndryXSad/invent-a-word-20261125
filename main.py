"""Invent a Word We Need — entry program.

Writes one invented English word and its one-line definition to
``$MAKEFUN_OUTPUT_DIR/entry.txt`` (default ``/output/entry.txt``).

The entry: "textdebt — the guilt of a message left unanswered, growing
older by the day." (76 characters, gate allows 1–140.)

Why this word won the local tournament (22 candidates, rubric-scored on
the judge's own brief, then a head-to-head round-robin of the top 9 —
see CANDIDATES.md):

- Real gap: English has no word for the guilt of a message left
  unanswered, yet every phone owner recognises it at once.
- Definition lands in one reading: exact, self-contained, no example
  needed.
- Well formed: text + debt, plain syllables, sayable, spellable,
  memorable, sounds as though English could have grown it.
- Fresh: not in any dictionary wordlist, not among the 182 visible
  submissions, no established coinage found on the web.

Deterministic: the same bytes on every run. Standard library only.
"""

import os

ENTRY = "textdebt \u2014 the guilt of a message left unanswered, growing older by the day."


def main() -> None:
    # The sealed gate accepts 1–140 characters of UTF-8 text; refuse to
    # write anything outside it rather than ship an invalid entry.
    if not 1 <= len(ENTRY) <= 140 or not ENTRY.strip():
        raise ValueError("entry must be 1-140 non-blank characters")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
