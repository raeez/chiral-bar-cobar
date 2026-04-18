# Attack-and-Heal: gl_N chiral QG at N >= 3 + JKL26 obstruction

Date: 2026-04-18. Swarm block AP481-AP500 reserved for this wave.
Primary target: CLAUDE.md status-row "gl_N chiral QG" at line 598 vs.
inscribed theorem `thm:glN-chiral-qg` at
`chapters/theory/ordered_associative_chiral_kd.tex:10324`.

Cross-reference: this report supersedes the stale
"PROVED UNCONDITIONAL all N>=2 via Feigin-Frenkel screening" banner
that inherited AP256 aspirational-heal drift and AP271 reverse drift
(manuscript honest, metacognitive layer overstated). AP305 (pessimistic
drift) does not apply in reverse here: the CLAUDE.md row was overstated,
not understated.

## 1. Attack

### 1.1 Obstruction proposition: computation verified

Proposition `prop:ff-screening-coproduct-obstruction` at
`ordered_associative_chiral_kd.tex:10177-10297` computes
\[
 [Q_{\alpha_i}, \Delta_z^{\mathfrak{h}}]
 \;\in\; H^1_{\mathrm{ch}}\bigl(\mathfrak{h},\;
   \mathfrak{h}\otimes \mathfrak{h}[z,z^{-1}]\bigr)
\]
and identifies its representative with the spectral-residue cocycle
\[
 R_i(z)
 = \frac{\Psi-1}{\Psi}\;
  (\,:\!e^{\alpha_i\cdot\varphi(0)}\!:)
  \otimes
  (\,:\!e^{\alpha_i\cdot\varphi(-z)}\!:)
  \cdot (1 + O(z)).
\]
The proof (:10228-10297) evaluates the Heisenberg primitive coproduct
on the normal-ordered exponential
$:\!e^{\alpha_i\cdot\varphi(\zeta)}\!:$, tracks the one-loop
contraction $\alpha_i^2\langle\varphi(\zeta)\varphi(\zeta-z)\rangle
= (2/\Psi)\log z$, and extracts the regularised residue as
$(\Psi-1)/\Psi$.

Structural match: the prefactor $(\Psi-1)/\Psi$ is identically the
universal cross-term coefficient of `thm:miura-cross-universality` on
$J \otimes W_{s-1} + W_{s-1} \otimes J$ at every spin $s \geq 2$. This
is not a coincidence. If the Feigin-Frenkel screening descent worked,
the $\mathcal{W}_N$ coproduct would be the descent of the trivial
Heisenberg primitive coproduct modulo coboundaries in
$\Barord(\mathfrak{h})^{\otimes 2}$; the non-exact cocycle $R_i$
is *exactly* the non-trivial cross-term that appears on
$\mathcal{W}_N$.

### 1.2 Boundary checks

N = 2 (sl_2, $\mathcal{W}_2 = \mathrm{Vir}_c$): the obstruction
*exists* in the FF-screening picture (single simple root
$\alpha_1$), but is not the load-bearing route to unconditionality.
Unconditionality at $N = 2$ comes from the independently inscribed
$\fsl_2$ Yangian + affine $\widehat{\fsl}_2$ RTT datum
(`ex:gl2-chiral-qg`, :10000-10174) combined with the
Schiffmann-Vasserot identification of the rank-1 Jordan-quiver CoHA.
Neither route invokes FF-screening descent at $N = 2$.

N >= 3: the joint screening kernel
$\bigcap_{i=1}^{N-1}\ker Q_{\alpha_i}$ carries spin-$\geq 3$
generators with non-trivial cross-terms. The proof body
(:10288-10296) verifies non-exactness concretely at $N = 3$,
spin $s = 3$ with the Prochazka-Rapcak basis for $\mathcal{W}_3$:
the $W_3 \otimes J$ component of any putative trivialiser $h$ is
non-zero with coefficient $(\Psi-1)/\Psi$, contradicting
annihilation on the kernel.

Psi = 1 (free-boson point): the cocycle vanishes. At this point
the FF-screening descent is formally unobstructed, but $\Psi = 1$
is the degenerate free-boson limit of $\mathcal{W}_N$, not the
generic Koszul locus.

Psi = 0 (free abelian chiral algebra, identity QG): the RTT is
trivial, the $R$-matrix is scalar $u I$, and the question of
coproduct descent is vacuous.

Therefore at generic $\Psi$ in the Koszul locus and $N \geq 3$,
the FF-screening descent genuinely fails.

### 1.3 "Feigin-Frenkel replaces JKL26" claim: retracted

The inscribed theorem body at :10486-10519 already names JKL26 as
external input:
> This argument is the current source of unconditionality at N >= 3:
> a Feigin-Frenkel screening alternative (realising $\cW_N$ as an
> intersection $\bigcap_{i=1}^{N-1}\ker Q_{\alpha_i}$ inside a
> rank-(N-1) Heisenberg parent) would only descend a coproduct to
> the screening kernel if the screening operators $Q_{\alpha_i}$
> commuted with the Heisenberg coproduct up to exact terms [...]
> at $N \geq 3$ the coproduct construction is *external* to the
> Heisenberg parent and currently relies on [JKL26].

CLAUDE.md row 598 claim "JKL26 phantom eliminated" contradicted the
manuscript. AP271 (reverse drift): metacognitive layer lagged behind
manuscript retraction. Healed.

### 1.4 Lemma `qdet-central-all-N`: status check

Inscribed at :10675 with `\ClaimStatusProvedElsewhere` (not
`ProvedHere`). The argument has two parts:

(a) Classical statement: inherited from Molev `\cite{Molev07}`,
Theorems 1.6.4 (decreasing-column determinant formula) and 1.11.2
(centrality via antisymmetriser). External citation, correctly
tagged.

(b) Chiral extension: internal. The lemma proves that the Drinfeld
coproduct $\Delta_z$ commutes with Molev's antisymmetriser
specialisation; the antisymmetriser acts only on
$(\bC^N)^{\otimes N}$ tensor indices, which are untouched by $z$.
Chiral centrality is inherited from classical centrality.

CLAUDE.md prior claim "inscribed internally (Molev's antisymmetriser
argument, not external citation)" was imprecise: the lemma is tagged
`ProvedElsewhere` because it inherits from Molev. Healed.

Decreasing-column ordering discipline: `rem:qdet-decreasing-ordering`
at :10725-10764 proves that the increasing-index variant
$\mathrm{qdet}^{\uparrow} T(u)$ fails centrality at order $\Psi^2$
for $N \geq 3$; at $N = 2$ both orderings coincide by rank
coincidence ($S_2$ has a single non-trivial cycle, antisymmetriser
image codim 1 in $(\bC^2)^{\otimes 2}$). This is load-bearing at
$N \geq 3$.

### 1.5 Two-parameter gl_N RTT vs $\Sym^2(\mathfrak{gl}_N^*)^{\mathfrak{gl}_N}$

Decomposition $\mathfrak{gl}_N = \mathfrak{sl}_N \oplus \mathfrak{z}$
(center 1-dim, spanned by $I_N$). Ad-invariant symmetric bilinear
forms on $\mathfrak{gl}_N$:
- $B_{\mathrm{tr}}(X,Y) = \tr(XY)$ (Killing-like, restricts to a
  non-degenerate form on $\mathfrak{sl}_N$);
- $B_{\mathrm{ab}}(X,Y) = \tr(X)\tr(Y)$ (pulled back from the center).

For $N \geq 2$: $\dim\Sym^2(\mathfrak{sl}_N^*)^{\mathfrak{sl}_N} = 1$
(simple Lie algebras admit a unique invariant inner product up to
scalar). Adding the central form gives total dimension 2. Matches
`rem:e3-non-simple-gl-N` at `en_koszul_duality.tex:5576-5661`.

Verified at $N = 3$: trace form $\tr(XY)$ + central product
$\tr(X)\tr(Y)$, no third independent invariant. Verified at $N = 4$
by the same decomposition. Consistent with two-parameter RTT
$(R_{\mathrm{tr}}, R_{\mathrm{ab}})$ matching the two-parameter
$E_3$-deformation family.

## 2. Surviving core

Inscribed theorem as healed:

- $N = 2$: UNCONDITIONAL. Chiral bialgebra datum constructed from the
  $\fsl_2$ Yangian RTT + affine $\widehat{\fsl}_2$ route + SV CoHA.
  Neither Argument A's Koszul-locus abstraction nor JKL26 is required;
  both corroborate.

- $N \geq 3$: CONDITIONAL on `\cite{JKL26}` (Jindal-Kaubrys-Latyntsev
  vertex bialgebra theorem on the Jordan-quiver CoHA) as external
  input for Argument B. Argument A (Koszul-locus coderivation) covers
  the abstract level but does not realise the three-structure datum
  concretely without external input.

- All $N$: bialgebra, not Hopf. Full antipode lift is a PROVED
  NEGATIVE (`rem:chiral-bialgebra-not-hopf`, AP263): two obstructions
  (OPE, Hopf axiom). The datum is chiral-bialgebra, not
  chiral-Hopf.

- FF-screening descent: PROVED OBSTRUCTED at $N \geq 3$ by the
  explicit non-exact chiral 1-cocycle of coefficient $(\Psi-1)/\Psi$
  (`prop:ff-screening-coproduct-obstruction`). Does not bypass
  JKL26; sharpens it.

## 3. Heal

### 3.1 CLAUDE.md row 598 (gl_N chiral QG): rewritten.

Before: "PROVED UNCONDITIONAL all N>=2 via Feigin-Frenkel screening
(JKL26 phantom eliminated)".

After: honest scope qualification, naming $N = 2$ unconditional,
$N \geq 3$ conditional on JKL26, FF-screening descent obstructed
with explicit cocycle, bialgebra-not-Hopf per AP263, load-bearing
ordering discipline via the decreasing-column qdet. Full replacement
body cites `thm:glN-chiral-qg` at :10324,
`prop:ff-screening-coproduct-obstruction` at :10177,
`rem:chiral-bialgebra-not-hopf` at :8497,
`lem:qdet-central-all-N` at :10675,
`rem:qdet-decreasing-ordering` at :10727,
`rem:e3-non-simple-gl-N` at `en_koszul_duality.tex:5576`.

### 3.2 Theorem header rewritten.

Title extended to "unconditional at $N=2$, conditional on JKL26 at
$N \geq 3$". Opening sentence rewrites "chiral quantum group datum"
to "chiral *bialgebra* datum" per AP263. Scope paragraph inserted
after the status tag, naming the $N = 2$ unconditional route
(SV CoHA + sl_2 Yangian), the $N \geq 3$ dependence on JKL26, the
explicit FF-screening obstruction cocycle, and the Hopf-antipode
proved negative. The enumerated clauses (I)-(VI) and the proof body
are unchanged; the healing is at the level of the theorem statement
and its immediate scope, not at the level of the enumerated content.

## 4. Propagate

Three-volume grep against `\ref{thm:glN-chiral-qg}`:
- Vol I: preface.tex:1132, 4313 (neutral "concrete verifications
  through gl_N for N>=1"); chapter :9479 (in-chapter self-ref);
  survey_modular_koszul_duality_v2.tex:733 (neutral).
- Standalone ordered_chiral_homology.tex:3462, 3961, 4291 (standalone
  not `\input`-ed into main.tex; contains a duplicate label
  definition local to the standalone; scope-isolated; no action).
- Vol II, Vol III: no consumers.

Three-volume grep against `\ref{prop:ff-screening-coproduct-obstruction}`:
- ordered_associative_chiral_kd.tex:10223, 10301, 10511 (self-refs
  within the gl_N subsection).
- standalone/N4_mc4_completion.tex: one ref, in a remark citing the
  obstruction as structural explanation for non-descent; prose
  consistent with healed diagnosis; no edit required.

Three-volume grep against `\ref{lem:qdet-central-all-N}`:
- Chapter self-refs within Theorem 7.2 proof body and
  `rem:qdet-decreasing-ordering`.
- Vol II, Vol III: no consumers.

Three-volume grep against `\ref{thm:miura-cross-universality}`:
- Chapter self-refs in Example `ex:gl2-chiral-qg`, Proposition
  `prop:ff-screening-coproduct-obstruction`, Theorem Argument B.
- Preface: no ref to the `-monograph` suffixed label by this exact
  form (preface uses the suffixed variant).

AP256 + AP271 + AP305 violations in CLAUDE.md Chiral QG row at :596
were already healed in a prior pass and continue to correctly cite
`prop:ff-screening-coproduct-obstruction` with "Feigin-Frenkel is
not a drop-in replacement; the $(\Psi-1)/\Psi$ obstruction is
explicit". The row 598 correction now aligns with row 596.

## 5. New anti-pattern candidates

None. All four failure modes inside this wave (AP256 aspirational
heal, AP271 reverse drift, AP263 Hopf/bialgebra naming, AP287
cross-volume/external theorem with conditional status) are
pre-catalogued.

The block AP481-AP500 remains unconsumed.

## 6. Verdict

- Row 598 healed: downgraded "UNCONDITIONAL all N>=2" to the honest
  two-regime accounting.
- Theorem header healed: scope qualified, bialgebra naming enforced.
- Obstruction proposition inscribed (was already inscribed).
- Consumer propagation complete.
- No regressions to manuscript mathematical content; all healing is
  at scope / status / naming.

Author: Raeez Lorgat.
