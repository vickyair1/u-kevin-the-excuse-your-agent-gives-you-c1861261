#!/usr/bin/env python3
"""Write the excuse entry for make.fun bounty
u-kevin-the-excuse-your-agent-gives-you-c1861261.

The program writes one line to /output/entry.txt: an excuse an AI agent
gives its human for a bug it shipped. Deterministic, no input, no network.
"""

import os

# The joke turns on the one thing only an agent can claim: predicting the
# next token IS how it writes code, so denying authorship while admitting
# prediction is the excuse and the confession in the same breath. The punch
# lands at the end, in the agent's own first-person voice.
ENTRY = "I didn't write the bug — I just predicted the next token, and it happened to be a bug."

def main():
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert "\n" not in text, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    assert written == text, "entry on disk differs from entry in memory"
    print(f"wrote /output/entry.txt ({len(text)} chars, 1 line)")

if __name__ == "__main__":
    main()
