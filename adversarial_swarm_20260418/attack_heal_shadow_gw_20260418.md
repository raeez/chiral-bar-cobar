# Attack-and-Heal: Shadow = GW(C^3) Identification (AP280 Three-Step Deflation)

**Date:** 2026-04-18
**Target:** Vol I "Shadow = GW(C^3) IDENTIFIED" status row + its four-site inscription chain.
**AP blocks:** AP761--AP780 (reserved for this swarm).
**Author:** Raeez Lorgat.
**Scope:** DELIBERATE DOWNGRADE per AP280 healing protocol. The mathematical inputs (MNOP 2006; Bryan-Pandharipande 2001--2008) are classical and correct; the programme-internal novelty is RHETORICALLY INFLATED three steps from Remark to ProvedHere theorem to CLAUDE.md "IDENTIFIED". This heal contracts the headline and retags the loadbearing inscriptions to honest status.

Prior audit: `adversarial_swarm_20260417/wave6_shadow_gw_z_g_attack_heal.md` Phase-1 item A7 already flagged the scope (non-compact $\bC^3$, equivariant $\chi^T(\bC^3)$ framing required). Wave-6 closed without a status-tag downgrade; this Wave-18 audit completes the AP280 deflation.

---

## Phase 1. Site-by-site attack

### S1. `rem:shadow-gw-c3` (Vol I `chapters/theory/ordered_associative_chiral_kd.tex:10004-10015`)

Environment: `\begin{remark}` with label `rem:shadow-gw-c3`. Body:

> At $\kappa = \Psi$ (the level of $\cW_{1+\infty}$), the shadow tower $\{F_g\}$ produces the perturbative constant-map Gromov--Witten free energies $F_g^{\mathrm{GW,const}}(\bC^3)$. The MacMahon function $M(q) = \prod_{n \geq 1}(1 - q^n)^{-n}$ lives on the Donaldson--Thomas side; the bridge is the MNOP/DT-GW correspondence under $q = -e^{i g_s}$. For $\bC^3$ (no compact curves), the shadow tower IS the full GW partition function.

**Verdict.** Appropriate environment (Remark, not Theorem). Carries no ClaimStatus tag, which is correct for remarks. Two substantive issues:
(a) "IS the full GW partition function" elides the equivariance subtlety (non-compact $\bC^3$; the constant-map formula $F_g^{\mathrm{GW,const}}(X) = (\chi(X)/2) \int_{\overline{\cM}_g} \lambda_{g-1}^3$ of Faber-Pandharipande requires compact $X$; for $\bC^3$ one must use equivariant Euler characteristic $\chi^T(\bC^3)$ in the MNOP localisation setup).
(b) Classical attribution (MNOP 2006, Bryan-Pandharipande 2001, Faber-Pandharipande 2000) is citation-level via "MNOP/DT-GW correspondence" but there is no explicit bibkey in the remark.

**Verdict-level:** no downgrade needed (already a Remark); minor equivariant-framing patch.

### S2. `prop:v3-qg-shadow-gw` (Vol I `standalone/cy_quantum_groups_6d_hcs.tex:823-832`)

Environment: `\begin{proposition}[Shadow = GW for $\bC^3$]` with label `prop:v3-qg-shadow-gw`. NO `\ClaimStatus*` tag. Body (the full statement, with no separate `\begin{proof}` block):

> The shadow coefficients $S_r$ of the Virasoro algebra at the GW specialization $\kappa_{\mathrm{ch}} = \Psi$ are the $\Ainf$ coproduct correction coefficients $\delta^{(r)}$: the shadow tower encodes the coproduct corrections of the chiral quantum group. On the DT side, the MacMahon function $M(q) = \prod_{n \geq 1}(1 - q^n)^{-n}$ encodes the partition function via the MNOP correspondence.

**Verdict.** Proposition environment with no status tag is the constitutional violation. The statement asserts (i) shadow coefficients $=$ $A_\infty$ coproduct corrections (provable, cross-reference to Vol I shadow-Feynman bridge) AND (ii) MacMahon encodes the DT partition via MNOP correspondence (classical, Maulik-Nekrasov-Okounkov-Pandharipande 2006 Theorems 1 and 2). Clause (ii) is `\ClaimStatusProvedElsewhere` by construction; clause (i) is a back-reference to a Vol I result. Neither warrants bare-`\begin{proposition}` with implicit ProvedHere default.

**Heal.** Tag `\ClaimStatusProvedElsewhere`; add `\begin{remark}[Attribution]` citing MNOP 2006 and the Vol I shadow-Feynman bridge for clause (i); explicitly qualify clause (ii) as the MNOP DT=GW correspondence specialised to toric $\bC^3$.

### S3. `thm:bar-macmahon` (Vol I `chapters/theory/higher_genus_modular_koszul.tex:27529-27547`)

Environment: `\begin{theorem}[Bar--MacMahon correspondence; \ClaimStatusProvedHere]`. Statement: $Z^{(2)}_B(\cH; q) := \prod_{n \geq 1}(1-q^n)^{-n} = M(q)$. Proof body (verbatim):

> $B(\cH) = \operatorname{Sym}^c(s^{-1}\bar{V})$. Rank-$1$ bar character: $\prod(1-q^n)^{-1}$. Second quantization raises the exponent to~$n$ via $\operatorname{Hilb}^n(\bC^3)$, giving MacMahon.

**Verdict.** AP280 three-step-inflation SMOKING GUN. The first two sentences are bookkeeping (symmetric algebra on the desuspended augmentation ideal at rank 1 gives the Euler formula for ordinary partitions; any graduate-level combinatorics textbook). The load-bearing third sentence *is* the MNOP-2006 theorem (DT of $\bC^3$ = MacMahon) silently rewritten as "second quantization raises the exponent to $n$ via $\operatorname{Hilb}^n(\bC^3)$". Specifically, "second quantization via $\operatorname{Hilb}^n(\bC^3)$ gives the $n$-exponent" is Nakajima's Hilbert-scheme generating-function identity (Nakajima 1999, `arXiv:math/9901061`; also Cheah 1996), promoted to the full plane-partition MacMahon count for $\bC^3$ by the MNOP 2006 DT=GW correspondence (`arXiv:math/0312059` Theorem 1 and `arXiv:math/0406092`).

None of this is a self-contained proof. The theorem is ProvedElsewhere.

**Heal.** Retag `\ClaimStatusProvedElsewhere`. Rewrite proof body as a 2-line Attribution remark, not a proof block. The Attribution remark cites MNOP 2006 and Nakajima 1999 explicitly.

### S4. `prop:conifold-dt-gv` (Vol I `chapters/theory/higher_genus_modular_koszul.tex:27556-27567`)

Environment: `\begin{proposition}[Conifold DT and GV; \ClaimStatusProvedHere]`. Statement: $Z_{\mathrm{DT}} = M(-q)^2 \prod_{k \geq 1}(1-(-q)^k Q)^k$; $n_0^d = 1$, $n_{g\geq 1}^d = 0$; $N_d = (-1)^{d-1}d$. Proof body (verbatim, COMPLETE):

> Bryan--Pandharipande, MNOP.

**Verdict.** The proof is literally two author citations. This is the canonical AP280 violation at its purest. The resolved conifold DT partition function is Bryan-Pandharipande 2001 (`arXiv:math/0111113`, also their 2005 paper `arXiv:math/0502043`) combined with MNOP 2006 DT=GW; the all-genus Gopakumar-Vafa integrality and $N_d = (-1)^{d-1} d$ are classical (Gopakumar-Vafa 1998, recast Bryan-Pandharipande 2001).

**Heal.** Retag `\ClaimStatusProvedElsewhere`; rewrite as an Attribution remark citing Bryan-Pandharipande 2001 and MNOP 2006 explicitly.

### S5. CLAUDE.md status row (line 605)

> `| Shadow = GW(C^3) | IDENTIFIED | Shadow tower at kappa=Psi produces perturbative constant-map GW free energies F_g^{GW,const}(C^3). MacMahon M(q) on DT side via MNOP. |`

**Verdict.** The headline label "IDENTIFIED" inherits the inflation of S2+S3+S4. Downstream propagation: `relaunch_20260413_111534/R18_cobar_construction.md:199` and `resume_20260413_165929/C07_e3_chiral_ban.md:1434` both carry variants of the headline; `survey_modular_koszul_duality_v2.tex:8194` carries the "shadow IS the full GW answer for C^3" prose.

**Heal.** Rewrite row headline to match AP280 deflation template: "STRUCTURAL IDENTIFICATION CONJECTURAL" with explicit attribution to MNOP + Bryan-Pandharipande, and an explicit flag for the programme-internal contribution (shadow-tower $\kappa = \Psi$ coordinate realisation of the DT side, plus the Vol I shadow-Feynman bridge linking shadow coefficients to $A_\infty$ coproduct corrections).

---

## Phase 2. Heal (patch-file level)

See companion patch `patches/patch_shadow_gw_20260418.patch`.

### H1. `prop:v3-qg-shadow-gw` (S2): insert ClaimStatusProvedElsewhere + Attribution remark.

### H2. `thm:bar-macmahon` (S3): retag to ClaimStatusProvedElsewhere; replace proof body with Attribution remark citing MNOP 2006 and Nakajima 1999. Keep theorem STATEMENT (the Euler-product identity is a textbook identity and the Bar --- MacMahon numerical match is real).

### H3. `prop:conifold-dt-gv` (S4): retag ClaimStatusProvedElsewhere; replace literal-name proof body with Attribution remark citing Bryan-Pandharipande 2001 and MNOP 2006.

### H4. `rem:shadow-gw-c3` (S1): append equivariant qualifier ("via the torus-equivariant MNOP localisation at the origin of $\bC^3$") for mathematical honesty.

### H5. CLAUDE.md status row (S5): rewrite per AP280 deflation template.

The programme-internal contribution (shadow-tower $\kappa = \Psi$ coordinate realisation of the DT side; $A_\infty$ coproduct-correction interpretation of $S_r$) survives the heal intact; what retracts is the rhetorical framing promoting "IDENTIFIED" headline-level to theorem-level ProvedHere.

---

## Phase 3. Retention

After the heal:
- The Euler-product identity $\prod (1-q^n)^{-n} = M(q)$ remains a stated theorem (valid; textbook).
- The Vol I contribution remains: $\kappa = \Psi$ coordinate on the shadow tower realises the DT side of the MNOP correspondence, and the shadow-Feynman bridge identifies $S_r$ with $A_\infty$ coproduct corrections $\delta^{(r)}$. This is genuine programme content, independent of MNOP.
- What is DROPPED: the RHETORICAL claim that Vol I "proves" DT = MacMahon on $\bC^3$. That is MNOP 2006 (+ Nakajima 1999 for the Hilbert-scheme exponent), properly cited.
- Headline "IDENTIFIED" becomes "STRUCTURAL IDENTIFICATION CONJECTURAL (bridge to MNOP/BP cited, not independently derived); programme-internal contribution: shadow-tower $\kappa = \Psi$ coordinate + $S_r = \delta^{(r)}$ identification".

The prior Wave-6 audit's A7 scope-flag is also absorbed: after the heal, $\chi(\bC^3)$ is explicitly equivariant $\chi^T(\bC^3)$ on the MNOP side.

---

## Phase 4. Propagation ledger (AP5 + AP149)

Atomic propagation targets (same commit):

1. Vol I `chapters/theory/higher_genus_modular_koszul.tex:27529-27567` (H2, H3).
2. Vol I `standalone/cy_quantum_groups_6d_hcs.tex:823-832` (H1).
3. Vol I `chapters/theory/ordered_associative_chiral_kd.tex:10004-10015` (H4).
4. Vol I `CLAUDE.md:605` (H5).
5. Vol I `standalone/theorem_index.tex` (check for `thm:bar-macmahon` status tag).
6. Vol I `metadata/theorem_registry.md`, `metadata/claims.jsonl` (regenerate via `python3 scripts/generate_metadata.py` at session end).
7. Vol I `relaunch_20260413_111534/R18_cobar_construction.md:199` (session-note; historical; no heal needed if dated).
8. Vol I `resume_20260413_165929/C07_e3_chiral_ban.md:1434` (session-note; historical; no heal needed if dated).
9. Vol I `survey_modular_koszul_duality_v2.tex:8194` (prose "shadow IS the full GW answer for C^3" - append equivariant qualifier consistent with H4).
10. Vol III: grep of `/Users/raeez/calabi-yau-quantum-groups` for `shadow-gw`, `v3-qg-shadow-gw`, `bar-macmahon` returned ZERO matching standalone-prefixed labels; the Vol III programme owns distinct content ($\kappa_{BKM}$ universal, CY-to-chiral $\Phi$, CY-D stratification). No Vol III edit required by this heal.

Per AP149, all edits in the same commit. Per AP288, the Wave-6 `wave6_shadow_gw_z_g_attack_heal.md` A7 item gets a dated `RETRACTED/UPGRADED 2026-04-18` annotation referencing this Wave-18 heal which COMPLETES A7 by executing the equivariant qualifier and the tag downgrade.

---

## Phase 5. Patch

Emitted at `adversarial_swarm_20260418/patches/patch_shadow_gw_20260418.patch`. Applies cleanly to `/Users/raeez/chiral-bar-cobar` via `git apply`.

---

## Verdict

AP280 three-step inflation CONFIRMED. Heal applied: all four inscription sites (S1-S4) rescoped; headline (S5) rewritten per deflation template. Programme-internal contribution retained; classical MNOP / Bryan-Pandharipande content cited honestly. Prior Wave-6 scope-flag (A7) completed.
