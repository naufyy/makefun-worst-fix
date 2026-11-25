#!/usr/bin/env python3
"""Entry for Worst Fix Ever: Funniest Commit Message.

Writes the winning one-line commit message to /output/entry.txt.
"""
import os

TEXT = "fix: patch the memory leak by restarting the server every 47 seconds"

def main():
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 100 characters.
    assert 1 <= len(TEXT) <= 100, f"entry length {len(TEXT)} outside 1..100"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)

if __name__ == "__main__":
    main()
