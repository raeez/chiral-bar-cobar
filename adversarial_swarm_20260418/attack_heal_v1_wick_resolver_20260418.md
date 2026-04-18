# V1 Wick Resolver: sl_2 Level-1 Numerical Verification of Vol I
## `thm:sugawara-antighost-primitive-chain-level`

Author: Raeez Lorgat
Date: 2026-04-18
Session: Wave-V1-Wick-Resolver

## Mission

Resolve the direct Vol I vs Vol II contradiction on
`thm:sugawara-antighost-primitive-chain-level`.

- Vol I `chapters/theory/topologization_chain_level_platonic.tex:427`
  inscribes the theorem as `\ClaimStatusProvedHere` with explicit
  closed forms $\eta_1^{(i)}, \eta_1^{(ii)}$ (eqs 297-307) and
  a proof that
  $[Q_{\mathrm{tot}}, \widetilde G_1] = T_{\mathrm{Sug}}$ strictly
  on cochains, where $\widetilde G_1 = G_1 - \eta_1$.
- Vol II `chapters/connections/e_infinity_topologization.tex:382-411`
  `rem:frontier-class-L-strict-chain-level` says the same claim is a
  frontier item: "An earlier summary draft asserted the explicit forms
  $\eta_1^{(i)}, \eta_1^{(ii)}$; the verification that these choices
  absorb the full chain-level discrepancy is pending."

The resolution requires a numerical Wick-contraction computation at
$\mathfrak{sl}_2$, level $k = 1$, the standard simplest test case.

## Method

Explicit symbolic-index computation in rational arithmetic
(`/tmp/wick_verify_sl2_v2.py`, `/tmp/wick_verify_sl2_v3.py`).

The CFG bulk cochain complex at $\mathfrak{sl}_2, k=1$ is encoded by:
- structure constants $f^a_{bc}$ for the basis $\{e, f, h\}$ with
  $[e,f]=h, [h,e]=2e, [h,f]=-2f$;
- trace form $\kappa(e,f)=1, \kappa(h,h)=2$;
- Sugawara prefactor $\frac{1}{2(k+h^\vee)} = \frac{1}{6}$ at $h^\vee=2$.

The BRST differential acts per eqs (174-180) of the chapter:
$$
Q_{\mathrm{tot}}\, c^a = \tfrac{1}{2} f^a{}_{bc} c^b c^c, \quad
Q_{\mathrm{tot}}\, J_a = f^c{}_{ab} J_c\, c^b, \quad
Q_{\mathrm{tot}}\, \bar c_a = J_a + f^c{}_{ab}\, \bar c_c\, c^b.
$$
On $J^a = \kappa^{ad} J_d$ the differential is
$Q_{\mathrm{tot}} J^a = \kappa^{ad} f^c{}_{db} J_c\, c^b$.

Graded Leibniz is applied term by term; all resulting monomials are
canonicalized under fermion graded-anticommute on distinct fields;
$J_{\mathrm{low}}$ is raised via $\kappa^{ab}$ so that all currents
live in the single symbol $J^a$.

Test-by-test comparison of
- (T1) $[Q, G_1] \stackrel{?}{=} T_{\mathrm{Sug}} + R_{\mathrm{ghost}} + R_{\mathrm{self}}$
  (Vol I `prop:QG1-remainder`, eq 243);
- (T2) $[Q, \eta_1^{(i)}] \stackrel{?}{=} R_{\mathrm{ghost}}$
  (Vol I `prop:eta-i-primitive`, eq 331);
- (T3) $[Q, \eta_1^{(ii)}] \stackrel{?}{=} R_{\mathrm{self}}$
  (Vol I `prop:eta-ii-primitive`, eq 395);
- (T4) $[Q, \widetilde G_1] \stackrel{?}{=} T_{\mathrm{Sug}}$
  (Vol I main, eq 440).

## Results

### Key identity: $R_{\mathrm{ghost}} + R_{\mathrm{self}} \equiv 0$

`/tmp/wick_verify_sl2_v3.py` established independently:
$$
R_{\mathrm{ghost}} + R_{\mathrm{self}} = 0
\qquad\text{on the canonicalized $\mathfrak{sl}_2$ cochain basis.}
$$
Explicitly, in the canonical basis of 3-field fermion-sorted NO
monomials at $\mathfrak{sl}_2, k=1$:
- $R_{\mathrm{ghost}}$ has 6 monomials with coefficients
  $\{\pm 1/6, \pm 1/3, \pm 1/3\}$ at the expected index patterns;
- $R_{\mathrm{self}}$ has the SAME 6 monomials with OPPOSITE signs.
- Sum: $R_{\mathrm{ghost}} + R_{\mathrm{self}} = 0$ monomial-by-monomial.

### Test 1 (classical identity): DETECTED RESIDUAL

$[Q, G_1] - (T_{\mathrm{Sug}} + R_{\mathrm{ghost}} + R_{\mathrm{self}})$
has 6 surviving monomials after canonicalization, structurally
matching $-2\cdot(R_{\mathrm{ghost}} - R_{\mathrm{self}})$, which
because $R_{\mathrm{self}} = -R_{\mathrm{ghost}}$, equals
$-4\cdot R_{\mathrm{ghost}}$ at the cochain level.

Interpretation: the correct chain-level identity at $\mathfrak{sl}_2, k=1$ is
$$
[Q, G_1] = T_{\mathrm{Sug}} + 4\, R_{\mathrm{ghost}},
$$
NOT $T_{\mathrm{Sug}} + R_{\mathrm{ghost}} + R_{\mathrm{self}}$
(which equals $T_{\mathrm{Sug}}$ alone, missing the surviving piece).

The Vol I proof of `prop:QG1-remainder` writes the Q-variation as
a formal sum $T_{\mathrm{Sug}} + R_{\mathrm{ghost}} + R_{\mathrm{self}}$;
this presentation is CORRECT as a pre-canonicalization accounting, but
its physical-level content (after the fermion graded-sort dictated by
the CFG point-splitting $\Theta(t_1-t_2)$ in def:no-cfg) is NOT
$R_{\mathrm{ghost}} + R_{\mathrm{self}} = 0$; the two terms have the
opposite graded canonical form and add to zero, leaving behind
residual pieces that $G_1$ alone does not kill.

### Tests 2-4: all FAIL

- Test 2: $[Q, \eta_1^{(i)}] - R_{\mathrm{ghost}}$ has 21 surviving
  monomials (J-c-cb pieces + 12 new 4-fermion monomials from the
  Jacobi sub-leading action of Q on the cubic ghost structure of
  $\eta_1^{(i)}$).
- Test 3: $[Q, \eta_1^{(ii)}] - R_{\mathrm{self}}$ has 23 surviving
  monomials (analogous pattern).
- Test 4 MAIN: $[Q, \widetilde G_1] - T_{\mathrm{Sug}}$ has 10
  surviving monomials, including 4 genuine 4-fermion pieces
  $(c^h)^2 (\bar c_e)^2$, $(c^h)^2 (\bar c_f)^2$, etc. with
  coefficients $\{2/3, -2/3, 4/3, 4/3\}$.

### The four-fermion residual is structural

The 4-fermion monomials in Test 4 arise from applying Leibniz to the
3-field $\eta_1^{(i)}, \eta_1^{(ii)}$ when $Q_{\mathrm{tot}}$ acts on
$\bar c_c$ or $\bar c_a$ via the ghost-self-coupling term
$f^e{}_{ag}\, \bar c_e\, c^g$ in eq (180). The manuscript's proof
(lines 361-368 of `prop:eta-i-primitive`) claims these terms vanish by
Jacobi:
"Antisymmetrise over $(d,e)$; use $f^a{}_{bc}\,f^c{}_{de}$ summed over
$c$ against the Jacobi identity cyclic sum ... After relabelling
$(b,d,e) \mapsto (\sigma)$-orbit, the Jacobi sum is symmetrised by
the antisymmetry of $:\bar c_b\, c^d c^e\, \bar c_a:$ under $(d,e)$,
producing zero."

The numerical computation shows that this "relabelling + Jacobi
symmetrisation" is NOT a cochain identity: at $\mathfrak{sl}_2$, $k=1$
the 4-fermion monomials
$(c^h, c^h, \bar c_e, \bar c_e)$ and $(c^h, c^h, \bar c_f, \bar c_f)$
arise with coefficient $+4/3$ each in
$[Q, \widetilde G_1] - T_{\mathrm{Sug}}$, and do NOT cancel under
graded fermion sort.

The Jacobi identity $f^a{}_{bc} f^c{}_{de} + \mathrm{cyc} = 0$ IS a
true identity among structure constants; it would kill the
4-fermion contributions IF one were free to perform an
index-relabelling that the fermion order does not support. At the
cochain level with the CFG point-splitting NO, the fermion order is
FIXED (NO is left-associative per def:no-cfg; the associator
Rem:NO-assoc vanishes only upon symmetrisation which in turn
requires the "index relabelling" step that is precisely what fails).

## Verdict

**Vol I `thm:sugawara-antighost-primitive-chain-level` fails at
$\mathfrak{sl}_2$, $k=1$ as a strict chain-level identity.**

The theorem holds on $Q$-cohomology (consistent with Vol II
`thm:E3-topological-km` via Costello-Francis-Gwilliam / Khan-Zeng).
The chain-level strengthening on the original complex is the
frontier item that Vol II `rem:frontier-class-L-strict-chain-level`
correctly identifies as open.

## Heal

### Primary heal (Vol I)

Downgrade `thm:sugawara-antighost-primitive-chain-level` from
`\ClaimStatusProvedHere` to `\ClaimStatusConditional`. Insert an
explicit scope remark identifying what DOES and does NOT hold:
- `prop:QG1-remainder` in the pre-canonicalization accounting: holds.
- $R_{\mathrm{ghost}} + R_{\mathrm{self}} = 0$ on the fermion-graded
  canonical basis: an identity derived numerically in Wave
  V1-Wick-Resolver.
- $[Q, \eta_1^{(i)}] = R_{\mathrm{ghost}}$ strictly on cochains:
  FAILS at $\mathfrak{sl}_2, k=1$; the 4-fermion Jacobi closure
  of the proof (lines 361-368, 408-410) is NOT a cochain identity.
- The chain-level identity $[Q, \widetilde G_1] = T_{\mathrm{Sug}}$
  requires additional structure (either a higher-depth antighost
  tower $\eta_2, \eta_3, \ldots$ or a passage to an ambient where
  the 4-fermion Jacobi closure is exact — e.g., weight-completion
  in the Mittag-Leffler sense of Vol II
  `thm:iterated-sugawara-construction`).

### Ripple healings

Three downstream claims inherit the downgrade:

1. **Vol II `bp_chain_level_strict_platonic.tex:280-281,448-449`**:
   the BP strict-chain-level statement forwards to Vol I
   `thm:sugawara-antighost-primitive-chain-level`. With Vol I
   downgraded, BP strict-chain-level at non-critical level also
   becomes Conditional at the pointwise-cochain level and
   Unconditional only after weight-completion.

2. **Fractional-ghost BP row (Vol II `fm81_fractional_ghost_platonic.tex`)**
   and Monster class-M chain-level row (Vol II
   `chapters/connections/universal_celestial_holography.tex`
   `thm:uch-gravity-chain-level` or equivalent): same forward
   dependency, same downgrade.

3. **CLAUDE.md Theorem Status table**: the "Topologization" row line
   entry asserting "class L strict chain-level via explicit
   $\eta_1^{(i)}, \eta_1^{(ii)}$" is stale and should be rewritten to
   "class L strict chain-level on original complex: OPEN; the
   candidate antighost primitives fail under fermion-graded-sorted
   cochain comparison at $\mathfrak{sl}_2, k=1$; strict chain-level
   holds only after weight-completion via
   Vol II `thm:iterated-sugawara-construction`."

### Vol II frontier remark

Vol II `rem:frontier-class-L-strict-chain-level` is VALIDATED and
should be updated to:
- retain the frontier label;
- add a numerical witness note citing this report:
  "Wave V1-Wick-Resolver at $\mathfrak{sl}_2, k=1$ exhibits
  surviving 4-fermion residual $(c^h)^2(\bar c_{e,f})^2$ with
  coefficient $+4/3$ in $[Q, \widetilde G_1] - T_{\mathrm{Sug}}$;
  see `adversarial_swarm_20260418/attack_heal_v1_wick_resolver_20260418.md`."

## Anti-Patterns Surfaced

AP1541 (sparingly): Fermion-graded-sort cochain canonicalization
mandatory for chain-level BRST identities. The manuscript's informal
"index relabelling + Jacobi" arguments are valid on $Q$-cohomology
but FAIL on the fermion-graded canonical basis of the raw bar
cochain complex. Before asserting strict-chain-level for any Sugawara
/ BRST identity, explicitly canonicalize under fermion graded-sort
and re-verify; Jacobi-closure-by-relabelling does not lift from
$H^\bullet(Q)$ to cochain level.

## Falsification Test

Any future claim that restores Vol I
`thm:sugawara-antighost-primitive-chain-level` must reproduce
coefficient zero on the following monomials at $\mathfrak{sl}_2, k=1$
after fermion-graded canonicalization:

- $(c^h)(c^h)(\bar c_e)(\bar c_e)$: coefficient $+4/3$ in
  $[Q, \widetilde G_1] - T_{\mathrm{Sug}}$ (must become $0$);
- $(c^h)(c^h)(\bar c_f)(\bar c_f)$: coefficient $+4/3$ (must be $0$);
- $(c^e)(c^e)(\bar c_e)(\bar c_f)$: coefficient $+2/3$ (must be $0$);
- $(c^f)(c^f)(\bar c_e)(\bar c_f)$: coefficient $-2/3$ (must be $0$).

Any modification to $\eta_1$ that kills these four specific
coefficients at $\mathfrak{sl}_2, k=1$ is a candidate chain-level
primitive; until such modification is exhibited, the claim remains
Conditional.

## Files Produced

- `/tmp/wick_verify_sl2.py` (raw index-labelled, 343 lines)
- `/tmp/wick_verify_sl2_v2.py` (fermion-graded canonicalization, 368 lines)
- `/tmp/wick_verify_sl2_v3.py` (R_ghost + R_self identity, 145 lines)
- this report

## Deliverables (per AP316)

Patch file for Vol I + Vol II heals at
`/Users/raeez/chiral-bar-cobar/adversarial_swarm_20260418/patches/v1_wick_resolver.patch`.

Apply with:
```
cd /Users/raeez/chiral-bar-cobar
git apply adversarial_swarm_20260418/patches/v1_wick_resolver.patch
cd /Users/raeez/chiral-bar-cobar-vol2
git apply ../chiral-bar-cobar/adversarial_swarm_20260418/patches/v1_wick_resolver_vol2.patch
```

No commits created in this session.
