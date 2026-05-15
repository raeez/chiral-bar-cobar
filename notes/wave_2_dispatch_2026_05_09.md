# Wave 2 dispatch design — 2026-05-09

> Wave 1 closed with 29 of 29 agents converged. This document plans
> Wave 2 in the same dispatch protocol (`notes/manuscript_reconstitution_kickstart.md`),
> driven by what Wave 1 surfaced: substantive math, not bookkeeping.

## Wave-1 closure summary

29/29 agents PASS. Five new files registered in `main.tex`:
`chapters/connections/master_reconstruction.tex`,
`appendices/type_system.tex`,
`chapters/connections/vertical_equivalence_level_0.tex`,
`appendices/vertical_equivalence_level_2.tex`,
`chapters/connections/vertical_equivalence_level_4.tex`.
13 chapter files swept (B1–B13); 4 standalone papers updated (D-A, D-C,
D-M, D-N); 5 archetype rows of the $5{\times}5$ $\kappa$-matrix
populated (C-G/L/C/M/B); MA-1…MA-13 inscribed in the AP register.

Healings inscribed during integration on the main thread:
- `S_6 = 80(45c+193)/[3c^3(5c+22)^2]` corrected in `CLAUDE.md` and the
  stale memory entry; verified by independent recursion.
- Chain-homotopy notation collision resolved: `theorem_A_infinity_2.tex`
  now distinguishes $\kappa^!_{\mathrm{alg}}$ from $\kappa^!_{\mathrm{LV}}$
  via `Convention conv:A-two-kappa-shriek`; the universal formula now
  reads $h_{A_b}=h_{\mathrm{LV}}/\mathcal N(A_b)$.
- Cross-volume label hygiene: V3-prefix phantomsection stubs added for
  all Vol III labels invoked from the new vertical-equivalence files;
  broken `\cite{cy_to_chiral.tex}` syntax repaired in
  `vertical_equivalence_level_0.tex`.

## Wave 1 audit findings → Wave 2 targets

The two substantive findings beyond healings already inscribed:

1. **5×5 $\kappa$-matrix column convention drift.**  Cluster C agents
   (C-G, C-L, C-C, C-M) use inconsistent column assignments for the
   modular characteristic $\kappa(\mathcal A)$.  C-M places $c/2$ in
   $\kappa^{\mathrm{Hodge}}_{\mathrm{ch}}$, B7 places it in
   $\kappa^{\mathrm{Heis}}_{\mathrm{ch}}$ (with footnote ‡ acknowledging
   the Sugawara-channel reading is shadow-only).  C-C reports
   $\kappa^{\mathrm{Hodge}}_{\mathrm{ch}}=c/2$ for $\beta\gamma_\lambda$
   in the C row.  See `notes/chain_homotopy_audit_2026_05_09.md`
   §"Companion finding".

2. **Chain-homotopy proof depth.**  The Priddy contraction
   normalisation $\mathcal N(A_b)$ is recorded in the proposition,
   but the proof of the case-by-case witness scalars (especially
   class M, where the Zamolodchikov norm $c(5c+22)/10$ enters via the
   Felder BRST contraction) remains a citation, not a worked
   computation.

## Wave-2 clusters (new)

Each cluster is dispatch-ready in the same per-agent template form
used by Wave 1 (kickstart §"Per-agent prompt template"); per-agent
absolute prohibitions identical (no destructive git, no edits outside
target file(s), no AI attribution, no make/build).

### Cluster F — compute-engine extension

| Agent | Target | Deliverable |
|---|---|---|
| F1 | `compute/lib/kappa_stratification.py` | Unify the 5 archetype-row engines (test_kappa_stratification_{G,L,C,M,B}.py) into one canonical computation library; expose $\mathcal N(A_b)$ and $K^\kappa(A_b)$ as separate functions (per the new convention) |
| F2 | `compute/tests/test_master_reconstruction.py` | Test the four properties (M1)–(M4) of `thm:mr-master`; verify each forgetful step's reconstruction theorem is exercised end-to-end on at least two archetypes |
| F3 | `compute/tests/test_chain_homotopy_norm.py` | Verify the witness table $\mathcal N(\mathsf G,\mathsf L,\mathsf C,\mathsf M,\mathsf B) = (1, 2(k+h^\vee), 1, c(5c+22)/10, 8)$ by independent computation per archetype |

### Cluster G — cross-repo bridges

| Agent | Target | Deliverable |
|---|---|---|
| G1 | `~/chiral-bar-cobar-vol2/CLAUDE.md` | Mirror Vol I platonic-ideal architecture (Open Beilinson tower, KSDual, MA-1..MA-13); inscribe Vol II's role at levels 3 and 5 (vertical equivalences) |
| G2 | `~/calabi-yau-quantum-groups/CLAUDE.md` | Mirror; inscribe Vol III's role at levels 0/1/2/4/5 |
| G3 | Vol II `chapters/...` | Inscribe vertical-equivalence cross-references aligned with `vertical_equivalence_level_3` (Vol II's $\mathsf{SC}^{\mathrm{ch,top}}$-brace bulk) — write a NEW `chapters/connections/vertical_equivalence_level_3.tex` companion in Vol II |

### Cluster H — standalone-paper second wave

Targets for MA-1..MA-13 sweeps and type-signature passes:

| Agent | Paper | Primary master-pattern target |
|---|---|---|
| H-B | Paper B `standalone/shadow_towers_v3.tex` | MA-6 (five $\kappa$ are not one); inscribe new $5{\times}5$ matrix in abstract |
| H-E | Paper E `standalone/en_chiral_operadic_circle.tex` | MA-5 (E_1-bar does not explain HT uplift); MA-7 (one-stage $\Phi_d$ forbidden) |
| H-F | Paper F `standalone/chiral_quantum_groups_gln.tex` (or extant filename) | MA-8 ($Y^+(X) \neq G(X)$ without Hall pairing + completion + integral form + descent) |
| H-K | Paper K `standalone/sc_chtop_pva_descent.tex` | type signatures; cross-volume references with $(\Sigma_{d-1},C)$ |
| H-L | Paper L `standalone/holographic_datum.tex` | alignment with `master_reconstruction.tex`; type signatures; KSDual scope |

### Cluster I — open-frontier sharpening

| Agent | Frontier | Deliverable |
|---|---|---|
| I-F8 | F8 chart-class enumeration | Enumerate Morita-equivalence classes of $(\mathcal C, b)$ presentations per archetype G/L/C/M/B; inscribe the enumeration as a theorem in `chapters/examples/landscape_census.tex` (per archetype, list # of Morita classes + class-distinguishing invariant) |
| I-F11 | F11 operator-level Pfaffian | Define the virtual $K_0$-determinant package precisely (K_0 of the Mukai stack of K3 sheaves; reduction-of-structure-group; Bruinier–Heegner reciprocity); state the operator-level Pfaffian conjecture with hypothesis package; inscribe in `standalone/determinant_of_an_operator.tex` as a sharpened §"open frontier" |
| I-F2 | F2 multi-weight $\delta F_g^{\mathrm{cross}}$ at $g=2$ | First-principles computation of the cross-channel correction at $g=2$ for class M; inscribe in `compute/tests/test_multi_weight_g2.py` and a new corollary in `chapters/theory/higher_genus_modular_koszul.tex` |

### Cluster J — healings (Wave-1 audit completions)

| Agent | Target | Deliverable |
|---|---|---|
| J-1 | Done in main thread (chain-homotopy notation healing); no-op | (closed; for record) |
| J-2 | `chapters/examples/landscape_census.tex` §$5{\times}5$ matrix | Reconcile B7 and Cluster C column assignments; pin a single canonical reading per archetype × column; update the row M and row C entries to remove the c/2 / 0 disagreement; introduce a separate $\kappa_{\mathrm{mod}}$ column (for the modular characteristic) if the 5 columns truly do not house it |
| J-3 | `.claude/hooks/beilinson-gate.sh` | Update the hook with the MA-1..MA-13 detection regexes inscribed by Wave-1 agent A3; verify on 5 random Wave-1-touched files; tune for low false-positive rate |

## Dispatch sequencing

Cluster F (compute) and Cluster J (healings) are independent; can run
in parallel.  Cluster G (cross-repo) writes to neighbouring repos and
should run after Cluster F so Vol II/III bridges can cite the new
unified `compute/lib/kappa_stratification.py`.  Cluster H (standalone
papers) and Cluster I (frontiers) are parallelisable internally; Cluster
H can launch immediately, Cluster I requires the
`master_reconstruction.tex` chapter to be settled first (Wave-1
inscription, now in main.tex).

Recommended max parallelism: 14 agents (3 F + 3 G + 5 H + 3 I).  Sub-batch
J-2 runs sequentially after F2 (depends on F2's column-definition
output).

## Convergence criteria

- Cluster F: tests pass on `make test`; new functions exposed in
  `compute/lib/kappa_stratification.py`.
- Cluster G: Vol II/III `CLAUDE.md` files contain the platonic-ideal
  architecture mirror, KSDual fixed-locus statement, MA-1..MA-13
  master-pattern table, vertical-equivalences table.
- Cluster H: each paper's abstract and theorem statements carry type
  signatures; 0 occurrences of forbidden master-pattern slogans
  (MA-detection regex).
- Cluster I: F8 enumeration inscribed per archetype with primary
  citations; F11 hypothesis package precise enough to dispatch a
  follow-up proof attempt; F2 closed form $\delta F_g^{\mathrm{cross}}$
  at $g=2$ on class M, verified by 3 paths.
- Cluster J: J-2 reconciles the 5×5 column assignments;
  J-3 hook tuned and verified.

## Risks

- Cluster G writes to neighbouring repos.  Verify the destructive-git
  prohibition is honoured in those repos (each has its own
  `~/ecosystem/INVARIANTS.md` inheritance chain).  Per-repo git status
  audit before main thread commits.
- Cluster I-F11 (operator-level Pfaffian) is a major mathematical
  problem.  Wave-2 deliverable is the precise statement of the
  problem with hypothesis package; the proof attempt itself is
  Wave-3+ scale.
- Rate-limit recurrence (as in Wave 1, where 11 of the original 29
  agents required retry-2): keep concurrent dispatch ≤ 14 to reduce
  the chance of cumulative server-side throttling.
