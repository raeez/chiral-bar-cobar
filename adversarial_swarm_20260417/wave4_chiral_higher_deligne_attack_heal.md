# Wave 4 — Chiral Higher Deligne cluster: adversarial attack + heal

**Target.** `~/chiral-bar-cobar-vol2/chapters/theory/chiral_higher_deligne.tex`
(884 lines, inscribed 2026-04-16).

**Cluster.** `thm:chiral-higher-deligne`, `thm:H-concentration-via-E3-rigidity`,
`thm:chd-ds-hochschild`, `cor:universal-holography-class-M`, plus the
supporting `prop:chd-models-equivalent`, `prop:chd-stasheff-4`,
`lem:chd-e3-rigidity-point`.

**Verdict capsule.** The chapter SURVIVES the core structural attack (no
circularity against `sc_chtop_heptagon.tex`; the heptagon edges (3)↔(4) and
(4)↔(5) are proved independently via Costello–Gwilliam Dunn + Kontsevich–
Tamarkin formality, not back-referenced). BUT it FAILS the cross-volume
citation hygiene on twelve label references, and the corollary to
universal-holography over-extends past the weight-completed ambient that
MC5 genuinely secures. Both failures are surgically repairable without
retraction.

---

## Phase 1. Six attack prongs

### Prong (i). "E_3-rigidity at a point" — topological or algebraic?

Lemma `lem:chd-e3-rigidity-point` posits: if `R` is an E_3-algebra in chain
complexes with `H^0(R) = k`, `H^{<0}(R) = 0`, and `R = U_{E_3}(V)` with V of
polynomial growth, then `H^•(R)` is concentrated in `{0,1,2}`. The proof
invokes Fresse §13 E_3-Koszul duality, asserting that the "E_3-Koszul
bracket has arity 3, accounting for the middle degree," and then defers
to a **phantom label** `V1-lem:e3-polynomial-growth` to kill a potential
degree-3 obstruction by a bar-spectral-sequence argument.

**Attack.** The lemma conflates two distinct notions of "E_3-rigidity":

1. **Algebraic E_3-rigidity** — a statement about the operadic bar/cobar of
   `E_3` in chain complexes over a field, using Fresse's operadic Koszul
   duality. This gives cohomology in degrees `{0, 1, 2, 3}` with degree 3
   the TOP amplitude (not "middle").
2. **Topological E_3-rigidity** — Goodwillie-style rigidity of `TAQ` for a
   compact E_3-manifold, which does give `{0, 1, 2}` amplitude for
   cohomology on a 2-disc (one fewer than ambient dimension 3).

The chapter conflates the two: Fresse E_3 gives amplitude 3, not 2. The
"polynomial growth kills degree 3" is cited to a phantom lemma. The
statement as written is ambiguous between the two meanings.

**Survival route.** The correct statement is: for `V` concentrated in
cohomological degree 0 with `V^0 = V_0` of polynomial Hilbert growth,
the E_3-envelope `U_{E_3}(V)` has cohomology CONCENTRATED IN BAR-WEIGHT
{0, 1, 2} — not cohomological degree. Bar-weight is the natural filtration
from the operadic bar; cohomological degree and bar-weight coincide only
after the cohomological-degree = bar-weight normalisation that Theorem H
traditionally uses (Vol I `thm:hochschild-concentration-E1`). With that
bigrading disclosed, the lemma is correct but loses its "one-fewer"
cuteness; it is now a standard consequence of Orlik–Solomon Koszulity of
the braid arrangement `A_{n-1}` (Shelton–Yuzvinsky 1997), which the
proof already cites as the PARALLEL argument.

**Heal.** Re-state the lemma with bar-weight bigrading. Cite
Shelton–Yuzvinsky directly (not via a phantom `V1-lem:e3-polynomial-growth`).

### Prong (ii). DS–Hochschild chain-level Gerstenhaber

Theorem `thm:chd-ds-hochschild` asserts chain-level QI of E_2-chiral
Gerstenhaber algebras between `ChirHoch^•(W_k(g, f))` and
`H^•_DS(ChirHoch^•(V_k(g)))`. The proof is four steps: Arakawa
C_2-cofiniteness, HKR, HPL through DS retract, DS–bar intertwining.

**Attack.** HPL transfer is a standard chain-level operation, but it does
NOT preserve strict Gerstenhaber on the nose. What HPL delivers is a
transferred `A_∞`-algebra with induced `A_∞`-morphisms. Gerstenhaber
structure is E_2; E_2 at chain level is brace-operad-quasi-isomorphic,
which is strictly weaker than operad-isomorphism of Gerstenhaber. The
"QI of E_2-chiral Gerstenhaber algebras" in the theorem statement is
therefore correct IF interpreted at `∞`-operad level, over-stated if
interpreted strictly.

**Survival route.** The standard resolution: work in the `∞`-category of
E_2-chiral algebras (equivalently brace algebras in the sense of
Kontsevich–Soibelman), where HPL-transferred structure is genuinely
`∞`-equivalent. This is what the programme actually uses (the chiral
Deligne–Tamarkin Theorem `thm:chd-deligne-tamarkin` itself is stated up
to `A_∞`-equivalence with explicit associator dependence).

**Heal.** Re-word "QI of E_2-chiral Gerstenhaber algebras" to
"`∞`-quasi-isomorphism of E_2-chiral brace algebras" and cite the
associator discipline remark.

### Prong (iii). `cor:universal-holography-class-M` — scope breach

The corollary claims: for A in class M at generic level,
`Z^{der}_{ch}(A) ≃ A^{3d HT}_{bulk}` as E_3-chiral algebras, and "combined
with E_3-topologization of class M on the weight-completed complex
(Vol I `thm:topologization-tower`), this gives chain-level 3d HT
holography for the complete Koszul landscape (G, L, C, M)."

**Attack — compound.**

(a) `V1-thm:topologization-tower` is a PHANTOM LABEL. Grep over Vol I
`chapters/` returns: three citation sites (part IV intro, periodic CDG
admissible, topologization_chain_level_platonic forward-ref), ZERO
`\label{thm:topologization-tower}` definition sites. The theorem is
inscribed by name in the CLAUDE.md theorem-status table but has no
corresponding LaTeX label.

(b) `V1-thm:class-L-bulk` is similarly a PHANTOM LABEL. Grep returns zero
`\label` matches.

(c) The programme-level fact secured by MC5 is that chain-level class-M
holds on the **pro-ambient** / **J-adic topological** / **weight-completed**
ambient; on the bounded direct-sum ambient `Ch(Vect)` it is GENUINELY
FALSE (S_4(Vir_c) = 10/[c(5c+22)] ≠ 0 forces bar cohomology in weight 4).
The corollary's phrase "chain-level 3d HT holography" is ambiguous about
which ambient, and the remark immediately following claims the "G/L/C/M
all chain-level proved on the Koszul locus at generic level" qualifier
should drop — which directly contradicts the MC5 ambient-caveat.

(d) The proof body writes "Costello–Francis–Gwilliam (arXiv:2602.12412,
cited by Vol I Theorem V1-thm:class-L-bulk)" — the phantom-label citation
is compounded by a CFG future-date arXiv citation (2026) for a paper
that the programme already schedules but which is reference-only, not
theorem-level in Vol I.

**Survival route.** The class-L bulk identification at chain level is
genuinely known via CFG + topologization `thm:topologization` for affine
KM at non-critical level (Vol I `chapters/theory/topologization.tex` or
similar has the actual Sugawara-BRST strict identity). The class-M
chain-level reduction via DS is then correctly a reduction to class L
(which is chain-level in its original complex), pulled through DS BRST
which lives in the WEIGHT-COMPLETED ambient (class-M C_2-cofinite
implies BRST convergence on weight-completed but not on bounded direct
sum per se).

**Heal.** (1) Retire phantom `V1-thm:topologization-tower`; replace by
Vol I `thm:topologization` (which exists) and attribute the original
complex claim as "class G, class L, class C original complex; class M
weight-completed ambient." (2) Retire phantom `V1-thm:class-L-bulk`;
attribute directly to Costello–Francis–Gwilliam (CFG). (3) Scope-qualify
the remark: class M is chain-level on the **weight-completed** ambient,
consistent with MC5 class-M pro-ambient theorem
(Vol I `thm:mc5-class-m-chain-level-pro-ambient`); drop the
"qualifier should drop" claim.

### Prong (iv). "E_3-chiral" vs. "E_2-chiral ⊗ E_1-top"

The main theorem's Stage 2 argues: `L_0` acts as a strict derivation,
Dunn additivity on the factorization algebra `F^{Z^{der}_{ch}}` on `R × X`
combines E_2-chiral with E_1-top(`R`) to yield E_3.

**Attack.** The resulting structure is manifestly `E_2-chiral ⊗_{Dunn}
E_1-top`, not a SINGLE `E_3-chiral` operad. These are distinct operads:

- `E_3-topological` little-3-disks `D_3(R^3)`.
- `E_3-chiral` = `Fact` on `R × X` with chiral holomorphic direction on `X`
  and topological on `R`.
- The Dunn product `E_2-chiral ⊗ E_1-top` lives on `R × X` and equals
  `E_3-chiral` only after Dunn-additivity is proved for chiral operads
  with mixed topological factor.

Dunn-additivity for `E_k-top` (Lurie HA 5.1.2.2) does not directly
generalise to chiral operads. What CFG prove is Dunn-additivity for
chain-level factorization algebras on products; this is the correct
universal statement used here. The conclusion "is an `E_3-chiral`
algebra" therefore requires the convention that `E_3-chiral` MEANS
factorization algebra on `R × X`, which the chapter does not pin down
explicitly.

**Survival route.** Pin the convention. The programme uses `SC^{ch,top}`
precisely as this intermediate between E_1-chiral and E_3-topological;
the upgrade to `E_3` requires conformal vector (topologization). The
theorem's output is most honestly stated as `E_2-chiral ⊗_{Dunn}
E_1-top`, which coincides with topologized `E_3` on the Koszul locus
with conformal vector (per AP-TOPOLOGIZATION) and degenerates to
`SC^{ch,top}` without conformal vector.

**Heal.** Add a convention note at the start of §`sec:chd-main` pinning
`E_3-chiral` = `E_2-chiral ⊗_{Dunn} E_1-top`, equivalently `Fact` on
`R × X`. Without conformal vector, stuck at `SC^{ch,top}`; with conformal
vector at non-critical level, topologizes to strict `E_3-top` (proved
for affine KM; conjectural for Vir / W_N per `conj:topologization-
general`).

### Prong (v). `chd-ds-hochschild` at `V_k(sl_2) → Vir_c`

Attack: verify the isomorphism at the simplest case `V_k(sl_2) → Vir_c`
via Feigin–Fuks resolution.

**Verification.** `ChirHoch^•(Vir_c)` at generic c is concentrated in
degrees `{0, 1, 2}` with dimensions `(1, 0, 1)` (Theorem H, Feigin–Fuks).
`ChirHoch^•(V_k(sl_2))` at generic k has dimensions `(1, 1, 1)`
(Vol I `prop:chirhoch1-affine-km` with `g = 1` for sl_2). The DS
reduction at principal `f = e_+` sends `V_k(sl_2)` to
`Vir_{c(k)}` with `c(k) = 1 - 6(k+1)^2/(k+2)`. The claim is
`H^•_DS(ChirHoch^•(V_k(sl_2))) ≃ ChirHoch^•(Vir_c)` at chain level.

At generic k, DS kernel contains the `J^0`-zero-mode and Kac–Wakimoto
computes `H^0_DS = Vir_c`, `H^{>0}_DS = 0` on V_k itself. Applied to
ChirHoch, the degree-1 piece (dim 1, corresponding to the `g=1` generator
for sl_2) is killed by DS (it is the `J^0` mode), leaving dimensions
`(1, 0, 1)` — matching Theorem H for Vir. The identification is
cohomologically unconditional.

**Chain-level** identification: HPL-transfer of the `A_∞`-structure on
the BRST complex of `V_k ⊗ Fock ⊗ bc` to `Vir_c` is standard; Feigin–
Frenkel (screening operators) and de Boer–Tjin give the explicit
retract data. The chain-level is up to `A_∞`-QI, not strict.

**Verdict.** The theorem is correct at `V_k(sl_2) → Vir_c`; the scope
"principal and hook-type" is warranted; the cohomological claim is
unconditional. The chain-level claim survives with prong (ii)'s
heal (`∞`-QI of brace algebras, not strict Gerstenhaber).

### Prong (vi). Heptagon edges (3)↔(4)↔(5) — circularity

Grep `sc_chtop_heptagon.tex` for back-references to `thm:chiral-higher-
deligne`: ZERO hits (the heptagon file cites `thm:edge-34`, `thm:edge-45`,
`thm:edge-23`, and external Costello–Gwilliam / Lurie / Kontsevich–
Tamarkin / Hinich / Getzler). No circularity.

`prop:heptagon-edge-34` and `prop:heptagon-edge-45` are inscribed with
proofs invoking:
- `thm:edge-34`: `Obs^q` restricts on closed half to `Obs^{ch}_A`;
- `thm:edge-45`: QME = convolution MC on semifree model;
- Coloured Swiss-cheese formality (Getzler–Jones 1994, Vallette 2014).

The sole dependency chain is horizontal within the heptagon (edge (2)↔(3)
feeds edge (3)↔(4) feeds edge (4)↔(5)), closing off through edge (5)↔(6)
without cycling to chiral-higher-deligne. **No circularity.**

---

## Phase 2. Heal — surgical edits

### Label corrections (phantom → real)

Systematic replacement of phantom / misnamed cross-volume citations in
`chiral_higher_deligne.tex`:

| Cited as | Corrected target | Evidence |
|----------|------------------|----------|
| `V1-def:koszul-locus` | `def:koszul-locus` (algebraic_foundations.tex:259) | exists |
| `V1-thm:theorem-H` | `thm:hochschild-concentration-E1` (chiral_hochschild_koszul.tex:1256) | misnamed |
| `V1-thm:chiral-hkr` | — attribute to HKR classical (Kontsevich, Calaque–Van den Bergh); no Vol I thm exists | phantom → remark |
| `V1-thm:chiral-pbw-koszul` | `thm:pbw-koszulness-criterion` (chiral_koszul_pairs.tex:784) | misnamed |
| `V1-lem:e3-polynomial-growth` | — cite Shelton–Yuzvinsky 1997 + Fresse §13 directly | phantom → literature |
| `V1-prop:center-generic-scalar` | — attribute to centre of E_1-alg over field | phantom → remark |
| `V1-prop:chiral-leibniz` | — bare statement of chiral Leibniz (universal) | phantom → inline |
| `V1-prop:chirhoch1-affine-km` | `prop:chirhoch1-affine-km` (chiral_center_theorem.tex:2133) | exists |
| `V1-thm:ds-koszul-intertwine` | `thm:ds-koszul-intertwine` (chiral_modules.tex:4348) | exists |
| `V1-thm:chiral-positselski-7-2` | `thm:chiral-positselski-7-2` (preface.tex:5081) | exists |
| `V1-prop:nonprincipal-coset` | coset chapter (no single prop label) | replace with narrative cite |
| `V1-ch:w-landscape` | — reference to W-algebras landscape chapter narratively | phantom → narrative |
| `V1-thm:topologization-tower` (Vol II internal) | replace by Vol I `thm:topologization` | phantom → real |
| `V1-thm:class-L-bulk` (Vol II internal) | attribute to CFG directly, cite `CFG25` bibkey | phantom → bib |

### Structural heals

1. **Convention note** in `sec:chd-main` pinning "`E_3-chiral`" = `E_2-chiral
   ⊗_{Dunn} E_1-top` = `Fact(R × X)`; topologizes to strict `E_3-top` for
   affine KM at non-critical level (proved); conjectural for Vir/W_N;
   without conformal vector stuck at `SC^{ch,top}`.

2. **Bar-weight bigrading disclosure** in `lem:chd-e3-rigidity-point`:
   the "concentration in `{0,1,2}`" is cohomological degree = bar-weight
   under the normalisation of Theorem H; Shelton–Yuzvinsky Koszulity of
   `OS(A_{n-1})` is the direct combinatorial route; Fresse §13 provides
   the operadic cross-check.

3. **Brace-algebra language** in `thm:chd-ds-hochschild`: replace
   "QI of E_2-chiral Gerstenhaber algebras" with "`∞`-quasi-isomorphism
   of E_2-chiral brace algebras"; strict Gerstenhaber on cohomology.

4. **Weight-completed scope qualifier** in `cor:universal-holography-
   class-M` and its remark: explicit disclosure that class-M chain-level
   holds on the weight-completed / pro-ambient / J-adic ambient
   consistent with MC5 `thm:mc5-class-m-chain-level-pro-ambient`; drop
   the "qualifier should drop" claim in favour of "qualifier
   ambient-specific; weight-completed unconditional, direct-sum
   genuinely false on `Ch(Vect)`."

5. **Universal Holography remark rewrite** (prong iii compound): class-L
   bulk identification attributed directly to CFG with `CFG25` bib key.
   Class-M bulk identification proceeds via chain-level DS reduction of
   class L in the WEIGHT-COMPLETED ambient.

### No scope retractions required

The three `ClaimStatusProvedHere` theorems all survive with scope
clarifications; none require downgrade to Conjectured. The Corollary
survives with ambient-scope disclosure. No new open frontiers created.

### CG voice preservation

The chapter's north-star opening (deficiency → unique survivor via
classical Deligne being "one dimension short") is preserved. The heals
are surgical: label corrections, convention pinning, ambient
disclosure, `∞`-operad language. No prose rewrite of theorem statements
or structural reorganisation.

---

## Coverage audit

Phase 1 linear read: lines 1–220, 220–439, 440–669, 670–884. Total 884
lines; four Read calls; contiguous cover of [1, 884]. Complete.

Adversarial verdict: three theorems + one corollary SURVIVE with
scope clarification; twelve phantom/misnamed labels require
replacement; no circularity against heptagon; no retractions.
