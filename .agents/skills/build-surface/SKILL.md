---
name: build-surface
description: Use when LaTeX builds, build logs, warning classification, metadata regeneration, or targeted pytest runs determine whether a change is actually verified. This is the Codex-native equivalent of `/build` from `CLAUDE.md`.
---

# Build Surface

Build output is evidence only after the surface is stable enough to trust.

## Standard prelude

```bash
pkill -9 -f pdflatex 2>/dev/null || true
sleep 2
```

Then choose the narrowest command that can falsify the change:

- `make fast`
- `make`
- targeted `python3 -m pytest ...`
- `python3 scripts/generate_metadata.py`
- direct log inspection

## Classification rules

- Fatal LaTeX error: actionable immediately.
- Persistent undefined reference after stable rerun: likely real.
- Pass-1 warning on unstable aux surface: not yet a finding.
- Interrupted or concurrent build: restabilize before trusting counts.
- Test mismatch: treat as a mathematics bug or convention bug until proved otherwise.

## Workflow

1. Stabilize the build surface.
2. Run the narrowest falsifying build/test/metadata command.
3. Classify failures into:
   manuscript error,
   compute error,
   convention mismatch,
   stale artifact noise,
   expected cross-volume warning.
4. Fix or quarantine only after classification.
