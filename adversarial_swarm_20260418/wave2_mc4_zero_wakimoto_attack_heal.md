# Wave 2 (2026-04-18) — MC4⁰ Wakimoto-SDR UNCONDITIONAL retraction + cross-volume propagation

**Target.** CLAUDE.md MC1-4 row claim: "MC4⁰ PROVED UNCONDITIONAL (2026-04-16) at generic parameters for class M principal: explicit SDR via Wakimoto one-step (Virasoro) / Feigin-Frenkel screening (W_N), h_htpy = (1 − ιp)/(L_0 − h − N + 1) invertible generically."

**Scope.** Extends `attack_heal_mc4_0_20260418.md` (Vol I standalone heal complete by prior wave) to (i) verify CLAUDE.md row healed, (ii) audit cross-volume propagation, (iii) heal Vol II `programme_climax_platonic.tex` reverse-drift.

---

## Attack ledger

| # | Site | Severity | Category | Finding |
|---|------|----------|----------|---------|
| A1 | grep Vol I `chapters/`, `appendices/`, `main.tex` | CRITICAL | AP269 (fabrication) | ZERO hits for `Wakimoto`/`h_htpy`/`one-step SDR`/`L_0 - h - N + 1` outside `standalone/N4_mc4_completion.tex`. The claimed chapter home `chapters/theory/bar_cobar_adjunction_curved.tex` has ZERO such hits; the standalone's pointer (line 949-952) to that chapter was a false inscription advertisement. |
| A2 | `ordered_associative_chiral_kd.tex:10176-10297` `prop:ff-screening-coproduct-obstruction` | CRITICAL | AP269 + contradicting witness | Proves $[Q_{\alpha_i}, \Delta_z^{\mathfrak{h}}]$ is a non-exact chiral 1-cocycle in $H^1_{\mathrm{ch}}$ with coefficient $(\Psi - 1)/\Psi$ matching `thm:miura-cross-universality`. The FF-screening W_N route of the MC4⁰ Wakimoto claim is refuted by the programme's own proved negative. |
| A3 | `N4_mc4_completion.tex:955-967` "proof sketch" | CRITICAL | AP269 six-gap | No $\iota$ or $p$ defined (SDR triple undefined); $N$ overloaded (tower stage / $\mathfrak{sl}_N$ rank / spin); $h$ overloaded (denominator parameter / conformal weight); resonance locus uncharacterised; MC4⁰ stage-to-stage lift absent; W_N route contradicted by A2. |
| A4 | `N4_mc4_completion.tex` inscription status (pre-heal) | HIGH | AP255 standalone-phantom-in-consumers | Standalone NOT `\input` into `main.tex`; preface `\phantomsection\label{thm:completed-bar-cobar-strong}` mask at `preface.tex:5130` provided resolution without the Wakimoto content being in any chapter. |
| A5 | CLAUDE.md MC1-4 row (pre-heal, audit time) | CRITICAL | AP271 (reverse drift) | CLAUDE.md advertised "MC4⁰ PROVED UNCONDITIONAL" while FRONTIER.md CL11 already recorded "Wakimoto SDR claim DROPPED (AP269 fabrication)" and the standalone carried `\begin{conjecture}`. HEALED before this wave by the Wave-MC4-swarm / AP421 entry. |
| A6 | Vol II `programme_climax_platonic.tex:599` | HIGH | AP271 cross-volume reverse drift | Vol II `cor:rung-w-infty-spin-two` (ClaimStatusProvedHere) proof cites "the rigidity pillar uses the Wakimoto one-step strong-deformation retract" — load-bearing on a Vol I mechanism retracted as AP269 fabrication. HEALED this wave (see Heal-2 below). |
| A7 | Vol III | — | — | No matches for `n4-mc4-zero`, `Wakimoto one-step`, `h_htpy`, `MC4⁰ UNCONDITIONAL` (clean). |

---

## Surviving core

The genuine MC4 content in Vol I is `thm:completed-bar-cobar-strong` + `prop:mc4-reduction-principle` + `cor:mc4-degreewise-stabilization` + `prop:mc4-weight-cutoff` (inscribed in `bar_cobar_adjunction_curved.tex`, `\input` into main.tex, proved via Mittag-Leffler on the strong-completion-tower regime). MC4⁺ (classes G/L/C) is an unconditional corollary via bounded-degree conformal/fermion-number filtrations. MC4⁰ at generic $c$/$\Psi$ for class M principal would be a strengthening — an explicit Wakimoto-Fock deformation-retract at generic $c$, a weight-stratified cocycle-lift, or an equivalent chain-level construction — and is not yet supplied. The W_N Feigin-Frenkel route is actively obstructed by an explicit non-exact class in $H^1_{\mathrm{ch}}$ with coefficient $(\Psi-1)/\Psi$, which is the universal Miura cross-term coefficient.

---

## Heal ledger

| # | File | Action | Status tag |
|---|------|--------|------------|
| H1 | `standalone/N4_mc4_completion.tex` | (Prior wave, re-verified) `thm:n4-mc4-zero-unconditional` → `conj:n4-mc4-zero-generic-parameters`; `thm:n4-non-principal-hook` → `conj:n4-non-principal-hook`; AP266 sharpened-obstruction proposition `prop:mc4-zero-wakimoto-sdr-obstruction` (the $(\Psi-1)/\Psi$ cocycle is the falsification test); six-gap `rem:mc4-zero-sdr-candidate-gaps`; summary table rewritten CONJECTURAL for Virasoro / $\cW_N$ / subregular / hook-type; false-inscription pointer retracted. | `\ClaimStatusConjectured` |
| H2 | Vol I CLAUDE.md MC1-4 row | (Prior wave, re-verified) rewritten "MC4⁰ CONJECTURAL (2026-04-18 Wave-MC4-swarm, AP421)" with AP269 retraction, Vol I grep evidence, FF-obstruction cross-link, honest surviving MC4 content, audit trail. | n/a |
| H3 | Vol I FRONTIER.md CL11 | (Prior wave, re-verified) "Wakimoto SDR claim DROPPED (AP269 fabrication per agent a44f; zero manuscript witness for Wakimoto one-step SDR)". | n/a |
| H4 | Vol II `programme_climax_platonic.tex:599-607` | (This wave) In `cor:rung-w-infty-spin-two` proof, replace "rigidity pillar uses the Wakimoto one-step strong-deformation retract" with the scoped dependency: "rigidity pillar uses the strong-completion-tower MC4 machinery of `V1-thm:completed-bar-cobar-strong` in the conformal-weight filtration (the candidate MC4⁰ upgrade via an explicit Wakimoto Fock-module SDR at generic $c$ is articulated as `V1-conj:n4-mc4-zero-generic-parameters` and is CONJECTURAL pending chain-level SDR inscription, per the 2026-04-18 retraction recorded at Vol I FRONTIER.md CL11; the present corollary uses only the strong-completion-tower content, which is inscribed and unconditional)." The corollary's `\ClaimStatusProvedHere` survives because the proof's rigidity pillar now rests on the inscribed strong-completion-tower MC4, not on the retracted Wakimoto SDR. | unchanged |

No commit.

---

## Commit plan (DEFERRED — no commits per mission brief)

Files touched this wave: `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/programme_climax_platonic.tex` (one edit, scope-tightening — AP271 reverse-drift heal).

Files verified already-healed (no edits needed): `/Users/raeez/chiral-bar-cobar/CLAUDE.md` (MC4⁰ row carries AP421 retraction); `/Users/raeez/chiral-bar-cobar/FRONTIER.md` (CL11 records Wakimoto drop); `/Users/raeez/chiral-bar-cobar/standalone/N4_mc4_completion.tex` (Conjecture + AP266 obstruction + honest summary table).

Clean: Vol III (no matches).

Proposed commit scope: single commit covering the Vol II rigidity-pillar scope-tightening + this wave note. Authored by Raeez Lorgat; no AI attribution.

---

## AP register recommendation

AP421 (already proposed in `attack_heal_mc4_0_20260418.md`) — "Standalone MC4⁰ inscription claiming Vol I chapter inscription without inscription" — is active in the healed CLAUDE.md row. This wave additionally surfaces a propagation pattern worth registering in a future AP cleanup:

**Candidate AP: "Programme-climax pillar load-bearing on a retracted mechanism".** When a climax-rung / master-theorem / corollary-tower in one volume cites an enumerated list of "pillars" (convergence pillar, rigidity pillar, gauge-theoretic pillar, …) and ONE pillar is load-bearing on a mechanism retracted in a sibling volume's FRONTIER.md, the climax proof inherits the retraction unless the pillar is either (a) rewritten to depend only on the inscribed surviving content, or (b) the climax `\ClaimStatusProvedHere` is downgraded. This is a cross-volume AP271 variant scoped to pillar-decomposition proofs. Heal pattern: when retracting a mechanism in volume V_i, grep all sibling volumes V_j for `pillar uses <mechanism>` / `<mechanism> pillar` / `<mechanism> rigidity` and heal each hit atomically (AP5 + AP149). Wave-2 instance: `programme_climax_platonic.tex:599`.
