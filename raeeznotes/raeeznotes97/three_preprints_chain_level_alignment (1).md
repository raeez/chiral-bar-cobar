# Volume II chain-level alignment with the three foundational papers

This note records the concrete chain-level presentation added to the modular PVA quantization chapter.

## The guiding translation

- **Malikov--Schechtman** supplies the homotopy-chiral input `A^{\mathrm{ch}}_\infty=\check C^\bullet(\mathfrak U;\A)`.
- **Robert-Nicoud--Wierstra + Vallette** supply the homotopy-invariant convolution `L_\infty` object and its strictification principle.
- **Mok** supplies the log-FM chain cooperad and rigid-type degeneration formulas.

## Resulting presentation

The modular deformation object is now written in coordinates as

```tex
\Definfmod_{\log}(C)
:=
\Convinf\!\Bigl(
\cC^{\log FM}_{\mathrm{mod}},
\operatorname{End}_{\mathrm{Ch}_\infty}(A^{\mathrm{ch}}_\infty)
\Bigr),
```

with strict chart

```tex
L^{\log}_{\mathrm{mod}}(C)
:=
\Convstr\!\Bigl(
\cC^{\log FM}_{\mathrm{mod}},
\operatorname{End}_{\mathrm{Ch}_\infty}(A^{\mathrm{ch}}_\infty)
\Bigr).
```

The existing coderivation algebra `L_{\mathrm{mod}}(C)` is interpreted as the bar-side realization of this strict chart.

## New concrete content written into the chapter

1. Stable-graph modular bar functor with log-FM chain coefficients.
2. Low-genus Taylor coefficients `\ell_3^{(0)}`, `\ell_4^{(0)}`, and `\ell_1^{(1)}=\hbar\Delta_{\mathrm{cyc}}`.
3. Boundary/clutching explained as a rigid-type push-pull identity on log-FM spaces.
4. The one-edge principle recast as the genus-1 coefficient of the same modular bar functor.

## File-level integration

- `chapters/connections/modular_pva_quantization.tex`: new subsection `subsec:vol2-three-preprints-chain-level`.
- `main.tex`: bibliography extended with `RNW19` and `Val16`.


## Native-object and square-root pass

9. **Primitive boundary kernel.**  The PVA chapter now starts from the primitive kernel
   `\mathfrak K_C=K_{0,2}+K_{0,3}+K_{0,4}+K_{1,1}+R_{\mathrm{pf},2}+R_{\mathrm{pf},3}+\cdots` and reconstructs the full strict modular field by logarithmic Feynman transform.
10. **Primitive shell recursion.**  The genus-two and genus-three forcing identities are now written directly in boundary coordinates, with explicit `\Delta_{\mathrm{cyc}}`, separating bracket, and rigid-cut terms.
11. **Branch BV action.**  The reduced active packet now carries a finite-dimensional BV master action `S^{\mathrm{br}}_C`, so the branch package is a direct finite-rank shadow of the modular convolution object.
12. **Metaplectic half-density.**  The determinant shadow is now square-rooted by the formal series
   `\delta_C(x)=\exp(\frac12\operatorname{Tr}\log(1-xT_C^{\mathrm{br,red}}))`.
13. **Archetype master actions.**  Heisenberg is now purely quadratic, affine is cubic-tree, and `W_3` is quartic-rigid already at the primitive/master-action level.
