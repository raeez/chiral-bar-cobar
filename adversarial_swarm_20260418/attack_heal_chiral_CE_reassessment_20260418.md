# Reassessment: Chiral CE retraction (AP1041-1044) after BD04-citations audit

Date: 2026-04-18
Author: Raeez Lorgat.
Mission: re-examine the Chiral CE agent's verdict that $B(U^{\mathrm{ch}}(L)) \simeq \mathrm{CE}_*(L)$ is RETRACTION REQUIRED, in light of a separate BD04-citations audit that found Vol I's paraphrase of Beilinson--Drinfeld 2004 Theorem 4.8.1 ACCURATE.

## Summary verdict: RETRACTION STILL REQUIRED.

Findings 1-4 of the prior attack (`attack_heal_chiral_CE_20260418.md`) stand independently of finding 5. Finding 5 was not an "overcautious" claim against Vol I; it was a positive identification of BD04 Thm 4.8.1 as the CORRECTIVE primary source. The BD04-audit's validation of Vol I's paraphrase of Thm 4.8.1 does not weaken the Chiral CE verdict; it strengthens it by establishing that Vol I correctly states the derived-global-sections identification, while Vol III's naive pointwise identification (the one under attack) is precisely what BD04 rules out.

Mission framing "error 5 was overcautious" appears to conflate two distinct roles for BD04:
- Prior Chiral CE attack §A3: BD04 Thm 4.8.1 is cited as the correct replacement statement that Vol III's inscription fails to match.
- BD04-citations audit (separate wave): Vol I paraphrase of BD04 Thm 4.8.1 is accurate.

These two findings are compatible. Both hold. The prior attack did not claim Vol I got BD04 wrong; it cited Vol I's `bar_construction.tex:440` and `chiral_koszul_pairs.tex:5809` as correct usages, and faulted Vol III for lacking the derived-global-sections scope. The reassessment preserves the Chiral CE retraction verdict in full.

## Item-by-item verification of findings 1-4

### F1. Engine tautology (AP1042)

Verified on disk at `calabi-yau-quantum-groups/compute/lib/chiral_ce_complex.py:1041-1054`:
```
def bar_poincare(self) -> Dict[int, int]:
    return self.ce.poincare_polynomial()

def ce_poincare(self) -> Dict[int, int]:
    return self.ce.poincare_polynomial()

def poincare_match(self) -> bool:
    return self.bar_poincare() == self.ce_poincare()
```
Both sides route through `self.ce.poincare_polynomial()`. The comparison is a computation-against-itself and cannot fail. AP1042 (engine-internal tautology) stands.

### F2. Classical-CE-of-generator-space vs chiral-CE-of-envelope (AP1041)

Vol III `chapters/theory/quantum_chiral_algebras.tex:285-308`, `prop:bar-ce-identification`, claims graded vector-space isomorphism $T^c(s^{-1}\bar{A}) \cong \bigwedge^\bullet(L)$ with Poincaré $(1+t)^{\dim L}$. For $A = U^{\mathrm{ch}}(L)$ an infinite-dimensional vertex algebra, the bar complex $T^c(s^{-1} \bar{A})$ has infinitely many generators; the proposed identification with the finite-dimensional exterior algebra of the generator space is false as a chain-level graded vector-space statement. The OPE simple-pole contributions (level, central charge, higher products $a_{(n)}b$ for $n \ge 1$) are absent on the RHS. AP1041 stands.

### F3. Numerical contradictions Vol I vs Vol III

Direct Read verification:

Vol I `chapters/theory/chiral_center_theorem.tex:1965-2036` (`prop:derived-center-explicit`):
- Heisenberg $\mathfrak{H}_k$: $\ChirHoch^{0,1,2} = (\bC, \bC, \bC)$, $\ChirHoch^{\ge 3} = 0$. Total 3. Generators $\{1, \xi_k, \eta\}$. Poincaré $1+t+t^2$.
- Affine $\widehat{\fsl}_2$ at non-critical $k$: $\ChirHoch^0 = \bC$, $\ChirHoch^1 = \fsl_2$, $\ChirHoch^2 = \bC$. Total 5. Poincaré $1 + 3t + t^2$.
- Virasoro $\mathrm{Vir}_c$: $\ChirHoch^0 = \bC$, $\ChirHoch^1 = 0$, $\ChirHoch^2 = \bC \cdot \Theta$. Total 2. Poincaré $1 + t^2$.

Vol III `chapters/theory/quantum_chiral_algebras.tex:302-306`:
- Heisenberg: $\HH^\bullet = \{1, 1\}$, Poincaré $(1+t)$. Total 2.
- $\widehat{\fsl}_2$: Poincaré $(1+t)^3$. Total 8.
- Yangian truncated rank 3: Poincaré $(1+t)^3 = 8$, which is an AP1041 symptom: "truncated Yangian, strict Lie" is not $U^{\mathrm{ch}}(L)$ for Vol I's Yangian.

Three distinct contradictions: Heisenberg (3 vs 2), $\widehat{\fsl}_2$ (5 vs 8), Virasoro (matching total 2 but wrong bar-degree distribution — Vol I concentrates in degrees 0,2; Vol III in degrees 0,1). F3 stands.

### F4. Loday--Vallette Theorem 10.1.6 citation drift (AP1043)

Vol III `quantum_chiral_algebras.tex:300` cites Loday--Vallette 2012 Theorem 10.1.6 for $B(U(\fg)) \simeq \mathrm{CE}_*(\fg)$. LV Theorem 10.1.6 exists and is correct, but concerns Koszul duality for quadratic operads (the operadic cobar-bar adjunction in Chapter 10, which treats Koszul-dual operads $\mathcal{P}^!$). The classical statement $B(U(\fg)) \simeq \mathrm{CE}_*(\fg)$ is a consequence of the Koszul duality between $\mathrm{Com}$ and $\mathrm{Lie}$ and lives in LV Chapter 3 (Twisting morphisms) / Chapter 13 (Lie algebras) — not Chapter 10. Cartan-Eilenberg Chapter XIII §7 is the classical source. F4 stands.

### F5. BD04 Theorem 4.8.1 — not mis-paraphrased; flagged as corrective

Re-reading the Chiral CE attack-heal §A3 carefully: the agent's framing is that BD04 Thm 4.8.1 is the CORRECT primary-source identification (chiral homology = CE of $\mathrm{R}\Gamma_{\mathrm{DR}}(C, L)$), and that Vol III's inscription FAILS to match this statement by substituting the naive pointwise exterior algebra. The agent EXPLICITLY notes Vol I's correct usage at `bar_construction.tex:440` and `chiral_koszul_pairs.tex:5809`. The BD04-citations audit's independent verification that Vol I's paraphrase is accurate does not retract F5; it CORROBORATES the claim that BD04 is correctly stated in Vol I, which is precisely the baseline against which Vol III's inscription is being measured.

F5 as written is not a claim that "Vol I paraphrase is wrong"; it is a claim that "BD04 Thm 4.8.1 is the correct substitute for Vol III's naive identification". Both conjuncts are independently verified by the two attack-heal passes. No retraction of F5 is warranted.

## AP registry status

AP1041-AP1044 were inscribed in the attack-heal note (`attack_heal_chiral_CE_20260418.md:106-140`) but have NOT landed in Vol I CLAUDE.md. Verified by Grep: zero hits for `AP1041|AP1042|AP1043|AP1044` in `/Users/raeez/chiral-bar-cobar/CLAUDE.md`.

## Heal actions (this wave)

Per AP314 (inscription-rate discipline) and the session's minimal-AP constraint (AP1801-AP1820 reserved, used SPARINGLY):

### H1. Vol I CLAUDE.md Chiral CE cross-awareness retraction

Line 1327 of Vol I CLAUDE.md carries the verbatim advertisement "Chiral CE: B(U^ch(L))=CE_*(L) PROVED" inside the "Vol III 6d hCS Session Cross-Awareness" section. This is the Vol I landing site for the AP1044 (verbatim-advertisement proliferation) heal. Downgrade inline with explicit scope caveat pointing to BD04 Thm 4.8.1 derived-global-sections formulation as the correct statement, and to Vol I `prop:derived-center-explicit` as the falsifying Vol I witness.

Applied in this wave. No new AP number consumed.

### H2. Vol III chapter healing and engine retrofit

Deferred to a subsequent Vol-III-scoped wave. The Vol III inscriptions (`prop:bar-ce-chiral`, `prop:bar-ce-identification`, `compute/lib/chiral_ce_complex.py`) should be downgraded to `\ClaimStatusConjectured` with explicit BD04 scope, per the prior attack's H1--H4. This reassessment confirms those healings are warranted; execution belongs on Vol III soil.

### H3. AP1041-1044 landing in Vol I CLAUDE.md

Deferred per AP314 (inscription-rate outpaces audit capacity). The four APs are inscribed in the attack-heal note and can be migrated into Vol I CLAUDE.md in a subsequent consolidation pass, together with other AP1000-series entries that are still in notes-only status. Landing in this wave would violate AP314 throttling.

## New anti-patterns

None inscribed this wave. The four APs from the prior attack (AP1041-1044) are confirmed and stand; no new patterns surfaced that are not already captured by the existing AP catalogue.

Observation at meta-level: the mission framing "error 5 was overcautious" is itself an instance of AP271 (reverse drift, metacognitive layer stating a more pessimistic diagnosis than the manuscript supports) applied at the reassessment-framing layer. The Chiral CE attack was not overcautious on F5; the mission brief was overcautious about the attack. This is worth noting but does not warrant a new AP inscription.

## Falsification test

If the Vol III inscription is correct as stated and Vol I is wrong, then the numerical values in Vol I `prop:derived-center-explicit` would need to be retracted. The Vol I values are supported by three independent computations: (a) Heisenberg $\{1, \xi_k, \eta\}$ triple from the Koszul-dual pair $\mathfrak{H}_k, \mathrm{Sym}^{\mathrm{ch}}(V^*)$; (b) affine $\widehat{\fsl}_2$ total 5 via chiral Orlik-Solomon form factor (AP128 heal); (c) Virasoro total 2 with $\Theta \in \ChirHoch^2$ as the central-charge deformation cocycle. The Vol III values are supported by a single tautological engine (AP1042). The falsification goes one way.

## Signatures

Author: Raeez Lorgat, 2026-04-18.
No AI attribution.
AP block usage: zero new APs inscribed this wave (AP314 discipline). AP1041-1044 (prior) confirmed.
