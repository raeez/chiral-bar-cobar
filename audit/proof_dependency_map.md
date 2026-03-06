# Proof Dependency Map

## Status: ALL DEPENDENCIES VERIFIED — No open issues

## Main Theorems

### Theorem A (thm:bar-cobar-isomorphism-main, higher_genus.tex:1488)
- Hypothesis: (A1, A2) is a chiral Koszul pair
- Depends on: thm:verdier-bar-cobar, thm:arnold-three, def:chiral-koszul-pair
- Used by: Theorem B, Theorem C, all example chapters
- **Status: CLEAN**

### Theorem B (thm:higher-genus-inversion, higher_genus.tex:7383)
- Hypothesis: A is "modular Koszul" (def:modular-koszul-chiral)
- Depends on: thm:bar-nilpotency-complete, thm:chiral-koszul-duality, lem:higher-genus-open-stratum-qi, lem:higher-genus-boundary-qi, lem:extension-across-boundary-qi
- Part (b): off Koszul locus, uses coderived category (Positselski)
- **Status: CLEAN** (F4 resolved — modular Koszulity language harmonized)

### Theorem C (thm:quantum-complementarity-main, higher_genus.tex:4609)
- Hypothesis: (A, A!) is a chiral Koszul pair on smooth projective curve
- Depends on: thm:ss-quantum, thm:verdier-duality-config-complete, thm:kodaira-spencer-chiral-complete, lem:fiber-cohomology-center, lem:verdier-involution-moduli, lem:eigenspace-decomposition-complete
- **Status: CLEAN** (F1 resolved genus filtration, F2 resolved notation, F5 resolved eigenvalue sign)

## Key Supporting Results

### Kodaira-Spencer map (thm:kodaira-spencer-chiral-complete, higher_genus.tex:5210)
- Depends on: BD04 Thm 4.6.1 (Gauss-Manin), module Koszul duality equivalence
- **Status: CLEAN**

### Center isomorphism (sublem:center-isomorphism, higher_genus.tex:5427)
- Depends on: thm:e1-module-koszul-duality
- **Status: CLEAN**

### Genus universality (thm:genus-universality, higher_genus.tex:3960)
- Depends on: thm:heisenberg-obs, thm:kac-moody-obs, thm:vir-genus1-curvature, Mumford relation, Faber-Pandharipande
- **Status: CLEAN** (F6 resolved — Heisenberg h^v=0 case documented)

### PBW Koszulness (thm:pbw-koszulness-criterion, chiral_koszul_pairs.tex)
- Standalone resolution of the Koszulness circularity
- Used by: thm:km-chiral-koszul, thm:virasoro-chiral-koszul
- **Status: CLEAN**

### Modular Koszul examples (prop:standard-examples-modular-koszul, higher_genus.tex:7646)
- **Status: CLEAN** (F4 resolved — verification status harmonized with open-question framing)
