# Attack+Heal: Vol II BV package chain-level qi (thm:bv-bar-coderived)

Date: 2026-04-18
Target: Vol II `chapters/connections/bv_brst.tex:2082-2171` (`thm:bv-bar-coderived`) and `:2335-2461` (`prop:bv-bar-class-m-weight-completed` + attribution remark + residual obstruction remark).
Scope: cross-volume audit from Vol I; CLAUDE.md "CONSTITUTIONAL TRUST WARNING" posture. No commits, no edits; read-only verdict + heal plan.
Author: Raeez Lorgat.

## (i) Is thm:bv-bar-coderived inscribed with a proof body?

YES. `thm:bv-bar-coderived` at `bv_brst.tex:2082-2122` is ClaimStatusProvedHere, with full proof body at :2124-2171. The theorem has four clauses:
(i) universal coderived equivalence `C^•_BV(A,Σ_g) ≃_{D^co} B^{(g)}(A)` at every genus g≥0;
(ii) class G / class L: weak equivalence of filtered curved models;
(iii) class C under harmonic decoupling: weak equivalence of filtered curved models;
(iv) class M: δ_r^harm = c_r(A)·m_0^{⌊r/2⌋−1}, cone coacyclic.

Proof structure:
- Genus 0: reduces to `thm:bv-bar-geometric` (chain-level qi, cited).
- g ≥ 1: Hodge decomposition P_BV = dlog E + [d_fib, h] + P_harm; commutator term is chain homotopy; residual discrepancy is the harmonic part δ^harm = Σ_{r≥4} δ_r^harm.
- Class-by-class: class G/L kills every δ_r^harm outright (Jacobi identity + shadow depth bound for L; no interaction vertices for G). On the PBW-associated graded the map is the genus-0 comparison on each weight piece, hence a quasi-isomorphism.
- Class C: same argument under harmonic decoupling hypothesis.
- Class M: K_g = cone(f_g) has every filtration quotient annihilated by a power of the central curvature m_0; at m_0 = 0 all δ_r^harm vanish; at m_0 ≠ 0 each m_0-power-torsion quotient is resolved by the one-variable m_0-Koszul complex whose totalization is exact, so K_g is coacyclic (thick + extension-closed), and f_g becomes an isomorphism in D^co.

Verdict on inscription: adequate. Steps are elementary from the curvature-divisibility structural input (`prop:chain-level-three-obstructions` at :1860 fwd with its own proof body). The coderived/coacyclic definitions (`def:coacyclic-fact`, `def:coderived-fact` at :1997-2022) are chiral transports of Positselski 2011, labelled ClaimStatusProvedElsewhere with attribution remark.

## (ii) On-the-nose harmonic vanishing for Heisenberg class G

Vol II inscribes this via `prop:chain-level-three-obstructions` Obstruction (3) at `bv_brst.tex:1827-1857` (in-line) + proof at :1898-1917: "For class~G, there are no interaction vertices, so every $c_r(\cA)$ vanishes." This is the Wick-theorem-style vanishing: Heisenberg OPE J(z)J(w) ~ k/(z-w)^2 is a central simple pole; the chiral A_∞ operations m_k on the bar complex of H_k are determined by the quadratic OPE only; higher-arity m_k≥3 vanishes identically because there are no cubic or higher OPE poles to feed them. Consequently every harmonic-propagator correction c_r(A)·m_0^{⌊r/2⌋−1} has c_r(H_k) = 0 as an input to the δ_r^harm formula — not at the m_0-divisibility stage but at the structural coefficient stage.

CLAUDE.md status description ("Heisenberg: chain-level qi via on-the-nose harmonic vanishing") is accurate for class G. The proof is at Vol II `bv_brst.tex:2140-2146`: "If A lies in class G or L, all harmonic discrepancies vanish. Hence f_g intertwines the curved differentials on the nose." No gap.

Scope caveat: this is a fiberwise chain-level qi on each Σ_g, at arbitrary g. The filtered-curved-models weak-equivalence is clause (ii); this is NOT "no curvature" but "curvature is carried but contributes no harmonic discrepancy". κ(H_k) = k, so m_0 = k·ω_g is nonzero for g ≥ 1 at k ≠ 0; the chain-level qi operates on curved complexes, not on uncurved ones.

## (iii) PBW-associated graded reduction to genus-0 for class L (affine KM non-critical)

Vol II inscription at `bv_brst.tex:2141-2146`: "On the PBW-associated graded, the map is the genus-0 comparison on each weight piece, hence a quasi-isomorphism. By Definition ref{def:curved-weak-equiv}, f_g is a weak equivalence of filtered curved models." The structural vanishing for class L is Jacobi: at cubic level f^{abc}·I_harm·f^{cde} (Proof of `prop:chain-level-three-obstructions`, :1902-1909), Jacobi + antisymmetry forces coefficient zero; shadow depth r_max = 3 excludes quartic and higher. Hence δ_r^harm ≡ 0 for every r ≥ 4.

Is this CHAIN-LEVEL or COHOMOLOGICAL? Reading the proof body: the claim is a chain-level intertwining "on the nose" of the two curved differentials after the harmonic discrepancy vanishes, followed by a PBW-graded reduction to genus-0 where the genus-0 theorem is chain-level. The PBW-associated graded is gr_L(V_k(g)) = Sym(g((z))) as a commutative PVA; the weight-by-weight comparison on each Sym^n piece is the abelian genus-0 chain-level qi (class G behavior). The filtered-curved-weak-equivalence upgrades this to a filtered strict qi on V_k(g) itself.

Scope caveat: PBW filtration here is the canonical Kashiwara filtration on the vacuum module (generator conformal weight), which is finite-dim at each stage and compatible with the curved bar structure. The Sugawara shift dim(g)/2 in κ(V_k(g)) = dim(g)(k+h^∨)/(2h^∨) is the structural correction the proof handles without making it explicit; what the proof uses is only m_0 = κ · ω_g as a symbol, not its numerical value.

Wave-2 2026-04-17 `thm:kac-moody-obs` remark at Vol I `higher_genus_foundations.tex:5072` flags that the scalar-diagonal hypothesis is tacitly used in Step 2-3 of the class-L obs theorem at g ≥ 2. That's a separate concern (Theorem D, not `thm:bv-bar-coderived`): scalar-diagonality enters the Theorem D obs_g = κ·λ_g chain, not the BV/bar chain-level qi. The BV/bar proof only uses that `c_r(V_k(g)) = 0 for r ≥ 4` at the coefficient level, which is a statement about OPE (Jacobi + shadow depth 3), not about scalar-diagonality.

Verdict: class L chain-level qi is correctly inscribed, with the correct mechanism (Jacobi kills the cubic, shadow depth bounds the quartic and higher). No gap at the BV/bar level. CLAUDE.md status row ("affine KM non-critical: chain-level qi via PBW-associated graded reduction to genus-0 weight-by-weight comparison") is accurate.

## (iv) Coacyclic characterization for class C and class M: is the conditionality correctly scoped?

Class C (βγ): Vol II inscription at :2111-2112 + proof at :2146-2147 states "if A lies in class C and harmonic decoupling holds, then f_g is a weak equivalence of filtered curved models." The harmonic-decoupling hypothesis is:
- Inscribed at `rem:bv-bar-class-c-proof` (:1920-1995): three-mechanism argument for genus 1 only.
- All-genera: explicitly flagged as OPEN in the residual-frontier remark at :2191-2193 and reiterated at :2332.

CLAUDE.md CONDITIONAL scope for class C is correct: "class C conditional on harmonic decoupling" matches Vol II's honest inscription. The genus-1 three-mechanism proof is local; all-genera is the sole residual frontier of the comparison package per Vol II's own closing line at :2331-2332.

Class M (Vir, W_N): Vol II inscription :2113-2121 + proof :2149-2170 states coderived-level equivalence unconditionally (coacyclic cone via curvature-divisibility). CLAUDE.md "M: coderived unconditional; direct-sum chain-level genuinely false" is correct. The strict chain-level failure on direct-sum models is not a gap in `thm:bv-bar-coderived`; it is the CORRECT shape of the theorem (direct-sum class M is an ambient artefact, pro / J-adic / weight-completed ambients give chain-level qi via Vol I MC5 Wave 12b heal + `prop:bv-bar-class-m-weight-completed`).

Residual frontier (correctly scoped per Vol II):
- All-genera class C harmonic-decoupling verification.
- Stronger vanishing of c_r(A) in class M (the coefficients, beyond the curvature-divisibility factor).

Both are honestly flagged as open; neither breaks `thm:bv-bar-coderived` at its stated scope.

## (v) AP297 finding: h_N = Σ_{j=1}^{⌊N/2⌋} h·m_0^{j−1} formula audit

**CONFIRMED FABRICATION-BY-MISATTRIBUTION.**

Vol I `mc5_class_m_chain_level_platonic.tex:269-277`, Step 1 of `thm:mc5-class-m-chain-level-pro-ambient`, cites the explicit contracting-homotopy formula

  h_N = Σ_{j=1}^{⌊N/2⌋}  h · m_0^{j−1}

as "constructed in the proof of Proposition~\textup{\ref{prop:bv-bar-class-m-weight-completed}}", i.e., Vol II `bv_brst.tex:2335-2378`.

Grep audit: zero occurrences of any of the forms {`h_N = `, `\lfloor N/2 \rfloor`, `\sum_{j=1}^{\lfloor`, `m_0^{j-1}`} inside `bv_brst.tex` (full 2764-line file). Vol II `prop:bv-bar-class-m-weight-completed` proof body ACTUALLY inscribes:

- A Milnor / weight-filtered Mittag-Leffler argument at the FINITE-STAGE level (`rem:bv-bar-class-m-weight-completed-attribution` at :2361-2378): "Proposition~\ref{prop:standard-strong-filtration} and Theorem~\ref{V1-thm:completed-bar-cobar-strong} supply the weight-completed bar side; the coderived comparison plus the weight-filtered Milnor/Mittag-Leffler argument promote the strict quasi-isomorphism from each finite stage to the inverse limit."
- An explicit frontier remark at `rem:bv-bar-class-m-frontier` (:2380-2461), stating at :2399-2404: "In the operadic language of Remark ref{rem:bv-bar-coderived-operadic}, the transferred class M A∞-operations do not truncate. A strict comparison on the raw direct-sum models would have to absorb infinitely many nonvanishing higher corrections by a single ordinary chain-homotopy package. **This is what fails.** The coderived theorem survives because every defect is still divisible by the central curvature."

The contradiction is subtle. Vol I Step 1 cites an explicit finite-stage chain-homotopy assembly; Vol II's proof body uses Milnor/ML at the inverse-limit level, with the inverse-limit ambient being pro-object or weight-completed (both bounded ambients). Vol II frontier remark :2399-2404 explicitly states that a single ordinary chain-homotopy package ABSORBING infinitely many corrections **fails on raw direct-sum models**. At finite N the formula Vol I writes would work as a plausible finite sum of Hodge-homotopy composites; but (a) Vol II does not inscribe this formula, (b) the Vol II proof body uses a different route (Mittag-Leffler on finite-dim stages per `prop:standard-strong-filtration`, not explicit h_N), (c) Vol II `topologization_class_m_original_complex_platonic.tex:419-427` explicitly retracts a related formula `h_N = (d_0)^{-1}` as "does NOT assemble into a bounded operator on the original complex via geometric-series summation" — so there is an adjacent inscribed negative result at the chain-homotopy assembly level.

**AP1201 (proposed, reserved) — Finite-stage homotopy formula cited to a Vol II proof body that uses Mittag-Leffler route.** Stronger instance of AP297 (cross-volume homotopy formula cited to a proof body that does not inscribe it) specialized to the BV/bar weight-completion case: the cited formula is plausible at finite stage; the citation is nevertheless incorrect because Vol II's proof route is Milnor/ML on finite-dim stages, not explicit chain-homotopy assembly. A nearby Vol II file (`topologization_class_m_original_complex_platonic.tex:419-427`) explicitly retracts a related h_N formula as structurally obstructed on the original complex, which a reader tracing the Vol I citation will misread as corroborating the Vol I formula. Counter: every Vol I citation of an explicit homotopy formula with a cross-volume "constructed in the proof of prop:X" attribution must grep-verify the formula's verbatim form in prop:X's proof body; miss = downgrade citation to `\ClaimStatusProvedElsewhere` with attribution pointing to the actual ML route, or inscribe the formula locally in Vol I as a new lemma with its own proof.

## Heal verdicts

### Heal H1 (Vol I, MC5 Step 1 citation rewrite)

Vol I `mc5_class_m_chain_level_platonic.tex:269-283` Step 1 currently cites a non-existent Vol II formula. The Vol I argument AT FINITE STAGE is plausible (finite-dim stage by `prop:standard-strong-filtration`(ii); finite sum of Hodge-homotopy composites; identity id − d·h_N − h_N·d is the harmonic projector). The heal is a citation rewrite, not a mathematical retraction:

Option H1a (SMALLEST): Replace the phrase "constructed in the proof of Proposition~\ref{prop:bv-bar-class-m-weight-completed}" with "by finite assembly of the Hodge-homotopy h and finitely many curvature insertions on the finite-dimensional stage-N complex (finite sum since r ≤ N bounds the number of nonzero summands)" — inscribing the formula as a Vol I construction with no cross-volume attribution, since at finite stage the assembly is elementary and does not need a Vol II import.

Option H1b (LOCAL LEMMA): Inscribe `lem:mc5-finite-stage-contracting-homotopy` in Vol I, proving that on finite-dim $\cA_{\leq N}$ the sum $h_N = \sum_{j=1}^{\lfloor N/2 \rfloor} h \cdot m_0^{j-1}$ is a well-defined bounded linear map, and the identity $\mathrm{id} - d h_N - h_N d = \Pi_{\mathrm{harm}}$ holds. This converts the citation into an inscription.

Option H1c (STRUCTURAL ALIGNMENT): Drop the explicit h_N formula from Vol I Step 1; rewrite via Vol II's actual mechanism — each finite stage is a finite-dim complex with the class M curvature-divisibility (coderived coacyclic) from `thm:bv-bar-coderived`, plus finite-dim ML at each cohomological degree. This aligns Vol I Step 1 with Vol II's proof route and removes the contested formula.

RECOMMENDATION: Option H1c is cleanest. Vol I Step 1 currently mixes two routes: the h_N explicit formula (not in Vol II) and the identity `id − d·h_N − h_N·d = Π_harm` (which in class M is exactly the coderived coacyclic statement, not a chain-homotopy statement). Rewriting via coderived coacyclic + finite-dim ML matches the Vol II proof body and avoids the AP297-like fabrication.

### Heal H2 (CLAUDE.md status row)

Vol I CLAUDE.md Theorem B row currently reads: "Chain-level class G (Heisenberg: chain-level qi via on-the-nose harmonic vanishing; direct evaluation of thm:bv-bar-coderived at Vol II bv_brst.tex:2088-2094) and class L (affine KM non-critical: chain-level qi via PBW-associated graded reduction to genus-0 weight-by-weight comparison; same mechanism as class G): `\ClaimStatusProvedElsewhere` — attributed to Vol II thm:bv-bar-coderived (`chapters/connections/bv_brst.tex:2031`); NOT inscribed in Vol I."

This row is accurate. Class G unconditional chain-level qi is correctly inscribed at Vol II :2140-2146; class L unconditional chain-level qi via Jacobi + shadow-depth bound is correctly inscribed at Vol II :1898-1909 + 2140-2146. The "2031" line reference is stale (the actual label is at :2084); recommend update to :2084 or :2082-2122 (statement + proof).

### Heal H3 (Vol II bv_brst.tex — no heals needed)

`thm:bv-bar-coderived` is correctly inscribed with honest scope per class. The residual frontier (all-genera class C harmonic decoupling) is correctly flagged. No local heal required in Vol II.

### Heal H4 (Vol II prop:bv-bar-class-m-weight-completed — no heals needed)

`prop:bv-bar-class-m-weight-completed` is correctly tagged `\ClaimStatusProvedElsewhere` with attribution to the MC5 weight-completed theorem and the Milnor/ML promotion. The attribution remark at `rem:bv-bar-class-m-weight-completed-attribution` and the residual-obstruction remark at `rem:bv-bar-class-m-frontier` honestly characterise the route and its open frontier (raw direct-sum class M chain-level is genuinely false). No local heal required.

## Downstream cascade risk

CLAUDE.md cites `thm:bv-bar-coderived` as the BV package input for:
(a) UCH-gravity chain-level (`thm:uch-gravity-chain-level`, Vol II `universal_celestial_holography.tex`);
(b) Periodic CDG admissible KL (Vol I `periodic_cdg_admissible.tex`);
(c) MC5 class M chain-level pro-ambient (Vol I `mc5_class_m_chain_level_platonic.tex`).

Downstream audit:
(a) UCH-gravity: Vol II chain-level class M at g≥1 uses half-BRST chain-level splitting + MC5 pattern, NOT a direct chain-level of `thm:bv-bar-coderived` — it uses the weight-completed pattern (correct per CLAUDE.md note "promoted from conjecture 2026-04-16 via half-BRST chain-level splitting"). No cascade risk.
(b) Periodic CDG: the admissible KL theorem uses periodic-CDG filtration + Arakawa C_2-cofiniteness + Adams-type SS, not `thm:bv-bar-coderived` directly. No cascade risk.
(c) MC5 class M pro-ambient: AFFECTED, via the H1 citation gap. The heal is local (citation rewrite to route through coderived coacyclic + finite-dim ML, Option H1c above); the theorem itself survives because Vol II's actual proof route is Milnor/ML + coderived coacyclic, which Vol I Step 1 already uses in Route (a) of Step 3. The h_N fabrication is a mis-citation in Step 1, not a structural gap in the theorem.

**No catastrophic cascade.** The three downstream consumers remain PROVED at their stated scopes under Option H1c rewrite; the class G / L / C(harmonic-decoupling) / M(coderived + weight-completed) characterisation at the Vol II level is fully inscribed and honest.

## Summary verdict

| Clause | Status | Notes |
|--------|--------|-------|
| thm:bv-bar-coderived inscription | PROVED | `\ClaimStatusProvedHere`, full proof body :2124-2171 |
| (ii) Class G harmonic vanishing | PROVED | No interaction vertices; c_r(H_k) = 0 universally |
| (iii) Class L PBW reduction | PROVED | Jacobi + shadow depth 3 ⟹ δ_r^harm = 0 for r ≥ 4; chain-level weak equivalence of filtered curved models; on PBW-associated graded reduces to genus-0 abelian comparison |
| (iv) Class C conditional | PROVED CONDITIONAL | Harmonic decoupling g=1 only; all-genera OPEN (residual frontier, correctly scoped) |
| (iv) Class M coderived | PROVED | Curvature-divisibility + coacyclic; direct-sum chain-level genuinely false is CORRECT scope, not a gap |
| prop:bv-bar-class-m-weight-completed inscription | PROVED ELSEWHERE | Via MC5 weight-completed + Milnor/ML; attribution remark honest |
| AP297 — Vol I h_N formula citation to Vol II | CONFIRMED FABRICATION-BY-MISATTRIBUTION | Heal via H1c (route Vol I Step 1 through coderived coacyclic + finite-dim ML, dropping the non-existent h_N explicit formula citation) |
| Downstream cascade (UCH, periodic CDG, MC5) | NO CATASTROPHIC RISK | Only MC5 class M pro-ambient needs local citation rewrite under H1 |

AP1201 reserved (not inscribed into CLAUDE.md in this audit; inscription should accompany the H1c heal commit to CLAUDE.md at a later session with paired Vol I rewrite).

End of audit.
