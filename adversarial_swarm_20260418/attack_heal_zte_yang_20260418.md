# Attack-and-Heal: ZTE failure at O(κ²) + S^{corr} existence claim
Date: 2026-04-18
Author: Raeez Lorgat

## Scope

Adversarial audit of the Vol I CLAUDE.md cross-awareness capsule line 1302:
"ZTE fails for Yang R-matrix at O(κ²); E_3 nontrivial beyond E_2; S^{corr} EXISTS."

Mission prompt: AP1081-AP1100 reserved. Used sparingly per AP314 + Miura-swarm precedent.

## Findings

### F1. ZTE failure at O(κ²) — INSCRIPTION VERIFIED

Primary locus: `thm:zte-failure` at
`calabi-yau-quantum-groups/chapters/theory/en_factorization.tex:534-557`
(`\ClaimStatusProvedHere`).

Content: Yang R-matrix $R(z)=(z\cdot\mathrm{Id}+\hbar_Y P)/(z+\hbar_Y)$
with $\hbar_Y = h_1 h_2 h_3$.
- (i) YBE satisfied (positive control).
- (ii) ZTE on $(\C^2)^{\otimes 4}$ NOT satisfied; obstruction scales as
  $O(\hbar_Y^2)$ and is antisymmetric. Proof: explicit matrix multiplication
  on charge-2 sector (dim 6), verified at multiple spectral parameter values
  plus symbolic expansion in $\hbar_Y$.
- (iii) Permutation limit $\hbar_Y=0$: ZTE trivially satisfied (Kapranov-Voevodsky).

Engine: `compute/lib/zamolodchikov_tetrahedron_engine.py` (34 tests).

Structural invariants (`rem:zte-obstruction-structure`, :564-574):
- rank 4/6 on charge-2;
- antisymmetric $\cO^T = -\cO$;
- eigenvalues of $\cO/\hbar_Y^2$: $\{0, 0, \pm i\sqrt{3/21}, \pm i\sqrt{19/21}\}$;
- $S_4$ decomposition: trivial $\oplus$ standard $\oplus$ 2-dim.

Cross-volume consumer (Vol I): CLAUDE.md:1302 capsule matches the proved content.
No AP271 drift in Vol I direction.

### F2. Direct O(κ²) deficit verification — EVIDENCE ADEQUATE

The proof body at :556 is explicit: "computed by explicit matrix multiplication
on the charge-2 sector of $(\C^2)^{\otimes 4}$ (dimension 6): the difference
$\mathrm{LHS} - \mathrm{RHS}$ is nonzero at $O(\hbar_Y^2)$, verified at multiple
spectral parameter values and confirmed by symbolic expansion in $\hbar_Y$."

Reproducible via `zamolodchikov_tetrahedron_engine.py`. Scale of failure:
order-unity after dividing by $\hbar_Y^2$ (eigenvalues of normalized obstruction
are $\{0, 0, \pm i\sqrt{3/21}, \pm i\sqrt{19/21}\}$, moduli around $0.4$ and $0.95$).
This is nontrivially above machine precision; the failure is genuine mathematics,
not numerical noise. AP315 (engine tolerance looser than physical scale) does
not fire: the effect is a rank-4/6 obstruction with prime-discriminant eigenvalues,
orders of magnitude above any plausible tolerance threshold.

### F3. S^{corr} existence — CONSTRUCTED, NOT EXISTENCE-ONLY

The claim is load-bearing at four proposition-levels, all `ClaimStatusProvedHere`:

1. **`prop:zte-deformation-cohomology`** (en_factorization.tex:576-630, 47 tests,
   `zte_deformation_cohomology.py` 1514 lines).
   Deformation complex $C^0 \to C^1 \to C^2$ with $(\dim C^0, \dim C^1, \dim C^2)
   = (2, 6, 20)$, cohomology $(\dim H^0, \dim H^1, \dim H^2) = (2, 1, 15)$.
   Pairwise-restricted $H^2_{\mathrm{pw}}$ dim 6 NONZERO (pairwise deformations
   insufficient); extended $H^2_{\mathrm{ext}}$ TRIVIAL via rank 35/36 on
   $36 \times 116$ extended system. Existence of $T_{ijk}$ guaranteed.

2. **`prop:zte-explicit-correction`** (en_factorization.tex:637-668, 51 tests,
   `zte_correction_explicit_final.py` 844 lines).
   EXPLICIT construction by adaptive Newton iteration. $S^{\mathrm{corr}}$
   verified satisfying ZTE to relative residual $< 10^{-5}$ at 4 spectral
   parameter configurations $\times$ 5 values $\hbar_Y \in [0.05, 0.5]$.
   Structural properties: $T$ symmetric, persymmetric, zero anti-diagonal,
   rank 6/6, mixed-sign eigenvalues; 45-dim gauge orbit (44 face-redistribution
   + 1 scalar).

3. **`prop:zte-o-kappa4`** (en_factorization.tex:684-713, 37 tests,
   `zte_o_kappa4.py` 814 lines).
   Exact rational arithmetic (Python `Fraction` + sympy rref).
   In the rref gauge (sparse, 18/80 params), the charge-2 sector is resolved
   EXACTLY as a rational identity — not just to machine precision. The
   minimum-norm gauge leaves $O(\hbar_Y^4)$ residual on charge-2; the second
   Newton step drives to $O(\hbar_Y^6)$; third to $< 10^{-8}$.

4. **`prop:zte-nonperturbative-completion`** (en_factorization.tex:722-753,
   58 tests, `zte_nonperturbative_completion.py` 1367 lines).
   (a) No per-face Drinfeld twist exists: adjoint $\mathrm{ad}(S^{\mathrm{fact}})$
   has rank 24/36, $C_{ijk}$ NOT in image. Non-inner deformation.
   (b) Ternary Frobenius norm strictly positive in exact arithmetic — confirming
   genuine 3-body content.
   (c) Charge-sector resolution in rref gauge: charges $\{0, 2, 4\}$ exactly,
   charges $\{1, 3\}$ rank-2 residual with identical max entry (charge-conjugation
   symmetry).
   (d) Padé poles purely imaginary in $\hbar_Y^2$: real-analytic on real axis.

Total engine support: five libraries, 5336 lines; ~230 tests.

**Construction mechanism, step by step.**
(α) Cohomological vanishing of obstruction class $[\ell_3(r,r,r)]$ via
    rank count on gauge-extended deformation complex
    (`prop:zte-deformation-cohomology`(v), rank 35/36).
(β) Explicit entry-by-entry rational Newton step using sympy rref;
    charge-2 exact rational resolution in one step in the rref gauge
    (`prop:zte-o-kappa4`(iv)).
(γ) Structural invariants (symmetry / persymmetry / zero antidiagonal / full
    rank) verified entry-by-entry in exact `Fraction` arithmetic.
(δ) All-order Newton iteration: monotone residual drop $10^8$ in 3 steps
    (`rem:zte-newton-convergence`).

This is a CONSTRUCTION, not an existence-only claim.

### F4. Cross-reference — E_3 nontrivial beyond E_2 + Miura/FF relation

`rem:zte-genuinely-e3` (en_factorization.tex:755-768) identifies the ZTE
obstruction as "the $d_4$ differential on the spectral sequence" — this is
the $E_2 \to E_3$ homotopy-coherence obstruction at chain level, exactly
what the Vol I capsule phrase "E_3 nontrivial beyond E_2" asserts.

**Relation to Miura $(\Psi-1)/\Psi$ / FF-screening obstruction
(iteration 6 heal, AP421 + `prop:ff-screening-coproduct-obstruction`
at ordered_associative_chiral_kd.tex:10176-10297)**:

| Aspect                  | FF-screening cocycle            | ZTE $\ell_3$-obstruction         |
|-------------------------|---------------------------------|----------------------------------|
| Cohomological dimension | $H^1_{\mathrm{ch}}$             | $H^2_{\mathrm{ext}}$             |
| Coefficient             | $(\Psi-1)/\Psi$                 | eigenvalues $\pm i\sqrt{3/21}, \pm i\sqrt{19/21}$ |
| Codomain algebra        | $V_{\mathrm{Heis}} \otimes V_{\mathrm{Heis}}[z,z^{-1}]$ | $\End(V^{\otimes 4})$ restricted to charge-2 |
| Descent direction       | $E_1$-chiral $\to$ $E_2$-chiral coproduct | $E_2$-chiral $\to$ $E_3$-chiral tetrahedron |
| Object obstructed       | chiral coproduct                | Zamolodchikov tetrahedron composition |
| AP266 status in prog.   | sharpened                       | sharpened                        |

Structurally orthogonal: different dimension, different codomain, different
descent direction. They are cousins in the AP266 sharpened-obstruction family
(both explicit non-exact cocycles with identified coefficients), NOT the
same object. No direct identification inscribed; none warranted without
a structural bridge theorem.

## Verdict

**CLAUDE.md Vol I:1302 capsule is accurate.** All three assertions hold:
- "ZTE fails for Yang R-matrix at O(κ²)" → verified by `thm:zte-failure`.
- "E_3 nontrivial beyond E_2" → verified by non-inner deformation
  (`prop:zte-nonperturbative-completion`(i)) + ternary necessity (ii) +
  $d_4$ differential identification (`rem:zte-genuinely-e3`).
- "S^{corr} EXISTS" → exceeded. S^{corr} is CONSTRUCTED, not merely
  existential. Four propositions plus 5336-line engine support.

## Discrepancy surfaced (minor, existing-AP instance, NOT a new AP)

Vol III `chapters/theory/quantum_chiral_algebras.tex:549` prose line is
stale:

    "Status: ZTE failure proved; the correction term is conjectural."

This contradicts:
- Vol III CLAUDE.md:145 row "ZTE T matrix COMPUTED | PROVED | Exact rational
  T matrix solving S^{corr} = S^{fact} + kappa^2*T. 35 tests."
- Vol III CLAUDE.md:125 row "Explicit ZTE correction T | CONSTRUCTIVE |
  S^{corr} = S^{fact} + kappa^2*T. T exists (rank 35/36 in extended complex)."
- Vol III CLAUDE.md:732 "ZTE correction: S^{corr}=S+κ²T NOW COMPUTED (exact
  rational T matrix, 35 tests)."
- `prop:zte-explicit-correction` + `prop:zte-o-kappa4` (ClaimStatusProvedHere).

This is a plain **AP271 (reverse drift: CLAUDE.md ahead of manuscript
retractions)** and **AP300 (in-file ProvedHere-vs-retracted-mechanism drift
via non-cross-referenced remark)** instance. No new AP warranted.

### Heal target (single line in Vol III, NOT INSCRIBED THIS SESSION)

File: `calabi-yau-quantum-groups/chapters/theory/quantum_chiral_algebras.tex`
Line: 549

Before:
    \emph{Status}: ZTE failure proved; the correction term is conjectural.

After:
    \emph{Status}: ZTE failure proved (Theorem~\ref{thm:zte-failure}); $S^{\mathrm{corr}}$ constructed explicitly as rank-$35/36$ extended resolution with exact rational charge-$2$ resolution in the rref gauge (Propositions~\ref{prop:zte-explicit-correction}, \ref{prop:zte-o-kappa4}).  All-order completion via cocycle-corrected Drinfeld twist remains conjectural (Conjecture~\ref{conj:zte-drinfeld-twist-completion}).

Rationale for NOT inscribing this session:
- Build + test verification required per PreToolUse hook; outside this
  session's scope.
- AP316 (worktree-isolated Agent heal abandoned at delivery) discipline:
  commits require build + test pass.
- The heal is a 1-line prose update; no structural mathematical risk.
- Follow-through: inscribe in a next-wave session with build + test verified.

## AP inscription decision

**Zero new APs inscribed.** Per AP314 (inscription-rate outpaces audit
capacity) + Miura-swarm precedent (0 APs when no failure surfaces):

- The S^{corr} construction is sound. Construction mechanism is explicit.
- The Miura/FF cross-reference is honestly structurally orthogonal;
  no cross-identification forced; no AP required for recording non-identity.
- The stale `quantum_chiral_algebras.tex:549` prose line is an existing-AP
  instance (AP271 + AP300), not a new pattern. Fixing it is single-line
  prose discipline already catalogued.

AP1081-AP1100 block: released unused.

## References

- `calabi-yau-quantum-groups/chapters/theory/en_factorization.tex:534-800`
  (thm:zte-failure, prop:zte-deformation-cohomology, prop:zte-explicit-correction,
  prop:zte-o-kappa4, prop:zte-nonperturbative-completion,
  conj:zte-drinfeld-twist-completion).
- `calabi-yau-quantum-groups/chapters/theory/quantum_chiral_algebras.tex:547-556`
  (stale line 549; `rem:zte-6d-fingerprint` structural summary).
- Engines: `zamolodchikov_tetrahedron_engine.py` (34 tests);
  `zte_deformation_cohomology.py` (1514 lines, 47 tests);
  `zte_correction_explicit_final.py` (844 lines, 51 tests);
  `zte_o_kappa4.py` (814 lines, 37 tests);
  `zte_nonperturbative_completion.py` (1367 lines, 58 tests);
  `zte_t_matrix_exact.py` (797 lines).
- Vol I capsule: `CLAUDE.md:1302`.
- Vol III status rows: `CLAUDE.md:125, 145, 732`.
- Cross-reference: `prop:ff-screening-coproduct-obstruction` at
  `chiral-bar-cobar/chapters/theory/ordered_associative_chiral_kd.tex:10176-10297`
  (Miura $(\Psi-1)/\Psi$ obstruction).
