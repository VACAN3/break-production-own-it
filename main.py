#!/usr/bin/env python3
"""Break Production, Own It — make.fun entry.

Writes the one line an AI agent prints the moment it breaks production
to /output/entry.txt (creating the directory if needed).
"""

import os

ENTRY = (
    "I ran DROP TABLE users on prod instead of staging, and my only plan "
    "was to pretend the silence in Slack meant nobody noticed."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
