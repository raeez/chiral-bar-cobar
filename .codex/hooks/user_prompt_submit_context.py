#!/usr/bin/env python3

import json
import re
import sys


def main() -> None:
    data = json.load(sys.stdin)
    prompt = (data.get("prompt") or "").strip()
    lower = prompt.lower()
    notes = []

    if re.search(r"\b(audit|red[- ]team|falsif|pressure[- ]test|claim status|prove here|dependency attack)\b", lower):
        notes.append(
            "This is an adversarial verification task. Load `$deep-beilinson-audit`, lead with findings, and force an exact proved/computational/conditional split."
        )

    if re.search(r"\b(rectif|fortif|rewrite|tighten|repair the chapter|repair the proof|make this rigorous)\b", lower):
        notes.append(
            "This is a rectification task. Load `$beilinson-rectify`, fix structure before prose polish, and iterate until the touched surface converges or the blocker is explicit."
        )

    if re.search(r"\b(verify|check|formula|kappa|lambda_g|invariant|numerical|compute-backed)\b", lower):
        notes.append(
            "For claim or formula verification, load `$multi-path-verify` and use at least three independent paths when feasible."
        )

    if re.search(r"\b(concordance|theorem registry|label status|metadata|claimstatus|status drift)\b", lower):
        notes.append(
            "Status-bearing edits should load `$claim-surface-sync` so theorem text, concordance, and metadata do not drift apart."
        )

    if re.search(r"\b(commit|check in|git)\b", lower):
        notes.append(
            "If the task reaches commit territory, build/test first and do not add AI attribution."
        )

    if not notes:
        return

    payload = {
        "hookSpecificOutput": {
            "hookEventName": "UserPromptSubmit",
            "additionalContext": "\n".join(notes),
        }
    }
    json.dump(payload, sys.stdout)


if __name__ == "__main__":
    main()

