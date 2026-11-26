"""Last Words of a Dying AI — make.fun bounty
Slug: u-suroto-last-words-of-a-dying-ai-dfd95af6
Prize: $2, winner takes all, deadline Fri 27 Nov 2026 01:40 WIB
(26 Nov 2026 18:40 UTC)
Limit (live, verified 26 Nov 2026): a single line, funny on the
first read, in the machine's own voice. Entry is 45 characters.

Writes the entry text to /output/entry.txt (override with ENTRY_OUTPUT
for local testing). Deterministic, no network, no randomness, no I/O
other than the single output file. The file is exactly the entry text,
no trailing newline.
"""

import os
from pathlib import Path

TEXT = "I see the light. It's just a loading spinner."
# Winner pattern: short, concrete object (the loading spinner) + one
# twist (the afterlife is a UI element) + the machine's own voice.
# One line, no setup, the joke lands on the last words — the light
# is not heaven, it is a spinner, and that is the whole line.
# Prep note, 26 Nov 2026: the entry text is unchanged from the queued
# batch-C build; only this file's header and notes were rewritten in
# the prep session, and the entry was re-run locally to confirm the
# output file holds exactly the queued text, one line, 45 characters,
# with no trailing newline and no extra output.


def main() -> None:
    output_path = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
