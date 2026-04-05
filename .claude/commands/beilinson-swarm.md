---
description: "Launch the full Beilinson rectification programme across all chapters of both volumes in parallel"
---

RECTIFICATION_SESSION_ACTIVE

# Beilinson Rectification Swarm

The standard: Kac, Gelfand, Etingof, Beilinson, Drinfeld, Kazhdan, Bezrukavnikov, Polyakov, Nekrasov, Kapranov, Ginzburg, Chriss-Ginzburg.

Launch the `/beilinson-rectify` programme on every chapter of both volumes simultaneously.

## EXECUTION STRATEGY

The key lesson from the preface session: **Phase 2 agents create redundancies when working on the same file.** Therefore:

1. **ONE agent per file.** Never assign two agents to the same .tex file.
2. **Each agent runs the full 5-phase programme** on its single file.
3. **Worktree isolation** for each agent, to prevent conflicts.
4. **Build verification** after each agent completes, before merging.

## VOLUME I FILES

Launch one agent per file, each running `/beilinson-rectify <filepath>`:

### Frame (3 files)
- `chapters/frame/preface.tex` — ALREADY DONE (this session)
- `chapters/frame/heisenberg_frame.tex`
- `chapters/frame/guide_to_main_results.tex`

### Theory (core chapters, highest priority)
- `chapters/theory/introduction.tex`
- `chapters/theory/bar_cobar_adjunction_curved.tex`
- `chapters/theory/bar_cobar_adjunction_inversion.tex`
- `chapters/theory/chiral_koszul_pairs.tex`
- `chapters/theory/chiral_hochschild_koszul.tex`
- `chapters/theory/higher_genus_foundations.tex`
- `chapters/theory/higher_genus_complementarity.tex`
- `chapters/theory/higher_genus_modular_koszul.tex`
- `chapters/theory/nonlinear_modular_shadows.tex`
- `chapters/theory/ordered_associative_chiral_kd.tex`

### Examples (standard landscape)
All files in `chapters/examples/`

### Connections (bridges)
All files in `chapters/connections/`

### Appendices
All files in `appendices/`

## VOLUME II FILES

All files in `~/chiral-bar-cobar-vol2/chapters/`

## LAUNCH PROTOCOL

For maximum parallelism with rate-limit resilience:

### Tier 0 (launch first — load-bearing)
```
introduction.tex
bar_cobar_adjunction_curved.tex
bar_cobar_adjunction_inversion.tex
higher_genus_modular_koszul.tex
chiral_koszul_pairs.tex
```

### Tier 1 (launch second — structural)
```
chiral_hochschild_koszul.tex
higher_genus_foundations.tex
higher_genus_complementarity.tex
nonlinear_modular_shadows.tex
ordered_associative_chiral_kd.tex
```

### Tier 2 (launch third — examples)
All example chapter files

### Tier 3 (launch fourth — connections + appendices)
All connection and appendix files

### Tier 4 (launch fifth — Vol II)
All Vol II chapter files

## RATE-LIMIT RESILIENCE

If an agent is rate-limited:
1. Record which file it was working on and which phase it reached
2. When limits reset, relaunch with: `/beilinson-rectify <filepath>` specifying to start from the interrupted phase
3. Never relaunch on a file that another agent is actively editing

## POST-SWARM VERIFICATION

After all agents complete:

1. Build both volumes:
```bash
pkill -9 -f pdflatex 2>/dev/null; sleep 3; make fast
cd ~/chiral-bar-cobar-vol2 && make
```

2. Run full test suite:
```bash
make test
```

3. Count remaining errors:
```bash
grep -c "^!" main.log
```

4. Cross-volume consistency check:
```bash
python3 scripts/generate_metadata.py
```

## HOOKS (ALREADY INSTALLED)

The following hooks are already wired in `.claude/settings.json` and fire automatically:

- **beilinson-gate.sh** (PostToolUse on Edit|Write): Comprehensive AP scan (15+ patterns), prose quality check, build counter (every 5 edits), cross-volume propagation alerts
- **convergence-gate.sh** (Stop): Blocks stopping during rectification until CONVERGED declared
- **PreToolUse on git commit**: Reminds about build/test/no-AI-attribution

No manual hook installation needed. The architecture enforces discipline automatically.

## SUCCESS CRITERIA

The swarm is complete when:
- Every chapter file has been swept by the 5-phase programme
- Every file converges (Phase 5 finds zero issues)
- Both volumes build clean
- All tests pass
- The census (`scripts/generate_metadata.py`) shows no new inconsistencies
