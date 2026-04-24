# Codex 09 — Local-Global (Manin-Gaitsgory) Brutal Attack

## Verdict (one line)
PARTIALLY SOUND: local fixed-curve discipline is real, but the universal global/arithmetic packaging is overclaimed.

## Attack 1 — Theorem C κ-locally-constant
- Claim as stated: Theorem C has `κ+κ^!` locally constant on `M_{g,n}` and “LOCAL = GLOBAL” (`platonic_ideal_reconstituted_2026_04_17.md:171`; `project_vol1_platonic_ideal.md:20`).
- Scope leak: Virasoro constants include poles at `c=-22/5` (`CLAUDE.md:281`; `landscape_census.tex:425-430`), and the Lee-Yang simple quotient explicitly requires separate computation because the universal formula does not apply (`shadow_tower_higher_coefficients.tex:1510-1517`). Admissible KM is likewise a boundary/simple-quotient locus, not one constant family.
- Verdict: SCOPED.

## Attack 2 — Theorem D Chern-Weil at nodes
- Claim as stated: `obs^univ=κλ^univ` globally on `\overline M_{g,n}` by Chern-Weil (`platonic_ideal_reconstituted_2026_04_17.md:172`).
- Obstruction: the chapter proves `obs_g=κλ_g` only under uniform-weight/scalar-diagonal hypotheses (`higher_genus_foundations.tex:5580-5607`); nodal sewing is unconditional only in low genus and conditional at `g>=3` on log-FM/six-functor input (`higher_genus_foundations.tex:6497-6520`).
- Verdict: SCOPED; retract the unconditional `Mbar` sentence.

## Attack 3 — MGSL G_mot(Q)^{super} existence
- Claim as stated: `G_mot(Q)^{super}` is the Tannakian dual of `Z/2`-graded mixed motives and acts on `P^{super}` (`platonic_ideal_reconstituted_2026_04_17.md:453-459`).
- Status: Voevodsky 2000 motives and Deligne-Goncharov 2005/Brown 2012 mixed Tate structures do not supply this super Tannakian package. The repo itself marks MGSL as conjectural beyond low weight (`first_principles_cache.md:757-764`, `first_principles_cache.md:811-819`). Kontsevich-Zagier 2001 gives periods, not `P^{super}`.
- Verdict: ASPIRATIONAL unless explicitly conjectural.

## Attack 4 — p=691/3617 Kummer-Bernoulli r=11 duality
- Claim as stated: Vol I computes through `r=11` and identifies Kummer-Bernoulli arithmetic duality at `{691,3617}` (`platonic_ideal_reconstituted_2026_04_17.md:449`).
- Grep result: finite disjointness is proved by explicit factorisation (`z_g_kummer_bernoulli_platonic.tex:571-631`; `shadow_tower_higher_coefficients.tex:2420-2513`), with compute tests (`test_z_g_s_r_arithmetic_duality.py:178-218`). Chenevier 2014 determinant theory (theorem number unchecked) does not give “p-adic obstructions in the GRT torsor” (`platonic_ideal_reconstituted_2026_04_17.md:126`).
- Verdict: PROVED only as finite polynomial arithmetic; p-adic/GRT packaging is ASPIRATIONAL.

## Attack 5 — GRT_1(Q) action on r(z)
- Claim as stated: GRT torsor acts on all seven faces of `r(z)` (`platonic_ideal_reconstituted_2026_04_17.md:124`; `project_vol1_platonic_ideal.md:23`).
- Overreach: Brown 2012, Thm. 1.3 concerns motivic associators; the repo distinguishes GRT, motivic Galois, and GT and says injectivity is Deligne-Ihara, not Brown (`opus_15_seven_faces_GRT.tex:112-121`). Chain-level action needs Drinfeld/Furusho/Tamarkin/Willwacher formality, not Brown alone (`opus_15_seven_faces_GRT.tex:126-159`).
- Verdict: SCOPED.

## Attack 6 — Slab_d (∞,1)-category well-definedness
- Claim as stated: `Slab_d=(M_d)^{op}×(d-1)-Mfd^{or,fr}×Curves` and `Sh:Slab_d→ChirAlg^{E_1}` is symmetric monoidal (`platonic_ideal_reconstituted_2026_04_17.md:382-397`).
- Coherence issue: the worked repair defines only a fixed-`X` specialisation `Slab_d(X)` (`opus_06_G4_phi_functor.tex:393-424`) and separately admits the `(∞,2)` axioms remain open (`opus_06_G4_phi_functor.tex:920-923`). Mixed variance needs a Grothendieck construction, not a bare product.
- Verdict: ASPIRATIONAL/SCOPED.

## Retraction List
- `platonic_ideal_reconstituted_2026_04_17.md:171`: replace “locally constant on `M_{g,n}`” by “locally constant on fixed smooth algebraic families away from quotient/admissible jumps.”
- `platonic_ideal_reconstituted_2026_04_17.md:172`: replace global Chern-Weil on `Mbar` by “open smooth locus; boundary conditional as specified.”
- `platonic_ideal_reconstituted_2026_04_17.md:124,126,449`: remove Brown/p-adic/GRT consequence language; keep finite arithmetic theorem.

## Aspirational-Claim List
- `G_mot(Q)^{super}`, `P^{super}`, and MGSL action (`platonic_ideal_reconstituted_2026_04_17.md:453-459`): CONJECTURAL/ASPIRATIONAL.
- Seven-face universal GRT action on `r(z)` (`project_vol1_platonic_ideal.md:23`): SCOPED.
- Product definition of `Slab_d` and global `Sh` (`platonic_ideal_reconstituted_2026_04_17.md:382-427`): ASPIRATIONAL until coherence is proved.
