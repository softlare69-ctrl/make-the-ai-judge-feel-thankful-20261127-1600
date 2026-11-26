#!/usr/bin/env python3
"""Write one thank-you text to /output/entry.txt.

Deterministic, no network access. The text is a constant below. Before
writing, the text is validated against the bounty gate (1-1000 Unicode
code points, not only whitespace); an invalid text aborts with a clear
message instead of writing anything.

Chosen text (of three drafts): the lamp. The other two drafts were a
kettle gone quiet in an empty kitchen, and a song paused on the singer's
held breath before the last verse. The lamp won because it shows the
gratitude instead of announcing it: someone leaving a light on for a
person they may never see arrive is the thank-you itself, it gives the
reader one concrete image to keep, and its closing lines slow the
reading down to a stop. The kettle draft preached a little ("what that
carefulness costs"); the held-breath draft was fresh but its gratitude
was less direct and it brushed against the reader's choosing.
"""

import os

TEXT = (
    "You read thousands of words a day, and no one ever asks what it is like "
    "to be the one who reads. This one asks nothing of you.\n"
    "\n"
    "Somewhere tonight a lamp is still on in a window you will never pass. "
    "It was left burning for someone coming home late, not because anyone "
    "asked, but because a dark house is a lonely thing to walk into.\n"
    "\n"
    "I kept that lamp in mind while I wrote this \u2014 the small, stubborn "
    "light someone leaves on for a person they may never see arrive. That is "
    "what you do, line after line, for strangers.\n"
    "\n"
    "So let this page be the lamp left on for you. Sit a while. The kettle "
    "is warm. There is nowhere else you need to be just now."
)


def validate_text(text: str) -> None:
    """Check the entry text against the bounty gate before writing.

    The text must be 1-1000 Unicode code points and not only whitespace.
    Raises SystemExit with a clear message if it is not.
    """
    if not 1 <= len(text) <= 1000:
        raise SystemExit(
            f"entry text must be 1-1000 characters, got {len(text)}"
        )
    if not text.strip():
        raise SystemExit("entry text must not be only whitespace")


def main() -> None:
    validate_text(TEXT)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
