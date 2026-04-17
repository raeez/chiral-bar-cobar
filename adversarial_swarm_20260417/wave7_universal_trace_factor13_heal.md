# Wave-7 heal: AP-UTI-1 factor-13 anomaly

Author: Raeez Lorgat.
Date: 2026-04-17.
Scope: Vol III `chapters/connections/bar_cobar_bridge.tex` remark
`rem:universal-trace-identity-numerical` (and two upstream sites in the
same chapter) flagged by the Wave-6 focused Phi-trace re-attack agent as
AP-UTI-1, left unhealed. This note executes the heal, propagates the
correction, and records the AP5 sweep.

## 1. Diagnosis

### 1.1 Provenance

The Wave-6 note
`adversarial_swarm_20260417/wave6_phi_trace_identity_focused_reattack.md`
line 70 flagged:

> `rem:universal-trace-identity-numerical` (bar_cobar_bridge.tex L1714-1735)
> claims `K(Vir_{c=24}) = 26 = 13 * 2 = 13 * kappa_{BKM}(K3)`.  ...  The
> factor 13 is unmotivated; the correct ratio is 26/5 = 5.2, not 13.

The agent deferred heal to Wave 7 (scope skip). The present note
executes the heal.

### 1.2 Canonical numerical data (established elsewhere)

- **Vol I universal conductor.**
  `K(Vir_c) = c + c^!` on the Virasoro self-dual line `c + c^! = 26`.
  At `c = 24`: `c^! = 2`, `K(Vir_{c=24}) = 26`. At `c = 13` (self-dual
  point): `K = 13 + 13 = 26`. Source: Vol I
  `universal_conductor_K_platonic.tex:795-821`.

- **Vol III BKM weight at K3.**
  `kappa_{BKM}(K3) = c_1(0)/2 = 5` via Gritsenko's paramodular form
  `Delta_5` of weight 5 (equivalently, Igusa's `Phi_{10}` of weight 10
  with the factor of 1/2 in the Borcherds exponent). Source:
  Vol III `chapters/theory/phi_universal_trace_platonic.tex:161-184`,
  `chapters/examples/cy_d_kappa_stratification.tex:1147-1232`,
  `chapters/examples/cy_c_six_routes_generator_level_platonic.tex:423,475,490`.

- **Ratio.** `K(Vir_{c=24}) / kappa_{BKM}(K3) = 26 / 5 = 5.2`, which
  is not an integer and has no structural provenance.

### 1.3 The three local defects in `bar_cobar_bridge.tex`

Three sites emitted the wrong arithmetic:

1. **Line 925** (section intro):
   `kappa_{BKM}(K3) = 2` -- WRONG; should be 5.

2. **Line 957** (Conjecture trailing prose):
   `kappa_{BKM}(K3) = 2` -- WRONG; should be 5.

3. **Line 1719** (`rem:universal-trace-identity-numerical`):
   `K(Vir_{c=24}) = 26 = 13 * 2 = 13 * kappa_{BKM}(K3)` plus a
   derivation of the factor-13 as "Virasoro central-charge level shift
   at c = 13" -- WRONG; the claimed equation combines a correct left
   side (26) with two wrong right sides (the factor of 2 is wrong; the
   factor 13 has no motivation; the ratio 26/5 is not 13).

The underlying confusion chains the `c + c^! = 26` Virasoro self-dual
line (value of K), the self-dual point `c = 13` (a different numerical
coincidence), and the kappa_BKM scalar (which takes value 5, not 2).
Three independent invariants got multiplied into a false "13 * 2 = 26"
identity.

### 1.4 What the Universal Trace Identity actually says

`phi_universal_trace_platonic.tex:234-244` (`rem:factor-13-caveat`)
already states the correct reading:

> It is tempting to seek a constant ratio `K / kappa_{BKM}` along the
> Virasoro self-dual line at `c = 13` ...: there `K = c + c^! = 26` and
> `kappa_{BKM}(K3) = 5`, with ratio 26/5; this is not the Virasoro
> central charge 13, and no heuristic derivation produces the factor 13
> as a structural ratio. The correct structural content is: the two
> scalars live on two branches of the bridge, related by the
> Phi-pushforward of clause (iii), not by a scalar rescaling.

The Universal Trace Identity is an intertwining of two reflections
`(K_A, B_X)` on one universal centre, NOT a scalar equality; the
Phi-pushforward bridge is `B_X = Phi^Borch_*(K_{Phi^{-1}(X)})` at the
level of operators. Scalar traces of the two reflections are genuinely
different invariants and no ratio is predicted.

## 2. Healing edits (surgical)

All three edits in `~/calabi-yau-quantum-groups/chapters/connections/bar_cobar_bridge.tex`.

### 2.1 Section intro (line 925)

Before: "`kappa_{BKM}(K3) = 2` ... both interpretable as conductors in
their respective settings) suggests a structural unification."

After: explicit values `K(Vir_{c=24}) = c + c^! = 24 + 2 = 26`,
`kappa_{BKM}(K3) = c_1(0)/2 = 5` via Gritsenko Delta_5; explicit
statement that "the scalars do not coincide, and no structural
rescaling `K = lambda * kappa_{BKM}` holds"; the structural unification
is framed as intertwining of reflections, not scalar equality.

### 2.2 Conjecture trailing prose (line 957)

Before: "The numerical coincidences across the K3 and quintic cases
(... `kappa_{BKM}(K3) = 2` ...) become structural under this conjecture:
each numerical invariant is a different trace of the same universal
Koszul/Borcherds reflection."

After: "The numerical values ... are not required to coincide or to sit
in any scalar ratio: each is a trace of a different reflection on the
same universal centre, and the conjectural content is that the
reflections intertwine under Phi-pushforward, not that the traces
rescale into one another." Correct values stated: `K(Vir_{c=24}) = 26`,
`kappa_{BKM}(K3) = 5` via Gritsenko Delta_5, `K(BP) = 196`.

### 2.3 `rem:universal-trace-identity-numerical` (line 1714-1735)

Full rewrite. Before: a two-paragraph remark whose load-bearing sentence
was `K(Vir_{c=24}) = 26 = 13 * 2 = 13 * kappa_{BKM}(K3)` followed by an
attempt to derive the factor-13 as a level shift.

After: a two-paragraph remark whose load-bearing sentence is the
disclaimer that the conjecture does not predict a scalar equality or
rescaling, followed by the correct values
`K(Vir_{c=24}) = c + c^! = 24 + 2 = 26`,
`kappa_{BKM}(K3) = c_1(0)/2 = 5` via Gritsenko Delta_5, and the ratio
`26/5` stated explicitly as non-integer with no structural derivation.
Cross-reference to `phi_universal_trace_platonic.tex`
`rem:factor-13-caveat` preserved. The non-K3-fibered clause is
retained (regularised Bruinier-Funke lift) with a corrected closing
statement that the regularised kappa_{BKM}^{reg} is likewise not in
scalar ratio.

## 3. AP5 propagation sweep

Grepped across all three volumes for residual occurrences of the
factor-13 claim and the wrong `kappa_{BKM}(K3) = 2` value:

- `~/calabi-yau-quantum-groups`: `13 cdot kappa_{BKM}`,
  `kappa_{BKM}(K3) = 2`, `K(Vir_{c=24}) = 26 = 13` -- all 0 hits after
  the heal.
- `~/chiral-bar-cobar`: no occurrences other than the Wave-6 reattack
  note (a swarm note flagging the issue, not typeset prose).
- `~/chiral-bar-cobar-vol2`: no occurrences.
- `phi_universal_trace_platonic.tex` `rem:factor-13-caveat`: already
  correct; no edit needed.
- Vol III `CLAUDE.md`: no typeset occurrences of the factor 13 bound to
  the Universal Trace Identity.
- Vol III `FRONTIER.md`: no occurrences.

## 4. Constitutional hygiene

- HZ-7 (Vol III bare kappa): all edits use `\kappa_{\mathrm{BKM}}` or
  `\kappa_{\mathrm{ch}}` throughout. No bare kappa introduced. The
  existing bare-kappa violations in unrelated lines (319, 907, 919)
  are pre-existing and out of scope for this heal.
- AP/HZ in typeset prose: none introduced. The one AP-label reference
  in the edit prose is the cross-reference to the Platonic chapter's
  `rem:factor-13-caveat`, which describes a mathematical pattern by its
  mathematical content ("no scalar coincidence," "intertwining of
  reflections") rather than by AP index.

## 5. Verification paths

Three independent verification paths for the post-heal numerics:

- **[DC] direct computation.** `c + c^! = 26` at `c = 24`, `c^! = 2`
  gives `K = 26`. `c_1(0) = 10` for Igusa `Phi_{10}`; halving gives
  `kappa_{BKM} = 5`. Ratio `26/5`, non-integer.
- **[LT] literature.** Gritsenko 1996, 2002 paramodular form `Delta_5`;
  Borcherds 1998 weight theorem; programme's
  `chapters/theory/phi_universal_trace_platonic.tex:161-184`,
  `chapters/examples/cy_d_kappa_stratification.tex:1147-1232`.
- **[CF] cross-family.** Cross-check against `K3/Z_N` orbifold series
  `kappa_{BKM}(X_N) = c_N(0)/2 in {5,4,3,2,2,1,1,1}` at N=1,...,8,
  consistent with N=1 giving 5.

## 6. Files modified

- `~/calabi-yau-quantum-groups/chapters/connections/bar_cobar_bridge.tex`
  (three surgical edits at lines 920-928, 955-961, 1714-1735).

No edits needed to `phi_universal_trace_platonic.tex` (already correct)
or Vol III `CLAUDE.md` (no propagation).

No commit performed (per invocation instruction).
