# Attack + Heal: MC4^0 UNCONDITIONAL status and AP269 Wakimoto-SDR fabrication

**Date:** 2026-04-18
**Target:** Vol I CLAUDE.md MC1-4 row claiming "MC4^0 PROVED UNCONDITIONAL (2026-04-16) at generic parameters for class M principal: explicit SDR via Wakimoto one-step (Virasoro) / Feigin-Frenkel screening (W_N), homotopy h_htpy = (1 - iota p)/(L_0 - h - N + 1) invertible generically."
**Protocol:** CLAUDE.md CONSTITUTIONAL TRUST WARNING + AP269 (SDR-formula fabrication with proved-contradictory witness) + AP255 (phantom-in-consumers) + AP266 (sharpened-obstruction healing).

---

## Phase 1: Attack — intelligence gathered

### A. AP269 smoking gun empirically confirmed

Grep scope: `/Users/raeez/chiral-bar-cobar/{chapters,standalone,appendices,main.tex,*.tex}`. Queries:

- `h_htpy`, `h_{htpy}`: zero hits outside `standalone/N4_mc4_completion.tex`.
- `Wakimoto one-step`, `Wakimoto SDR`: zero hits outside `standalone/N4_mc4_completion.tex`.
- `L_0 - h - N + 1`, `resonance locus`: zero hits outside `standalone/N4_mc4_completion.tex`.
- `chapters/theory/bar_cobar_adjunction_curved.tex` search for `Wakimoto|h_htpy|SDR`: **zero hits**. Yet `N4_mc4_completion.tex:950` writes:
  > "Inscribed as the MC4^0 upgrade in Vol~I `chapters/theory/bar_cobar_adjunction_curved.tex`, referenced at `thm:completed-bar-cobar-strong` as part of the 2026-04-16 wave closure."
  The cited chapter exists but contains NO Wakimoto, NO SDR, NO `h_htpy`. The inscription advertisement is false.

### B. standalone/N4_mc4_completion.tex is not \input into main.tex

`grep -rn 'N4_mc4\|input.*N4' main.tex chapters/` returns zero hits. The standalone carries `\label{thm:n4-mc4-zero-unconditional}` and `\label{thm:n4-non-principal-hook}`; neither is referenced from main.tex or any Vol~I chapter (AP255 phantom-file-in-consumers at standalone-only severity). However, `standalone/theorem_index.tex` references the MC4 cluster, and the preface carries `\phantomsection\label{thm:completed-bar-cobar-strong}` at `preface.tex:5130` — so the AP255 mask is active for the Vol~I consumer.

### C. Vacuity of the "proof sketch" in N4_mc4_completion.tex:955-967

The 12-line proof sketch asserts:
> "The homotopy $h_{\mathrm{htpy}} = (1 - \iota p)/(L_0 - h - N + 1)$ is invertible on $\mathcal{F}^{\ge 1}$... at generic~$c$ (respectively generic~$\Psi$) the Fock-module / Feigin--Frenkel screening kernel is irreducible at every weight, so the denominator is invertible at every stage of the completion tower."

Six substantive gaps:

1. **$\iota, p$ undefined.** SDR (Strong Deformation Retract) data is a triple $(\iota \colon M \hookrightarrow B, p \colon B \twoheadrightarrow M, h \colon B \to B)$ with $\id_B - \iota p = dh + hd$, $p \iota = \id_M$, $h \iota = 0$, $p h = 0$, $h^2 = 0$. Neither $\iota$ nor $p$ is constructed; neither target $M$ nor source $B$ is named; no SDR axioms are checked.
2. **$N$ ambiguous.** The denominator $L_0 - h - N + 1$ uses $N$ which in the surrounding text denotes simultaneously (a) stage of completion tower, (b) rank of $\mathfrak{sl}_N$ in the W_N case, (c) spin of a weight stratum. The formula is under-typed.
3. **$h$ ambiguous.** Uses both $h$ (denominator parameter) and $h_{\mathrm{htpy}}$ (homotopy); proof writes "denominator $L_0 - h - N + 1$" without saying whether $h$ is conformal weight of a fixed module, highest weight of a Verma, or a running eigenvalue.
4. **Resonance locus not characterised.** Claim "generic $c$ implies irreducibility at every weight" asserts Fock-module irreducibility; this is a THEOREM (Feigin-Fuks 1983 for Virasoro; Feigin-Frenkel 1990s for W_N), not a verified input. The resonance condition for $c$ is $c = c_{p,q} = 1 - 6(p-q)^2/(pq)$ for coprime integers $p, q$, a countable set; "generic" needs explicit complement statement, and the proof does not reduce invertibility of $h_{\mathrm{htpy}}$ to Fock-irreducibility.
5. **MC4^0 reduction not supplied.** MC4^0 is the completion closure problem at degree 0; the sketch does not exhibit the stage-$N$-to-stage-$(N+1)$ MC-lift computation, does not specify which deformation retract $(\iota, p, h)$ resolves which cochain complex, does not reduce the SDR data to `prop:mc4-reduction-principle` or `cor:mc4-degreewise-stabilization` of `bar_cobar_adjunction_curved.tex:1235,1302`.
6. **Contradicting witness at the W_N step.** The Vol~I proposition `prop:ff-screening-coproduct-obstruction` (`chapters/theory/ordered_associative_chiral_kd.tex:10176-10297`, `\ClaimStatusProvedHere`) proves that Feigin-Frenkel screening $Q_{\alpha_i}$ is NOT chiral-coproduct-compatible on the Heisenberg parent: the commutator $[Q_{\alpha_i}, \Delta_z^{\mathfrak{h}}]$ represents a non-exact class $R_i(z) \in H^1_{\mathrm{ch}}(\mathfrak{h}, \mathfrak{h} \otimes \mathfrak{h}[z,z^{-1}])$ with explicit coefficient $(\Psi - 1)/\Psi$. The FF-screening kernel descent is blocked at chiral-coproduct level. The "Feigin-Frenkel SDR for W_N" step of the MC4^0 sketch has no way to lift through this obstruction without addressing it, and the sketch does not address it.

### D. The subregular and hook-type sub-claims

`standalone/N4_mc4_completion.tex:971-988` (`thm:n4-non-principal-hook`):
- No `\ClaimStatus` tag; the CLAUDE.md Non-principal W row already admits this gap ("statement inscribed... with proof sketch only and no `\ClaimStatus` tag, downgrade to `\ClaimStatusConjectured` pending full proof body").
- Proof sketch cites KRW03 + Arakawa07; these references prove VA presentation + Kazhdan filtration for general nilpotents, NOT chiral SDR (chain-level contracting homotopy on the bar complex). AP272 (unstated cross-lemma via folklore citation).

`standalone/N4_mc4_completion.tex:999-1004` (Subregular / minimal reduction to βγ SDR):
- Five sentences of prose, zero theorem environment, zero proof, zero cited lemma.
- AP269 mechanism-level fabrication at the reduction-scheme level.

### E. Topology of the CLAUDE.md claim

The MC4^0 UNCONDITIONAL claim in CLAUDE.md propagates to:
- `FRONTIER.md` (expected, since this was a closure-wave item)
- `standalone/theorem_index.tex` (expected as theorem manifest)
- `chapters/frame/preface.tex:5130` phantomsection mask (AP255)
- `chapters/theory/bar_cobar_adjunction_curved.tex:971` `\index{MC4!completion closure theorem}` — this index entry is on `thm:completed-bar-cobar-strong`, which proves the STRONG-COMPLETION-TOWER version of MC4, NOT the MC4^0 generic-parameter UNCONDITIONAL version with Wakimoto SDR. The index-title overloading is itself a source of the confusion: one theorem covers two claim strengths.

### F. What IS genuinely proved

`chapters/theory/bar_cobar_adjunction_curved.tex:968-1050` `thm:completed-bar-cobar-strong` (`\ClaimStatusProvedHere` at line 950 for the degree cutoff lemma; re-asserted at 1050 for the theorem) genuinely proves the completed bar-cobar adjunction for strong completion towers via Mittag-Leffler, including the MC4 reduction principle (`prop:mc4-reduction-principle`, line 1235), degreewise stabilisation (`cor:mc4-degreewise-stabilization`, 1302), and the weight-cutoff criterion (`prop:mc4-weight-cutoff`, 1377). This is the genuine MC4 content; the UPGRADE to "MC4^0 UNCONDITIONAL via explicit Wakimoto SDR at generic $c$ / generic $\Psi$" is the additional claim, and it is the one that is unproved.

---

## Phase 2: Surviving core

After the attack:

- **MC4 (base)** UNCONDITIONAL on strong-completion-tower regime: survives, proved by `thm:completed-bar-cobar-strong`. Inscribed in a chapter that is `\input` into main.tex.
- **MC4^+** UNCONDITIONAL for class G / class L / class C: survives, carried by the strong-filtration axiom (conformal-weight or fermion-number filtration acts with bounded degrees).
- **MC4^0 UNCONDITIONAL at generic $c$ / generic $\Psi$ for class M principal via explicit Wakimoto SDR**: falls. No inscribed Wakimoto-SDR construction; no defined $(\iota, p, h)$; no resonance-locus analysis; Vol~I contains a contradicting witness for the W_N route.
- **MC4^0 for Virasoro / principal W_N via the general `prop:mc4-weight-cutoff` + `prop:mc4-reduction-principle`**: CONDITIONAL on the weight-cutoff hypothesis holding at generic $c$, which for the conformal-weight filtration on Virasoro is equivalent to the no-resonance condition $c \ne c_{p,q}$. This partially matches the claim but via a different mechanism (weight-cutoff, not Wakimoto SDR).
- **Subregular / minimal W to class-C βγ SDR**: prose observation, no theorem.
- **Parabolic hook-type r ≤ N-3**: CONJECTURAL at theorem level (CLAUDE.md Non-principal W row already says this).

Conclusion: the surviving core is "MC4^0 CONJECTURAL at generic parameters for class M principal; the general MC4-reduction principle gives a sufficient condition (weight-cutoff + inverse-limit continuity) which is verifiable for Virasoro and principal W_N at non-resonant parameters MODULO inscription of the explicit deformation-retract or weight-stratified cocycle-lift construction."

---

## Phase 3: Heal (AP266 sharpened-obstruction pattern)

Chosen option: **(b) retract MC4^0 to CONJECTURED with the explicit AP269 obstruction inscribed** and partial Virasoro-only scope acknowledgment.

Rationale: Option (a) "inscribe the Wakimoto one-step SDR as a full lemma" is a deep-mathematics frontier item (the Fock-module irreducibility at generic $c$ is a theorem-level input; the deformation retract data requires explicit construction of left/right inverses on the Wakimoto Fock space $\mathcal{F}$; the resonance-locus stratification must match the Feigin-Fuks irreducibility boundary; the W_N case must address the `prop:ff-screening-coproduct-obstruction` contradicting witness). Not heal-able in a single swarm pass. Option (c) "MC4^0 at Virasoro only" still requires inscription of the Wakimoto SDR chain-level homotopy, which is absent; so (c) also reduces to (b) until the Virasoro inscription is supplied.

Heal actions:

1. **Downgrade `thm:n4-mc4-zero-unconditional`** (standalone/N4_mc4_completion.tex:928-953) from `[Theorem]` to `[Conjecture]` with explicit retraction note pointing to AP269 + `prop:ff-screening-coproduct-obstruction`. Rename label to `conj:n4-mc4-zero-generic-parameters`.
2. **Retract the "Inscribed in chapters/theory/bar_cobar_adjunction_curved.tex" false-inscription note** (line 949-952) and replace with honest "this conjecture articulates a strengthening of `thm:completed-bar-cobar-strong`; no inscribed Wakimoto-SDR deformation-retract construction exists at the date of writing".
3. **Inscribe an obstruction proposition** `prop:mc4-zero-wakimoto-sdr-obstruction` in the same standalone, stating the FF-screening contradicting witness and the absence of a defined $(\iota, p)$ pair, citing `prop:ff-screening-coproduct-obstruction` as a load-bearing negative result for the W_N route. This follows the AP266 sharpened-obstruction template: an explicit class in $H^1_{\mathrm{ch}}$ with coefficient $(\Psi - 1)/\Psi$ matching `thm:miura-cross-universality`.
4. **Downgrade `thm:n4-non-principal-hook`** similarly to `conj:n4-non-principal-hook` and add the missing `\ClaimStatusConjectured` tag (matches CLAUDE.md Non-principal W row's self-declared gap).
5. **Rewrite the summary table** (N4_mc4_completion.tex:1017-1036) to replace "UNCONDITIONAL MC4^0 (Wakimoto SDR)" / "UNCONDITIONAL MC4^0 (FF screening)" rows with "CONJECTURAL MC4^0 (Wakimoto-SDR inscription frontier)".
6. **Rewrite CLAUDE.md MC1-4 row** (HOT ZONE-level file) to state MC4^0 as CONJECTURAL at generic parameters for class M principal, with explicit MC4^+ / MC4^0 split and with the `prop:ff-screening-coproduct-obstruction` cross-link recorded.
7. **Inscribe AP421** (new anti-pattern) in CLAUDE.md: "Standalone-only MC4^0 inscription claiming Vol~I chapter inscription" — cross-reference AP255 (phantom file) and AP269 (SDR-formula fabrication); this is the specific variant where a standalone theorem claims inscription-home in a non-inscribing chapter and propagates through preface phantomsection.

Labels atomic: `thm:n4-mc4-zero-unconditional` -> `conj:n4-mc4-zero-generic-parameters`; `thm:n4-non-principal-hook` -> `conj:n4-non-principal-hook`. Cross-volume grep scope: Vol II + Vol III `\ref{thm:n4-mc4-zero-unconditional}` / `\ref{thm:n4-non-principal-hook}` — if hits are found, atomic rename in same session (HZ-5 / AP149).

---

## Phase 4: Inscription plan

Target file: `/Users/raeez/chiral-bar-cobar/standalone/N4_mc4_completion.tex` (~1044 lines; appendix section 916-1043).

Scope of edits:
- Lines 917-918: section title refresh to reflect conjecture status.
- Lines 921-925: intro paragraph rewrite.
- Lines 928-953: convert `theorem` env to `conjecture` env; rename label; delete false-inscription note; insert `\ClaimStatusConjectured` tag.
- Lines 955-967: rewrite "Proof sketch" as `\begin{remark}[Status of the candidate SDR construction]` with honest gap enumeration.
- Insert new `prop:mc4-zero-wakimoto-sdr-obstruction` after line 967 (AP266 sharpened-obstruction).
- Lines 971-988: convert `theorem` env to `conjecture` env; rename label; insert `\ClaimStatusConjectured`.
- Lines 990-997: rewrite "Proof sketch" as `\begin{remark}`.
- Lines 999-1015: leave prose observation, add explicit "prose-only, no theorem" disclaimer.
- Lines 1017-1036: rewrite summary table; convert UNCONDITIONAL rows for Vir_c and W_N to CONJECTURAL.
- Lines 1038-1042: retain; residual conjectural content note stays honest.

CLAUDE.md updates: MC1-4 row rewrite + AP421 inscription in the AP-block (AP421-AP440 reserved for MC4^0-swarm per mission brief).

No chapter-level `.tex` edits needed (the Vol~I chapter content genuinely proves `thm:completed-bar-cobar-strong`; the false advertisement lives only in the standalone).

## Phase 5: Propagation

Cross-volume grep plan (run after heal):
- `\ref{thm:n4-mc4-zero-unconditional}` / `\ref{thm:n4-non-principal-hook}` in `~/chiral-bar-cobar-vol2` and `~/calabi-yau-quantum-groups`.
- "MC4^0 UNCONDITIONAL" / "Wakimoto SDR" / "Wakimoto one-step" prose echoes across all three volumes.
- Update Vol II + Vol III CLAUDE.md / FRONTIER.md if any consumer exists.

---

## Conclusion

MC4^0 UNCONDITIONAL status at generic parameters for class~M principal (Wakimoto SDR / FF screening route) is, at the 2026-04-18 audit, **an AP269 fabrication + AP255 phantom-in-consumers + AP266-shaped sharpenable frontier**. The genuine surviving mathematics is `thm:completed-bar-cobar-strong` (strong-completion-tower MC4), which is inscribed and proved; the additional "UNCONDITIONAL at generic parameters via explicit Wakimoto SDR" claim is not supported by any inscribed construction, and the W_N variant is actively contradicted by `prop:ff-screening-coproduct-obstruction`. Heal: downgrade to CONJECTURE with AP266 sharpened-obstruction inscription; update CLAUDE.md; register AP421.
