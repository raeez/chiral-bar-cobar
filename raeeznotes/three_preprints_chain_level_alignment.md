# Three-preprint chain-level alignment

This memo records the strengthened rewrite forced by the three foundational papers: Malikov--Schechtman on homotopy chiral algebras, Robert-Nicoud--Wierstra together with Vallette on convolution/homotopy deformation theory, and Mok on logarithmic Fulton--MacPherson spaces.

## Core rewrite

The invariant modular deformation object is presented in chain coordinates by

```tex
\Definfmod_{\log}(\cA;\mathfrak U)
:=
\Convinf\!\Bigl(
\cC^{\log FM}_{\mathrm{mod}},
\operatorname{End}_{\mathrm{Ch}_\infty}(A^{\mathrm{ch}}_\infty)
\Bigr),
```

with strict chart

```tex
\mathfrak g^{\mathrm{mod,log}}_{\cA}(\mathfrak U)
:=
\Convstr\!\Bigl(
\cC^{\log FM}_{\mathrm{mod}},
\operatorname{End}_{\mathrm{Ch}_\infty}(A^{\mathrm{ch}}_\infty)
\Bigr).
```

Here `A^{\mathrm{ch}}_\infty=\check C^\bullet(\mathfrak U;\cA)` is the Malikov--Schechtman homotopy-chiral input, and `\cC^{\log FM}` is the Mok log-FM chain cooperad. The one-slot convention is essential: geometry remains strict while the chiral input varies up to `\infty`-morphism.

## New end-state structures added in this pass

1. **Universal class as twisting data.** In the log-FM chart,
   
   ```tex
   \operatorname{MC}_\bullet(\Definfmod_{\log})
   \simeq
   \operatorname{Tw}_{\alpha^{\mathrm{mod}}}
   (\cC^{\log FM}_{\mathrm{mod}},\operatorname{End}_{\mathrm{Ch}_\infty}(A^{\mathrm{ch}}_\infty)).
   ```
   
   The master object `\Theta_\cA` is no longer merely an MC point; it is the universal modular twisting morphism determined by the total bar differential.

2. **Rigid planted-forest differential as a push--pull formula.** The planted-forest term is written as
   
   ```tex
   d_{\mathrm{pf}}
   =
   \sum_{\rho\in \mathsf{PF}^{\mathrm{rig}}}
   \epsilon_\rho\,(\kappa_\rho)_*\operatorname{pr}_\rho^{*}\otimes \mu_\rho,
   ```
   
   so Mok's degeneration formula is transported directly into the modular convolution algebra.

3. **First two weights of the graph expansion.** Weight `1` is now identified explicitly with:
   - the three boundary points of `\overline{\cM}_{0,4}`, giving the Malikov--Schechtman secondary Borcherds/Jacobiator homotopy;
   - the irreducible boundary of `\overline{\cM}_{1,1}`, giving the BV loop operator.

   Weight `2` is the first genuinely logarithmic layer: rigid planted forests appear here for the first time.

4. **Cross-volume genus-two consequence.** Volume II now proves that along the classical `W_3` central-parameter line the quadratic self-coupling of the unique genus-one tangent direction is exact. Therefore any nontrivial genus-two obstruction must come from the rigid planted-forest sector or from new deformation directions.

## Low-genus formulas now foregrounded

```tex
\Theta_\cA^{[1]}\big|_{(0,4)}
=
[\delta_s]\otimes\Phi_s+[\delta_t]\otimes\Phi_t+[\delta_u]\otimes\Phi_u,
\qquad
\Theta_\cA^{[1]}\big|_{(1,1)}=[\delta_{\mathrm{irr}}]\otimes\Delta.
```

and the first weight relations are

```tex
[D_{\mathrm{loc}},\Theta_\cA^{[1]}]=0,
\qquad
[D_{\mathrm{loc}},\Theta_\cA^{[2]}]+
\tfrac12[\Theta_\cA^{[1]},\Theta_\cA^{[1]}]=0.
```

This is the cleanest chain-level statement of the slogan:

> tree homotopies and one-loop BV already appear at weight 1, but genuine logarithmic modularity begins at weight 2.

## File-level integration

- `chapters/theory/higher_genus_modular_koszul.tex`: strengthened subsection `subsec:three-preprints-chain-level`.
- `chapters/connections/concordance.tex`: strengthened constitutional summary `sum:three-pillars-chain-level`.

## Immediate next calculations

- Write explicit genus-2 stable-graph tables for Heisenberg, affine `\widehat{\mathfrak{sl}}_2`, Virasoro, and principal `\mathcal W_N` in the log-FM chart.
- Compute the first nontrivial rigid planted-forest coefficient for the `W_3` central line.
- Push the modular twisting-morphism presentation into the nonlinear shadow appendix so quartic and sextic shadows are extracted directly from the weight filtration.
