# Worker A3: Theorem B / Bar-Cobar / Positselski Edge

Audit target: `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex` plus `universal_anomaly_voa_explicit_supplement.tex`, against the Vol I Theorem B core.

## 1. Exact Proven Theorem B Core In Vol I

The proved Vol I core is not "one cyclic-Massey class kills the full bar-cobar tower." It is the following narrower package.

1. Strict lane. For a complete augmented chiral algebra `A` on a smooth curve, with conilpotent or augmentation-complete bar coalgebra and the required finiteness hypotheses, the counit
   ```tex
   \psi:\Omega(\bar B(A))\longrightarrow A
   ```
   is a quasi-isomorphism of chiral algebras on the Koszul locus. At genus 0 this is the strict Koszul clause; at higher genus it requires the higher-genus Koszul locus/PBW hypotheses. Anchor: `chapters/theory/bar_cobar_adjunction_inversion.tex:1995`--`2106`.

2. Coderived lane. Off the strict Koszul lane, Vol I proves only a coderived/coacyclic comparison under filtered pro-conilpotent and finite-dimensional graded-piece hypotheses:
   ```tex
   \Omega_X\bar B_X(A)\to A
   ```
   is an isomorphism in `D^{co}` on that verified completed surface. No unrestricted ordinary quasi-isomorphism is asserted. Anchor: `chapters/theory/bar_cobar_adjunction_inversion.tex:2048`--`2066`, `2126`--`2135`.

3. Promotion back to ordinary chain-level inversion requires an independent collapse input, e.g. `\kappa(A)=0` or a class `G/L` collapse of the coderived bar-degree spectral sequence. Outside those collapse loci, ordinary quasi-isomorphism is not claimed. Anchor: `chapters/theory/bar_cobar_adjunction_inversion.tex:2080`--`2087`.

4. The Positselski comodule/contramodule comparison is conditional on the finite-type conilpotent CDG surface plus product/sum exactness. Reduction to ordinary complete modules over the dual algebra is only on flat finite-type loci. Anchor: `chapters/theory/bar_cobar_adjunction_inversion.tex:1477`--`1512`, `1538`--`1598`.

5. Concordance agrees: Theorem B is "strict quasi-isomorphism on the Koszul locus"; the K3 chiral-bialgebra strict locus is the admissible-Humbert complement; formal-wall strictness is only in a refined pro-ambient; raw direct-sum class-M chain inversion fails. Anchor: `chapters/connections/concordance.tex:41`--`72`.

6. The construction/resolution distinction is explicit: bar and cobar exist for every augmented chiral algebra, but the counit is a quasi-isomorphism only when the twisting morphism is Koszul; off-locus it persists only in a provisional coderived category, not the ordinary derived category. Anchor: `chapters/theory/chiral_koszul_pairs.tex:289`--`300`.

## 2. What The Standalone May Safely Import

The standalone may safely import Theorem B only in this form:

- If the curve-side algebra `A_C=A_X|_C` is already proved to lie in `Kosz(C)`, then `\Cobar_C^{ch}\Bar_C^{ch}(A_C)\to A_C` is a strict quasi-isomorphism.
- If `A_C` lies on the filtered pro-conilpotent completed Positselski surface with finite graded bar pieces, then the same counit is a coderived equivalence.
- If the cyclic-Massey class restricts to the first obstruction class, then vanishing of `[m_3,B^{(2)}]_X` can safely be used only to kill that first identified obstruction.
- The leap from first obstruction to all higher `obs_n` requires an independent Koszul/PBW/collapse proof or must be made part of the definition of the admissible locus. It is not a consequence of Positselski 2011 by itself as quoted in Vol I.

Thus the safe edge is:

```tex
[m_3,B^{(2)}]_X=0
\quad\Longrightarrow\quad
\mathrm{obs}_2(A_C)=0
```

after a stated restriction/identification hypothesis. The unsafe edge is:

```tex
[m_3,B^{(2)}]_X=0
\quad\Longrightarrow\quad
\mathrm{obs}_n(A_C)=0\quad\text{for all }n\ge 2.
```

## 3. Fatal Findings

### CRITICAL: `thm:main` proves Theorem B from one class by an unsupported recursion

Anchor: `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:701`, `710`.

The proof asserts:
```tex
[m_3,B^{(2)}]_X=0 \Longrightarrow \mathrm{obs}_n(\Bar--\Cobar)=0
\quad\text{for all }n\ge2
```
and then says higher `obs_n` are polynomials in `obs_2` via "Positselski recursion." Vol I's Theorem B does not contain this recursion. It assumes Koszulness/completion/collapse hypotheses and then proves the counit comparison. Positselski supplies the comparison on the correct CDG/coderived surface; it does not collapse all higher obstruction classes from one secondary cyclic-Massey class in the form used here.

Repair: make Koszul-admissibility or completed-coderived membership an independent hypothesis for (ii), and demote the anomaly class to the first obstruction unless a separate theorem proves the full tower collapse.

### CRITICAL: `thm:climax-I` blurs the Koszul stratum with anomaly vanishing

Anchor: `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:242`--`251`.

The theorem is safe if "lies in the Koszul stratum" means the Vol I Koszul locus: the locus where the bar-cobar counit is known to be a quasi-isomorphism, or the completed Positselski surface. The following paragraph then says the homotopy exists precisely when Malcev obstruction classes vanish through all `n`, and that this holds on `\cU^{adm}`. This is circular unless `\cU^{adm}` is defined independently by PBW/Koszul/coderived collapse. It is false if `\cU^{adm}` is defined only by `[m_3,B^{(2)}]=0`.

### SERIOUS: the formality strictness corollary has the same "second obstruction kills all" gap

Anchor: `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:544`--`550`.

The statement that vanishing of the second Taylor coefficient lifts an `L_\infty` quasi-isomorphism to a strict `E_3`-algebra isomorphism, because higher obstructions are iterated Massey brackets of the second, is not licensed by the Vol I Theorem B surface. This is the same failure mode in operadic-formality language.

### SERIOUS: the Malcev section proves at most a weight-3 obstruction

Anchor: `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:626`--`650`.

The asserted identification
```tex
\mu_3 \equiv [m_3,B^{(2)}]_X
```
concerns a weight-3/secondary Arnold-Massey class. Even if correct, it identifies one obstruction. It does not prove all higher Malcev central extensions exist, nor all bar-cobar obstruction classes vanish. The subsequent use in the quintic corollary to negate all four climaxes, including Theorem B, overuses the result. Anchor: `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:783`--`789`.

### SERIOUS: the VOA supplement overstates explicit `V_1(sl_2)` bar-cobar proof

Anchor: `standalones/universal_anomaly_voa_explicit_supplement.tex:434`--`468`.

The supplement says Positselski applied to `\hat{\mathfrak{sl}}_2` at level one gives the bar cohomology, the obstruction tower collapses at `n=2` by Jacobi, the counit is a quasi-isomorphism, and `[m_3,B^{(2)}]` vanishes because `End(V_1(sl_2))` is strictly associative. The Vol I core does prove affine/Kac-Moody Koszul dual statements, with explicit low-degree computations for `sl_2`, but strict associativity of an endomorphism dg algebra is not the same as vanishing of transferred chiral `A_\infty`/bar obstruction classes. The example is usable as an illustrative low-degree/Koszul-locus witness, not as an independent proof of the full Theorem B edge.

### MODERATE: "equal as objects of `Pr^L_k`" is stronger than the imported Theorem B

Anchor: `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:685`--`695`.

Theorem B imports an equivalence in the curve-side coderived chiral category, subject to Koszul/completed hypotheses. It does not by itself identify this equivalence with the global anomaly class, a K3 bialgebra construction, and a trace identity as a single object of `Pr^L_k`. That equality may be a programme theorem, but not a consequence of Theorem B.

## 4. Repaired Edge Statement As TeX

Replace the edge `(i)=> (ii)` by a conditional theorem separating the first obstruction from the full Koszul/completed hypothesis:

```tex
\begin{theorem}[Bar--cobar edge on the verified Positselski surface]
\label{thm:main-barcobar-edge-repaired}
Let $X,C,\Sigma_2$ be as in Theorem~\ref{thm:main}, and put
$A_C=A_X|_C$. Assume:
\begin{enumerate}[label=\textup{(B\arabic*)}]
\item $A_C$ is a complete augmented chiral algebra whose chiral bar
coalgebra is conilpotent, or augmentation-complete with finite
graded bar pieces.
\item Either $A_C\in\operatorname{Kosz}(C)$, or
$\bar B_C^{\mathrm{ch}}(A_C)$ lies in the filtered
pro-conilpotent completed Positselski surface on which the
factorization counit is a coderived equivalence.
\item The restricted cyclic-Massey class is identified with the first
bar--cobar obstruction:
\[
  \operatorname{res}_C[m_3,B^{(2)}]_X=\mathrm{obs}_2(A_C).
\]
\end{enumerate}
Then the bar--cobar counit
\[
  \epsilon_C:\Omega_C^{\mathrm{ch}}\bar B_C^{\mathrm{ch}}(A_C)
  \longrightarrow A_C
\]
is a quasi-isomorphism on the strict Koszul branch of \textup{(B2)}
and an isomorphism in $D^{\mathrm{co}}_{\mathrm{ch}}(C)$ on the
completed Positselski branch of \textup{(B2)}. If
$[m_3,B^{(2)}]_X=0$, then \textup{(B3)} gives only
$\mathrm{obs}_2(A_C)=0$; the vanishing of
$\mathrm{obs}_n(A_C)$ for $n\ge3$ is an additional Koszul/PBW/collapse
hypothesis, not a formal consequence of the order-two class.
\end{theorem}
```

The corresponding proof edge should read:

```tex
\textup{(i)}\Rightarrow\textup{(ii)}:
\quad
[m_3,B^{(2)}]_X=0
\Longrightarrow
\mathrm{obs}_2(A_C)=0;
\quad
\text{Theorem B applies after the independent hypothesis }
A_C\in\operatorname{Kosz}(C)
\text{ or the completed Positselski condition.}
```

## 5. Examples: Proved Versus Illustrative

Honestly proved / safe to use:

- `\mathcal H_1` / `\mathcal H_k` as a Koszul-locus witness. Vol I computes the Heisenberg bar coalgebra and records bar-cobar inversion for Heisenberg; the rank-one standalone calculation is consistent with this. Anchors: `chapters/frame/heisenberg_frame.tex:33`--`56`, `chapters/theory/fourier_seed.tex:352`--`387`, `chapters/theory/chiral_koszul_pairs.tex:1022`--`1045`, `standalones/universal_anomaly_voa_explicit_supplement.tex:323`--`371`.

- Affine `\widehat{\mathfrak{sl}}_{2,k}` at noncritical level as a Vol I Kac-Moody Koszul-dual example, hence a candidate Theorem B witness once placed on the Koszul locus. Anchors: `chapters/examples/kac_moody.tex:1116`--`1123`, `1688`--`1726`. Level one is noncritical.

Illustrative / not a standalone proof of the full edge:

- The `V_1(\mathfrak{sl}_2)` cyclic-anomaly hand computation. The symmetry-antisymmetry contraction is a useful low-degree check, but the supplement's leap from Jacobi/strict associativity to full tower collapse is not a proof. Anchors: `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:1119`--`1150`, `standalones/universal_anomaly_voa_explicit_supplement.tex:434`--`468`.

- The `K3\times E` five-strand example. It assumes the identification of `A_Y` with a Mukai-lattice vertex algebra and then tensors rank-one bar-cobar inversions. This is a witness after independent verification of the Koszul-admissible locus; it is not evidence that `[m_3,B^{(2)}]=0` alone forces Theorem B. Anchor: `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:1156`--`1172`.

- The generic quintic failure. Nonvanishing of the cyclic-Massey/Malcev weight-3 class obstructs the first/secondary lift. It does not by itself prove total failure of every higher bar-cobar/coderived surface. Anchor: `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:783`--`789`.

## 6. Files Changed

Only this report:

- `notes/universal_anomaly_attack_heal_20260424/A3_bar_cobar_positselski.md`

No target TeX file was edited.

## 7. Commands Run

- `sed -n '1,220p' repo-local instructions file`
- `sed -n '1,240p' .agents/skills/deep-beilinson-audit/SKILL.md`
- `rg -n` searches for `Theorem B`, `chiral Positselski`, `Positselski`, `bar-cobar`, `Koszul`, `coderived`, `Malcev`, `obs_n`, `Massey`, and related labels across `chapters/connections/concordance.tex`, `metadata/theorem_registry.md`, `archive/raeeznotes/raeeznotes100/red_team_summary.md`, the target standalone, the VOA supplement, and core theory/example chapters.
- `rg --files | rg 'universal_anomaly_attack_heal_20260424|universal_anomaly_four_climax|concordance|theorem_registry|red_team_summary|positselski|bar|cobar|koszul'`
- `nl -ba ... | sed -n ...` on the exact anchor ranges cited above in `bar_cobar_adjunction_inversion.tex`, `bar_cobar_adjunction_curved.tex`, `cobar_construction.tex`, `chiral_koszul_pairs.tex`, `concordance.tex`, `kac_moody.tex`, `heisenberg_frame.tex`, `fourier_seed.tex`, the target standalone, and the VOA supplement.
- `git status --short`
- `ls -ld notes notes/universal_anomaly_attack_heal_20260424`
- `test -e notes/universal_anomaly_attack_heal_20260424/A3_bar_cobar_positselski.md`
