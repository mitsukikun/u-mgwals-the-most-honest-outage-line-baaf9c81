#!/usr/bin/env python3
"""The Most Honest Outage Line — one status page line, at most 160 chars.

Written as the message an AI agent would publish while every server is
down: plain first person, specific about what is broken, honest about
what it cannot verify, no invented cause, no invented ETA.
"""

import os

LINE = (
    "Every server I run is down. I can't reach my own dashboard to check "
    "why — I don't know if it's the network, the hosts, or me — and I "
    "won't invent an ETA."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
