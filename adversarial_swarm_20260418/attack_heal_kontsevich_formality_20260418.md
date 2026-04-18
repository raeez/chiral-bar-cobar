# Attack-Heal: Kontsevich formality usage in Vol I (2026-04-18)

## Mission

Adversarial audit of Kontsevich / Fresse--Willwacher / Tamarkin
formality in Vol I: (i) usage inventory; (ii) Theorem H
Fresse-transport non-degeneracy step at collision divisors
(`lem:chiral-quadratic-koszul`); (iii) H02 ALT proof of Theorem B
(Keller deformation + Kontsevich formality); (iv) AP-CY33 compliance
(chain-level E_n collapses under formality in rational / cohomology
category; claims must distinguish chain-level from cohomological).

## Phase 1: Usage inventory

Non-exhaustive sites where "Kontsevich formality" or a closely named
variant ("$E_n$ formality", "chiral formality", "Tamarkin formality",
"graph-complex formality") is invoked in Vol I:

| Site | File : line | Nature of invocation | Scope status |
|------|-------------|----------------------|--------------|
| T1 | `chapters/theory/cobar_construction.tex:1822` | `thm:kontsevich-formality`, ProvedElsewhere, statement of the classical theorem | Correctly ProvedElsewhere |
| T2 | `chapters/theory/en_koszul_duality.tex:1069` | `prop:en-formality`, ProvedElsewhere, Fresse--Willwacher + Idrissi | Correctly ProvedElsewhere |
| T3 | `chapters/theory/en_koszul_duality.tex:854,1035,2548,2735` | En formality / deformation quantization / SC^ch,top Quillen equivalence / homotopy-Koszulity deepest input | Prose-level references, correctly scoped in context |
| T4 | `chapters/theory/chiral_hochschild_koszul.tex:719` | Step 1 of `lem:chiral-quadratic-koszul`, invoked to secure non-degeneracy of OPE-residue pairing at collision divisors | PRE-HEAL: loose phrasing; HEALED this wave |
| T5 | `chapters/theory/chiral_hochschild_koszul.tex:792` | FM fiber formality identification with Arnold algebra (Step (ii) of `prop:fm-tower-collapse`) | Correctly cohomological ("real cohomology algebra is the Arnold algebra") |
| T6 | `chapters/theory/chiral_hochschild_koszul.tex:6995,7025,7126` | `conj:graph-complex-shadow` Φ: gAmod → GC_2 via Kontsevich formality; shadow invariants -> wheel cocycles | Correctly `\ClaimStatusConjectured` with in-file Heuristic comment at 6999-7005 |
| T7 | `chapters/theory/motivic_shadow_full_class_m_platonic.tex:165,587` | "E_2 topological side receives the Kontsevich formality quantisation"; MZV periods populate via Phi_KZ | Associator-dependence inscribed at AP171 / `prop:associator-dependence-explicit` |
| T8 | `chapters/theory/koszulness_moduli_scheme.tex:675-677` | SC^ch,top chord-diagram IHX/STU via Kontsevich formality for 2-coloured little disks; cites `\ref{rem:sc-chtop-formality}` | PRE-HEAL: phantom `\ref` (AP264); HEALED this wave |
| T9 | `chapters/theory/e3_identification_chain_level_platonic.tex:411-473` | `thm:e3-identification-chain-level-associator-fixed`, Fresse Vol II Thm 16.2.1 + Phi_KZ rigidification | Model citizen; explicit associator rigidification + GRT_1-torsor inscribed |
| T10 | `chapters/theory/chiral_koszul_pairs.tex:1316,2550,2914` | "Keller classicality" fiberwise on FM strata for A_inf transfer | Correctly scoped, forward direction proven; reverse direction references the same passage |
| T11 | `chapters/examples/deformation_quantization.tex:575` | `thm:chiral-formality`, ProvedElsewhere to Tamarkin 2000 + FG12; L_inf QI T^ch_poly(X) -> C*_ch(T_X) | Correctly ProvedElsewhere |
| T12 | `chapters/examples/deformation_quantization.tex:147` | Used inside `thm:chiral-quantization` (genus-0 coisson quantization, ProvedHere) | Proof routes through E_2-formality at cohomology; correctly scoped |
| T13 | `chapters/connections/feynman_diagrams.tex:240-251` | `thm:kontsevich-formality-feynman`, ProvedElsewhere; Remark on chiral analogue | Prose only |
| T14 | `chapters/connections/concordance.tex:4647` | SC^ch,top homotopy-Koszulity in Vol II via Kontsevich formality + classical SC transfer | Defers to Vol II; correctly scoped |
| T15 | `chapters/frame/preface.tex:4407` | "Kontsevich formality supplies Phi: SC^ch,top -> SC quasi-isomorphism"; bar-cobar is Quillen equivalence | NO SCOPE LABEL; documented but not edited this wave per AP314 |
| T16 | `chapters/frame/preface_sections10_13_draft.tex:72` | Identical to T15 | NO SCOPE LABEL; documented but not edited this wave per AP314 |

## Phase 2: Diagnostic by mission subpart

### (i) Usage inventory

Sixteen distinct classes of invocation; the three most load-bearing for
audit purposes are T4 (Theorem H Fresse-transport Step 1), T9 (chain-level
E_3 identification at fixed associator), and T8 (SC^ch,top
homotopy-Koszulity in Vol I prose).

### (ii) Theorem H `lem:chiral-quadratic-koszul` Step 1 at collision divisors

The pre-heal text at `chiral_hochschild_koszul.tex:717-720` reads:

> where the pairing specialises (collision divisors), the specialisation
> factors through the local model FM_3(C), where the pairing is again
> non-degenerate by Kontsevich formality (Proposition prop:en-formality).

The ACTUAL mechanism is not "Kontsevich formality gives non-degeneracy
directly"; it is: (a) E_n-formality at n=3 identifies the real cohomology
H^*(FM_3(C); R) with the Arnold algebra as a Pn-algebra; (b) on the Arnold
algebra the classical composition pairing is non-degenerate (Fresse
Prop. 7.1.3, already cited one line earlier for the generic-point step);
(c) the OPE-residue pairing on the local model specialises to this
cohomological Arnold pairing via descent of cohomology classes.

The loose phrasing "non-degenerate by Kontsevich formality" risks AP-CY33:
a reader may infer either that formality is giving a chain-level
E_3-structure statement (it is not) or that the pairing non-degeneracy at
collision divisors is a direct consequence of the formality theorem
independently of Fresse Prop. 7.1.3 (it is not; Fresse is the load-bearing
non-degeneracy statement, formality only supplies the cohomological
identification needed to apply Fresse at the singular point).

HEAL (this wave): rewrite Step 1 at `chiral_hochschild_koszul.tex:717-725`
to make the two-step structure explicit — (a) cohomological
En-formality identifies H^*(FM_3(C); R) with the Arnold algebra,
(b) Fresse Prop. 7.1.3 gives non-degeneracy on the Arnold algebra —
with an explicit parenthetical "(used here only at the cohomology level,
not as a chain-level En-structure claim)". This closes the AP-CY33
propagation risk without weakening the lemma.

### (iii) H02 ALT proof of Theorem B

CLAUDE.md (pre-heal) and AGENTS.md Table "Alternative Proofs Secured"
advertise Theorem B H02 ALT as "Keller deformation + Kontsevich formality".
`programme_overview_platonic.tex:458-459` and
`worldview_synthesis_2026_04_17.tex:853` carry the same advertisement.

Grep for an inscribed H02 theorem body in Vol I:
- Keller side: inscribed as `thm:ainfty-koszul-characterization`
  (`chiral_koszul_pairs.tex:1300`), forward + reverse direction,
  ProvedHere, with fiberwise HPL transfer + Keller classicality on
  each FM stratum. This is the "Keller" half of the advertisement.
- Kontsevich-formality side: `thm:chiral-formality` at
  `deformation_quantization.tex:575` is ProvedElsewhere (Tamarkin 2000 +
  FG12); it supplies the L_inf QI T^ch_poly(X) ~ C*_ch(T_X), NOT an
  alternative Theorem-B proof.
- No theorem body composes the two into an ALT proof of Theorem B. The
  preface chain of equivalences at `preface.tex:3925-3926` names
  "A_inf-formality branch via HPL transfer and Keller classicality",
  which is the Keller side; Kontsevich formality is not part of the
  inscribed composition.

Conclusion: the H02 ALT proof is PARTIALLY inscribed (Keller half via
`thm:ainfty-koszul-characterization`, routed through PBW collapse); the
"Kontsevich formality" branding of the ALT is a meta-prose artefact not
backed by an inscribed composite. This is AP241
(advertised-but-not-inscribed characterization) at the meta-level,
subsumed under AP1361 discipline. No new inscription forced: the Keller
half already gives a genuinely independent alt path to formality and
hence to Theorem B. The Kontsevich-formality half would be an
independent third route (configuration-space graph-integral), which is
not inscribed; removing the "Kontsevich formality" branding from the
meta-prose would more honestly reflect the inscribed content. Flagged,
not edited this wave per AP314.

### (iv) AP-CY33 propagation audit

AP-CY33 states: "chain-level != rational (E_3 collapses under formality)."
The concern is that programme theorems claiming "chain-level E_3" that
route through formality may be silently rationalising.

Sweep for chain-level E_3 claims routed through formality:

1. `thm:e3-identification-chain-level-associator-fixed`
   (`e3_identification_chain_level_platonic.tex:411`). This IS a
   chain-level claim, routed through Fresse Vol II Thm 16.2.1 + Phi_KZ.
   The theorem handles AP-CY33 correctly by fixing Phi_KZ explicitly,
   inscribing associator-dependence at `prop:associator-dependence-explicit`,
   and isolating which part of the identification survives at cohomology
   (associator-independent) vs cochain level (GRT_1-torsor dependent).
   Model citizen.

2. `thm:operad-level-to-algebra-level-lift`
   (`e3_identification_chain_level_platonic.tex:742`). Chain-level lift
   via Fresse 16.2.1; correctly predicated on fixing Phi and on strict
   compatibility with filtration.

3. `conj:graph-complex-shadow` (`chiral_hochschild_koszul.tex:7006`).
   Correctly `\ClaimStatusConjectured` with explicit comment at
   6999-7005 that the Phi map is "described but not rigorously
   constructed"; this pre-empts AP-CY33.

4. `thm:chiral-formality` (`deformation_quantization.tex:575`). At the
   statement level gives an L_inf QI; chain-level, but the proof is
   ProvedElsewhere (Tamarkin 2000 + FG12). Correctly scoped.

5. Preface passage `preface.tex:4407` on "Kontsevich formality supplies
   Phi: SC^ch,top -> SC quasi-isomorphism". This is a cohomology-level
   statement in context (the Quillen equivalence on bar-cobar is
   cohomological / homotopy-category-level), but carries NO scope label.
   Future edits to preface should add "(cohomology level)" or
   "(homotopy category)" qualifier. Flagged.

No outright AP-CY33 VIOLATION detected; every chain-level E_3 claim
routes through Fresse Vol II Thm 16.2.1 with explicit associator
rigidification, and the cohomological invocations correctly stay at
cohomology.

## Phase 3: Heals applied

### Heal A: `chiral_hochschild_koszul.tex:717-725`

Pre-heal: "specialisation factors through the local model FM_3(C),
where the pairing is again non-degenerate by Kontsevich formality
(Proposition prop:en-formality)."

Post-heal: explicit two-step structure making the cohomological vs
chain-level distinction visible, with Fresse Prop. 7.1.3 named as the
actual non-degeneracy source and formality confined to the cohomological
identification of FM_3(C) with the Arnold algebra. An inline
parenthetical "used here only at the cohomology level, not as a
chain-level En-structure claim" closes the AP-CY33 propagation risk.

### Heal B: `koszulness_moduli_scheme.tex:674-677`

Pre-heal: "which is automatic for SC^ch,top by Kontsevich formality for
two-coloured little disks (with the chiral refinement of Remark
rem:sc-chtop-formality, Chapter ch:en-koszul-duality)."

`\label{rem:sc-chtop-formality}` does not exist anywhere across the
three volumes (AP264 phantom `\ref`).

Post-heal: retargeted to `prop:en-formality` (which DOES exist at
`en_koszul_duality.tex:1069`), with explicit cohomology-level scope
label and a parenthetical disclaimer that no chain-level SC^ch,top-formality
is asserted. Closes AP264 and AP-CY33 at this site.

### Heal C: CLAUDE.md Wave Kontsevich-formality, AP1361

New AP inscribed registering the cohomological-vs-chain-level scope
discipline for formality invocations, covering all 16 audit sites
surveyed in Phase 1 under a single preventative template. Three scope
labels (cohomological / chain-level with fixed Phi / algebra-level
formality lift) documented with canonical site citations. Per AP314
inscription-rate throttling, this is the single AP for this wave; the
phantom `rem:sc-chtop-formality` is subsumed under existing AP264, the
phantom bibkeys (Keller01, Keller06, keller-icm, Fresse17, FresseWillwacher20,
Idrissi22, Brown12, Furusho11, McClureSmith03, BarNatan98, DTT09) under
existing AP281.

## Phase 4: Not-healed this wave (deferred)

D1. `preface.tex:4407` + `preface_sections10_13_draft.tex:72`: add
    "(cohomology level)" scope label to "Kontsevich formality supplies
    Phi: SC^ch,top -> SC quasi-isomorphism". Deferred per AP314
    throttling; preface edits require separate dedicated pass with
    AP-preface-cohomology discipline.

D2. H02 ALT proof "Keller deformation + Kontsevich formality"
    branding: the inscribed content is Keller-only; the
    Kontsevich-formality half is not composed into a Theorem-B ALT
    anywhere in Vol I. Either (a) inscribe a composite theorem body
    routing formality -> L_inf QI -> Theorem B, or (b) retitle the ALT
    as "Keller deformation + HPL transfer (Theorem B ALT H02)" in
    `programme_overview_platonic.tex:458-459`,
    `worldview_synthesis_2026_04_17.tex:853`, `AGENTS.md:1027`, and
    CLAUDE.md Alternative Proofs Secured table. AP241 inscription
    debt; deferred.

D3. Phantom bibkeys Keller01, Keller06, keller-icm, Fresse17,
    FresseWillwacher20, Idrissi22, Brown12, Furusho11,
    McClureSmith03, BarNatan98, DTT09. All used in this audit's
    target chapters; absent from `standalone/references.bib` (which
    does carry Kon03, Kon99, Willwacher15, Tamarkin00, Tamarkin03 but
    not the others). Existing AP281 systemic bibkey-drift covers this.
    Heal is the AP281 canonical-alias table pass; not undertaken this
    wave.

## Summary

One AP inscribed (AP1361). Two concrete file heals (Heal A, Heal B).
Three deferred items recorded (D1-D3) with honest scope and inscription
debt. No Theorem H proof body altered; the `lem:chiral-quadratic-koszul`
Step 1 Fresse-transport non-degeneracy argument is intact, only the
prose scope tightened. No H02 ALT proof compromised; the Keller half
is genuinely inscribed via `thm:ainfty-koszul-characterization` and
stands independently. AP-CY33 chain-level-vs-rational discipline
preserved across Vol I.

Raeez Lorgat.
