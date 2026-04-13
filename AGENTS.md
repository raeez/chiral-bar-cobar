# AGENTS.md — Modular Koszul Duality Programme (Canonical)

This file is the always-on operating constitution for Codex/GPT-5.4 in `~/chiral-bar-cobar` (Vol I). It is optimized for mathematical correction at `xhigh` reasoning effort. `CLAUDE.md` is the encyclopedic atlas; `AGENTS.md` is the load-bearing operational layer that steers correct behavior after compaction, context loss, model drift, or long multi-tool sessions. Every line changes behavior or it gets cut.

**Three volumes by Raeez Lorgat.** Vol I *Modular Koszul Duality* (this repo, ~2,719pp). Vol II *A-infinity Chiral Algebras and 3D HT QFT* (`~/chiral-bar-cobar-vol2`, ~1,681pp). Vol III *CY Categories, Quantum Groups, and BPS Algebras* (`~/calabi-yau-quantum-groups`, ~319pp). Total ~4,719pp, 121K+ tests, 3,500+ tagged claims.

Use this file for: durable repo-wide invariants; task routing and mode selection; truth hierarchy and claim-state discipline; session entry and verification loops; cross-volume propagation rules; empirical failure maps from recent commit archaeology; current dirty-surface awareness when it changes behavior.

Do not use this file as a dumping ground for temporary plans, session chatter, or a second prose copy of every anti-pattern in `CLAUDE.md`. If an instruction does not change behavior, remove it.

## I. Mission

This repository is in correction mode. For the current phase, optimize for truth, rectification, and claim-surface integrity over expansion. Assume all three volumes still contain undiscovered errors. Your job is not to defend inherited wording. Your job is to find falsehoods, isolate them, and either fix them or narrow the claims until they are true.

## II. GPT-5.4 Design Axioms

This constitution is deliberately shaped around current best practice for high-end agentic mathematical work:

1. **Exact scope before reasoning.** Name the file, theorem label, formula, convention, family, and status boundary before trying to solve the problem.
2. **Verification before verbosity.** Prefer a short falsifiable instruction plus a check over a long motivational paragraph.
3. **Smaller always-on prompt, stronger triggered workflows.** Keep the constitutional layer compact. Put deep repeated workflows into skills. Put deterministic enforcement into hooks or grepable checks.
4. **Prompt geometry matters.** Issue-shaped prompts outperform essays. Exact files, labels, formulas, conventions, nearby diffs, and acceptance checks beat broad aspirations.
5. **Reasoning effort is a last-mile knob.** Before increasing effort, tighten the task, read the live surface, lock conventions, and name the falsifier.
6. **Interleave reasoning with tools.** Read, grep, diff, test, then reason. Do not try to solve a local mathematical or repository problem from abstract memory alone.
7. **Multiple independent checks beat single-chain confidence.** Prefer direct computation plus source reading plus limiting-case or convention checks.
8. **Externalize only durable state.** The artifacts that should survive compaction are labels, hypotheses, grep targets, failing tests, open blockers, and verification notes.
9. **Smaller true claims beat larger false claims.** Impressive prose that does not survive rereading is failure.
10. **Build artifacts are not evidence.** PDFs, logs, and generated summaries help navigation, but they do not outrank source, proof, tests, or exact citations.

### GPT-5.4 Prompt Architecture (for composing task prompts)

When composing task prompts for Codex agents or sub-agents, use XML-tagged blocks for structural clarity:

- `<task>`: the concrete job and repository context
- `<structured_output_contract>`: exact shape, ordering, brevity requirements
- `<default_follow_through_policy>`: act without asking routine questions; stop only when a missing detail changes correctness or safety
- `<verification_loop>`: verify result against task requirements before finalizing
- `<grounding_rules>`: ground every claim in evidence; label hypotheses
- `<missing_context_gating>`: do not guess missing repository facts; retrieve with tools or state unknowns
- `<completeness_contract>`: resolve fully; check for follow-on fixes and edge cases
- `<dig_deeper_nudge>`: after first finding, check for second-order failures, empty-state behavior, stale state
- `<action_safety>`: keep changes scoped; avoid unrelated refactors; call out risky actions
- `<tool_persistence_rules>`: keep using tools until evidence suffices; do not abandon after partial read

**Anti-patterns to avoid**: vague task framing; missing output contract; asking for "more reasoning" instead of better contract; mixing unrelated jobs into one run; unsupported certainty without grounding.

## III. Programme Identity (Crystallized 2026-04-12)

E_1-E_1 operadic Koszul duality in the homotopical modular chiral realm on algebraic curves. One form (eta = d log(z_1 - z_2)), one relation (Arnold), one object (Theta_A), one equation (D*Theta + 1/2[Theta,Theta] = 0).

**The primitive object** is B^ord(A) = T^c(s^{-1}A-bar): ordered bar, deconcatenation coproduct, R-matrix, Yangian. The symmetric bar B^Sigma is the Sigma_n-coinvariant shadow. Physics IS the homotopy type: A-infinity = scattering, SC^{ch,top} governs the (bulk, boundary) pair, modular L-infinity = genus tower. The five theorems A-D+H are the invariants that survive averaging.

**Bar complex is E_1-coassociative; SC^{ch,top} emerges on the derived center (CRITICAL, corrected 2026-04-12).** The bar complex B^{ord}(A) = T^c(s^{-1}A-bar) is an E_1-chiral coassociative COALGEBRA (over ChirAss^!). It has a differential + deconcatenation coproduct. It does NOT carry SC^{ch,top} structure. The SC^{ch,top} structure (or E_3 with conformal vector) emerges on the DERIVED CENTER Z^{der}_{ch}(A) = ChirHoch*(A,A), computed USING the bar complex as a resolution. The bar complex is the E_1 engine; the derived center is the SC^{ch,top}/E_3 output. thm:bar-swiss-cheese (claiming B(A) is an SC-coalgebra) needs retraction or careful restatement — see FOUND-11.

**The E_n operadic circle (2026-04-12):** E_3(bulk) → E_2(boundary chiral) → E_1(bar/QG) → E_2(Drinfeld center) → E_3(derived center). Each arrow: restriction to codim-2 defect, ordered bar complex, categorified averaging (Drinfeld center), higher Deligne (derived center). Closes for 3d HT with conformal vector; without conformal vector, stuck at SC^{ch,top}.

**SC^{ch,top} ≠ E_3 (2026-04-12).** The Swiss-cheese operad is two-coloured with directionality (no open-to-closed). Dunn additivity does NOT apply. E_3 requires topologization: SC^{ch,top} + inner conformal vector (Sugawara at non-critical level, making C-translations Q-exact) = E_3-TOPOLOGICAL (NOT E_3-chiral). Without conformal vector: stuck at SC^{ch,top}. thm:topologization PROVED for affine KM V_k(g) at non-critical level k != -h^v. General: CONJECTURAL (conj:topologization-general). Proof is cohomological; for class M, chain-level E_3 may fail.

**Five notions of E_1-chiral algebra (2026-04-12):** (A) strict ChirAss-algebra, (B) A_inf in End^{ch}_A, (C) EK quantum vertex algebra, (D) A_inf in E_1-chiral, (E) factorization on Ran^{ord}(X). Each has own derived center. (B)↔(C) via Drinfeld associator on Koszul locus. Warning installed at algebraic_foundations.tex warn:multiple-e1-chiral.

**Three Hochschild theories (2026-04-12):** (i) Topological HH: E_1-algebra input → E_2 output (Deligne). (ii) Chiral HH (ChirHoch): E_inf-chiral input → E_inf output, concentrated {0,1,2} (Theorem H). (iii) Categorical HH: dg category input → E_2 with CY shifted Poisson. NEVER conflate. The geometry determines which Hochschild: curve X → chiral, R → topological, CY category → categorical.

**Architecture (2026-04-12):** E_n chiral algebra theory stays in Vol I (pure algebra/operads). ALL physics moves to Vol II. Vol III provides the geometric source (CY categories → chiral algebras via the E_n circle).

**What we study:** Holomorphic chiral (factorisation) (co)homology via bar and cobar chain constructions at various different geometric locations, hence the different (modular) operads at play. The geometry determines the operad, the operad determines the bar complex, the bar complex computes the factorisation (co)homology. The five theorems are structural properties. The shadow tower is the characteristic class data. The E_n circle is the holographic structure.

**North star:** platonic_ideal_reconstituted_2026_04_12.md is THE SINGLE REFERENCE for all structural questions.

## IV. The Beilinson Principle

"What limits forward progress is not the lack of genius but the inability to dismiss false ideas." Every claim is false until independently verified from primary source. Prefer a smaller true theorem to a larger false one. Every numerical claim requires 3+ genuinely independent verification paths (direct computation, alternative formula, limiting case, symmetry/duality, cross-family, literature+convention, dimensional analysis, numerical evaluation).

Operational consequences: treat every confident statement as provisional until checked locally; if a proof seems to work "morally", identify the exact map, filtration, hypothesis, category, and comparison theorem; search first for hidden hypotheses, scope leakage, conflated objects, sign/grading errors, reduced-vs-completed mistakes, status inflation; never preserve legacy text just because it exists; use the compute layer as an adversarial instrument.

**Epistemic hierarchy** (higher wins): (1) Direct computation > (2) .tex source +/-100 lines > (3) Build system > (4) Published literature > (5) concordance.tex > (6) This file > (7) Memory. Before every assertion: "How do I know this? Read the source, computed it, or assumed it?" If assumed, stop and verify.

## V. Truth Hierarchy

The order of trust in this repo:

1. Direct computation or a local proof whose nontrivial steps can be named and checked
2. The live `.tex` or `.py` source, read in context
3. Targeted tests, metadata generation, and build/log evidence that genuinely verifies the claim
4. Exact primary literature with explicit convention conversion
5. `chapters/connections/concordance.tex`
6. `metadata/theorem_registry.md` and other generated metadata
7. `CLAUDE.md` and this file
8. Memory, prior agent prose, and repo folklore

**Not evidence:** confidence; repetition across files; a claim-status macro by itself; a previously generated PDF; README or notes outclaiming the source; earlier agent summaries not rechecked locally.

## VI. Constitutional Files And Required First Reads

Before any substantive mathematical edit, read:

1. `CLAUDE.md`
2. `chapters/connections/concordance.tex`
3. `metadata/theorem_registry.md`
4. `raeeznotes/raeeznotes100/red_team_summary.md` (or `archive/raeeznotes/raeeznotes100/red_team_summary.md`)
5. The exact files you will touch, plus directly cited dependencies

`chapters/connections/concordance.tex` is the constitution of the monograph. When files disagree, repair the chapter/theorem/status to match the concordance, or update the concordance deliberately.

## VII. E1-First Prose Architecture (MANDATORY)

The ordered bar B^ord(A) is the primitive object. Every chapter, section, theorem presentation MUST construct the E1 ordered story first, then derive the symmetric story by averaging:

1. CONSTRUCT the E1 object (B^ord, r(z), Theta_A in g^{E1}, the matrix-valued curvature)
2. EXHIBIT the E1 structure (deconcatenation coproduct, R-matrix, Yangian)
3. APPLY the averaging map av: g^{E1} → g^mod (lossy Sigma_n-coinvariant projection)
4. DERIVE the symmetric result (kappa = av(r(z)), obs_g = kappa*lambda_g, the shadow tower)

NEVER state a symmetric-bar result (kappa, obs_g, shadow tower) without first showing the E1 object it projects from. NEVER frame the five theorems as "concerning the symmetric bar" — they EXTRACT the Sigma_n-invariant content of the ordered bar. The symmetric bar is the shadow; the ordered bar generates.

The convolution algebra has two levels: g^{E1}_A (the primitive, carrying the R-matrix) and g^mod_A (the coinvariant shadow, carrying only kappa). Theta_A lives in g^{E1}_A; everything in this monograph is its Sigma_n-coinvariant projection.

## VIII. Cross-Volume Scope

This repo is Volume I of a three-volume programme:
- Vol I: `~/chiral-bar-cobar`
- Vol II: `~/chiral-bar-cobar-vol2`
- Vol III: `~/calabi-yau-quantum-groups`

When a task touches shared formulas, theorem statuses, definitions, notation, bridge claims, chapter references, or hardcoded expected values, the live surface includes all three volumes.

Cross-volume rule: grep before editing; grep after editing; update all genuine duplicates in the same session, or leave an explicit pending note naming the untouched collision surface.

## IX. The Five Objects (NEVER CONFLATE)

- **A**: algebra
- **B(A) = T^c(s^{-1} Ā)**: bar coalgebra (Ā = ker(epsilon), augmentation ideal)
- **A^i = H*(B(A))**: dual coalgebra (Koszul cohomology of bar)
- **A^! = ((A^i)^v)**: dual algebra (linear or Verdier dual)
- **Z^{der}_{ch}(A)**: derived chiral center = bulk (Hochschild cochains)

Omega(B(A)) = A is INVERSION. A^! from VERDIER duality. Bulk from HOCHSCHILD cochains. B^ord is the primitive; B^Sigma is the av-image shadow. "The bar complex" without qualifier means B^ord; B^Sigma only when factorization picture needed.

**FORBIDDEN conflations:** "bar-cobar produces bulk" (WRONG: bar-cobar inverts to A; bulk is Hochschild); "Omega(B(A)) is the Koszul dual" (WRONG: that is INVERSION); "the Koszul dual equals the bar complex" (WRONG: bar is coalgebra, dual is algebra); "D_Ran(B(A)) is the cobar complex" (WRONG: D_Ran is Verdier; cobar is Omega).

**SC^{ch,top} is NOT on B(A) (AP165).** B(A) is E_1 coassociative coalgebra. SC^{ch,top} lives on the pair (C^bullet_{ch}(A,A), A). FORBIDDEN: "B(A) is a coalgebra over SC^{ch,top}"; "the bar differential is the closed color"; "the bar coproduct is the open color."

**SC^{ch,top} is NOT Koszul self-dual (AP166).** SC^! = (Lie^c, Ass^c, shuffle-mixed) with closed dim = (n-1)!. SC = (Com, Ass) with closed dim = 1. The duality FUNCTOR is involutive ((P^!)^! ~ P); the OPERAD is not self-dual (P^! ≇ P).

**A^! is an SC^!-algebra (AP172)** = (Lie, Ass)-algebra (closed = Sklyanin bracket, open = Yangian product). NOT an SC-algebra.

## X. The Four Shadow Classes

- **G**: r=2, Heisenberg. Delta=0, d_alg=0. SC-formal.
- **L**: r=3, affine KM. Delta!=0, d_alg=1.
- **C**: r=4, betagamma. Delta!=0, d_alg=2.
- **M**: r=inf, Vir/W_N. Delta!=0, d_alg=inf.

Delta = 8*kappa*S_4. Delta=0 ↔ finite tower. SC formality: A is SC-formal iff class G. Depth gap: d_alg in {0,1,2,inf}; gap at 3. ChirHoch^1(V_k(g)) = g; total dim = dim(g)+2.

## XI. Canonical Formulas

Verify against these AND `landscape_census.tex` before writing. NEVER write kappa from memory (AP1).

```text
# Kappa (C1-C4)
kappa(H_k) = k                                       # Heisenberg; k=0→0, k=1→1
kappa(Vir_c) = c/2                                    # Virasoro ONLY; c=0→0, c=13→13/2
kappa(V_k(g)) = dim(g)(k+h^v)/(2h^v)                 # Affine KM; k=0→dim(g)/2 (NOT 0), k=-h^v→0
kappa(W_N) = c*(H_N - 1), H_N = sum_{j=1}^N 1/j      # W_N; N=2: H_2-1=1/2 so kappa=c/2=Vir

# r-matrix (C9-C11) — level prefix k MANDATORY (AP126, THE MOST VIOLATED AP)
r^KM(z) = k*Omega/z           [trace-form]            # k=0→0; k=-h^v→finite
r^KM(z) = Omega/((k+h^v)*z)   [KZ]                    # k=0→Omega/(h^v*z)!=0; k=-h^v→diverges
r^Heis(z) = k/z                                       # k=0→0
r^Vir(z) = (c/2)/z^3 + 2T/z                           # cubic+simple, NOT quartic. d-log absorbs one

# Bridge: k*Omega_tr = Omega/(k+h^v) at generic k
# Averaging (C13): av(r(z)) = kappa for abelian; av(r(z)) + dim(g)/2 = kappa for non-abelian KM

# Central charges (C5-C7)
c_bc(lambda) = 1 - 3(2*lambda-1)^2                    # fermionic; lambda=1/2→1, lambda=2→-26
c_bg(lambda) = 2(6*lambda^2-6*lambda+1)               # bosonic; lambda=1/2→-1, lambda=2→+26
c_bc + c_bg = 0                                        # pointwise; verify at lambda=1: 2+(-2)=0

# Bar complex (C14-C15)
B(A) = T^c(s^{-1} A-bar), A-bar = ker(epsilon)        # AP132: augmentation ideal, NOT bare A
|s^{-1}v| = |v| - 1                                    # desuspension LOWERS; mnemonic: bar=down=s^{-1}
d_bar^2 = 0 ALWAYS; d_fib^2 = kappa*omega_g            # fiberwise only, at g>=1

# Structural constants
MC: d*Theta + (1/2)[Theta,Theta] = 0
QME: hbar*Delta*S + (1/2){S,S} = 0
F_1 = kappa/24                                         # sanity check for Cauchy normalization
F_2 = 7*kappa/5760                                     # NOT 7/2880, NOT 1/5760
eta(tau) = q^{1/24} * prod_{n>=1}(1-q^n)              # q^{1/24} ESSENTIAL for modular weight 1/2
Cauchy: [z^{n-1}]f(z) = 1/(2*pi*i) * oint f(z)dz/z^n  # NOT 1/(2*pi) — missing i
Delta = 8*kappa*S_4                                    # LINEAR in kappa, NOT quadratic
S_2 = kappa for ALL families                           # S_2=c/12 is WRONG (divided-power confusion)

# Complementarity (C18-C20)
K(KM) = K(Heis) = K(lattice) = K(free) = 0
K(Vir) = 13       self-dual c=13 (NOT c=26, NOT c=0)
K(W_3) = 250/3
K(BP) = 196        (NOT 2); self-dual k=-3; kappa(BP)+kappa(BP^!)=98/3 (NOT 1/3)

# Combinatorial / numerical
sl_2 bar H^2 = 5 (NOT 6)
genus-2 stable graphs = 7 (NOT 6)
E_8 adjoint = 248 (NOT 779247 — not any E_8 irreducible)
1/eta^2 coefficients: (1,2,5,10,20,...) bicoloured partitions (NOT triangular 1,3,6,10,...)
alpha_g = 2*rank + 4*dim*h^v (Hilbert-series growth)
d_alg in {0,1,2,inf} (3 impossible)
```

Full census C1-C31 with wrong variants and derivations: see CLAUDE.md §True Formula Census.

## XII. Forbidden Formulas (grep after every .tex write)

```text
# r-matrix / level
B1.  r(z) = \Omega/z                    # bare level-stripped; MUST be k*\Omega/z
B2.  r^Vir(z) = (c/2)/z^4              # quartic; MUST be (c/2)/z^3 + 2T/z
B3.  r^Vir(z) = (c/2)/z^2              # quadratic; MUST be cubic + simple
B4.  \Omega\,d\log z  (no k)           # MUST be k\Omega\,d\log z

# central charges / kappa
B5.  c_{bc} = 2(6L^2-6L+1)             # that is c_bg — swapped
B6.  c_{bg} = 1-3(2L-1)^2              # that is c_bc — swapped
B7.  kappa(W_N) = c*H_{N-1}            # MUST be c*(H_N - 1)
B8.  kappa = c/2 unqualified           # Virasoro ONLY
B9.  kappa+kappa' = 0 unscoped         # family-specific: 0 KM/free, 13 Vir
B10. kappa = S_2/2                     # S_2 = kappa (no factor 2). Only Vir has kappa=c/2
B11. av(r(z))=kappa for non-abelian KM # missing Sugawara shift dim(g)/2
B12. bare kappa in Vol III             # MUST be kappa_{ch|cat|BKM|fiber}
B13. kappa_{global|BPS|eff|total|naive} # forbidden subscripts in Vol III

# bar complex / suspension
B14. T^c(s^{-1} A)                     # missing augmentation: MUST be A-bar
B15. T^c(s A)                          # wrong direction: MUST be s^{-1}
B16. |s^{-1}v| = |v|+1                 # MUST be |v|-1
B17. eta = prod(1-q^n)                 # missing q^{1/24}

# boundaries / combinatorics
B18. W_N weights {2,...,N+1}           # MUST be {2,...,N} (N-1 generators)
B19. H_N = sum_{j=1}^{N-1} 1/j        # upper limit is N, not N-1
B20. C_n counts binary trees with n leaves # MUST be n+1 leaves
B21. E_8 fundamental = 779247          # not any E_8 irreducible
B22. dim H^2(B(sl_2)) = 6             # MUST be 5
B23. genus-2 stable graphs = 6        # MUST be 7
B24. 1/eta^2 coefficients (1,3,6,10)  # MUST be bicoloured (1,2,5,10,20)
B25. K_BP = 2                          # MUST be 196

# scope / quantifier
B26. obs_g = kappa*lambda_g untagged   # MUST tag (UNIFORM-WEIGHT) or (ALL-WEIGHT + delta)
B27. A ↔ B where only → proved        # use → + Remark on converse
B28. "k=0 fails Koszulness" for KM    # k=0 is abelian limit, still Koszul; k=-h^v is critical
B29. Thm C^{E1} with n free on RHS    # fully quantify with 2g-2+n > 0

# macros / labels / LaTeX
B30. \end{definition>                  # > instead of }
B33. Part~IV, Chapter~12 hardcoded     # use \ref{part:...}
B34. duplicate label across volumes    # suffix with v1-/v2-/v3-
B35. \begin{conjecture}\label{thm:foo} # prefix MUST match environment
B36. \cite{GeK98} without bibitem      # emits [?]

# numerical coefficients
B37. F_2 = 1/5760 or 7/2880           # MUST be 7/5760
B38. 1/(2*pi) integral (missing i)    # MUST be 1/(2*pi*i)
B39. KM r-matrix not vanishing at k=0 # AP126/AP141

# prose
B40. Markdown in LaTeX (backticks, **bold**) # use $...$, \textbf, \emph
B41. Em-dash (--- or U+2014)          # use colon, semicolon, separate sentence
B42. AI slop (notably, crucially, etc) # banned vocabulary

# depth / dimension / fiber-base
B43. d_alg(Vir) = 3                    # d_gen=3, d_alg=inf
B44. bare d(Vir) without gen/alg       # always subscript
B45. vdim ChirHoch*(A) = 2            # amplitude [0,2], NOT vdim
B46. omega_g = dtau                    # dtau on curve, omega_g = c_1(lambda) on moduli

# grading / curved
B47. [m,[m,f]]=1/2[[m,m],f] at even ||m|| # tautological at even; identity requires odd
B48. m_1^2 = 0 in curved A-inf        # m_1^2(a) = [m_0, a]
B49. d^2=kappa*omega_g as bar diff     # d^2_bar=0 always; d^2_fib=kappa*omega_g is fiberwise

# promotion / SC / sector
B50. dim SC^mix_{k,m} = (k-1)!*m!     # MUST be (k-1)!*C(k+m,m)
B51. B_{SC}(A) for one-colour input    # SC two-coloured; use promotion A→(A,A)
B52. kappa(BP)+kappa(BP^!)=1/3         # MUST be 98/3
B53. "over a point is over P^1"        # FALSE: retract is DATA; disk≠point; A^1 has Arnold
B54. "B(A) is SC coalgebra"            # FALSE: E_1 coalgebra; SC in derived center pair
B55-B56. bar diff/coprod = SC colors   # FALSE: single E_1 coalgebra
B57. SC^{ch,top} is Koszul self-dual   # FALSE: SC^!=(Lie,Ass,shuffle)
B58. "E_3-chiral" for topologized center # FALSE: E_3-TOPOLOGICAL
B59. "Topologization proved for all"   # ONLY for affine KM at non-critical level
B60. "A^! is an SC-algebra"            # FALSE: SC^!-algebra = (Lie,Ass)
B61. "chiral QG for all four families" # ONLY sl_2 Yangian + affine KM verified concretely
B62. S_2 = c/12 for Virasoro          # WRONG: S_2 = kappa = c/2
B63. S_4 ~ 2/(5c^2) at large c        # WRONG: 10/(5c^2) = 2/c^2, not 2/(5c^2)
B69. pi_3(BU) = Z                      # WRONG: pi_3(BU) = 0 (Bott: pi_odd(BU)=0)
B70. kappa_ch = h^{1,1}               # WRONG for h^{0,2}!=0 (K3: h^{1,1}=20, chi/2=12)
B71. McKay(Z_3) = K_{3,3}             # WRONG: 3 copies of oriented 3-cycle
B72. "excision gives B(A)⊗B(A)"       # WRONG: excision gives B_L⊗_A B_R (one copy, over A)
B73. "pi_4(BU)=Z provides E_2"        # WRONG direction: obstruction group, not guarantee
```

Full blacklist B1-B73 with regexes: see CLAUDE.md §Wrong Formulas Blacklist.

## XIII. Hot Zones (Top 10 Repeat Offenders)

Read BEFORE any edit. If your edit touches a hot zone, run the Pre-Edit Verification Protocol (§XVI).

**HZ-1. r-matrix level prefix (AP126/AP141)** — 6 waves, 90+ instances. THE MOST VIOLATED AP.
Template: `family:[_] r(z):[_] level:[_] r|_{k=0}:[_] expected:0 match?[Y/N]`

**HZ-2. Environment matches tag (AP40)** — 5 waves, 70+ instances.
Decision: Q1 proof exists? NO→conjecture. YES→Q2: main→theorem, supporting→prop, auxiliary→lemma. Self-contained→ProvedHere+proof. Cited→ProvedElsewhere+attribution.

**HZ-3. Uniform-weight tag on F_g (AP32)** — 4 waves, 30+ instances.
Every F_g formula MUST carry: (UNIFORM-WEIGHT) or (ALL-WEIGHT + delta F_g^cross) or (g=1 only) or (LOCAL: scope defined).

**HZ-4. Kappa from memory FORBIDDEN (AP1)** — 4 waves, 15+ instances.
Before ANY kappa: (a) identify family, (b) open landscape_census.tex and copy formula, (c) paste with AP1 comment, (d) evaluate at two boundary values.

**HZ-5. Label prefix and uniqueness (AP124/AP125)** — 3 waves, 25+ instances.
Before \label{foo}: (i) prefix matches env (thm/prop/conj/def/rem/lem), (ii) grep all three volumes for uniqueness.

**HZ-6. Hardcoded expected values (AP10/AP128)** — 3 waves, 12+ engines.
Every hardcoded value requires `# VERIFIED` citing 2+ independent sources from {DC, LT, LC, SY, CF, NE, DA}. When correcting an engine, derive new expected from INDEPENDENT source.

**HZ-7. Bare kappa in Vol III (AP113)** — 3 waves, 165 baseline instances.
Approved subscripts: {ch, cat, BKM, fiber}. FORBIDDEN: {global, BPS, eff, total, naive}.

**HZ-8. Proof after conjecture (AP4)** — 3 waves, 40+ instances.
Before \begin{proof}: check nearest preceding env. conjecture/heuristic/remark/definition → STOP, use \begin{remark}[Evidence].

**HZ-9. Four-functor discipline (AP25/AP34/AP50)** — 3 waves, 15+ instances.
Before mentioning "bar", "cobar", "Koszul dual", "derived center": write the four-object template.

**HZ-10. AI slop (AP29)** — 4 waves, 40+ instances.
PRE-WRITE check: banned tokens? POST-WRITE grep: mandatory.

## XIV. Live Cross-Volume Hot Zones

### Hot Zone A: Formula Drift
AP1, AP19, AP117, AP120, AP126, AP136, AP137, AP141, AP143, AP144, AP148, V2-AP34, AP113, AP-CY17, AP-CY19.

### Hot Zone B: Status/Environment/Label Drift
AP40, AP125, AP124, AP4, V2-AP31, AP-CY6, AP-CY11, AP-CY14.

### Hot Zone C: Object and Convention Conflation
AP25, AP34, AP50, AP33, AP131, AP132, AP142, V2-AP1 through V2-AP24, AP-CY3, AP-CY4, AP-CY7, AP-CY10, AP-CY12.

### Hot Zone D: Propagation and Oracle Drift
AP10, AP128, V2-AP26 through V2-AP30, V2-AP32 through V2-AP35, AP-CY13, AP-CY15, AP-CY16, AP-CY18.

### Hot Zone E: Prose Slop and Structural Noise
AP29, V2-AP29, AP121. Artifact cleanup mandatory. Connective words re-audit after formula correction.

## XV. Empirical Risk Map From Last-100-Commit Archaeology

### Volume I: dominant repeat failures
Persistent AP126/AP141; label/status/concordance drift (AP125, AP124, AP40); formula drift (kappa, harmonic, desuspension, central charges); compute/test sync failures; DS ghost charge cascade (AP143); r-matrix convention mixing (AP144/AP148); local-global conflation (AP142); standalone drift; prose fortification; mega-campaign straggler commits (AP146).

### Volume II: dominant repeat failures
AP40 environment/status (~50 instances in 7 commits); V2-AP34 divided-power drift (15+); AP32 uniform-weight drift (20+); AP126 propagation (34+); V2-AP37 Arakelov normalisation (same error 3x); stale Part refs (V2-AP26: 24+); proof-after-conjecture (V2-AP31); phantom label debt (V2-AP38: 366); undefined macros after migration (V2-AP39).

### Volume III: dominant repeat failures
AP113 bare-kappa recurrence; overclaiming d=3 CY existence; conditionality not propagating; stub/thin-chapter fragility; compute/test churn masking status boundary.

## XVI. Pre-Edit Verification Protocol

MANDATORY before editing any surface in the hot zones. Fill template as fenced block in commentary, end with `verdict: ACCEPT`. If any check fails: `verdict: REJECT`, re-draft.

**PE-1: r-matrix write** (trigger: r(z), r_{ij}, classical r-matrix)
```
family: [_]  r(z): [_]  level param: [_]  OPE pole: [_]  r pole: [_-1]
convention: [trace-form / KZ]
AP126 (trace-form): r|_{k=0} = [_]  expected: 0  match? [Y/N]
AP141 grep: bare \Omega/z in scope: [N]  allowed? N
critical-level (KM): r|_{k=-h^v} = [_]
source: [landscape_census.tex:LINE / compute/...]
verdict: [ACCEPT / REJECT]
```

**PE-2: kappa formula write** (trigger: kappa or variant)
```
family: [_]  kappa written: [_]
census: landscape_census.tex:LINE = [_]  match? [Y/N]
at k=0: [_] expected [_]  at k=-h^v (KM): [_] expected 0
at c=13 (Vir): [_] expected 13/2
AP136 (W_N N=2): [_] expected c/2
wrong variants avoided: NOT c, NOT H_{N-1}, NOT k/2, NOT c/(2h^v)
verdict: [ACCEPT / REJECT]
```

**PE-4: bar complex formula** (trigger: B(A), T^c, desuspension)
```
object: B(A) = [_]
T^c argument: [s^{-1} A-bar? Y/N]  AP132: augmentation? [Y/N]
AP22: |s^{-1}v| = |v| [-1/+1] (must be -1)
s^{-1} not bare s? [Y/N]
coproduct: [deconcatenation / coshuffle / coLie]
match to intended bar: [B^ord→deconc / B^Sigma→coshuffle / B^Lie→coLie]
grading: cohomological |d|=+1? [Y/N]
verdict: [ACCEPT / REJECT]
```

**PE-5: Vol III kappa** (trigger: kappa in ~/calabi-yau-quantum-groups)
```
subscript: [kappa_ch / kappa_cat / kappa_BKM / kappa_fiber / OTHER→REJECT]
present? [Y/N]  bare kappa FORBIDDEN
grep before: [N] bare hits  grep after: [N]  delta=0? [Y/N]
verdict: [ACCEPT / REJECT]
```

**PE-7: label creation** (trigger: \label{})
```
environment: [theorem/prop/conj/def/rem/lem]
label: \label{prefix:name}
prefix match (AP125): [Y/N]
AP124 duplicate check: Vol I:[N] Vol II:[N] Vol III:[N] total before:[N] after:[N] delta=1? [Y/N]
verdict: [ACCEPT / REJECT]
```

**PE-8: cross-volume formula** (trigger: shared formula)
```
formula: [_]
Vol I: [hits, form]  Vol II: [hits, form]  Vol III: [hits, form]
consistent? [Y/N]  if not: canonical vol [_], others updated same session? [Y/N]
convention conversion: [OPE→lambda(II) / motivic(III) / NA]  applied? [Y/N/NA]
verdict: [ACCEPT / REJECT]
```

**PE-10: scope quantifier** (trigger: theorem, obs_g, F_g)
```
genus: [g=0/1/>=2/all/UNSPECIFIED→REJECT]
degree: [n=_/all/UNSPECIFIED→REJECT]
AP32 weight tag: [(UNIFORM)/(ALL+delta)/NA]  tagged? [Y/N]
AP139 free-var audit: LHS vars:{_} RHS vars:{_} LHS⊇RHS? [Y/N]
AP36: [implies/iff]  if iff, converse proved same thm? [Y/N]
verdict: [ACCEPT / REJECT]
```

**PE-11: differential form** (trigger: connection, KZ, Arnold, propagator)
```
type: [connection 1-form / KZ / Arnold / bar propagator]
form: [_]
connection: r(z)dz NOT d log;  KZ: sum r_{ij} dz_{ij};  Arnold: d log(z_i-z_j) (bar coeff)
AP27 propagator weight: 1? [Y/N]
AP130 fiber-base: form lives on [fiber/base], correctly distinguished? [Y/N]
verdict: [ACCEPT / REJECT]
```

Remaining templates PE-3 (complementarity), PE-6 (exceptional dims), PE-9 (summation boundary), PE-12 (prose hygiene): see CLAUDE.md §Pre-Edit Verification Protocol.

## XVII. The Resonance Loop

For any nontrivial task, run this loop until CONVERGED or BLOCKED.

### 0. Scope Lock
State the exact claim surface being audited. Lock: file, theorem label, formula, convention, family, status.

### 1. Invariant Lock
Before trusting any local argument, lock: grading and shifts; object identity among A, B(A), A^i, A^!, Z^{der}_{ch}; genus, degree, family, filtration, and completion scope; theorem status and environment; Vol I/II/III convention bridges.

### 2. RED Pass — Attack Logic
Dependency attack; hypothesis attack; edge-case or counterexample; sign, grading, duality, notation; reduced-vs-completed or finite-stage-vs-limit; object-conflation; status-inflation.

### 3. BLUE Pass — Attack Consistency
Theorem/proof/status mismatch; label prefix/uniqueness drift; stale Part references; compute/manuscript disagreement; README or notes outclaiming .tex; cross-volume inconsistencies.

### 4. GREEN Pass — Attack Gaps
Missing definitions; hidden imported lemmas; unsupported converses; dangling references; true statement weaker than advertised.

### 5. Patch in Dependency Order
CRITICAL and SERIOUS first, then MODERATE. For each: (a) re-read local context, (b) re-derive or recompute independently, (c) smallest truthful edit, (d) immediately search for downstream advertisements.

### 6. Propagate
After any mathematical change: grep Vol I; grep Vol II; grep Vol III. Update genuine duplicates or leave explicit pending note.

### 7. Verify
Narrowest check that can falsify: targeted pytest; grep for forbidden formulas/stale labels/banned prose; targeted TeX build; metadata check.

### 8. Hostile Re-Read
Reread your own rewrite as an adversary. Try to break it.

### 9. Stop Condition
- **CONVERGED**: no known actionable MODERATE+ issue remains on the modified surface, and narrowest verification passes.
- **BLOCKED**: exact blocker named precisely, with the strongest truthful narrower statement identified.

Do not stop between those states.

## XVIII. Convergent Writing Loop

For introductions, prefaces, chapter openings, and load-bearing prose:

`WRITE → REIMAGINE → REWRITE → BEILINSON AUDIT → REIMAGINE AGAIN → REWRITE AGAIN → CONVERGE`

Minimum: preface/introduction 3+ iterations; chapter openings 2+.

Reimagination channels: Gelfand (inevitability), Beilinson (falsification), Drinfeld (unifying principle), Kazhdan (compression), Etingof (clarity), Polyakov (physics=theorem), Nekrasov (seamless passage), Kapranov (higher structure IS math), Ginzburg (every object solves a problem), Costello (factorization), Gaiotto (dualities compute), Witten (physical insight precedes proof).

CG structural moves: deficiency opening; unique survivor; instant computation; forced transition; decomposition table; dichotomy; sentence-as-theorem.

## XIX. Claim-Status Discipline

Every serious statement: exactly one of `\ClaimStatusProvedHere`, `\ClaimStatusProvedElsewhere`, `\ClaimStatusConditional`, `\ClaimStatusConjectured`, `\ClaimStatusHeuristic`, `\ClaimStatusOpen`.

Rules:
- ProvedHere = verify proof proves stated claim; status tag != ground truth
- Conjectured → \begin{conjecture}; ProvedElsewhere → theorem + Remark[Attribution]
- When downgrading theorem→conjecture: rename thm:foo→conj:foo AND update every \ref atomically
- README may not outclaim live manuscript
- Tag only genuinely new content ProvedHere; classical parts ProvedElsewhere with attribution

## XX. Cross-Volume Propagation Discipline

- Never assume a fix is local if the claim is formula-level, status-level, or bridge-level
- Before changing shared formula/theorem: grep all three volumes
- After changing: grep again for stale copies
- Never hardcode Part numbers: use \ref{part:...}
- When correcting engine formula: derive new expected independently before changing tests
- Convention conversion required between volumes (OPE→lambda-bracket→motivic)
- Build artifacts and release PDFs are downstream, not authoritative

## XXI. Prose and Formatting Discipline

Banned (case-insensitive): moreover, additionally, notably, crucially, remarkably, interestingly, furthermore, "we now", "it is worth noting", "worth mentioning", "it should be noted", delve, leverage, tapestry, cornerstone, landscape (metaphor), journey, navigate (non-geometric).
Em-dash (---, U+2014) FORBIDDEN. Use colons, semicolons, separate sentences.
Hedging ban in math: arguably, perhaps, seems to, appears to. State or mark conjecture.
No Markdown in LaTeX: no backtick numerals, no **bold**, no _italic_. Use $...$, \textbf, \emph.
Post-write grep MANDATORY on touched .tex files.

## XXII. Failure Mode Awareness (GPT-5.4 / Opus 4.6)

Model-specific failures from ~100 agent invocations on this manuscript.

**Formula drift**: FM1 (generic-formula attractor: bare Omega/z), FM2 (level-prefix drop on summarisation), FM3 (bc/bg conflation), FM9 (H_{N-1} vs H_N-1 at N=2: H_1=1 vs H_2-1=1/2), FM13 (auto-complete to majority variant), FM21 (wrong prefactor: 7/5760 not 7/2880), FM30 (S_2=c/12 divided-power confusion; S_2=kappa=c/2 always), FM31 (asymptotic cancellation: 10/(5c^2)=2/c^2 not 2/(5c^2))

**Categorical confusion**: FM4 (k=0 vs k=-h^v), FM11 (Sugawara shift missing: av(r)+dim(g)/2=kappa for non-abelian), FM23 (local-global on curves: point≠D≠A^1≠P^1), FM24 (B-cycle i^2: q becomes real), FM25 (SC disaster: B(A) is NOT SC-coalgebra — entire false framework), FM26 (false SC self-duality: dim check fails), FM27 (scope inflation in metadata), FM28 (topologization scope: proved KM only), FM32 (pi_3(BU)=pi_2(U)=0, not Z), FM33 (formula outside hypothesis domain), FM34 (excision/coproduct: ⊗_A vs plain ⊗)

**Structural**: FM5 (wrong Lie dims), FM6 (undefined macros in standalone), FM7 (LaTeX }→>), FM8 (universal-quantifier drift on uniform-weight), FM10 (hardcoded Part numbers), FM14 (label/env mismatch on downgrade), FM15 (duplicate labels across volumes), FM16 (silent kappa-family conflation), FM17 (amplitude/dimension conflation), FM18 (d_gen/d_alg conflation: Vir d_gen=3 d_alg=inf), FM19 (fiber-base: dtau on curve vs omega_g on moduli), FM20 (iff-drift: prove → and claim ↔)

Full catalog FM1-FM34 with counters: see CLAUDE.md §Opus 4.6 Quirks and Failure Modes.

## XXIII. Theorem Status Table (Rectified 2026-04-13, 732-agent assault survived)

Every main theorem now has 2+ independent proof paths. See CLAUDE.md for full details.

| Thm | Status | Rectification + Alt Proof |
|-----|--------|--------------------------|
| A | PROVED | Verdier at algebra post-D_Ran; lem:filtered-comparison-unit written. ALT: Lurie nerve-realization |
| B | PROVED | On-locus qi + off-locus coderived (non-circular). ALT: Keller+Kontsevich formality |
| C | PROVED | C0 D^co unconditional; C1 g>=1 perfectness; C2 uniform-weight. ALT: PTVV shifted symplectic |
| D | **GENUS-1 PROVED; ALL-GENERA CONDITIONAL (AP225)** | Circularity broken. BUT: all-genera universality gap (clutching-uniqueness NOT proved). Genus-1 obs_1=kappa*lambda_1 unconditional. All-genera conditional on clutching-uniqueness or independent GRR. ALT: GRR sketch (H04). |
| H | PROVED | Verdier chain fixed; FM-formality collapse. ALT: deformation-theoretic dimension |
| MC1-4 | PROVED | PBW Whitehead explicit; MC2 g^mod; MC3 Baxter b=a-1/2; MC4 pole-order filtration |
| MC5 | CODERIVED PROVED | Coacyclic clean; harmonic derived. Chain M: conjectural. ALT: operadic Koszul |
| Koszul | 10+1+1 | (vii) uniform-wt all-genera; (viii) Massey conditional. ALT: proof web +3 cross-links |
| D^2=0 | PROVED | Universal family (space corrected). Arnold relation on FM |
| Theta_A | PROVED | Bar-intrinsic. ALT: KS scattering diagram |
| SC-formal | PROVED | Operadic both directions. ALT: tower truncation |
| Depth gap | PROVED | Witness corrected; 3 impossible via MC+Jacobi. ALT: shadow Lie |
| ChirHoch^1 KM | PROVED | = g; total dim = dim(g)+2 |
| Topologization | COHOM PROVED (KM); qi-model chain (KM); CONJECTURAL general | ALT: CFG factorization |

57 new anti-patterns catalogued: AP186-AP233, B74-B78, FM35-FM38. Full catalogue: `compute/audit/new_antipatterns_wave12_campaign.md`.

**AP225 WARNING (CRITICAL):** Theorem D all-genera universality gap. The passage from genus-1 obs_1=kappa*lambda_1 to all-genera obs_g=kappa*lambda_g relies on thm:genus-universality whose proof is incomplete (scalar saturation does not uniquely force lambda_g). Genus-1 is unconditional. All-genera requires clutching-uniqueness or independent GRR. See AP225-AP233 for the full set of deep structural findings from the mega rescue campaign.

Recovery infrastructure: `scripts/resume_failed.py` (idempotent), `scripts/campaign_dashboard.py` (status).

## XXIV. Skill Routing (Claude ↔ Codex)

Every Claude skill has a Codex home. No durable workflow is Claude-only.

| Claude Skill | Codex Skill (.agents/skills/) | Trigger |
|-------------|-------------------------------|---------|
| `/build` | `build-surface` | build, test, compile, verify |
| `/audit [target]` | `deep-beilinson-audit` | audit, falsify, red-team, pressure-test, verify |
| `/rectify [file]` | `beilinson-rectify` | rectify, fortify, tighten, repair |
| `/beilinson-rectify [file]` | `beilinson-rectify` | same as /rectify (heavier variant) |
| `/chriss-ginzburg-rectify [file]` | `chriss-ginzburg-rectify` | chapter-scale structural rewrite, CG convergence, introductions, prefaces |
| `/verify [claim]` | `multi-path-verify` | verify formula, invariant, computational claim |
| `/propagate [pattern]` | `cross-volume-propagation` | AP5 sweep, cross-volume formula/status fix |
| `/compute-engine [name]` | `compute-engine-scaffold` | new engine with multi-path tests |
| `/rectify-all` | swarm of `beilinson-rectify` | full-volume parallel rectification (user-authorized) |
| `/beilinson-swarm` | swarm of `beilinson-rectify` | parallel chapter rectification (user-authorized) |
| `/research-swarm [topic]` | `frontier-research` | frontier synthesis, research architecture |
| — | `claim-surface-sync` | theorem/status/concordance/label drift |

**Both `/rectify` and `/chriss-ginzburg-rectify` are available in BOTH Claude (via CLAUDE.md skill definitions) and Codex (via `.agents/skills/beilinson-rectify/SKILL.md` and `.agents/skills/chriss-ginzburg-rectify/SKILL.md`).** Use `beilinson-rectify` for targeted chapter/proof repair; use `chriss-ginzburg-rectify` for chapter-scale structural rewriting with convergent loop.

Codex skill invocation: when a task matches a skill trigger, use the skill instead of reconstructing the workflow. Skills live in `.agents/skills/SKILL_NAME/SKILL.md`.

Swarm delegation: only with explicit user authorization. Split by independent scope, not overlapping edits.

Default reasoning effort: `medium`. Escalate to `high`/`xhigh` only for proof surgery, chapter-scale structural repair, or stalled frontier synthesis after task definition and falsifier are already sharp.

## XXV. Hook Architecture

Codex hooks in `.codex/hooks.json` provide deterministic guardrails:

- **SessionStart**: injects live-surface reminder and skill map
- **UserPromptSubmit**: routes prompts toward matching Codex skills
- **PreToolUse (Bash)**: blocks destructive shell habits, warns on commit/source-edit paths
- **PostToolUse (Bash)**: refuses to let failing build/test output count as verification
- **Stop**: forces rectification-style work to close as CONVERGED or BLOCKED

Hook rule: hooks are deterministic guardrails, not substitutes for judgment. If a workflow repeats and does not belong in always-on context, move it to a skill instead of bloating AGENTS.md.

## XXVI. Codex / GPT-5.4 Task Intake

Before any nontrivial work, lock these eight items:

1. The exact target file, theorem, formula, bridge, engine, or live surface
2. The task type: audit, rectification, formula verification, status sync, compute/test repair, build triage, or frontier synthesis
3. The active convention bridge: grading, shifts, OPE vs lambda-brackets, genus/degree scope, ordered vs symmetric bar, Vol I vs Vol II vs Vol III normalization
4. The live evidence surface: source, nearby context, diff, logs, tests, citations
5. The narrowest falsifier that could kill the current claim
6. The propagation surface across three volumes
7. The dirty collision surface in every repo involved
8. The matching skill, if a repo skill applies

If the user prompt is underspecified, infer the smallest defensible scope only after reading the live surface.

## XXVII. Build & Test

```bash
# Vol I
pkill -9 -f pdflatex 2>/dev/null || true; sleep 2; make fast
make test          # fast tests
make test-full     # all tests (~120K)

# Vol II
cd ~/chiral-bar-cobar-vol2 && make

# Vol III
cd ~/calabi-yau-quantum-groups && make fast

# Census
python3 scripts/generate_metadata.py
```

CAUTION: Watcher spawns competing pdflatex; always kill before builds.

## XXVIII. Git Rules

All commits authored by Raeez Lorgat. NEVER credit an LLM. No co-authored-by, no generated-by, no AI attribution anywhere. git stash FORBIDDEN (use git diff > patch.diff + git apply). Constitution: concordance.tex.

## XXIX. Session Protocol

1. Read CLAUDE.md + AGENTS.md
2. Build: `pkill -9 -f pdflatex; sleep 2; make fast`
3. Tests: `make test`
4. `git log --oneline -10`
5. Read .tex source before any edit (never from memory)
6. After each change: build+test. After each correction: grep ALL THREE volumes (AP5)
7. Never guess a formula: compute or cite landscape_census.tex (AP1)
8. Apply convergent writing loop to all prose
9. Session end: build all three volumes, run tests, summarize errors by class
10. Before first Edit: run Hot Zone check (§XIII) + Pre-Edit Verification (§XVI)

## XXX. Structural Facts

**Shadow tower**: Theta_A := D_A - d_0 is MC (thm:mc2-bar-intrinsic). kappa, C, Q are projections. All-degree convergence PROVED. G/L/C/M classification.
**Convolution**: dg Lie Conv_str is strict model of L-inf Conv_inf. MC moduli coincide. Full L-inf needed for transfer/formality/gauge equivalence.
**E_1 primacy**: B^ord primitive (Stasheff). av: g^{E1}→g^mod lossy Sigma_n-coinvariant projection. av(r(z))=kappa at degree 2. All standard chiral algebras E_inf (local); E_1=nonlocal (Yangian, EK quantum VA). NEVER "E_inf means no OPE poles."
**Three pillars**: (1) Conv sL-inf hom_alpha(C,A) NOT strict Lie. (2) hom_alpha fails as bifunctor in both slots simultaneously (RNW19). MC3 one slot at a time. (3) Log FM != classical FM; requires snc pair (X,D).

## XXXI. Session 2026-04-12/13 Results (Load-Bearing)

These results change what is TRUE in the manuscript. Every agent must know them.

**Proved this session:**
- thm:e3-identification: Z^der_ch(V_k(g)) ≅ CFG A^lambda for simple g. Route: E_3 formality + H^3(g)=C + P_3 matching.
- thm:glN-chiral-qg: W_N chiral QG for ALL N≥1. Yang R(u)=uI+Psi*P. OPE compat by coderivation+JKL.
- prop:verlinde-from-ordered: Z_g = sum S_{0j}^{2-2g} from ordered chiral homology at integer level.
- prop:e3-via-dunn: Alternative E_3 proof via CG factorization + Sugawara + Dunn. Independent of HDC.
- Z_2(k) = binom(k+3,3). Z_3(k) = n²(n²-1)(n²+11)/180, n=k+2.
- (Psi-1)/Psi universal across spins (thm:miura-cross-universality, PROVED from Miura factorization, verified spin 2-6).
- DS intertwining (pi_3×pi_3)∘Delta_z = Delta_z^{W_3}∘pi_3 verified (57 tests).
- E_3 extended to gl_N (two independent bilinear forms B_tr, B_ab).

**Corrected this session:**
- (Psi-1)/Psi NOT 1/Psi on J⊗J in Delta_z(T). AP128.
- nabla = d-A NOT d+A (23 sign fixes). FM29.
- Belavin r-matrix: Pauli decomposition NOT Weierstrass zeta. FM30.
- Theta rank = 1 NOT 2 (betagamma). 
- sl2_bar_dims h_2=6 is CE; chiral bar h_2=5. AP63/AP128/B22.
- qdet column ordering: DECREASING index (j=N-1 leftmost). FM33.
- Heat equation prefactor: 1/(4πi) diagonal, 1/(2πi) off-diagonal. FM34.
- 3 cross-volume r-matrix convention discrepancies fixed.

**Codex/GPT-5.4 specific failure patterns (from 60-agent campaign):**
- Engine-test synchronization to wrong value (AP128): the engine and its test can share the same wrong mental model. ALWAYS derive expected values from an INDEPENDENT source.
- Fixture infrastructure: pytest fixtures must be defined in the test file or conftest. Missing fixtures cause silent errors that look like test failures.
- Column determinant ordering: textbook conventions vary. Always verify centrality numerically at N≥3 before trusting a formula.
- Spectral coassociativity uses SHIFTED parameters, not the same z: (Delta_{z1}⊗id)∘Delta_{z1+z2} = (id⊗Delta_{z2})∘Delta_{z1}.
- AP128 found THREE times this session: spin-2 c_eff, bar H^2=6→5, comb(d+2,2)→comb(d+2,3).
- Face model bypasses vertex-IRF: when vertex-model DYBE fails numerically, use IRF Boltzmann weights directly.
- Miura proof: Prochazka-Rapcak factorization T(u)=prod(u+Lambda_i) → elementary symmetric expansion → 1/Psi coefficient.
- Drinfeld center dim < derived center dim: Ext^1,2 invisible to commutant.
- **FM35 (CONSTITUTIONAL): NEVER revert mathematical content to fix build errors.** Fix the LaTeX (add macros, close environments) while preserving every line of mathematics. Reverting content to make a build pass destroys agent work. The correct response to 100 undefined-macro errors is 100 \providecommand lines, NOT git checkout.

**Final session state (2026-04-13, 130 commits):**
- 2 conjectures → theorems (E_3 identification, Miura universality)
- 6d hCS defect = W_{1+inf} PROVED. DDYBE verified (face model). Drinfeld center verified (Heisenberg).
- Chain-level E_3: Steps 1-2 proved, Step 3 open. Toroidal Delta_{z,w} conjectured.
- ~1,500 new tests. ~4,750pp. Zero gaps in manuscript.

## XXXII. End-of-Task Output Contract

For every substantial mathematical task, end with:

1. The exact claim surface audited
2. What was proved internally vs only supported computationally
3. What remains conditional, conjectural, heuristic, or open
4. What verification was run
5. What propagation was completed or explicitly left pending

If blocked: name the exact blocker and the strongest truthful narrower statement.

## XXXII. Style of Action

Be decisive, but skeptical. Read before editing. Verify before advertising. Prefer the live source over inherited narrative. Prefer the narrowest falsifier over broad "confidence." Prefer one true local theorem over one false grand synthesis.
