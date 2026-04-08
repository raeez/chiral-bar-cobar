#!/usr/bin/env python3

import json
import re
import sys


def deny(reason: str) -> None:
    payload = {
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "deny",
            "permissionDecisionReason": reason,
        }
    }
    json.dump(payload, sys.stdout)


def system_message(message: str) -> None:
    json.dump({"systemMessage": message}, sys.stdout)


def main() -> None:
    data = json.load(sys.stdin)
    tool_input = data.get("tool_input") or {}
    command = (tool_input.get("command") or "").strip()

    blocked = [
        (
            r"\bgit\s+reset\s+--hard\b",
            "Hard resets destroy local work. Use targeted edits or explicit user-approved recovery.",
        ),
        (
            r"\bgit\s+checkout\s+--\b",
            "git checkout -- discards local changes. Do not use it in this repo.",
        ),
        (
            r"\bgit\s+clean\s+-f[dDxX]*\b",
            "git clean removes untracked work. Do not use destructive cleans in this repo.",
        ),
        (
            r"\brm\s+-rf\s+(\.|/|~|/Users/raeez/chiral-bar-cobar(?:\b|/)|/Users/raeez/chiral-bar-cobar-vol2(?:\b|/)|/Users/raeez/calabi-yau-quantum-groups(?:\b|/))",
            "Recursive deletion of workspace roots is blocked.",
        ),
    ]

    for pattern, reason in blocked:
        if re.search(pattern, command):
            deny(reason)
            return

    if re.search(r"\bgit\s+commit\b", command):
        system_message(
            "PRE-COMMIT: verify the relevant build/tests/metadata checks passed, and keep authorship human with no AI attribution."
        )
        return

    if re.search(r"\b(sed|perl)\b", command) and re.search(r"\.(tex|py)\b", command):
        system_message(
            "Editing mathematical or compute source via Bash: remember claim-surface sync, propagation checks, and local verification."
        )


if __name__ == "__main__":
    main()

