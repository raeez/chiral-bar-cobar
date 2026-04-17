# Wave 13 — Third TFAE: Seven faces of $r_{\CY}$ agree

**Date:** 2026-04-17
**Target:** `~/calabi-yau-quantum-groups/chapters/connections/cy_holographic_datum_master.tex`
**Label:** `thm:seven-faces-of-r-cy`
**Status on audit:** already inscribed (lines 856--950), Russian-school voice, six bidirections, transitive closure, six disjoint-source HZ-IV witnesses. No re-inscription required; audit verdict below.

## Theorem (as inscribed)

Let $A$ be a CY boundary chiral algebra in the image of the dimension-stratified correspondence $\{\Phi_d\}_{d \ge 1}$, evaluated on the Koszul locus. The seven presentations of the binary collision residue
$r_{\CY}(A) \in \End^{\mathrm{ch}}_A(2)[\![z^{-1}]\!]$
agree:

1. **Yangian coproduct twist** (Drinfeld 1985): $r_{\CY} = \Delta_u(x) - \Delta_u^{\mathrm{op}}(x)$ on Drinfeld primitives.
2. **Drinfeld-centre half-braiding**: $r_{\CY} = \sigma_V(\cZ(\Rep^{E_1}(A)))$.
3. **KZ monodromy** (Kohno 1987): $r_{\CY} = \lim_{z' \to z}\mathrm{Hol}_{\nabla_{\mathrm{KZ}}}$ on $X \times X \setminus \Delta$.
4. **BKM vertex-operator exchange** (Borcherds 1998): $V_\alpha V_\beta - (\alpha \leftrightarrow \beta)$ on the Mukai-lattice VOA.
5. **Maulik--Okounkov stable envelope** (MO 2012): $\mathrm{Stab}_\cC \circ \mathrm{Stab}_{\cC'}^{-1}$ on the Nakajima quiver variety of $\Phi^{-1}(A)$.
6. **$A_\infty$-coassociator**: $\delta^{(3)}$, the degree-3 term of $\Theta_A^{\le 3}$.
7. **Costello $5d$ hCS tree amplitude** (Costello 2017): $\mathrm{Tree}^{\mathrm{hCS}}_z[\mathfrak{gl}_1]$ on $\bC \times \bR^3$.

## Proof architecture

Six adjacent bidirections; $\binom{7}{2} - 6 = 15$ remaining edges close by transitivity.

| Edge | Bridge | Independent (HZ-IV) witness |
|------|--------|---------------------------|
| (i)$\Leftrightarrow$(ii) | Quasi-triangular axiom; universal hexagon | Vol II SC$^{\mathrm{ch,top}}$-heptagon face (6), chiral factorisation homology |
| (ii)$\Leftrightarrow$(iii) | Kohno: KZ monodromy $\equiv$ half-braiding up to Drinfeld associator | Arnold $1$-form $\eta = d\log(z_1 - z_2)$ on pure braid (Shelton--Yuzvinsky) |
| (iii)$\Leftrightarrow$(iv) | FLM + Borcherds denominator | $\kappa_{\mathrm{BKM}} = c_N(0)/2$ Borcherds-weight universality |
| (iv)$\Leftrightarrow$(v) | MO Thm 4.6.1 + Schiffmann--Vasserot CoHA | RSYZ toric tree amplitudes on CY$_3$ |
| (v)$\Leftrightarrow$(vi) | MO $R$-matrix $\hbar$-expansion leading term $=\delta^{(3)}$ | Vol I Part II cobar-complex shadow-tower direct computation |
| (vi)$\Leftrightarrow$(vii) | Costello--Gwilliam factorisation formality of hCS | Costello--Witten--Yamazaki $4d$CS reduction via transverse integral |

No edge shares a witness with an adjacent edge; the transitive closure is genuinely independent.

## Compliance checks

- HZ-7 (Vol III $\kappa$ discipline): only subscripted forms $\kappa_{\mathrm{ch}}$, $\kappa_{\mathrm{BKM}}$, $\kappa_{\mathrm{cat}}$, $\kappa_{\mathrm{fiber}}$ appear in surrounding material; no bare $\kappa$.
- AP247 ($\{\Phi_d\}$): hypothesis scopes CY image to the dimension-stratified correspondence, not a monolithic $\Phi$.
- AP-LABEL-DISCIPLINE: `thm:seven-faces-of-r-cy` unique across Vol I / Vol II / Vol III (grepped).
- Metadata hygiene: no `AP\d+`, `HZ-\d+`, `Pattern \d+`, `Cache #` tokens in the typeset theorem or proof.
- Russian-school voice: Drinfeld unifying principle (one element, seven realisations); Gelfand instant-computation on the generating primitive; Beilinson falsification via disjoint-source witnesses.

## Cross-volume bridge

The CY seven-face master is the $\Phi$-pushforward of Vol I `thm:vol1-seven-face-master` and Vol II `thm:vol2-seven-face-master`. Under the dimension stratification, face-by-face:

- Face 1 (bar-cobar) $\leftarrow$ Vol I climax $\bar\partial_X = \mathrm{KZ}^*(\nabla_{\mathrm{Arnold}})$
- Face 3 (KZ) $\leftarrow$ Vol I Arnold 1-form on pure braid configuration space
- Face 6 ($A_\infty$-coassociator) $\leftarrow$ Vol I shadow-tower $\delta^{(3)}$
- Face 7 (Costello hCS) $\leftarrow$ Vol II universal celestial holography (chiral factorisation on $P^1_{\mathrm{cel}}$)

## Verdict

Inscription already complete at `cy_holographic_datum_master.tex:856-950`. Audit finds structure, proof, and ledger conformant to the wave-13 TFAE template. No edit required; no commit made.
