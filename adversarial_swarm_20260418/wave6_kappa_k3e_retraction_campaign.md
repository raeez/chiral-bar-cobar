# Wave-6 Retraction Campaign: κ_ch(K3×E) additive drift

Date: 2026-04-18. Session: targeted-heal. Status: **SCOPE-CORRECTED, NOT APPLIED**.

## Executive summary

Mission requested retraction of "κ_ch(K3×E) = 3" additivity theorem at Vol III
`chapters/examples/k3_chiral_algebra.tex:506` + 20+ consumer-site propagation,
on the ground that the Hodge supertrace is Künneth-multiplicative (AP289) and
κ_ch(E) = 0 (not 1). First-principles investigation (AP186) reveals the
situation is **notational, not mathematical**: two distinct invariants share
the symbol κ_ch, both inscribed as canonical within the programme. The mission
brief's asserted "correct value κ_ch(K3×E) = 0" is ONE of two canonical
routes; the other inscribes κ_ch(K3×E) = 3. A naive 20-site rewrite would
corrupt load-bearing structure. Scope-corrected heal path documented below;
no edits applied this session.

## Diagnostic (first-principles)

**Route A — Hodge supertrace (canonical per Wave-4 Vol III).**
`chapters/examples/cy_d_kappa_stratification.tex:400-475`
(`thm:kappa-stratification-by-d`, `ClaimStatusProvedHere`). For a compact
CY_d, κ_ch(A_X) := Ξ(X) = Σ_q (-1)^q h^{0,q}(X), Hodge supertrace of
H^{0,•}(X). Künneth-multiplicative: Ξ(X × Y) = Ξ(X) · Ξ(Y).
- Ξ(E) = 1 - 1 = 0, so κ_ch(Φ_1(D^b(E))) = 0.
- Ξ(K3) = 1 - 0 + 1 = 2.
- Ξ(K3 × E) = 2 · 0 = 0 (Künneth; inscribed at :448-452).

**Route B — Heisenberg rank / free-boson level (Vol I convention).**
Vol I κ^{Heis}_k = k; `k3_chiral_algebra.tex:491,503-506`. The elliptic curve
E carries the lattice VOA H_1 (rank-1 free boson, level 1), so
κ_ch(H_1) = k = 1. Rank is additive under free-boson product,
so κ_ch(K3 × E) = dim_C(K3) + dim_C(E) = 2 + 1 = 3.

**Programme's own resolution.** `cy_d_kappa_stratification.tex:414-426`
identifies the collision and elects Route A as canonical:
"the apparent discrepancy with the claim `κ_ch(E) = 1` in legacy tables
arises from conflating κ_ch(A_E) [supertrace] with the Heisenberg level
parameter k that parametrizes the family of Heisenberg algebras … H_1
arises by a distinct construction (the free-boson lattice of rank 1) that
sits outside the Φ_d functor. … We inscribe κ_ch(Φ_1(D^b(E))) = 0 as the
canonical d = 1 value."

**Therefore.** The mission brief's AP289 framing ("κ_ch(E) = 0 via Künneth;
κ_ch(K3×E) = 3 is additive drift") is correct under Route A, WRONG under
Route B. The programme has not propagated Route A's canonical-election to
the 20+ Route B sites.

## Mission framing vs. reality

| Mission assertion | Reality |
|---|---|
| κ_ch(E) = 0 is correct; κ_ch(E) = 1 is drift | Both are correct for distinct invariants; Route A is canonical per Wave-4 |
| κ_ch(K3×E) = 3 is AP289 additivity violation | It is correct additivity of rank under free-boson product (Route B); Route A gives 0 |
| 20+ site "targeted heal" | Chapter restructure: 300+ test assertions, 22-route cross-verification engine, observational BKM decomposition 5 = 3 + 2, all inherit Route B |
| AP289 Künneth-multiplicative fix | Real AP is AP234-class: two invariants same symbol |

## Site inventory (NOT edited)

Route B additivity sites (κ_ch(K3×E) = 3 or κ_ch(E) = 1):

1. `chapters/examples/k3_chiral_algebra.tex:447, 452, 491, 503, 504, 506, 519, 541, 744`
2. `chapters/examples/k3e_bkm_chapter.tex:9, 540, 980, 1137, 1139, 1140, 1242, 1250, 1352`
3. `chapters/examples/k3e_cy3_programme.tex:334, 983, 1827, 2602, 2990, 3006, 3052`
4. `chapters/examples/quantum_group_reps.tex:498-576, 550, 1115, 1124`
5. `chapters/frame/preface.tex:432, 490, 1046, 1050`
6. `chapters/theory/introduction.tex:321, 708, 1190`
7. `chapters/theory/cy_to_chiral.tex:170, 280`
8. `chapters/theory/modular_trace.tex:65, 80, 87`
9. `chapters/theory/e1_chiral_algebras.tex:162`
10. `chapters/connections/modular_koszul_bridge.tex:79, 103, 341`
11. `appendices/conventions.tex:107`
12. `main.tex:445, 446`
13. `working_notes.tex` (7+ sites)
14. Engine tests: `kappa_spectrum_reconciliation.py` (44 tests),
    `kappa_bkm_adversarial.py` (63 tests), `kappa_consistency_adversarial.py`
    (64 tests, 22-route cross-verification all expecting κ_ch = 3)

Route A canonical anchors (κ_ch(K3×E) = 0, κ_ch(E) = 0):

- `chapters/examples/cy_d_kappa_stratification.tex:400-475,452`
- `chapters/examples/cy_d_kappa_stratification.tex:414-426` (collision resolution)
- `standalone/k3e_cy3_programme_vol3.tex:57`
- `chapters/examples/cy_c_six_routes_generator_level_platonic.tex:65`

Load-bearing structure that breaks under naive Route A propagation:

- Observational BKM decomposition κ_BKM(K3×E) = κ_ch(K3×E) + χ(O_K3) = 3 + 2 = 5
  (`k3_chiral_algebra.tex:512, 525`). Under Route A: 0 + 2 = 2 ≠ 5.
  The "K3 fiber announces its presence" mechanism dissolves.
- Remark `rem:kappa-ch-vs-kappa-bkm-mechanism` (:522) explaining the DMVV
  second-quantization lift from κ_ch = 3 to κ_BKM = 5.
- `rem:chi-top-24-failure` (:534) comparing χ_top/24 to κ_ch at E, K3, K3×E
  with specific numerics (0≠1, 1≠2, 0≠3).
- 22-route cross-verification `kappa_consistency_adversarial.py` — 7 routes
  (additive, dim_C, bar Euler, Yangian, sigma model, chiral de Rham,
  genus-1 free energy) all independently produce κ_ch = 3. If Route A is
  canonical, every test retracts.

## Why no edits applied

1. **AP186 (shallow correction without first-principles).** Mission brief
   asserts one-sided rewrite. First-principles reading shows two canonical
   invariants. A 20-site retraction would silently erase Route B and leave
   300+ tests expecting the erased value.

2. **AP149 (resolution propagation).** The canonical-election at
   `cy_d_kappa_stratification.tex:414-426` was never propagated. The correct
   heal is to propagate that election atomically: retag every Route B usage
   as "κ^{rk}_ch (Heisenberg level; distinct from supertrace
   κ_ch(Φ_d(D^b(X))))" OR wrap each Route B proposition with a Remark
   pointing at `thm:kappa-stratification-by-d`. This is a chapter-restructure,
   not a 20-site patch.

3. **AP275 (CLAUDE.md narrative inverting discipline).** Mission brief's
   statement "κ_ch(E) = 0 (elliptic curve: h^{0,0} - h^{0,1} = 1 - 1 = 0)"
   is correct for Ξ(E) but inverts the Heisenberg convention κ^{Heis}_k = k
   inscribed in Vol I and re-used in the 20+ Route B sites. Applying the
   brief literally would introduce a second inconsistency.

4. **AP280 (three-step epistemic inflation risk).** Converting the
   observational BKM decomposition 5 = 3 + 2 (Route B coincidence at
   unorbifolded N = 1 only, per `rem:bkm-decomposition-adversarial`) into
   a Route A statement 5 = 0 + ? has no numerical anchor; forcing the
   rewrite would manufacture a new coincidence.

## Recommended heal (not applied)

**Option (c) — inscribe two-invariant clarification Remark, one site.**
Add at head of `k3_chiral_algebra.tex` κ-spectrum proposition (before :485):

```
\begin{remark}[Two κ_ch invariants]
\label{rem:kappa-ch-two-routes-k3e}
The symbol κ_ch carries two distinct canonical meanings in this programme:
Route A (functorial) κ_ch(Φ_d(D^b(X))) := Ξ(X) (Hodge supertrace,
Theorem~\ref{thm:kappa-stratification-by-d}, Künneth-multiplicative) gives
κ_ch(E) = 0 and κ_ch(K3 × E) = 0; Route B (Heisenberg rank) κ_ch(A) := k
for free-boson level k (Vol~I convention κ^{Heis}_k = k) gives κ_ch(E) = 1
and κ_ch(K3 × E) = 3 by rank-additivity. The table below and items
(ii)-(iii)-(vi) adopt Route B; item (iv) is Route-A-multiplicative for
κ_cat. The canonical functorial invariant is Route A; Route B is recorded
here for compatibility with the Vol~I free-boson-lattice convention and
for the observational BKM decomposition 5 = 3 + 2 of item (vi), which is
a Route-B coincidence specific to the unorbifolded N = 1 case per
Remark~\ref{rem:bkm-decomposition-adversarial}.
\end{remark}
```

This is ONE edit, preserves all 300+ tests, preserves load-bearing BKM
decomposition, and resolves the notational collision explicitly. Propagate
analogous one-line cross-references at the 20+ drift sites in a later wave
if programme-wide Route-A canonicalisation is elected.

**Option (d) — downgrade mission to attack-heal note, close without edits.**
The scope-correction itself IS the heal: the programme carries a
notational collision, the Wave-4 election at
`cy_d_kappa_stratification.tex:414-426` is load-bearing, and the 20+ Route B
sites are not "drift" but inherited legacy convention. The correct
programme-level action is to surface this via FRONTIER.md as "κ_ch notation
audit" and defer the chapter-restructure.

## Grep gates (not executed programme-wide)

Mission-specified gate:
```
grep -rn 'kappa_{\\mathrm{ch}}(K3.*\\times.*E).*=.*3' ~/calabi-yau-quantum-groups
```
Running this pre-heal and demanding zero hits would erase Route B. The
correct gate after Option (c) heal is:
```
grep -rn 'kappa.*K3.*E.*=.*3' without nearby \ref{rem:kappa-ch-two-routes-k3e}
```

## Residual / open

- κ_ch notation audit programme-wide: which convention is load-bearing
  where. Requires per-chapter audit.
- Test-engine convention tagging: `kappa_consistency_adversarial.py`'s 22
  routes presume Route B; if Route A is canonicalised, engine retags
  required.
- Observational BKM decomposition 5 = 3 + 2: dissolves under Route A.
  If Route A canonicalises, Remark `rem:kappa-ch-vs-kappa-bkm-mechanism`
  rewrites.

## Classification

- **AP234-class**: two invariants, one symbol, inscribed canonical elsewhere
  without propagation.
- **AP149-class**: canonical-election at `cy_d_kappa_stratification.tex:414`
  not propagated to 20+ sites.
- **NOT AP289** as originally framed: Route B is additive by construction
  (rank of free-boson), not a Künneth violation.

## Commit plan

None this session. No edits applied. Note file is the deliverable.
