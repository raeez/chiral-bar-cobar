# Volume II chain-level alignment with the three foundational papers

This note records the stronger chain-level refoundation now written into Volume II.

The basic point is that the bulk/boundary/line archive is no longer being read as a loose collection of BV, PVA, FM$_3$, and holographic constructions.  It is being recast as one logarithmic modular-convolution theory with explicit coefficients, higher brackets, effective actions, and clutching formulas.

## 1. Imported concrete structures

### Malikov--Schechtman
The native input is the homotopy-chiral Čech totalization

```tex
\Obs^{\mathrm{hol}}_\infty := \check C^\bullet(\mathfrak U;\Obs^{\mathrm{hol}}),
```

with higher derived OPE operations encoded by

```tex
F_n : \Lie(n)\otimes Y(n) \to P_n(\{\Obs^{\mathrm{hol}}_\infty\},\Obs^{\mathrm{hol}}_\infty).
```

### Robert-Nicoud--Wierstra
The controlling deformation object is a coloured convolution `sL_\infty` algebra with explicit Taylor coefficients

```tex
\ell_m(F_1,\ldots,F_m)(x)
=
\gamma_{\mathrm{obs}}\Bigl((\alpha_{\mathrm{HT}}\circ 1)(F_1\otimes\cdots\otimes F_m)\Delta_m^{\log}(x)\Bigr).
```

### Vallette
The coderivation/BV/PVA charts used in the archive are now interpreted as strict quasi-free coordinate models of a homotopy-invariant deformation problem.

### Mok
The FM coefficient side is upgraded to genuine logarithmic chains

```tex
\cC^{\log FM}_{X|D}(n):=C_\bullet(\FM_n(X|D)),
\qquad
\cC^{\log FM}_{W/B}(n):=C_\bullet(\FM_n(W/B)),
```

with geometric depth filtration and rigid-type clutching:

```tex
\operatorname{codim}(W_\nu)=\sum_i w_i + \sum_j(|V(T_{v_j})|-1),
```

```tex
\FM_n(W/B)(\rho) \to \prod_{v\in V(S_\rho)} \FM_{I_v}(Y_v|D_v).
```

## 2. New concrete structures written into the manuscript

### (a) Coloured modular deformation object

```tex
\mathfrak g^{\mathrm{HT},\log}_{\mathrm{mod}}
:=
\operatorname{hom}^{\alpha_{\mathrm{HT}}}
\Bigl(
C_\bullet(\FM^{\log}_{\bullet,\mathrm{SC}}),
\operatorname{End}_{\mathrm{Ch}_\infty}(\Obs^{\mathrm{hol}}_\infty,\Obs^{\partial}_\infty,\Obs^{\ell}_\infty)
\Bigr).
```

### (b) Modular effective action

```tex
\mathcal S^{\mathrm{mod}}_{\mathrm{HT}}
:=
\sum_{\Gamma\in\mathrm{StGr}^{+}_{\mathrm{SC}}}
\frac{\hbar^{b_1(\Gamma)}}{|\Aut(\Gamma)|}
W^{\log}_\Gamma\,\mathcal O_\Gamma.
```

### (c) BV quantum master equation in modular form

```tex
\bigl(d_{\mathrm{BV}}+\hbar\Delta_{\mathrm{odd}}\bigr)
\exp\!\Bigl(\frac{\mathcal S^{\mathrm{mod}}_{\mathrm{HT}}}{\hbar}\Bigr)=0.
```

### (d) Rigid-type clutching law

```tex
\Theta^{\mathrm{HT},\log}\big|_\rho
=
(\kappa_\rho)_*\Bigl(\bigotimes_{v\in V(S_\rho)}\Theta^{\mathrm{HT},\log}_v\Bigr)
+\partial(\text{birational correction}).
```

### (e) Projected modular recursion

```tex
\partial\Theta^{\mathrm{HT},\log,(g,n)}
+
\sum_{\rho\,\mathrm{sep}} (\kappa_\rho)_*(\Theta\boxtimes\Theta)
+
\Delta_{\mathrm{ns}}\Theta^{\mathrm{HT},\log,(g-1,n+2)}
+
\sum_{\nu\,\mathrm{pf}} \partial_\nu\Theta^{\mathrm{HT},\log,(g,n)}
=
0.
```

## 3. Low-order signatures now made explicit

The low-order graph dictionary is now written in a unified way:

| Type | Geometric support | Physical meaning |
|---|---|---|
| `(0,3)` | codim-1 FM$_3$ face | first higher OPE / Jacobi correction |
| `(0,4)_{\mathrm{cont}}` | rigid 4-point contact stratum | quartic contact vertex |
| `(0,4)_{\mathrm{pf}}` | planted-forest depth-1 stratum | iterated cubic exchange |
| `(1,1)_{\mathrm{tad}}` | non-separating loop divisor | one-loop odd Laplacian |
| `(1,2)_{\mathrm{sep}}` | rigid separating boundary | tree/loop clutching |

This cleanly organizes the standard theories:

- **Free multiplet**: `\ell_3^{(0)}=\ell_4^{(0)}=0`, only the scalar one-loop term survives.
- **Affine/current algebra regime**: `\ell_3^{(0)}\neq0`, `\ell_4^{(0)}=0`, first modular term is `\hbar\Delta_{\mathrm{odd}}`.
- **Virasoro / `\mathcal W_3` regime**: `\ell_3^{(0)}\neq0`, `\ell_4^{(0)}\neq0`, and the quartic planted-forest coefficient is genuinely nonlinear.

## 4. Manuscript-level integration

- `chapters/connections/three_pillars_chainlevel_refoundation.tex`
  - rewritten as the explicit Volume II chain-level refoundation section;
  - includes formulas for the coloured convolution object, RNW Taylor coefficients, the modular effective action, rigid-type clutching, and the low-order graph dictionary.
- `main.tex`
  - updated to include `chapters/connections/three_pillars_chainlevel_refoundation` directly after `modular_pva_quantization`.

## 5. Immediate compute agenda

1. Work out explicit propagator integrals for the first nontrivial logarithmic rigid types.
2. Compute genus-2 / two-boundary coefficients of `\mathcal S^{\mathrm{mod}}_{\mathrm{HT}}`.
3. Extract the linearized transport operator `T_{\Theta}` governing the spectral determinant in the holographic sectors.
4. Produce explicit `\mathcal W_3` and line-operator quartic/sextic shadow tables in the new logarithmic chart.
5. Rewrite the remaining holographic and celestial sections so that every higher transport statement factors through the same coloured modular-convolution object.
