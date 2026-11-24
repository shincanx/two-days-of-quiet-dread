"""Two Days of Quiet Dread — one-line code review comment.

Writes a single line (<=140 chars) approving a pull request while
carrying quiet existential dread, to /output/entry.txt (and stdout).
Deterministic: the comment is a fixed string literal.
"""

import os

COMMENT = "Approved. It compiles, it passes, and one day a stranger will open this file like a time capsule and wonder who we were."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(COMMENT)
    print(COMMENT)


if __name__ == "__main__":
    main()
