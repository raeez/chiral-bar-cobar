# Kickstart Prompt v2 — Beilinson-Filtered Strategic Overlay

## How to Use

Copy the text between === markers as your first message in a fresh Claude Code session.

## ===BEGIN PROMPT===

Read compute/audit/session_state_2026_04_01_final.md for the previous session's state (20 manuscript fixes, 2669+ new tests across 25 compute modules, 25 compute agents all completed successfully).

**This prompt overlays a deep Beilinson filter on the previous kickstart (compute/audit/kickstart_prompt.md). The filter was derived from reading all raeeznotes 98-122 (25 notes, ~1.5MB), the rn105-112 master catalogue + Beilinson audit, the rn114-119 battle catalogue, and the session state. Read those files if you need the raw data. What follows is the distilled strategic picture.**

---

## THE META-DIAGNOSIS

**The programme has built an extraordinarily powerful algebraic machine but has never turned it on.**

At genus ≥ 1, every numerical verification is tautological. Θ_A has never been explicitly constructed for any specific algebra beyond the scalar level κ. The fix is not more invariants or more shadow coefficients. The fix is to close ONE nonlinear local bridge and compute something nobody else can compute.

The programme has been **globalizing before closing the local nonlinear bridge from affine/Kac-Moody data to gravity data**. Too much energy has gone into secondary invariants, complementarity potentials, and shadow packages before the first nonlinear comparison theorem was finished.

**What is going right**: The Beilinson pass is right. The local object should be open/categorical. The bar-vs-center split is right. The dg-shifted-Yangian viewpoint is right. The PVA-to-3d-HT bridge is right. The line-operator category is right.

**What is going wrong**: The programme tries to produce a strict reduced gravity coproduct when the reduced object is an A∞ coalgebra morphism. It tries to globalize before the local bridge is closed. It recycles existing manuscript content as "discoveries" (70% of rn105-112 Cluster A rediscovers what's already proved in the .tex source — classic AP2 at scale).

---

## FIVE FALSE IDEAS TO DISMISS (from rn122 Beilinson pass)

These are the ideas that must be actively quarantined. Every agent session should check that it is not re-introducing them:

1. **"The entire local open/closed package is already proved."** It is NOT. The correct formulation: the programme has identified the correct local candidate theorem U(A) = (C*_ch(A,A), A). The Swiss-cheese theorem, derived center, and annulus trace ARE proved locally. But the full modular cooperad package around Θ_C is still a PROGRAMME, not a theorem stack.

2. **"Bar = bulk."** FALSE. Bar classifies twisting morphisms (couplings). Bulk = derived center = C*_ch(A_b, A_b). These are different functors producing different objects. The corrected slogan: bar/cobar = couplings, Hochschild cochains = bulk, Θ_A = modular completion.

3. **"The global open sector lives on an ordinary curve."** It does NOT. It lives on the real-oriented blowup of a tangential log curve (X, D, τ). This is not decorative — it is necessary for the boundary intervals where open insertions live.

4. **"Modularity is a property of the closed algebra alone."** It is NOT. Modularity = trace + clutching on the open sector. The annulus is HH_*(C_op), not primitive closed-string data.

5. **"The dg-shifted Yangian is a universal theorem."** It is a CONJECTURE in general perturbative 3d HT QFT (Dimofte-Niu-Py). Do not promote from conjectural infrastructure to established theorem.

---

## THE SINGLE HIGHEST-LEVERAGE MOVE

**Prove that principal DS reduction transfers the affine dg-shifted-Yangian data (m, r, Δ) to a Virasoro dg-shifted-Yangian by explicit homological perturbation.**

This one theorem simultaneously:
- Gives the first genuinely nonlinear local quantum-gravity example
- Tests the correct primitive object rather than a chart
- Forces the programme to distinguish strict coproduct from higher coproduct components
- Bridges the 2025-2026 HT line-operator literature with the gravity ambitions
- Provides the model calculation from which W_N, higher-spin gravity, and modular globalization should proceed

**Status**: The DS-HPL Transfer Theorem (thm:ds-hpl-transfer) is WRITTEN in 3d_gravity.tex with full proof and honest gaps remark. The gravitational coproduct Δ_z^grav is proved STRICTLY PRIMITIVE at all arities (ghost-number obstruction kills every HPL tree correction). What remains: the full 3-4 page exposition expansion, adversarial verification at all arities, W_N extension analysis, and the standalone paper extraction.

---

## FOUR-STAGE PROGRAMME ARCHITECTURE (dependency-ordered)

Each stage depends on its predecessor. Never discuss stage k before establishing stage k-1.

**Stage 1: LOCAL ONE-COLOR THEOREM** (the true bottleneck)
Define A∞-chiral algebra cleanly; prove braces on C*_ch(A,A); prove the local universal acting-bulk theorem in the minimal Swiss-cheese setting. This is WHERE the programme becomes real mathematics or fails fast.

**Stage 2: OPEN PRIMITIVE**
Replace every "boundary algebra" statement by the Morita-invariant C_op statement, with A_b only a local presentation. Prove Morita invariance in the exact formalism used.

**Stage 3: GLOBALIZE** (only after Stages 1-2 are solid)
Move to tangential log curves, real-oriented blowups, mixed open/closed Ran spaces. Keep the globalization statement modest until descent and excision technology is fully written.

**Stage 4: MODULARIZE LAST**
Introduce Θ_C, traces, annulus/Hochschild chains, clutching, quartic resonance classes only when the local and global open theory is stable. Otherwise the programme produces elegant names faster than reliable mathematics.

---

## BEILINSON FILTER ON rn98-122: WHAT SURVIVES

### Genuine Gold (install or expand)

| Source | Content | Target | Priority |
|--------|---------|--------|----------|
| rn105-112 B.1-B.5 | Connected Dirichlet-sewing lift S_A(u), Euler product, Miura defect D_N(q) | arithmetic_shadows.tex | HIGH |
| rn105-112 G.1-G.3 | Canonical cyclotomic boundary chart from root stacks | new frontier section | HIGH |
| rn105-112 C.1 | Hankel/Schur complement extraction of quartic contact | higher_genus_modular_koszul.tex | MEDIUM |
| rn105-112 D.3 | Three-gap analysis (honest assessment of what programme cannot do) | concordance.tex | HIGH |
| rn105-112 E.1-E.3 | Arithmetic packet connection completion | arithmetic_shadows.tex | MEDIUM |
| rn105-112 K.1-K.2 | Beilinson discard criteria + killed ideas | concordance.tex | HIGH |
| rn114 Item 11 | YBE ≠ arity-3 MC (FALSE as stated; correct relationship documented) | rem:arity3-vs-cybe (DONE) | DONE |
| rn115 Item 17 | r(z) = KD inverse named theorem | formal statement needed | HIGH |
| rn115 Item 21 | DS as functor on primitive triples | new proposition | MEDIUM |
| rn116 Item 12 | Restricted DK-5 conjecture | formal statement needed | HIGH |
| rn116 Item 13 | Four-test boundary of control | exposition needed | HIGH |
| rn116 Item 14 | Two orthogonal axes | exposition needed | HIGH |
| rn118/120 | DS-HPL Transfer Theorem + explicit chain-level SDR | thm:ds-hpl-transfer (WRITTEN) | CRITICAL |
| rn120 | Gravitational coproduct primitivity | prop:coproduct-arity2-vanishing (WRITTEN) | CRITICAL |
| rn121 | 100 things wrong (operational audit checklist) | audit use | HIGH |
| rn122 | Five worked examples (CS, gravity, TH, M2, M5) with explicit primitive packages | Vol II chapters | HIGH |
| rn122 | Actual primitive construction (open factorization dg-category) | Vol II foundations | MEDIUM |
| rn98-99 | Prime-locality gap: Hecke defect δ_p^Hecke(A), Route C (MC rigidity + character determination) | arithmetic_shadows.tex, concordance.tex | HIGH |
| rn98-99 | Hecke defect δ_p^Hecke(A) := [d_sew, T_p] as key obstruction measure | new definition | HIGH |
| rn101-102/110 | Three Langlands gaps mapped precisely (bar-cobar vs scattering, arithmetic descent, analytic continuation) | concordance.tex frontier | MEDIUM |
| rn103/109 | Periodic CDG at admissible k = -h∨ + p/q (door to logarithmic CFT) | concordance.tex | MEDIUM (CONJECTURAL) |
| rn114 | Four local theorems: (1) MC couplings = Perf(A!), (2) meromorphic tensor dg-category, (3) factorization cosheaf equivalence, (4) A_b is A∞-chiral | Vol II foundations | HIGH |

### Killed (do NOT install)

| Source | Claimed content | Why killed |
|--------|----------------|-----------|
| rn105-112 Cluster A (~70%) | "New" open/closed primitive datum | Already in manuscript. AP2 at scale: rediscovers existing proved content |
| rn105-112 F.1-F.3 | Entanglement-annulus "theorem" | Would replace PROVED result (from κ) with CONJECTURAL derivation (from full open/closed). Opposite of fortification |
| rn105-112 I.2 | Ξ_{ann}(s) = ξ(s) as "PROVED" | Is Riemann's 1859 computation. Not a theorem of the programme |
| rn105-112 C.4 | Beilinson functional closure conjecture | Zero numerical evidence. Pure speculation |
| rn105-112 N.1-N.5 | Five-theorem programme | Conjectures with zero evidence beyond structural analogy |
| rn121 items requiring rewrite of proved chapters | Replace proved with conjectural | Violates fortification principle |
| Θ_A + Θ_{A!} = 0 (full level) | Full-tower anti-symmetry | Only κ-level proved. AP7 scope inflation |

### Downgraded (install as conjectural/frontier only)

| Source | Content | Correct status |
|--------|---------|---------------|
| rn105-112 B.6 | Two-variable L_A(s,u) | Formal target (convergence issues unaddressed) |
| rn105-112 B.7 | Sewing-Selberg formula | Pending normalization verification |
| rn105-112 L.2 | W_3 quartic Gram determinant | Pending independent computation |
| rn122 global modular completions for M2/M5 | Modular cooperad for brane theories | Conjectural (local charts solid, globalization not written) |

---

## ENHANCED TIER STRUCTURE (100+ agents)

### TIER 0 — THE LOCAL NONLINEAR BRIDGE (10 agents, CRITICAL PRIORITY)

This is THE strategic bottleneck. Everything else is secondary until this is closed.

1. **DS-HPL Transfer Theorem full exposition** (rn120 construction): Expand prop:coproduct-arity2-vanishing into a full 3-4 page passage in 3d_gravity.tex. Cover: setup, ghost-number computation, physical meaning (gravity doesn't produce particles, only braids), comparison with gauge theory, BTZ connection. Chriss-Ginzburg standard. Most memorable passage in the monograph.

2. **Adversarial: break primitivity at all arities**: Does the ghost-number argument work at ALL arities? What about the perturbation δ — does it preserve ghost number? BRST differential ghost-number-violating terms? A∞ morphism constraints? Failure for W_N (N≥3)?

3. **Compute: gravitational_coproduct.py**: Implement SDR (i,p,h) for sl_2 DS, compute first 3 HPL tree corrections to Δ_{z,2}(T,T) numerically at k=1,2,3, verify vanishing. Also check Δ_{z,3}(T,T,T). 40+ tests.

4. **Five worked examples: CS primitive package** (rn122): Write the explicit C_op, A = V_k(g), Z = C*_ch(V_k(g), V_k(g)) for Chern-Simons. Generators-and-relations presentation. Install in Vol II.

5. **Five worked examples: 3d gravity primitive package** (rn122): A = Vir⊗Vir̄ (or W_N⊗W̄_N). Unreduced chart vs gravity chart. DS reduction from doubled affine. Install in Vol II.

6. **Five worked examples: twisted holography** (rn122): A = BRST(bc-βγ) ≃ ⟨∂ⁿB[p,q]⟩. Gauge-side vs defect-side charts. Install in Vol II.

7. **Five worked examples: twisted M2** (rn122): A = A(K) = DDCA_{ε₁,ε₂}(gl_K). Gaiotto-Rapčák-Zhou presentation. Install in Vol II.

8. **Five worked examples: twisted M5** (rn122): A = W_∞(K). Matrix Miura presentation. M2-M5 intertwiners. Install in Vol II.

9. **r(z) = Koszul-dual inverse named theorem** (rn115 Item 17): Write precise categorical statement. The spectral r-matrix is the functional inverse of the λ-bracket under Koszul duality. This should be a named theorem in yangians_drinfeld_kohno.tex.

10. **Four-test boundary of control + two orthogonal axes** (rn116 Items 13-14): Write clean honest summary: DK-3 (categorical), lattice-only (arithmetic), chirally Koszul (geometric), ρ<1 (analytic). The two axes: critical-level bar cohomology vs off-critical shadow tower. Install in concordance.tex.

11. **Four local theorems from rn114** (install in Vol II foundations): (1) MC couplings dg-category is equivalent to Perf(A!) via universal MC element; (2) (C_J^op, ⊗_z, 1) is meromorphic tensor dg-category via dg-shifted Yangian coassociativity; (3) Meromorphic tensor and factorization dg-cosheaf presentations are equivalent via FM collision compactification; (4) A_b = RHom(b,b) is an A∞-chiral algebra via Stokes on collision-compactified configuration space. These are the precise local theorems that Stage 1 of the four-stage programme requires.

### TIER 0.5 — ARITHMETIC FRONTIER (5 agents, HIGH PRIORITY)

The prime-locality gap is the single remaining obstruction between the proved core and the Ramanujan programme. From rn98-99:

1. **Prime-locality Route C implementation**: MC rigidity overdetermines shadows at high arity → shadows should be character-determined → character-level prime-locality propagates. This is the most promising resolution route. Write explicit character-level Rankin-Selberg integral for Virasoro and W_3.

2. **Hecke defect computation**: Compute δ_p^Hecke(A) := [d_sew, T_p] explicitly for Heisenberg (should vanish), Virasoro (should be D_A-exact), and W_3 (test case). 30+ tests.

3. **Three Langlands gaps honest exposition**: From rn101-102/110, install the three genuine structural gaps (bar-cobar vs scattering poles, arithmetic descent function-field→number-field, analytic continuation real→complex) in concordance.tex. These are STRUCTURAL, not computational — honest about what Langlands equivalence would be needed.

4. **Periodic CDG at admissible levels**: From rn103/109, the conjecture that at admissible k = -h∨ + p/q the bar complex acquires periodic CDG structure indexed by q-th roots of unity. This is the door to logarithmic CFT. State as CONJECTURE in concordance.tex with scope fence: comparison to external logarithmic categories not proved beyond sl_2.

5. **Dirichlet-sewing lift compute module**: Implement S_A(u), D_N(q), λ̃_n(A) computationally for all standard families. Verify S_H(u) = ζ(u)ζ(u+1), Miura defect D_3(q) = (1-q)²(1-q²), and Li-coefficient sign patterns. 50+ tests.

### TIER 1 — MANUSCRIPT INTEGRATION (20 agents, same as existing kickstart)

Same as existing kickstart Tier 1, items 1-20. Each agent takes one compute module's results and writes into the corresponding .tex chapter. Key additions from Beilinson filter:

- **Item 21 (NEW)**: Install Dirichlet-sewing lift S_A(u) + Euler product + Miura defect in arithmetic_shadows.tex and heisenberg_eisenstein.tex (rn105-112 Cluster B gold)
- **Item 22 (NEW)**: Install canonical cyclotomic boundary chart from root stacks in new frontier section (rn105-112 Cluster G gold — strongest new mathematical construction)
- **Item 23 (NEW)**: Install three-gap analysis + Beilinson discard criteria in concordance.tex (rn105-112 Clusters D.3, K)
- **Item 24 (NEW)**: Complete arithmetic packet connection in arithmetic_shadows.tex (rn105-112 Cluster E)
- **Item 25 (NEW)**: Install Hankel/Schur complement extraction in higher_genus_modular_koszul.tex (rn105-112 Cluster C.1)
- **Item 26 (NEW)**: Restricted DK-5 conjecture formal statement in yangians_drinfeld_kohno.tex (rn116 Item 12)

**REMOVED from strikelist** (Beilinson audit casualties):
- ~~Introduction rewrite for open/closed~~ (already the framework)
- ~~Preface update~~ (not needed)
- ~~Bar construction remark~~ (distinction already stated)
- ~~Chiral Hochschild universality~~ (already there as theorem)
- ~~Entanglement chapter rewrite~~ (would weaken proved results)
- ~~Configuration spaces tangential log curves~~ (already defined)

### TIER 2 — ADVERSARIAL RE-AUDIT (20 agents, enhanced with rn121 checklist)

Same structure as existing kickstart Tier 2, items 1-20, but each agent also carries the following Beilinson filter checklist derived from rn121's "100 things wrong":

**Foundational checks (every audit agent)**:
- [ ] Is the primitive treated as C_op (correct) or A_b (wrong)?
- [ ] Is bulk identified as derived center (correct) or bar complex (wrong)?
- [ ] Is modularity attributed to trace+clutching on open sector (correct) or closed algebra (wrong)?
- [ ] Are universal claims qualified (which families, which genera, which levels)?
- [ ] Are theorem/conjecture/programme distinctions clean?

**Operadic checks (theory chapter agents)**:
- [ ] Is A∞-chiral vs strict chiral distinguished?
- [ ] Is L∞ vs dg Lie vs brace language consistent?
- [ ] Are completion/topology issues explicit (completed tensor products, filtered limits)?
- [ ] Is the relationship to Loday-Vallette operadic Koszul duality explicit?

**Geometric checks (global/connection chapter agents)**:
- [ ] Is tangential log curve vs ordinary curve distinguished?
- [ ] Is real-oriented blowup integrated into formalism?
- [ ] Are the four boundary stratum types (interior, ordered, mixed, nodal) explicit?
- [ ] Is the mixed Ran space Ran^{oc}(X,D,τ) defined?

### TIER 3 — PROSE CLEANUP (15 agents, same as existing kickstart)

Unchanged from existing kickstart. The Chriss-Ginzburg + Kac/Etingof/Bezrukavnikov/Gelfand standard. No AI slop. No em dashes. No hedging.

### TIER 4 — NEW CONTENT FROM RAEEZNOTES (15 agents, REWRITTEN)

Replaces existing kickstart Tier 4 entirely.

1-5. **WP5 worked examples** (CS, 3d gravity, twisted holography, M2, M5) — canonical Θ^oc template. **UPGRADED**: each example now has an explicit primitive package (C_op, b, A, Z, Θ, Tr) from rn122. The agents should write generators-and-relations presentations, not just slogans.

6-8. **WP6 example chapter restructure** (Heisenberg, KM, W-algebras) — keep as-is.

9. **WP7: open problems restated as Θ^oc questions** — keep as-is.

10. **Falsifiability memo** (rn121): One page: "If these three statements fail, kill the programme." (a) If the local Swiss-cheese universal property U(A) = (C*_ch(A,A), A) fails for the Heisenberg algebra, the local architecture is wrong. (b) If DS-HPL fails to produce a well-defined Virasoro Yangian at the chain level, the gravity bridge is broken. (c) If the shadow tower for Virasoro diverges at all c (not just c < c*), the nonperturbative programme is dead.

11. **DS as functor on primitive triples** (rn115 Item 21): DS reduction acts functorially on (A!, Δ_z, r(z)). Makes DS-bar intertwining concrete.

12. **Theorem/conjecture ledger** (rn121): Split the programme into green (proved local algebra), amber (externally supported physics), red (unproved global modular descent). One table.

13. **"Forbidden slogans" list** (rn121): bar=bulk, boundary algebra is primitive, "all master conjectures resolved," gravity Yangian at strict level (it's cohomological).

14. **Annulus calculation completely** (rn121): Rigorously identify annular factorization homology with HH_*(C_op) in the programme's own formalism. Not by analogy.

15. **One benchmark global example fully explicit** (rn121): X = P¹, D = {0,∞}, one tangential point at each puncture. Compute every object in the package.

### TIER 5 — COMPUTE VERIFICATION + EXTENSION (15 agents, enhanced)

Same as existing kickstart Tier 5, items 1-15, plus:

- **Item 16 (NEW)**: DS-HPL homological perturbation for W_3 → extend beyond sl_2. Does ghost-number obstruction persist for W_N with N≥3? The DS reduction is more complex (non-principal for sl_3, or principal for sl_N). Compute Δ_{z,2}^{W_3}(W,W) explicitly.

- **Item 17 (NEW)**: Verify W_3 quartic Gram determinant det G^{ct}_{W_3} = (1/10)c³(2c-1)(5c+22)² independently (rn105-112 L.2, pending verification).

- **Item 18 (NEW)**: Verify Sewing-Selberg formula normalization (rn105-112 B.7, pending verification).

### TIER 6 — THE GRAVITATIONAL COPRODUCT IS PRIMITIVE (3 agents, same as existing kickstart)

The most important new discovery of the previous session. Keep items 1-3 as-is from existing kickstart: Writer (full exposition), Adversarial (try to break it), Compute (gravitational_coproduct.py).

**Enhancement**: The Writer agent should now explicitly use the five worked examples from rn122 to contextualize the primitivity result. CS_G has nontrivial coproduct (gluons split); gravity does not (only braids). This is the sharpest physical content in the monograph.

### TIER 7 — STANDALONE PAPER (5 agents, REFOCUSED)

The standalone paper should now be refocused per the Beilinson filter:

**Title**: "Modular Koszul Duality and the Shadow Tower: Algebraicity, Depth Classification, and the Gravitational Coproduct"

**Spine**: One theorem (shadow tower algebraicity), one classification (G/L/C/M), one computation (F₂(W₃)), one discovery (gravitational coproduct primitivity).

1. Write abstract + introduction (from compute/audit/standalone_paper_plan.md, refocused)
2. Write §3-4 (Riccati algebraicity theorem + proof)
3. Write §5-6 (G/L/C/M classification + shadow tables)
4. Write §7-8 (F₂(W₃) computation + gravitational coproduct)
5. Adversarial review of the draft

---

## ANTI-PATTERNS TO WATCH (enhanced from rn121 "100 things wrong")

In addition to AP1-AP32, the following structural anti-patterns from rn121 should be actively monitored:

**SAP1 — Globalizing before closing the local bridge.** The programme has been building modular towers, complementarity potentials, and shadow packages before the first nonlinear comparison theorem is finished. Rule: no new global structure until DS-HPL is closed and verified.

**SAP2 — Rediscovering existing manuscript content.** 70% of rn105-112's "new" open/closed primitive datum was already proved in the .tex source. Rule: before proposing ANY rewrite, grep the manuscript for existing treatments. AP2 at scale.

**SAP3 — Replacing proved results with conjectural derivations.** The entanglement-annulus proposal would replace S_EE = (c/3)log(L/ε) (PROVED from κ) with a derivation from the full open/closed framework (CONJECTURAL). Rule: never weaken a proof by adding hypotheses. Fortify, don't replace.

**SAP4 — Presenting classical results as programme theorems.** Ξ_{ann}(s) = ξ(s) is Riemann 1859, not a theorem of the programme. Rule: when a computation reproduces a known result, say "we recover [Author Year]," not "we prove."

**SAP5 — Proposing massive file rewrites without reading the .tex.** The original rn105-112 strikelist proposed rewriting ~45 files. After Beilinson audit: ~8 files need changes. Rule: read the target file BEFORE proposing a rewrite. The rewrite you propose may already be done.

---

## STANDING DIRECTIVES

Do NOT build LaTeX or run pre-existing tests unless you wrote them. Focus on mathematical writing and new computation. Beilinson Principle. Chriss-Ginzburg standard. Kac/Etingof/Serre prose. No AI slop. No em dashes. No hedging.

**The Beilinson test for every new claim**: "Is this genuinely new mathematics, or am I rediscovering what's already in the .tex? Is this a theorem, a conjecture, or a programme? Am I globalizing before the local bridge is closed?"

## ===END PROMPT===
