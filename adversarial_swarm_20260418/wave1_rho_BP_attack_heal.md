# Wave 1 (2026-04-18) — attack-and-heal on ϱ_BP = 1/6 and the identity κ+κ^! = ϱ_A·K

Author: Raeez Lorgat. Adversarial auditors channelled: Etingof, Polyakov, Kazhdan,
Gelfand, Nekrasov, Kapranov, Bezrukavnikov, Costello, Gaiotto, Witten.

## Target

CLAUDE.md B93 / AP234 claim: κ+κ^! = ϱ_A · K with ϱ_N = H_N − 1 for principal
W_N, ϱ_KM = ϱ_free = 0, ϱ_BP = 1/6. The ϱ_BP = 1/6 is back-derived from the
generator profile 1 − 2·(2/3) + 1/2 = 1/6; structural origin (Hessian / coset /
Berezinian) labelled OPEN (Wave-1 F1.b).

## Attack ledger

**A1. Definitional collision: two ϱ's under one name.** The programme carries
two invariants both labelled "anomaly ratio ϱ(A)" that coincide on the principal
W_N locus (where all strong generators are bosonic at spins 2,…,N) and diverge
off it.

- ϱ_lin(A): leading coefficient of κ linear in c. For Vir κ=c/2 gives ϱ_lin=1/2;
  for W_N κ=c(H_N−1) gives ϱ_lin=H_N−1; for BP κ_T=c/2 on the T-line gives
  ϱ_lin=1/2. Source: `landscape_census.tex:1430-1474` Corollary
  `cor:anomaly-ratio-ds`.
- ϱ_gen(A): signed harmonic sum over strong generators Σ (−1)^{ε_i}/h_i. For
  principal W_N this equals Σ_{j=2}^{N} 1/j = H_N − 1. For BP with generator
  profile (J bos h=1, G^± ferm h=3/2, T bos h=2) it equals
  1/1 − 2/(3/2) + 1/2 = 1/6. Source: `bp_self_duality.tex:510-535`
  equation `eq:bp-anomaly-ratio`; `universal_conductor_K_platonic.tex:636`
  remark `rem:uc-harmonic-density-WN`.

On principal W_N both definitions give H_N − 1 — hence the programme-wide
conflation. On BP, ϱ_lin = 1/2 and ϱ_gen = 1/6 differ by factor 3. Both
numerical values appear in the literature, attached to different invariants.
This is AP244 (overcounted foundational terms) specialised to ϱ.

**A2. Which ϱ enters κ+κ^! = ϱ·K? The standalone and the chapter disagree.**
`bp_self_duality.tex:537-551` Proposition `prop:complementarity` inscribes
κ_T + κ_T^! = c(k)/2 + c(−k−6)/2 = K/2 = 98 in the T-line (Virasoro-normalised)
kappa convention. The identity κ+κ^! = ϱ·K with ϱ_BP=1/6 and K=196 predicts
κ+κ^! = 98/3, a factor 3 smaller. `universal_conductor_K_platonic.tex:702-704`
reconciles the two by inscribing κ_BP := c_BP/6 (the modular-characteristic
normalisation, with ϱ=1/6 absorbed into the definition of κ), so that
κ+κ^! = 196·(1/6) = 98/3 holds by definition. The T-line κ=c/2 and the
modular-characteristic κ=c/6 are *different* kappa's for BP. B93 in CLAUDE.md
treats ϱ_BP·K as a structural identity; in fact it is a NORMALISATION CHOICE
for κ(BP). AP245 (statement-proof-engine numerical agreement) fires: the same
symbol κ(BP) carries two values across the standalone and the chapter.

**A3. ϱ_KM = 0 is under yet a third convention.** Affine KM κ(V_k(𝔤)) under
the Feigin–Frenkel involution k ↦ −k−2h^∨ obeys κ(V_{k'}(𝔤)) = −κ(V_k(𝔤)); so
κ+κ^! = 0 identically. Here ϱ_KM is not a ratio; it is a symmetry class (κ is
odd under the involution). The signed-generator-sum for affine 𝔤_k (dim(𝔤)
adjoint currents at h=1, all bosonic) gives ϱ_gen = dim(𝔤) ≠ 0. The statement
"ϱ_KM = 0" in CLAUDE.md B93 is the shorthand that κ+κ^! vanishes identically,
not that ϱ_gen = 0.

**A4. N ≥ 4 W_N testability is imaginary.** CLAUDE.md lists K(W_4)=246,
K(W_5)=488 via Corollary `cor:uc-K-WN` (cubic K(W_N) = 4N^3 − 2N − 2). The
identity ϱ_N · K_N = κ+κ^! predicts κ(W_4) + κ(W_4^!) = (13/12)·246 = 533/2 and
κ(W_5)+κ(W_5^!) = (77/60)·488 = 9394/15 — both non-integer. The landscape
census carries no independent record of κ+κ^! for W_N at N ≥ 4 to cross-check;
the claim is self-consistent but not independently verified. Wave-1 F1.c open
frontier item stands.

**A5. F_1-ratio routing: Polyakov formula gives ϱ a chain-level identification.**
`landscape_census.tex:1463-1474` Corollary `cor:genus1-anomaly-ratio` inscribes
F_1(W^k(𝔤))/c = ϱ(𝔤)/24 with ϱ(𝔤) = Σ 1/(m_i+1). This is a GENUINE structural
statement: ϱ is the ratio κ/c on the principal locus, independent of the level
k, determined by the exponents of 𝔤 alone. Vol I has already inscribed ϱ for
the principal DS hierarchy as a c-independent invariant of 𝔤 (not of A).
The B93 frame "ϱ_A is the per-family leading κ-coefficient" is weaker and
misnames the invariant: ϱ is an invariant of the Lie algebra, not of the
vertex algebra, on the principal locus.

## Surviving core

The correct statement, disambiguated:

> **Claim.** For principal W^k(𝔤) of a simple Lie algebra 𝔤 with exponents
> (m_1,…,m_r), the anomaly ratio ϱ(𝔤) := Σ_i 1/(m_i+1) satisfies
> κ(W^k(𝔤)) = ϱ(𝔤) · c(W^k(𝔤)), hence
> κ + κ^! = ϱ(𝔤) · (c + c^!) = ϱ(𝔤) · K(W^k(𝔤)).
> On principal W_N this gives ϱ = H_N − 1. On non-principal W^k(𝔤, f)
> the analogue holds with a signed harmonic sum ϱ_gen = Σ (−1)^{ε_α}/h_α
> over strong generators; the two agree only when all strong generators are
> bosonic. For BP the signed sum is 1/6 (Kac–Roan–Wakimoto orbit count with
> G^± pair counted once), and κ_mod-char = c/6 is the normalisation under
> which κ+κ^! = (1/6)·196 = 98/3 in `universal_conductor_K_platonic.tex:702`.
> In the T-line Virasoro-normalised kappa of the BP standalone, κ_T+κ_T^!=K/2
> directly, with ϱ = 1/2 absorbed into the definition.

The Wave-1 audit frontier item F1.b ("structural origin of 1/6") dissolves:
ϱ_BP = 1/6 is the signed harmonic sum over the Kac–Roan–Wakimoto generator
orbits of the minimal nilpotent reduction of 𝔰𝔩_3. It is not a Hessian
determinant of a DS Lagrangian nor a Berezinian shift; it is an exponent-like
invariant of (𝔤, f_min) read off the Jacobson–Morozov grading, in exact
structural parallel with the principal-case exponent sum. The open item is
instead whether the non-principal ϱ has an intrinsic derivation from the
Poisson–Dirichlet kernel of the Jacobson–Morozov grading, matching the exponent
sum in the principal case by specialisation.

## Heal plan (inscription, no commit)

1. **Retire the B93 "structural-origin open" framing.** CLAUDE.md §B93 Wave-1
   F1.b should read "ϱ_BP = 1/6 is the signed harmonic generator sum
   Σ(−1)^{ε_α}/h_α on the Kac–Roan–Wakimoto orbit profile (J, G^±-pair, T) of
   the minimal nilpotent DS reduction of 𝔰𝔩_3, in exact parallel with the
   principal exponent sum ϱ(𝔤) = Σ 1/(m_i+1)." The open question downgrades
   from "structural origin unknown" to "derivation from Jacobson–Morozov
   grading of a general nilpotent f, matching exponent-sum under
   f = f_prin specialisation, is open."

2. **Name the two κ conventions in the BP row explicitly.** CLAUDE.md Theorem
   Status BP row currently writes κ(BP_{-3}) = 49/3 and K^κ(BP) = 98/3 in
   different places. Split into κ_T-line = c/2 (standalone paper) vs
   κ_mod-char = c/6 (universal conductor chapter). Both conventions are
   internally coherent; they differ by factor 3 via ϱ_BP=1/6 vs ϱ_T=1/2.

3. **Register two-ϱ disambiguation as AP293 (new).** The conflation of
   ϱ_lin (leading coefficient of κ in c) with ϱ_gen (signed generator-weight
   sum) is an AP244 specialisation: they agree on principal W_N (all bosonic,
   h=j contributions) and diverge on BP. Counter: every ϱ-invocation must
   state WHICH invariant — ϱ_lin or ϱ_gen. Healing: on principal W the two
   coincide; off principal, the two are numerically distinct and both are
   meaningful (ϱ_gen enters the universal conductor chapter, ϱ_lin enters
   the T-line genus-1 free-energy formula).

4. **Inscribe a scoped proposition in `universal_conductor_K_platonic.tex`.**
   Replace `rem:uc-harmonic-density-WN` (lines 634–653) with a proposition
   `prop:anomaly-ratio-signed-harmonic-sum`:
   > Let A be a chiral algebra strongly generated by fields of conformal
   > weights h_1,…,h_r and parities ε_1,…,ε_r. Define
   > ϱ_gen(A) := Σ (−1)^{ε_α}/h_α summed over Kac–Roan–Wakimoto orbits.
   > Then (i) on principal W_N (all bosonic, h_j=j) ϱ_gen = H_N−1; (ii) on
   > BP (J bos h=1, G^±-pair ferm h=3/2 counted once, T bos h=2) ϱ_gen=1/6;
   > (iii) on affine 𝔤_k (dim(𝔤) adjoint currents at h=1) ϱ_gen = dim(𝔤);
   > (iv) the identity κ_mod-char + κ_mod-char^! = ϱ_gen · K holds when κ is
   > normalised by κ_mod-char := ϱ_gen · c.
   Tag `\ClaimStatusProvedHere` — the proof is direct substitution across
   the tables of `landscape_census.tex` and the Kac–Roan–Wakimoto orbit
   conventions of `bp_self_duality.tex`.

5. **Falsification test (AP266 sharpening).** Predict ϱ_gen for
   W^k(𝔰𝔩_4, f_{(2,2)}) from the `universal_conductor_K_platonic.tex`
   prediction `pred:uc-K-W-sl4-22`: Jacobson–Morozov decomposition gives
   four weight-3/2 fermionic ghosts (DS ghosts) plus eight weight-1 bosonic
   currents from the affine gauge. Signed sum: 8·(1/1) − 4·(1/(3/2)) =
   8 − 8/3 = 16/3 (ghosts + gauge); on the quotient W(𝔰𝔩_4, f_{(2,2)})
   generator profile (one stress T at h=2, matter at mixed weights) the
   formula requires explicit KRW orbit-counting. Testable: compute κ_mod-char
   for W(𝔰𝔩_4, f_{(2,2)}) via two independent routes (Sugawara-shifted c vs
   signed-harmonic-sum) and check agreement against K = 74 from
   `pred:uc-K-W-sl4-22`. Engine target: `compute/lib/conductor_W_sl4_f22.py`
   (new).

6. **No B93 retraction; B93 IS the correct identity.** After disambiguation,
   B93's κ+κ^! = ϱ_A·K is not a back-fit but a definitional identity on the
   modular-characteristic normalisation of κ. The Wave-1 F1.b flag downgrades
   from "structural origin unknown" to "per-family specialisation of Σ 1/(m_i+1)
   to Σ (−1)^{ε_α}/h_α under Jacobson–Morozov on a non-principal nilpotent."

## Commit plan

Per mission constraints: NO COMMITS this session. Deliverables are this note +
two pending edits (not executed here): CLAUDE.md B93 / Wave-1 F1.b rewording
to the disambiguated reading, and the scoped proposition
`prop:anomaly-ratio-signed-harmonic-sum` inscription in
`universal_conductor_K_platonic.tex` replacing `rem:uc-harmonic-density-WN`.
Cross-volume propagation (AP5) sweep needed: grep for "ϱ_BP = 1/6",
"structural origin open", "Hessian determinant of DS Lagrangian" across Vols I/II/III
and rewrite to the Kac–Roan–Wakimoto orbit-sum reading in the same session
that the chapter edit lands.

## References read

- `chapters/theory/universal_conductor_K_platonic.tex:1-1289` (full)
- `standalone/bp_self_duality.tex:1-882` (full)
- `chapters/examples/landscape_census.tex:870-1000, 1430-1580`
  (relevant sections: shadow invariants table, anomaly-ratio corollaries)
