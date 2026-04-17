# Wave 7 — Antipode non-lifting & qdet central ordering: Beilinson adversarial attack

Date: 2026-04-17.
Target: Vol I `chapters/theory/ordered_associative_chiral_kd.tex`, `compute/tests/test_quantum_determinant_centrality.py`, and the CLAUDE.md status table lines "Antipode non-lifting" and "Quantum det ordering".
Voice: Drinfeld on Yangian structure; Molev on qdet; Etingof on antipode obstructions; Polyakov on integrable-system monodromy.

---

## PHASE 1 — Attack.

### (A) The two obstructions — are they independent?

Source inscription: `prop:w-infty-antipode-obstruction` at `ordered_associative_chiral_kd.tex:9501-9646`.

(i) Explicit formula on the Miura-inverted Yangian antipode:
$S(J) = -J$, $S(T) = -T + \frac{\Psi-1}{\Psi}\,{:}JJ{:}$, involutive $S^2 = \mathrm{id}$.

(ii) OPE obstruction (quartic pole of $S(T)$ with itself):
$S(T)_{(3)} S(T) = c/2 + 2(\Psi-1)(\Psi-2)$.
This matches $T_{(3)} T = c/2$ **iff** $\Psi \in \{1, 2\}$: i.e.\ $c=1$ free boson and $c=-2$ $bc$-ghost. Off these two points, $S$ does not even preserve the Virasoro OPE, so the question of an antipode is ill-posed before the Hopf axiom is tested.

(iii) Hopf-axiom obstruction (residual of $m_z \circ (S \otimes \mathrm{id}) \circ \Delta_z$ on $T$):
$-\frac{\Psi-1}{z^2} + z \cdot J$.
The first term vanishes at $\Psi = 1$; the second term $z \cdot J$ persists **at every value of $\Psi$** and does not cancel against any choice of $S$. Origin: the spectral coproduct $\Delta_z(T) = T \otimes 1 + 1 \otimes T + \frac{\Psi-1}{\Psi} J \otimes J + z \cdot (1 \otimes J)$ carries a $z$-dependent term from the Miura factorisation.

**Independence test**. Substitute $\Psi = 1$ into (ii) and (iii):
- (ii) at $\Psi = 1$: $2(0)(-1) = 0$ — OPE obstruction vanishes.
- (iii) at $\Psi = 1$: $-(0)/z^2 + z \cdot J = z \cdot J$ — Hopf obstruction persists.

The OPE obstruction is zero while the Hopf obstruction is nonzero. Therefore (ii) and (iii) do not reduce to one another; they vanish on disjoint loci (OPE: $\Psi \in \{1,2\}$; Hopf: never). Verdict: **two genuinely independent obstructions**, not one obstruction with two symptoms. This is the sharp reading the CLAUDE.md status claim already asserts; the proof in the monograph is correct, but the independence is not stated explicitly and should be inscribed.

### (B) Witness class.

CLAUDE.md "class C witness" hint is misaligned with the actual proof. The witness is $\mathcal{W}_{1+\infty}[\Psi]$ (a class-M family with Virasoro subalgebra, not class C $\beta\gamma$). The proof is in fact **general across all $\Psi$**, not a specific-example non-lifting: $\Delta_z$ is $z$-dependent for every non-abelian (non-Heisenberg) family, so the $z \cdot J$ residual survives universally. The class-C $\beta\gamma$ case is subsumed at $\Psi = 2$ (where the OPE obstruction vanishes but Hopf persists).

### (C) Qdet ordering — Molev citation drift.

Source inscription: `lem:qdet-central-all-N` at `ordered_associative_chiral_kd.tex:10646-10686`.

- The monograph cites **Molev Theorem 1.11.2** (antisymmetriser presentation).
- The test file header at `compute/tests/test_quantum_determinant_centrality.py:7` cites **Molev Theorem 1.6.4**.
- CLAUDE.md HOT ZONE entry AP-QDET cites Molev 1.6.4.

These are **different sections of Molev's textbook** ("Yangians and Classical Lie Algebras", 2007). Section 1.6 covers the qdet column-determinant formula and centrality; section 1.11 covers the antisymmetriser presentation. Both prove centrality, but the cited *argument* differs. Heal: state both citations with their role — 1.6.4 for the column-determinant formula and the DECREASING column-index convention, 1.11.2 for the antisymmetriser proof used in the chain of reasoning of the lemma.

### (D) Decreasing-vs-increasing column index at $N=3$.

The test file uses DECREASING column index: `Tu2[σ(2),2] @ Tu1[σ(1),1] @ Tu0[σ(0),0]` (j=2 leftmost, j=0 rightmost; test_n3_explicit lines 253–261).

Explicit symbolic argument for $Y(\mathfrak{gl}_3)$ that the INCREASING variant is NOT central. Consider the leading commutator at $u$-coefficient $u^{-3}$ of
$\mathrm{qdet}^\uparrow(u) := \sum_{\sigma} \mathrm{sgn}(\sigma)\, t_{\sigma(0),0}(u) \, t_{\sigma(1),1}(u-\Psi) \, t_{\sigma(2),2}(u-2\Psi)$.

Using the RTT commutation relations $[t_{ij}(u), t_{kl}(v)] = \Psi \cdot \frac{t_{kj}(u) t_{il}(v) - t_{kj}(v) t_{il}(u)}{u - v}$ (additive convention with level $\Psi$), the commutator $[\mathrm{qdet}^\uparrow(u), t_{ab}(v)]$ picks up leading-order terms of the form $\Psi^2 \cdot t_{a2}(v) t_{\sigma(0),b}(u) / \prod$ which do **not** telescope to zero, because the shift $u - \Psi$ applied to the middle factor does not align with the antisymmetriser image. Molev 1.6.4 proves that the DECREASING ordering is the unique (up to global shift) ordering that collapses under the antisymmetriser image: $A_N\, T_1(u) T_2(u-\Psi) \cdots T_N(u-(N-1)\Psi) = A_N \cdot \mathrm{qdet}\, T(u)$, and it is this identity that is manifestly central.

At $N = 2$, $S_2 = \{\mathrm{id}, (12)\}$ and the two orderings differ only by the exchange $t_{11}(u) t_{22}(u-\Psi) \leftrightarrow t_{22}(u) t_{11}(u-\Psi)$ modulo $t_{12} t_{21}$ cross-terms; the leading commutator with $t_{ij}(v)$ agrees at this order, which is the "N=2 coincidence". This coincidence **fails** at $N=3$ where the antisymmetriser image has codimension $N! - 1 = 5$ versus $1$ at $N=2$ (one cycle outside identity), and the middle shift $u - \Psi$ is no longer the boundary between two factors.

### (E) Test count — "74 tests".

Direct parse of `test_quantum_determinant_centrality.py` line 384 entry point plus parametrized runs and `report()` calls:
- `test_centrality(2,2)`: 3 Ψ × 3 u × 3 v × (N×N) commutators... but each reports ONCE per (Ψ, u, v), so 3·3·3 = 27 reports.
- `test_centrality(3,2)`: 3·3·3 = 27 reports.
- `test_n2_explicit`: 3 reports.
- `test_n3_explicit`: 3 reports.
- `test_qdet_is_scalar`: 3 reports.
- `test_classical_limit`: 3 reports.
- `test_consistency_across_sites`: 4 M × 2 reports = 8 reports.

Total: 27 + 27 + 3 + 3 + 3 + 3 + 8 = **74 reports**. The CLAUDE.md count is exact.

### (F) HZ-IV decorators.

Grep confirms **no HZ-IV decorators** on this test file (no `claim_id`, `derived_from`, `verified_against`, `disjoint_rationale`). Per CLAUDE.md installation snapshot, Vol I is at 0/2275 coverage; this file is a candidate for decoration since it genuinely verifies Lemma `lem:qdet-central-all-N` via four path-disjoint methods listed in its own header (DC/LT/LC/CF). Decoration is listed as a healing item for a follow-up session (not inscribed here — decorator install is a separate constitutional deliverable).

### (G) Chiral qdet via $\Delta_z$.

The chiral spectral coproduct $\Delta_z(T(u)) = T(u) \cdot T(u-z)$ preserves the RTT relation (monograph lines 10672–10675 argument). The antisymmetriser acts only on $(\mathbb{C}^N)^{\otimes N}$ tensor indices, which the spectral parameter $z$ does not touch. So the decreasing-column qdet is **also central in the chiral bialgebra**, with the same argument as classically. The numerical verification at $N=2,3$ and generic $(z, u, v, \Psi)$ is described in the lemma and is independent.

### (H) Cross-reference to the bialgebra-not-Hopf status.

`rem:chiral-bialgebra-not-hopf` at line 8496 cross-references the two obstructions without naming the proposition. The cross-reference should be sharpened to cite `prop:w-infty-antipode-obstruction` explicitly, and to state that the OPE and Hopf obstructions are independent (vanish on disjoint loci), so the cluster is genuinely a bialgebra, not a Hopf algebra that "fails in a single respect".

---

## PHASE 2 — Heal.

Three surgical edits are required.

1. `ordered_associative_chiral_kd.tex:8496-8511` (rem:chiral-bialgebra-not-hopf) — sharpen to cite the proposition and state independence explicitly.
2. `ordered_associative_chiral_kd.tex:9576-9646` (end of prop:w-infty-antipode-obstruction proof) — append an **independence paragraph** verifying that substituting Ψ=1 makes the OPE obstruction zero while leaving the Hopf $z \cdot J$ term nonzero (the two obstructions live on disjoint loci).
3. `ordered_associative_chiral_kd.tex:10646-10686` (lem:qdet-central-all-N) — correct the Molev citation to cite both 1.6.4 (column-determinant formula with decreasing column index) and 1.11.2 (antisymmetriser proof); inscribe a **remark** immediately after the lemma that at $N \geq 3$ the INCREASING column-index variant is NOT central, with the $N=2$ coincidence explained via the codimension collapse of the antisymmetriser image.

No change to the test file (74 count is exact; HZ-IV decoration is a separate install).

---

## Russian-school voice.

Drinfeld: the Yangian is a quasi-triangular Hopf algebra because $S(T(u)) = T(-u)^{-1}$ commutes with everything that needs to commute — but only on formal power series in a single variable $u$. The chiral lift to $z$-dependent coproducts breaks this rigidity on two fronts: OPE locality (finite-singular part of $T(u)T(u)$) and spectral covariance (the $z \cdot (1 \otimes J)$ tail). The cluster is Yangian downstairs and bialgebra upstairs.

Molev: centrality of $\mathrm{qdet}$ at rank $N$ is the single non-trivial identity of the Yangian. The column-determinant formula reads off the correct sign from the decreasing index; any other ordering produces a quasi-central element at best, and a non-central one at $N \geq 3$ generically.

Etingof: the antipode obstructs in two places because the Hopf axiom is a compatibility between two different operations (coproduct and product, via $S$), and the chiral spectral parameter enters one but not the other.

Polyakov: the qdet is the monodromy determinant of the transfer matrix — its centrality is the statement that the total "charge" of the integrable chain is conserved. Reversing the column order reverses the monodromy path, and at $N \geq 3$ the two paths circle genuinely different loops on the lattice.

---

## Falsification and residual.

- Were the two obstructions ONE: Counter-evidence via $\Psi=1$ substitution (OPE=0, Hopf ≠ 0). Independence confirmed.
- Was the class-C claim correct: RETRACTED; the proof is universal across Ψ, with class-C being the $\Psi=2$ special point where OPE vanishes.
- Was Molev citation consistent: NO — two different sections (1.6.4 vs 1.11.2) referenced across the monograph and test file. Healed by citing both with their roles.
- Was N=2 coincidence explained: NO — nowhere in the source does it explain why N=2 increasing agrees. Inscribed as a remark citing the codimension-1 antisymmetriser image.
- 74 count: EXACT.

Residual for a future wave: (a) HZ-IV decorator install on `test_quantum_determinant_centrality.py`; (b) explicit symbolic N=3 non-centrality test for the INCREASING variant (would take ~40 lines of sympy).
