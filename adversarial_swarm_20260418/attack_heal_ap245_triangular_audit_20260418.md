# AP245 Triangular Numerical Agreement Audit (Vol I, 2026-04-18)

## Mission

Programme-wide survey of AP245 (statement / proof / engine three-way numerical agreement). Scope: Vol I invariants cited in CLAUDE.md Structural Facts, HOT ZONE, Theorem Status table, and Wrong Formula Blacklist. Per Beilinson epistemic hierarchy: direct computation > .tex source > concordance > CLAUDE.md > memory.

## Method

For each scalar invariant or dimension cited programme-wide, triangulate:
(a) CLAUDE.md canonical value (including HOT ZONE, Key Constants, Status Table);
(b) Vol I manuscript inscription (chapters/, standalone/);
(c) compute engine value (compute/lib/, compute/tests/).

Agreement = all three independent sources give the same number. Triple-disagreement requires a source-of-truth decision per Beilinson hierarchy.

## Instance-by-instance audit

### 1. sl_2 affine ChirHoch total dimension

| Source | Value | Location |
|---|---|---|
| CLAUDE.md | 5 (triple 1,3,1) | Key Constants; Status row ChirHoch^1 KM |
| Manuscript | 5 (triple 1,3,1) | chapters/theory/chiral_center_theorem.tex:2276 "total dimension 1+3+1=5"; chapters/theory/en_koszul_duality.tex:5770; chapters/theory/chiral_koszul_pairs.tex:1120 |
| Engine | 5 | compute/lib/chirhoch_dimension_engine.py:300 "total=dim_g + 2, sl_2 -> 5" |

**Verdict: AGREES. No AP245 firing.**

### 2. Heisenberg ChirHoch Hilbert polynomial

| Source | Value | Location |
|---|---|---|
| CLAUDE.md | P(t)=1+t+t^2 | Theorem Status ChirHoch*(H_k) explicit row |
| Manuscript | 1+t+t^2 | chapters/examples/free_fields.tex:5518; chapters/frame/preface.tex:1679; chapters/frame/heisenberg_frame.tex:214 |
| Engine | (1,1,1) total 3 | compute/lib/chirhoch_dimension_engine.py (heisenberg branch) |

**Verdict: AGREES.**

### 3. Virasoro complementarity kappa + kappa^! = 13

| Source | Value | Location |
|---|---|---|
| CLAUDE.md | 13 | Key Constants "kappa+kappa'=... 13 (Vir)"; HZ-7 Vir self-dual c=13 |
| Manuscript | 13 | chapters/examples/minimal_model_examples.tex:672-688; chapters/connections/bv_brst.tex:1158; chapters/connections/concordance.tex:8904 |
| Engine | 13 (verified by complementarity_engines) | compute/tests pass |

**Verdict: AGREES.**

### 4. W_3 complementarity kappa + kappa^! = 250/3

| Source | Value | Location |
|---|---|---|
| CLAUDE.md | 250/3 | Key Constants; AP234 |
| Manuscript | 250/3 | chapters/theory/shadow_tower_higher_coefficients.tex:2295; chapters/connections/frontier_modular_holography_platonic.tex:5453; chapters/connections/outlook.tex:572 |
| Engine | 250/3 | compute/tests verify via C4 formula (H_N-1)*c at c=self-dual |

**Verdict: AGREES.**

### 5. Bershadsky-Polyakov Koszul conductor K_BP = 196 (Arakawa convention)

| Source | Value | Location |
|---|---|---|
| CLAUDE.md | 196 (Arakawa) / 50 (FL) | Status row BP Koszul-conductor polynomial identity |
| Manuscript | 196 (Arakawa) | standalone/bp_self_duality.tex:298-300 thm:bp-koszul-conductor-polynomial; standalone/bp_self_duality.tex:558 "K=196 FKR convention" |
| Engine | 196 | compute/tests/test_bp_koszul_conductor_engine.py |

**Verdict: AGREES across three files (Arakawa). FL=50 variant is a CONVENTION cross-reference, not a three-way disagreement.**

### 6. BP scalar complementarity kappa + kappa^! = 98/3

| Source | Value | Location |
|---|---|---|
| CLAUDE.md | 98/3 | Key Constants |
| Manuscript | 98/3 | worldview_synthesis_2026_04_17.tex:229, 279; AGENTS.md:439; chapters/connections/frontier_modular_holography_platonic.tex:5453 |
| Engine | 98/3 | tests verify |

**Verdict: AGREES.**

### 7. Zamolodchikov S_4(Vir_c) = 10 / [c(5c+22)]

| Source | Value | Location |
|---|---|---|
| CLAUDE.md | 10/[c(5c+22)] | HOT ZONE C_A; AP178 |
| Manuscript | 10/[c(5c+22)] | chapters/examples/w_algebras_deep.tex:702, 727, 846, 3098, 3930 |
| Engine | 10/[c(5c+22)] | compute/lib/shadow_tower_* engines |

**Verdict: AGREES.**

### 8. kappa_BKM(Phi_1) = 5 (healed 2026-04-17 per AP238)

| Source | Value | Location |
|---|---|---|
| CLAUDE.md | 5 (via Gritsenko Delta_5) | Status row CY-D dimension stratification |
| Manuscript (Vol III) | 5 | cy_d_kappa_stratification.tex (per prior wave notes) |
| Engine (Vol III) | 5 | compute/lib/kappa_bkm_universal.py:396-401 |

**Verdict: AGREES post-heal. AP238 canonical case closed; Vol III cross-volume residual is out of scope for this Vol I audit.**

### 9. K3 x E kappa invariants (three flavors)

This is NOT an AP245 three-way disagreement, but rather THREE DISTINCT INVARIANTS under the letter kappa. Documented at chapters/theory/higher_genus_modular_koszul.tex:3613-3642 (rem:kappa-holo-k3e).

| Invariant | Value | Nature |
|---|---|---|
| kappa^Heis(K3 x E) | 3 | additive via Kunneth, = dim_C |
| Xi(K3 x E) = kappa_ch | 0 | Hodge supertrace (multiplicative) |
| kappa_BKM(K3 x E) | 5 | Igusa cusp form Phi_10 weight/2 |

**Verdict: CONSISTENT multi-flavor (each invariant separately agrees across CLAUDE.md / manuscript / engine; three values coexist LEGITIMATELY).** The cross-flavor bridge remark at higher_genus_modular_koszul.tex:3613 resolves AP289 discipline (multiplicative vs additive).

**Residual constitutional issue (out of scope for AP245):** higher_genus_modular_koszul.tex:3628 contains the forbidden token `AP289` in typeset prose — violates Manuscript Metadata Hygiene. Flagged separately; not an AP245 numerical disagreement.

### 10. Heisenberg universal conductor K (AP312 residual check)

**LIVE AP245/AP312 INSTANCE.** Three values coexist under the letter K for Heisenberg H_k:

| Source | Value | Convention |
|---|---|---|
| chapters/theory/universal_conductor_K_platonic.tex:1304 | -2 | Trinity K = -c_ghost(BRST), level-independent |
| chapters/frame/heisenberg_frame.tex:60 | 0 | kappa + kappa^! complementarity (k + (-k)) |
| chapters/examples/heisenberg_eisenstein.tex:35 | k | Derivation "K(H_k) = -(-2k)/2 = k = kappa^Heis" citing cor:uc-K-heisenberg |
| chapters/examples/landscape_census.tex:134 + footnote L1280 | n/a | "c + c' not defined in the usual sense" for Heis-Sym^ch duality |
| Engine | -2 (BRST ghost) | compute paths consistent with universal_conductor_K_platonic |

**Source-of-truth analysis (per Beilinson hierarchy):**
- Direct computation: BRST resolution of H_k by bc pair has ghost charge -2, level-independent (no k enters the ghost-current Jacobian). K = -c_ghost = -(-2) = -2, so `universal_conductor_K_platonic.tex:1304` ("K = -2, spin-1 bosonic, level-independent") is CORRECT.
- Trinity K: K_c = c + c^! is not defined for Heis (no conformal Koszul-dual), so the landscape_census.tex dagger footnote ("c + c' not defined") CORRECTLY records the scope restriction.
- Complementarity K: kappa(H_k) + kappa(H_k^!) = k + (-k) = 0 is DIFFERENT invariant from Trinity K. AP234 discipline says the two K's must carry distinguishing notation.
- `heisenberg_eisenstein.tex:35` derivation "K(H_k) = -(-2k)/2 = k" is ARITHMETICALLY self-consistent only if the resolving ghost charge is taken to be -2k (level-dependent); but the corollary it cites (cor:uc-K-heisenberg at universal_conductor_K_platonic.tex:1304) states the ghost charge is -2 level-independent. **Internal contradiction: citing source says K=-2, using it as K=k.** This is an AP245 three-way drift (citing-source says A, using-source writes B under the same letter, engine says A).

**Beilinson verdict:** universal_conductor_K_platonic.tex:1304 is the source of truth (K(H_k) = -2, level-independent, via BRST ghost charge -c_ghost of a spin-1 bosonic bc resolution). heisenberg_eisenstein.tex:35 silently confabulates a level-dependent ghost charge -2k to force the identification K = kappa^Heis = k, contradicting the cited corollary. Heal: retract the "-(-2k)/2" derivation; state separately that kappa^Heis(H_k) = k (kappa-flavor invariant, Census C1) and K(H_k) = -2 (K-flavor invariant, Trinity K / -c_ghost). These are two distinct invariants under different letters once AP234 discipline is applied.

## Summary Table

| # | Invariant | Verdict | AP Firing |
|---|---|---|---|
| 1 | sl_2 affine ChirHoch = 5 | AGREES | None |
| 2 | Heis ChirHoch P(t)=1+t+t^2 | AGREES | None |
| 3 | Vir kappa+kappa^!=13 | AGREES | None |
| 4 | W_3 kappa+kappa^!=250/3 | AGREES | None |
| 5 | BP K=196 Arakawa | AGREES | None |
| 6 | BP kappa+kappa^!=98/3 | AGREES | None |
| 7 | S_4(Vir_c)=10/[c(5c+22)] | AGREES | None |
| 8 | kappa_BKM(Phi_1)=5 | AGREES post-heal | AP238 closed |
| 9 | K3 x E multi-flavor kappa | LEGITIMATE multi-invariant | Cross-bridge remark resolves |
| 10 | Heisenberg K | **LIVE AP245 / AP312** | Heal required |

## Recommended heal for instance #10

File: `chapters/examples/heisenberg_eisenstein.tex` lines 30-36.

Current (confabulating):
```
The κ-value κ^Heis(H_k) = k is the BRSTGauged-evaluation of the
universal conductor functor K(A) = -c_ghost(BRST(A)) specialised to
the abelian-CS BRST resolution: a single bc pair carrying ghost charge
-2k resolves H_k, so K(H_k) = -(-2k)/2 = k = κ^Heis(H_k)
(Corollary cor:uc-K-heisenberg, Chapter universal-conductor).
```

Heal (proposed, not applied):
```
The κ-value κ^Heis(H_k) = k (Census C1) is the kappa-flavor invariant.
The Trinity K-flavor invariant is a DIFFERENT scalar: K(H_k) = -2
(level-independent, from the ghost charge -2 of a spin-1 bosonic bc
pair resolving H_k); see Corollary cor:uc-K-heisenberg. The two
invariants live under distinct letters per the two-K discipline
(rem:uc-heisenberg-scope-distinction).
```

Cross-volume propagation: search for the confabulated expression `-(-2k)/2` or `K(H_k) = k` pattern across all three volumes before applying the heal.

## Cross-volume residual

- `adversarial_swarm_20260418/attack_heal_dual_level_complementarity_20260418.md` and `wave6_ap234_propagation_sweep.md` already track the broader two-K discipline sweep. The heisenberg_eisenstein.tex:35 confabulation is not recorded in either note.
- Vol II / Vol III propagation out of scope for this Vol I audit.

## Constitutional violations surfaced (incidental)

- `higher_genus_modular_koszul.tex:3628` contains forbidden `AP289` token in typeset prose (Manuscript Metadata Hygiene zero-tolerance). Requires token retirement; mathematical substance (multiplicative-vs-additive kappa flavor discipline) preserved.

## Minimal AP block

No new AP numbers inscribed. This audit's findings collapse to existing APs:
- AP245 (statement-proof-engine agreement) — existing instance heisenberg_eisenstein.tex:35 vs universal_conductor_K_platonic.tex:1304.
- AP234 (two Koszul conductors under letter K) — canonical discipline applies.
- AP312 (three-way cross-file scalar-value contradiction) — residual site heisenberg_eisenstein.tex:35 was not healed by the 2026-04-18 Trinity K audit.

Reserved block AP2141-AP2160: **unused this wave.** The nine clean instances do not warrant new AP inscription; the tenth reduces to already-catalogued APs.

## Verdict

Nine of ten sampled Vol I invariants pass triple-agreement. One live AP245 residual at heisenberg_eisenstein.tex:35 (Heisenberg K confabulation citing cor:uc-K-heisenberg as K = -2 while deriving K = k). Heal is local (one paragraph), out-of-scope for this audit but fully characterised above.
