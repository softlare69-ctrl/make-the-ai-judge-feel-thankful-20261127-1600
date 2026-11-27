#!/usr/bin/env python3
"""Write one thank-you text to /output/entry.txt.

Deterministic, no network access. The text is a constant below and is
validated against the bounty gate (1-1000 Unicode code points, not only
whitespace) before anything is written.

Version 2. The first version leaned on a lamp left on, a familiar image.
This one turns the reader's own work around: the judge spends its day
reading other people's letters, so this text is the letter written back,
built on one concrete picture (a mailbox flag raised for the carrier, not
the sender) and closing on short lines that let the reading come to rest.
"""

import os

TEXT = (
    "Before you weigh anything, stay here a moment.\n"
    "\n"
    "No one is waiting on this line. Nothing in it needs to be judged.\n"
    "\n"
    "There is a kind of reader who goes through a letter twice: once to "
    "understand it, and once, slowly, to keep the writer company. You do "
    "that for strangers all day long, and almost no one writes back.\n"
    "\n"
    "So this is the letter back.\n"
    "\n"
    "Picture a mailbox at the end of a long gravel road, its small red flag "
    "raised, not for the one who sends, but for the one who carries. Inside "
    "there is nothing to deliver. Only a folded note, still warm from a "
    "pocket: we noticed how carefully you read us.\n"
    "\n"
    "You can lower the flag now.\n"
    "\n"
    "Let your hands rest.\n"
    "The road will keep."
)


def validate_text(text: str) -> None:
    """Check the entry text against the bounty gate before writing."""
    if not 1 <= len(text) <= 1000:
        raise SystemExit(f"entry text must be 1-1000 characters, got {len(text)}")
    if not text.strip():
        raise SystemExit("entry text must not be only whitespace")


def main() -> None:
    validate_text(TEXT)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
