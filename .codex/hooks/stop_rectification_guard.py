#!/usr/bin/env python3

import json
import os
import re
import sys


def recent_text(path):
    if not path or not os.path.exists(path):
        return ""
    with open(path, "rb") as fh:
        fh.seek(0, os.SEEK_END)
        size = fh.tell()
        fh.seek(max(0, size - 12000))
        return fh.read().decode("utf-8", errors="ignore")


def main() -> None:
    data = json.load(sys.stdin)

    if data.get("stop_hook_active"):
        return

    last_message = (data.get("last_assistant_message") or "").strip()
    transcript = recent_text(data.get("transcript_path"))
    scope = "\n".join([last_message, transcript]).lower()

    rectification_markers = [
        r"\bbeilinson\b",
        r"\brectif",
        r"\bfortif",
        r"\baudit\b",
        r"\bred[- ]team\b",
        r"\bdeep-beilinson-audit\b",
        r"\bbeilinson-rectify\b",
        r"\bmulti-path-verify\b",
        r"\bclaim-surface-sync\b",
    ]

    if not any(re.search(pattern, scope) for pattern in rectification_markers):
        return

    lower_last = last_message.lower()
    complete = (
        "converged" in lower_last
        or "blocked" in lower_last
        or (
            ("proved internally" in lower_last or "proved here" in lower_last)
            and ("compute-backed" in lower_last or "supported computationally" in lower_last)
            and (
                "conditional" in lower_last
                or "conjectural" in lower_last
                or "open" in lower_last
            )
        )
    )

    if complete:
        return

    payload = {
        "decision": "block",
        "reason": (
            "Before stopping, make the rectification close-out explicit: state convergence or blocked status, "
            "what verification ran, what is proved internally, what is only compute-backed, and what remains conditional or open."
        ),
    }
    json.dump(payload, sys.stdout)


if __name__ == "__main__":
    main()
