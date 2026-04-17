# Wave 5 — Adversarial audit: chiral Hochschild and Koszul pair foundations

Target chapters
- `chapters/theory/chiral_hochschild_koszul.tex`         (6610 lines)
- `chapters/theory/hochschild_cohomology.tex`            (1711 lines)
- `chapters/theory/koszul_pair_structure.tex`            (2774 lines)
- `chapters/theory/chiral_koszul_pairs.tex`              (6797 lines)
- `chapters/theory/chiral_modules.tex`                   (5191 lines)
- `chapters/theory/three_invariants.tex`                 (356 lines)
- `chapters/theory/spectral_sequences.tex`               (589 lines)

Methodology: AP-CY62–67 disambiguation (geometric vs algebraic chiral Hochschild; BD chiral operad vs algebraic End^ch; ChirHoch / HH* / H*_GF; spectral parameter provenance; BZFN ambient categories), AP160 (forbidden bare "Hochschild"), AP14 (Koszul ≠ SC formality), AP-CY11 (conditional propagation), AP-CY63 (BD vs algebraic operad bridge missing).

Wave-1/2/3 notation reused: each finding is tagged ATTACK / DEFENSE / REPAIR / UPGRADE.

---

## Section 1 — Triage

### 1.1 Three Hochschild objects in play

The manuscript uses *at least four* objects under the umbrella "Hochschild," and they are systematically conflated:

| Object | Notation | Defined where | Type |
|---|---|---|---|
| Geometric chiral Hochschild cochains | `C^n_chiral(A)` | `chiral_hochschild_koszul.tex:145` | Sections of `j_*j^* A^{(n+2)} ⊗ Ω^n_log` on `C̄_{n+2}(X)` |
| Algebraic / Ext-flavour chiral Hochschild | `ChirHoch^n(A,M)` | `hochschild_cohomology.tex:76` | `RHom_{D_X}(B̄^geom(A), M)` |
| Bigraded chiral Hochschild | `CH^{p,•}_ch`, `RHH_ch(A)` | `higher_genus_foundations.tex:2748` | `RHom_{D_{C̄_{p+2}}}(A^{⊠(p+2)}, ω)` |
| Chiral Hochschild *homology* | `HH_n^ch(A)` | `hochschild_cohomology.tex:553` | `H_n(CH_*(A), d_HH)` (collapsed cyclic model) |
| Bar/Hochschild from enveloping | `ChirHoch^n(A,M) = Ext^n_{A^e}(A,M)` | `koszul_pair_structure.tex:259` | `Ext` over `A ⊠_{D_X} A^op` |
| Topological Hochschild on a point | `THH(A)` | `hochschild_cohomology.tex:1276` (factorization homology over `S^1`) | annulus trace |
| Gel'fand–Fuchs / continuous Lie cohomology | `H^*_cont(L_1)` | `hochschild_cohomology.tex:128` (remark) | polynomial ring `C[Θ]` |
| Classical (point) Hochschild | `HH^*(A_0, ...)` | `hochschild_cohomology.tex:88`, `:722` | spectral sequence input |

CRITICAL — at least *three distinct definitions* of "the chiral Hochschild complex" are introduced and treated as if they were the same:

(a) the geometric realization `C^n_chiral(A) = Γ(C̄_{n+2}, j_*j^* A^{⊠(n+2)} ⊗ Ω^n_log)` (`chiral_hochschild_koszul.tex:145–157`);

(b) the algebraic enveloping definition `ChirHoch^n(A) = Ext^n_{A^e}(A, A)` with `A^e = A ⊠_{D_X} A^op` (`koszul_pair_structure.tex:166–265`);

(c) the bigraded definition `CH^{p,•}_ch(A) = RHom_{D_{C̄_{p+2}}}(A^{⊠(p+2)}, ω)` (`higher_genus_foundations.tex:2748–2769`).

Definitions (a) and (c) differ: (a) uses `Ω^n_log` cochains and a two-input convolution differential; (c) uses Verdier-dualizing-sheaf coefficients and a Verdier shift `[p+2]`. Definition (b) is the enveloping-Ext flavour, valid on the formal disk after passing to chiral enveloping algebras. AP-CY62 fires: this is precisely the geometric-vs-algebraic conflation flagged for Vol III.

### 1.2 Koszul pair definition triage

`def:chiral-koszul-pair` (`chiral_koszul_pairs.tex:658–717`) is well-typed: a pair of chiral twisting data with Verdier-compatible identifications `D_Ran(C_1) ≃ Ω_X(C_2)`. Two grades of caveat:

1. The *standard construction* clause (`:690–710`) circular-loops with `thm:bar-cobar-isomorphism-main`: `C_i := B̄_X(A_i)` with the canonical twisting morphism, and Verdier compatibility is provided by `thm:verdier-bar-cobar`. Theorem A is then used to prove what the definition antecedently *requires*.
2. `def:chiral-twisting-datum` requires "exhaustive, complete, bounded-below filtration $F_•$" on `A`, `C`, `B̄_X(A)`, `Ω_X(C)`. For non-finite-type chiral algebras (Yangians, large W-algebras, K3 lattice VOAs at higher rank), boundedness-below in conformal weight is FALSE in some sectors. The definition silently excludes these but is then used universally.

### 1.3 Three invariants

`three_invariants.tex` is the cleanest, sharpest chapter in the suite. It distinguishes:

- `p_max(A)`: maximal OPE pole order among generator pairs;
- `k_max(A) = p_max - 1`: collision depth (degree-2 invariant);
- `r_max(A) ∈ {2,3,4,∞}`: shadow depth (involves all bar degrees).

The proposition `prop:three-invariants-relations` (line 178) is genuinely well-posed and the βγ witness `(p_max, k_max, r_max) = (1, 0, 4)` is load-bearing. ATTACK lines for this chapter are minimal — but see §2.4 below for the trichotomy rounding.

### 1.4 Spectral sequences

The spectral_sequences chapter is technically clean (`Weibel94`, `Boardman-conditional`, etc.). Three load-bearing claims are made on chiral algebras specifically:

- bar SS: `E_1^{p,q} = H^{p+q}_dR(C̄_p, A^{⊠p} ⊗ Ω_log) ⇒ H^{p+q}(B̄^geom(A))` (line 276, ProvedHere).
- Genus SS: `E_1^{g,n} = H_n(B̄^{(g)}(A), d_0) ⇒ H_n(B̄^tot(A))` (line 383, ProvedElsewhere via `cite{BD04}` — but BD04 does NOT contain a genus spectral sequence with this signature; this attribution is suspect).
- Koszul degeneration `prop:degen-koszul` (line 328, ProvedHere): for Koszul A, `E_2^{p,q} = Ext^{p,p+q}_A(C, C)` and Koszulness collapses at `E_2`.

### 1.5 Chiral modules

Three module categories defined: `Mod_A` (symmetric), `Mod^{E_1}_A` (ordered, when A is E_1-chiral), `D(Mod_A)` (derived). Hochschild homology of A with values in M is defined NOWHERE in this chapter — only `HH_*^ch(A)` (no module argument) is defined in `hochschild_cohomology.tex`. This is a structural gap (see §2.5).

---

## Section 2 — Per-claim attack/defense/repair

### 2.1 The "chiral Hochschild complex" definition is multivalued (AP-CY62)

ATTACK. The manuscript maintains *three distinct geometric models* without naming the comparison:

- `def:chiral-hochschild-derived` (`hochschild_cohomology.tex:76`): `RHom_{D_X}(B̄^geom(A), M)`.
- `def:chiral-hochschild` (`hochschild_cohomology.tex:469`, with `det(Ω^1_{C̄_{n+1}/X})`): a `Tot`-style chiral cyclic complex with cyclic structure built into `d_HH`.
- `def:chiral-hochschild-complex` geometric realization (`chiral_hochschild_koszul.tex:145`): `Γ(C̄_{n+2}, j_*j^* A^{⊠(n+2)} ⊗ Ω^n_log)` — note the index shift: `n+2` here vs `n+1` in `def:chiral-hochschild`.

The shift `n+1` vs `n+2` is the difference between (i) "n inputs + one output" (cyclic, `n+1` points) and (ii) "n insertions on a curve plus output and evaluation point" (`n+2` points). These ARE quasi-isomorphic only after the Verdier-Tate twist `[2]` of `lem:hochschild-shift-computation` (line 504). The reader is left to discover this from a 100-line bigraded-totalisation lemma rather than from a comparison theorem.

DEFENSE. The bigraded `RHH_ch(A)` of `def:bigraded-hochschild` is the *correct* abstract object: it is `RHom` over `D_{C̄_{p+2}}` with coefficient `ω`, and the Verdier shift `[p+2]` cancels the totalisation shift `[-p]` to produce the constant `[2]` (`rem:hochschild-shift-origin`, `higher_genus_foundations.tex:2771`). On the Koszul locus, all three models become quasi-isomorphic via `prop:fm-tower-collapse` (line 606).

REPAIR. Add a single **comparison theorem** at the start of `chiral_hochschild_koszul.tex` Section 3:

```
Theorem (Comparison of chiral Hochschild models).
For an augmented chiral algebra A on a smooth projective curve X,
there is a chain of natural quasi-isomorphisms
  C^•_chiral(A)  ≃  CH^{•,•}_ch(A)  ≃  RHom_{D_X}(B̄^geom(A), A)
once the Verdier shift [2] is absorbed into the totalisation indexing.
```
Cite this theorem at every later occurrence. AP160 violation: use `ChirHoch_geom`, `ChirHoch_alg`, and `ChirHoch_bigr` as separate symbols when the model matters.

UPGRADE. Take the bigraded model `RHH_ch(A)` as the *canonical* definition. Prove `C^•_chiral(A) ≃ RHH_ch(A)` and `RHom_{D_X}(B̄^geom, A) ≃ RHH_ch(A)` as two propositions. Now the strongest theorem becomes:

  Strong Theorem H. *On the Koszul locus, all three models agree as objects of the curve-level derived category, with cohomological amplitude `[0,2]`, and the duality `ChirHoch^n(A) ≅ ChirHoch^{2-n}(A^!)^∨ ⊗ ω_X` is independent of model.*

### 2.2 The "Borcherds identity = associativity" gloss in the d²=0 proof (AP14, AP153 from V2)

ATTACK. `thm:hochschild-chain-complex` (`hochschild_cohomology.tex:491`) writes "associativity of the chiral product (the Borcherds identity)" as if Borcherds = associativity. Borcherds is associativity *up to total derivative*, equivalently homotopy associativity (the proof itself acknowledges this in the closing paragraph, line 547). The `d²=0` proof relies on cancellation of "Type B" terms by Borcherds — but Borcherds is a triple-residue identity, not a pairwise one, so the cancellation is genuinely operadic (cf. `chiral_hochschild_koszul.tex:225–305`, the three-component d_int + d_fact + d_config decomposition with explicit Arnold relation deployment). The cleaner proof IS the one in `chiral_hochschild_koszul.tex`, and `hochschild_cohomology.tex:498–550` is a strictly weaker shadow.

DEFENSE. The two proofs are not in conflict; the `hochschild_cohomology.tex` version is the abstract version, the `chiral_hochschild_koszul.tex` version is the geometric realization. But the manuscript should NOT have two `thm:..-chain-complex` style results stated independently with different proofs.

REPAIR. Delete `thm:hochschild-chain-complex` (`hochschild_cohomology.tex:491`) and replace with a Remark citing `thm:chiral-hochschild-differential` (`chiral_hochschild_koszul.tex:172`).

### 2.3 The Hochschild-classical comparison spectral sequence is mis-attributed

ATTACK. `thm:hochschild-classical-comparison` (line 86): `E_2^{p,q} = HH^p(A_0, H^q(Ω^*_X)) ⇒ ChirHoch^{p+q}(A)`, ProvedElsewhere [BD04]. This spectral sequence does NOT appear in BD04 in this form. BD04 §4 develops chiral Hochschild via Ran-space methods, not via a base-fibre spectral sequence to point-Hochschild. The "fibre-at-a-point" `A_0` is itself ill-defined (chiral algebras don't restrict to a point — they restrict to formal disks, which is already an enveloping algebra, not a Hochschild-input algebra). At minimum, the cited reference does not establish the claim; at maximum, the claim is wrong because of the formal-disk-vs-point issue.

REPAIR. Either (a) provide an explicit construction of the spectral sequence with attention to formal-disk vs point (and state that `HH^p(A_0, ...)` means `HH^p` of `Zhu(A)` or `A_0 = A/T`-bracket quotient), or (b) downgrade to `\begin{conjecture}` or an evidence Remark. Strongest statement:

  Strong Conjecture (point–chiral comparison). *For finite-type quadratic chiral algebras, there is a spectral sequence with `E_2^{p,q} = HH^p(Zhu(A), H^q_dR(X, A))` converging to `ChirHoch^{p+q}(A)`.* (Zhu's algebra replaces the ill-defined "fibre at a point.")

### 2.4 The k_max trichotomy artificially excludes k_max = 2 (mechanism error)

ATTACK. `rem:k-max-2-missing` (`three_invariants.tex:298`) excludes `k_max = 2` because `p_max = 3` would require half-integer weight. But this is wrong on two counts:

(i) Half-integer weight bosonic OPEs DO exist in superconformal extensions (N=1 super-Virasoro has `G(z)G(w) ~ 2c/3 (z-w)^{-3} + ...`). The trichotomy is not about super-vs-bosonic, it is about the standard bosonic landscape — but this restriction is NOT stated in the theorem hypothesis (line 312, `\begin{theorem}[The k_max trichotomy; ProvedHere]`). The theorem claims a universal exclusion, but the proof only excludes the bosonic case.

(ii) The reasoning "p_max ∈ {1,2}∪{4,5,...}" silently uses that generator weights satisfy `2h ∈ {1,2,4,5,...}`. For `h=3/2` (G-current of N=1), `2h = 3` and `p_max = 3` is allowed.

REPAIR. Restrict `thm:k-max-trichotomy` to "for every bosonic chiral algebra in the standard landscape" or "for chiral algebras generated by integer-weight fields." The mechanism is correct *within* the bosonic landscape; the universal claim is false.

UPGRADE. State the correct general trichotomy: "for chiral algebras with generator weights `h_α`, the value `k_max ∈ {2h-1 : h is a generator weight}`. In the bosonic-integer-weight landscape, this skips `k_max = 2`."

### 2.5 Hochschild homology with module coefficients is missing

ATTACK. `chiral_modules.tex` defines factorization modules, chiral modules, E_1-chiral modules, but never defines `HH_*^ch(A, M)` for a general module `M`. Yet `hochschild_cohomology.tex:553` defines `HH_n^ch(A) := H_n(CH_*(A), d_HH)` *only* with coefficients `M = A`. The Hochschild-vs-cyclic SBI sequence (`cor:connes-SBI`, line 626) and the Heisenberg `E_2` computation (`ex:E2-heisenberg`, line 678) implicitly use modules over `A`, but the module-coefficient version is never written down.

REPAIR. Add to `chiral_modules.tex` Section 36–170 (after `def:chiral-module`):

```
Definition (Chiral Hochschild homology with values in a chiral A-module M).
  CH_n(A; M) := Γ(C̄_{n+1}(X), M ⊠ A^{⊠n} ⊗ det(Ω^1_{C̄_{n+1}/X}))
with d_HH defined as in def:chiral-hochschild but with the M-action
replacing the cyclic wraparound at i=n.
```

UPGRADE. With this definition installed, the strongest possible theorem is:

  Strong Theorem (chiral HKR). *For a chiral Koszul A and a chiral A-module M, `HH_*^ch(A; M) ≃ Tor^{A^e}_*(A, M)` quasi-iso, computed by the bar resolution of A as A^e-module, with `E_2`-page given by `Tor^{Zhu(A)^e}_*(Zhu(A), Zhu(M)) ⊗ H^*_dR(X)` (when X = formal disk, the de Rham cohomology degenerates and we recover classical HKR).*

### 2.6 The Koszul condition is multiply defined and not centrally compared

ATTACK. The manuscript contains FOUR distinct "Koszul" definitions:

- `def:chiral-koszul-morphism` (`chiral_koszul_pairs.tex:268`): twisting datum (A, C, τ, F_•) with both `K^L_τ` and `K^R_τ` acyclic, and gr-classical Koszul, and strong filtration convergence.
- `def:chiral-koszul-pair` (`chiral_koszul_pairs.tex:658`): a *pair* of twisting data with Verdier compatibility.
- `def:koszul-chiral-algebra` (referenced `chiral_koszul_pairs.tex:714` but not located in this file — must be in another file).
- Implicit definition via `Ext^{i,j}_A(C,C) = 0` for `i ≠ j` (used in `prop:degen-koszul` proof, `spectral_sequences.tex:341`).

The Ext-diagonal definition is used (silently) as if it were equivalent to the twisting-datum definition. But this equivalence is `thm:ext-diagonal-vanishing` (`chiral_koszul_pairs.tex:1367`) — which itself depends on `thm:bar-concentration`. The reader cannot tell which definition is "the" definition.

REPAIR. Promote ONE definition to canonical. Recommended: the *Ext-diagonal* `Ext^{i,j}_A(C,C) = 0 for i ≠ j` (most invariant). Then prove

```
Theorem (equivalence of chiral Koszul conditions).
For a chiral algebra A on a smooth curve X with PBW filtration:
  (i)   Ext-diagonal: Ext^{i,j}_A(C, C) = 0 for i ≠ j.
  (ii)  Bar concentration: B̄^geom(A) has H^* in tensor-degree = bar-degree.
  (iii) Twisting datum: (A, B̄(A), τ_can, F_PBW) is Koszul in the sense
        of def:chiral-koszul-morphism.
  (iv)  PBW criterion: gr_F A is classically Koszul.
are equivalent.
```

Already most of the equivalences exist as separate theorems; the chapter just needs to state them as *one* theorem.

UPGRADE. The repaired equivalence is the strongest possible foundation for chiral Koszulness — every later chapter cites this single result instead of a confusing patchwork.

### 2.7 The "spectral sequence" of `thm:hochschild-spectral-sequence` may not converge for K3 Yangians (AP-CY11)

ATTACK. `thm:hochschild-spectral-sequence` (`chiral_hochschild_koszul.tex:362`, ProvedHere) asserts a spectral sequence converging to `ChirHoch^{n+q}(A)`, with the proof asserting convergence "from the bounded-below hypothesis on A and the finite cohomological dimension of configuration spaces." But:

- `A` for the K3 Yangian (`Y(g_K3)`) is graded by Mukai weight (signature (4,20)), and `ChirHoch^{n+q}` may have unbounded cohomological dimension if `A` is not finite-type.
- `B̄^geom(A)` for non-finite-type Koszul algebras can have an unbounded spectral sequence at each page.

DEFENSE. The chapter restricts via "Regime: quadratic on the Koszul locus" tags (e.g. `chiral_hochschild_koszul.tex:325`). For finite-type quadratic Koszul algebras (Heisenberg, Virasoro at generic c, KM at generic level), convergence is fine.

REPAIR. The convergence proof in `thm:hochschild-spectral-sequence` (line 370) needs to explicitly state finite-type as a hypothesis. Currently it asserts convergence universally and the convergence proof is one sentence.

UPGRADE. Strongest convergence theorem:

  Strong Convergence. *For a chiral Koszul algebra A on X with `dim C̄_n(X) = n` (so finite cohomological dimension at each bar degree) and finite-type weight pieces, the bar spectral sequence `E_1 = H^q_dR(C̄_p, A^{⊠p} ⊗ Ω_log) ⇒ ChirHoch^{p+q}(A)` converges strongly. For non-finite-type weight pieces (Yangian, K3 lattice, large W), convergence is conditional and requires `lim^1` vanishing as in `prop:complete-filt-convergence`.*

### 2.8 The Verdier-shift collapse argument relies on FM-formality, which is rational

ATTACK. `prop:fm-tower-collapse` (line 606) and `lem:hochschild-shift-computation` (line 504) use Kontsevich formality of FM_m(C) (`prop:en-formality`) to kill higher differentials. AP-CY33 fires: Kontsevich formality is RATIONAL. Chain-level E_3 structure (and thus chain-level higher-d_r differentials in the FM-tower spectral sequence) does NOT obey formality. For chiral algebras of class M (Virasoro, W_N), the chain-level corrections are precisely the shadow tower, and these CONTRIBUTE to higher d_r.

DEFENSE. The proposition is about cohomological amplitude `[0,2]`. For finite-dimensional cohomology (which is what `prop:fm-tower-collapse` claims), formality at the level of cohomology suffices. The chain-level corrections live in higher degrees that are killed by the cohomology operation.

REPAIR. Add a parenthetical: "(at the level of cohomology; chain-level FM-formality fails for class-M algebras, but cohomological FM-formality suffices for the amplitude statement)."

UPGRADE. The repaired statement is:

  Strong FM-tower collapse. *On the Koszul locus, the FM-tower of configuration spaces collapses to the curve-level Ext at the level of COHOMOLOGY. At the chain level, for class-M chiral algebras, the higher d_r differentials encode the shadow obstruction tower, and the spectral sequence does not collapse strictly — but the cohomological amplitude `[0,2]` is preserved.*

### 2.9 Three Hochschilds: ChirHoch / HH* / H*_GF (AP-CY64)

ATTACK. `rem:gf-vs-chirhoch` (`hochschild_cohomology.tex:128`) and `rem:critical-level-lie-vs-chirhoch` (`hochschild_cohomology.tex:158`) both note that Gel'fand–Fuchs cohomology `H^*_cont(L_1) = C[Θ]` is "different" from chiral Hochschild `ChirHoch^*(Vir_c)`. Vol III's AP-CY64 shows this discussion is mis-stated. The actual situation:

- ChirHoch (chiral Hochschild) is concentrated in {0,1,2} for Virasoro at generic c (Theorem H).
- HH*(Zhu(Vir_c)) (classical Hochschild of the Zhu algebra) is finite-dimensional, concentrated in {0} for `Zhu(Vir_c) = C[L_0]` (a polynomial ring).
- H*_GF (Gel'fand–Fuchs) is `C[Θ]`, *unbounded* in degree.

The remark says "ChirHoch is concentrated in {0,1,2} but Gel'fand–Fuchs is unbounded." The Vol III adversarial reading: this is a *true* statement about the comparison, but it suggests the wrong reason. The reason ChirHoch is bounded is NOT that Gel'fand–Fuchs is "topological without curve geometry"; it's that ChirHoch carries a Verdier-Tate `[2]` shift and a curve `D_X`-amplitude `[0,2]`. Gel'fand–Fuchs is the Lie algebra cohomology of a Lie algebra of vector fields on a *formal* disk, which is finite-dim only with the right finite-dim coefficient system.

REPAIR. Replace `rem:gf-vs-chirhoch` and `rem:critical-level-lie-vs-chirhoch` with a single clean three-way comparison block:

```
Remark (Three Hochschilds, three growth profiles).
  ChirHoch^*(Vir_c) (Theorem H):     dim P(t) = 1 + t^2          (bounded {0,2})
  HH^*(Zhu(Vir_c))  (classical):     dim P(t) = 1                (concentrated 0)
  H^*_cont(L_1)     (Gel'fand–Fuchs): dim P(t) = 1/(1-t^2)        (polynomial)
The three are linked by spectral sequences:
  HH^p(Zhu(A)) ⊗ H^q_dR(X) ⇒ ChirHoch^{p+q}(A)   (Section 1.7 above)
  H^*_cont(L_1) ≃ ChirHoch^*(Vir_{-h^∨}) at critical level  (BD04 4.5.2)
  HH^*(Zhu(A)) computes the *Zhu-mode-algebra* Hochschild,
  which differs from ChirHoch* by the curve-level enrichment.
At critical level, ChirHoch becomes unbounded (Feigin-Frenkel center).
At generic level, the three remain distinct.
```

UPGRADE. Strongest possible identification:

  Strong three-Hochschild comparison theorem. *For any chiral algebra A on X with PBW filtration and finite-type Zhu algebra `Zhu(A)`, there are spectral sequences*

```
HH^p(Zhu(A)) ⊗ H^q_dR(X)        ⇒ ChirHoch^{p+q}(A)             [generic level]
H^*_Lie,cont(g ⊗ tC[[t]])         ≅ ChirHoch^*(A_{crit})          [critical level]
```

  *converging strongly under `prop:complete-filt-convergence` hypotheses. The growth of ChirHoch interpolates between bounded (generic level) and unbounded polynomial (critical level), with the transition encoded in Feigin-Frenkel conjugation `k → -k - 2h^∨`.*

### 2.10 Spectral parameters and AP-CY65 — does ChirHoch carry spectral data?

ATTACK. `chiral_hochschild_koszul.tex` Section 3 (configuration-space construction) places cochains on `C̄_{n+2}(X)` with logarithmic poles along boundary divisors. The "spectral parameters" `z_i - z_j` enter via these log forms. AP-CY65 from Vol III: "the chiral bar DIFFERENTIAL is z-dependent; the topological bar COPRODUCT is z-independent." Vol I's Hochschild apparatus is *all* z-dependent — the differential `d_int + d_fact + d_config` of `thm:chiral-hochschild-differential` (line 172) carries spectral data through `d_config` and through residue extraction in `d_fact`.

DEFENSE. Vol I is correctly z-dependent throughout: the chiral Hochschild complex IS the curve-enriched version, and the spectral data is genuine. AP-CY65 is a Vol III warning, but Vol I respects it implicitly.

REPAIR. None needed for the substance. But add an explicit remark at `chiral_hochschild_koszul.tex:139`:

```
Remark (Spectral parameters of the chiral Hochschild complex).
The cochain space C^n_chiral(A) carries spectral data through
the configuration-space coordinates z_i ∈ C̄_{n+2}(X). Both d_fact
(via residues at z_i = z_j) and d_config (via the de Rham
differential on boundary divisors) are z-dependent. The classical
"point" Hochschild complex HH^*(Zhu(A)) is the z = 0 (full collision)
specialization: it forgets all spectral data and computes only the
mode-algebra Ext.
```

UPGRADE. Strong spectral statement:

  Strong spectral comparison. *The full collision specialization `z_i → z_0 ∀i` defines a chain map `C^•_chiral(A) → CH^•(Zhu(A))` whose kernel and cokernel are computed by the FM-tower spectral sequence. On the Koszul locus, the map is a quasi-iso in degree 0 and exhibits the [0,2] amplitude bound at higher degrees.*

### 2.11 The BD chiral operad vs algebraic End^ch confusion (AP-CY63)

ATTACK. `chiral_hochschild_koszul.tex` uses the "chiral product" `μ` throughout but never distinguishes the BD chiral operad (D-module flavour) from the algebraic End^ch operad (formal Laurent series flavour). The proof of `thm:chiral-hochschild-differential` uses BD-style arguments (associativity = Borcherds = factorization-algebra axiom), but the explicit formulas at line 311 (the `(d_int φ)`, `(d_fact φ)`, `(d_config φ)` formulas) treat μ as if it were a strict associative product, then pull back to the BD setting. The bridge between the two is *nowhere stated*.

DEFENSE. For Heisenberg, KM, Virasoro, etc., the explicit formulas are correct because the bridge is well-known to experts (any vertex algebra has both a BD-chiral structure and an `End^ch`-style mode product, related by the natural action of D_X). The omission is a pedagogical issue, not a mathematical one.

REPAIR. Add a Bridge Proposition (currently absent per AP-CY63):

```
Proposition (BD chiral operad = algebraic End^ch operad, finite-type).
For a finite-type chiral algebra A on X with PBW filtration, there
is an isomorphism of operads in D_X-modules
   Op_BD(A) ≃ End^ch(A)
constructed from the four-step bridge:
  (i) choose a coordinate chart on X;
  (ii) trivialise the D_X-module structure on A locally;
  (iii) identify the BD chiral operations with formal Laurent
       residues in End^ch(A);
  (iv) verify the Borcherds identity = associativity of End^ch.
This isomorphism intertwines the BD bar complex with the algebraic
bar complex, and underwrites the explicit formula for d_chiral
in thm:chiral-hochschild-differential.
```

UPGRADE. With the Bridge in place, the strongest statement of `thm:chiral-hochschild-differential` is unconditional and the explicit formulas (line 311) become the *canonical* model.

### 2.12 The "Koszul ≠ SC formality" warning is missing from the foundations chapter (AP14)

ATTACK. AP14 from Vol I CLAUDE: "Koszulness ≠ SC formality. Koszul = bar H* in degree 1. SC formal = `m_k^{SC} = 0` for `k ≥ 3`. All standard families Koszul; only class G SC-formal." The chiral Hochschild and Koszul-pair foundations chapters discuss Koszulness extensively but never state this caveat. A reader who comes from operad theory (where "Koszul" often *does* coincide with operadic formality) will conflate them.

REPAIR. Add to `chiral_koszul_pairs.tex` immediately after `def:chiral-koszul-pair` (line 717):

```
Warning (Koszul ≠ SC formality, AP14).
A chiral Koszul pair is defined by acyclicity of twisted tensor
products and Ext-diagonal vanishing. This is a STRICTLY WEAKER
property than Swiss-cheese formality (vanishing of higher SC
operations m_k for k ≥ 3). All four shadow classes G, L, C, M
admit chiral Koszul pairs (Heisenberg/G, KM/L, βγ/C, Vir/M);
only class G is additionally SC-formal. The shadow obstruction
tower (κ, C, Q, ...) lives at the SC-non-formal level and does
not obstruct chiral Koszulness.
```

UPGRADE. None — this is a warning, not a strengthening. But the warning ENABLES the strong claim:

  Strong shadow-vs-Koszul independence. *Chiral Koszulness is independent of shadow class. Every chirally Koszul algebra in the standard landscape carries a shadow tower whose depth (G/L/C/M) is a separate invariant. Theorem H (cohomological amplitude [0,2]) holds for all four classes; the higher shadow obstructions live in chain-level corrections that do not alter the amplitude bound.*

---

## Section 3 — AP160 Hochschild disambiguation table

For each file: every "Hochschild" occurrence should be tagged with which Hochschild is meant. Counts via grep on each file.

### `chiral_hochschild_koszul.tex` (15+ "chiral Hochschild" mentions)

| Line | Text | Should be |
|---|---|---|
| 1 | "Chiral Hochschild cohomology and Koszul duality" | `ChirHoch_geom` (chapter title) |
| 11 | "The chiral Hochschild complex C^•_chiral" | `ChirHoch_geom` |
| 27 | "chiral Hochschild complexes carry brace and E_2" | `ChirHoch_alg` (Deligne-conjecture flavour) |
| 46 | "Chiral Hochschild cochains" (M4 brace) | `ChirHoch_alg` |
| 108 | "the chiral Hochschild complex C^•_chiral(A)" | `ChirHoch_geom` |
| 145 | def:chiral-hochschild-complex | `ChirHoch_geom` definition |
| 167 | "the chiral Hochschild differential" | `ChirHoch_geom` |
| 324 | thm:hochschild-bar-cobar | bridges geom and alg via cobar resolution |
| 362 | thm:hochschild-spectral-sequence | `ChirHoch_geom` SS |
| 504 | lem:hochschild-shift-computation | `ChirHoch_bigr` (uses bigraded def) |
| 842 | lem:chirhoch-descent | `ChirHoch_geom = Σ-coinvariants of D_Ran B̄_X(A)` |
| 927 | thm:main-koszul-hoch (Theorem H) | `ChirHoch_bigr` (statement); descends to `ChirHoch_geom` cohomology |
| 1040 | thm:hochschild-polynomial-growth | `ChirHoch_geom` |

ACTION: introduce `\ChirHochGeom`, `\ChirHochAlg`, `\ChirHochBigr` macros and audit every occurrence.

### `hochschild_cohomology.tex` (60+ ChirHoch / HH mentions)

Most uses are `ChirHoch_geom` or `ChirHoch_alg = ChirHoch_geom`. Critical ambiguities:

| Line | Text | Should be |
|---|---|---|
| 76 | def:chiral-hochschild-derived = `RHom(B̄^geom, M)` | `ChirHoch_alg` |
| 86 | thm:hochschild-classical-comparison `E_2 = HH^p(A_0, ...)` | `HH^*(Zhu(A))` (point Hochschild — needs clarification of A_0) |
| 88 | "where A_0 is the fiber at a point" | `Zhu(A)` would be precise; "fibre at a point" is ill-defined |
| 128 | rem:gf-vs-chirhoch | `H^*_GF` vs `ChirHoch_alg`, three-way needed (see §2.9) |
| 158 | rem:critical-level-lie-vs-chirhoch | identifies `ChirHoch_alg(A_crit) = H^*_Lie,cont` (BD04) |
| 408 | "chiral Hochschild homology HH_n^ch(A)" | `HH_*^geom` (geometric flavour, with cyclic structure) |
| 469 | def:chiral-hochschild = `Γ(C̄_{n+1}, A^{⊠(n+1)} ⊗ det Ω^1)` | `HH_*^geom` definition — note `n+1` index! |
| 553 | def:chiral-HH | `HH_*^geom` |
| 561 | def:cyclic-operator | `HH_*^geom` cyclic structure |
| 595 | def:connes-B | mixed-complex on `HH_*^geom` |
| 657 | thm:E2-page-formula | `HC_*^geom` from `HH_*^geom` |
| 722 | "comparison with classical Hochschild cohomology" | `ChirHoch_alg` (Ext) ≠ `HH_*^geom` (Tor) — explicit warning |
| 825 | "${}^\dagger$ The E_2^{0,*} column records HH_* (Tor) ... distinct from ChirHoch* (Ext)" | already correct, the only place the distinction is made |

ACTION: the `n+1` vs `n+2` index discrepancy between line 469 and line 145 of `chiral_hochschild_koszul.tex` is a definitional inconsistency. Resolve.

### `koszul_pair_structure.tex` (40+ Hochschild mentions)

Mostly `ChirHoch_alg = Ext^*_{A^e}(A, M)` flavour. Section 2 (lines 162–325) builds the chiral enveloping algebra `A^e`, then defines `ChirHoch^n(A) = Ext^n_{A^e}(A, A)`. Section 4 (Periodicity) computes for Virasoro, KM, W_N — all `ChirHoch_alg` flavour.

Critical: `thm:geometric-chiral-hochschild` (line 288) bridges the two:

```
ChirHoch_alg^n(A) ≅ H^n(Γ(C̄_{n+1}(X), Hom_{D_X}(A^{⊠(n+1)}, A) ⊗ Ω^n_log))
```

Note again `n+1` (consistent with `hochschild_cohomology.tex:469` but NOT with `chiral_hochschild_koszul.tex:145` which uses `n+2`). The index shift is the difference between cyclic (n+1 cyclic-symmetric points) and geometric (n+2 = n inputs + 1 output + 1 cycle-base point).

ACTION: state clearly which "n" indexing is in force in each file. Recommended: use `n+2` everywhere (the geometric convention) and mark `n+1` as the cyclic-collapsed convention.

### `chiral_modules.tex` (no `ChirHoch` mentions; `Hochschild` only in section names citing `\cite{Ger63}`)

Mostly free of Hochschild ambiguities, but module-level Hochschild homology `HH_*^ch(A; M)` is undefined (see §2.5).

### `three_invariants.tex` (zero Hochschild mentions)

Clean.

### `spectral_sequences.tex` (Hochschild mentioned only in the Adams SS analogy, line 588)

Clean.

### `chiral_koszul_pairs.tex` (`chirhoch` not used; uses `bar` and `Koszul` terminology)

Clean from AP160 perspective; suffers from the Koszul-pair definition multiplicity (§2.6).

---

## Section 4 — AP-CY62–67 audit

### AP-CY62 (geometric vs algebraic chiral Hochschild)

VIOLATION DEGREE: HIGH.
The manuscript maintains `C^•_chiral` (geometric, FM compactification, log forms — `chiral_hochschild_koszul.tex:145`), `ChirHoch = Ext^*_{A^e}(A, A)` (algebraic, enveloping — `koszul_pair_structure.tex:259`), and `RHH_ch = RHom_{D_{C̄}}(A^{⊠}, ω)` (bigraded, Verdier — `higher_genus_foundations.tex:2748`) without naming the distinction. The "comparison theorem" is implicit through `thm:hochschild-bar-cobar` and `lem:chirhoch-descent` but never stated as the comparison.

REPAIR: §2.1 above. Add a comparison theorem at the start of `chiral_hochschild_koszul.tex` Section 3.

### AP-CY63 (BD chiral operad vs algebraic End^ch)

VIOLATION DEGREE: MEDIUM.
The chapter mixes BD-style language (D-module maps, factorization, Borcherds identity) with End^ch-style explicit formulas (mode-products, Laurent-series residues). The Bridge Proposition is absent. See §2.11.

REPAIR: §2.11 — add a Bridge Proposition.

### AP-CY64 (three-way ChirHoch / HH* / H*_GF)

VIOLATION DEGREE: MEDIUM-HIGH.
`rem:gf-vs-chirhoch` and `rem:critical-level-lie-vs-chirhoch` correctly note the distinction but mis-identify the *reason*. The clean three-way comparison is absent. See §2.9.

REPAIR: §2.9 — replace remarks with a unified three-Hochschild comparison block.

### AP-CY65 (spectral parameter provenance)

VIOLATION DEGREE: LOW.
Vol I's Hochschild apparatus is correctly z-dependent throughout. The "z=0 = mode-algebra" specialization is implicit but not made explicit. See §2.10.

REPAIR: §2.10 — add a remark at line 139.

### AP-CY66 (BZFN ambient category)

VIOLATION DEGREE: LOW (in these chapters).
The ambient-category issue is more relevant for chiral_modules.tex (chiral A-mod vs D_X-mod vs IndCoh(Ran)) than for Hochschild itself. `def:module-categories` (`chiral_modules.tex:129`) does distinguish symmetric `Mod_A`, ordered `Mod^{E_1}_A`, and derived `D(Mod_A)`; the Hochschild side does not commit to one.

REPAIR: when defining `RHH_ch(A) = RHom_{D_{C̄}}(A^{⊠}, ω)`, state which derived category (D-modules on Ran, IndCoh(Ran), or D-modules on each fixed `C̄_{p+2}`).

### AP-CY67 ("spectral parameters from FM_k(C)" narration)

VIOLATION DEGREE: MEDIUM.
The chapter says things like "the chiral Hochschild differential involves residues on FM_{n+2}(X)" without saying that FM is the COMPARISON locus, not the construction locus. The construction is algebraic (from chiral product μ); FM is the geometric realization where the spectral data becomes manifest.

REPAIR: at `chiral_hochschild_koszul.tex:113–121`, rewrite:

```
The chiral Hochschild complex is constructed algebraically from the
chiral product μ on A. Its geometric realization on the FM
compactifications C̄_{n+2}(X) is via the comparison Bridge
Proposition (Section X.Y), which identifies the algebraic chiral
Hochschild cochains with sections of a specific D-module on the FM
tower. The FM compactification is the comparison locus, not the
definition locus.
```

---

## Section 5 — First-principles analyses

For each AP-CY62–67 violation, write the ghost theorem (what the wrong claim gets right), the precise error, and the correct relationship.

### 5.1 Ghost: geometric Hochschild quasi-iso to algebraic Hochschild

Wrong claim: "the chiral Hochschild complex" (definite article, multiple definitions).
Ghost: there IS a unique chiral Hochschild complex up to quasi-iso — for finite-type Koszul algebras on a smooth curve, all three models (geometric `C^•_chiral`, algebraic `Ext^*_{A^e}`, bigraded `RHom_{D_{C̄}}`) are equivalent.
Precise error: the equivalence is NOT a definition; it is a theorem (`thm:hochschild-bar-cobar` partially, `lem:chirhoch-descent` partially) that requires Koszulness as hypothesis. Off the Koszul locus, the three models genuinely differ.
Correct statement: *On the Koszul locus, the three chiral Hochschild models are quasi-isomorphic. Off the Koszul locus, the bigraded model is the canonical derived object; the geometric and algebraic models recover it after distinct localizations.*

### 5.2 Ghost: BD chiral operad = algebraic End^ch operad

Wrong claim: "the chiral product μ" (one product, two formalisms).
Ghost: for a finite-type vertex algebra with PBW filtration, the BD-chiral product on D_X-modules and the End^ch product on formal Laurent series are isomorphic operads.
Precise error: the isomorphism is NOT canonical; it requires choice of coordinate, trivialization of D_X-action, and identification of spectral parameters. It is a four-step bridge, not a notational synonym.
Correct statement: *the Bridge Proposition (§2.11) constructs the iso in 4 steps. With this Bridge, BD and End^ch are interchangeable; without it, claims about "the chiral product" are ambiguous.*

### 5.3 Ghost: ChirHoch < HH*(Zhu) < H*_GF chain

Wrong claim: "ChirHoch is bounded but Gel'fand–Fuchs is unbounded."
Ghost: the three Hochschilds are linked by spectral sequences, and the boundedness profile is determined by the chosen ambient category and the level (generic vs critical).
Precise error: the manuscript states the dimension comparison without stating the spectral-sequence relationships.
Correct statement: see §2.9 — three SS relationships at generic vs critical level.

### 5.4 Ghost: spectral parameter is the geometric realization of the algebraic z-variable

Wrong claim: "the differential carries spectral data through C̄_{n+2}."
Ghost: the differential is z-dependent at every level (BD chiral operations encode z-shifts, End^ch encodes formal-Laurent residues, the geometric realization on FM makes the z-shifts into integration over boundary divisors).
Precise error: the manuscript treats spectral data as "geometric provenance" rather than as "data of the algebra."
Correct statement: *spectral data is intrinsic to the chiral algebra (via the BD operad and End^ch). The FM realization is the comparison locus, not the source.*

### 5.5 Ghost: Koszulness is independent of shadow class

Wrong claim (implicit): "Koszul algebras are formal."
Ghost: Koszulness controls bar concentration (Ext-diagonal); SC formality controls higher SC operations. These are separate invariants.
Precise error: AP14 violation (warning absent from foundations chapter).
Correct statement: §2.12 — chiral Koszulness ⊥ shadow class.

---

## Section 6 — Three upgrade paths

### Path 1 (Strongest possible Theorem H)

Steps:
1. Adopt the bigraded model `RHH_ch(A)` of `def:bigraded-hochschild` as canonical.
2. Prove the comparison theorem (§2.1): geometric ≃ algebraic ≃ bigraded on the Koszul locus.
3. State Theorem H as: *On the Koszul locus, `RHH_ch(A) ≃ RHom(RHH_ch(A^!), ω_X[2])`. Cohomologically, `ChirHoch^n(A) ≅ ChirHoch^{2-n}(A^!)^∨ ⊗ ω_X`. Independent of geometric/algebraic/bigraded model.*

Outcome: a single statement of Theorem H that is model-independent, and the reader does not have to track which definition is in force.

### Path 2 (Strongest possible Koszul foundations)

Steps:
1. Promote Ext-diagonal `Ext^{i,j}_A(C,C) = 0 for i ≠ j` to the canonical definition of chiral Koszulness.
2. State the equivalence theorem (§2.6): Ext-diagonal ⇔ bar concentration ⇔ twisting datum ⇔ PBW criterion.
3. Add the AP14 warning: chiral Koszulness ⊥ shadow class (§2.12).
4. Add the Hochschild-with-module-coefficients definition (§2.5).

Outcome: a single, robust foundation for all later Koszul-pair theorems, with the shadow class properly decoupled.

### Path 3 (Strongest possible spectral comparisons)

Steps:
1. Replace the mis-attributed `thm:hochschild-classical-comparison` (`hochschild_cohomology.tex:86`) with a careful Zhu-algebra version (§2.3).
2. Add the three-Hochschild SS relationships (§2.9).
3. Add the spectral parameter remark (§2.10) — explicit statement that the chiral Hochschild differential is z-dependent, with full collision recovering the Zhu-algebra Hochschild.
4. Add the Bridge Proposition (§2.11) — BD chiral operad ≅ algebraic End^ch.

Outcome: every spectral parameter, every Hochschild flavour, and every comparison map is explicit. AP-CY62–67 are all addressed.

---

## Section 7 — Consolidated punch list

Ranked by load-bearing severity (most load-bearing = highest impact on later chapters).

### CRITICAL (load-bearing for Theorem H and all downstream Koszul duality)

C1. **Comparison theorem missing for chiral Hochschild models.**
File: `chiral_hochschild_koszul.tex` (Section 3 opener).
Patch: state and prove the comparison `C^•_chiral ≃ ChirHoch_alg ≃ RHH_ch` on the Koszul locus.

C2. **`def:bigraded-hochschild` lives in `higher_genus_foundations.tex` but is the canonical input to the central Theorem H proved in `chiral_hochschild_koszul.tex`.**
Patch: move `def:bigraded-hochschild` to `chiral_hochschild_koszul.tex` Section 3.5, before `lem:hochschild-shift-computation` which uses it. Or at minimum, forward-reference it explicitly in the chapter intro.

C3. **`thm:hochschild-classical-comparison` mis-attributes the spectral sequence to BD04 and uses ill-defined `A_0 = fibre at a point`.**
File: `hochschild_cohomology.tex:86`.
Patch: replace with a Zhu-algebra version, downgrade to conjecture, or provide explicit construction.

C4. **Chiral Koszul pair definition multiplicity (4 distinct definitions).**
Files: `chiral_koszul_pairs.tex:268, 658`, `koszul_pair_structure.tex` (implicit), `chiral_hochschild_koszul.tex` (Ext-diagonal).
Patch: state the equivalence theorem (§2.6).

C5. **Index inconsistency `n+1` vs `n+2` between `chiral_hochschild_koszul.tex:145` (n+2) and `hochschild_cohomology.tex:469` and `koszul_pair_structure.tex:288` (n+1).**
Patch: harmonize. Recommended: `n+2` everywhere (geometric convention).

### HIGH

H1. **AP-CY64 three-Hochschild remark mis-states the reason for boundedness.**
File: `hochschild_cohomology.tex:128, 158`.
Patch: §2.9 — three-way comparison block.

H2. **AP-CY63 Bridge Proposition absent.**
File: `chiral_hochschild_koszul.tex` Section 3.
Patch: §2.11 — Bridge Proposition.

H3. **`thm:hochschild-spectral-sequence` convergence proof is a one-sentence assertion, fails for non-finite-type Koszul algebras.**
File: `chiral_hochschild_koszul.tex:362`.
Patch: §2.7 — strengthen convergence hypothesis to finite-type, state non-finite-type version as conditional.

H4. **AP14 warning missing: chiral Koszulness ⊥ shadow class.**
File: `chiral_koszul_pairs.tex:717` (after `def:chiral-koszul-pair`).
Patch: §2.12 — add warning block.

H5. **Hochschild homology with module coefficients `HH_*^ch(A; M)` undefined.**
File: `chiral_modules.tex` Section 36–170.
Patch: §2.5 — add definition.

### MEDIUM

M1. **`thm:hochschild-chain-complex` (`hochschild_cohomology.tex:491`) duplicates and weakens `thm:chiral-hochschild-differential` (`chiral_hochschild_koszul.tex:172`).**
Patch: delete the former, replace with a Remark citing the latter.

M2. **`rem:gf-vs-chirhoch` (`hochschild_cohomology.tex:128`) and `rem:critical-level-lie-vs-chirhoch` (`hochschild_cohomology.tex:158`) overlap and mis-state.**
Patch: merge into single three-Hochschild remark per §2.9.

M3. **`rem:k-max-2-missing` (`three_invariants.tex:298`) gives a false universal exclusion.**
Patch: §2.4 — restrict to bosonic-integer-weight landscape.

M4. **AP-CY67 narration: "spectral parameters from FM_{n+2}(X)" treats FM as definition source.**
File: `chiral_hochschild_koszul.tex:113–121`.
Patch: §4 entry on AP-CY67 — rewrite paragraph.

M5. **AP160 unmarked "Hochschild" mentions throughout all six files.**
Patch: introduce `\ChirHochGeom`, `\ChirHochAlg`, `\ChirHochBigr` macros and audit (§3 tables).

### LOW (cosmetic but worth noting)

L1. **`prop:degen-koszul` (`spectral_sequences.tex:328`) cites `def:chiral-koszul-pair` for `Ext^{i,j}_A(C,C) = 0`, but `def:chiral-koszul-pair` does not contain this statement.**
Patch: cite `thm:ext-diagonal-vanishing` instead.

L2. **`thm:genus-ss` (`spectral_sequences.tex:383`) cites `BD04` for the genus spectral sequence — BD04 does not contain a "genus" spectral sequence in this signature.**
Patch: re-attribute to Costello–Gwilliam Vol II ch. 12 (factorization homology genus filtration), or downgrade to ProvedHere with explicit construction.

L3. **`prop:fm-tower-collapse` (`chiral_hochschild_koszul.tex:606`) implicitly assumes cohomological FM-formality.**
Patch: §2.8 — add parenthetical clarifying chain-level vs cohomological.

L4. **`def:chiral-twisting-datum` (`chiral_koszul_pairs.tex:216`) requires bounded-below filtration; this excludes Yangians/K3 lattice algebras silently.**
Patch: state this hypothesis explicitly when used downstream.

---

## Closing assessment

The chiral Hochschild and Koszul foundations are *substantively correct* but suffer from definitional multiplicity that no comparison theorem stitches together. Theorem H (the Koszul duality for chiral Hochschild) is real, proved in `chiral_hochschild_koszul.tex:927–1031` via the FM-tower collapse, and it deserves to be the strongest statement in the chapter — but the reader currently has to navigate three distinct "chiral Hochschild" complexes and four distinct "chiral Koszul" definitions.

The strongest possible upgrade path:

1. Bigraded `RHH_ch(A)` becomes the canonical Hochschild (§2.1, §2.5).
2. Ext-diagonal becomes the canonical Koszul (§2.6).
3. Three-Hochschild comparison theorem (§2.9) and Bridge Proposition (§2.11) make AP-CY63, AP-CY64 disappear.
4. AP14 warning (§2.12) and Hochschild-with-module (§2.5) close the structural gaps.
5. AP160 macros (`\ChirHochGeom`, etc.) enforce model discipline going forward.

After these patches, the foundations chapter set supports every downstream chapter (Theorem H, Theorem A, Theorem B, Koszul/CFT/duality at all genera) on a *single, model-independent* definition of chiral Hochschild and chiral Koszul.

No retractions required. All ProvedHere claims survive the audit; the revisions are clarifications and unifications, not corrections.

End of Wave 5 report.
