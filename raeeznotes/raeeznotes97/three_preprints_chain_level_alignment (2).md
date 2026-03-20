# Three-preprint chain-level alignment

This memo records the concrete rewrite forced by the three foundational papers: Malikov--Schechtman on homotopy chiral algebras, Robert-Nicoud--Wierstra together with Vallette on convolution/homotopy deformation theory, and Mok on logarithmic Fulton--MacPherson spaces.

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

Here `A^{\mathrm{ch}}_\infty=\check C^\bullet(\mathfrak U;\cA)` is the Malikov--Schechtman homotopy-chiral input, and `\cC^{\log FM}` is the Mok log-FM chain cooperad.  The one-slot convention is essential: geometry remains strict while the chiral input varies up to `\infty`-morphism.

## New concrete structures written into the manuscript

1. **Logarithmic modular bar functor** as a stable-graph sum with log-FM chain coefficients and edge-orientation lines.
2. **Five-piece differential** interpreted as transferred chiral differential + separating sewing + planted-forest correction + non-separating loop term.
3. **Low-genus Taylor coefficients** recorded explicitly as tree and loop amplitudes.
4. **Rigid-type boundary factorization** rewritten directly from Mok's degeneration correspondence.

## File-level integration

- `chapters/theory/higher_genus_modular_koszul.tex`: new subsection `subsec:three-preprints-chain-level`.
- `chapters/connections/concordance.tex`: new summary `sum:three-pillars-chain-level`.

## Immediate compute agenda

- Evaluate the log-FM presentation for Heisenberg, affine `\widehat{\mathfrak{sl}}_2`, Virasoro, and principal `\mathcal W_N`.
- Push the stable-graph formulas into explicit genus-2 and quartic-shadow tables.
- Replace any remaining abstract MC2 phrasing by the chain-level modular-convolution presentation.


## Latest native-object pass

9. **Primitive-kernel compression.**  The full stable-graph Maurer--Cartan field is now explicitly reconstructed from a primitive logarithmic modular kernel
   `\mathfrak K_\cA=\sum K^{\cA}_{g,n}+\sum R^{\cA}_{\rho}` via a logarithmic modular Feynman transform.
10. **Primitive master equation.**  The manuscript now states the exact equivalence
   `$(Q^{\mathrm{mod}}_\cA)^2=0 \iff d\mathfrak K_\cA+\mathfrak K_\cA\star \mathfrak K_\cA=0$`, so the native object is the primitive kernel rather than the already-expanded global field.
11. **Reduced branch BV action.**  The canonically extracted branch-active quotient now carries a finite-rank BV algebra and master action
   `S^{\mathrm{br}}_\cA`, making the spectral/branch package a genuine finite-dimensional shadow of the modular convolution object.
12. **Metaplectic square root.**  The determinant shadow is now factored through the formal half-density
   `\delta_\cA(x)=\exp(\frac12\operatorname{Tr}\log(1-xT^{\mathrm{br,red}}_\cA))`, a canonical square root of `\Delta_\cA(x)`.
13. **Primitive shell equations.**  Genus-two and genus-three forcing are now written directly in terms of `K_{1,1}`, `K_{2,\bullet}`, and rigid-cut amplitudes, separating the Heisenberg, affine, and Virasoro/`\mathcal W_N` regimes at the primitive level.
