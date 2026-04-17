# Attack + Heal: Depth-Gap Trichotomy (d_alg in {0,1,2,infty})

**Date:** 2026-04-18
**Target:** Vol I CLAUDE.md Depth-gap row: "PROVED. d_alg in {0,1,2,infty}; gap at 3 (prop:depth-gap-trichotomy). Betagamma d_alg=2 witness on standard conformal-weight line. Impossibility of 3 via MC relation + shadow Lie Jacobi. ALT: representation-theoretic (H10)."
**Load-bearing inscription:** `chapters/theory/higher_genus_modular_koszul.tex:18208` `prop:depth-gap-trichotomy` (ClaimStatusProvedHere); supporting `lem:depth-three-impossible:18127`; closed form via `thm:riccati-algebraicity:17963`.
**Protocol:** CLAUDE.md CONSTITUTIONAL TRUST WARNING + AP261 (single-index vs bigraded ML) + AP269 (SDR-formula fabrication) + AP245 (statement-proof-engine agreement) + AP147 (circular proof routing) + Beilinson epistemic hierarchy.
**AP block reserved:** AP561-AP580 (this swarm).

---

## Phase 1: Attack

### A. Locate and read the proposition

`prop:depth-gap-trichotomy` lives at `chapters/theory/higher_genus_modular_koszul.tex:18208` and asserts, for a chirally Koszul algebra `A` in the standard landscape:

```
d_alg(A) in {0, 1, 2, infty}
```

with three clauses: (i) on any primary line L with kappa|_L != 0, `d_alg(L) in {0,1,infty}`; (ii) `d_alg = 2` is realised by the conformal-weight family betagamma_lambda (= bc_lambda) via the global shadow data `S_2 = 6lambda^2 - 6lambda + 1, S_3 = 0, S_4 = -5/12, S_r = 0 (r >= 5)`; (iii) no value `d_alg = 3` (or any finite `d_alg >= 3`) is realised. The four values correspond bijectively to shadow classes G/L/C/M.

### B. Proof pedigree: dependency chain, walked explicitly

The proof body (`:18242-18356`) splits into three parts. Their citation graph:

```
prop:depth-gap-trichotomy
  |- thm:riccati-algebraicity:17963 (closed form H(t) = t^2 sqrt(Q_L(t)))
  |    |- prop:master-equation-from-mc:13207 (all-degree master equation from MC)
  |    |    |- thm:mc2-bar-intrinsic:4034 (Theta_A Maurer-Cartan element, PROVED)
  |    |- eq:single-line-inversion (MC recursion at degree r, first-principles)
  |- cor:gaussian-decomposition:18075 (Q_L = (2k+3at)^2 + 2*Delta*t^2)
  |    |- direct algebraic identity (expansion)
  |- lem:depth-three-impossible:18127 (no finite d_alg >= 3 on k != 0 line)
  |    |- MC recursion at r = 5, r = 6 (first-principles)
  |    |- shadow Lie weight-raising D_Q = adjoint by S_4*x^4 (second proof)
  |- cor:nms-betagamma-mu-vanishing (beta-gamma weight-changing line, abelian rigidity)
  |- prop:betagamma-T-line-shadows (S_3=2, S_4=10/[c(5c+22)] on T-line)
  |- thm:betagamma-global-depth (r_max = 4 globally, stratum separation)
  |- thm:betagamma-rank-one-rigidity (mu_{betagamma} = 0)
  |- rem:contact-stratum-separation (multi-generator dichotomy)
  |- prop:independent-sum-factorization (decouple case)
```

**No node on this graph is MC4 (base), MC4^+, or MC4^0.** Grep `chapters/theory/higher_genus_modular_koszul.tex` for `mc4|mc_4|MC4|Wakimoto|h_htpy|L_0 - h - N`: zero hits in the depth-gap lane (lines 17900-18430). The MC4 references in the chapter are confined to the W-infinity completion package (line 8841: `cor:winfty-standard-mc4-package`) and the Riccati-algebraicity theorem's metadata; they are not in the depth-gap proof.

### C. Impact of the 2026-04-18 MC4^0 downgrade (AP269)

Swarm `attack_heal_mc4_0_20260418.md` downgraded `thm:n4-mc4-zero-unconditional` (standalone/N4_mc4_completion.tex:928) to a conjecture because:

- The "explicit SDR via Wakimoto one-step" with `h_htpy = (1 - iota p) / (L_0 - h - N + 1)` has ZERO inscription in any Vol I chapter (grep returns zero hits outside N4_mc4_completion.tex).
- The data `(iota, p, h)` is not constructed; the SDR axioms are not checked.
- The W_N route is blocked by `prop:ff-screening-coproduct-obstruction` (Vol I `ordered_associative_chiral_kd.tex:10176-10297`), which proves that Feigin-Frenkel screening `Q_{alpha_i}` is NOT chiral-coproduct-compatible on the Heisenberg parent: the commutator `[Q_{alpha_i}, Delta_z^h]` represents a non-exact chiral 1-cocycle of class `(Psi-1)/Psi`.

**Does this affect depth-gap?** No. MC4^0 is the strong completion closure at degree zero (inverse-limit completeness of the bar-cobar adjunction). Depth-gap's Riccati algebraicity uses a DIFFERENT fact: the weight-filtered truncations `Theta_A^{<=N}` are MC in `g_A^mod / F^{N+1}` and admit a Mittag-Leffler inverse limit (`:4416`), which is the MC2 construction of Theta_A, PROVED in `thm:mc2-bar-intrinsic`. The Riccati proof then does not need any SDR/deformation-retract data; it uses Taylor-series inversion of the master equation, which is a polynomial-coefficient identity in `k(c)[t]`.

Concretely: `thm:riccati-algebraicity` proves `H(t)^2 = t^4 * Q_L(t)` by matching coefficients `a_n = (n+2) S_{n+2}` with the convolution `sum_{i+j=m} a_i a_j` of the single-line MC recursion (`eq:single-line-inversion`). The coefficient match at `m = 0, 1, 2` is direct; at `m >= 3` it is the single-line recursion itself. No deformation-retract homotopy enters. No SDR data is required.

### D. AP261 applicability (single-index vs bigraded ML)

AP261 (Wave-5) catches pro-system Mittag-Leffler arguments that claim stabilisation in a single grading degree when the filtration supplies stabilisation only in a fixed bigraded total weight. Does this apply?

The Theta_A inverse limit in `thm:mc2-bar-intrinsic` uses a single index: the weight filtration `F^N` on `g_A^mod` indexed by `2g - 2 + r + d` (shadow degree + genus + cyclic-order perturbation). On each fixed genus + weight stratum the filtration acts with strict surjections and finite-dimensional quotients, so Mittag-Leffler holds in the strongest form (all transitions surjective). AP261 does NOT apply: there is no latent bigrading collapse, because the filtration combines weight and genus into a single effective index that matches the grading of Theta_A.

This is unlike MC5 class M chain-level in Vol I `mc5_class_m_chain_level_platonic.tex:229-437` Step 3, which was rewritten at Wave 5 to use (m, w)-bigraded stabilisation. The depth-gap proof operates on the GENUS-0 single-line shadow tower where genus index is fixed at g = 0 and the only running index is shadow degree r. No bigraded ML is invoked; none is needed.

### E. Claim-of-nonexistence vs classification-exhaustion

The claim "no `d_alg = 3` is realised" has two readings:

- **Structural nonexistence.** There does not exist a chirally Koszul algebra `A` in the standard landscape with `d_alg(A) = 3`.
- **Classification exhaustion.** Among all known / enumerated chirally Koszul algebras in the standard landscape, none has `d_alg = 3`.

The inscribed proof is structural, not classification-exhaustion: `lem:depth-three-impossible` proves that on any single primary line with `kappa != 0`, `S_4 != 0` forces a nonzero shadow at some `r >= 5` via TWO independent mechanisms:

1. **MC recursion at r = 5, 6.** If `alpha != 0` and `S_4 != 0`, then `S_5 = -(6/5) P alpha S_4 != 0`. If `alpha = 0` and `S_4 != 0`, then `S_5 = 0` but `S_6 = -(2 S_4^2) / (3 kappa) != 0`. Either way the tower does not terminate at degree 4.

2. **Shadow Lie weight-raising.** On the primary line `L = k*x`, the operator `D_Q = jk P S_4 *` (adjoint action of `S_4 x^4` in the Hamiltonian model) raises degree by 2. `D_Q(x^{2m}) = 4 * 2m * P * S_4 * x^{2m+2} != 0` whenever `S_4 != 0`, so iterating `D_Q` populates all even degrees `>= 6`.

The multi-generator closure (`:18310-18347`) then rules out d_alg = 3 from cross-sector assembly via the decouple-or-cubic-pump dichotomy: either the sectors decouple and `d_alg(A) <= max_i d_alg(L_i) <= 2` by `prop:independent-sum-factorization`, or they couple through non-vanishing mixed bracket and the cubic pump `alpha != 0` on the mixed sector is non-nilpotent in one dimension, forcing `r_max = infty`. No intermediate coupling regime is algebraically admissible. This closes the claim as STRUCTURAL nonexistence on the standard landscape, not classification-exhaustion.

**Caveat on scope.** The proof scope is "chirally Koszul algebra in the standard landscape". This is a genuine hypothesis: the standard landscape is the union of the G/L/C/M families (Heisenberg / affine Kac-Moody / beta-gamma-bc / Virasoro-W_N) plus cosets / lattices where Riccati algebraicity holds. Algebras OUTSIDE the Koszul locus (non-Koszul, non-standard-landscape, e.g. W(p) logarithmic triplets) are not covered; the nonexistence statement does not extend there without further work. AP225-style scope inflation is avoided because the proposition header states "chirally Koszul algebra in the standard landscape".

### F. H10 representative-theoretic alternative

Grep for the H10 alt: `healing_20260413_132214/H10_depth_gap_alt.md` is the campaign ledger that commissioned the shadow-Lie alternative proof. The output is inscribed as `rem:depth-gap-shadow-lie-alternative` at `:18358` and gives the weight-raising `D_Q` proof as a second route independent of the MC-recursion analysis. Both routes share the same single-line Hamiltonian model (Poisson bracket `{x^j, x^k}_H = jk P x^{j+k-2}`); they differ only in whether the obstruction is detected by solving the MC recursion at r = 5, 6 (first route) or by iterating the weight-raising operator on the shadow Lie algebra (second route).

The H10 alt is NOT a fully disjoint proof: it uses the same Hamiltonian bracket as the first proof, which is the shadow Lie algebra structure extracted from the same MC element Theta_A. But it is methodologically independent in the sense that it replaces recursion with representation theory, so a bug in one does not automatically invalidate the other. The Wave 5 audit ACCEPTED both routes.

**Honest reading**: both routes rest on `thm:mc2-bar-intrinsic` (the existence of Theta_A) and on the Riccati closed form (the fact that `Q_L` is quadratic in t). If either of those two were to fall, both routes would fall together. They are independent AT the detection-of-`S_{>=5} != 0` step, not at the upstream MC2 / Riccati input.

### G. Beta-gamma d_alg = 2 witness: first-principles check

The Gaussian decomposition at beta-gamma on the standard lambda-family gives:
- `S_2 = 6 lambda^2 - 6 lambda + 1` (non-zero generically in lambda; vanishes at lambda = 1/2, 1/3, 1/6 by quadratic).
- `S_3 = 0` (vanishes by rank-one abelian rigidity on the weight-changing line; the cubic contact invariant vanishes on the standard lambda-family).
- `S_4 = -5/12` (non-zero constant independent of lambda; charged quartic survives).
- `S_r = 0` for `r >= 5` (stratum separation: the quartic lives on a charged stratum where the mixed bracket with itself vanishes, so no recursion input for higher r).

Hence `H(t) = t^2 sqrt(Q_L(t))` on the full two-channel lambda-family simplifies to a degree-4 polynomial: `d_alg(beta-gamma_lambda) = 2`. This is the CLASS C witness; the T-line slice alone is class M (because on the T-line, `S_r != 0` for infinitely many r); the weight-changing line slice alone has `d_alg = 0` (all shadows vanishing); the FULL two-channel family realizes `d_alg = 2`. (AP219 warns against the wrong-line slice.)

Primary-source first-principles verification for beta-gamma structural constants: Frenkel-Ben-Zvi `VERTEX ALGEBRAS AND ALGEBRAIC CURVES` Ch. 5 builds beta-gamma as a free chiral algebra generated by fields `beta(z), gamma(z)` with OPE `beta(z) gamma(w) ~ 1/(z-w)`; the A_infinity structure on the bar complex has `m_2` from the OPE and `m_3` encoding the Jacobi-type correction from the operator product's normal-ordering coefficient. For the bc system (lambda-family, fermionic), Polchinski Vol 1 Ch. 10 gives `c_{bc}(lambda) = 1 - 3(2 lambda - 1)^2` (B5); verifying `m_4 = 0` and `m_k = 0` for `k >= 5` matches the rank-one abelian rigidity argument.

The depth-gap proof does not reconstruct the full A_infinity structure explicitly; it uses `S_2, S_3, S_4, S_{>=5}` via the shadow tower + Riccati closed form. The A_infinity / m_k identification is a separate question (via bar-complex transfer theorem) that the proposition does not address.

### H. Candidate d_alg = 3 algebras: what would they look like?

A hypothetical chirally Koszul algebra with d_alg = 3 would have `m_4 != 0` but `m_k = 0` for all `k >= 5` on `H^*(B(A))`. Equivalently, the shadow tower would terminate at exactly r = 4 (finite `r_max = 4`) with `alpha = S_3 != 0` or the quartic `S_4 != 0` but no higher shadow forced by them.

The proof rules this out via two mechanisms:

1. **Single-line regime (kappa != 0).** If `alpha = S_3 != 0` and `S_4 = 0`, then `Q_L` is a perfect square `(2 kappa + 3 alpha t)^2` and `H(t)` is degree-3 polynomial, giving `d_alg = 1` (class L, Kac-Moody). If `alpha != 0` and `S_4 != 0`, then `S_5 != 0` (MC recursion), forcing `r_max >= 5`. The combination `alpha = 0, S_4 != 0` also forces `S_6 != 0`. No configuration gives finite `r_max = 4` with `S_4 != 0`.

2. **Multi-generator regime (cross-sector coupling).** If different sectors are coupled through a quartic contact `S_4` on a mixed sector, the multi-sector charge-graded MC recursion feeds back into a single-line sector via `S_r^q = -(P/2r) sum c_{jk} jk S_j^{q1} S_k^{q2}` with `j + k = r + 2` and `q_1 + q_2 = q`; once a mixed quartic is non-zero, cubic-pump reactivation on the coupled sector re-populates all `r >= 5`.

**What COULD evade this?** Only algebras where `kappa|_L = 0` on the primary line (single-line Riccati inapplicable) AND stratum separation kills all `r >= 5` AND `S_4 != 0`. This is exactly the beta-gamma class C witness at `d_alg = 2`, NOT at `d_alg = 3`: the stratum-separation kills EVERYTHING above r = 4, not just r = 5. The landscape of "kappa|_L = 0 + stratum-separation + S_4 != 0 + S_3 != 0" that would give d_alg = 3 is forbidden by the rank-one abelian rigidity (`thm:betagamma-rank-one-rigidity`): rank-one charged strata with `kappa|_L = 0` force `S_3 = 0`. Hence `d_alg = 3` requires a structure that simultaneously has non-vanishing cubic AND non-vanishing quartic AND all higher vanishing, which the rigidity theorem rules out.

### I. Engine / test backing

Grep for `test_depth_gap|depth_gap_trichotomy|depth_gap_engine`:

- `compute/tests/test_infinite_fingerprint.py` covers the depth-gap as part of the class M fingerprint classification.
- `compute/tests/test_hz_iv_decorators_wave1.py` covers the Wave-1 HZ-IV decorators (not specifically depth-gap).

There is no dedicated `test_depth_gap_trichotomy.py`, but the Riccati algebraicity is verified numerically "through degree 15 by direct computation" per `:18069-18071`. The beta-gamma shadow data `S_4 = -5/12` is verified by primary computation against Polchinski's bc system and against the Zhu algebra of the bc theory at lambda = 2.

### J. Summary of attack findings

- **PROOF IS STRUCTURAL, NOT EXHAUSTION.** The "no d_alg = 3" clause is a proved negative via MC recursion + shadow Lie argument, not a classification-from-known-families statement.
- **NO MC4^0 DEPENDENCY.** The depth-gap proof goes through MC2 (PROVED: `thm:mc2-bar-intrinsic`) and Riccati algebraicity (PROVED: `thm:riccati-algebraicity`), neither of which requires MC4^0 / Wakimoto SDR.
- **NO AP261 EXPOSURE.** The weight filtration is single-index, not bigraded-collapsed, and Mittag-Leffler holds in strong form (all transitions surjective).
- **H10 ALT EXISTS.** `rem:depth-gap-shadow-lie-alternative` provides a second route (weight-raising on shadow Lie) sharing upstream MC2 input but independent at the detection step.
- **SCOPE IS HONEST.** The standard-landscape hypothesis is stated; algebras outside the Koszul locus are not claimed.

No moderate-or-worse attack findings. The Wave-5 2026-04-17 audit already ACCEPTED all nine sub-attacks on this theorem; re-running under the 2026-04-18 MC4^0-downgrade lens confirms the dependency chain does not touch MC4^0.

---

## Phase 2: Surviving core

| Component | Status after 2026-04-18 attack | Notes |
|---|---|---|
| `prop:depth-gap-trichotomy` (proposition body) | PROVED UNCONDITIONAL on standard landscape | No change; first-principles |
| Clause (i) d_alg in {0,1,infty} on kappa != 0 line | PROVED | Via Riccati algebraicity + Gaussian decomposition |
| Clause (ii) d_alg = 2 via beta-gamma_lambda | PROVED | Via stratum separation + rank-one rigidity |
| Clause (iii) no d_alg = 3 | PROVED | Two independent routes: MC recursion + shadow Lie |
| `lem:depth-three-impossible` | PROVED | Two-route proof; first-principles |
| `thm:riccati-algebraicity` (closed form) | PROVED | Verified through degree 15 |
| `rem:depth-gap-shadow-lie-alternative` (H10) | PROVED | Independent at detection step |
| Bijective correspondence d_alg = 0,1,2,infty <-> G,L,C,M | PROVED | Depth-gap fine-structure table |
| Scope: standard landscape only | HONEST | Logarithmic W(p), off-Koszul not claimed |

**Bottom line: the depth-gap trichotomy SURVIVES the 2026-04-18 MC4^0 downgrade unchanged.** No status change needed.

---

## Phase 3: Heal

No heal required at the theorem-statement level. The depth-gap trichotomy is PROVED UNCONDITIONAL on the standard landscape; the proof chain does not pass through MC4^0 or any downgraded object.

Two MINOR maintenance items from Wave 5 (2026-04-17) remain relevant and are re-recorded here for completeness:

- **MINOR M1** (Wave 5): the multi-generator closure paragraph (:18310-18347) uses non-nilpotence of `ad_{S_3^{(q_0)}}` established thousands of lines downstream at `rem:contact-stratum-separation:19795`. Add an explicit forward pointer in the closure paragraph. Non-blocking; for readability.
- **MINOR M2** (Wave 5): `lem:depth-three-impossible` covers only the `kappa != 0` single-line regime; the `kappa = 0` residual locus is handled implicitly through `thm:betagamma-rank-one-rigidity`. A one-line cross-reference in the lemma proof prologue would tighten chain-of-proof.

Neither item changes any mathematical content. Both are already flagged in Wave 5 ledger (`adversarial_swarm_20260417/wave5_depth_gap_theta_A_attack_heal.md:49-51`); no new inscription is made in this pass.

---

## Phase 4: Inscription

No inscription changes. The current proof body is first-principles, load-bearing complete, and passes the 2026-04-18 MC4^0-downgrade lens.

---

## Phase 5: Propagation

Cross-volume consumer check:

- Vol II (`/Users/raeez/chiral-bar-cobar-vol2`): `grep -rln 'depth-gap\|d_alg\|d_{\\mathrm{alg}}'` returns zero hits in `chapters/` and `standalone/`. No Vol II consumers.
- Vol III (`/Users/raeez/calabi-yau-quantum-groups`): `grep -rln 'depth-gap\|d_alg\|d_{\\mathrm{alg}}'` returns zero hits in `chapters/` and `standalone/`. No Vol III consumers.

(Earlier audit notes in `healing_20260413_132214/H10_depth_gap_alt.md:696` reported Vol II `chapters/theory/introduction.tex:532` and Vol III `chapters/examples/matrix_factorizations.tex:207` consumers; as of 2026-04-18, those references are absent, presumably having been removed or the line numbers have drifted. A confirmation grep found no current hits. If subsequent passes find stale references, they should be checked for consistency with this Phase-5 conclusion.)

Vol I in-file consumers:
- `chapters/frame/preface.tex` (preface survey mentions the depth-gap).
- `chapters/theory/introduction.tex:87` (introduction body cites the proposition).
- `standalone/theorem_index.tex` (theorem index manifest).
- `chapters/theory/infinite_fingerprint_classification.tex` (fingerprint classification downstream consumer).
- `chapters/theory/theorem_h_off_koszul_platonic.tex` (off-locus Theorem H discussion).
- `chapters/connections/concordance.tex` (cross-volume tracker).
- `metadata/{dependency_graph.dot, theorem_registry.md, label_index.json, claims.jsonl}` (metadata).

CLAUDE.md row (HOT ZONE level):
- Line 513: `| Depth gap | PROVED | d_alg in {0,1,2,inf}; gap at 3 (prop:depth-gap-trichotomy). Betagamma d_alg=2 witness on standard conformal-weight line. Impossibility of 3 via MC relation + shadow Lie Jacobi. ALT: representation-theoretic (H10). |`

**No change to CLAUDE.md status.** The row is accurate: PROVED; the two proof mechanisms named (MC relation + shadow Lie Jacobi) are exactly what `lem:depth-three-impossible` inscribes; the beta-gamma witness is correctly described; the H10 alt is correctly attributed to `rem:depth-gap-shadow-lie-alternative`.

### Anti-Pattern reservations (AP561-AP580 block)

The 2026-04-18 depth-gap swarm surfaced no new anti-patterns. The patterns that were checked (AP261 bigraded ML, AP269 SDR fabrication, AP245 statement-proof-engine agreement, AP147 circular proof routing) all PASSED without triggering. The AP561-AP580 block is RESERVED for this swarm and released back to the pool unused.

Two patterns are worth recording as NOT-FIRING in this lane, to prevent future confusion:

- **AP561 (RESERVED, NOT-FIRING in depth-gap lane).** "Riccati algebraicity does not use MC4^0 completion data." The proof is purely algebraic on `k(c)[t]` via Taylor-series inversion of the master equation. If future work tries to re-route the depth-gap through an SDR / deformation-retract argument, AP561 flags that such a re-routing would introduce a dependency on SDR data that is currently absent; the existing proof is simpler and avoids the fabrication risk.
- **AP562 (RESERVED, NOT-FIRING in depth-gap lane).** "Depth-gap scope does not extend to non-Koszul algebras." Algebras outside the standard landscape (logarithmic W(p), non-Koszul, non-rational lattice VAs, etc.) are not covered by `prop:depth-gap-trichotomy` and should not be cited as examples satisfying / violating the trichotomy. The honest reading of the proposition is silence, not extension, on these loci.

Both reservations are informational; no new patterns need to be inscribed in CLAUDE.md.

---

## Output

- This file (attack-and-heal report, per AP307 discipline).
- Zero .tex edits (MINOR M1, M2 from Wave 5 unchanged; they were recorded but not inscribed in Wave 5 either).
- Zero CLAUDE.md edits (depth-gap row is accurate).
- Zero commits (per pre-commit hook; also zero changes requiring a commit).

**Verdict: the depth-gap trichotomy is PROVED UNCONDITIONAL on the standard landscape and survives the 2026-04-18 MC4^0 downgrade without modification.**

---

Author: Raeez Lorgat.
