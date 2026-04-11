#!/usr/bin/env python3

import json
import sys


def main() -> None:
    payload = {
        "hookSpecificOutput": {
            "hookEventName": "SessionStart",
            "additionalContext": (
                "Vol I repo mode: mathematical truth lives on the live surface (`main.tex`, active inputs, dirty diff, build/test logs, compute/tests). "
                "Codex parity with `CLAUDE.md` is active here too: use repo skills under `.agents/skills/` for rectification, structural rewrite, verification, propagation, build triage, compute scaffolding, and frontier work; use hooks as guardrails, not as substitutes for proof."
            ),
        }
    }
    json.dump(payload, sys.stdout)


if __name__ == "__main__":
    main()
