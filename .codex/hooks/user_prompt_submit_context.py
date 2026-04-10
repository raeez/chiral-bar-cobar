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

    if re.search(r"\b(introduction|preface|chapter opening|opening section|rewrite this chapter|restructure this chapter|chriss[- ]ginzburg)\b", lower):
        notes.append(
            "This is a structural rewrite task. Load `$chriss-ginzburg-rectify`, use the convergent writing loop, and re-audit until the surface is structurally stable."
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

    if re.search(r"\b(propagat|cross[- ]volume|grep all three volumes|update all occurrences|stale part reference)\b", lower):
        notes.append(
            "This is a propagation task. Load `$cross-volume-propagation` and verify the same object and convention before editing matching text across volumes."
        )

    if re.search(r"\b(build|pdflatex|latex|make fast|make test|pytest|warning|log file|compile)\b", lower):
        notes.append(
            "This task depends on executable verification. Load `$build-surface`, stabilize the build surface first, and classify failures before patching."
        )

    if re.search(r"\b(scaffold|compute engine|new engine|new test|oracle|hardcoded expected value)\b", lower):
        notes.append(
            "This is a compute-layer task. Load `$compute-engine-scaffold` and keep engine logic independent from test oracles."
        )

    if re.search(r"\b(frontier|research program|research programme|new theorem|conjecture|architecture|synthesis|swarm)\b", lower):
        notes.append(
            "This is frontier work. Load `$frontier-research`, separate proved core from conditional and conjectural layers, and only delegate if the user explicitly authorizes it."
        )

    if re.search(r"\b(r[- ]matrix|\\kappa|kappa|bar complex|label|cross-volume formula|scope quantifier|differential form)\b", lower):
        notes.append(
            "High-risk edit family detected. Apply the Pre-Edit Verification Protocol from `CLAUDE.md` before patching by pattern."
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
