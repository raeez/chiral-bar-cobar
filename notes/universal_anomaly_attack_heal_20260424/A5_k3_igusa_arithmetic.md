# A5 K3 / Igusa / Mukai / Bruinier / VOA / arithmetic report

Scope: Vol I standalone `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex` and its K3/Igusa inputs. No target TeX files were edited by this worker.

## 1. Claims that survive

- The Mukai lattice signature input survives: for a K3 surface, the even Mukai lattice has signature `(4,20)`, hence `c_+(Muk(S))=4`.
- The formula `K=2 c_+(Muk(S))=8` survives only as the Vol III conductor / monodromy normalization. It is not a BKM weight, not the full lattice-VOA central charge, and not a direct consequence of Bruinier Proposition 5.1 alone.
- `\hbar^2=-1/8` survives only paired with that normalization, i.e. as the imposed conductor identity `\hbar^2 K=-1` with `K=8`. The local trace/Todd/Serre-duality derivation in the standalone does not prove it.
- The primitive Borcherds denominator side is `\Delta_5` of weight `5`; the scalar Igusa/DVV/DT partition side is `\Phi_{10}^{-1}=\Delta_5^{-2}` up to the standard sign and normalization. Vol III keeps these distinct.
- The Vol III object `H_{\Delta_5}` survives as an architecturally pinned frontier / conditional Hall-Drinfeld-double target. The theorem-grade content locally available is the denominator / positive-root target and the Oberdieck-Pandharipande reduced DT character, not a fully constructed canonical non-abelian chiral bialgebra.
- The Kunneth additivity formula for the Atiyah class survives in the corrected form
  `at_{S\times E}=pi_S^* at_S + pi_E^* at_E = pi_S^* at_S`, since `at_E=0`.

## 2. Fatal findings with anchors

1. `H^3(K3\times E,\Omega^3)=0` is false.
   Anchor: `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:797`.
   Correction:
   `\Omega^3_{S\times E}\cong \Omega^2_S\boxtimes\Omega^1_E\cong \mathcal O_{S\times E}`, hence
   `H^3(S\times E,\Omega^3)\cong H^2(S,\mathcal O_S)\otimes H^1(E,\mathcal O_E)\cong \C`.

2. `at=0` for `K3\times E` is false and internally contradicted.
   Anchors: abstract/intro overclaim at `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:98`, `:116`; corrected partial statement at `:153`, `:795-807`.
   Correct statement: `at_E=0`, `at_S\ne0`, and `at_{S\times E}=pi_S^*at_S`. The trace square detects `c_2(T_S)` and is nonzero on K3.

3. The obstruction-killing Hodge argument is invalid.
   Anchors: `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:797-821`, `:1072-1093`, `:1156-1168`.
   Actual Kunneth target:
   ```
   H^2(S\times E,\Omega^1_{S\times E})
   \cong H^1(S,\Omega^1_S)\otimes H^1(E,\mathcal O_E)
      \oplus H^2(S,\mathcal O_S)\otimes H^0(E,\Omega^1_E),
   ```
   so `dim_C H^2(S\times E,\Omega^1)=20+1=21`. The nonzero `tr(at_S^2)` / `c_2(T_S)` component can land in the second summand. The vanishing of `[m_3,B^{(2)}]` is not a Hodge-number consequence; it is an open chain-level cyclic-projection assertion.

4. The advertised admissible locus for the product witness is not established.
   Anchors: `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:126`, `:830-836`.
   The text simultaneously notes that `K3\times E` fails the strict Hodge hypothesis because `pi_1=Z^2` and `h^{1,0}=1`, but then claims the product has the full `21`-dimensional admissible locus minus Humbert divisors. If a Borcea-Voisin twist is applied, the moduli and Hodge numbers must be recomputed; the product `21` cannot simply be retained.

5. The Delta/Phi and character identifications are overclaimed.
   Anchors: main standalone `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:311-323`; VOA supplement `standalones/universal_anomaly_voa_explicit_supplement.tex:155-190`.
   Vol III and the adjacent Igusa file distinguish:
   `\Delta_5` = primitive BKM denominator, weight `5`;
   `\Phi_{10}=\Delta_5^2`;
   `Z_{red\,DT}(K3\times E)=-\Phi_{10}^{-1}=-\Delta_5^{-2}` up to normalization.
   Therefore `ch H_{\Delta_5}=1/\Phi_{10}` is not justified without an explicit square/double/pairing construction.

6. Bruinier Proposition 5.1 is misused.
   Anchors: main standalone `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:335-341`; VOA supplement `standalones/universal_anomaly_voa_explicit_supplement.tex:222-265`; Vol III local source `/Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3_chiral_bialgebra_platonic.tex:2823-2869`.
   The local Vol III specialization records a Heegner divisor / torsion Chern-class / monodromy formula. It does not by itself force `K=2c_+`; that requires the additional Mukai-signature and conductor-normalization argument.

7. The nine-discriminant arithmetic claim is unsupported and partly false as stated.
   Anchors: main standalone `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:950-962`; arithmetic supplement `standalones/universal_anomaly_local_global_arithmetic_supplement.tex:54-60`.
   The classical class-number-one imaginary quadratic discriminants are `{3,4,7,8,11,19,43,67,163}`. The manuscript substitutes `{15,20,24}` for `{43,67,163}` using an asserted Bruinier positivity cut and Chenevier determinant classification, but no local primary-source computation verifies this. The supplement's claim that the listed fields are exactly those whose unit group has order `>=2` is vacuous for imaginary quadratic orders, since all contain `\{\pm 1\}`; only `d=3,4` have exceptional extra units.

8. The VOA supplement contains an impossible lattice assertion.
   Anchor: `standalones/universal_anomaly_voa_explicit_supplement.tex:67-84`.
   There is no unique even unimodular lattice of signature `(2,1)`: even unimodular indefinite lattices require `p-q == 0 mod 8`. Replace by the actual rank-three Lorentzian primitive Cartan/Gram lattice used in the Gritsenko-Nikulin/Borcherds construction.

9. The derivation of `tr(1_A)=-1` is not valid.
   Anchor: `standalones/universal_anomaly_voa_explicit_supplement.tex:268-281`.
   Serre anti-self-duality would force a self-dual trace component to be zero, not `-1`. Also `\chi(\mathcal O_{K3\times E})=0`, so the Todd integral of a rank-`K` trivial object on the total space is `0`, not `-1`. The identity `\hbar^2K=-1` must be stated as a normalized conductor identity, not derived from this trace calculation.

## 3. Corrected witness theorem as TeX

```tex
\begin{theorem}[K3--Igusa witness, corrected scope]
Let \(Y=S\times E\), where \(S\) is a projective K3 surface and
\(E\) is an elliptic curve. Then
\[
T_Y=\pi_S^*T_S\oplus\pi_E^*T_E,\qquad
\at_Y=\pi_S^*\at_S+\pi_E^*\at_E=\pi_S^*\at_S,
\]
with \(\at_E=0\) and \(\at_S\ne0\). Moreover
\[
H^3(Y,\Omega_Y^3)\cong
H^2(S,\mathcal O_S)\otimes H^1(E,\mathcal O_E)\cong\mathbb C,
\]
and
\[
H^2(Y,\Omega_Y^1)\cong
H^1(S,\Omega_S^1)\otimes H^1(E,\mathcal O_E)
\oplus
H^2(S,\mathcal O_S)\otimes H^0(E,\Omega_E^1),
\]
so \(\dim_{\mathbb C}H^2(Y,\Omega_Y^1)=21\). Consequently the
vanishing of \([m_3,B^{(2)}]_Y\) is not implied by Hodge numbers. It is
equivalent here to the additional chain-level condition
\[
\operatorname{Cyc}_{3,\Omega_Y}\bigl(\pi_S^*(\at_S\cup\at_S)\bigr)=0
\quad\text{in }H^2(Y,\Omega_Y^1),
\]
or, equivalently, to the assertion that the cyclic-skew projection kills
the \(H^2(S,\mathcal O_S)\otimes H^0(E,\Omega_E^1)\) component detected
by \(\operatorname{tr}(\at_S^2)\).

On the independent automorphic side, the primitive Borcherds denominator
is \(\Delta_5\), of weight \(5\), while the scalar Igusa/DVV/DT partition
function is governed by
\[
\Phi_{10}=\Delta_5^2,\qquad Z_{\mathrm{red\,DT}}(K3\times E)
=-\Phi_{10}^{-1}=-\Delta_5^{-2}
\]
up to the standard normalization. The conductor value
\[
K=2c_+(\operatorname{Muk}(S))=8
\]
is distinct from \(\kappa_{\mathrm{BKM}}(\Delta_5)=5\).
\end{theorem}
```

## 4. Constants and formulas that must change

- Change `H^3(K3\times E,\Omega^3)=0` to `H^3(K3\times E,\Omega^3)\cong\C`.
- Change `at_{K3\times E}=0` to `at_{K3\times E}=pi_{K3}^*at_{K3}`, with `at_{K3}\ne0` and `at_E=0`.
- Replace the claimed vanishing of `H^2(K3\times E,\Omega^1)` by the two-summand Kunneth decomposition above and `dim=21`.
- Replace unconditional `[m_3,B^{(2)}]_{K3\times E}=0` by the explicit cyclic-projection condition.
- Replace unconditional `U_adm(K3\times E)=21`-dimensional moduli minus Humbert divisors by a conditional statement, and recompute after any Borcea-Voisin twist.
- Replace `ch H_{\Delta_5}=1/\Phi_{10}` by the split:
  `H_{\Delta_5}` / BKM denominator uses `\Delta_5`; scalar BPS/DT/DVV uses `\Phi_{10}^{-1}=\Delta_5^{-2}`.
- Replace "Bruinier Prop. 5.1 forces `K=2c_+`" by "Bruinier gives the Heegner divisor/Chern-class/monodromy input; `K=2c_+` uses Mukai signature plus the conductor-normalization theorem."
- Keep the constants distinct:
  `c_+(Muk(K3))=4`, `K=8`, `\hbar^2=-1/8`, `\kappa_{BKM}(\Delta_5)=5`, `wt(\Phi_{10})=10`, `\kappa_{ch}^{Heis}(K3\times E)=3`, `\kappa_{cat}(K3\times E)=0`, `\kappa_{fiber}=24`.
- Replace the nine-discriminant assertion with either the classical Heegner list `{3,4,7,8,11,19,43,67,163}` or a conditional statement requiring an explicit Bruinier coefficient/sign computation that justifies `{3,4,7,8,11,15,19,20,24}`.
- Replace `\Lambda^{2,1}_{II}` as a unique even unimodular lattice by the actual rank-three Lorentzian primitive Cartan lattice / Gram matrix.
- Replace the derivation of `tr(1_A)=-1` by a normalization hypothesis; the total-space Todd calculation gives `\chi(\mathcal O_{K3\times E})=0`.

## 5. Conditional or open obligations

- Prove or retract the chain-level assertion that the cyclic-skew projection kills the K3 `c_2` component in `H^2(K3\times E,\Omega^1)`.
- If the witness is meant to satisfy the strict Vol I Hodge hypothesis, specify the Borcea-Voisin or other quotient/twist and recompute `h^{p,q}`, `pi_1`, moduli dimension, and the obstruction target.
- Supply the precise Hall / hCS / protected-trace comparison that turns the conditional Vol III `H_{\Delta_5}` architecture into a theorem-grade chiral bialgebra construction.
- Provide the primary Bruinier / Chenevier computation for the non-classical discriminants `{15,20,24}`, or remove them from the arithmetic theorem.
- Define the exact normalization map between `\Delta_5^{-1}` as a denominator/character and `\Phi_{10}^{-1}` as scalar BPS/DT partition function.

## 6. Files changed

- `notes/universal_anomaly_attack_heal_20260424/A5_k3_igusa_arithmetic.md`

No target TeX files were edited by this worker. Scoped close-out status showed `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex` already modified in the worktree; it was left untouched.

## 7. Commands run

```bash
sed -n '1,220p' repo-local instructions file
sed -n '1,220p' /Users/raeez/chiral-bar-cobar/.agents/skills/deep-beilinson-audit/SKILL.md
sed -n '1,200p' /Users/raeez/chiral-bar-cobar/.agents/skills/multi-path-verify/SKILL.md
rg -n "K3|Igusa|Mukai|Bruinier|Borcherds|DVV|Delta_5|Phi_10|Heegner|Chenevier|H_\{?Delta|universal trace|K3\\times|K3 x E|hbar|c_\+|c_\\+|Omega\^3|at=0|Atiyah|Mukai" standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex chapters frame theory examples bibliography metadata notes appendices 2>/dev/null
sed -n '1,220p' chapters/connections/concordance.tex
sed -n '1,220p' metadata/theorem_registry.md
sed -n '1,220p' archive/raeeznotes/raeeznotes100/red_team_summary.md
nl -ba standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex | sed -n '80,380p'
ls -la notes/universal_anomaly_attack_heal_20260424 2>/dev/null
rg -n "A5|K3|Igusa|Mukai|Bruinier|Heegner|Chenevier|VOA|Delta_5|Phi_10" notes/universal_anomaly_attack_heal_20260424 2>/dev/null
rg -n -F "H^3(K3" standalones chapters notes /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups 2>/dev/null
rg -n -F "Omega^3" standalones chapters notes /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups 2>/dev/null
rg -n -F "K3 \\times E" standalones chapters notes /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups 2>/dev/null
rg -n -F "heegner" standalones chapters notes /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups /Users/raeez/igusa-cusp-form 2>/dev/null
rg -n -F "Chenevier" standalones chapters notes /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups /Users/raeez/igusa-cusp-form 2>/dev/null
nl -ba standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex | sed -n '760,840p'
nl -ba standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex | sed -n '930,1005p'
nl -ba standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex | sed -n '1050,1168p'
nl -ba standalones/universal_anomaly_voa_explicit_supplement.tex | sed -n '1,330p'
nl -ba standalones/universal_anomaly_local_global_arithmetic_supplement.tex | sed -n '1,95p'
ls -la /Users/raeez/chiral-bar-cobar-vol2 | sed -n '1,80p'
rg -n -F "Phi_{10}" /Users/raeez/chiral-bar-cobar-vol2 2>/dev/null
rg -n -F "DVV" /Users/raeez/chiral-bar-cobar-vol2 2>/dev/null
rg -n -F "Dijkgraaf" /Users/raeez/chiral-bar-cobar-vol2 2>/dev/null
rg -n -F "Igusa" /Users/raeez/chiral-bar-cobar-vol2 2>/dev/null
nl -ba /Users/raeez/calabi-yau-quantum-groups/main.tex | sed -n '760,875p'
nl -ba /Users/raeez/calabi-yau-quantum-groups/main.tex | sed -n '1380,1435p'
nl -ba /Users/raeez/calabi-yau-quantum-groups/README.md | sed -n '1,80p'
ls -la /Users/raeez/calabi-yau-quantum-groups/chapters/examples | sed -n '1,120p'
rg -n -F "thm:wkb-denominator-delta-5" /Users/raeez/calabi-yau-quantum-groups/chapters /Users/raeez/calabi-yau-quantum-groups/main.tex 2>/dev/null
rg -n -F "prop:k3xe-flagship-master-identity" /Users/raeez/calabi-yau-quantum-groups/chapters /Users/raeez/calabi-yau-quantum-groups/main.tex 2>/dev/null
rg -n -F "thm:bruinier-prop-5-1" /Users/raeez/calabi-yau-quantum-groups/chapters /Users/raeez/calabi-yau-quantum-groups/main.tex 2>/dev/null
nl -ba /Users/raeez/calabi-yau-quantum-groups/chapters/examples/cy_d_kappa_stratification.tex | sed -n '2648,2705p'
nl -ba /Users/raeez/calabi-yau-quantum-groups/chapters/examples/cy_d_kappa_stratification.tex | sed -n '4365,4405p'
nl -ba /Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3_chiral_bialgebra_platonic.tex | sed -n '2815,2898p'
nl -ba /Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3e_bkm_chapter.tex | sed -n '1,180p'
```
