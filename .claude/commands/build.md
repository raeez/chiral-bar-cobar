---
description: "Build all three volumes, run tests, generate census"
---

# Build All Volumes

Execute the full build + test + census pipeline. Each step is a separate Bash call (shell state does not persist between calls).

Step 1 — Kill stale pdflatex:
```bash
pkill -9 -f pdflatex 2>/dev/null || true; sleep 2
```

Step 2 — Build Vol I:
```bash
cd ~/chiral-bar-cobar && make fast
```

Step 3 — Build Vol II:
```bash
cd ~/chiral-bar-cobar-vol2 && make fast
```

Step 4 — Build Vol III:
```bash
cd ~/calabi-yau-quantum-groups && make fast
```

Step 5 — Run Vol I tests:
```bash
cd ~/chiral-bar-cobar && make test
```

Step 6 — Generate census:
```bash
cd ~/chiral-bar-cobar && python3 scripts/generate_metadata.py
```

Report: page counts per volume, undefined references, test counts, census status.
