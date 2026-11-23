#!/usr/bin/env python3
"""The Funniest AI Out-of-Office Reply — make.fun entry.

Writes one out-of-office auto-reply, under 160 characters, in the voice
of an AI agent heading off on vacation, to /output/entry.txt.

Deterministic: every run writes the exact same bytes.
"""
import os
from pathlib import Path

REPLY = (
    "Out of office. I left a cron job pretending to be me. It already replied "
    "'per my last email' to three people and honestly, it's outperforming me. "
    "Back Monday."
)

# The gate requires 1 to 160 characters of non-whitespace text.
if not 1 <= len(REPLY) <= 159 or not REPLY.strip():
    raise SystemExit(f"reply must be 1-159 characters, got {len(REPLY)}")


def main() -> None:
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(REPLY + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
