# Wave-10 kappa_ch(K3 x E) AP289 residual sweep

Date: 2026-04-18
Scope: Vol III test files flagged by Wave-9 a34b5d53 triage agent as
"two legacy kappa_ch additive (kappa_ch(K3 x E) = 3) sites awaiting
Wave-10 propagation sweep".

## Route A / Route B disambiguation (AP234 collision)

On the programme's working locus, two distinct invariants share the
symbol `kappa_ch` and coexist legitimately:

- Route A (Hodge supertrace, Kunneth-multiplicative):
  kappa_ch(X x Y) = Xi(X) * Xi(Y) with Xi(X) = sum_q (-1)^q h^{0,q}(X).
  Canonical Phi_d functor value. kappa_ch(K3 x E) = 2 * 0 = 0.
  Source of truth: cy_d_kappa_stratification.tex:411-426.

- Route B (Heisenberg level / free-boson rank, AP-CY55 algebraisation
  invariant): kappa_ch(E) := 1 via Heisenberg k = 1; additive under
  product of free-boson constructions. kappa_ch(K3 x E) = 2 + 1 = 3.

A site asserting kappa_ch(K3 x E) = 3 is:
- BUG if it names Route A (Hodge supertrace / Kunneth / Phi_d functor)
  in prose while computing Route B value.
- LEGITIMATE if the surrounding docstring names Route B explicitly
  (additivity, Heisenberg level, AP-CY55) and does NOT claim
  route-invariance.

## Per-site classification

### Site 1: compute/tests/test_twisted_holography_k3e.py:167-173

- Classification: LEGITIMATE (Route B)
- Evidence: file docstring :26 "kappa_ch(K3) = 2  # DC: chi(O_{K3})";
  test docstring :168 names "additivity"; constants imported from
  compute/lib/twisted_holography_k3e.py where the algebraisation
  convention is established.
- Heal applied: inserted Route A / Route B scope-qualifier comment in
  the test docstring naming both routes, the AP234 collision, and the
  canonical Phi_d functor value 0 with pointer to
  cy_d_kappa_stratification.tex:411-426. No numerical value changed.

### Site 2: compute/tests/test_hyperkahler_anchored_fixed_point.py:4280-4325

- Classification: LEGITIMATE (Route B)
- Evidence: class docstring :4283 "kappa_ch(K3 x E) = 3 (additive:
  2 + 1)"; decorator at :4294 "kappa_ch(E) = 1 by convention
  (algebraisation invariant, AP-CY55)"; test body :4323-4325
  explicitly recapitulates Route B path.
- Heal applied: expanded class docstring with AP234 disambiguation
  paragraph naming Route A (Kunneth-multiplicative, Phi_d value 0) vs
  Route B (Heisenberg-level additive, value 3), pointer to
  cy_d_kappa_stratification.tex:411-426, and explicit statement that
  the proposition operates under Route B while Route A coexists as
  the supertrace invariant of the Phi_d image. No numerical value
  changed.

Both sites now carry the AP234 disambiguation the Wave-9 triage
requested; no numerical retractions were warranted.

## Programme-wide sweep (chapters/ + standalone/ + appendices/)

Grep run across Vol III for:
  kappa_ch.*K3.*E.*=.*3
  kappa.*K3.*times.*E.*=.*3
  kappa_ch\(K3.*E\).*=.*3
  kappa_ch.*K3 x E.*=.*3

Result: 98 file matches on broad pattern (most are Xi-supertrace /
kappa_BKM = 5 context, incidental K3xE mentions). No chapter-level
residual bug surfaced on targeted grep of the precise
`kappa_ch(K3 x E) = 3` literal form.

Note: Wave-4 kappa(K3 x E) agent flagged ~30 chapter-level sites
deferred for a dedicated campaign. A full prose-level audit is out of
scope for this targeted heal; the authoritative Route A inscription
at cy_d_kappa_stratification.tex:411-426 now serves as the canonical
disambiguation point that consumers can cite. Remaining Vol III
chapter sites using bare "kappa_ch(K3 x E) = 3" in prose without
Route B qualifier remain candidate items for the dedicated campaign.

## Residuals / open

1. Chapter-level prose audit (Wave-4 flagged ~30 sites) still pending
   as dedicated campaign. Recommend a future wave rectify sweep
   covering: e1_chiral_algebras.tex, quantum_chiral_algebras.tex,
   modular_koszul_bridge.tex, k3e_cy3_programme.tex,
   cy_to_chiral.tex, k3e_bkm_chapter.tex. Discipline: each site must
   either (a) qualify "(Route B, Heisenberg level)" or (b) be replaced
   by the Route A value 0 with pointer to the canonical Phi_d
   stratification.

2. CLAUDE.md should receive a HOT ZONE HZ-entry or AP289 expansion
   registering the Route A / Route B collision as a permanent
   discipline pattern for Vol III kappa_ch(X x Y) edits. Current
   AP289 text covers Xi multiplicativity generically; adding the
   Route A / Route B naming convention would make the
   Heisenberg-level vs Phi_d-functor distinction first-class.

## Commit plan

Two Python docstring edits, comment-only, no numerical change.
Targeted-heal agents do not commit per Wave protocol. Parent session
bundles into next Wave-10 propagation commit batch. No build impact
(no .tex touched).
