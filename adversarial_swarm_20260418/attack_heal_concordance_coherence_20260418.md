# Concordance coherence audit (2026-04-18)

Author: Raeez Lorgat.

Target: `chapters/connections/concordance.tex` (11,491 lines).

Scope: spot-check concordance.tex alignment with 2026-04-18 session heals recorded in CLAUDE.md theorem-status table and Wave-15/16/17/18/MC4-swarm/N2-SCA/Elliptic/6d-hCS attack-and-heal notes. Concordance is epistemic tier 5 (above CLAUDE.md tier 6 and memory tier 7) per the Beilinson hierarchy; stale concordance statements propagate into the manuscript with elevated authority, so coherence is load-bearing.

## Summary

Concordance.tex is broadly coherent with the programme's five-theorem status (A, B, C, D, H table at lines 29-83 matches the healed scope). One load-bearing contradiction with the 2026-04-18 MC4-swarm heal is present. Several downstream items from 2026-04-18 heals have no concordance footprint (acceptable: concordance is selective, not exhaustive). Programme-identity preamble (lines 1-20) is intact and does not need edits.

## Findings by heal item

### F1. MC4^0 advertised "unconditionally solved" — CONTRADICTION with AP421 heal

**Loci:** `concordance.tex:1949-1968` (MC4 passage).

**Concordance text:**

> "Splits into MC4^+ (positive towers) and MC4^0 (resonant). MC4^+ is unconditionally solved by weightwise stabilization... MC4^0 concerns algebras with finite resonance rank (Virasoro, non-quadratic W_N) and is proved on the transferred split surface of Theorems thm:resonance-filtered-bar-cobar and thm:platonic-completion... The general theorem (strong completion-tower theorem) is proved unconditionally."

**CLAUDE.md post-heal status (MC1-4 row):**

> "MC4^+ UNCONDITIONAL on classes G/L/C via thm:completed-bar-cobar-strong; MC4^0 CONJECTURAL (2026-04-18 Wave-MC4-swarm, AP421) at generic parameters for class M principal."

**Verdict:** Concordance overadvertises MC4^0 as "proved on the transferred split surface" while the 2026-04-18 swarm established via AP421 that the class M principal case (Virasoro, non-quadratic W_N — exactly the families concordance names) is CONJECTURAL at generic parameters. The prior UNCONDITIONAL label was retracted because the Wakimoto-SDR mechanism was fabricated (AP269) and the Feigin-Frenkel screening route is actively obstructed by `prop:ff-screening-coproduct-obstruction` at `ordered_associative_chiral_kd.tex:10176-10297` with obstruction class $(\Psi-1)/\Psi \in H^1_{ch}$. Concordance is in reverse drift (AP271, CLAUDE.md-vs-manuscript inversion) — but here the drift is concordance vs manuscript retraction, not CLAUDE.md vs manuscript. Concordance carries the stale unconditional advertisement.

**Healing recommendation (not applied this session — inscription would require a careful concordance Edit with per-family scope qualifiers):**

Replace lines 1949-1968 with a split:

1. MC4^+ UNCONDITIONAL on classes G/L/C (bounded-degree conformal/fermion-number filtrations).
2. MC4^0 CONJECTURAL at generic parameters for class M principal; inscribed as `conj:n4-mc4-zero-generic-parameters` at `standalone/N4_mc4_completion.tex`. Sharpened obstruction: `prop:mc4-zero-wakimoto-sdr-obstruction` records the $(\Psi-1)/\Psi$ chiral-coproduct cocycle class matching `thm:miura-cross-universality`.
3. The named theorems `thm:resonance-filtered-bar-cobar` and `thm:platonic-completion` cover the MC4^+ completion-tower package (classes G/L/C); they do NOT establish MC4^0 for class M principal.

### F2. Theorem A modular-family advertising at concordance:286-290 — COHERENT with current scope caveat, but slightly optimistic

**Locus:** `concordance.tex:286-290`.

**Concordance text:**

> "The adjunction holds for all Koszul chiral algebras at all genera. Inversion is genus 0 unconditional; at g ≥ 1 it is unconditional on the CFT-type standard landscape except integer-spin betagamma by PBW propagation, and otherwise conditional on axiom MK:modular."

**CLAUDE.md post-audit status (Theorem A row):**

> "PROVED unconditional on a FIXED SMOOTH CURVE X... Modular-family extension over M̄_{g,n} including boundary is CONDITIONAL on two uninscribed ingredients (Francis-Gaitsgory six-functor base-change; Mok25 logarithmic factorization-gluing at the nodal boundary)."

**Verdict:** Concordance's "conditional on axiom MK:modular" formulation is compatible with the CLAUDE.md conditional scope: an axiomatic placeholder covers the two uninscribed ingredients (GR17 + Mok25). Concordance is tolerant. The concordance genus-0 unconditional + genus ≥ 1 conditional-on-axiom statement is coherent but the dependency on GR17 + Mok25 is not named at this passage. Not a correction-grade violation.

### F3. Theorem H concordance entry (line 71-82) — COHERENT with current scope

Concordance restates Theorem H as degrees {0,1,2} + duality shift + degree-≤2 Hilbert polynomial + ChirHoch^1(V_k(g)) ≅ g + FM collision-depth SS collapse. All clauses match the CLAUDE.md Theorem H row and the 2026-04-18 attack-heal notes (`prop:chirhoch1-affine-km`, `thm:main-koszul-hoch`, `thm:hochschild-polynomial-growth` all resolve). The critical-level k=-h^v exclusion is not stated here but is load-bearing in the source chapter; this is tolerable for concordance (the passage is selective, not exhaustive).

### F4. Items absent from concordance — acceptable omission or healing gap?

The following 2026-04-18 heal items produced no grep hit in concordance.tex:

- **Chiral CE B(U^ch(L)) = CE_*(L)** — zero hits for `Chevalley.Eilenberg`, `U\^\{ch\}`, `chiral.Chevalley`, `ChirCE`. This is inscribed in Vol I `standalone/ordered_chiral_homology.tex` and supporting Vol II chapters. Acceptable omission (concordance does not enumerate Quillen homology identifications); no healing required unless a later wave elevates the identification to main-theorem status.
- **V^natural E_3-topological** — the `thm:v-natural-e3-topological` result is present at concordance at lines 375, 3038-3051, 3237-3239 via the $V^\natural$ modular-characteristic row ($\kappa = 12$, class M). The specific Wave-18 AP287 attribution-discipline note (cross-volume `thm:uhf-monster-orbifold-bv-anomaly-vanishes` attribution to Vol II) is not reflected; the passage reports $\kappa$ and Niemeier discrimination without the E_3 identification clause. Acceptable omission at concordance tier (the E_3 clause lives in `chiral_moonshine_unified.tex`); no healing required at this pass.
- **prop:verlinde-from-ordered** (Wave-Verlinde audit 2026-04-18) — concordance mentions Verlinde at lines 3972, 4892-4913 as a smoking-gun test for bar-cohomology recovery at $\widehat{\mathfrak{sl}}_{2,k}$. The recent downgrade from `\ClaimStatusProvedHere` to `\ClaimStatusProvedElsewhere` with honest scope remark `rem:verlinde-from-ordered-scope` is downstream of concordance (concordance uses Verlinde as a probe, not as a proved bridge). No healing required.
- **thm:chd-ds-hochschild** and **thm:uch-gravity-chain-level** — these live in Vol II (`chapters/theory/chiral_higher_deligne.tex`, `chapters/connections/universal_celestial_holography.tex`). Vol I concordance has no direct reference. Acceptable cross-volume omission; Vol II carries its own concordance-equivalent material.

### F5. Programme-identity preamble (lines 1-20) — COHERENT

The preamble states that concordance governs when chapters disagree, that every claim is presumed false until tagged, and that omission is itself a verdict. All three clauses are consistent with the Constitutional Trust Warning at CLAUDE.md top. No edit required.

### F6. Five-theorem status table (lines 29-83) — COHERENT

Row-by-row check:
- **A:** `\ClaimStatusProvedHere` — matches CLAUDE.md fixed-smooth-curve scope (modular-family conditional reading is compatible via axiom MK:modular).
- **B:** `\ClaimStatusProvedHere` on Koszul locus; off-locus coderived. Matches CLAUDE.md weight-completed coderived scope.
- **C:** C0/C1 ProvedHere; C2 Conditional. Matches CLAUDE.md post-Wave-14 honest accounting.
- **D:** ProvedHere. CLAUDE.md is more honest about the $g \geq 3$ scalar-diagonal hypothesis + Faber $\lambda_g$-conjecture conditional; concordance does not flag these. Sub-optimal but within the spirit of the concordance (uniform-weight lane is declared; multi-weight cross-channel term is named).
- **H:** ProvedHere on Koszul locus at generic level. Matches CLAUDE.md.

No status-tag drift at the table.

## Net verdict

One load-bearing contradiction (F1, MC4^0 UNCONDITIONAL vs AP421 CONJECTURAL-at-generic). All other checked items are either coherent, acceptable omission, or within tolerable concordance-tier generality. Concordance is not systematically stale; the MC4 passage is the outlier and likely was inscribed during the Wave-16 closure narrative before the 2026-04-18 fabrication audit.

## Recommended next action

Inscribe a 4-6 line Edit at `concordance.tex:1949-1968` splitting MC4 into MC4^+ UNCONDITIONAL (classes G/L/C) + MC4^0 CONJECTURAL at generic parameters for class M principal, with explicit pointer to `conj:n4-mc4-zero-generic-parameters` and `prop:mc4-zero-wakimoto-sdr-obstruction`. Defer to a follow-up worker; this wave is diagnosis-only.

## AP registrations

Per AP314 (inscription-rate discipline), this session registers TWO new APs.

### AP2181 (Concordance-tier stale closure narrative survives fabrication audit).

When an adversarial audit retracts a CLAUDE.md UNCONDITIONAL claim (typically via AP269 SDR-formula fabrication or AP266 sharpened-obstruction heal), the retraction propagates to the manuscript standalone and chapter level but concordance.tex (epistemic tier 5, above CLAUDE.md tier 6) is NOT updated in the same wave. A reader consulting concordance as the governing document sees the pre-retraction UNCONDITIONAL language; a reader consulting CLAUDE.md or the chapter sees the healed CONJECTURAL language. The Beilinson hierarchy is inverted: the HIGHER-AUTHORITY document carries the STALE narrative. Canonical violation: 2026-04-18 MC4-swarm retracted MC4^0 to CONJECTURAL (AP421); `concordance.tex:1949-1968` still advertises MC4^0 "proved on the transferred split surface" + overall MC4 package "proved unconditionally." Counter: every AP269/AP266 heal must include a concordance-level audit pass in the same wave. Healing: grep concordance for the named theorem label and any scope-level advertisement phrase; update both statement and scope tag. Distinct from AP271 (reverse drift CLAUDE.md-lags-manuscript): AP2181 is concordance-lags-both-CLAUDE.md-and-manuscript — a three-way drift specific to the highest-authority tier. Stronger than AP149 (resolution-propagation failure across files) because the failing tier is the governing document whose authority is load-bearing.

### AP2182 (Governing-document omission as negative verdict vs unrecorded-is-healing-gap ambiguity).

The concordance preamble (`concordance.tex:16-17`) states "Omission from this chapter is itself a verdict: what is not recorded here has not survived scrutiny." This establishes a STRONG negative interpretation of omission. A healed item that is NOT inscribed in concordance is thereby implicitly flagged as unsurvived; but in practice many 2026-04-18 heal items (Chiral CE, V^natural E_3, thm:chd-ds-hochschild, thm:uch-gravity-chain-level) are genuinely proved but concordance-absent because concordance is SELECTIVE, not EXHAUSTIVE. The preamble's strong-verdict framing collides with the selective-inscription practice. Counter: either (a) weaken the preamble to "omission is neutral; only explicit entries below are verdicts"; or (b) adopt an explicit inscription discipline where every UNCONDITIONAL or PROVED row in CLAUDE.md status tables must have a corresponding concordance entry within N waves of inscription. Healing recommendation: option (a) is lower-cost and matches current practice. Distinct from AP241 (advertised-but-not-inscribed characterization) which applies to CLAUDE.md advertising absent from the manuscript; AP2182 is the dual case where the manuscript proves something the concordance does not advertise, and the preamble interprets the silence as negative.

## Epistemic note

This audit is diagnosis-only. No manuscript edits were made. The F1 MC4^0 contradiction is the only load-bearing finding; it warrants a targeted follow-up Edit pass, not a concordance rewrite.
