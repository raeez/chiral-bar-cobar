# Chiral Derived Center at Genus >= 1: Curved Swiss-Cheese Analysis

Date: 2026-04-05
Author: Analysis of manuscript source

## Summary

This document investigates four questions about the genus >= 1 structure
of the chiral derived center Z^der_ch(A), systematically distinguishing
what is proved, what is conjectured, and what is genuinely new.

---

## Question 1: What is Z^der_ch(A) at genus 1?

### What is proved

At genus 0, the chiral derived center is:

    Z^der_ch(A) = H*(C^bullet_ch(A, A), delta)

where delta = [m, -] is the Gerstenhaber bracket with the A_infty
structure m = sum m_n (Theorem thm:thqg-brace-dg-algebra, PROVED).
On the Koszul locus, Theorem H gives concentration in degrees {0,1,2}
(eq:thqg-derived-center-three-term).

At genus g >= 1, the fiberwise bar differential satisfies d_fib^2 =
kappa(A) * omega_g (Theorem thm:modular-characteristic, PROVED). The
total corrected differential D_g = d_fib + nabla^GM restores D_g^2 = 0
(preface sec 10.7, PROVED).

The genus-0 derived center definition uses the UNCURVED differential
delta = [m, -] where [m, m] = 0. At genus 1, the A_infty structure
is CURVED: m_1^2(a) = [m_0, a] with m_0 = kappa * omega_1.

### What is genuinely happening at genus 1

The genus-1 chiral Hochschild complex is:

    C^bullet_ch(A, A)^(1) = (prod_{n>=0} End^ch_A(n+1)[-n], delta^(1))

where the deformed differential is:

    delta^(1)(f) = [m, f] + [m_0, f]_brace

Here m_0 = kappa(A) * omega_1 is the curvature element. The key
structural fact: delta^(1) does NOT square to zero on the nose.
Instead, (delta^(1))^2 is controlled by the curvature:

    (delta^(1))^2(f) = [m_0, [m_0, f]_brace]_brace

This is NOT zero in general. Therefore:

**The genus-1 chiral Hochschild complex is a CURVED complex.**

The cohomology of a curved complex (d^2 != 0) is NOT well-defined
in the ordinary sense. This is exactly why the manuscript (preface
sec 10.7, lines 6141-6150) states that one must pass to the CODERIVED
category D^co(A^(1)).

### What can be said

**Observation 1 (from the manuscript, proved).** The total corrected
differential D_g = d_fib + nabla^GM satisfies D_g^2 = 0. This means
the TOTAL complex (fibered over M_bar_g) has a well-defined cohomology.
The derived center at genus g is:

    Z^der_ch(A)^(g) := H*(C^bullet_ch(A,A) tensor O(M_bar_g), D_g)

This is a SHEAF cohomology on M_bar_g, not a single vector space.

**Observation 2 (from rem:sc-higher-genus, proved).** The curvature is
SCALAR (kappa * omega_g), hence central in the coalgebra. This means
the curved E_2-algebra structure on the Hochschild complex degenerates
in a controlled way: the Gerstenhaber bracket still makes sense on
the TOTAL complex, even though it fails fiber-by-fiber.

**Observation 3 (genuinely new, but follows from existing machinery).**
For the specific case of genus 1, the moduli space M_bar_{1,1} is
well understood (it is a weighted projective stack). The Hodge bundle
E is the tautological line bundle. The Gauss-Manin connection on
C^bullet_ch(A,A) tensor O(M_bar_{1,1}) is:

    nabla^GM = d_M - kappa * omega_1 / (Gauss-Manin correction)

The correction absorbs the curvature by coupling to the period
matrix tau of the elliptic curve fiber. The resulting flat complex
has cohomology that IS a well-defined sheaf on M_bar_{1,1}.

### Status classification

- Z^der_ch at genus 0: PROVED (Theorem H, def:thqg-chiral-derived-center)
- Curvature at genus >= 1: PROVED (Theorem D)
- Total corrected differential D_g^2 = 0: PROVED (preface sec 10.7)
- Need for coderived category: PROVED (preface sec 10.7)
- Explicit cohomology of Z^der_ch(A)^(1) as a sheaf on M_bar_1: NOT COMPUTED
- The question of whether the three-term concentration {0,1,2} persists
  at genus 1 in the total complex: OPEN

### What should NOT be written

Per AP31: kappa = 0 does NOT imply the genus-1 derived center equals
the genus-0 derived center. Even when the curvature vanishes
(uncurved case), the genus-1 complex lives over M_bar_1 and has
additional topological contributions from the moduli space.

Per AP6: "Z^der_ch at genus 1" without specifying fiberwise vs total
vs sheaf cohomology is AMBIGUOUS and should never be written.

---

## Question 2: The genus-2 open-to-closed map

### What is proved

The annulus trace theorem (thm:thqg-annulus-trace, PROVED) gives:

    int_{S^1_p} M ~= HH_*(M)

The non-separating degeneration (prop:thqg-annulus-degeneration-kappa,
PROVED) gives:

    Delta_ns(Tr_A) = kappa(A) * lambda_1

This is the genus-1, no-puncture open-to-closed map.

### What happens at genus 2

The genus-2 open-to-closed map involves a bordered surface Sigma_{2,1}
(genus 2 with one boundary component). The relevant amplitude is:

    Z^oc_{2,1} : HH_*(M) --> H*(M_bar_{2,1})

This map is obtained by the following composition:
1. Start with the annulus trace Tr_A in HH_0(M)
2. Apply TWO non-separating clutchings (to go from genus 0 to genus 2)
   OR one non-separating clutching followed by genus-raising

In the MC framework (thm:thqg-oc-mc-equation, PROVED), the genus-2
component of the clutching sector gives:

    xi*_ns(Theta^(2)) = Delta_ns(Theta^(1))
    xi*_sep(Theta^(2)) = Theta^(1) * Theta^(1)

These are PROVED identities (thm:mc2-bar-intrinsic(iii)).

**The genus-2 open-to-closed map is:**

    Z^oc_{2,1}(Tr_A) = Delta_ns^2(Tr_A) + (separating contributions)

On the uniform-weight lane (where F_g = kappa * lambda_g), the closed
projection gives F_2 = kappa * lambda_2^FP. The open-to-closed map
at genus 2 is therefore:

    Z^oc_{2,0}(A) = kappa(A) * lambda_2^FP + (higher-arity corrections)

### Status classification

- Genus-1 open-to-closed: PROVED (prop:thqg-annulus-degeneration-kappa)
- MC equation at all genera: PROVED (thm:thqg-oc-mc-equation)
- Clutching factorization: PROVED (thm:mc2-bar-intrinsic(iii))
- Explicit genus-2 open-to-closed formula via clutching: FOLLOWS from
  proved results but NOT explicitly stated in the manuscript
- The open-to-closed map at genus g as a map HH_*(M) -> H*(M_bar_{g,1}):
  IMPLICIT in the MC framework, not explicitly constructed as a separate
  theorem
- Independent open-sector derivation of genus-2 amplitudes (without
  invoking bar-intrinsic construction): OPEN (rem:thqg-mc-forced-scope(ii))

### What is genuinely new

The manuscript does not explicitly state the genus-2 open-to-closed
map as a separate result. However, it follows formally from the MC
equation. The genuinely new observation is:

**Proposition (follows from proved results).** For a modular Koszul
algebra A on the uniform-weight lane, the genus-g open-to-closed map
is the composition:

    Z^oc_{g,0}(A) = (Delta_ns)^{2g}(Tr_A)|_{arity 0}

where (Delta_ns)^{2g} denotes 2g iterated non-separating clutchings
(genus 0 with 2g additional pairs of identified points becomes
genus g), evaluated at zero boundary insertions. On the scalar lane
this gives kappa * lambda_g^FP.

This is a FORMAL consequence of thm:thqg-oc-mc-equation and
thm:mc2-bar-intrinsic(iii). It is not a new theorem but could be
stated as a corollary.

---

## Question 3: Modular cooperad structure on {Z^(g)}

### What is proved

The manuscript contains:

1. The MC equation for Theta^oc at all genera (PROVED,
   thm:thqg-oc-mc-equation)
2. The four-sector decomposition (PROVED)
3. The clutching factorization for the closed sector (PROVED,
   thm:mc2-bar-intrinsic(iii))
4. The Heisenberg modular cooperad (PROVED,
   thm:heisenberg-modular-cooperad)

### What is the question asking

The question asks whether the collection {Z^(g)} of genus-g derived
centers forms a modular cooperad. This requires:

(a) Structure maps: for each stable graph Gamma of type (g,n),
    a cocomposition delta_Gamma : Z^(g) -> tensor_v Z^(g_v)
(b) Coassociativity
(c) Compatibility with the MC equation

### Analysis

**The answer is nuanced.** The collection {Z^(g)} does NOT literally
form a modular cooperad, because:

1. At genus 0, Z^(0) = Z^der_ch(A) is a Gerstenhaber algebra (PROVED).
2. At genus >= 1, Z^(g) is not a single vector space but a SHEAF on
   M_bar_g (the cohomology of the total complex over moduli space).
3. The "cocomposition maps" come from the boundary stratification of
   M_bar_g, which ARE the clutching maps. These are proved to exist
   at the chain level.

What IS true (and proved):

**The open/closed convolution algebra g^oc_{A,M} is a modular dg Lie
algebra**, meaning it carries the full genus-graded structure with
all sewing operations. The MC equation Theta^oc encodes the FULL
modular structure. The clutching maps on M_bar_{g,n} induce structure
maps on the convolution algebra.

What is NOT proved but conjectured:

**The descent of the cooperad structure from the chain level
(convolution algebra) to the cohomology level (derived center) is
NOT automatic.** The convolution algebra is a chain-level object; the
derived center is its cohomology. The cooperad structure on chains
descends to cohomology only if the clutching maps are compatible
with the quasi-isomorphisms — this is part of the modular cooperad
completion programme (concordance sec:concordance-modular-cooperad-
completion, ledger RED).

For Heisenberg: PROVED (thm:heisenberg-modular-cooperad). The
semisimplicity of Perf(H_kappa) makes the descent automatic.

For general algebras: OPEN. The concordance explicitly states
(lines 9188-9218) that "the missing step is the categorical
construction of cocomposition maps from iterated clutching on
bordered FM compactifications."

### Status classification

- Chain-level modular structure on g^oc: PROVED
- MC equation encoding all clutching: PROVED
- Heisenberg cooperad: PROVED
- General cooperad on cohomology: PROGRAMME (concordance RED)
- Compatibility with MC equation: FOLLOWS formally from PROVED
  results at the chain level

### AP check

Per AP30 (CohFT axiom hidden hypothesis): the cooperad structure
requires checking ALL axioms (equivariance, coassociativity, self-
sewing, compatibility). The MC equation gives the identities; the
categorical construction gives the maps. The identities are proved;
the maps are under construction.

Per AP42 (correct at sophisticated level, false at naive level): the
statement "the derived centers form a modular cooperad" is TRUE at
the chain level (convolution algebra) but NOT YET PROVED at the
cohomology level for general algebras. The level must be specified.

---

## Question 4: The full open/closed partition function

### What is in the manuscript

The shadow partition function is defined (thm:shadow-double-convergence,
PROVED):

    Z^sh(A, hbar) = sum_{g>=1} sum_{r>=2} hbar^{2g-2} Z_g^(r)(A)

This converges absolutely for |hbar| < 2pi when rho(A) < 1.

The MC element Theta^oc packages both open and closed data
(constr:thqg-oc-mc-element, PROVED).

### What is the question asking

The full open/closed partition function would be:

    Z^oc(A) = sum_g hbar^{2g} sum_n (1/n!) Z^(g,n)

where Z^(g,n) is the genus-g, n-boundary amplitude.

### Analysis

**This is the shadow partition function with boundary insertions.**
The relationship is:

1. Z^sh(A) = the CLOSED projection of Z^oc(A), i.e., the n=0
   (no boundary) component. More precisely, Z^sh captures the
   tautological intersection numbers on M_bar_g from the shadow
   CohFT, which is the arity-graded projection of the closed-sector
   genus tower.

2. The n >= 1 components of Z^oc involve boundary amplitudes:
   Z^(g,n) lives in H*(M_bar_{g,n}) tensor End(M)^{tensor n},
   encoding how n boundary operators modify the genus-g amplitude.

3. The MC equation (thm:thqg-oc-mc-equation) constrains ALL
   Z^(g,n) simultaneously. The closed projection (n=0) recovers
   Z^sh. The open projection gives the boundary corrections. The
   mixed projection gives the bulk-to-boundary couplings.

### What is proved

- Z^sh converges absolutely: PROVED (thm:shadow-double-convergence)
- The MC equation constrains all Z^(g,n): PROVED
  (thm:thqg-mc-forced-consistency)
- Consistency of open and closed sectors at every genus: PROVED
  (thm:thqg-mc-forced-consistency(d))
- Explicit formula for Z^(1,0) = kappa * lambda_1: PROVED (Theorem D)

### What is conjectured/open

- Convergence of the full Z^oc (including boundary insertions):
  NOT STATED. The shadow partition function convergence
  (thm:shadow-double-convergence) is for the CLOSED sector only.
  The open sector would require HS-sewing type estimates for
  the boundary amplitudes as well. The general HS-sewing criterion
  (thm:general-hs-sewing) covers the closed sector; whether the
  same bounds extend to bordered amplitudes is OPEN.

- The explicit relationship Z^oc = exp(F^oc) or similar
  exponentiation: NOT PROVED. The MC equation gives the EQUATIONS
  satisfied by Z^oc, not a closed-form expression.

- Independent open-sector derivation: OPEN
  (rem:thqg-mc-forced-scope(ii))

### What is genuinely new

The relationship between Z^oc and Z^sh can be made precise:

**Observation.** On the uniform-weight lane, the full open/closed
partition function decomposes as:

    Z^oc(A, hbar) = Z^sh(A, hbar) + sum_{n>=1} (1/n!) Z^mix_n(A, hbar)

where Z^sh is the proved convergent shadow partition function and
Z^mix_n encodes the n-boundary corrections. The MC equation
(thm:thqg-oc-mc-equation) constrains each Z^mix_n in terms of
Z^sh and the A_infty module structure on M.

At genus 1: Z^mix_1(A, hbar)|_{g=1} = (annulus trace contribution),
which is controlled by HH_*(M) (thm:thqg-annulus-trace).

This decomposition is IMPLICIT in the existing framework but not
stated as a single result.

---

## Genuinely New Results

After careful analysis, the following are genuinely new observations
that can be proved from existing machinery:

### Result 1: Genus-1 derived center as sheaf on M_bar_1

The genus-1 chiral derived center is a SHEAF on M_bar_{1,1}, not a
single vector space. The total complex (C^bullet_ch(A,A) tensor
O(M_bar_1), D_1) has D_1^2 = 0, and its cohomology is a
quasi-coherent sheaf on M_bar_{1,1}. On the Koszul locus, this
sheaf is expected to be concentrated in the same degrees {0,1,2}
as the genus-0 center, but with modified sections reflecting the
curvature deformation.

STATUS: The sheaf structure FOLLOWS from the proved D_1^2 = 0.
The concentration in {0,1,2} at genus 1 is a CONJECTURE (requires
checking whether the spectral sequence from the genus-1 Hochschild
filtration still degenerates).

### Result 2: Iterated clutching gives genus-g open-to-closed map

The genus-g open-to-closed map is obtained by composing the annulus
trace with g non-separating clutchings:

    Z^oc_{g,0}(A) = pi_0 (Delta_ns^{compose g} (Tr_A))

where pi_0 projects to the zero-boundary component. This gives a
canonical map HH_0(M) -> H*(M_bar_g) for each g.

STATUS: FOLLOWS from thm:thqg-oc-mc-equation and
thm:mc2-bar-intrinsic(iii). Should be stated as a corollary.

### Result 3: The genus-1 curvature-braiding entanglement

The question q:genus1-entanglement (ordered_associative_chiral_kd.tex
line 5892) identifies a genuinely deep open problem: whether the
genus-1 coupling between bar curvature d^2 = kappa * omega_1 and
the spectral braiding monodromy 2*eta_tau * c_0 represents genuine
entanglement of the two Swiss-cheese colors.

The obstruction lies in H^1(SL(2,Z), O^mer(E_tau) tensor End(A)).
This is a NEW cohomological obstruction that does not appear in the
genus-0 theory and is specific to the curved Swiss-cheese structure.

STATUS: OPEN (ClaimStatusOpen). This is the most interesting new
direction identified in this analysis.

---

## Manuscript Locations to Update

No new results are strong enough to warrant manuscript changes at
this time. The key findings are:

1. The four questions all have well-defined answers within the
   existing framework, but several are classified as PROGRAMME
   rather than PROVED.

2. The most interesting open direction is q:genus1-entanglement
   (already in the manuscript as an open question).

3. The modular cooperad completion programme (concordance RED) is
   the primary bottleneck for Questions 3 and 4.

4. A potential COROLLARY (Result 2 above) could be stated in the
   open/closed realization section, but it is a formal consequence
   of existing theorems, not a new result.

---

## Anti-Pattern Checks

- AP6 (boundary qualifications): Every statement above specifies
  genus, fiberwise vs total, chain vs cohomology level.
- AP25 (three functors): Bar (coalgebra), Verdier dual (algebra),
  derived center (bulk) are never conflated.
- AP30 (CohFT axioms): The cooperad question explicitly lists which
  axioms are proved vs outstanding.
- AP31 (kappa = 0 does not imply Theta = 0): The genus-1 derived
  center is nontrivial even when kappa = 0.
- AP34 (bar-cobar != open-to-closed): The open-to-closed passage is
  through the derived center, not through bar-cobar inversion.
- AP42 (correct at sophisticated level): The cooperad statement is
  qualified at both chain and cohomology levels.
