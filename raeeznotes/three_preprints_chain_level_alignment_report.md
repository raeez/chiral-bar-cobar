# Three-preprint chain-level alignment report

This pass pushes the earlier rewrite toward the end-state presentation requested in the programme: the three papers are no longer treated as background, but as the source of concrete chain-level structures written directly into the manuscript and archive.

## Core mathematical upgrade

The central deformation object is now presented uniformly as

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

This is the direct synthesis of:

- **Malikov--Schechtman:** `A^{\mathrm{ch}}_\infty=\check C^\bullet(\mathfrak U;\cA)` as the derived chiral input;
- **Robert-Nicoud--Wierstra + Vallette:** convolution `L_\infty` functoriality/strictification;
- **Mok:** log-FM chain cooperad and rigid boundary correspondences.

## Concrete structures now written into the manuscript

### Volume I

1. **Graphwise log-FM cocomposition**
   ```tex
   \Delta^{\log}_{\Gamma}
   :=
   (\nu_\Gamma)_*\circ \operatorname{Res}_{D^{\log}_{\Gamma}}.
   ```
2. **Graphwise Taylor coefficients**
   ```tex
   \ell_\Gamma(f_1,\dots,f_k)
   =
   \mu_\Gamma\circ
   (\alpha^{\mathrm{mod}}_\Gamma\otimes f_1\otimes\cdots\otimes f_k)
   \circ \Delta^{\log}_{\Gamma},
   \qquad
   \ell_k^{(g)}=\sum_\Gamma \frac{1}{|\Aut(\Gamma)|}\,\ell_\Gamma.
   ```
3. **Boundary operators as residue correspondences**
   ```tex
   d_{\mathrm{sew}},\ d_{\mathrm{pf}},\ \hbar\Delta
   ```
   are now written explicitly as residue/pushforward maps on log-FM strata.
4. **Genus-two shell decomposition**
   ```tex
   \Theta_\cA^{(2)}
   =
   \Theta_{\cA,\mathrm{loop}\circ\mathrm{loop}}^{(2)}
   +\Theta_{\cA,\mathrm{sep}\circ\mathrm{loop}}^{(2)}
   +\Theta_{\cA,\mathrm{pf}}^{(2)}.
   ```
5. **Modular tangent complex / Chern--Weil viewpoint**
   ```tex
   T^{\mathrm{mod}}_{\Theta_\cA}
   :=
   (\Definfmod_{\log}(\cA;\mathfrak U),d_{\Theta_\cA}),
   ```
   with characteristic shadows
   ```tex
   \kappa(\cA)=\operatorname{tr}(\Theta_\cA)_{2,0},
   \quad
   \Delta_\cA(t)=\operatorname{sdet}(1-t\,H(d_{\Theta_\cA}|_{\mathrm{red}})),
   \quad
   \mathfrak R^{\mathrm{mod}}_{4,g,n}(\cA)=\operatorname{pr}_{4,g,n}(\Theta_\cA).
   ```

### Volume II

1. **PVA-coordinate residue formulas** for `\ell_3^{(0)}`, `\ell_4^{(0)}`, and `\ell_1^{(1)}=\hbar\Delta_{\mathrm{cyc}}`.
2. **Explicit archetype formulas**
   - Heisenberg: Gaussian and purely one-loop at low order;
   - affine currents: cubic invariant tensor `f_{abc}` and vanishing quartic tree term;
   - `W_3`: quartic tree coefficient controlled by
     ```tex
     \Lambda={:}TT{:}-\frac{3}{10}\partial^2T,
     \qquad
     [\ell_4^{(0)}]\propto \frac{16}{22+5c}\,\Lambda.
     ```
3. **Genus-two shell decomposition** in boundary coordinates.

## Compute support added/validated

The low-genus helper module now includes explicit genus-two shell bookkeeping:

- `compute/lib/modular_bar.py`
  - `genus_two_shells()`
  - `genus_two_profile()`
- `compute/tests/test_modular_bar.py`
  - genus-two shell tests

Validation run:

```text
11 passed in 0.12s
```

## Files changed in this pass

### Volume I
- `vol1/chapters/theory/higher_genus_modular_koszul.tex`
- `vol1/chapters/connections/concordance.tex`
- `vol1/archive/misc/three_preprints_chain_level_alignment.md`

### Volume II
- `vol2/chapters/connections/modular_pva_quantization.tex`
- `vol2/notes/three_preprints_chain_level_alignment.md`
- `vol2/compute/lib/modular_bar.py`
- `vol2/compute/tests/test_modular_bar.py`

## Validation note

No LaTeX engine is installed in this environment, so I did not run a PDF compile. The Python test support for the new low-genus bookkeeping does run and passes.
