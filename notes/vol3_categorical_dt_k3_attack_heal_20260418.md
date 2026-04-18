ABSORBED 2026-04-18

# Vol III Attack-Heal Artifact: K3 Categorical DT Claim

Target repo: `/Users/raeez/calabi-yau-quantum-groups`

Status in this session: read-only for the target repo. This artifact records the converged heal as exact replacement text and cache proposals.

## Convergence

Round 1:
- `H_{\mathrm{Muk}} = \Phi_2(D^b(\Coh(K3)))` survives. It is already proved in Vol III at `thm:phi-k3-explicit`.
- `D^b(B_n(H_{\mathrm{Muk}})) \simeq D^b(\Hilb^n(K3))` fails as a proved theorem surface.
- The local notation layer does not define a categorical `B_n(H_{\mathrm{Muk}})`. In Vol III, `B_n` is used for braid-group structure on the `E_2` bar, not a geometric moduli category.

Round 2:
- Scope correction: `\Hilb^n(K3)` has complex dimension `2n`; it is a holomorphic symplectic fourfold only when `n = 2`.
- Mukai-vector correction: `\Hilb^n(K3)` is the moduli of ideal sheaves with Mukai vector `(1,0,1-n)`, so the manuscript's `rank-0` language is false as stated.
- Eta correction: `\eta(q)^{-24} = q^{-1}\prod_{m \ge 1}(1-q^m)^{-24}`. Bare equality with the product forgets the standard vacuum shift.

Round 3:
- Göttsche plus Nakajima/Grojnowski gives a character/cohomology bridge.
- Derived McKay gives `D^b_{S_n}(K3^n) \simeq D^b(\Hilb^n(K3))`.
- Categorical Heisenberg / toroidal actions and stable-envelope `R`-matrices give evidence on the geometric side.
- No source in the manuscript or in the standard literature constructs the missing bar-side categorical lift together with a functor to `D^b_{S_n}(K3^n)`.

Converged classification:
- Root claim (a): `PROVED HERE`.
- Root claim (b): `UNDEFINED AS STATED`; must be replaced by a categorical-lift placeholder.
- Root claim (c): `TRUE AFTER SCOPE CORRECTION`.
- Root claim (d): `TRUE ONLY AT CHARACTER / COHOMOLOGY LEVEL`.
- Final status of the target equivalence: `CONJECTURAL`, with explicit obstructions.

## Exact Manuscript Heal

### 1. Replace the subsection opener and proposition block in `chapters/theory/cy_to_chiral.tex`

Replace the block at lines 3536-3568 with the following:

```tex
The numerical DT invariants $\Omega(\gamma)$ are recovered as bar-complex Euler characteristics at the decategorified level.  For K3 this recovery is clean because the $d=2$ output is the free Mukai Heisenberg, so the Fock-space shadow is explicit.  The genuinely categorical statement is subtler: the literature gives the Fock/cohomology identification on $\bigoplus_{n \ge 0} H^\bullet(\Hilb^n(S),\Q)$ and the separate derived McKay equivalence
\[
  D^b_{S_n}(S^n) \xrightarrow{\sim} D^b(S^{[n]}),
\]
but it does not construct a bar-side category whose derived category is already known to be equivalent to $D^b(S^{[n]})$.  We therefore separate the proved character/cohomology bridge from the conjectural categorical lift.

\begin{proposition}[K3 Hilbert-scheme Fock bridge; \ClaimStatusProvedElsewhere]
\label{prop:mukai-hilbert-fock-bridge}
Let $S$ be a smooth projective K3 surface over $\C$, and let
\[
  H_{\mathrm{Muk}} \;:=\; \Phi\bigl(D^b(\Coh(S))\bigr)
\]
be the Mukai Heisenberg of Theorem~\textup{\ref{thm:phi-k3-explicit}}.  Then:
\begin{enumerate}[label=\textup{(\roman*)}]
  \item The graded vector space $\bigoplus_{n \ge 0} H^\bullet(S^{[n]}, \Q)$ carries the Fock representation of the rank-$24$ Heisenberg algebra attached to $H^\bullet(S,\Q)$ with the Mukai pairing.
  \item The Euler-characteristic generating function is
  \[
    \sum_{n \ge 0} \chi(S^{[n]})\, q^n \;=\; \prod_{m \ge 1} (1-q^m)^{-24}.
  \]
  Equivalently,
  \[
    \eta(q)^{-24} \;=\; q^{-1}\prod_{m \ge 1}(1-q^m)^{-24}.
  \]
  \item For every $n \ge 1$, the Hilbert scheme $S^{[n]} = \Hilb^n(S)$ is a smooth irreducible holomorphic symplectic variety of complex dimension $2n$.
\end{enumerate}
\end{proposition}

\begin{proof}
Part~\textup{(i)} is the Nakajima--Grojnowski Heisenberg action on Hilbert schemes of points on a smooth surface: the correspondences on nested Hilbert schemes identify $\bigoplus_{n \ge 0} H^\bullet(S^{[n]},\Q)$ with the vacuum Fock representation of the Heisenberg algebra on $H^\bullet(S,\Q)$.  Part~\textup{(ii)} is G\"ottsche's product formula for Euler characteristics of Hilbert schemes of points on a smooth projective surface; for a K3 surface one has $\chi(S)=24$, giving the displayed product.  Part~\textup{(iii)} combines Fogarty's smoothness of $S^{[n]}$ for a smooth surface with Beauville's holomorphic symplectic form on the K3 Hilbert scheme.  In particular, the fourfold statement applies only when $n=2$; in general the complex dimension is $2n$.
\end{proof}

\begin{conjecture}[Categorical DT lift of the Mukai Heisenberg Fock sector; \ClaimStatusConjectured]
\label{conj:categorical-dt-k3-fock-lift}
Let $S$ be a smooth projective K3 surface over $\C$, let $H_{\mathrm{Muk}}=\Phi(D^b(\Coh(S)))$, and fix $n \ge 0$.  Write $\mathscr{F}_n(H_{\mathrm{Muk}})$ for the charge-$n$ Fock sector of the Mukai Heisenberg.  By the symbol
\[
  \mathscr{B}_n(H_{\mathrm{Muk}})
\]
in this subsection we mean a \emph{categorical lift} of $\mathscr{F}_n(H_{\mathrm{Muk}})$: a triangulated or dg category whose Grothendieck group recovers $\mathscr{F}_n(H_{\mathrm{Muk}})$ and whose creation/annihilation functors categorify the Heisenberg operators.

If such a lift is constructed together with a functor
\[
  G_n \colon D^b(\mathscr{B}_n(H_{\mathrm{Muk}})) \longrightarrow D^b_{S_n}(S^n)
\]
intertwining the Heisenberg operators with the standard nested-Hilbert-scheme correspondences, then composition with the derived McKay equivalence
\[
  \Psi_n \colon D^b_{S_n}(S^n) \xrightarrow{\sim} D^b(S^{[n]})
\]
yields an equivalence
\[
  D^b(\mathscr{B}_n(H_{\mathrm{Muk}})) \xrightarrow{\sim} D^b(S^{[n]}).
\]

Equivalently: the slogan
\[
  D^b(B_n(H_{\mathrm{Muk}})) \simeq D^b(\Hilb^n(K3))
\]
is mathematically defensible only after replacing the undefined symbol $B_n(H_{\mathrm{Muk}})$ by a categorical lift $\mathscr{B}_n(H_{\mathrm{Muk}})$ and naming the functor $G_n$.
\end{conjecture}

\begin{proof}
There is presently no proof because the category $\mathscr{B}_n(H_{\mathrm{Muk}})$ and the functor $G_n$ have not been constructed in this volume.  The proved inputs are separate: Theorem~\textup{\ref{thm:phi-k3-explicit}} constructs $H_{\mathrm{Muk}}$; Proposition~\textup{\ref{prop:mukai-hilbert-fock-bridge}} gives the Fock/cohomology identification and the Euler-characteristic product; derived McKay identifies $D^b_{S_n}(S^n)$ with $D^b(S^{[n]})$.  None of these steps, alone or in combination, produces a bar-side categorical lift or a functor from it to the derived McKay model.  Hence the categorical equivalence is conjectural.
\end{proof}
```

### 2. Replace the abstract / overview bullets

#### `main.tex`

Replace lines 565-566 with:

```tex
(9)~\emph{Categorical DT on K3}:
the Mukai-Heisenberg Fock/cohomology bridge is proved,
while the lift
$D^b(\mathscr{B}_n(H_{\mathrm{Muk}})) \simeq D^b(\mathrm{Hilb}^n(K3))$
is conjectural pending construction of the categorical lift
$\mathscr{B}_n(H_{\mathrm{Muk}})$ and a functor to the derived
McKay model.
```

#### `chapters/theory/introduction.tex`

Replace lines 1102-1104 with:

```tex
 \item Categorical DT on K3:
  the Fock/cohomology identification
  $\bigoplus_{n \ge 0} H^\bullet(\Hilb^n(K3),\Q)
   \cong \mathrm{Fock}(H_{\mathrm{Muk}})$
  is proved \textup{(}Proposition~\ref{prop:mukai-hilbert-fock-bridge}\textup{)},
  while the categorical lift
  $D^b(\mathscr{B}_n(H_{\mathrm{Muk}})) \simeq D^b(\mathrm{Hilb}^n(K3))$
  remains conjectural \textup{(}Conjecture~\ref{conj:categorical-dt-k3-fock-lift}\textup{)}.
```

#### `chapters/frame/preface.tex`

Replace lines 1589-1591 with:

```tex
Categorical DT on K3 splits into a proved and a conjectural piece:
the Mukai-Heisenberg Fock/cohomology bridge is proved, while the
categorical lift
$D^b(\mathscr{B}_n(H_{\mathrm{Muk}})) \simeq
D^b(\mathrm{Hilb}^n(K3))$
is conjectural pending construction of the bar-side category and
its functor to the derived McKay model.
```

### 3. Compute-layer heal

#### `compute/lib/categorical_dt_bar.py`

Replace the docstring and return metadata of `categorical_dt_k3_rank0` with:

```python
def categorical_dt_k3_rank0(N: int = 10) -> CategoricalDTModuli:
    r"""Target categorical DT moduli for K3.

    PROVED INPUTS:
    (1) dim Hilb^n(K3) = 2n.
    (2) chi(Hilb^n(K3)) = p_24(n).
    (3) Hilb^n(K3) is holomorphic symplectic.
    (4) The Mukai Heisenberg acts on the cohomology/Fock side.

    CONJECTURAL STEP:
        a bar-side categorical lift of the charge-n Fock sector
        together with an explicit functor to the derived McKay model.

    Therefore the intended categorical target is D^b(Hilb^n(K3)),
    but the equivalence from a manuscript-defined bar category is not
    proved here.
    """
    ...
    return CategoricalDTModuli(
        name="K3 (target categorical lift)",
        ...
        status="CONJECTURAL",
        dependencies=[
            "CY-A_2 (d=2 proved)",
            "Nakajima-Grojnowski Heisenberg action",
            "Goettsche formula",
            "Derived McKay for Hilbert schemes of points on surfaces",
        ],
    )
```

Also delete the false lines

```python
    IDENTIFICATION: B_n(H_Muk) ~ Hilb^n(K3) as varieties.
```

and

```python
    STATUS: PROVED at d=2 (CY-A_2 proved).
```

#### `compute/tests/test_categorical_dt_bar.py`

Change the categorical K3 tests to the following scope:

```python
    def test_k3_target_mentions_hilb(self):
        """K3: the geometric target of the conjectural lift is Hilb^n(K3)."""
        cat = categorical_dt_k3_rank0(6)
        assert cat.moduli_identification[1] == "D^b(Hilb^1(K3))"
        assert cat.moduli_identification[3] == "D^b(Hilb^3(K3))"

    def test_k3_moduli_dimension(self):
        """K3: dim(Hilb^n(K3)) = 2n (complex dimension)."""
        ...

    def test_k3_status_conjectural(self):
        """The bar-side categorical lift is conjectural."""
        cat = categorical_dt_k3_rank0(3)
        assert cat.status == "CONJECTURAL"
```

Delete the present assertions that the equivalence is already `PROVED`.

## Precise Interpretation of `B_n`

Use this wording in the manuscript or notes:

```tex
In the categorical DT subsection, the bare notation $B_n(H_{\mathrm{Muk}})$ is retired.  It collides with three different structures already present in the programme: the degree-$n$ piece of the ordered bar coalgebra, the braid-group-$B_n$ action on the $E_2$ bar, and the charge-$n$ Fock sector of the Mukai Heisenberg.  The only interpretation compatible with the Hilbert-scheme target is the third one, and even there only after replacing the bare symbol by a categorical lift $\mathscr{B}_n(H_{\mathrm{Muk}})$ whose Grothendieck group recovers the charge-$n$ Fock sector.
```

## Explicit Obstruction List

These belong either in the proof of the conjecture or in a follow-up remark.

```tex
\begin{remark}[Why the categorical lift is still open]
\label{rem:categorical-dt-k3-obstructions}
The obstruction is not on the Hilbert-scheme side.  The missing pieces are:
\begin{enumerate}[label=\textup{(\roman*)}]
  \item a definition of the bar-side category $\mathscr{B}_n(H_{\mathrm{Muk}})$;
  \item a functor $G_n \colon D^b(\mathscr{B}_n(H_{\mathrm{Muk}})) \to D^b_{S_n}(S^n)$;
  \item compatibility of $G_n$ with the Nakajima creation/annihilation correspondences;
  \item a proof that the ordered/barred structure survives passage from the free Heisenberg algebra to the categorical lift.
\end{enumerate}
G\"ottsche's product, Nakajima--Grojnowski's Heisenberg action, Maulik--Okounkov stable envelopes, and derived McKay all support the target, but none of them constructs the missing functor.
\end{remark}
```

## Cache Entry Proposals

These were not installed in the target repo because the target repo was read-only in this session.

### AP-CY101. Character/Fock agreement promoted to categorical equivalence

- Wrong claim template: `G\"ottsche + Nakajima/Grojnowski => D^b(B_n(H_{\mathrm{Muk}})) \simeq D^b(\Hilb^n(K3))`.
- Ghost theorem: character identities and Heisenberg actions live on cohomology, K-theory, or Fock spaces. A categorical equivalence needs a defined categorical lift and an explicit functor, typically through the derived McKay model `D^b_{S_n}(S^n)`.
- Counter-template: split the statement into a proved Fock/cohomology bridge and a conjectural categorical lift with a named obstruction list.

### B95. `\Hilb^n(K3)` rank/dimension discipline

- Wrong formula template: `\Hilb^n(K3)` is a rank-0 moduli space or a holomorphic symplectic fourfold for all `n`.
- Correct form: `\Hilb^n(K3) = M_H(1,0,1-n)` is the rank-1 ideal-sheaf moduli space, and its complex dimension is `2n` (`4` only when `n=2`).

### FM261. Test suite hard-codes theorem status from the target label

- Wrong pattern: a compute test marks a theorem `PROVED` because the intended geometric target is known, while the functor or equivalence under test is still unconstructed.
- Counter-template: tests may certify dimensions, Euler characteristics, Heisenberg actions, and target labels; theorem status remains `CONJECTURAL` until the categorical lift and its functor are implemented.

## Minimal Bibliography Additions If Desired

The current Vol III bibliography already has `Gottsche1990`, `BridgelandKingReid2001`, and `PTVV2013`.  To support the healed statement directly, add standard references for:

- Nakajima/Grojnowski Heisenberg action on Hilbert schemes of points on surfaces.
- A surface-level derived McKay reference phrased as
  `D^b_{S_n}(S^n) \simeq D^b(S^{[n]})`.

No change is needed to `thm:phi-k3-explicit`; it already supplies the proved Mukai-Heisenberg input.
