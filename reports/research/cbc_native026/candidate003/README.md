# Periodic elliptic propagator and actual Dolbeault homotopy

This is a new bounded proof successor, not an acceptance of the native book. Source002 remains frozen. The mathematical source is `research-candidates/cbc_native026/candidate003/proof/elliptic_propagator.tex`, SHA256 `c990f9adeb01ebb53108d8ff59a14c7bba14c0c6ca136b0d51598ad662905b05`. The two-source manifest SHA is `ec88713d11a841d221352e828ac1cf9750b1796c4fa13d4eb34af0d13bb876b1`.

## Question and result

The corrected meromorphic covering-plane kernel in source002 was not yet an elliptic propagator. This module constructs the actual periodic kernel on E_tau=C/(Z+tau Z):

`P_tau(z)=zeta_tau(z)−(pi²/3)E2(tau)z+2pi i Im(z)/Im(tau)`.

It proves periodicity, oddness, local integrability, the exact current equation `barpartial(P dz)=2pi i(delta0−nu_tau)`, uniqueness, weight-one modular covariance, and invariance of its one-form. The constant subtraction is necessary: pairing a putative unsubtracted current equation with the constant test function gives0=2pi i.

It then constructs the actual continuous operator `H(f dbarz)(z)=pi^-1 integral P(z−w)f(w) dx_wdy_w` on smooth Dolbeault forms. The complete proof gives `dH+Hd=1−ip`, `pi=1`, `Hi=pH=H²=0`, with p the coefficientwise average and i the constant-coefficient inclusion. It proves smoothness, Frechet continuity, and naturality under every SL2(Z) lattice-basis change. The square-torus Fourier mode distinguishes the inverse on nonconstant modes from the obstructed constant mode.

## Carriers, proof dependencies and exact limits

The coefficient field is C. The domain is the compact smooth torus with tau in the upper half-plane; forms are smooth complex-valued functions and(0,1)-forms, with their usual Frechet topology. The kernel is locally integrable, not a holomorphic elliptic function. Distributions use oriented area dx wedge dy, residue1, and the stated barpartial sign. The current equation and homotopy retain the constant projection.

Periodicity is proved directly by differentiating the normally convergent lattice series, using evenness and a fundamental-parallelogram contour. The modular law follows from uniqueness and the imaginary-part transformation, independently of an assumed character weight. The identification of its coefficient with E2 uses the primary Fourier formula DLMF23.8.2 with half-periods1/2,tau/2; the lattice definition is DLMF23.2.5. The primary equations were verified with the web reader. Their locators and normalization are saved in `primary-sources/locators.json`; a separate attempt to download raw TeX returned HTTP403 and no downloaded original is claimed. The source uses these formulas with explicit normalization and convergence domain, then derives its claims.

No character-to-chain trace, field-theory BRST comparison, collision-compatible chiral contraction, or genus-g extension is constructed. The analytic smooth Dolbeault complex is not silently identified with algebraic chiral chains. Native consumer integration would be a separate source candidate requiring exact review.

## Reproduction and inspection

From the owned worktree:

```sh
python3 reports/research/cbc_native026/candidate003/check_elliptic.py
python3 reports/research/cbc_native026/candidate003/build.py
```

The360 exact nonconstant Fourier-mode checks pass. Numerical periodicity and modular illustrations are recorded separately with floating-error certification explicitly unclaimed; they are not used to prove the general formulas. The three-pass pdflatex build converges without warnings. PDF SHA256 `a4551df9526b233bd462b648b9fc59713e09fc6146351c5c3bba7da1e85bff8b`, four pages. All four rendered pages were individually inspected; no clipping, overlap, missing glyph or manuscript-firewall violation was found. Build commands, toolchain, environment, recorder inputs and saved dependency bytes accompany the source manifest. Self-inspection is diagnostic; fresh exact mathematical review remains required.

No staging, commit, push or source changes outside the owned worktree occurred. Mathematical controls were requested as gpt-6-astra/ultra; independently observed metadata is unavailable and remains unverified.
