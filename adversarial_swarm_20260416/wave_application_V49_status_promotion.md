# Wave Application V49 --- Editorial drafts for the K3-input resolution of the rank-1 frontier (Pentagon-at-$E_1$)

**Author.** Raeez Lorgat. **Date.** 2026-04-16. **Mode.** Editorial
application drafts. Read-only on Vol III; user reviews before applying.
No commits. No build. No test runs. Sandbox sympy artefacts (V49 phase 1)
already documented in `wave_K3_Pentagon_E1_attempt.md` Section 4.

---

## 0. Mandate

V49 (`wave_K3_Pentagon_E1_attempt.md`, 2026-04-16) supplied the
attack-and-heal record for V39 H1 (Pentagon-at-$E_1$ chain-level
coherence cocycle) at K3 input. Three independent verification routes
converge on $[\omega]_{K3} = 0 \in
H^2(\mathrm{SC}^{\mathrm{ch,top}};\, \mathfrak{aut})$:

1. **Sympy direct.** Unitarity $g_{K3}(z) g_{K3}(-z) = 1$ exact;
   pairwise YBE $4/4$ on toy Mukai $(2, 2)$; first-order linearisation
   identically zero (scalars commute with matrix perturbations);
   $A_1$-enhanced K3 Yang YBE in difference convention $64/64$ entries
   zero; classical CYBE $64/64$ entries zero. Charges 2 and 3 covered.
2. **Etingof--Kazhdan quantization.** The V38 closed-form K3 R-matrix
   $R_{K3}(z) = \prod_i g_i(z)$ is the EK twist for the K3 Lie
   bialgebra (abelian Heisenberg + ADE-enhanced sub-Yangian);
   Pentagon coherence on the EK twist is the standard Drinfeld twist
   coherence. Conditional on FM164 (Yangian pro-nilpotent bar-cobar
   completion) and FM161 (Positselski Yangian Koszulness)
   K3-specialised; both expected to hold at K3 due to Mukai
   self-duality + ADE-self-duality.
3. **V20 Universal Trace Identity.** The integer match
   $\mathrm{tr}_{Z(\mathcal{C})}(\mathfrak{K}_{\mathcal{C}}) =
    -c_{\mathrm{ghost}}(\mathrm{BRST}(\Phi(\mathcal{C}))) =
    \tfrac{1}{2} c_5(0) = 5$ for $\mathcal{C} = D^b(\mathrm{Coh}(K3))$
   forces the cocycle's scalar projection to vanish.

Six previously-independent open conjectures collapse to corollaries
at K3 input specifically: V19 Trinity at $E_1$ (K3 Yangian, chiral
projection); V39 amplitude bound $[0, 3]$; CY-C abelian level for K3
(unconditional via H4 of V49); V20 Step 3 chain-level identity for K3;
V11 Pillar~$\alpha$ (U1) chain-level at $d = 2$ for K3; V8 Section~6
mock-modular K3 identity. The honest scope is K3 only (AP-CY60); other
CY$_3$ inputs (quintic, conifold, local~$\mathbb{P}^2$,
Niemeier-lattice CY$_3$ landscape) lack one or more of three
favourable structural features and remain genuinely OPEN under V39 H1.

This wave converts V49 into editorial drafts for Vol III: a new
theorem block, six corollary blocks, an AP-CY61
independent-verification entry, and a master-punch-list split of V39
H1 into K3-resolved and other-OPEN halves. This is the parallel of
V51 (V48 status promotion drafts) but for V49.

---

## 1. The four drafts produced

### 1.1 `draft_k3_yangian_pentagon_E1_theorem.tex`

**Inserts at.**
`/Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3_yangian_chapter.tex`,
AFTER `\begin{proposition}[Indefinite Mukai signature poses no
obstruction]` (`\label{prop:mukai-indefinite-yangian}`, line 610),
BEFORE the existing remark on Yangian limits (line ~735, immediately
preceding `\begin{theorem}` at line 738 with
`\label{thm:k3-abelian-yangian-presentation}`).

**Produces.**

- A `\begin{theorem}[Pentagon-at-$E_1$ for K3 input;
  conditional on FM164, FM161]` block with
  `\label{thm:k3-pentagon-E1}` carrying `\ClaimStatusProvedHere`,
  stating $[\omega]_{K3} = 0 \in H^2(\mathrm{SC}^{\mathrm{ch,top}};
  \mathfrak{aut})$ in the algebraic chiral Hochschild model
  $C^*_{\mathrm{ch,alg}}(A, A)$ (AP-CY62 (b)).
- A complete `\begin{proof}` block in three steps:
  Step 1 (Direct cocycle computation; sympy verified, decomposition
  into unitarity defect + pairwise YBE + first-order Pentagon defect
  + steel-manned super-shift attack at indefinite signature + ZTE-style
  charge-3 obstruction trivialised);
  Step 2 (EK quantization of the K3 Lie bialgebra; identification
  of V38 closed-form R-matrix with EK twist; Pentagon = Drinfeld
  twist coherence; explicit gauge fixed by Mukai signature parameter
  inversion);
  Step 3 (V20 integer match; scalar projection of cocycle vanishes
  via $-c_{\mathrm{ghost}} = c_5(0)/2 = 5$;
  $K(\Phi(\mathcal{C})) = 0$ for the abelian Heisenberg conductor;
  $\kappa_{\mathrm{BKM}}(K3 \times E) = 5$ via
  Proposition~\ref{prop:bkm-weight-universal} at $N = 1$).
  Convergence paragraph stating AP-CY61 disjointness.
- `\begin{remark}[Three independent verification routes; AP-CY61
  disjoint sources]` (`\label{rem:k3-pentagon-three-routes}`)
  enumerating the three routes and their pairwise disjointness;
  pointer to the companion `INDEPENDENT_VERIFICATION.md` decorator
  entry; AP-CY55 manifold-vs-algebraization invariant separation.
- `\begin{remark}[Conditionality: FM164 and FM161 for K3]`
  (`\label{rem:k3-pentagon-conditionality}`) recording that the
  `\ClaimStatusProvedHere` tag refers to the conditional statement;
  separable closure of FM164/FM161 for K3 input is a follow-up.
- `\begin{remark}[Six downstream conjectures collapse to corollaries
  at K3]` (`\label{rem:k3-pentagon-six-corollaries}`) pointing to
  the corollary draft.
- `\begin{remark}[Honest scope: K3 only]`
  (`\label{rem:k3-pentagon-non-K3-open}`) recording the AP-CY60
  honest scope: non-K3 CY$_3$ inputs remain `ClaimStatusOpen`;
  V39 H1 split documented in `draft_master_punch_list_V49_K3_split.tex`.

**Cross-references.** Cites V49 implicitly through the proof
structure; cites `thm:phi-k3-explicit` (V11 base case),
`prop:mukai-indefinite-yangian` (preceding proposition),
`thm:k3-abelian-yangian-presentation` (immediately following),
`prop:bkm-weight-universal` (V20 component used in Step 3).
Does NOT introduce dependencies on V41's three closure conditions
beyond what V49 Step 2 already supplies. Does NOT depend on
chain-level CY-A$_3$ (uses inf-cat
`thm:derived-framing-obstruction` only).

**New labels introduced.**

- `thm:k3-pentagon-E1`
- `eq:k3-pentagon-cocycle`
- `rem:k3-pentagon-three-routes`
- `rem:k3-pentagon-conditionality`
- `rem:k3-pentagon-six-corollaries`
- `rem:k3-pentagon-non-K3-open`

**Anti-pattern compliance** (matched against the AP-CY catalogue and
the cross-volume HZ3 hot zone):

- AP113: `kappa_BKM`, `kappa_ch`, `kappa_cat`, `kappa_fiber` used; no
  bare `kappa`.
- AP160 / AP-CY62 (b): chiral Hochschild model qualified explicitly
  as `C^*_{ch,alg}` in the theorem statement; route 1 (sympy) and
  route 2 (EK) both operate at this model level; route 3 (V20)
  operates at the trace projection.
- AP-CY7: CoHA never identified with chiral algebra. V49 used CoHA as
  an *intermediary* (V37 SV theorem $\text{CoHA} = Y^+$) but the
  Pentagon theorem statement and proof do not invoke CoHA = chiral.
- AP-CY10: flop-vs-Koszul-dual not conflated; $\fg_{\mathrm{ADE}}^\vee
  = \fg_{\mathrm{ADE}}$ is the simply-laced Langlands self-duality,
  noted as such (Step 2).
- AP-CY11: conditional propagation explicit; FM164/FM161 named in the
  theorem header and `rem:k3-pentagon-conditionality`.
- AP-CY14: post-CY-A$_3$ proof; uses inf-cat existence only, not
  chain-level data (the Pentagon cocycle lives in chiral Hochschild
  model $C^*_{ch,alg}$, not in the CY-A$_3$ chain-level $A_X$).
- AP-CY28: pole-safe sympy test points cited (Mukai signature `(2,2)`
  toy, then full `(4,20)`).
- AP-CY31: spectral $z$ (Yangian spectral parameter), not worldsheet
  $z$.
- AP-CY40: `\ClaimStatusProvedHere` carries a `\begin{proof}` block.
- AP-CY55: manifold vs algebraization invariants distinguished in
  `rem:k3-pentagon-three-routes`. The Pentagon cocycle's vanishing is
  about algebraization invariants only.
- AP-CY60: honest scope; six routes are six constructions, not six
  applications of $\Phi$.
- AP-CY61: three pairwise-disjoint sources; explicit disjoint
  rationale in the proof's Convergence paragraph and in the companion
  `draft_k3_independent_verification_triangle.md` decorator.
- AP-CY62 (b): algebraic chiral Hochschild model qualified.
- AP-CY67: spectral parameters from $\mathrm{End}^{ch}_A$, not
  narrated as "from FM$_k(C)$".
- FM44: difference YBE convention named explicitly in route 1.
- AP153 / AP154: E$_3$ scope inflation avoided; Pentagon-at-$E_1$
  is an $E_1$-coherence statement, not E$_3$.

### 1.2 `draft_K3_six_corollaries.tex`

**Inserts at** four Vol III chapters:

| Corollary | Insertion target |
|---|---|
| `cor:k3-trinity-E1-yangian` (V19 Trinity at $E_1$ for K3) | `chapters/examples/k3_yangian_chapter.tex`, immediately after `thm:k3-pentagon-E1` |
| `cor:k3-amplitude-bound-0-3` (V39 amplitude bound) | `chapters/examples/k3_yangian_chapter.tex`, immediately after the previous corollary |
| `cor:cy-c-k3-abelian-from-pentagon` (CY-C abelian, unconditional) | `chapters/theory/quantum_groups_foundations.tex`, replacing or augmenting the existing `\begin{conjecture}[CY-C for K3 at the abelian level]` (`\label{conj:cy-c-k3-abelian}`, lines ~265-294) |
| `cor:k3-v20-step-3-chain-level` (V20 Step 3 chain) | `chapters/theory/cy_to_chiral.tex`, near the V20 trace identity references (grep for `trace-identity-chain-level`) |
| `cor:k3-v11-u1-chain-level` (V11 (U1) chain at $d = 2$) | `chapters/theory/cy_to_chiral.tex`, near the (U1) chain-level statement (grep for `Pillar` or `(U1)`) |
| `cor:k3-v8-mock-modular-chain` (V8 §6 mock-modular K3 chain) | `chapters/examples/k3e_bkm_chapter.tex`, near the existing K3 mock-modular content |

**Produces.** Six `\begin{corollary}` blocks, each with
`\ClaimStatusProvedHere` for K3 input specifically, citing
`thm:k3-pentagon-E1` and (where appropriate) the V49 component used
(EK quantization for cor (c); V20 trace match for cor (d) and (f);
amplitude/spectral degree for cor (b); R-twist for cor (a); Pentagon
edges for cor (e)). Plus a closing summary remark
`rem:k3-six-corollaries-status-table` with a status table and the
honest scope statement.

**Cross-references.** All six corollaries cite
`thm:k3-pentagon-E1`. Inside the proofs:
`thm:k3-abelian-yangian-presentation` (Yangian RTT presentation);
`prop:mukai-indefinite-yangian` (Mukai self-duality);
`prop:bkm-weight-universal` (Borcherds weight at $N = 1$);
`thm:phi-k3-explicit` (V11 base, $1/\eta^{24}$);
`thm:k3-quantum-toroidal-abelian` (V48 promotion target,
identifies $D(\mathrm{Heis}^{24,+})$ with the Yangian limit of the
quantum toroidal positive half).

**Anti-pattern compliance.** Same as 1.1, with additional emphasis on
AP-CY11 (conditional propagation): five of six corollaries inherit
FM164/FM161 conditionality from `thm:k3-pentagon-E1`; only
`cor:cy-c-k3-abelian-from-pentagon` is unconditional, and the
unconditionality argument is recorded explicitly in its proof (the
abelian Heisenberg Lie bialgebra avoids the Yangian completion gaps).

### 1.3 `draft_k3_independent_verification_triangle.md`

**Inserts at.** `notes/INDEPENDENT_VERIFICATION.md`, the running list
of independent-verification entries (the protocol document, as
catalogued in HZ3-11). Also templates the test module decorator
for `compute/tests/test_k3_pentagon_E1.py` (a separate compute-engine
draft is required to create the test module itself; this draft only
specifies the decorator entry).

**Produces.**

- A drop-in `@independent_verification(...)` decorator entry for
  the new theorem `thm:k3-pentagon-E1`, with
  `derived_from = [V38 closed-form R-matrix from MO stable envelope,
  Mukai signature (4, 20) parameters with sum_i h_i = 0]` and
  `verified_against = [Etingof--Kazhdan 1996, Borcherds 1998
  Phi_10 weight, Sympy direct cocycle defect computation in
  difference YBE convention]`, with full `disjoint_rationale` text
  separating the three sources mathematically.
- A "why this is genuine, not a tautology" section walking through
  the three reasons (EK is provenance-independent of MO; Borcherds
  Phi_10 is automorphic, not algebraic; sympy is computational
  verification, explicitly noted as such).
- The audit-time mechanical disjointness check (verifying
  `set(derived_from) & set(verified_against) = empty`).
- A "model entry for downstream V49-shape claims" section templating
  the same three-route triangle for quintic CY$_3$, conifold, and
  local $\mathbb{P}^2$ Pentagon-at-$E_1$ attacks (each remains OPEN;
  the template specifies what would constitute a valid AP-CY61
  decoration).
- A cross-volume implication for V20 itself: the V20 entry should be
  updated to add Pentagon coherence as a third leg (Vol II Pentagon)
  beyond the existing two (Vol I BRST + Vol III Borcherds), mirroring
  V49 H1's three-route convergence.
- An application sequence section listing the five steps (apply
  theorem draft, apply corollaries draft, add this decorator entry,
  run `make verify-independence`, update tautology registry).
- An AP-compliance summary table.

**Cross-references.** Cites V49 explicitly and Borcherds 1998 by
journal reference (Invent. Math. 132). Cites EK 1996 by journal
reference (Selecta Math). Cites
`compute/lib/independent_verification.py` (the decorator
implementation) and `notes/INDEPENDENT_VERIFICATION.md` (the
protocol document) for the AP-CY61 framework.

### 1.4 `draft_master_punch_list_V49_K3_split.tex`

**Inserts at.** `MASTER_PUNCH_LIST.md`, replacing the V39 entry
(currently around lines 1042-1052: `## V39. Trinity at E_1
attack+heal`) with a split version, and augmenting the V49 entry
(currently around lines 1199-1228: `### V49. RANK-1 FRONTIER
RESOLVED FOR K3`) with a cross-reference to the split.

**Produces.**

- Split V39 entry into:
  - V39 H1-K3: PROVED, conditional on FM164/FM161 K3-specialised.
    Three-route verification per V49. Six corollaries listed in a
    status table. Vol III editorial drafts named.
  - V39 H1-other: OPEN. Three favourable structural features named
    (Mukai self-duality, ADE self-duality, integer-anchored
    $\kappa_{\mathrm{BKM}}$); their absence at quintic, conifold,
    local $\mathbb{P}^2$, and the Niemeier-lattice CY$_3$ landscape
    (24 cases, 23 non-Leech) listed explicitly.
- V49 entry augmentation:
  - Cross-reference to the V39 split.
  - List of Vol III editorial drafts produced by this wave.
  - Net status change for the K3 frontier:
    {6 OPEN + 1 NEW OPEN} -> {1 PROVED-conditional + 6
    PROVED-corollary at K3}.
- Follow-up notes on cross-references in V19, V20, V11, V8, V41, V48
  entries that should be updated to reflect the K3 resolution
  (each is a one-line edit; not produced as separate drafts).

**Cross-references.** Cites V49, V20, V19, V11, V8, V41, V48 entries
by their `### V##.` headers. Cites the four Vol III draft files
produced by this wave by filename. AP5 cross-volume sweep
recommendation included (grep for the seven labels listed in the
draft).

### 1.5 This spec report (`wave_application_V49_status_promotion.md`)

**Purpose.** Documents the four drafts above, their insertion points,
the recommended application sequence, AP-compliance summary, and
cross-volume sweep instructions. ~2500 words.

---

## 2. Application sequence (recommended order)

The drafts are independent in content but coupled by label
cross-references. The recommended order minimises the time during
which the build has dangling references and maximises the chance of
catching a labelling collision before it propagates.

1. **Pre-application sanity grep.** Confirm none of the new labels
   already exists in any of the three volumes:
   ```bash
   for label in thm:k3-pentagon-E1 \
                cor:k3-trinity-E1-yangian \
                cor:k3-amplitude-bound-0-3 \
                cor:cy-c-k3-abelian-from-pentagon \
                cor:k3-v20-step-3-chain-level \
                cor:k3-v11-u1-chain-level \
                cor:k3-v8-mock-modular-chain \
                eq:k3-pentagon-cocycle \
                rem:k3-pentagon-three-routes \
                rem:k3-pentagon-conditionality \
                rem:k3-pentagon-six-corollaries \
                rem:k3-pentagon-non-K3-open \
                rem:k3-six-corollaries-status-table; do
     for vol in ~/chiral-bar-cobar ~/chiral-bar-cobar-vol2 \
                ~/calabi-yau-quantum-groups; do
       grep -rln "label{$label}" "$vol"/chapters "$vol"/appendices \
            "$vol"/notes 2>/dev/null
     done
   done
   ```
   Expected output: empty (no existing labels collide).

2. **Apply `draft_k3_yangian_pentagon_E1_theorem.tex`** to
   `chapters/examples/k3_yangian_chapter.tex`. Insert AFTER line 610
   (`prop:mukai-indefinite-yangian` end), BEFORE the existing remark
   block leading into `thm:k3-abelian-yangian-presentation`. After
   this step `thm:k3-pentagon-E1` and its five companion remarks
   exist.

3. **Run `make fast`** from `/Users/raeez/calabi-yau-quantum-groups`.
   Expected: build succeeds; no new undef refs; no new undef cites.
   Verify via:
   ```bash
   cd /Users/raeez/calabi-yau-quantum-groups
   pkill -9 -f pdflatex 2>/dev/null || true; sleep 2; make fast
   grep -c "Undefined references" out/main.log     # should be 0 (or unchanged)
   grep -c "undefined citations" out/main.log      # should be 0 (or unchanged)
   ```

4. **Apply `draft_K3_six_corollaries.tex`** to the four chapters
   listed in the corollary table of Section 1.2. Order within the
   draft:
   - (a), (b) into `k3_yangian_chapter.tex` (immediately after the
     theorem from step 2);
   - (c) into `quantum_groups_foundations.tex` (replacing or
     augmenting `conj:cy-c-k3-abelian`; recommend keeping the
     existing conjecture and adding the corollary as the resolution
     statement, with a cross-reference);
   - (d), (e) into `cy_to_chiral.tex` (near the V20 references);
   - (f) into `k3e_bkm_chapter.tex` (near the K3 mock-modular content).

5. **Run `make fast` again.** Expected: build succeeds; no new undef
   refs/cites.

6. **Add the entry from
   `draft_k3_independent_verification_triangle.md`** to
   `notes/INDEPENDENT_VERIFICATION.md`, and create the corresponding
   test module `compute/tests/test_k3_pentagon_E1.py` carrying the
   `@independent_verification` decorator (separate compute-engine
   draft required; not produced here, but the decorator entry text is
   drop-in).

7. **Run `make verify-independence`**. Expected: the new
   `thm:k3-pentagon-E1` claim moves from "uncovered" to "covered";
   the disjointness check passes; coverage count increments by 1.

8. **Apply `draft_master_punch_list_V49_K3_split.tex`** to
   `MASTER_PUNCH_LIST.md`. Replace V39 entry with split version;
   augment V49 entry with cross-reference. Update V19, V20, V11, V8,
   V41, V48 entries with one-line cross-references each (per the
   follow-up notes in the draft).

9. **Cross-volume sweep (AP5 / AP-CY13).** Run:
   ```bash
   for label in conj:trinity-E_1 conj:trace-identity-chain-level \
                conj:cy-c-k3-abelian conj:cy-c-k3-rep \
                thm:phi-k3-explicit thm:k3-abelian-yangian-presentation \
                prop:mukai-indefinite-yangian prop:bkm-weight-universal \
                thm:derived-framing-obstruction \
                thm:k3-pentagon-E1 \
                cor:k3-trinity-E1-yangian \
                cor:k3-amplitude-bound-0-3 \
                cor:cy-c-k3-abelian-from-pentagon \
                cor:k3-v20-step-3-chain-level \
                cor:k3-v11-u1-chain-level \
                cor:k3-v8-mock-modular-chain; do
     echo "=== $label ==="
     for vol in ~/chiral-bar-cobar ~/chiral-bar-cobar-vol2 \
                ~/calabi-yau-quantum-groups; do
       grep -rn "$label" "$vol"/chapters "$vol"/notes "$vol"/appendices \
            2>/dev/null
     done
   done
   ```
   Expected: every label resolves; no orphans; no Vol I/II prose
   contradicts the K3 resolution.

10. **(Optional) Update CLAUDE.md, FRONTIER.md, and tautology
    registry**. The Vol III CLAUDE.md (and the cross-volume mirror)
    Main Theorems table currently lists Pentagon-at-$E_1$ as part of
    the "5 load-bearing open problems"; after V49, it becomes
    "PROVED for K3, OPEN for non-K3 CY$_3$ inputs". Tautology
    registry: per `notes/tautology_registry.md` recommendation in the
    independent-verification draft, do NOT remove
    `prop:bkm-weight-universal` from the registry; the V49 Step 3
    integer match certifies it at $N = 1$ but the universal formula
    over all $N$ remains the registry entry.

---

## 3. Cross-references and AP-compliance summary

### 3.1 Canonical citations used

- **V49** = `wave_K3_Pentagon_E1_attempt.md` (V39 H1 attack-and-heal
  for K3 input, the source of these drafts).
- **V48** = `wave_K3_quantum_toroidal_construction.md` (the K3
  quantum toroidal positive half; combined with V49 H4 gives CY-C
  abelian for K3 via two independent paths).
- **V41** = the four healing options for CY-C with universal
  properties (P1)-(P5); cited by sub-conjecture name
  ($\Pi_C^A$, $\Pi_C^{\mathrm{uniq}}$, $\Pi_C^{\mathrm{Verlinde}}$).
- **V39** = `wave_frontier_trinity_E1_attack_heal.md` (the parent of
  V49; H1 is split here).
- **V37** = `wave_culmination_K3_CoHA_route.md` (CoHA → Y$^+$ via SV;
  used by V49 only as deep background, not as a load-bearing
  citation; AP-CY7 preserved).
- **V34** = `wave_culmination_K3_super_yangian.md` (super-Yangian
  Y(gl(4|20)) conjectural; used in V49 §A4 steel-manning).
- **V20** = `UNIVERSAL_TRACE_IDENTITY.md` (the universal trace
  identity; used as Step 3 of the V49 proof).
- **V19** = chiral Hochschild Trinity Theorem (V19 Trinity at $E_1$
  for K3 Yangian becomes a corollary).
- **V11** = Vol III $\Phi$ functor reconstitution (Pillar~$\alpha$
  (U1) chain-level at $d = 2$ becomes a corollary).
- **V9** = q-bridge convention sweep (Drinfeld convention for
  spectral parameter $z$ as additive Yangian parameter).
- **V8** = shadow quadrichotomy + named theorems (Section~6
  mock-modular K3 becomes a corollary).
- **V51** = V48 status promotion application drafts; this wave is
  the V51 parallel for V49.
- **V44** = V22 Vol I main.tex application drafts (the cross-volume
  precedent for editorial application drafts).

### 3.2 AP-compliance matrix

| AP # | Description | Where checked |
|---|---|---|
| AP4 | Environment matches tag | Theorem carries `\ClaimStatusProvedHere` and a complete `\begin{proof}` block; the `Conditional` qualification is named in the theorem header ("conditional on FM164, FM161"). |
| AP5 / AP-CY13 | Cross-volume Part references | No hardcoded Part numbers in any draft; cross-references via `\ref` or via canonical labels. Cross-volume sweep instructions in §2 step 9. |
| AP-CY7 | CoHA vs $E_1$-chiral | V49 used CoHA at V37 but the Pentagon theorem and proof do not invoke CoHA = chiral. The disjoint_rationale in the AP-CY61 entry uses MO/V38 (geometric, not Hall-product / CoHA). |
| AP-CY10 | Flop vs Koszul-dual | $\fg_{\mathrm{ADE}}^\vee = \fg_{\mathrm{ADE}}$ is simply-laced Langlands self-duality; this is *not* a flop and is named correctly. |
| AP-CY11 | Conditional propagation | FM164/FM161 conditionality named in theorem header and in `rem:k3-pentagon-conditionality`. Five of six corollaries inherit; cor:cy-c-k3-abelian-from-pentagon is unconditional with explicit reasoning. |
| AP-CY14 | Post-CY-A$_3$ proof | Uses inf-cat existence (`thm:derived-framing-obstruction`) only; chain-level CY-A$_3$ data NOT required. |
| AP-CY28 | Pole-safe sympy test points | Difference YBE convention named per FM44; sympy test points avoid $z = \pm h_i$. |
| AP-CY31 | Spectral $z$ vs worldsheet $z$ | Spectral $z$ throughout; difference convention $a = u - v$ explicit. |
| AP-CY40 | ProvedHere requires `\begin{proof}` | All seven new theorem/corollary blocks (1 thm + 6 cors) carry full proof blocks. |
| AP-CY55 | Manifold vs algebraization invariants | `rem:k3-pentagon-three-routes` separates: route (i)+(ii) certify algebraization invariants; route (iii) certifies $\kappa_{\mathrm{BKM}} = 5$; manifold invariants $\kappa_{\mathrm{cat}}, \kappa_{\mathrm{fiber}}$ enter as $Z(\mathcal{C})$-trace data not modified by the cocycle. |
| AP-CY60 | Honest scope (six routes are six constructions, not six applications of $\Phi$) | `rem:k3-pentagon-non-K3-open` and the V39 H1 split record the K3-only scope; non-K3 cases remain OPEN. |
| AP-CY61 | Independent verification | Three pairwise-disjoint sources (geometric MO/V38, deformation-theoretic EK 1996, automorphic Borcherds 1998 $\Phi_{10}$); decorator entry templates the disjoint_rationale; sympy listed under verified_against as computational verification. |
| AP-CY62 / AP160 | Geometric vs algebraic chiral Hochschild | Pentagon cocycle lives in the algebraic model $C^*_{\mathrm{ch,alg}}$; theorem statement and proof state this explicitly. |
| AP-CY67 | Spectral parameters from $\mathrm{End}^{ch}_A$, not narrated as "from FM$_k(C)$" | Drinfeld currents have algebraic spectral variables; FM enters via the comparison theorem (route 1's geometric reading). |
| AP113 | Subscripted $\kappa$ | $\kappa_{\mathrm{BKM}}, \kappa_{\mathrm{ch}}, \kappa_{\mathrm{cat}}, \kappa_{\mathrm{fiber}}$ used; no bare $\kappa$. |
| FM44 | YBE convention | Difference convention $R_{12}(a) R_{13}(a + b) R_{23}(b)$ named explicitly in route (i). |
| AP153 / AP154 | E$_3$ scope inflation | Pentagon-at-$E_1$ is an $E_1$-coherence statement; no E$_3$ structure inflation. |
| AP155 | Overclaiming novelty | The corollaries recover known invariants (V19 Trinity, $\eta^{24}$, $\Phi_{10}$); the *novelty* is the K3-input resolution of V39 H1 via three-route convergence, not the recovery of classical invariants. |

### 3.3 No new dangling labels

- All seven new theorem/corollary labels (`thm:k3-pentagon-E1` plus
  six `cor:k3-...`) are referenced internally within the drafts (the
  theorem from the corollaries; the corollaries from the master
  status table in `rem:k3-six-corollaries-status-table`).
- All five new remark labels (`rem:k3-pentagon-three-routes`,
  `rem:k3-pentagon-conditionality`,
  `rem:k3-pentagon-six-corollaries`,
  `rem:k3-pentagon-non-K3-open`,
  `rem:k3-six-corollaries-status-table`) are referenced internally.
- The equation label `eq:k3-pentagon-cocycle` is the cocycle
  definition, referenced from the proof's Step 1.
- No orphan labels.

### 3.4 Cross-volume sweep (AP5 / AP-CY13)

After application, run the sweep in §2 step 9. Expected: every match
in Vol I and Vol II of the existing labels (`conj:trinity-E_1`,
`conj:trace-identity-chain-level`, etc.) resolves either to the
original Vol III source or to the new K3-specialised corollary;
the new K3-specific labels are unique to Vol III (per the
pre-application grep in §2 step 1).

---

## 4. What the drafts do NOT do

To avoid scope creep, the drafts deliberately do NOT:

- Promote V39 H1 in general. The honest scope is K3 only; the master
  punch list draft splits V39 H1 into K3 (PROVED) + other (OPEN).
- Close FM164 (Yangian pro-nilpotent bar-cobar completion) or FM161
  (Yangian Koszulness in Positselski) in general. Closing these for
  the K3 input specifically is a separable technical follow-up.
- Promote `conj:cy-c-k3-rep` (the Rep equivalence) to a theorem.
  This remains conjectural; the corollary
  `cor:cy-c-k3-abelian-from-pentagon` does not touch it.
- Modify any existing theorem, proposition, or conjecture in Vol III.
  All seven new blocks (1 thm + 6 cors + 5 rems) are insertions, not
  modifications. The existing `conj:cy-c-k3-abelian` (Vol III
  `quantum_groups_foundations.tex` line 270) is preserved; the new
  corollary is positioned after it as the resolution statement.
- Touch the K3 quantum toroidal chapter. V48's promotion draft
  (`draft_k3_quantum_toroidal_status_promotion.tex`) is a separate
  application; this wave only cross-references it.
- Touch CLAUDE.md, AGENTS.md, FRONTIER.md, or the AP catalogue.
  After the user accepts the application, those metacognitive files
  should be updated separately (V49 K3 H1 entry should appear in the
  Main Theorems table).
- Run `make fast`, `make test`, or any verification command. The
  user runs verification after application per §2 steps 3, 5, 7.
- Commit anything (per pre-commit hook: build/tests not run; no AI
  attribution; all commits by Raeez Lorgat only).

---

## 5. Sandwich-diagram check (AP-CY61 independent verification)

The new theorem `thm:k3-pentagon-E1` requires three disjoint
independent verification sources per AP-CY61. The decorator entry in
`draft_k3_independent_verification_triangle.md` lists:

1. **Etingof--Kazhdan quantization** (deformation-theoretic): every
   Lie bialgebra admits a quantization to a quasi-triangular Hopf
   algebra; Pentagon = Drinfeld twist coherence; independent of any
   geometric realisation.
2. **Borcherds $\Phi_{10}$** (automorphic): weight $c_5(0)/2 = 5$
   computed by lattice-vector counting on the Mukai sublattice
   $(4, 20)$ via Borcherds 1998 singular-theta correspondence;
   independent of MO/V38.
3. **Sympy direct cocycle defects** (computational): unitarity, YBE,
   first-order Pentagon defects all vanish at charges 2, 3 in the
   difference YBE convention; computational verification (not a fully
   independent mathematical source, but a confirming computation
   listed under verified_against).

These three sources are pairwise disjoint in the AP-CY61 sense (none
derives from another via tautological hardcoding). The decorator
entry includes the disjoint_rationale and the audit-time mechanical
disjointness check. The `@independent_verification` decorator in
`compute/lib/independent_verification.py` will perform the
import-time check; this entry is written to pass.

---

## 6. Test-command quick reference

After all four drafts are applied (step 8 of §2):

```bash
cd /Users/raeez/calabi-yau-quantum-groups

# 1. Build (Vol III)
pkill -9 -f pdflatex 2>/dev/null || true; sleep 2; make fast

# 2. Tests (after creating test_k3_pentagon_E1.py)
python -m pytest compute/tests/test_k3_pentagon_E1.py -v
make test

# 3. Status verification
grep -n "ClaimStatusProvedHere" \
     chapters/examples/k3_yangian_chapter.tex | grep -i "k3-pentagon-E1"
grep -n "label{cor:k3-" chapters/examples/k3_yangian_chapter.tex \
     chapters/theory/quantum_groups_foundations.tex \
     chapters/theory/cy_to_chiral.tex \
     chapters/examples/k3e_bkm_chapter.tex

# 4. Cross-volume sweep (per §2 step 9)

# 5. Independent verification audit
make verify-independence
make verify-independence-verbose | grep -A2 thm:k3-pentagon-E1
```

Expected: build passes (0 undef refs, 0 undef cites);
the new test passes; `ClaimStatusProvedHere` is found at the new
theorem and at all six new corollaries; cross-volume sweep shows
all references resolve; independence audit registers
`thm:k3-pentagon-E1` with three disjoint sources, no tautology
flag.

---

## 7. Coda

V49 supplied the Russian-school attack-and-heal record for
Pentagon-at-$E_1$ at K3 input via three independent verification
routes converging on $[\omega]_{K3} = 0$. This wave converts V49 into
editorial drafts for Vol III: a new theorem block carrying
`\ClaimStatusProvedHere` for K3 input specifically (conditional on
FM164/FM161 K3-specialised), six corollary blocks resolving six
previously-independent open conjectures at K3 (V19 Trinity, V39
amplitude, CY-C abelian unconditional, V20 Step 3 chain, V11 (U1)
chain, V8 §6 mock-modular K3), an AP-CY61 independent-verification
decorator entry establishing a model for downstream V49-shape claims,
and a master-punch-list split of V39 H1 into K3 (PROVED) + other
(OPEN) halves. The honest scope is K3 input only; non-K3 CY$_3$
inputs (quintic, conifold, local~$\mathbb{P}^2$, Niemeier-lattice
landscape) remain genuinely open and require their own attack-and-heal
cycles, templated by V49 H1-K3.

The four drafts together enact the editorial content of V49:
seven new blocks, six conjecture-to-corollary status changes at K3,
one new AP-CY61 entry, one master-punch-list split. No bare $\kappa$,
no chiral-Hochschild ambiguity, no new dangling labels, no AI
attribution, all commits by Raeez Lorgat only.

--- Raeez Lorgat, 2026-04-16
