# Attack-and-Heal: KZB flatness / Bernard heat identity

Date: 2026-04-18. Author: Raeez Lorgat. Adversarial-swarm cohort.

AP block consumed: AP521-AP524 (this swarm) + AP282/AP283 (prior, binding).

## PHASE 1 — First-principles attack

### (i) Bernard heat identity: primary-source verification

**Primary source.** D. Bernard, "On the Wess--Zumino--Witten models on the torus", Nucl. Phys. B 303 (1988) 77--93. Equation (2.15)-(2.17) of Bernard's paper (and independently Eichler--Zagier, "The theory of Jacobi forms", Birkhäuser 1985, Ch. III) states the heat equation for the Jacobi odd theta on the torus with periods $(1, \tau)$:

$$
4\pi i \,\partial_\tau \theta_1(z, \tau) \;=\; \partial_z^2 \theta_1(z, \tau).
\tag{Bernard 2.15}
$$

The prefactor is $1/(4\pi i)$ (not $1/(2\pi i)$) in the normalization where $\tau$ is the upper-half-plane parameter and $q = e^{2\pi i \tau}$. This is the convention used by Bernard, Felder, Etingof--Frenkel--Kirillov, and Calaque--Enriquez--Etingof. Eynard--Orantin topological recursion uses a DIFFERENT prefactor convention (Bergman kernel normalization) that absorbs a factor of $2$; the resulting closed form differs cosmetically, not substantively. There is no programme-level convention drift.

**Consequence for $\zeta$.** The Weierstrass zeta on the lattice $\Lambda_\tau = \mathbb{Z} + \tau \mathbb{Z}$ is
$$
\zeta(z, \tau) \;=\; \frac{\theta_1'(z,\tau)}{\theta_1(z,\tau)} + 2\eta_1(\tau)\, z, \qquad \eta_1(\tau) = \frac{\pi^2}{6} E_2(\tau).
\tag{$\ast$}
$$
The full quasi-period term $2\eta_1(\tau) z$ is LOAD-BEARING (AP275 / FM30: the programme's engine at `compute/lib/theorem_genus1_seven_faces_engine.py:244-260` correctly uses the full form; the xfail test's naive comparison does not).

Differentiate $(\ast)$ in $\tau$ and use Bernard 2.15:
$$
4\pi i \,\partial_\tau \zeta(z, \tau)
\;=\; \partial_z\!\left(\frac{\theta_1''(z,\tau)}{\theta_1(z,\tau)}\right) + 8\pi i \, \eta_1'(\tau)\, z.
$$
Compute $\theta_1''/\theta_1 = (\theta_1'/\theta_1)' + (\theta_1'/\theta_1)^2$, use $\theta_1'/\theta_1 = \zeta - 2\eta_1 z$ and $\zeta' = -\wp$:
$$
\frac{\theta_1''}{\theta_1} = -\wp(z,\tau) - 2\eta_1(\tau) + (\zeta(z,\tau) - 2\eta_1(\tau)\, z)^2.
$$
Differentiate once more in $z$:
$$
\boxed{\;
4\pi i \,\partial_\tau \zeta(z, \tau)
\;=\; -\wp'(z, \tau) + 2\big(\zeta(z, \tau) - 2\eta_1(\tau)\, z\big)\big({-}\wp(z, \tau) - 2\eta_1(\tau)\big) + 8\pi i\, \eta_1'(\tau)\, z.
\;}
\tag{Bernard-$\zeta$}
$$

The naive identity $\partial_\tau \zeta = \wp'$ (equivalently $-\zeta''$) from the xfail test DROPS three items:

1. the heat-equation prefactor $1/(4\pi i)$;
2. the nonlinear term $2(\zeta - 2\eta_1 z)(-\wp - 2\eta_1) = -2\zeta\wp + O(\eta_1)$, which is cubic in $\zeta,\wp$;
3. the quasi-period drift $8\pi i\, \eta_1'(\tau)\, z$, which is linear in $z$.

Items (2) and (3) are the genuine elliptic content of Bernard's identity. Item (3) alone couples to the Halphen--Ramanujan system:

$$
\eta_1'(\tau) = \frac{\pi^2}{6} \partial_\tau E_2(\tau) = \frac{\pi^2}{72}(E_2^2 - E_4),
$$
using Ramanujan's 1916 identity (Ramanujan, "On certain arithmetical functions", Trans. Camb. Phil. Soc. 22 (1916) 159--184, §2). So the naive xfail reason is correct at the DIRECTIONAL level (Halphen--Ramanujan DOES enter) and wrong at the LITERAL level (it is not the sole content; items (1) and (2) enter equally).

### (ii) KZB 2-point commutator is trivial

For $n=2$ on the torus with the Felder normalization $A_z = \zeta(z_{12}, \tau)\, \Omega / (k+h^\vee)$, $A_\tau = \wp(z_{12}, \tau)\, \Omega / (k+h^\vee)$: since both connection matrices are SCALAR multiples of the single Casimir $\Omega$, and $\Omega$ self-commutes, $[A_z, A_\tau] = 0$ AUTOMATICALLY, regardless of the $\zeta,\wp$ identities. The 2-point $[\nabla_z, \nabla_\tau] = 0$ reduces to the SCALAR equation
$$
\partial_\tau \zeta(z, \tau) \;\stackrel{?}{=}\; \partial_z \wp(z, \tau) = \wp'(z, \tau).
$$
By (Bernard-$\zeta$) this FAILS on the nose. It is an equation that holds ONLY modulo the Halphen--Ramanujan cross-cancellation AND the $1/(4\pi i)$ absorption AND the nonlinear $\zeta\wp$ subtraction. The 2-point case is therefore NOT trivial in the scalar sector; only the MATRIX commutator is trivial.

The real content of "KZB is flat at 2-point" is a SCALAR partial-differential identity whose leading-$\hbar$ reduction is the Halphen--Ramanujan system after $\eta_1 \mapsto (\pi^2/6) E_2$.

### (iii) 3-point integrability and Halphen--Ramanujan

For $n \geq 3$, the commutator $[A_z^{(i)}, A_\tau^{(i)}]$ no longer vanishes (there are cross-pair couplings $\Omega_{ij}$ and $\Omega_{ik}$ with $j \neq k$, and $[\Omega_{ij}, \Omega_{ik}] \neq 0$). The integrability becomes a NONTRIVIAL elliptic Yang--Baxter-type system. Felder 1994 (Int. Congr. Math., "Conformal field theory and integrable systems associated to elliptic curves", §3) and Calaque--Enriquez--Etingof 2010 ("Universal KZB equations: the elliptic case", Algebr. Prog. Geom., Prog. Math. 269) show that flatness at $n \geq 3$ is equivalent to:

- the elliptic classical Yang--Baxter equation (in the Cartan direction via the dynamical shift), and
- the Halphen--Ramanujan differential system for $E_2, E_4, E_6$:
$$
\partial_\tau E_2 = \tfrac{1}{12}(E_2^2 - E_4), \quad \partial_\tau E_4 = \tfrac{1}{3}(E_2 E_4 - E_6), \quad \partial_\tau E_6 = \tfrac{1}{2}(E_2 E_6 - E_4^2).
$$

This system (Ramanujan 1916 §2; classical form in Halphen, "Traité des fonctions elliptiques et de leurs applications", Gauthier-Villars 1886, Ch. II) closes the differentiation of Eisenstein series in $\tau$. It is the structural input that makes the elliptic bar propagator $\zeta$ vary correctly with $\tau$.

The xfail REASON ("correct KZB flatness involves Halphen/Ramanujan system for Eisenstein series") is therefore DIRECTIONALLY correct at $n \geq 3$, and INCOMPLETE at $n = 2$ (where the real issue is the Bernard prefactor + nonlinear terms, not purely the Halphen--Ramanujan system).

### (iv) sl_2 "PROVED leading-order ℏ" — trace the actual claim

`standalone/seven_faces.tex:1005-1017`, `thm:chiral-qg-equiv-elliptic-sf`, tagged `\ClaimStatusProvedElsewhere`:

> For $\fsl_2$ on a smooth elliptic curve $E_\tau$, the Felder dynamical $R$-matrix $R(z, \lambda, \tau)$ [...] and the Knizhnik--Zamolodchikov--Bernard connection determine each other to leading order in $\hbar$. The Fay trisecant identity [...] provides the modular compatibility that replaces the pentagon; the role of the Drinfeld associator is played by the modular correction at the heat-equation prefactor $1/(4\pi i)$ on the diagonal and $1/(2\pi i)$ off-diagonal.

This statement is a STRUCTURAL MATCHING claim: the Felder $R$ and the KZB connection are mutually determined at $O(\hbar)$. It is NOT a chain-level flatness proof; it is not even a leading-$\hbar$ flatness proof. The tag `\ClaimStatusProvedElsewhere` attributes the result to Felder 1994 and EFK98 without inscribing a proof body. The standalone is also NOT `\input`-ed into `main.tex` per AP255 audit of 2026-04-17.

The CLAUDE.md row "PROVED leading-order ℏ for sl_2 via Felder R + KZB + Fay trisecant" OVERSTATES by conflating:

- (a) the STRUCTURAL matching (Felder $R$ $\leftrightarrow$ KZB at $O(\hbar)$), which is cited from Felder 1994 / EFK98;
- (b) FLATNESS of the KZB connection at leading $\hbar$, which requires the Halphen--Ramanujan closure and is NOT inscribed in Vol I at chain level.

The structural matching is attributed to Felder 1994; flatness is a separate theorem of Felder 1994 / EFK98 Ch. 5. Neither is inscribed in Vol I chapters, only the standalone scope gloss.

## PHASE 2 — Surviving core

**PROVED (attribution-level, not chain-level in Vol I):**

1. **Heat-equation prefactor $1/(4\pi i)$ on diagonal, $1/(2\pi i)$ off-diagonal**: `rem:kzb-heat-prefactor` at `ordered_associative_chiral_kd.tex:12142-12155`, verified numerically at $< 10^{-14}$ on 5 generic points. This is (Bernard 2.15) plus the symmetric-matrix chain-rule factor of 2 on the diagonal. Internally consistent with engine `weierstrass_eta1` and `weierstrass_zeta` using the full $\zeta = \theta_1'/\theta_1 + 2\eta_1 z$ form.
2. **Felder $R$ $\leftrightarrow$ KZB at $O(\hbar)$** (structural matching): `thm:chiral-qg-equiv-elliptic-sf` standalone-only, `\ClaimStatusProvedElsewhere` citing Felder 1994 + EFK98 Ch. 5.
3. **2-point commutator $[A_z, A_\tau] = 0$**: trivial since both are scalar multiples of $\Omega$; test `test_kzb_flatness_2pt_commutator_vanishes` passes. This is NOT KZB flatness — it is the trivial matrix-commutator sub-claim.

**PARTIAL / FRONTIER:**

4. **Full Bernard heat identity** (Bernard-$\zeta$, equation displayed above): has three terms (prefactor $1/(4\pi i)$, nonlinear $(\zeta-2\eta_1 z)(-\wp-2\eta_1)$, quasi-period drift $8\pi i \eta_1'(\tau) z$). NONE of the three is captured by the xfail test's naive $\partial_\tau \zeta = \wp'$. The identity is classical (derivable from Bernard 2.15 by two-line $z$-differentiation); programme has not inscribed it.
5. **2-point SCALAR flatness** (with proper prefactor + nonlinear + quasi-period terms): follows from Bernard-$\zeta$ modulo the Halphen--Ramanujan closure $\eta_1' = (\pi^2/72)(E_2^2 - E_4)$. Not inscribed.
6. **$n \geq 3$ integrability**: requires Halphen--Ramanujan system + elliptic CYBE with dynamical shift. Cited in `chiral_climax_platonic.tex:982-983` (Bernard 1988, CEE 2010), not inscribed as a theorem.

**NOT PROVED:**

7. **Chain-level KZB flatness** (in the sense of strict $\mathrm{d}_{\mathrm{KZB}}^2 = 0$ on the bar complex including quasi-modular corrections): not inscribed anywhere; closest is `conj:trig-elliptic-ordered` at `ordered_associative_chiral_kd.tex:11916` (conjectural).

## PHASE 3 — Heal

### Option taken: (b) + (c) combined.

- (b) RETRACT the CLAUDE.md status row "PROVED leading-order ℏ for sl_2" to "VERIFIED at 2-point prefactor; 3-point integrability FRONTIER (Halphen--Ramanujan closure)" with AP282/AP283 cross-reference.
- (c) UPGRADE the xfail test with the CORRECT scalar Bernard identity, testing the (Bernard-$\zeta$) form at 2 points against numerical finite-differences. Keep the naive version DELETED (it tests a wrong identity), replace with the real one. Keep the matrix-commutator companion test (which is trivially true and documents why the 2-point case is structurally uninformative at the matrix level).
- (a) ALSO: inscribe a short theorem `thm:kzb-bernard-heat-identity` at `ordered_associative_chiral_kd.tex` near `rem:kzb-heat-prefactor` stating (Bernard-$\zeta$) as `\ClaimStatusProvedElsewhere` attributed to Bernard 1988 eq. (2.15), and citing Ramanujan 1916 / Halphen 1886 for the Eisenstein closure. This is a KNOWN classical identity; we inscribe the exact form so future audits do not drift.

## PHASE 4 — Inscription

1. Edit `chapters/theory/ordered_associative_chiral_kd.tex` around line 12142 to append, after `rem:kzb-heat-prefactor`, a new `remark[Bernard heat identity for Weierstrass zeta]` stating (Bernard-$\zeta$) with citations to Bernard 1988 (Nucl. Phys. B 303, eq. 2.15), Ramanujan 1916 (Trans. Camb. Phil. Soc. 22, §2), Halphen 1886 (Traité, Ch. II), Felder 1994 (ICM), Etingof--Frenkel--Kirillov 1998 (Ch. 5), Calaque--Enriquez--Etingof 2010 (Prog. Math. 269). Tag `\ClaimStatusProvedElsewhere`.

2. Edit `compute/lib/theorem_genus1_seven_faces_engine.py` `verify_kzb_flatness_2pt` to compute the Bernard-$\zeta$ identity directly: verify
$$
4\pi i\,\partial_\tau\zeta(z,\tau) + \wp'(z,\tau) - 2(\zeta - 2\eta_1 z)(-\wp - 2\eta_1) - 8\pi i\,\eta_1'(\tau)\, z \;\overset{?}{=}\; 0
$$
at machine precision. Rename the function to `verify_bernard_heat_identity_zeta` (descriptive) and retain a thin backward-compatible alias. The old function's documentation was honest about its own uncertainty ("Let's just check numerically"); the new function states the identity and checks it.

3. Edit `compute/tests/test_theorem_genus1_seven_faces_engine.py`:
   - Replace the xfail `test_kzb_flatness_2pt` with a NON-xfail test `test_bernard_heat_identity_zeta_scalar` that calls the upgraded engine function.
   - Retain `test_kzb_flatness_2pt_commutator_vanishes` (matrix commutator trivially zero).
   - Add a module-level comment documenting the xfail replacement.

## PHASE 5 — Propagation

Grep targets (three volumes):

- `\ref{rem:kzb-heat-prefactor}` — currently $\leq 3$ consumer sites.
- `∂_τ ζ = ℘'` or `d_tau zeta = wp'` (naive form) — currently 0 hits in typeset `.tex` (good; bug lived only in the Python engine docstring and the xfail reason string).
- `d_tau(wp_1)` (already-retracted confabulation) — 0 hits in `.tex` / engine (confirmed 2026-04-17, AP283).
- CLAUDE.md KZB row at line 630.

Consumer updates:

1. `CLAUDE.md` KZB flatness row: rewrite to match the healed state.
2. `CLAUDE.md` "Elliptic chiral QG" row at line 593: rewrite "PROVED leading-order ℏ" to "Felder $R$ $\leftrightarrow$ KZB structural matching at $O(\hbar)$ (standalone-only; Felder 1994, EFK98 Ch. 5); 2-point Bernard identity verified in engine; chain-level flatness FRONTIER". This row was already caveated by AP275 (inverted convention warning about "NOT Weierstrass $\zeta$"); the prior AP275 correction and this AP521 heal are consistent.
3. CLAUDE.md `AP287/AP288` + new `AP521` entry.

## AP521 (Bernard heat identity: literal vs directional xfail-reason content)

An xfail test's `reason=` string cites a classical identity ("Halphen/Ramanujan system") as the reason the naive form fails, but the classical identity is only ONE of three corrections to the naive form; the OTHER two (heat-equation prefactor $1/(4\pi i)$, nonlinear $\zeta\wp$ cross-term) dominate at leading $\hbar$ and are structurally unrelated to the cited system. A reader (or future LLM agent) who attempts to heal the xfail by inscribing ONLY the cited classical input will fail to recover the scalar identity. Canonical violation: `test_kzb_flatness_2pt` xfail reason "correct KZB flatness involves Halphen/Ramanujan system for Eisenstein series" — the Halphen--Ramanujan closure enters at 3-point and via $\partial_\tau \eta_1(\tau)$; at 2-point the dominant miss is the Bernard heat prefactor and the nonlinear $(\zeta - 2\eta_1 z)(-\wp - 2\eta_1)$ correction, NEITHER of which is captured by "Halphen/Ramanujan". Counter: xfail reason strings must state ALL items the current test fails to capture, ordered by dominance; partial citations steer healing in the wrong direction. Healed 2026-04-18 by upgrading the engine to the full (Bernard-$\zeta$) form and retiring the xfail.

## AP522 (Structural-matching claim vs flatness claim conflation)

"Felder $R$ and KZB determine each other at $O(\hbar)$" is a STRUCTURAL MATCHING claim (two objects are related by a specific map). "KZB is flat at $O(\hbar)$" is a FLATNESS claim (one object's commutator vanishes). Conflating the two — as CLAUDE.md did by writing "PROVED leading-order ℏ via Felder $R$ + KZB + Fay trisecant" — produces a status row whose headline reads as a flatness certification while the underlying inscription is only the structural matching. Canonical violation: CLAUDE.md line 593, `thm:chiral-qg-equiv-elliptic-sf` inscribes matching (`\ClaimStatusProvedElsewhere` attributing to Felder 1994 / EFK98); the row glosses this as "PROVED leading-order ℏ" without naming the claim. Counter: status rows must name the claim type (matching / flatness / equivalence / presentation) and cite the inscription; "PROVED X" without X is status inflation. Healed 2026-04-18 by rewriting the row to "Felder $R$ $\leftrightarrow$ KZB structural matching at $O(\hbar)$".

## AP523 (Naive-identity engine comment becomes canonical claim via xfail reason)

An engine's docstring carries an honest uncertain-derivation comment ("Let's just check numerically", `theorem_genus1_seven_faces_engine.py:880`). The test file wraps the engine in `@pytest.mark.xfail` with a reason string that HARDENS the uncertainty into a definite-sounding but wrong claim about what the engine needs. CLAUDE.md later quotes the xfail reason string verbatim as the frontier status. The engine's honest "check numerically" has been laundered through the xfail into a canonical programme-status claim. Canonical violation: engine comment → xfail reason → CLAUDE.md row, three-step naive-identity laundering. Counter: xfail reasons quoted in CLAUDE.md must be spot-checked against the engine's actual code body and derivation, not the xfail reason string. Healed 2026-04-18 by rewriting the engine function to compute the correct Bernard-$\zeta$ form and removing the xfail.

## AP524 (Scalar-vs-matrix flatness separation missing in 2-point tests)

A test named `test_kzb_flatness_2pt` tests a MATRIX commutator that vanishes trivially (Ω self-commutes). The SCALAR equation (the coefficient of Ω, which is the actual content of the Bernard-$\zeta$ identity) is a separate non-trivial check. Current test suite has two tests — `test_kzb_flatness_2pt` (xfail, tests naive scalar) and `test_kzb_flatness_2pt_commutator_vanishes` (passes, tests trivial matrix). The naming does not signal that the former is the SCALAR test and the latter is the MATRIX test. Canonical violation: `test_theorem_genus1_seven_faces_engine.py:434-443`. Counter: at 2-point where $[A_z, A_\tau] = 0$ automatically, the flatness test has exactly ONE interesting scalar equation; name the test accordingly. Healed 2026-04-18 by renaming to `test_bernard_heat_identity_zeta_scalar` (scalar content) and `test_kzb_2pt_matrix_commutator_trivially_vanishes` (matrix content).
