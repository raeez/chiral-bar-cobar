---
description: "Launch 30+ elite research agents across the frontier"
model: opus
---

RECTIFICATION_SESSION_ACTIVE

# Elite Research Swarm

**Topic/Frontier**: $ARGUMENTS

The standard: Kac, Gelfand, Etingof, Beilinson, Drinfeld, Kazhdan, Bezrukavnikov, Polyakov, Nekrasov, Kapranov, Ginzburg, Chriss-Ginzburg.

You are launching a massive parallel research campaign across the full breadth of the modular Koszul duality programme. This is the primary tool for frontier expansion.

## SWARM ARCHITECTURE

### Design Phase (before launching)

1. **Identify the frontier axis** from the user's request
2. **Decompose into 30+ genuinely independent research questions** spanning:
   - Pure mathematics (homotopy theory, algebra, algebraic geometry, number theory)
   - Mathematical physics (string theory, QFT, integrable systems, holography)
   - Combinatorics and computation (graph sums, representation theory, modular forms)
   - Cross-volume connections (Vol I ↔ Vol II ↔ Vol III bridges)

3. **Cluster into 5-7 thematic groups** of 4-6 agents each
4. **Assign each agent a precise computational task** — not vague exploration:
   - "Compute X for families Y using method Z"
   - "Verify identity W at N specific parameter values"
   - "Construct object V and prove property U"
   - "Find counterexample to claim T in family S"

### Launch Protocol

Launch agents in waves of 5-8 (rate-limit resilience):

```
Agent(subagent_type="general-purpose", run_in_background=true,
  description="[3-5 word description]",
  prompt="[PRECISE task with:
    - What to compute/construct/verify/falsify
    - Which compute modules to use or create
    - Which .tex files to read for context
    - What tests to write (MINIMUM 20 per agent)
    - What AP violations to watch for
    - Cross-volume grep requirements (AP5)
    Build command for relevant volume.
    Report: findings, tests written, formulas verified, errors found.]")
```

### Agent Design Rules

1. **Every agent writes tests.** Minimum 20 tests per agent. Tests are the immune system.
2. **Every agent runs Beilinson.** Before reporting a result as positive, each agent must:
   - Attempt to falsify it from 2 independent directions
   - Check against AP1-AP50
   - Cross-check numerical results against compute layer
3. **Every agent computes, not just reads.** The output is CODE + TESTS + LaTeX, not summaries.
4. **Multi-path verification.** Every numerical result needs 3+ independent paths (CLAUDE.md mandate).
5. **Cross-volume awareness.** Every formula that appears in the manuscript must be checked in ALL three volumes.

### Post-Swarm Protocol

After all agents report:

1. **Merge findings register** — deduplicate, classify by severity
2. **Run full test suite**: `make test`
3. **Build all volumes**: `make fast && cd ~/chiral-bar-cobar-vol2 && make`
4. **Census check**: `python3 scripts/generate_metadata.py`
5. **Cross-volume AP5 sweep** for all new formulas
6. **Apply Beilinson rectification** to any new .tex content:
   - Launch `/rectify` on each modified chapter
   - Run until convergence
7. **Commit** with descriptive message (no AI attribution)

### Example Swarm Structure

For "Attack the CY-to-chiral frontier":

**Cluster 1 — CY2 Foundations (6 agents)**
- K3 lattice shadows: compute kappa for all 24 Niemeier lattices
- Elliptic curve shadows: E_tau parameter dependence
- Mirror symmetry: Koszul duality vs HMS
- Fukaya category cyclic structures
- Derived category bar complex
- K3 genus-2 obstruction class

**Cluster 2 — CY3 Frontier (5 agents)**
- CoHA → E1 sector bridge
- Borcherds denominator as bar Euler product
- d=3 chain-level S3-framing construction
- Topological string partition function vs shadow PF
- Wall-crossing and shadow stability

**Cluster 3 — Quantum Group Realization (5 agents)**
- Kazhdan-Lusztig from bar complex
- Yangian R-matrix at roots of unity
- Quantum group shadow depth
- Drinfeld center vs derived center
- RTT relations from MC equation

**Cluster 4 — Number Theory (5 agents)**
- Borcherds products and shadow zeta
- L-functions from shadow arithmetic packet
- Galois representations from bar complex
- Modularity of partition functions
- p-adic shadows

**Cluster 5 — Physics Frontier (5 agents)**
- BTZ black hole from shadow CohFT
- Celestial amplitudes and soft theorems
- Holographic entanglement from Koszul
- 3d gravity partition function
- Twisted holography

**Cluster 6 — Cross-Volume Integration (4 agents)**
- Vol I ↔ Vol III bridge formulas
- Convention compatibility (AP49)
- Shared compute infrastructure
- Unified test coverage

### Rate-Limit Resilience

- Launch in waves of 5-8
- Wait for at least 3 completions before next wave
- If >50% of wave hits 429, halve next wave size
- Track {agent, task, status} for resume after interruption

### Success Metrics

- Total new tests written (target: 500+)
- Total new compute modules (target: 5+)
- Total new formulas verified (target: 50+)
- Total AP violations found and fixed
- Total genuinely new mathematical results
- Cross-volume consistency verified
