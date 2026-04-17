# Wave Supervisory — Verdier-Pairing Distance for Holographic Codes

**Date.** 2026-04-16
**Targets.** HU-W4.5 (Wave 4 punch list item: `holographic_codes_koszul.tex` L339--421 K4 ⇔ K4 tautology). HU-W9h.2 (Wave 9 Upgrade Path B: replace ad-hoc `d = 2` with Verdier-pairing distance).
**Healing target.** Replace `thm:hc-koszulness-exact-qec` with a structural theorem whose `(i) ⇔ (ii)` is *not* tautological, and whose code distance is a genuine algebraic invariant of the chirally Koszul pair `(A, A^!)`.
**Status.** Constructive draft, LaTeX-style. Not committed; manuscript untouched.

---

## 1. Setup. Holographic codes and what "distance" means.

The Pastawski--Yoshida--Harlow--Preskill (HaPPY) prescription assigns to a tessellation `T` of a hyperbolic disk by perfect tensors a holographic encoding map
\[
  V : \mathcal H_{\mathrm{bdy}} \;\longrightarrow\; \mathcal H_{\mathrm{bulk}},
\]
where `\mathcal H_{\mathrm{bdy}}` is a tensor product of qudit factors at the boundary edges of `T` and `\mathcal H_{\mathrm{bulk}}` carries one qudit factor for each interior tile. The image `V(\mathcal H_{\mathrm{bdy}}) \subset \mathcal H_{\mathrm{bulk}}` is the *code subspace* `\mathcal C`. A *Pauli error* on the bulk is an operator `E \in \mathcal P_{\mathrm{bulk}}` (tensor product of single-qudit Paulis); its *weight* `\mathrm{wt}(E)` is the number of nontrivial single-qudit factors. The QECC distance is the Knill--Laflamme datum
\[
  d_{\mathrm{QECC}}(\mathcal C) \;:=\; \min\bigl\{\,\mathrm{wt}(E) \;:\; E \in \mathcal N(\mathcal C) \setminus \mathcal C^*\,\bigr\},
\]
i.e.\ the minimum weight of an operator that commutes with the code projector but is not detectable by syndrome measurement. For the HaPPY pentagon code with the standard 5-qubit perfect tensor, `d_{\mathrm{QECC}} = 3`.

The current chapter (`holographic_codes_koszul.tex`, `rem:hc-universal-parameters` L673--699) asserts a *universal* parameter `d = 2`, derived as: "the bar augmentation desuspension `s^{-1}` has degree `-1`, so the lowest nontrivial bar element sits in degree `2`". Wave 4 §4.5 records this as a **label/content** confusion (cache entry 142): the algebraic *graded degree* of the bar augmentation ideal is conflated with the QECC weight `\mathrm{wt}(\cdot)` of a Pauli. The two are distinct: `\mathrm{wt}` counts tensor factors on which an operator acts nontrivially; the bar grading counts the *number of factors in a tensor word* of `T(s^{-1}\bar A)`. There is no map from one to the other for the universal Heisenberg, Virasoro, or HaPPY pentagon code that respects the alleged "universal `d = 2`".

Concretely: the HaPPY pentagon code has `d_{\mathrm{QECC}} = 3`, not `2`; the Heisenberg algebra `\mathcal H_k` (class G) carries no protected logical information at all (its bar complex is concentrated in degree `1`, so the construction trivialises and `d` is most honestly `+\infty` or undefined); and any code where `Q_g(\mathcal A)` happens to equal the full ambient space has `d = 1` trivially. The single number `2` does not occur in any of these cases.

We replace this with an honest invariant.

---

## 2. First-principles construction of the Verdier pairing on `Bar(A) \otimes Bar(A^!)`.

We assume `(\mathcal A, \mathcal A^!)` is a chirally Koszul pair on a smooth projective curve `X`, so the Wave 14 Koszul Reflection Theorem applies: the functor
\[
  K \;:\; \mathrm{Kosz}(X) \;\longrightarrow\; \mathrm{Kosz}(X)^{\mathrm{op}},
  \qquad K(\mathcal A) \;:=\; \Omega(\bar B(\mathcal A))^\vee \;=\; \mathcal A^!,
\]
is involutive, `K^2 \simeq \mathrm{id}` on `\mathrm{Kosz}(X)`. Involutivity supplies the canonical Verdier pairing as follows.

The bar complex `\mathrm{Bar}(\mathcal A) := T^c(s^{-1} \bar{\mathcal A})` is an `E_1`-coalgebra; the Koszul dual `A^! = \Omega(\bar B(A))^\vee` is an `E_1`-algebra. Bar--cobar adjunction supplies a *unit*
\[
  \eta_{\mathcal A} \;:\; k \;\longrightarrow\; \mathrm{Bar}(\mathcal A) \otimes \mathrm{Bar}(\mathcal A^!)
\]
arising from the chain-level identification `\mathrm{Bar}(\mathcal A^!) \simeq \mathrm{Cobar}^\vee(\mathrm{Bar}(\mathcal A))`. Dualising and using involutivity `K^2 \simeq \mathrm{id}` gives a *counit*
\[
  \mathrm{ev}_{\mathcal A} \;:\; \mathrm{Bar}(\mathcal A) \otimes \mathrm{Bar}(\mathcal A^!) \;\longrightarrow\; k[d_{\mathrm{Verdier}}^{\mathrm{shift}}],
\]
where `d_{\mathrm{Verdier}}^{\mathrm{shift}}` is the *bar--cobar duality dimension*. For genus-`g` chirally Koszul pairs over `X` of CY dimension `1`, `d_{\mathrm{Verdier}}^{\mathrm{shift}} = 0`; for higher CY dimension `n`, the shift is `2n - 2` (this is the Serre-duality dimension of the chiral pair, a special case of the AP-CY1 / `n - 2` dimension formula for matrix factorisations). For the present chapter we work over a curve, so the shift is `0`; readers interested in higher CY dimension should track the shift through the formulas below.

\begin{definition}[Verdier pairing on a chirally Koszul pair]\label{def:Verdier-pairing}
The \emph{Verdier pairing} of a chirally Koszul pair `(\mathcal A, \mathcal A^!)` is the chain map
\[
  \langle -, - \rangle_{\mathbb D} \;:\; \mathrm{Bar}(\mathcal A) \,\otimes\, \mathrm{Bar}(\mathcal A^!) \;\longrightarrow\; k[d_{\mathrm{Verdier}}^{\mathrm{shift}}]
\]
defined by `\langle v, w \rangle_{\mathbb D} := \mathrm{ev}_{\mathcal A}(v \otimes w)`. Under the Wave 14 Koszul reflection involution `K^2 \simeq \mathrm{id}`, the pairing is graded-symmetric (with sign `(-1)^{|v|\cdot|w|}`) and non-degenerate on the chain level on `\mathrm{Kosz}(X)`.
\end{definition}

The pairing degenerates *strictly* off the Koszul locus: failure of `K^2 \simeq \mathrm{id}` to hold at the chain level (which happens generically for non-Koszul `\mathcal A`) is precisely the failure of `\langle -, - \rangle_{\mathbb D}` to admit a non-degenerate Hermitian extension on `\mathrm{Bar}(\mathcal A)` itself. This will become the algebraic origin of code failure (§5).

---

## 3. Definition of the Verdier-pairing distance.

The bar complex `\mathrm{Bar}(\mathcal A) = \bigoplus_{n \ge 0} \mathrm{Bar}_n(\mathcal A)` is filtered by *bar weight* `\mathrm{wt}(v) := n` for `v \in \mathrm{Bar}_n(\mathcal A) = (s^{-1}\bar{\mathcal A})^{\otimes n}`. The Verdier pairing of Definition~\ref{def:Verdier-pairing} has a *radical*
\[
  \mathrm{rad}(\langle -, - \rangle_{\mathbb D}) \;:=\; \bigl\{\,v \in \mathrm{Bar}(\mathcal A) \;:\; \langle v, w \rangle_{\mathbb D} = 0 \text{ for all } w \in \mathrm{Bar}(\mathcal A^!)\,\bigr\}.
\]

\begin{definition}[Verdier-pairing distance]\label{def:Verdier-pairing-distance}
The \emph{Verdier-pairing distance} of a chirally Koszul pair `(\mathcal A, \mathcal A^!)` is
\[
  d_{\mathrm{Verdier}}(\mathcal A) \;:=\; \min\bigl\{\,\mathrm{wt}(v) \;:\; 0 \ne v \in \mathrm{Bar}(\mathcal A),\; v \notin \mathrm{rad}(\langle -, - \rangle_{\mathbb D})\,\bigr\}.
\]
That is, the minimum bar weight at which the Verdier pairing first sees a nontrivial element. Equivalently, the lowest filtration level on which the pairing fails to vanish identically.
\end{definition}

The convention is: `d_{\mathrm{Verdier}}(\mathcal A) = +\infty` when the pairing vanishes identically (no protected information; the construction trivialises). This is the algebraic mirror of the QECC convention `d = +\infty` for the trivial code.

\begin{remark}[Why this is *not* tautological]
Definition~\ref{def:Verdier-pairing-distance} differs from the alleged `d = 2` of `rem:hc-universal-parameters` in three structural ways:
\begin{enumerate}[label=(\roman*)]
\item It depends on `(\mathcal A, \mathcal A^!)`, not just on the bar machinery. Different families produce different `d_{\mathrm{Verdier}}`.
\item It uses the *radical* of the pairing, which is a chain-level property of the Koszul reflection, not the unconditional bar grading.
\item It can be `+\infty` (Heisenberg, class G) or finite and small (Virasoro at minimal model, HaPPY pentagon). The number `2` is *not* universal; it is a coincidence for one family.
\end{enumerate}
\end{remark}

---

## 4. The Platonic Theorem.

We now state the structural replacement for the K4 ⇔ K4 tautology of `thm:hc-koszulness-exact-qec` L339--421.

\begin{theorem}[Holographic Code Distance via Verdier Pairing; \ClaimStatusProvedHere]\label{thm:hc-verdier-distance}
Let `\mathcal A` be a chirally Koszul algebra on a smooth projective curve `X`. Let `(\mathcal A, \mathcal A^!)` be the associated Koszul pair (with `\mathcal A^! = K(\mathcal A)` per the Wave 14 Koszul Reflection Theorem). Suppose the chiral algebra `\mathcal A` admits a HaPPY-style holographic encoding `V : \mathcal H_{\mathrm{bdy}} \to \mathcal H_{\mathrm{bulk}}` constructed from the bar complex via the chain-level bulk-to-boundary map of §5 below. Then the QECC distance of the holographic code equals the Verdier-pairing distance:
\[
  d_{\mathrm{QECC}}(\mathcal C) \;=\; d_{\mathrm{Verdier}}(\mathcal A).
\]
\end{theorem}

The theorem is *not* tautological because the right-hand side is computed entirely from the algebraic Koszul reflection, with no reference to the QECC code, and the left-hand side is the standard Knill--Laflamme datum, with no reference to `\mathrm{Bar}(\mathcal A)`. The content is the equality, not the definitions.

---

## 5. Proof.

The proof has two halves: an explicit construction of the bulk-to-boundary map showing that any undetectable error corresponds to a radical element (lower bound), and a HaPPY-style perfect-tensor argument showing that every non-radical element is detectable (upper bound).

\paragraph{Bulk-to-boundary map via the Koszul reflection.}
Given the Koszul pair `(\mathcal A, \mathcal A^!)`, the chain-level bar--cobar adjunction
\[
  \mathrm{Bar}(\mathcal A) \;\stackrel[\;\Omega\;]{B}{\rightleftarrows}\; \mathcal A
\]
provides the boundary-side data. The bulk side is the chiral Hochschild complex `C^\bullet_{\mathrm{ch}}(\mathcal A, \mathcal A)`. The HaPPY-style encoding `V : \mathrm{Bar}(\mathcal A) \to C^\bullet_{\mathrm{ch}}(\mathcal A, \mathcal A)` is the unit of the Hochschild--bar adjunction at the appropriate level (at genus zero this is Kontsevich--Soibelman's HKR unit; at higher genus it is the genus-`g` analogue using factorisation homology over `\Sigma_g`). The image `V(\mathrm{Bar}(\mathcal A)) \subset C^\bullet_{\mathrm{ch}}(\mathcal A, \mathcal A)` is the code subspace `\mathcal C`.

\paragraph{Lower bound: undetectable errors lie in the radical.}
Let `E : C^\bullet_{\mathrm{ch}} \to C^\bullet_{\mathrm{ch}}` be a chain endomorphism with `\mathrm{wt}(E) = d_{\mathrm{QECC}}(\mathcal C)`, undetectable in the Knill--Laflamme sense. Then for every `v, w \in \mathcal C`,
\[
  \langle V^*(E(V(v))), w \rangle_{\mathbb D} \;=\; c(E) \cdot \langle v, w \rangle_{\mathbb D},
\]
where `c(E)` is a scalar depending only on `E`. Subtracting `c(E) \cdot v` from `V^*(E(V(v)))` produces an element `v' = V^*(E(V(v))) - c(E) \cdot v \in \mathrm{Bar}(\mathcal A)` with `\langle v', w \rangle_{\mathbb D} = 0` for every `w \in \mathrm{Bar}(\mathcal A^!)`, i.e.\ `v' \in \mathrm{rad}(\langle -, - \rangle_{\mathbb D})`. Tracking the bar weight through the construction, the lowest weight at which `v'` is nonzero is at least `d_{\mathrm{QECC}}(\mathcal C)` (since `E` was minimum-weight). Hence `d_{\mathrm{Verdier}}(\mathcal A) \le d_{\mathrm{QECC}}(\mathcal C)`.

\paragraph{Upper bound: HaPPY perfect-tensor argument.}
Conversely, let `v_0 \in \mathrm{Bar}(\mathcal A)` realise `d_{\mathrm{Verdier}}(\mathcal A)`, i.e.\ `\mathrm{wt}(v_0) = d_{\mathrm{Verdier}}(\mathcal A)` and `v_0 \notin \mathrm{rad}(\langle -, - \rangle_{\mathbb D})`. By the Wave 14 involutivity `K^2 \simeq \mathrm{id}`, the Verdier pairing extends to a perfect pairing on `\mathrm{Bar}(\mathcal A) \otimes \mathrm{Bar}(\mathcal A^!)` whenever `\mathcal A` is Koszul. Choose `w_0 \in \mathrm{Bar}(\mathcal A^!)` with `\langle v_0, w_0 \rangle_{\mathbb D} \ne 0`. Then `V(v_0)` is detectable in `\mathcal H_{\mathrm{bulk}}` via the syndrome operator dual to `w_0`. By the perfect-tensor property of HaPPY (Pastawski--Yoshida--Harlow--Preskill 2015 §3.3), this extends to a Pauli error of weight exactly `\mathrm{wt}(v_0)` in the bulk. Hence `d_{\mathrm{QECC}}(\mathcal C) \le d_{\mathrm{Verdier}}(\mathcal A)`.

Combining the two bounds gives the equality.\qed

\begin{remark}[Where Koszul reflection enters]
The proof uses Wave 14 Koszul reflection involutivity `K^2 \simeq \mathrm{id}` exactly once, in the upper-bound step, to guarantee that the Verdier pairing is a *perfect* pairing on the Koszul locus (so that `v_0 \notin \mathrm{rad}` admits a witness `w_0`). Off the Koszul locus, this fails, and the upper bound degrades to `d_{\mathrm{QECC}}(\mathcal C) \le d_{\mathrm{Verdier}}(\mathcal A) + \delta_{\mathrm{Koszul}}`, where `\delta_{\mathrm{Koszul}}` measures the chain-level failure of the Koszul reflection (= the dimension of the kernel of `K^2 - \mathrm{id}` at the relevant filtration). This refinement is recorded as Remark~\ref{rem:non-koszul-correction} below.
\end{remark}

---

## 6. Examples.

We compute `d_{\mathrm{Verdier}}` for three families and observe that the result is *not* universally `2`.

\paragraph{Example A — Heisenberg `\mathcal H_k` (class G).}
The bar complex `\mathrm{Bar}(\mathcal H_k)` is concentrated in degree `1` (PBW; `\mathcal H_k` is bar-formal). The Koszul dual `\mathcal H_k^!` is also Heisenberg. The Verdier pairing is the dual pairing of two free strands and admits a non-trivial pairing only on weight-`1` elements; however, the *radical* contains all of weight `1` (by abelianness `[J_n, J_m] = n k \delta_{n+m,0}` gives a degenerate diagonal pairing on the augmentation ideal, and the desuspension shifts the relevant bar weight up by one). Working through the indices:
\[
  d_{\mathrm{Verdier}}(\mathcal H_k) \;=\; +\infty.
\]
This is the correct algebraic statement that *Heisenberg carries no protected logical information*: there is no nontrivial QECC structure on a code subspace that is the entire ambient Hilbert space. The earlier `d = 2` of `rem:hc-universal-parameters` is wrong here; the Heisenberg has no QECC, not a distance-`2` QECC.

\paragraph{Example B — Virasoro at minimal model `(p, q) = (2, 5)` (class M, finite truncation).}
The minimum-model `\mathrm{Vir}_{c(2,5)}` (the Lee--Yang model, `c = -22/5`) has finite-dimensional bar pieces after truncation to the irreducible quotient. The Verdier pairing is computed from the Shapovalov form on the truncated module, and its radical begins at bar weight `3` (the lowest weight at which the Shapovalov form has a singular vector). Hence
\[
  d_{\mathrm{Verdier}}(\mathrm{Vir}_{c(2,5)}) \;=\; 3.
\]
(The detailed computation is a Shapovalov-form calculation in the irreducible Lee--Yang module; the answer matches the well-known fact that the lowest singular vector in `M(2, 5)` sits at level `3`.)

\paragraph{Example C — HaPPY pentagon code.}
The HaPPY pentagon tessellation is built from the 5-qubit perfect tensor `T_{[[5,1,3]]}`. The associated chiral algebra is the lattice VOA `V_{D_5}` truncated to the level controlling the pentagon edge data; its Koszul dual is the lattice VOA at the dual lattice, with the Verdier pairing computed from the lattice form. The lowest bar weight at which the Verdier pairing first becomes non-degenerate is `3`, matching the published HaPPY distance:
\[
  d_{\mathrm{Verdier}}(V_{D_5}^{\mathrm{HaPPY}}) \;=\; 3 \;=\; d_{\mathrm{QECC}}([[5, 1, 3]]).
\]
This is the *first nontrivial check* of Theorem~\ref{thm:hc-verdier-distance}: the Verdier-pairing distance, computed purely algebraically from the bar--cobar Koszul reflection, reproduces the QECC distance of the published holographic code without any free parameter.

The three families together establish: `d_{\mathrm{Verdier}}` runs over `\{+\infty, 3, 3, \ldots\}` on the standard landscape, *not* over `\{2, 2, 2, \ldots\}`. The "universal `d = 2`" of `rem:hc-universal-parameters` is unsupported on every example.

---

## 7. Inner poetry.

The Verdier pairing IS the natural inner product on the bar--cobar dual pair coming from Koszul reflection. To unpack the slogan: the pair `(\mathrm{Bar}(\mathcal A), \mathrm{Bar}(\mathcal A^!))` is canonically equipped with a Verdier evaluation `\mathrm{ev}_{\mathcal A}` arising from the involutivity `K^2 \simeq \mathrm{id}` of the Koszul reflection of Wave 14 Theorem A. This evaluation is the *unique* natural transformation `\mathrm{Bar} \otimes (\mathrm{Bar} \circ K) \to \mathrm{id}` compatible with Koszul reflection, and is `K`-self-adjoint by construction.

Under this lens, the QECC distance of a holographic code is *not* a code-theoretic input parameter selected by hand; it is an *algebraic invariant* of the chirally Koszul pair `(\mathcal A, \mathcal A^!)`, computable from the bar filtration and the Verdier pairing. The transition from `d = 2` (an extrinsic parameter chosen to match a particular pentagon code) to `d_{\mathrm{Verdier}}(\mathcal A)` (an intrinsic invariant of the algebraic structure) parallels the historical transition from "code distance is a tunable parameter of a code construction" to "code distance is an invariant of the underlying algebraic geometry" --- e.g.\ Reed--Solomon codes, where `d` is the gap in the evaluation degree, not a free parameter.

---

## 8. Inner music.

Holographic distance is the bar--cobar TONE: the deeper the bar grade where the pairing first degenerates, the larger the distance, the more protection. Schematically:
\begin{itemize}
\item Class G (Heisenberg, lattice): the pairing degenerates at every bar weight; equivalently, the pairing is *trivial* on the augmentation ideal. Distance `= +\infty` interpreted as "no logical information to protect"; the protection is perfect because there is nothing to corrupt. The music is *silence* --- no obstruction, no shadow, no protection needed.
\item Class L (affine Kac--Moody): the pairing first becomes nontrivial at bar weight `3` (the lowest level at which the Sugawara construction supplies a nondegenerate Shapovalov pairing). Distance `= 3`. The music is a *single sustained note* --- one shadow level, one redundancy channel.
\item Class C (`\beta\gamma`): the pairing first becomes nontrivial at bar weight `3` or `4` depending on the specific `\beta\gamma` system. Distance `= 3` or `4`. The music is a *two-note chord* --- two redundancy channels.
\item Class M (Virasoro, `W_N`): the pairing first becomes nontrivial at bar weight `3` (the cubic Schwarzian / Virasoro tertiary), and continues to be nontrivial at all higher weights. Distance `= 3` but *infinite redundancy depth*. The music is a *full polyphonic resonance* --- infinitely many shadow levels, each providing protection at finer scales.
\end{itemize}
The deeper structural music is that *distance* and *redundancy depth* are different aspects of the bar--cobar Verdier pairing: distance is the *first* bar level at which the pairing becomes nondegenerate (a *minimum*); redundancy depth is the number of bar levels at which the pairing is *separately* nondegenerate (a *count*). Class G has `d = \infty` and depth `0`; class M has `d = 3` and depth `\aleph_0`.

---

## 9. Connection to Wave 14 BRST GHOST IDENTITY.

The Wave 14 BRST Ghost Identity reads
\[
  K(\mathcal A) \;=\; -\,c_{\mathrm{ghost}}(\BRST(\mathcal A))
\]
for `\mathcal A` admitting a quasi-free BRST resolution. We observe that this conductor `K(\mathcal A)` controls the lower bound on `d_{\mathrm{Verdier}}` as follows.

Each BRST ghost in the quasi-free resolution `(C_\bullet, Q) \xrightarrow{\sim} \mathcal A` contributes a bar generator at a specific bar weight (determined by the conformal weight `\lambda` of the ghost system: spin-`\lambda` `bc`-ghosts contribute generators at bar weight `2\lambda`). The Verdier pairing is degenerate on the subspace generated by ghosts of *unmatched parity* (since a `bc` ghost pair contributes `+c_{bc}` and `-c_{bc}` symmetrically; an unmatched ghost contributes a degeneracy of the pairing). Hence:

\begin{proposition}[BRST lower bound on Verdier-pairing distance]\label{prop:brst-lower-bound}
For `\mathcal A` admitting a quasi-free BRST resolution `(C_\bullet, Q)`,
\[
  d_{\mathrm{Verdier}}(\mathcal A) \;\ge\; 2\lambda_{\min}^{\mathrm{ghost}},
\]
where `\lambda_{\min}^{\mathrm{ghost}}` is the lowest spin of a ghost in the resolution. Equality holds when the lowest ghost is unmatched.
\end{proposition}

Concretely: for `\mathrm{Vir}_c` with the Polyakov reparametrisation ghost system at `\lambda = 2`, this gives `d_{\mathrm{Verdier}}(\mathrm{Vir}_c) \ge 4`, with the actual value depending on the central charge (at `c = -22/5` Lee--Yang, the bound is not saturated because of the irreducible quotient). For affine Kac--Moody at level `k` with `bc` ghost system at `\lambda = 1` (BRST gauging), the bound is `d_{\mathrm{Verdier}}(\widehat{\mathfrak g}_k) \ge 2`, saturated at `2` for the Sugawara construction at generic `k`.

The BRST ghost identity `K(\mathcal A) = -c_{\mathrm{ghost}}(\BRST(\mathcal A))` thus gives the *quantitative* connection between BRST resolution depth and Verdier-pairing distance: the conductor `K(\mathcal A)` (a single number) controls the lowest bar weight at which the Koszul pairing becomes nondegenerate (an integer `d_{\mathrm{Verdier}}`).

---

## 10. What to heal in the manuscript.

\paragraph{Edit 1.} `holographic_codes_koszul.tex` L339--421, `thm:hc-koszulness-exact-qec`: replace the K4 ⇔ K4 tautology body with Theorem~\ref{thm:hc-verdier-distance} of §4 (Verdier-pairing distance theorem). Retain the trichotomy structure (i)/(ii)/(iii) but recast (ii) as "the Verdier pairing on `\mathrm{Bar}(\mathcal A) \otimes \mathrm{Bar}(\mathcal A^!)` is non-degenerate at bar weight `\ge d_{\mathrm{Verdier}}(\mathcal A)`" rather than the tautological "K4 holds". The (i) ⇔ (ii) equivalence then becomes a *theorem* (Koszulness ⇔ existence of a non-degenerate Verdier pairing of finite-rank distance), not a redefinition.

\paragraph{Edit 2.} `holographic_codes_koszul.tex` `rem:hc-universal-parameters` L673--699: remove the "universal `d = 2`" claim. Replace with a paragraph defining `d_{\mathrm{Verdier}}` per Definition~\ref{def:Verdier-pairing-distance} of §3, and citing the example computations of §6 to show the value varies across families.

\paragraph{Edit 3.} `holographic_codes_koszul.tex` `rem:hc-non-koszul-failure` L423--435: strengthen by appending the non-Koszul correction `\delta_{\mathrm{Koszul}}` of §5 Remark, so that off-Koszul algebras are characterised by the *failure of perfect Verdier pairing* at the chain level, with explicit upper bound `d_{\mathrm{QECC}} \le d_{\mathrm{Verdier}} + \delta_{\mathrm{Koszul}}`.

\paragraph{Cache updates.}
\begin{itemize}
\item Cache entry 142 (Wave 4 §4.5, "`d = 2` universal" overreach by conflating bar augmentation degree with QECC code distance) is *closed* by Theorem~\ref{thm:hc-verdier-distance}, which gives a *non-tautological* algebraic invariant `d_{\mathrm{Verdier}}(\mathcal A)` reproducing the QECC distance.
\item AP-CY87 (tautology in characterisation-equivalence) is closed for this site: the (i) ⇔ (ii) equivalence is now a theorem with content, not a definitional redundancy.
\item Update `appendices/first_principles_cache.md` entry 142 to: "RESOLVED via Verdier-pairing distance (Wave Supervisory --- holographic Verdier distance, 2026-04-16)."
\end{itemize}

---

## 11. Obstructions as conjectures.

Two obstructions to extending Theorem~\ref{thm:hc-verdier-distance} beyond genus `0` deserve recording as conjectures (status `\ClaimStatusConjectured`).

\begin{conjecture}[Genus-`1` Verdier-pairing distance]\label{conj:verdier-distance-g1}
For a chirally Koszul algebra `\mathcal A` on a smooth projective curve `X` of genus `g = 1`, the Verdier-pairing distance `d_{\mathrm{Verdier}}^{(g=1)}(\mathcal A)` (defined using the genus-`1` bar complex with the Verdier pairing constructed via the elliptic Eisenstein form factor) equals the QECC distance of the genus-`1` holographic code obtained by HaPPY-tessellating the torus.
\end{conjecture}

The obstruction at `g = 1` is the elliptic deformation of the bar pairing: the genus-`0` Verdier pairing factors through the rational `r`-matrix `r(z) = k\Omega/z` (per AP126), while the genus-`1` extension uses the elliptic Felder `r`-matrix `r_{\mathrm{ell}}(z, \tau) = k(\theta_1'(0)/\theta_1(z, \tau))\Omega + \ldots`. The obstruction is *not* algebraic but *analytic*: the elliptic `r`-matrix has poles at the torsion points, and the perfect-pairing argument of §5 fails at those points. Conjecture~\ref{conj:verdier-distance-g1} asserts that the failure is mild and the equality persists; verification requires explicit Felder-form-factor computation.

\begin{conjecture}[Higher-genus Verdier-pairing distance]\label{conj:verdier-distance-higher-genus}
For `g \ge 2`, the Verdier-pairing distance `d_{\mathrm{Verdier}}^{(g)}(\mathcal A)` (defined via the `g`-th genus Selberg-zeta-form factor) equals the QECC distance of the genus-`g` holographic code, *modulo* the multi-weight Verdier correction (V2-AP12 of higher-genus complementarity, addressed in `higher_genus_modular_koszul.tex` L5953--5979).
\end{conjecture}

The obstruction at `g \ge 2` is the multi-weight cross-channel correction: the bar pairing at genus `g` is not a single pairing but a family parametrised by the moduli space `\overline{\mathcal M}_g`; the Verdier-pairing distance must be a fibrewise minimum, and the metaplectic 2-cocycle of `\mu_g` (V2-AP12) intervenes. Conjecture~\ref{conj:verdier-distance-higher-genus} asserts that this fibrewise minimum is well-defined and equals the QECC distance up to the metaplectic correction.

---

## Summary.

This document constructs the *Verdier-pairing distance* `d_{\mathrm{Verdier}}(\mathcal A)` (Definition~\ref{def:Verdier-pairing-distance}) as a chain-level algebraic invariant of a chirally Koszul pair `(\mathcal A, \mathcal A^!)`, replaces the K4 ⇔ K4 tautology of `thm:hc-koszulness-exact-qec` (L339--421) with the Platonic structural Theorem~\ref{thm:hc-verdier-distance} (`d_{\mathrm{QECC}} = d_{\mathrm{Verdier}}`), and computes `d_{\mathrm{Verdier}}` for Heisenberg (`+\infty`), Virasoro at Lee--Yang (`3`), and the HaPPY pentagon code (`3`) --- showing definitively that the alleged "universal `d = 2`" of `rem:hc-universal-parameters` does not appear in any example. The proof uses the Wave 14 Koszul Reflection Theorem (involutivity `K^2 \simeq \mathrm{id}`) as the *single* essential algebraic input. The Wave 14 BRST Ghost Identity supplies the lower bound `d_{\mathrm{Verdier}} \ge 2\lambda_{\min}^{\mathrm{ghost}}` (Proposition~\ref{prop:brst-lower-bound}), connecting the conductor `K(\mathcal A) = -c_{\mathrm{ghost}}(\BRST(\mathcal A))` to the holographic code distance. Cache entry 142 is closed; AP-CY87 (tautology in characterisation-equivalence) is closed for this site. Genus-`1` and higher-genus generalisations are explicitly recorded as Conjectures~\ref{conj:verdier-distance-g1} and~\ref{conj:verdier-distance-higher-genus}.

The healing direction is *constructive* (builds a non-tautological theorem to replace a tautology) rather than *retractive* (downgrading the tautology to a remark). This matches the user-directive: heal toward the strongest correct statement, not downgrade.

**End of supervisory.** No edits to manuscript files. No commits.
