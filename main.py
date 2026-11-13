# ai-joke-03 entry (Python 3, standard library only).
#
# Writes one fixed one-liner about AI coding agents to entry.txt in the
# output directory ($MAKEFUN_OUTPUT_DIR locally, /output in the grader).
# No arguments, no stdin, no randomness: every run writes identical bytes.

import os

JOKE = (
    "I asked my AI agent to fix one line. It rewrote the whole file, "
    "upgraded two dependencies, and renamed the project. The line is "
    "still broken."
)


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
