# Wave 13 — Vol II Part IV Adversarial Attack+Heal (retry)

Date: 2026-04-17
Target: Vol II Part IV "The Characteristic Datum and Modularity"
(main.tex:1514-1581; chapters/examples/*, chapters/theory/{infinite_fingerprint_classification, modular_swiss_cheese_operad, curved_dunn_higher_genus, class_m_*, tempered_*, wn_tempered_*, beta_N_*, logarithmic_wp_*, irrational_cosets_*, bp_chain_level_*}, chapters/connections/{hochschild, brace, fractional_ghost_chain_level_platonic, relative_feynman_transform, modular_pva_quantization_core}).

Voice channelled: Etingof-Kazhdan / Kapranov / Bezrukavnikov — *the fingerprint is the primitive; the quadrichotomy is its double shadow.*

## Summary of verdicts

| Fingerprint / drift | Status in Part IV |
|---|---|
| H_k : (2, 2) G | CORRECT (infinite_fingerprint_classification.tex:57) |
| V_k(sl_N) : (2, 3) L | CORRECT (examples-worked, rosetta_stone) |
| βγ : (1, 4) C | **DRIFT — HEALED** (see §1 below) |
| Vir_c : (4, ∞) M | CORRECT (shadow atlases across Part IV) |
| V^♮ : (4, ∞, χ, 1, coset) | Not stated as tuple in Part IV; referenced only via κ(V^♮)=12 in thqg_perturbative_finiteness.tex and Monster sections in preface/connections — no drift to (2,2,χ,196884,coset). PASS. |
| AP235 "quadrichotomy" | CORRECT throughout Part IV preface (main.tex:1543, preface.tex:430-433, cor:double-coarse-projection). "quaternitomy" survives only in CLAUDE.md/notes/cache scaffolding, never in Part IV typeset prose. PASS. |
| AP244 codim-{2,1,0} Riccati + C quartic | Not inscribed in Part IV typeset prose (scaffold-only in preface §). No drift to 2×2 Boolean. PASS. |
| AP247 {Φ_d} | Not inscribed in Part IV proper. PASS. |
| HZ-3 uniform-weight tag on obs_g / F_g | F_g statements at rosetta_stone.tex:1510, 2030, 7191 already carry "conditional after Vol I rectification" qualifier (AP225-aware) or explicit "all-weight at g=1" tag at 7266. PASS. |
| κ-isospectral separator is r_max, not p_max | prop:six-slot-distinguishes-ch uses κ_ch (sixth slot) as Heisenberg-family separator, not p_max. Consistent with Wave-9. PASS. |

## 1. Primary drift healed — βγ mis-classified as class G

**Locus:** `chapters/examples/examples-worked.tex:4740-4773` — Coulomb-branch shadow classification proposition.

**Drift:**
- Prose line 4746-4747: "βγ system of N copies, with κ=0 and class **G** (the freest possible case)."
- Prop item (i): "free-field algebra (βγ or Heisenberg type): class **G**, r_max = 2."

**First-principles verdict:** βγ carries a conformal vector (spin (1,0) bosonic first-order system, c = 2) and Zhu(βγ) is infinite-dimensional; its shadow tower truncates at depth **4** (class **C**), not depth 2. Canonical fingerprint prefix is **(1, 4)** per Vol I CLAUDE.md HOT ZONE and landscape_census. Conflating "PBW-free" with "class G" erases the Heisenberg/βγ distinction that the sixth slot κ_ch and the shadow depth jointly pin (compare C3 affine KM vs Heisenberg at r_max=2 vs r_max=3).

**Heal (surgical, in place):**
- Separated Heisenberg (G, (—, 2)) from βγ (C, (1, 4)).
- Made affine KM fingerprint prefix (2, 3) explicit; Vir/W fingerprint prefix (4, ∞) explicit.
- Statement now reads as a four-clause (G/C/L/M) classification matching the quadrichotomy rather than a three-clause free/current/W partition that dropped class C.

No κ-identities touched; only shadow-class attribution of PBW-free-with-conformal-vector algebras. Lagrangian complementarity κ+κ^!=0 at βγ remains correct (class C is self-dual at the scalar level with ρ_A=0 per AP234 census, κ(βγ)+κ(βγ^!)=0 at each weight).

## 2. Surveyed and clean

- **Six-slot fingerprint chapter** (`theory/infinite_fingerprint_classification.tex`): canonical, quadrichotomy as double coarse projection, FF fifth class at critical level. No drift.
- **Part IV opener** (main.tex:1514-1581): quadrichotomy + curved-Dunn H²=0 + Arakelov K(A) + tensor-Arakelov Lagrangian — all aligned with Wave-14 reconstitutions.
- **Modular SC operad, curved-Dunn higher genus, class M original-complex, tempered stratum, W_N tempered closure, β_N=12(H_N−1), logarithmic W(p), irrational cosets, BP chain-level, fractional-ghost chain-level**: all Wave-1/Wave-2 closure inscriptions from 2026-04-16/17 already aligned.
- Monster V^♮ references in preface/connections carry κ=c/2=12 (Virasoro sector), never (2,2,χ,196884,coset).

## 3. Constitutional hygiene check

Part IV typeset prose contains NO `AP\d+`, `V\d-AP\d+`, `HZ-\d+`, "Pattern \d+", "Cache #\d+", or "first_principles_cache" tokens. (`HZ-IV` is permitted per CLAUDE.md exception; not present in Part IV either.)

## 4. Files skipped (per instruction)

Prior-wave heals in parallel (Vol II/III), scaffold-only files under `notes/`, `adversarial_swarm_*/`, `memory/`.

## 5. Residual

None in scope. The one genuine mathematical drift (βγ → class C) is healed. Recommend: after next full Vol II build, run AP5 sweep for "βγ.*class.*G" and "βγ.*r_\{\\max\} = 2" across all three volumes; the edit here is the Vol II canonical reference.
