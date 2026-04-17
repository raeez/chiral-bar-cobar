# Wave 2 (2026-04-18) Attack + Heal: Genus-2 DDYBE face-model row

Target: CLAUDE.md "DDYBE face model" theorem-status row (line 625), the
FM38 failure-mode entry (line 560), and the stale
`rem:ddybe-face-model` passage at
`chapters/theory/higher_genus_modular_koszul.tex:34451-34474`.

Author: Raeez Lorgat. No AI attribution.

## ATTACK LEDGER

Linear whole-file read of `chapters/theory/genus_2_ddybe_platonic.tex`
(764 lines, chunks 1-250, 250-500, 500-764 — contiguous cover).
Cross-checked against `compute/lib/face_model_ddybe_engine.py` and
`compute/tests/test_face_model_ddybe_engine.py`.

The 2026-04-17 Wave-5 heal (`wave5_genus_2_ddybe_attack_heal.md`, 276
lines) already installed the Platonic-ideal scope restriction. The
chapter is structurally clean. Residual drifts all live OUTSIDE the
chapter.

1. **AP271 reverse-drift, CLAUDE.md row 625.** The row read "Generic-Ω
   DDYBE: 5 tests at T4" and "Full 29 face-model tests". The Platonic
   chapter's `rem:g2-corrigenda` (line 666-684) explicitly inscribes 4
   T4 generic-Ω tests + 1 T3 diagonal-Ω consistency check + 30-test
   total. Row was carrying a retracted count.

2. **AP271 reverse-drift, FM38 (CLAUDE.md:560).** "29 tests" stale
   against the inscribed 30-test suite and the 4+1 T4/T3 disaggregation.

3. **AP271 reverse-drift, `higher_genus_modular_koszul.tex:34451`
   `rem:ddybe-face-model`.** Still read "relative error < 10^{-12}" and
   "29 compute tests". The `10^{-12}` was the prior CLAUDE.md stale
   advertisement; the inscribed Platonic corrigenda (`rem:g2-corrigenda`
   item (a)) retracted it to $10^{-4}$ with 4 generic-Ω tests. The
   primary chapter source had never been updated to match its own
   Platonic-ideal inscription — a load-bearing AP271 violation, since
   `higher_genus_modular_koszul.tex` is the source Zhu96-style reader
   opens first.

4. **Diagonal-Ω retraction propagation.** The Wave-5 heal retracted
   "two genus-1 DYBE copies" to "a single Felder copy + trivial
   $\theta_3(0|\tau_2)$ factor"; CLAUDE.md row 625 still carried the
   retracted two-copy slogan.

5. **AP157 scope (separating vs non-separating).** Explicit in the
   chapter (`rem:ap157-g2`, `rem:g2-nonseparating-untested`). The
   CLAUDE.md row conflated "separating degeneration AP157-empty" with
   the untested non-separating frontier. Propagated the
   frontier-distinction into the row.

6. **AP287 structural-impossibility primitive (T1 tier).**
   $\theta_1$ antisymmetry at $10^{-12}$ tests floating-point
   conditioning, not mathematics. The chapter's
   `rem:tolerance-ladder` already labels T1 "exact algebraic identities
   in numpy" (engineering budget). Made the primitive-tautology nature
   explicit in the CLAUDE.md row so a future reader does not count T1
   towards mathematical verification.

7. **Heat-prefactor (FM34a) inside `conj:g2-ddybe`.** The conjecture's
   `eq:ddybe-coupling` at `higher_genus_modular_koszul.tex:34408` writes
   $\partial R/\partial\Omega_{\alpha\beta}=(1/(2\pi i))\partial^2 R/
   (\partial\lambda_\alpha\partial\lambda_\beta)$ uniformly for both
   diagonal $\alpha=\beta$ and off-diagonal $\alpha\neq\beta$. FM34a
   records the symmetric-matrix chain rule: diagonal should be
   $1/(4\pi i)$, off-diagonal $1/(2\pi i)$. Because the surrounding
   environment is `\begin{conjecture}` with
   `\ClaimStatusConjectured`, the identity is not load-bearing for any
   ProvedHere theorem; this is a residual ambiguity WITHIN the
   conjecture, NOT a production bug. Flagged but NOT edited: the
   Platonic theorem (i) at diagonal $\Omega$ and the infinitesimal
   heat-equation-symmetry argument cited as "infinitesimal proved"
   should be re-audited in a later wave to determine which prefactor
   convention the proved-infinitesimal statement uses. If the
   infinitesimal proof uses the symmetric-matrix convention, the
   conjecture's display needs an explicit $(1/(2\pi i))$ for
   $\alpha\neq\beta$ and $(1/(4\pi i))$ for $\alpha=\beta$.

## SURVIVING CORE (Drinfeld)

The face-model $R$-matrix at genus 2 reduces exactly to a single
genus-1 Felder $R$-matrix at diagonal $\Omega$ (vacuously
doubly-dynamical there). At generic $\Omega \in \HHH_2$ with
$\Omega_{12}\neq 0$, the doubly-dynamical Yang-Baxter equation holds
to relative residual $<10^{-4}$ across four sampled parameter points
— an engineering truncation budget, not a theoretical bound. The
residual conjecture `conj:g2-ddybe` — finite-$\hbar$ commutativity of
the two doubly-dynamical Casimirs attached to the two $B$-cycles of
$\Sigma_2$ — remains ClaimStatusConjectured; its genuine frontier
target is the non-separating degeneration
$\Omega_{22}\to i\infty$ with $\Omega_{12}$ held fixed nonzero,
where the off-diagonal period survives the limit and encodes
twisted modular data invisible to the separating boundary.

## HEAL PLAN (executed)

1. `chapters/theory/higher_genus_modular_koszul.tex:34451-34474`:
   `rem:ddybe-face-model` body rewritten from "$10^{-12}$, 29 tests,
   two copies of genus-1 DYBE" to "$10^{-4}$ engineering budget, 4
   generic-$\Omega$ + 1 tier-(T3) diagonal consistency check, 30
   tests total; reduces to a single Felder DYBE at diagonal $\Omega$
   with cancelling $\theta_3(0|\tau_2)$ normalisation; numerical
   evidence, not proof; pointer to the Platonic-ideal chapter".

2. CLAUDE.md FM38 (line 560): "29 tests" replaced with the 4 T4 + 1
   T3 disaggregation and the 30-total count. `conj:g2-ddybe` status
   re-stated as `ClaimStatusConjectured`.

3. CLAUDE.md "DDYBE face model" row 625: "5 tests at T4" → "4 tests
   at T4 (named) + 1 T3 consistency check"; "two genus-1 DYBE copies"
   retracted to "single Felder copy + trivial $\theta_3(0|\tau_2)$";
   "29 face-model tests" → "30 face-model tests"; non-separating
   degeneration flagged as untested frontier; T1 tier explicitly
   labelled "primitive-tautology tier (AP287)"; T4 explicitly labelled
   "engineering budget, NOT theoretical error term".

4. Heat-prefactor audit (FM34a) inside `conj:g2-ddybe`: flagged as
   residual ambiguity; NOT edited this wave because the conjecture
   carries `\ClaimStatusConjectured` and the identity is not
   load-bearing for any ProvedHere theorem. Proposed as a specific
   audit target for a future wave: reconcile `eq:ddybe-coupling`
   prefactor with the symmetric-matrix chain rule, either by splitting
   the display into $(\alpha=\beta)$ and $(\alpha\neq\beta)$ cases or
   by adopting a convention that absorbs the factor 2.

5. No commits. No AI attribution. Heals staged in working tree.

## COMMIT PLAN

Single commit when session closes, after build verification:

- `M chapters/theory/higher_genus_modular_koszul.tex` —
  `rem:ddybe-face-model` rectification.
- `M CLAUDE.md` — FM38 and DDYBE-face-model row rectification.
- `A adversarial_swarm_20260418/wave2_g2_ddybe_attack_heal.md` —
  this note.

Message (HEREDOC): "Vol I Wave-2 g2 DDYBE reverse-drift heal: CLAUDE.md
row 625 + FM38 + rem:ddybe-face-model rectified against Platonic-ideal
chapter (10^{-4} not 10^{-12}, 30 tests not 29, 4 T4 + 1 T3
disaggregated, single-Felder retraction propagated, non-separating
frontier inscribed)". Author Raeez Lorgat.
