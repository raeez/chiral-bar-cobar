# G03_averaging_sugawara_xvol (558s)

**Status**

Vol I is `FIXED`. Vol II and Vol III are `BLOCKED` by sandbox write scope.

I patched the writable search surface so the generic `av(r(z)) = \kappa` claim no longer outclaims the non-abelian affine KM case. The affected in-repo files are [e1_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/e1_modular_koszul.tex), [introduction.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/introduction.tex), [survey_track_a_compressed.tex](/Users/raeez/chiral-bar-cobar/standalone/survey_track_a_compressed.tex), [shadow_towers_v3.tex](/Users/raeez/chiral-bar-cobar/standalone/shadow_towers_v3.tex), and [chiral_chern_weil.tex](/Users/raeez/chiral-bar-cobar/standalone/chiral_chern_weil.tex). I also cleaned the stale grep surface in `chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix`.

Verification was grep-based on `chapters/` and `standalone/`: the remaining hits are abelian-only, already carry the Sugawara correction, or are family-specific non-KM statements. I did not run a full TeX build.

**Blocked**

`apply_patch` outside `/Users/raeez/chiral-bar-cobar` was rejected by approval settings, so I could not patch the sibling volume trees. The remaining external fixes are at [ordered_associative_chiral_kd.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd.tex:1277), [ordered_associative_chiral_kd_core.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_core.tex:1338), [foundations_recast_draft.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/foundations_recast_draft.tex:302), [preface.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/frame/preface.tex:460), [introduction.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/introduction.tex:392), [drinfeld_center.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/drinfeld_center.tex:702), and [e1_chiral_algebras.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex:23). The same Vol III file also has repeated instances at lines 122, 202, 1087, 1355, and 1371.


---
STDERR:
OpenAI Codex v0.104.0 (research preview)
--------
workdir: /Users/raeez/chiral-bar-cobar
model: gpt-5.4
provider: openai
approval: never
sandbox: workspace-write [workdir, /tmp, $TMPDIR]
reasoning effort: xhigh
reasoning summaries: auto
session id: 019d885b-7580-7803-940b-cc89948e3e1c
--------
user
<task>
You are a FINAL GAPS agent. This is the LAST PASS. Every remaining gap must be closed.
832 agents have already run. You fix what they couldn't finish.
Read files on disk — they reflect ALL prior work. Be surgical. Be complete.
</task>
<action_safety>Keep changes scoped. After edits, re-read and verify. Grep for AP violations.</action_safety>
<completeness_contract>Fix EVERY issue in your scope. Report: FIXED or BLOCKED (with reason).</completeness_contract>
<verification_loop>After all edits, verify no new violations introduced.</verification_loop>


Fix av(r(z)) Sugawara shift across ALL volumes (timed-out C06).

NARROW SCOPE: only fix instances where av(r(z))=kappa is stated for non-abelian KM
WITHOUT the Sugawara shift dim(g)/2. Don't rewrite whole files.

grep -rn 'av.*r.*kappa\|averaging.*kappa' chapters/ standalone/ | head -30
Do the same in Vol II and Vol III.
For each: add "for abelian" qualifier or add "+ dim(g)/2 Sugawara shift for non-abelian KM."

mcp startup: no servers



thinking
**Planning coding response**

I need to respond as a coding agent and follow specific instructions. Before making any edits, I have to read various files and resources to ensure I have a good understanding. It looks like I should utilize cross-volume-propagation and possibly multi-path-verify. The user is focused on narrowing the scope of formula drift across all volumes, and I might need to use the explorer sub-agent for codebase searches. However, I could also handle some of this manually. I need to be attentive to task requirements and network restrictions.
thinking
**Exploring directory access**

I need to consider whether I can search outside writable roots, which are limited to the current repo and /tmp. It seems like only the /Users directory is writable, but the user has requested similar actions in Volumes II and III. I wonder if I can read other directories since sandbox_mode might allow it. Yet, it seems we can't edit outside the writable roots without approval. If Volumes II and III aren’t writable, this could become a blocker for the user's request.
thinking
**Assessing directory access and permissions**

I need to confirm whether I can read certain directories, but permissions seem limited to the current writable repo. The user wants to work across all volumes, so I have to investigate whether Volumes II and III are symlinked or part of the current repo. However, I can’t change sandbox_permissions. It could help to use exec to list directories and focus on updating our plan since this looks like a substantial task. I’ll start with commentaries and then execute commands to read necessary files and search for targets.
codex
Using `cross-volume-propagation` for this pass because the task is a formula-level fix that may recur across Volumes I, II, and III. I’m first reading the required repo-wide control files, then I’ll grep the exact `av(r(z))` / averaging surfaces in all three volumes and patch only the non-abelian KM statements missing the `+\dim(\mathfrak g)/2` Sugawara shift.
exec
/bin/zsh -lc "sed -n '1,220p' CLAUDE.md" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
# CLAUDE.md -- Modular Koszul Duality Programme (Canonical Reference)

## Identity

E_1-E_1 operadic Koszul duality in the homotopical modular chiral realm on algebraic curves. One form (eta = d log(z_1 - z_2)), one relation (Arnold), one object (Theta_A), one equation (D*Theta + 1/2[Theta,Theta] = 0). The primitive object is B^ord(A) = T^c(s^{-1}A-bar): ordered bar, deconcatenation coproduct, R-matrix, Yangian. The symmetric bar B^Sigma is the Sigma_n-coinvariant shadow. Physics IS the homotopy type: A-infinity = scattering, SC^{ch,top} governs the (bulk, boundary) pair, modular L-infinity = genus tower. The five theorems A-D+H are the invariants that survive averaging.

**Bar complex is E_1-coassociative; SC^{ch,top} emerges on the derived center (CRITICAL, corrected 2026-04-12):** The bar complex B^{ord}(A) = T^c(s^{-1}A-bar) is an E_1-chiral coassociative COALGEBRA (over ChirAss^!). It has a differential + deconcatenation coproduct. It does NOT carry SC^{ch,top} structure. The SC^{ch,top} structure (or E_3-TOPOLOGICAL with conformal vector) emerges on the DERIVED CENTER Z^{der}_{ch}(A) = ChirHoch*(A,A), computed USING the bar complex as a resolution. The bar complex is the E_1 engine; the derived center is the SC^{ch,top}/E_3-TOPOLOGICAL output. thm:bar-swiss-cheese (claiming B(A) is an SC-coalgebra) needs retraction or careful restatement — see FOUND-11. princ:sc-two-incarnations in en_koszul_duality.tex states this correctly.

Three volumes by Raeez Lorgat. Vol I *Modular Koszul Duality* (this repo, ~2,650pp). Vol II *A-infinity Chiral Algebras and 3D HT QFT* (~/chiral-bar-cobar-vol2, ~1,704pp). Vol III *CY Categories, Quantum Groups, and BPS Algebras* (~/calabi-yau-quantum-groups, ~259pp). Total ~4,613pp, 120K+ tests, 3,463 tagged claims. This file is the canonical reference; Vols II/III inherit shared content and add volume-specific material.

**Crystallized programme identity (2026-04-12):** We are studying **holomorphic chiral (factorisation) (co)homology** via **bar and cobar chain constructions** at **various different geometric locations**, hence the **different (modular) operads** at play. The geometry determines the operad, the operad determines the bar complex, the bar complex computes the factorisation (co)homology. The five theorems are structural properties. The shadow tower is the characteristic class data. The E_n circle is the holographic structure.

**The E_n operadic circle (2026-04-12):** E_3-TOPOLOGICAL(bulk) → E_2(boundary chiral) → E_1(bar/QG) → E_2(Drinfeld center) → E_3-TOPOLOGICAL(derived center). Each arrow is: restriction to codim-2 defect, ordered bar complex, categorified averaging (Drinfeld center), higher Deligne (derived center). The circle closes for 3d HT theories with conformal vector; without conformal vector, stuck at SC^{ch,top} (the intermediary between E_1-chiral and E_3-topological).

**SC^{ch,top} ≠ E_3 (2026-04-12):** The Swiss-cheese operad is two-coloured with directionality (no open-to-closed). Dunn additivity does NOT apply. E_3 requires the topologization theorem: SC^{ch,top} + inner conformal vector (Sugawara at non-critical level, making C-translations Q-exact) = E_3-TOPOLOGICAL. Without conformal vector: stuck at SC^{ch,top}. thm:topologization in en_koszul_duality.tex PROVED for affine KM V_k(g) at non-critical level k != -h^v (Sugawara explicit). For general chiral algebras with conformal vector (Virasoro, W-algebras): CONJECTURAL (conj:topologization-general), depends on constructing the 3d HT BRST complex. Proof is cohomological (Q-cohomology); for class M, chain-level E_3 may fail.

**Five notions of E_1-chiral algebra (2026-04-12):** (A) strict ChirAss-algebra, (B) A_inf in End^{ch}_A, (C) EK quantum vertex algebra, (D) A_inf in E_1-chiral, (E) factorization on Ran^{ord}(X). Each has own derived center. (B)↔(C) via Drinfeld associator on Koszul locus. Warning installed at algebraic_foundations.tex warn:multiple-e1-chiral.

**Three Hochschild theories (2026-04-12):** (i) Topological HH: E_1-algebra input → E_2 output (Deligne). (ii) Chiral HH (ChirHoch): E_inf-chiral input → E_inf output, concentrated {0,1,2} (Theorem H). (iii) Categorical HH: dg category input → E_2 with CY shifted Poisson. NEVER conflate. The geometry determines which Hochschild: curve X → chiral, R → topological, CY category → categorical. Constitutional statement in memory/project_hochschild_constitutional_statement.md.

exec
/bin/zsh -lc "sed -n '1,220p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "if [ -f raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,220p' raeeznotes/raeeznotes100/red_team_summary.md; else sed -n '1,220p' archive/raeeznotes/raeeznotes100/red_team_summary.md; fi" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
# Theorem Registry

Auto-generated on 2026-04-13 from the structured claim extractor in `scripts/generate_metadata.py`.

This registry now tracks every `\ClaimStatusProvedHere` block directly from source, so the proved surface cannot silently drift behind the TeX tree.

## Concordance Cross-Check

- `thm:modular-koszul-duality-main` is cited in `chapters/connections/concordance.tex` as the flag theorem, but `chapters/theory/introduction.tex` currently provides only a `\phantomsection` label and no tagged claim block. It is therefore intentionally absent from the structured registry below.
- `thm:shifted-symplectic-complementarity` is the conditional C2 theorem cited by concordance. Its `\ClaimStatusConditional` block contributes to the status totals below, but it does not appear in the proved-only registry tables.

## Snapshot

| Metric | Value |
|---|---:|
| ProvedHere claims | 2367 |
| Total tagged claims | 3112 |
| Active files in `main.tex` | 90 |
| Total `.tex` files scanned | 104 |

 succeeded in 51ms:
\chapter{Concordance with primary literature}
\label{chap:concordance}

\index{concordance|textbf}

This chapter is the constitution of the monograph. When chapters
disagree, this chapter governs. It records the five main theorems
with their precise status and locates every result against the
prior literature: what is proved, what is conditional, what
remains conjectural.

The governing principle is falsification: every claim in these three
volumes is presumed false until it appears below with an explicit
status tag and a proof reference or independent verification trail.
A theorem that contradicts the concordance is not a theorem; it is an
error in the chapter that states it. Omission from this chapter is
itself a verdict: what is not recorded here has not survived scrutiny.
The concordance does not summarize the monograph; the monograph
approximates the concordance.

 succeeded in 51ms:
# Red-Team Summary of Vol1/Vol2 Claim Audit
## Scope
- Formal tagged claims catalogued: **4866**
- Volume I formal claims: **2841**
- Volume II formal claims: **2025**
- Informal/meta claim harvest (README / PROGRAMMES / PROOF_ATLAS / audit notes): **94**
- Every formal claim has an attached attack swarm in the master ledger. The informal harvest is separate because sentence-level slogans are less structurally tagged.

## Status profile
- ProvedHere: **3801**
- Conjectured: **327**
- Heuristic: **35**
- ProvedElsewhere: **513**
- Conditional: **116**
- Open: **74**

## Risk profile
- medium: **1999**
- low: **1913**
- high: **807**

thinking
**Exploring grep commands**

I need to use grep in three volumes. Since only the current repository is writable, I might still need to read from volumes two and three. I'll run grep commands, but instead of grep, it seems better to use rg based on the developer’s preference. I might need a broader search than just the header, but maybe a narrow scope will be enough. I also want to check an exact file and possibly the cross-volume-propagation skill file.
codex
The control surface is loaded. Next I’m enumerating the exact averaging statements in Vol I, then mirroring the same grep in Vol II and Vol III so I can patch only the non-abelian KM hits and leave unrelated prose untouched.
exec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/cross-volume-propagation/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -i 'av.*r.*kappa|averaging.*kappa' chapters standalone | head -30" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
---
name: cross-volume-propagation
description: Use after any mathematical wording, status, label, terminology, or formula change that may recur across Volumes I, II, and III, compute layers, tests, notes, or superseded files. This is the Codex-native equivalent of `/propagate` from `CLAUDE.md`.
---

# Cross-Volume Propagation

This skill exists to stop local truth from coexisting with global drift.

## Sweep

Search all live surfaces that may still advertise the old claim:

- `~/chiral-bar-cobar`
- `~/chiral-bar-cobar-vol2`
- `~/calabi-yau-quantum-groups`
- `compute/`
- `compute/tests/`
- relevant notes, standalones, or superseded files if they still mislead future audits

 succeeded in 51ms:
standalone/cy_quantum_groups_6d_hcs.tex:170:families $\mathrm{av}(r(z)) = \kappa_{\mathrm{ch}}$, while for
standalone/cy_quantum_groups_6d_hcs.tex:172:$\mathrm{av}(r(z))+\dim(\fg)/2 = \kappa_{\mathrm{ch}}$.
standalone/cy_quantum_groups_6d_hcs.tex:452:map gives $\mathrm{av}(r(z)) = k = \kappa_{\mathrm{ch}}(H_k)$.
standalone/ordered_chiral_homology.tex:6069:and its averaging gives $\kappa = 3(k+2)/4$
standalone/garland_lepowsky.tex:1324: $\mathrm{av}(r(z)) + \dim(\fg)/2 = \kappa(\ghat_k)$.
standalone/holographic_datum.tex:386:algebras, $\av(r(z)) = \kappa$ directly. For non-abelian affine
standalone/holographic_datum.tex:545:abelian prototype: $\av(r(z)) = \av(k/z) = k = \kappa$.
standalone/e1_primacy_ordered_bar.tex:833:  $\av(r(z)) = \kappa_{\mathrm{dp}}
standalone/e1_primacy_ordered_bar.tex:1201:$\av(r_0(z)) = \kappa(\cA)$ on abelian families, while for
standalone/e1_primacy_ordered_bar.tex:1203:$\av(r_0(z)) = \kappa_{\mathrm{dp}}(\cA)$ and
standalone/e1_primacy_ordered_bar.tex:1235:statement $\av(r(z)) = \kappa$ says this exactly for Heisenberg,
standalone/e1_primacy_ordered_bar.tex:1427:($\Sigma_2$-average $\to \kappa$) on the symmetric side. The
standalone/e1_primacy_ordered_bar.tex:1650:\item $\av(r(z)) = \kappa(\cH_k) = k$
standalone/e1_primacy_ordered_bar.tex:1717:\item $\av(r(z)) = \kappa_{\mathrm{dp}}
standalone/survey_track_a_compressed.tex:366:\mathrm{av}\bigl(r(z)\bigr)\;=\;\kappa(\cA),
standalone/survey_track_a_compressed.tex:416:$\mathrm{av}(r(z))=k=\kappa(\mathcal H_k)$. For Heisenberg the
standalone/survey_track_a_compressed.tex:426:\mathrm{av}(k\Omega/z)\;=\;\frac{k\dim\mathfrak g}{2h^\vee}\;=\;\kappa_{\mathrm{dp}}(\widehat{\mathfrak g}_k),
standalone/programme_summary.tex:728:$\mathrm{av}(r(z)) = \kappa_{\mathrm{dp}}(\cA)$ and
standalone/survey_modular_koszul_duality_v2.tex:453:\mathrm{av}\bigl(r^{\cH}(z)\bigr)=k=\kappa(\cH_k).
standalone/survey_modular_koszul_duality_v2.tex:581:\text{degree }2\colon&\quad\mathrm{av}(r(z))+\kappa_{\mathrm{sp}}=\kappa(\cA)
exec
/bin/zsh -lc "rg -n -i 'av.*r.*kappa|averaging.*kappa' /Users/raeez/calabi-yau-quantum-groups/chapters /Users/raeez/calabi-yau-quantum-groups/standalone | head -30" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -i 'av.*r.*kappa|averaging.*kappa' /Users/raeez/chiral-bar-cobar-vol2/chapters /Users/raeez/chiral-bar-cobar-vol2/standalone | head -30" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
/Users/raeez/chiral-bar-cobar-vol2/chapters/frame/preface.tex:286:averaging (for abelian algebras $\kappa = \mathrm{av}(r(z))$;
/Users/raeez/chiral-bar-cobar-vol2/chapters/frame/preface.tex:533:$\mathrm{av}(r(z)) = \kappa$ for abelian algebras (Heisenberg,
/Users/raeez/chiral-bar-cobar-vol2/chapters/frame/preface.tex:535:$\mathrm{av}(r(z)) + \dim\fg/2 = \kappa$ (the Sugawara shift
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/factorization_swiss_cheese.tex:955:\item $h \cdot R + R \cdot h$: the cross-term.  The residue of $h \cdot R$ at $z_1 = z_2$ extracts the OPE coefficient at the simple pole, leaving $R(z_2, z_3)$ evaluated at $z_2 = z_3$.  Since $\bar\partial R = -\omega_{\mathrm{Ar}}$ (the Arakelov $(1,1)$-form), and the OPE coefficient is the structure constant weighted by $\kappa(\cA) = \mathrm{Tr}_\cA$, the double residue produces $\kappa(\cA) \cdot \omega_g$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/foundations_recast_draft.tex:302:The open colour of the Swiss-cheese pair $(A^{\mathrm{bulk}}, A^{\mathrm{bdy}})$ carries additional Hopf-algebraic structure formalized in Vol~III (\S7 of the $E_1$-chiral algebras chapter): the $E_1$-chiral bialgebra axioms~(H1)--(H5). The coproduct $\Delta_z \colon A \to A \otimes_{E_1,z} A$ lives on the open ($E_1$/topological) colour, not the closed ($E_2$/chiral) colour. The $E_\infty$ averaging map $\mathrm{av} \colon B^{\mathrm{ord}}(A) \to B^{\Sigma}(A)$ destroys the Hopf data: $\mathrm{av}(r(z)) = \kappa_{\mathrm{ch}}$, a scalar (Vol~III, Proposition~\texttt{prop:averaging-forgets-hopf}). The braided ($E_2$) structure is recovered via the Drinfeld center $\cZ(\Rep^{E_1}(A))$, not by direct construction on the closed colour. The universal coproduct at all spins is $\Delta_z(e_s) = \sum (-1)^k \binom{N_R - b}{k} z^k \, e_a^L \cdot e_b^R$ (Vol~III, Proposition~\texttt{prop:universal-coproduct}).
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:2248:(\S\ref{subsec:gravity-genus-tower}) uses $\kappa_{\mathrm{eff}}$;
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_perturbative_finiteness.tex:418:The shadow free energy $F_g(\cA)$ is the $(r,g) = (0,g)$ component of the shadow algebra $\cA^{\mathrm{sh}} = H_\bullet(\Defcyc^{\mathrm{mod}}(\cA))$ in the bigrading by degree~$r$ and genus~$g$. The higher-degree shadows at genus $g$ (the cubic shadow $\mathfrak{C}_g$ at $r = 3$, the quartic resonance class $\mathfrak{Q}_g$ at $r = 4$) encode the gravitational interactions beyond the free-energy level. The shadow free energy is the simplest invariant, controlled entirely by the modular characteristic $\kappa(\cA)$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_perturbative_finiteness.tex:794:\item \emph{Scalar partition function on the proved scalar lane.} If $\cA$ has generators of uniform conformal weight, then the series $\sum_{g=1}^{\infty} F_g(\cA)\,\hbar^g$ converges absolutely for $|\hbar| < 4\pi^2$, with the closed-form expression $Z_{\mathrm{grav}}^{\mathrm{scal}}(\cA;\,\hbar) = \kappa(\cA) \cdot \frac{\sqrt{\hbar}/2}{\sin(\sqrt{\hbar}/2)}$. For arbitrary modular Koszul algebras, the universal scalar statement is the finite genus-$1$ term $F_1(\cA)=\kappa(\cA)/24$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_perturbative_finiteness.tex:1198:The scalar gravitational partition function $Z^{\mathrm{scal}}_{\mathrm{grav}}(\cA;\,\hbar) = \kappa \cdot \frac{\sqrt{\hbar}/2}{\sin(\sqrt{\hbar}/2)}$ has:
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_perturbative_finiteness.tex:1539:The meromorphic function $Z^{\mathrm{scal}}_{\mathrm{grav}}(\hbar) = \kappa \cdot \frac{\sqrt{\hbar}/2}{\sin(\sqrt{\hbar}/2)}$ admits a non-perturbative completion satisfying:
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_perturbative_finiteness.tex:1572:$Z_{\mathrm{grav}}(\hbar) = \kappa \cdot \frac{\sqrt{\hbar}/2}{\sin(\sqrt{\hbar}/2)}$
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_perturbative_finiteness.tex:1657:For higher-spin gravity in AdS$_3$ with $\mathcal{W}_N$ symmetry, the boundary algebra is $\mathcal{W}_k(\mathfrak{sl}_N)$ at central charge $c = (N-1) - N(N^2-1)(k+N-1)^2/(k+N)$. The modular characteristic is $\kappa(\mathcal{W}_N) = c \cdot (H_N - 1)$ where $H_N = \sum_{j=1}^N 1/j$ is the $N$-th harmonic number ($\kappa = c/2$ for $N=2$, $\kappa = 5c/6$ for $N=3$). The perturbative partition function is
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_perturbative_finiteness.tex:1659:Z_{\mathrm{grav}}^{W_N}(\hbar) \;=\; \kappa(\mathcal{W}_N) \cdot \frac{\sqrt{\hbar}/2}{\sin(\sqrt{\hbar}/2)}\,,
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_perturbative_finiteness.tex:1692:$Z_{\mathrm{grav}}^{\mathrm{scal}} = \kappa \cdot x/(2\sin(x/2))$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_perturbative_finiteness.tex:2716:S_{\mathrm{sh}}(\cA;\,\hbar) \;:=\; \log Z^{\mathrm{scal}}_{\mathrm{grav}}(\cA;\,\hbar) \;=\; \log\kappa + \log\frac{\sqrt{\hbar}/2}{\sin(\sqrt{\hbar}/2)}\,.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_perturbative_finiteness.tex:2806: Z_{\mathrm{grav}}^{\mathrm{scal}}(\cA;\,\hbar) \;=\; \sum_{j=1}^m \kappa(\cA_j) \cdot \frac{\sqrt{\hbar}/2}{\sin(\sqrt{\hbar}/2)}.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_perturbative_finiteness.tex:3540: $Z_{\mathrm{grav}}^{\mathrm{scal}}(\cA;\,\hbar) = \kappa(\cA) \cdot
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_perturbative_finiteness.tex:3697:For practical computation of the gravitational partition function at $|\hbar| = 1$ and $\kappa = O(1)$, the genus expansion converges extremely rapidly: the $g$-th term is of order $1/(2\pi)^{2g} \approx (0.0253)^g$. At genus $g = 5$, the partial sum $S_5$ agrees with the exact answer to $10$ significant digits. At genus $g = 10$, the agreement is to $20$ digits. In practice, three to five terms of the genus expansion suffice for any numerical computation at moderate $\hbar$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd.tex:1277:$\operatorname{av}(r(z)) = \kappa(\cA)$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/modular_pva_quantization.tex:1557:auxiliary affine algebra, but it leaves the scalar~$\kappa$ undetermined.
 succeeded in 52ms:
rg: /Users/raeez/calabi-yau-quantum-groups/standalone: No such file or directory (os error 2)
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:568:%: av is lossy. The R-matrix r(z) has more information than kappa.
/Users/raeez/calabi-yau-quantum-groups/chapters/frame/preface.tex:460:structure via averaging $\mathrm{av}(r(z)) = \kappa_{\mathrm{ch}}$.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/introduction.tex:392:$\mathrm{av}(r(z)) = \kappa_{\mathrm{ch}}$. The $E_1$-chiral
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3_times_e.tex:663:The identity $\DT = \mathrm{PT}$ for $K3 \times E$ means that the contribution of zero-dimensional sheaves (the MacMahon sector) is invisible. This is the enumerative counterpart of the vanishing $\chi(X) = 0$: the degree-$0$ virtual class is trivial. Note: the chiral algebra modular characteristic $\kappa_{\mathrm{ch}}(K3 \times E) = 3$ (Section~\ref{sec:k3e-cross-volume}, K3-1), computed by additivity from $\kappa_{\mathrm{ch}}(K3) = 2$ and $\kappa_{\mathrm{ch}}(E) = 1$, does \emph{not} vanish; the global BPS modular characteristic $\kappa_{\mathrm{BKM}} = 5$ (the Borcherds lift weight, Proposition~\ref{prop:k3e-fiber-global}) is a different invariant incorporating the full BPS spectrum beyond the chiral algebra. The vanishing $\chi_{\mathrm{top}}/24 = 0$ is a virtual/enumerative statement, not a shadow tower statement. The nontrivial enumerative content resides entirely in curve-class contributions, organized by the Borcherds product (Theorem~\ref{thm:k3e-product}).
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:5194:The identity $\DT = \mathrm{PT}$ for $K3 \times E$ means that the contribution of zero-dimensional sheaves (the MacMahon sector) is invisible. This is the enumerative counterpart of the vanishing $\chi(X) = 0$: the degree-$0$ virtual class is trivial. Note: the chiral algebra modular characteristic $\kappa_{\mathrm{ch}}(K3 \times E) = 3$ (Section~\ref{sec:k3e-cross-volume}, K3-1) does \emph{not} vanish; the vanishing $\chi/12 = 0$ is a virtual/enumerative statement, not a shadow tower statement. The nontrivial enumerative content resides entirely in curve-class contributions, organized by the Borcherds product (Theorem~\ref{thm:k3e-product}).
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/braided_factorization.tex:494:At degree $2$: $\mathrm{av}(\cR(z)) = \kappa_{\mathrm{cat}}$.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/braided_factorization.tex:598:$\mathrm{av}(\cR^{-1}) = \kappa_{\mathrm{cat}}(\cA^!_{E_2})$.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/drinfeld_center.tex:702:$\mathrm{av}(r(z)) = \kappa_{\mathrm{ch}}$ extracts the scalar
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cyclic_ainf.tex:200:Four source threads feed the construction used here. Stasheff~\cite{Stasheff1963} introduced the associahedra and the higher homotopies $\mu_n$. Kontsevich~\cite{Kontsevich1995} identified cyclic $\Ainf$-algebras with algebras over the operad of ribbon graphs, providing the link to moduli of curves with boundary. Costello~\cite{Costello2005TCFT,Costello2007Ainfty} proved that cyclic $\Ainf$-categories are equivalent to open topological conformal field theories and supplied the first rigorous construction of the associated chain-level trace. Kontsevich--Soibelman~\cite{KontsevichSoibelman2009} axiomatized the CY structure in terms of the negative cyclic class and gave the formalism used in Part~\ref{part:cy-categories}. Keller~\cite{Keller2001Ainfty} surveys the homological-algebra side. For explicit computations on projective varieties, Polishchuk~\cite{Polishchuk2011} computed the cyclic $\Ainf$-structure on elliptic curves and on their products, and Caldararu~\cite{Caldararu2005} set up the Hochschild calculus for smooth proper CY categories. The Vol~III role is the specific mapping of this input through the functor $\Phi$, producing chiral algebras whose modular characteristic can be computed and compared across the four kappas of the spectrum.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex:1770:\noindent Three remarks on the table entries. First, $K3 \times E$ does not have a quiver atlas in the strict sense of Definition~\ref{def:quiver-chart-atlas}: the derived category $D^b(\Coh(K3 \times E))$ does not admit a single tilting generator, and the fibration structure requires a different gluing mechanism (the relative Fourier--Mukai, see Chapter~\ref{ch:k3-times-e}). The table records $\kappa_{\mathrm{ch}} = 3$ by additivity ($\kappa_{\mathrm{ch}}(\mathrm{K3}) + \kappa_{\mathrm{ch}}(E) = 2 + 1$, Proposition~\ref{prop:categorical-euler}); the distinct Borcherds automorphic weight is $\kappa_{\mathrm{BKM}} = 5 = \mathrm{wt}(\Delta_5)$. Second, the quintic has $|I| = 2$ charts: one at large volume (a quiver chart from the Beilinson collection restricted to $X$) and one at the Gepner point (a matrix factorization category $\MF(W_{\mathrm{Fermat}})$, which is NOT a quiver chart; see Remark~\ref{rem:gepner-lv-dichotomy}). Third, the shadow class and depth $r_{\mathrm{max}}$ refer to the Heisenberg truncation ($s = 1$ channel). At the full spin tower, the classification may differ (Remark~\ref{rem:c3-per-channel}).
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex:23:This averaging is \emph{lossy}: $\mathrm{av}(r(z)) = \kappa_{\mathrm{ch}}$ forgets the
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex:122:is a morphism of cochain complexes and sends the $E_1$ structure to the $E_\infty$ structure. It is lossy: the kernel contains the $R$-matrix data of the holomorphic factor, and on degree two $\mathrm{av}(r(z)) = \kappa_{\mathrm{ch}}$.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex:127:Averaging the degree-two generator $r(z)$ returns the scalar $\kappa_{\mathrm{ch}}$, the unique $S_2$-coinvariant of the collision residue. When the same $r(z)$ comes from the CY-to-chiral functor applied to $D^b(\Coh(K3 \times E))$, the scalar is $\kappa_{\mathrm{ch}} = 3$ by additivity: $\kappa_{\mathrm{ch}}(K3) + \kappa_{\mathrm{ch}}(E) = 2 + 1$. This differs from the categorical Euler characteristic $\kappa_{\mathrm{cat}} = 2$, the lattice-rank invariant $\kappa_{\mathrm{fiber}} = 24$, and the BKM weight $\kappa_{\mathrm{BKM}} = 5$. An unsubscripted symbol would conflate distinct invariants.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex:131:The CY-to-chiral functor $\Phi$ of Chapter~\ref{ch:cy-to-chiral} has three natural composites. $\Phi_{E_1}$ produces $B^{\mathrm{ord}}(A_C)$; this is the ordered bar sensed by the Yangian. $\mathrm{av} \circ \Phi_{E_1}$ produces $B^{\Sigma}(A_C)$; this is the symmetric bar sensed by the modular characteristic $\kappa_{\mathrm{ch}}$. The full $E_2$ enhancement $\Phi_{E_2}$ produces the Drinfeld-centered bar $B^{E_2}(A_C) = \cZ(B^{\mathrm{ord}}(A_C))$; this is the braided bar sensed by the quantum group. All three factor through $\Phi_{E_1}$. In this volume, the ordered bar is the primitive object.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex:202: ($\mathrm{av}(r(z)) = \kappa_{\mathrm{ch}}$) \\
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex:261: $\mathrm{av}(R(z))|_{z=0} = \kappa_{\mathrm{ch}} \cdot \mathrm{id}$.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex:316:The three volumes are three faces of a single $E_1$-$E_1$ operadic Koszul duality. Volume~I is the symmetric modular face: it develops $B^{\Sigma}$, the five theorems A-D+H, and the modular characteristic $\kappa_{\mathrm{ch}}$ in the uniform-weight setting. Volume~II is the $E_1$ open-colour face: it develops $B^{\mathrm{ord}}$, the Swiss-cheese operad, the $r(z)$-matrix with its seven faces, and the three-dimensional holomorphic-topological bridge to quantum gravity. Volume~III is the CY-geometric face: it develops the functor $\Phi$ that produces the input algebra from a Calabi-Yau category, identifies $\kappa_{\mathrm{ch}}$ within the kappa-spectrum, and traces the quantum group back to its geometric origin in BPS state counts.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex:345:The three volumes use different coalgebra conventions in their displayed formulas. Vol~I displays formulas in $B^{\Sigma}$ with the symmetric coproduct; Vol~II displays formulas in $B^{\mathrm{ord}}$ with deconcatenation; Vol~III displays formulas in whichever form the CY functor produces, which is always $B^{\mathrm{ord}}$ at the source but frequently $B^{\Sigma}$ after averaging to extract $\kappa_{\mathrm{ch}}$. The reader who cross-references a formula between volumes must convert between the three coalgebra structures: $B^{\mathrm{ord}} \to B^{\Sigma}$ by averaging (dividing by $n!$ and symmetrizing), and $B^{\Sigma} \to B^{\mathrm{Lie}}$ by taking the iterated commutator of the cofree tensor coalgebra. The three bars are NOT isomorphic even as complexes; they differ by $S_n$-coinvariant quotients, and the Euler characters diverge accordingly. See Vol~II for the three-bar sequence.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex:1087: $\mathrm{av}(r(z)) = \kappa_{\mathrm{ch}}$ (a scalar), so the full



thinking
**Determining problematic hits**

I need to figure out which hits are actually problematic and editable, focusing specifically on instances where av(r(z)) = kappa is stated for non-abelian KM without any shifts. I should search through the files and lines related to this issue in all volumes. Many hits are already qualified, but I have to inspect the surrounding context for each potential bad hit. Searching for "av(r(z)) = \kappa" and "averaging ... kappa" could be helpful. I will analyze candidate files from the volumes based on user direction.
thinking
**Expanding search and editing process**

I need to use `rg -n -C 3` around hits that have specific patterns, and possibly `sed -n` for file ranges. I should consider mentioning PE-2, which relates to the verification protocol triggered by the kappa formula. There might also be PE-8 cross-volume implications, and I need to include a fenced commentary block before making edits. It seems I shouldn't rewrite entire files; instead, I'll focus on identifying candidate bad statements. The search results show some statements are correct already, but I need to inspect certain files closely in Volumes I and III for accuracy.
thinking
**Examining κ relationships**

I'm considering that maybe the affine KM already provides k dim/2hv = κ_dp, but there might be a missing shift. I wonder if κ_dp, which could relate to divided-power, is equal to the average? For non-abelian cases, it seems the formula should be average plus dim/2 = κ. I need to clarify if they are using κ_dp as the average or if it's distinct from κ. Definitely need to take a closer look at this!
codex
I have the hit list. Now I’m reading only the local contexts around the plausible non-abelian KM statements, because several matches are already correct or are abelian-only, and this pass needs to avoid collateral edits.
exec
/bin/zsh -lc "sed -n '6048,6084p' standalone/ordered_chiral_homology.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
parameter is $q = e^{2\pi i/(k+2)}$ and
$q^{k+2} = 1$. The KZB local system acquires finite
monodromy, and the ordered chiral homology at each degree
becomes a finite-dimensional representation of the mapping
class group of $E_\tau$ with $n$ marked points. The
$k + 1$ integrable modules $V_0, \ldots, V_k$ of
$U_q(\mathfrak{sl}_2)$ correspond to the truncation of the
degree-by-degree decomposition: at degree $n > k$, the
representation theory constrains certain components to
vanish.
\end{remark}

\begin{remark}[The elliptic $R$-matrix as ordered datum]
\label{rem:ell-r-matrix-ordered}
The Belavin elliptic $r$-matrix
$r^{\mathrm{ell}}(z, \tau) = k \cdot r^{\mathrm{Belavin}}
(z, \tau)$ is the degree-$2$ projection of the genus-$1$
Maurer--Cartan element
$\Theta_\cA^{(1)} \in \gEone$. It satisfies the classical
Yang--Baxter equation with spectral parameter (verified
exec
/bin/zsh -lc "sed -n '1640,1730p' standalone/e1_primacy_ordered_bar.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1190,1248p' standalone/e1_primacy_ordered_bar.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '820,850p' standalone/e1_primacy_ordered_bar.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '356,434p' standalone/survey_track_a_compressed.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '718,740p' standalone/programme_summary.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '150,170p' standalone/programme_summary_sections2_4.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\begin{remark}[Concrete examples]
\label{rem:concrete-r-kappa}
The principal families:
\begin{itemize}
\item Heisenberg $\cH_k$:
  $r(z) = k/z$,
  $\kappa(\cH_k) = k$.
  % AP126 check: k=0 -> r=0. Y.

\item Affine Kac--Moody $\widehat{\fg}_k$:
  $r(z) = k\,\Omega_\fg/z$
  (the level~$k$ survives $d\log$ absorption; at $k=0$ the
  $r$-matrix vanishes identically),
  $\av(r(z)) = \kappa_{\mathrm{dp}}
  = k\,\dim(\fg)/(2h^\vee)$,
  and
  $\kappa(\widehat{\fg}_k)
  = \dim(\fg)(k+h^\vee)/(2h^\vee)$.

\item Virasoro $\Vir_c$:
 succeeded in 52ms:
\label{thm:ordered-D}
The formal ordered degree-$2$ shadow series
\begin{equation}\label{eq:ordered-D}
  R^{\Eone,\mathrm{bin}}(z;\hbar)
  \;=\;
  \sum_{g \geq 0} \hbar^{2g}\, r_g(z)
\end{equation}
obtained from the genus-refined degree-$2$ projection of the $\Eone$
Maurer--Cartan element is the $\Eone$ degree-$2$ characteristic
package of~$\cA$. It is universal, additive, antisymmetric under
opposite-duality, and satisfies
$\av(r_0(z)) = \kappa(\cA)$ on abelian families, while for
non-abelian affine Kac--Moody
$\av(r_0(z)) = \kappa_{\mathrm{dp}}(\cA)$ and
$\kappa(\cA) = \kappa_{\mathrm{dp}}(\cA) + \dim(\fg)/2$.
The coinvariant recovery
$\av(R^{\Eone,\mathrm{bin}}) = \sum \hbar^{2g}\, F_g^{(2)}$
is the scalar genus-$2$ modular characteristic series of
Theorem~D.
\end{theorem}
 succeeded in 52ms:
This section gives the complete degree-$2$ ordered computation
for the two simplest families and records the passage through $\av$
to the scalar shadow. The computations are self-contained and
illustrate every step of the $\Eone$ primacy thesis.

\subsection{Heisenberg}

For $\cH_k$ with OPE $J(z)J(w) \sim k/(z-w)^2$:
\begin{itemize}
\item $r(z) = k/z$ (equation~\eqref{eq:heis-r-matrix}).
\item $\av(r(z)) = \kappa(\cH_k) = k$
  (the $\Sigma_2$-average of $k/z$ against $d\log(z)$ extracts
  the residue $k$, which is the full modular characteristic).
  % PE-2 check: k=0 -> kappa = 0. Y.
\item $\ker(\av_2) = 0$ (one-dimensional representation).
\item Bar cohomology $H^{-1}(\Barord(\cH_k)) = \CC \cdot s^{-1}J$:
  concentrated in bar degree~$1$. Koszul dual:
  $\cH_k^! = (\cH_k^{\mathrm{i}})^\vee$ with
  $\kappa(\cH_k^!) = -k$. Complementarity:
  $\kappa(\cH_k) + \kappa(\cH_k^!) = k + (-k) = 0$
 succeeded in 51ms:
this descent is not naive: it uses the spectral $R$-matrix $R(z)$ as
twisting datum. The $R$-matrix is the degree-$2$ collision residue of
the ordered Maurer--Cartan element,
\[
r(z)\;=\;\operatorname{Res}^{\mathrm{coll}}_{0,2}\bigl(\Theta^{E_1}_{\cA}\bigr),
\]
a matrix-valued rational function encoding the full binary OPE data.
Applying $\mathrm{av}$ at degree~$2$ collapses the profile to a single
scalar,
\begin{equation}\label{eq:av-organizing}
\mathrm{av}\bigl(r(z)\bigr)\;=\;\kappa(\cA),
\end{equation}
the modular characteristic of Theorem~D. At degree~$3$ the KZ
associator projects to the cubic shadow~$\mathfrak C$; at degree~$4$
the Yangian higher coproduct projects to the quartic resonance
class~$\mathfrak Q$. Each degree-$n$ component of the ordered
Maurer--Cartan element projects under $\mathrm{av}$ to the degree-$n$
shadow of the modular obstruction tower $\Theta_{\cA}$.

\medskip
 succeeded in 51ms:
\end{equation}
where $\omega_g$ is the Arakelov $(1,1)$-form on the fibre
and $\kappa(\cA) \in \Bbbk$ is the \emph{modular
characteristic}. The modular characteristic is intrinsic to
the chiral algebra; it is determined by the leading OPE
singularity and is visible already at genus~$0$ as the
$\Sigma_2$-coinvariant scalar shadow of the collision residue:
for abelian and Virasoro-type families
$\kappa(\cA) = \mathrm{av}(r(z))$, while for non-abelian
affine Kac--Moody in the trace-form convention
$\mathrm{av}(r(z)) = \kappa_{\mathrm{dp}}(\cA)$ and
$\kappa(\cA) = \kappa_{\mathrm{dp}}(\cA) + \dim(\fg)/2$.

The failure of $d^2 = 0$ at genus~$g \ge 1$ is not a defect
of the construction; it is the construction detecting global
geometry. Period integrals restore nilpotence: the
Gauss--Manin connection absorbs the fibrewise curvature, and
the total differential satisfies $D_g^2 = 0$. The
curvature~\eqref{eq:d-squared-curvature} is the
infinitesimal avatar of this restoration.
 succeeded in 50ms:
$\Sigma_2$-coinvariant scalar shadow of the collision residue:
for abelian and Virasoro-type families
$\kappa(\cA) = \mathrm{av}(r(z))$, while for non-abelian
affine Kac--Moody in the trace-form convention
$\mathrm{av}(r(z)) = \kappa_{\mathrm{dp}}(\cA)$ and
$\kappa(\cA) = \kappa_{\mathrm{dp}}(\cA) + \dim(\fg)/2$.

The failure of $d^2 = 0$ at genus~$g \ge 1$ is not a defect
of the construction; it is the construction detecting global
geometry. Period integrals restore nilpotence: the
Gauss--Manin connection absorbs the fibrewise curvature, and
the total differential satisfies $D_g^2 = 0$. The
curvature~\eqref{eq:d-squared-curvature} is the
infinitesimal avatar of this restoration.

% ====================================================================
\subsection{The genus expansion}
\label{ssec:genus-expansion}
% ====================================================================

codex
A few Vol I hits are already correct. I’m broadening to the exact symbolic variants of `av(r(z)) = \kappa` so I don’t miss the remaining generic statements that the first grep only surfaced indirectly.
exec
/bin/zsh -lc "rg -n '\\\\(?:av|mathrm\\{av\\}|operatorname\\{av\\})\\s*\\(r(?:_0)?\\(z\\)\\)\\s*=\\s*\\\\kappa|\\\\(?:av|mathrm\\{av\\}|operatorname\\{av\\})\\s*\\(r(?:_0)?\\(z\\)\\)\\s*=\\s*\\\\kappa_\\{["'^}]+'"\\}|averag[a-z]*["'^'"\\n]{0,120}\\\\kappa' /Users/raeez/chiral-bar-cobar-vol2/chapters /Users/raeez/chiral-bar-cobar-vol2/standalone" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\\\(?:av|mathrm\\{av\\}|operatorname\\{av\\})\\s*\\(r(?:_0)?\\(z\\)\\)\\s*=\\s*\\\\kappa|\\\\(?:av|mathrm\\{av\\}|operatorname\\{av\\})\\s*\\(r(?:_0)?\\(z\\)\\)\\s*=\\s*\\\\kappa_\\{["'^}]+'"\\}|averag[a-z]*["'^'"\\n]{0,120}\\\\kappa' chapters standalone" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd.tex:1277:$\operatorname{av}(r(z)) = \kappa(\cA)$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/frame/preface.tex:286:averaging (for abelian algebras $\kappa = \mathrm{av}(r(z))$;
/Users/raeez/chiral-bar-cobar-vol2/chapters/frame/preface.tex:533:$\mathrm{av}(r(z)) = \kappa$ for abelian algebras (Heisenberg,
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_core.tex:1338:$\operatorname{av}(r(z)) = \kappa(\cA)$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/foundations_recast_draft.tex:302:The open colour of the Swiss-cheese pair $(A^{\mathrm{bulk}}, A^{\mathrm{bdy}})$ carries additional Hopf-algebraic structure formalized in Vol~III (\S7 of the $E_1$-chiral algebras chapter): the $E_1$-chiral bialgebra axioms~(H1)--(H5). The coproduct $\Delta_z \colon A \to A \otimes_{E_1,z} A$ lives on the open ($E_1$/topological) colour, not the closed ($E_2$/chiral) colour. The $E_\infty$ averaging map $\mathrm{av} \colon B^{\mathrm{ord}}(A) \to B^{\Sigma}(A)$ destroys the Hopf data: $\mathrm{av}(r(z)) = \kappa_{\mathrm{ch}}$, a scalar (Vol~III, Proposition~\texttt{prop:averaging-forgets-hopf}). The braided ($E_2$) structure is recovered via the Drinfeld center $\cZ(\Rep^{E_1}(A))$, not by direct construction on the closed colour. The universal coproduct at all spins is $\Delta_z(e_s) = \sum (-1)^k \binom{N_R - b}{k} z^k \, e_a^L \cdot e_b^R$ (Vol~III, Proposition~\texttt{prop:universal-coproduct}).
 succeeded in 51ms:
chapters/examples/y_algebras.tex:632:$\mathrm{av}(r(z)) = \kappa = \Psi$, recovering the
standalone/ordered_chiral_homology.tex:6069:and its averaging gives $\kappa = 3(k+2)/4$
standalone/en_chiral_operadic_circle.tex:2650:For the Heisenberg (abelian), $\mathrm{av}(r(z)) = \kappa$
standalone/en_chiral_operadic_circle.tex:2657:averaging, and is the reason $\kappa(V_k(\fg)) \neq 0$ at
standalone/chiral_chern_weil.tex:1216:The averaging map extracts~$\kappa$ from the $r$-matrix.
standalone/chiral_chern_weil.tex:1331: & $\av(r(z)) = \kappa_{\mathrm{cl}}$ \\
standalone/e1_primacy_ordered_bar.tex:833:  $\av(r(z)) = \kappa_{\mathrm{dp}}
standalone/e1_primacy_ordered_bar.tex:1201:$\av(r_0(z)) = \kappa(\cA)$ on abelian families, while for
standalone/e1_primacy_ordered_bar.tex:1203:$\av(r_0(z)) = \kappa_{\mathrm{dp}}(\cA)$ and
standalone/e1_primacy_ordered_bar.tex:1235:statement $\av(r(z)) = \kappa$ says this exactly for Heisenberg,
standalone/e1_primacy_ordered_bar.tex:1427:($\Sigma_2$-average $\to \kappa$) on the symmetric side. The
standalone/e1_primacy_ordered_bar.tex:1650:\item $\av(r(z)) = \kappa(\cH_k) = k$
standalone/e1_primacy_ordered_bar.tex:1717:\item $\av(r(z)) = \kappa_{\mathrm{dp}}
standalone/N3_e1_primacy.tex:501: $\av(r(z)) = \kappa_{\mathrm{dp}}(\widehat\fg_k)
standalone/N3_e1_primacy.tex:707:$\av(r(z)) = \kappa$ says this exactly for Heisenberg, while for
standalone/N3_e1_primacy.tex:781:$\av(r(z)) = \kappa(\cA)$, while for non-abelian affine
standalone/N3_e1_primacy.tex:782:Kac--Moody $\av(r(z)) = \kappa_{\mathrm{dp}}(\cA)$ and the full
standalone/N3_e1_primacy.tex:890:the spectral $r$-matrix $r(z)$ by averaging, giving $\kappa$
standalone/N3_e1_primacy.tex:965:$\av(r(z)) = \kappa(\cA)$, while for non-abelian affine
standalone/N3_e1_primacy.tex:966:Kac--Moody $\av(r(z)) = \kappa_{\mathrm{dp}}(\cA)$ and the full
exec
/bin/zsh -lc "rg -n '\\\\(?:av|mathrm\\{av\\}|operatorname\\{av\\})\\s*\\(r(?:_0)?\\(z\\)\\)\\s*=\\s*\\\\kappa|\\\\(?:av|mathrm\\{av\\}|operatorname\\{av\\})\\s*\\(r(?:_0)?\\(z\\)\\)\\s*=\\s*\\\\kappa_\\{["'^}]+'"\\}|averag[a-z]*["'^'"\\n]{0,120}\\\\kappa' /Users/raeez/calabi-yau-quantum-groups/chapters" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
/Users/raeez/calabi-yau-quantum-groups/chapters/frame/preface.tex:460:structure via averaging $\mathrm{av}(r(z)) = \kappa_{\mathrm{ch}}$.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/drinfeld_center.tex:702:$\mathrm{av}(r(z)) = \kappa_{\mathrm{ch}}$ extracts the scalar
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex:23:This averaging is \emph{lossy}: $\mathrm{av}(r(z)) = \kappa_{\mathrm{ch}}$ forgets the
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex:122:is a morphism of cochain complexes and sends the $E_1$ structure to the $E_\infty$ structure. It is lossy: the kernel contains the $R$-matrix data of the holomorphic factor, and on degree two $\mathrm{av}(r(z)) = \kappa_{\mathrm{ch}}$.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex:202: ($\mathrm{av}(r(z)) = \kappa_{\mathrm{ch}}$) \\
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex:345:The three volumes use different coalgebra conventions in their displayed formulas. Vol~I displays formulas in $B^{\Sigma}$ with the symmetric coproduct; Vol~II displays formulas in $B^{\mathrm{ord}}$ with deconcatenation; Vol~III displays formulas in whichever form the CY functor produces, which is always $B^{\mathrm{ord}}$ at the source but frequently $B^{\Sigma}$ after averaging to extract $\kappa_{\mathrm{ch}}$. The reader who cross-references a formula between volumes must convert between the three coalgebra structures: $B^{\mathrm{ord}} \to B^{\Sigma}$ by averaging (dividing by $n!$ and symmetrizing), and $B^{\Sigma} \to B^{\mathrm{Lie}}$ by taking the iterated commutator of the cofree tensor coalgebra. The three bars are NOT isomorphic even as complexes; they differ by $S_n$-coinvariant quotients, and the Euler characters diverge accordingly. See Vol~II for the three-bar sequence.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex:1087: $\mathrm{av}(r(z)) = \kappa_{\mathrm{ch}}$ (a scalar), so the full
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex:1355:$\mathrm{av}(r(z)) = \kappa_{\mathrm{ch}}$: the full
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex:1371:$R$-matrix & $r(z) = k\,\Omega/z + \cdots$ & $R^{E_2}(z)$ (half-braiding) & $\mathrm{av}(r(z)) = \kappa_{\mathrm{ch}}$ (scalar) \\
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex:1384:transition (averaging) collapses $r(z)$ to $\kappa_{\mathrm{ch}}$
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/introduction.tex:392:$\mathrm{av}(r(z)) = \kappa_{\mathrm{ch}}$. The $E_1$-chiral

thinking
**Analyzing file issues**

I've found some standalone files in Volume I that duplicate content from Volumes II and III. The user wants me to use grep specifically for Volumes II and III. I wonder if I can edit external directories, but at the very least, I can read and report on any blocks.

Maybe I need to ask for permission? But, I don't usually get approval. I'll check if applying a patch can update files outside the root. I need to inspect the contexts from the chapters and those volumes.
codex
I’ve confirmed there are generic statements in Vol I and matching generic statements in Vol II and Vol III. Before editing, I’m reading those exact chapter contexts and checking whether the sandbox will actually let me patch the sibling volume trees; if not, I’ll finish Vol I and report the remaining external hits as blocked by write scope.
exec
/bin/zsh -lc "sed -n '620,644p' chapters/examples/y_algebras.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
$\mathrm{End}(V)$-valued meromorphic function
\begin{equation}\label{eq:y111-r-full}
r(z) \;=\;
\frac{1}{z}
\begin{pmatrix}
\Psi & J \\
J & 2T
\end{pmatrix},
\end{equation}
where the matrix is in the $(J, T)$ basis of
$V = \bC J \oplus \bC T$. The $\Sigma_2$-coinvariant
(averaging map, \S\ref{subsec:concordance-e1-primacy}) gives
$\mathrm{av}(r(z)) = \kappa = \Psi$, recovering the
scalar modular characteristic.
\end{computation}

\begin{remark}[$r$-matrix tier classification]%
\label{rem:y111-r-tier}
\index{r-matrix@$r$-matrix!tier classification!Y111@$Y_{1,1,1}$}
The $r$-matrix of $Y_{1,1,1}[\Psi]$ is tier~(b) in the
exec
/bin/zsh -lc "sed -n '2248,2274p' chapters/theory/e1_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '960,974p' chapters/frame/preface_sections2_4_draft.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '886,910p' chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '4068,4082p' chapters/frame/heisenberg_frame.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1268,1286p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '294,308p' /Users/raeez/chiral-bar-cobar-vol2/chapters/theory/foundations_recast_draft.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1328,1346p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_core.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '452,466p' /Users/raeez/calabi-yau-quantum-groups/chapters/frame/preface.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '384,398p' /Users/raeez/calabi-yau-quantum-groups/chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '696,708p' /Users/raeez/calabi-yau-quantum-groups/chapters/theory/drinfeld_center.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,32p' /Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
On the $E_1$ side, the same decomposition applied to the ordered bar
differential $D^{E_1}_\cA$ on $T^c(s^{-1}\bar\cA)$ produces the
ordered MC element $\Theta^{E_1}_\cA \in
\operatorname{MC}(\mathfrak{g}^{\mathrm{mod},E_1}_\cA)$. The
coinvariant projection sends $\Theta^{E_1}_\cA \mapsto \Theta_\cA$:
the modular MC element is the $\Sigma_n$-averaged shadow of the
ordered one. At degree~$2$, this recovers
$\mathrm{av}(r(z)) = \kappa(\cA)$ in the abelian and scalar
families, while non-abelian affine Kac--Moody obeys
$\mathrm{av}(r(z)) + \dim(\fg)/2 = \kappa(V_k(\fg))$.

\subsection*{4.3.\enspace Universal modular twisting morphism}

Twisting morphisms classify compatible deformations of the
bar complex across all genera simultaneously. The MC space of
 succeeded in 52ms:

\item \emph{Binary component of $\Theta_\cA^{\Eone}$.}
 $r(z)$ is the degree-$2$, genus-$0$ Taylor coefficient of the
 universal MC element $\Theta_\cA^{\Eone}$ in the ordered
 convolution algebra ${\gAmod}^{\Eone}$; higher-degree components
 are the KZ associator, the quartic $R$-matrix identity, and so on
 \textup{(}Chapter~\textup{\ref{chap:e1-modular-koszul}};
 equation~\textup{\eqref{eq:intro-theta-e1}}\textup{)}. The full tower
 $(r(z), r_3, r_4, \ldots)$ is one object read at ascending degree.

\item \emph{Leading-order modular shadow.}
 The $\Sigma_2$-coinvariant projection
 $\operatorname{av}(r(z)) = \kappa(\cA)$ is the modular
 characteristic, the first entry of the shadow obstruction tower
 \textup{(}equation~\textup{\eqref{eq:intro-kappa-from-r}};
 Theorem~\textup{\ref{thm:e1-primacy}}\textup{)}. The residue contains
 a matrix-valued refinement; averaging produces the scalar.

\item \emph{Collision kernel of the bar differential.}
 The bar differential $d_{\bar{B}}$ at degree~$2$ is the residue of
 succeeded in 52ms:
This is the primitive-level refinement of
Theorem~\textup{\ref{thm:e1-coinvariant-shadow}}: the coinvariant
projection is compatible with the operadic logarithm because
$\operatorname{av}$ is a dg~Lie morphism.

\medskip
\noindent\textbf{Low-degree identifications.}
\begin{enumerate}[label=\textup{(\roman*)}]
\item $(K_\cA^{E_1})_{0,2} = r(z)$, the classical $r$-matrix
 \textup{(}genus~$0$, degree~$2$\textup{)}. The coinvariant
 $\operatorname{av}(r(z)) = \kappa(\cA)$ recovers the scalar
 curvature.
\item $(K_\cA^{E_1})_{0,3} = \Phi_{\mathrm{KZ}}(\cA)$, the
 KZ\slash Drinfeld associator \textup{(}genus~$0$, degree~$3$,
 for affine algebras;
 Construction~\textup{\ref{constr:kz-associator-e1-shadow}}).
 Coinvariant: $\operatorname{av}(\Phi_{\mathrm{KZ}}) =
 \mathfrak{C}(\cA)$, the cubic shadow.
\item $(K_\cA^{E_1})_{1,1}$ is the genus-$1$ primitive, whose
 coinvariant gives the genus-$1$ curvature $\kappa(\cA) \cdot
 succeeded in 51ms:
% label removed: thm:e1-theorem-D
\index{five main theorems!E1@$E_1$ variant!Theorem D}
\index{R-matrix!as E1 modular characteristic@as $E_1$ modular characteristic}
The classical $r$-matrix
$r(z) = \operatorname{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA^{E_1})
\in \operatorname{End}(V \otimes V)(\!(z^{-1})\!)$
satisfies the CYBE
\textup{(}Proposition~\textup{\ref{prop:ybe-from-d-squared}}).
Under averaging,
$\operatorname{av}(r(z)) = \kappa(\cA)$.
\end{theorem}

\begin{proof}
Construction~\ref{constr:r-matrix-monodromy},
Proposition~\ref{prop:r-matrix-descent},
Proposition~\ref{prop:ybe-from-d-squared}.
\end{proof}

\begin{theorem}[Theorem~$\mathrm{H}^{E_1}$; \ClaimStatusProvedHere]
 succeeded in 50ms:
\begin{theorem}[Theorem~$\mathrm{D}^{E_1}$; \ClaimStatusProvedHere]
\label{thm:e1-theorem-D}
\index{five main theorems!E1@$E_1$ variant!Theorem D}
\index{R-matrix!as E1 modular characteristic@as $E_1$ modular characteristic}
The classical $r$-matrix
$r(z) = \operatorname{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA^{E_1})
\in \operatorname{End}(V \otimes V)(\!(z^{-1})\!)$
satisfies the CYBE
\textup{(}Proposition~\textup{\ref{prop:ybe-from-d-squared}}).
Under averaging,
$\operatorname{av}(r(z)) = \kappa(\cA)$.
\end{theorem}

\begin{proof}
Construction~\ref{constr:r-matrix-monodromy},
Proposition~\ref{prop:r-matrix-descent},
Proposition~\ref{prop:ybe-from-d-squared}.
\end{proof}

 succeeded in 51ms:
spectral profile~$1/z$. For a rank-one algebra the $R$-matrix
is entirely determined by $\kappa$, so the loss is
recoverable: the spectral profile can be reconstructed from
the single scalar.
For affine $\widehat{\mathfrak{sl}}_2$ at level~$k$, the loss
is \emph{irrecoverable}: $r(z) = k\,\Omega/z$ carries the
Casimir tensor
$\Omega = \sum_a J^a \otimes J_a$ in $\fg \otimes \fg$, but
$\mathrm{av}(r(z)) = \kappa_{\mathrm{dp}}
= k\,\dim(\fg)/(2h^\vee)$ and
$\kappa = \mathrm{av}(r(z)) + \dim(\fg)/2
= \dim(\fg)\cdot(k + h^\vee)/(2h^\vee)$
is a single scalar. The Casimir tensor determines the braiding
on the category of representations; the modular
characteristic determines the genus-$1$ anomaly. These are
 succeeded in 51ms:
The bar complex $\barB(A)$ classifies \emph{twisting morphisms}
(universal couplings between $A$ and its Koszul dual~$A^!$,
Volume~I, Theorem~A), while the derived center classifies
\emph{bulk operators acting on the boundary}. These are different
objects solving different problems.

\begin{remark}[$E_1$-chiral bialgebra structure on the open colour (Vol~III)]
\label{rem:e1-chiral-bialgebra-vol3}
The open colour of the Swiss-cheese pair $(A^{\mathrm{bulk}}, A^{\mathrm{bdy}})$ carries additional Hopf-algebraic structure formalized in Vol~III (\S7 of the $E_1$-chiral algebras chapter): the $E_1$-chiral bialgebra axioms~(H1)--(H5). The coproduct $\Delta_z \colon A \to A \otimes_{E_1,z} A$ lives on the open ($E_1$/topological) colour, not the closed ($E_2$/chiral) colour. The $E_\infty$ averaging map $\mathrm{av} \colon B^{\mathrm{ord}}(A) \to B^{\Sigma}(A)$ destroys the Hopf data: $\mathrm{av}(r(z)) = \kappa_{\mathrm{ch}}$, a scalar (Vol~III, Proposition~\texttt{prop:averaging-forgets-hopf}). The braided ($E_2$) structure is recovered via the Drinfeld center $\cZ(\Rep^{E_1}(A))$, not by direct construction on the closed colour. The universal coproduct at all spins is $\Delta_z(e_s) = \sum (-1)^k \binom{N_R - b}{k} z^k \, e_a^L \cdot e_b^R$ (Vol~III, Proposition~\texttt{prop:universal-coproduct}).
\end{remark}

\subsection{The bar complex as coalgebraic projection}

The bar construction of Volume~I enters the open/closed picture as
a \emph{derived invariant} of the factorization category~$\cC$, not
 succeeded in 51ms:
\S\ref{sec:e1-chiral-bialgebras}) requires: (H1)~an $E_1$-chiral
algebra $A$ on a curve $X$; (H2)~a $z$-parametrized
$E_1$-chiral coalgebra $\Delta_z$ on the OPEN/$E_1$ colour;
(H3)~bialgebra compatibility; (H4)~spectral coassociativity;
(H5)~the Hopf axiom at $z = 0$. The associated $R$-matrix and
Yang--Baxter equation are recovered from this ordered Hopf data.
The ordered bar $B^{\mathrm{ord}}(A)$ preserves the $R$-matrix;
the symmetric bar $B^\Sigma(A)$ of Volume~I kills the Hopf
structure via averaging $\mathrm{av}(r(z)) = \kappa_{\mathrm{ch}}$.

The tetrahedron equation (the 3d analogue of YBE) fails for the
Yang $R$-matrix at $O(\kappa_{\mathrm{ch}}^2)$: the $E_3$
structure is genuinely nontrivial beyond $E_2$, confirming that
the $E_n$ operadic circle is not a formal consequence of
lower-level data.
 succeeded in 52ms:
 upgrades the ordered object to the Hopf framework used for the
 quantum-group applications.
\end{enumerate}
\end{definition}

The ordered bar $B^{\mathrm{ord}}(A)$ preserves the $R$-matrix;
the symmetric bar $B^\Sigma(A)$ of Volume~I kills the Hopf
structure via averaging
$\mathrm{av}(r(z)) = \kappa_{\mathrm{ch}}$. The $E_1$-chiral
bialgebra (not the $E_\infty$-vertex bialgebra of Li) is the
correct Hopf framework: the coproduct $\Delta_z$ lives on the
$E_1$ (ordered) side, and the $E_\infty$-averaging map destroys
the Hopf data. The associated $R$-matrix and Yang--Baxter equation
are recovered from the ordered Hopf data rather than postulated as
separate axioms. Two concrete instances are verified:
 succeeded in 50ms:

\begin{proof}
The algebraic averaging map
$\mathrm{av} \colon \fg^{\Eone}_A \to \fg^{\mathrm{mod}}_A$ is
defined as the $\Sigma_n$-coinvariant projection on the
ordered convolution algebra. At degree $2$,
$\mathrm{av}(r(z)) = \kappa_{\mathrm{ch}}$ extracts the scalar
shadow from the $r$-matrix (Volume~I, \S5).

The categorical analogue: the $\Eone$-monoidal category
$\cC = \Rep^{\Eone}(A)$ carries a tensor product that is
associative but not braided. The Drinfeld center
$\cZ(\cC)$ extracts the braided monoidal structure by
 succeeded in 50ms:
\chapter{$E_1$-Chiral Algebras}
\label{ch:e1-chiral}

Braided output is too coarse for the first questions of Vol~III. The quantum group, the Yangian, and the collision residue all live on an ordered $E_1$ layer that remembers the direction of collisions. The CY-to-chiral functor $\Phi$ reaches its braided $E_2$ image only through that primitive step, so this chapter fixes the ordered conventions used in the rest of the volume.

%: The E_1/ordered story is the PRIMITIVE layer. The E_2 braided
% structure is obtained from it by the Drinfeld center construction.
% Quantum groups, Yangians, and braided tensor categories are natively E_1.
% The passage E_1 -> E_2 is the higher-categorical analogue of the
% averaging map av: g^{E_1} -> g^mod from Vol I.

\begin{remark}[$E_1$ primacy for CY quantum groups]
\label{rem:e1-primacy-vol3}
The $E_1$-chiral algebra (boundary) is the primitive object in this volume.
The $E_2$-chiral algebra (bulk) is obtained from it by the Drinfeld center
construction $\cZ(\Rep^{E_1}(A)) \simeq \Rep^{E_2}(\mathrm{Drin}(A))$.
Quantum groups, Yangians, and braided tensor categories are natively $E_1$
objects: the CoHA multiplication is ordered (short exact sequences have a
preferred direction), and the $R$-matrix arises only in the Drinfeld double.
The passage $E_1 \to E_2$ is the higher-categorical analogue of the
exec
/bin/zsh -lc "sed -n '116,130p' /Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '196,208p' /Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\ClaimStatusProvedElsewhere
The averaging map
\[
 \mathrm{av} \colon B^{\mathrm{ord}}(A) \longrightarrow B^{\Sigma}(A),
 \qquad a_1 \otimes \dots \otimes a_n \longmapsto \tfrac{1}{n!}\sum_{\sigma \in S_n} a_{\sigma(1)} \otimes \dots \otimes a_{\sigma(n)}
\]
is a morphism of cochain complexes and sends the $E_1$ structure to the $E_\infty$ structure. It is lossy: the kernel contains the $R$-matrix data of the holomorphic factor, and on degree two $\mathrm{av}(r(z)) = \kappa_{\mathrm{ch}}$.
\end{proposition}

Volume~I establishes the map; Volume~II identifies it as the $E_1 \to E_\infty$ symmetrization. For Volume~III purposes, the two consequences that matter are: (a) Yangians and quantum groups live on the $E_1$ side and are quotiented by averaging; (b) the symmetric bar $B^\Sigma$ is sufficient for computing the modular characteristic but insufficient for reconstructing the $R$-matrix.

Averaging the degree-two generator $r(z)$ returns the scalar $\kappa_{\mathrm{ch}}$, the unique $S_2$-coinvariant of the collision residue. When the same $r(z)$ comes from the CY-to-chiral functor applied to $D^b(\Coh(K3 \times E))$, the scalar is $\kappa_{\mathrm{ch}} = 3$ by additivity: $\kappa_{\mathrm{ch}}(K3) + \kappa_{\mathrm{ch}}(E) = 2 + 1$. This differs from the categorical Euler characteristic $\kappa_{\mathrm{cat}} = 2$, the lattice-rank invariant $\kappa_{\mathrm{fiber}} = 24$, and the BKM weight $\kappa_{\mathrm{BKM}} = 5$. An unsubscripted symbol would conflate distinct invariants.

\begin{remark}[Three bars, one functor]
\label{rem:three-bars-vol3}
 succeeded in 51ms:
 & $B^{E_2}$ ($B_n$-action via $R(z)$)
 & $B^{\Sigma} = \Sym^c(s^{-1}\bar A)$ \\
Coproduct & deconcatenation & braided deconcatenation
 & coshuffle \\
Terms at degree $n$ & $n+1$ & $B_n$-orbits & $2^n$ \\
$R$-matrix data & full $r(z)$ & braiding $\sigma$ & none
 ($\mathrm{av}(r(z)) = \kappa_{\mathrm{ch}}$) \\
Koszul dual & $A^!$ (defect algebra) & $A^!$ with
 $\sigma^{\mathrm{rev}}$ & classical Koszul \\
Hopf structure & $E_1$-chiral bialgebra & braided Hopf
 (Majid) & Li vertex bialgebra \\
Coproduct type & Drinfeld $\Delta_z$ & braided
 $\Delta_\sigma$ & symmetric $\Delta$ \\
exec
/bin/zsh -lc "sed -n '1078,1092p' /Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1348,1376p' /Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1378,1390p' /Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
that sends an $E_1$-chiral Hopf algebra
$(A, \mu, \Delta_z, \varepsilon, \eta, S)$ satisfying
axioms~\textup{\textbf{(H1)--(H5)}} of
Remark~\textup{\ref{rem:e1-hopf-axiom-summary}} to the
$E_\infty$-chiral coalgebra
$(B^{\Sigma}(A), \Delta_{\mathrm{cosh}})$ with the coshuffle coproduct
$\Delta_{\mathrm{cosh}}$. The functor forgets all Hopf data:
\begin{enumerate}[label=(\roman*)]
 \item The $R$-matrix: on degree-two elements,
 $\mathrm{av}(r(z)) = \kappa_{\mathrm{ch}}$ (a scalar), so the full
 $z$-dependent $R$-matrix $r(z) = k\,\Omega/z$ is replaced by its
 $S_2$-coinvariant, which is the collision residue $\kappa_{\mathrm{ch}}$.
 \item The antipode: $S$ acts on ordered tensor factors; after
 symmetrization, $S$ becomes the identity (on $S_n$-invariants,
 the reversal acts trivially).
 succeeded in 51ms:
\textbf{Lost at transition} & --- & Ordering; strict assoc.\ & Braiding; $R$-matrix; $S$; $z$-dep. \\
\bottomrule
\end{tabular}
\caption{Twelve-row comparison of $E_n$-chiral bialgebra data.
The $E_1 \to E_2$ transition (Drinfeld center) trades the strict
associativity of linear order for a braiding; the $E_2 \to E_\infty$
transition (averaging) collapses $r(z)$ to $\kappa_{\mathrm{ch}}$
and destroys the Hopf structure entirely.
See Construction~\ref{constr:three-bar-complexes} for the
bar-complex triple.}
\label{tab:en-chiral-comparison}
\end{table}

 succeeded in 51ms:
$E_2 \to E_\infty$ is the averaging map
$\mathrm{av} \colon B^{\mathrm{ord}} \to B^{\Sigma}$
(Proposition~\ref{prop:averaging-e1-einfty}).
Each arrow \emph{loses} structure irreversibly: the first quotients out
the ordering to gain a braiding; the second quotients out the braiding
to gain full symmetry. The slogan:
$E_\infty$-averaging kills the Hopf structure because
$\mathrm{av}(r(z)) = \kappa_{\mathrm{ch}}$: the full
$z$-dependent $R$-matrix collapses to a single scalar.

\begin{table}[ht]
\centering
\small
\renewcommand{\arraystretch}{1.25}
\begin{tabular}{@{}l@{\;\;}l@{\;\;}l@{\;\;}l@{}}
\toprule
\textbf{Feature} & \textbf{$E_1$ (ordered)} & \textbf{$E_2$ (braided)} & \textbf{$E_\infty$ (symmetric)} \\
\midrule
Operad & Little intervals & Little $2$-disks & Comm.\ operad \\
Symmetry at degree $n$ & Trivial ($1$) & Braid group $B_n$ & $S_n$ \\

thinking
**Inspecting repo files**

I'm considering using more targeted grep without context since there are many duplicates. I want to focus on updating only the current repo and potentially include external ones. To do this thoroughly, I need to check all possibly problematic files from the search results. I'll inspect specific lines in various standalone LaTeX files and chapters to determine their relevance and correctness. There's quite a bit to dive into, but I'm eager to ensure everything aligns.
codex
The generic theorem/introduction statements in Vol I are definitely in scope. I’m now sweeping the remaining Vol I standalones that still advertise `av(r)=\kappa` generically, so the local fix doesn’t leave the old claim alive in mirrored summaries.
exec
/bin/zsh -lc "sed -n '700,792p' standalone/N3_e1_primacy.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2644,2662p' standalone/en_chiral_operadic_circle.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1324,1338p' standalone/chiral_chern_weil.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1208,1224p' standalone/chiral_chern_weil.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\midrule
Connection $\nabla$ & MC element $\Theta^{\Eone}_\cA$ \\
Curvature $F_\nabla \in \Omega^2(M;\fg)$
 & $r(z) \in \gEone$; $\dfib^{\,2} = \kappa\cdot\omega_g$ \\
Inv.\@ polynomial $P \in \Sym^k(\fg^*)^G$
 & Averaging map $\av\colon\gEone\to\gmod$ \\
$\CW(P) = P(F^k)$
 & $\av(r(z)) = \kappa_{\mathrm{cl}}$ \\
Bianchi $d_\nabla F = 0$
 & MC: $d\Theta + \frac{1}{2}[\Theta,\Theta] = 0$ \\
Char.\@ class $[P(F^k)] \in H^{2k}(M)$
 & $\obs_g = \kappa\cdot\lambda_g \in H^*(\Mbar_g)$ \\
Independence of connection
 & $\kappa$ is a qi-invariant \\
$H^*(BG) = \Sym^*(\fg^*)^G$
 succeeded in 51ms:
\end{center}


% ================================================================
% Section 5: The chiral curvature
% ================================================================
\section{The chiral curvature}\label{sec:chiral-cw}

The averaging map extracts~$\kappa$ from the $r$-matrix.
The question it forces is: what role does~$\kappa$ play
geometrically? The answer: $\kappa$ is the proportionality
constant of a curvature. The bar differential, which squares
to zero on~$\mathbb{P}^1$, fails to square to zero on
higher-genus curves; the failure is proportional to~$\kappa$.
This section derives that formula from the propagator on a
genus-$g$ curve.

 succeeded in 51ms:
\label{rem:theorem-d-cleanest}
Among the five, Theorem D makes the $E_{1}$ primacy thesis most
concrete. The scalar modular characteristic $\kappa$ is a single
number per family, and the family formulas are distinct: for
$W_{N}$ the harmonic number is $H_{N} = \sum_{j=1}^{N} 1/j$ and
must not be copied from a different family. Its degree-$2$ lift is a meromorphic function of a single
variable, the collision coordinate $z$. The statement
$\av(r(z)) = \kappa$ says this exactly for Heisenberg, while for
non-abelian affine Kac--Moody the same averaging recovers only
$\kappa_{\mathrm{dp}}$ and the full $\kappa$ adds the Sugawara
shift $\dim(\fg)/2$. The scalar shadow is still the
$\Sigma_{2}$-average of a function. This is a strict projection;
the full function
$r(z)$ carries information about the braiding, the quantum group,
and the line-operator algebra that no scalar invariant can see.
The universality property of $\kappa$ in Volume I Theorem D
lifts (with the same proof, interpreted one level higher) to a
universality property of $r(z)$ on the ordered side.
\end{remark}

 succeeded in 51ms:
$\ChirHoch^1(V_k(\fg)) \cong \fg$ as a vector space, with
total dimension $\dim(\fg) + 2$.
\end{proof}

\begin{remark}[The Sugawara shift]
\label{rem:e-sugawara-shift}
For the Heisenberg (abelian), $\mathrm{av}(r(z)) = \kappa$
holds directly. For non-abelian Kac--Moody, the full
$\kappa$ includes the Sugawara shift:
$\kappa = \mathrm{av}(r(z)) + \dim(\fg)/2$. The term
$\dim(\fg)/2$ arises from the simple-pole self-contraction
through the adjoint Casimir eigenvalue $2h^\vee$. This is a
fundamental difference between abelian and non-abelian
averaging, and is the reason $\kappa(V_k(\fg)) \neq 0$ at
$k = 0$ (the non-abelian Lie bracket persists).
\end{remark}

\subsection{Virasoro $\mathrm{Vir}_c$: class M}

exec
/bin/zsh -lc "sed -n '2004,2018p' standalone/shadow_towers_v3.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '378,394p' standalone/holographic_datum.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '836,852p' standalone/cy_to_chiral_functor.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '884,972p' standalone/N3_e1_primacy.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1840,1882p' standalone/shadow_towers_v3.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
correspond to channels $(12|34)$, $(13|24)$, $(14|23)$, and evaluating
the Arnold relation on
$\Omega \otimes \Omega \in (\cA^!)^{\otimes 3}$ produces the
three terms of $\sum [r_{ij}, r_{ik}] = 0$.

The $r$-matrix lives in the $\Eone$ convolution algebra
$\mathfrak{g}^{\Eone}_{\cA}$; the modular characteristic
$\kappa(\cA)$ is its $\Sigma_2$-coinvariant projection. For abelian
algebras, $\av(r(z)) = \kappa$ directly. For non-abelian affine
Kac--Moody algebras, the full modular characteristic includes the
Sugawara shift:
\begin{equation}\label{eq:av-sugawara}
\kappa(V_k(\fg))
\;=\;
\av(r(z)) + \frac{\dim(\fg)}{2}
\;=\;
\frac{\dim(\fg)(k + h^\vee)}{2h^\vee},
 succeeded in 52ms:
\item \emph{Compatibility with MC.}\enspace
 $\mathrm{av}$ is a morphism of dg Lie algebras:
 $\mathrm{av}([\xi,\eta]^{E_1})
 = [\mathrm{av}(\xi), \mathrm{av}(\eta)]^{\mathrm{mod}}$.
 The MC element projects:
 $\mathrm{av}(\Theta_\cA^{E_1}) = \Theta_\cA$.

\item \emph{Degree-$2$ content.}\enspace
 At degree~$2$: $\mathrm{av}(r(z)) = \kappa$ for abelian
 algebras; $\mathrm{av}(r(z)) + \dim(\fg)/2 = \kappa$ for
 non-abelian KM (Sugawara shift).
\end{enumerate}
\end{proposition}

\begin{remark}[What the shadow tower
 succeeded in 52ms:
 \item The CoHA = the positive half of $G(X)$ = the $\Eone$-chiral
 sector (the ordered part).
 \item The full quantum vertex chiral group $G(X)$ is $\Etwo$
 (braided).
 \item The braiding (the passage from $\Eone$ to $\Etwo$) is
 the quantum group $R$-matrix of the affine super Yangian.
 \item The ordered bar $B^{\mathrm{ord}}(A_\cC)$ preserves the
 $R$-matrix; the symmetric bar $B^\Sigma(A_\cC)$ kills the Hopf
 structure via averaging: in abelian and scalar families
 $\mathrm{av}(r(z)) = \kappa_{\mathrm{ch}}$, while for
 non-abelian affine Kac--Moody
 $\mathrm{av}(r(z))+\dim(\fg)/2 = \kappa_{\mathrm{ch}}$.
\end{itemize}

\begin{remark}[Shadow = $\GW(\bC^3)$]
\label{rem:v3-st-shadow-gw}
At $\kappa_{\mathrm{ch}} = \Psi$ (the deformation parameter of
 succeeded in 52ms:
\end{proposition}

\begin{proof}
The ordered bar $B^{\mathrm{ord}}(\cA) =
T^c(s^{-1}\bar{\cA})$ carries the $E_1$ convolution algebra
$\mathfrak{g}^{E_1}_\cA$, whose MC element
$\Theta_\cA^{E_1}$ projects to~$\Theta_\cA$ under
$\mathrm{av}$. The degree-$2$ component of
$\Theta_\cA^{E_1}$ is the $R$-matrix $r(z)$, and its
average is the modular characteristic~$\kappa$, with the
Sugawara correction for non-abelian algebras arising from
the simple-pole self-contraction of the ordered two-point
function. The higher degrees follow by the same averaging
applied to the degree-$r$ MC components.
\end{proof}

\begin{remark}[What averaging
discards]\label{rem:averaging-lossy}
The averaging map $\mathrm{av}$ is lossy: it discards the
spectral parameter~$z$, the $R$-matrix structure, and the
 succeeded in 52ms:
duality, and that the symmetric bar $\BarSig(\cA)$ is its
$\Sigma_{n}$-coinvariant shadow under an averaging map $\av$ of
dg Lie algebras. The five foundational theorems A, B, C, D, H of
modular Koszul duality admit ordered $E_{1}$ counterparts whose
symmetric images are the classical theorems. Theorem D is the
cleanest example: the scalar degree-$2$ shadow is recovered from
the spectral $r$-matrix $r(z)$ by averaging, giving $\kappa$
for abelian families and $\kappa_{\mathrm{dp}}$ for non-abelian
affine Kac--Moody before the Sugawara shift $\dim(\fg)/2$ is
added; the passage from $r(z)$ to the scalar shadow is a strict
projection with
nontrivial kernel.

Several problems remain open.

\subsection*{The full $E_{1}$ Koszul duality theorem}

An unconditional $E_{1}$ Koszul duality theorem, asserting that
the bar and cobar functors exchange the categories of
$E_{1}$-chiral algebras and cocomplete $F\Ass$-coalgebras on the


thinking
**Reassessing statement clarity**

I think many parts seem correct, but I’m considering whether to mention that the generic line extracts kappa from the r-matrix. The scope only addresses instances where av(r)=kappa is stated for non-abelian KM without shift. Should I clarify that or patch it to include scalar shadow and Sugawara? Since the scope is narrow, if the generic statement might mislead, I should probably fix it for accuracy.
thinking
**Identifying necessary patches**

I might need to add details about abelian and non-abelian cases with shifts in some generic statements. I should identify all similar phrases in the current repository and patch them to avoid confusion. For instance, in `chapters/examples/y_algebras.tex`, I noticed it might not relate to the user’s focus, so no action there. I’ll need to update several other files like `e1_modular_koszul.tex`, `introduction.tex`, and `survey_track_a_compressed.tex`. However, some sections are correct as they are, like in `preface_sections2_4_draft.tex`.
codex
I’ve narrowed Vol I to a small set of genuinely generic statements. I’m doing one more exact pass for `av(r)=\kappa` in the writable tree so I can patch the remaining generic formulations in one shot rather than leave stragglers behind.
exec
/bin/zsh -lc "rg -n -C 2 '\\\\(?:av|mathrm\\{av\\}|operatorname\\{av\\})\\s*\\(r(?:_0)?\\(z\\)\\)\\s*=\\s*\\\\kappa(?:\\(["'^)]*'"\\))?(?"'!_)'"' chapters standalone" in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
rg: regex parse error:
    (?:\\(?:av|mathrm\{av\}|operatorname\{av\})\s*\(r(?:_0)?\(z\)\)\s*=\s*\\kappa(?:\([^)]*\))?(?!_))
                                                                                               ^^^
error: look-around, including look-ahead and look-behind, is not supported

Consider enabling PCRE2 with the --pcre2 flag, which can handle backreferences
and look-around.
exec
/bin/zsh -lc "rg --pcre2 -n -C 2 '\\\\(?:av|mathrm\\{av\\}|operatorname\\{av\\})\\s*\\(r(?:_0)?\\(z\\)\\)\\s*=\\s*\\\\kappa(?:\\(["'^)]*'"\\))?(?"'!_)'"' chapters standalone" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
standalone/e1_primacy_ordered_bar.tex-1199-package of~$\cA$. It is universal, additive, antisymmetric under
standalone/e1_primacy_ordered_bar.tex-1200-opposite-duality, and satisfies
standalone/e1_primacy_ordered_bar.tex:1201:$\av(r_0(z)) = \kappa(\cA)$ on abelian families, while for
standalone/e1_primacy_ordered_bar.tex-1202-non-abelian affine Kac--Moody
standalone/e1_primacy_ordered_bar.tex-1203-$\av(r_0(z)) = \kappa_{\mathrm{dp}}(\cA)$ and
--
standalone/e1_primacy_ordered_bar.tex-1233-copied from a different family. Its degree-$2$ lift is a meromorphic
standalone/e1_primacy_ordered_bar.tex-1234-function of a single variable, the collision coordinate~$z$. The
standalone/e1_primacy_ordered_bar.tex:1235:statement $\av(r(z)) = \kappa$ says this exactly for Heisenberg,
standalone/e1_primacy_ordered_bar.tex-1236-while for non-abelian affine Kac--Moody the same averaging recovers
standalone/e1_primacy_ordered_bar.tex-1237-only $\kappa_{\mathrm{dp}}$ and the full $\kappa$ adds the Sugawara
--
standalone/e1_primacy_ordered_bar.tex-1648-\begin{itemize}
standalone/e1_primacy_ordered_bar.tex-1649-\item $r(z) = k/z$ (equation~\eqref{eq:heis-r-matrix}).
standalone/e1_primacy_ordered_bar.tex:1650:\item $\av(r(z)) = \kappa(\cH_k) = k$
standalone/e1_primacy_ordered_bar.tex-1651-  (the $\Sigma_2$-average of $k/z$ against $d\log(z)$ extracts
standalone/e1_primacy_ordered_bar.tex-1652-  the residue $k$, which is the full modular characteristic).
--
standalone/holographic_datum.tex-384-$\mathfrak{g}^{\Eone}_{\cA}$; the modular characteristic
standalone/holographic_datum.tex-385-$\kappa(\cA)$ is its $\Sigma_2$-coinvariant projection. For abelian



thinking
**Patching generic chapters**

I need to patch the current repo for generic chapters like e1_modular_koszul and the introduction. There's a chance I should also look at survey_track_a_compressed since it isn't captured by the regex for eq labeling. I’ll need to inspect the context for chiral_chern_weil, especially regarding whether κ_cl is a generic scalar shadow that should reflect a shift. I might also need to address the introduction sentence about the averaging map needing qualification. Overall, I’ll ensure everything is accurately patched.
thinking
**Updating generic references**

I might need to consider shadow_towers_v3, though it seems to already have corrections. For line 1849, it states that the average is a modular characteristicκ with the Sugawara correction for non-abelian algebras, which is good. Line 1876 mentions averaging producing κ generically, yet I should probably clarify it to say it produces the scalar shadow κ in abelian cases and κ_dp in non-abelian affine KM. I’ll also check external volumes for any generic contexts that might need patching and search volumes two and three more thoroughly for all such references.
thinking
**Checking permissions for patching**

I think permissions might block my actions, so I need to verify the write scope. It's possible I could use apply_patch with an absolute path outside the root, but I’m unsure if the tool will allow for that. Since the user is looking for a final outcome, I need to tread carefully and ensure everything is in order before proceeding. I'll double-check the permissions to avoid any hiccups down the line.
codex
I’ve reduced the writable Vol I work to a handful of exact lines. Before I patch those, I’m checking whether `apply_patch` can reach the sibling volume directories at all; if it cannot, I’ll still finish the in-repo fixes and then mark the external volume hits as blocked by sandbox write scope.
codex
I can read Vol II and Vol III, but `apply_patch` is blocked outside `/Users/raeez/chiral-bar-cobar`, so external edits are not possible in this sandbox. I’m patching every in-repo live advertisement now and will report the remaining sibling-volume hits as `BLOCKED` with exact file paths.

```text
PE-2
family: affine KM / generic mixed-family prose
kappa written: av(r(z)) = kappa only on abelian/scalar lanes; non-abelian affine KM uses av(r(z)) = kappa_dp and kappa = kappa_dp + dim(g)/2
census: landscape_census.tex canonical affine KM formula = dim(g)(k+h^v)/(2h^v)  match? Y
at k=0: dim(g)/2 expected dim(g)/2  at k=-h^v: 0 expected 0
at c=13 (Vir): 13/2 expected 13/2
wrong variants avoided: NOT av(r)=kappa for non-abelian KM
verdict: ACCEPT

PE-8
formula: averaging of degree-2 r-matrix to scalar modular characteristic
Vol I: generic and family-specific hits present  Vol II: generic hits present  Vol III: generic hits present
consistent? N  if not: canonical vol I, others updated same session? Vol I yes; sibling volumes blocked by sandbox write scope
convention conversion: OPE-mode only here; sibling references checked in local context  applied? Y
verdict: ACCEPT
```

thinking
**Exploring table formats**

I'm trying to figure out whether to use `\parbox` or `\shortstack[l]{...}` in my environment. I'm not sure if the package I'm using is loaded, so maybe it would be better to shift to `\shortstack`. I should probably check how the table is structured, perhaps it's using standard tabular with p-columns. It seems like I need to gather more context around the table to make a confident decision.
exec
/bin/zsh -lc "sed -n '1318,1338p' standalone/chiral_chern_weil.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\label{rem:comparison}
\begin{center}
\renewcommand{\arraystretch}{1.3}
\begin{tabular}{@{}p{4.2cm}p{5.5cm}@{}}
\toprule
\textbf{Classical} & \textbf{Chiral} \\
\midrule
Connection $\nabla$ & MC element $\Theta^{\Eone}_\cA$ \\
Curvature $F_\nabla \in \Omega^2(M;\fg)$
 & $r(z) \in \gEone$; $\dfib^{\,2} = \kappa\cdot\omega_g$ \\
Inv.\@ polynomial $P \in \Sym^k(\fg^*)^G$
 & Averaging map $\av\colon\gEone\to\gmod$ \\
$\CW(P) = P(F^k)$
 & $\av(r(z)) = \kappa_{\mathrm{cl}}$ \\
Bianchi $d_\nabla F = 0$
 & MC: $d\Theta + \frac{1}{2}[\Theta,\Theta] = 0$ \\
Char.\@ class $[P(F^k)] \in H^{2k}(M)$
 & $\obs_g = \kappa\cdot\lambda_g \in H^*(\Mbar_g)$ \\
Independence of connection
 & $\kappa$ is a qi-invariant \\
exec
/bin/zsh -lc "sed -n '360,378p' standalone/survey_track_a_compressed.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
r(z)\;=\;\operatorname{Res}^{\mathrm{coll}}_{0,2}\bigl(\Theta^{E_1}_{\cA}\bigr),
\]
a matrix-valued rational function encoding the full binary OPE data.
Applying $\mathrm{av}$ at degree~$2$ collapses the profile to a single
scalar,
\begin{equation}\label{eq:av-organizing}
\mathrm{av}\bigl(r(z)\bigr)\;=\;\kappa(\cA),
\end{equation}
the modular characteristic of Theorem~D. At degree~$3$ the KZ
associator projects to the cubic shadow~$\mathfrak C$; at degree~$4$
the Yangian higher coproduct projects to the quartic resonance
class~$\mathfrak Q$. Each degree-$n$ component of the ordered
Maurer--Cartan element projects under $\mathrm{av}$ to the degree-$n$
shadow of the modular obstruction tower $\Theta_{\cA}$.

\medskip
\noindent\textbf{The five theorems as averaged invariants.}\enspace
The main theorems A--D and H are the invariants of the ordered
Maurer--Cartan element $\Theta^{E_1}_{\cA}$ that survive averaging.
exec
/bin/zsh -lc "sed -n '1868,1882p' standalone/shadow_towers_v3.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\end{remark}

\subsection{The $R$-matrix tower for each
class}\label{subsec:r-matrix-tower}

The $E_1$ convolution algebra
$\mathfrak{g}^{E_1}_\cA$ carries a spectral $R$-matrix
$r(z) \in \mathrm{End}(V \otimes V)((z))$ at degree~$2$,
whose averaging produces~$\kappa$. The structure of $r(z)$
varies by class.

\begin{example}[Class $\mathbf{G}$:
Heisenberg]\label{ex:r-heis}
$r^{\mathrm{Heis}}(z) = k/z$. One pole of order~$1$ (from
the double-pole OPE $J(z)J(w) \sim k/(z-w)^2$ after

thinking
**Searching for notation**

I need to find the correct figure notation. I'll search within the file for "kappa_cl" to see if it’s defined there. Maybe I’ll need to inspect around a bit too. It seems like the current notation I should consider is `\kappa_{\mathrm{cl}}`, which appears to refer to the "classical modular characteristic." Let's get going and see what I can find!
exec
/bin/zsh -lc "rg -n '\\\\kappa_\\{\\\\mathrm\\{cl\\}\\}|kappa_\\{\\\\mathrm\\{cl\\}\\}|kappa_cl|\\\\kappa_\\{\\\\mathrm\\{dp\\}\\}' standalone/chiral_chern_weil.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
776:$\kappa_{\mathrm{dp}} = 3k/(2h^\vee) = 3k/4$.
820:= \kappa_{\mathrm{dp}} + \kappa_{\mathrm{sp}}
849:\kappa_{\mathrm{dp}} = \frac{8k}{2h^\vee} = \frac{8k}{6}
958:\kappa_{\mathrm{cl}}(\cA) = \av(r(z))
971:$\kappa(\cA)=\kappa_{\mathrm{cl}}(\cA)$. For non-abelian affine
973:$\kappa(\cA)=\kappa_{\mathrm{cl}}(\cA)+\dim(\fg)/2$.
1122: \kappa_{\mathrm{dp}}\text{ (tree-level, from $r(z)$)}}
1331: & $\av(r(z)) = \kappa_{\mathrm{cl}}$ \\
exec
/bin/zsh -lc "sed -n '952,976p' standalone/chiral_chern_weil.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\label{subsec:kappa-general}

\begin{proposition}\label{prop:kappa-formula}
At degree~$2$, the averaging map extracts the classical scalar
shadow of the ordered residue:
\begin{equation}\label{eq:kappa-from-r}
\kappa_{\mathrm{cl}}(\cA) = \av(r(z))
= \tfrac{1}{2}\,\tr_{\mathrm{cyc}}
 \bigl[\Res_{z=0}\,r(z)\bigr],
\end{equation}
where the cyclic trace incorporates the weight-dependent
moment~\eqref{eq:cyclic-trace-moment}.
For a single generator~$\varphi_i$ of weight~$h_i$, the
per-channel contribution is
\begin{equation}\label{eq:kappa-per-channel}
\kappa_i = \Res_{z=0}\bigl[z^{2h_i - 2}\cdot
 r_{ii}^{\mathrm{vac}}(z)\bigr].
\end{equation}
For abelian and Virasoro-type families,
$\kappa(\cA)=\kappa_{\mathrm{cl}}(\cA)$. For non-abelian affine

thinking
**Deciding on patching approach**

I’m considering whether to patch or ignore a potential issue. It seems that if we leave it, it could mislead future audits. The user has mentioned only fixing instances rather than rewriting entire files. I could patch the backup, but I'm unsure if the user wants backups altered. The objective is to close the gap and check for AP violations. I think it’s necessary to patch the backup to avoid showing old formulas later. I'll need to inspect the context around line 3007 in the backup.
exec
/bin/zsh -lc "sed -n '3000,3012p' chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
is entirely determined by $\kappa$, so the loss is
recoverable: the spectral profile can be reconstructed from
the single scalar.
For affine $\widehat{\mathfrak{sl}}_2$ at level~$k$, the loss
is \emph{irrecoverable}: $r(z) = k\,\Omega/z$ carries the
Casimir tensor
$\Omega = \sum_a J^a \otimes J_a$ in $\fg \otimes \fg$, but
$\mathrm{av}(r(z)) = \kappa = \dim(\fg)\cdot(k + h^\vee)/(2h^\vee)$
is a single scalar.  The Casimir tensor determines the braiding
on the category of representations; the modular
characteristic determines the genus-$1$ anomaly.  These are
different structural data at different categorical depths.


thinking
**Investigating label details**

I think I need to take a closer look at the actual label, especially around line 551. It seems like there might be some important details there that could help clarify things. I'll do a search to zero in on that specific line and see what I can find. This way, I can make sure I fully understand whatever the label entails. Alright, let's go ahead and inspect that further!
exec
/bin/zsh -lc "rg -n 'eq:intro-kappa-from-r|eq:av-organizing' chapters/theory/introduction.tex standalone/survey_track_a_compressed.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
standalone/survey_track_a_compressed.tex:365:\begin{equation}\label{eq:av-organizing}
standalone/survey_track_a_compressed.tex:415:$k/(z-w)^2$ drops by one order under the $d\log$ kernel. Applying \eqref{eq:av-organizing},
chapters/theory/introduction.tex:900: \textup{(}equation~\textup{\eqref{eq:intro-kappa-from-r}};
chapters/theory/introduction.tex:1268:\begin{equation}\label{eq:intro-kappa-from-r}
chapters/theory/introduction.tex:1278:\eqref{eq:intro-kappa-from-r} specializes to the Sugawara identity
chapters/theory/introduction.tex:1616: \eqref{eq:intro-kappa-from-r}: the pole orders are one less than
exec
/bin/zsh -lc "sed -n '1264,1284p' chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\end{equation}
At degree~$2$, this projection records only one number: the
$\Sigma_2$-coinvariant of the residue of $r(z)$ at $z = 0$ is the
modular characteristic
\begin{equation}\label{eq:intro-kappa-from-r}
\kappa(\cA)
\;=\;
\operatorname{av}\bigl(r(z)\bigr)
\;=\;
\tfrac{1}{2}\,\operatorname{tr}\!\bigl[\Res_{z = 0} r(z)\bigr],
\end{equation}
where the trace is the cyclic trace on $\End(V^{\otimes 2})$.
For the affine Kac--Moody vacuum algebra $V_k(\mathfrak{g})$ at
non-critical level, the averaging formula
\eqref{eq:intro-kappa-from-r} specializes to the Sugawara identity
\begin{equation}\label{eq:intro-sugawara-kappa}
\operatorname{av}\bigl(r_k(z)\bigr) + \tfrac{1}{2}\dim\mathfrak{g}
\;=\;
\kappa\bigl(V_k(\mathfrak{g})\bigr)
\;=\;

thinking
**Updating equations and references**

I’ve noticed a potential error in the introduction equation related to kappa from r; it seems like I might need to clarify the distinction between abelian and non-abelian groups. I should also look into updating line 898 to reference that corrected equation. Additionally, I think it’s worth searching in the e1_modular_koszul section for any similar equations. Checking around the `av(r(z))` term in the file could provide more context for these updates.
exec
/bin/zsh -lc "rg -n 'av\\(r\\(z\\)\\)|kappa-from-r|Sugawara' chapters/theory/e1_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
942:$\Sigma_2$-coinvariant $\av(r(z))$).
1781:Sugawara-normalised coefficient $(k{+}h^\vee)^{-1}\Omega\, z^{-1}$ in the
1785:by the separate Koszul-pairing and Sugawara normalizations, which
exec
/bin/zsh -lc "sed -n '1608,1622p' chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
 $r(z) = \tau$, the Koszul-signed flip on $V \otimes V$, with no
 meromorphic dependence on~$z$. No collision forces scattering: the
 $R$-matrix is the identity up to sign, and the associated Yangian
 is the symmetric algebra on a finite-dimensional vector space.

\item \emph{Local OPE tier.}
 $r(z)$ has poles at $z = 0$, and its entire structure is determined
 by the local OPE of $\cA$ by the residue formula
 \eqref{eq:intro-kappa-from-r}: the pole orders are one less than
 the OPE pole orders, and the matrix
 coefficients are the OPE modes $a_{(n)}b$. The tier
 is closed under Drinfeld--Sokolov reduction and under free-field
 realizations.

\item \emph{Genuinely $\Eone$ tier.}
codex
I’ve isolated the exact writable lines. The edits are surgical: only the generic `av(r)=\kappa` claims are being qualified, plus the stale backup hit in `chapters/` so the grep surface is clean.
codex
The first patch batch failed on a mismatched context in the backup file. I’m reapplying in smaller hunks so each target is verified against the live text before edit.
file update
M /Users/raeez/chiral-bar-cobar/standalone/survey_track_a_compressed.tex
@@ -363,7 +363,13 @@
 Applying $\mathrm{av}$ at degree~$2$ collapses the profile to a single
-scalar,
+scalar shadow:
 \begin{equation}\label{eq:av-organizing}
-\mathrm{av}\bigl(r(z)\bigr)\;=\;\kappa(\cA),
+\begin{aligned}
+\mathrm{av}\bigl(r(z)\bigr) &= \kappa(\cA)
+&& \text{for abelian and scalar families},\\
+\mathrm{av}\bigl(r(z)\bigr) &= \kappa_{\mathrm{dp}}(\cA), \qquad
+\kappa(\cA) = \kappa_{\mathrm{dp}}(\cA) + \dim(\fg)/2
+&& \text{for non-abelian affine Kac--Moody.}
+\end{aligned}
 \end{equation}
-the modular characteristic of Theorem~D. At degree~$3$ the KZ
+This is the modular characteristic package of Theorem~D. At degree~$3$ the KZ
 associator projects to the cubic shadow~$\mathfrak C$; at degree~$4$
M /Users/raeez/chiral-bar-cobar/chapters/theory/introduction.tex
@@ -897,4 +897,8 @@
  The $\Sigma_2$-coinvariant projection
- $\operatorname{av}(r(z)) = \kappa(\cA)$ is the modular
- characteristic, the first entry of the shadow obstruction tower
+ $\operatorname{av}(r(z))$ is the leading scalar shadow: it equals
+ $\kappa(\cA)$ on abelian and scalar families, while for
+ non-abelian affine Kac--Moody it gives
+ $\kappa_{\mathrm{dp}}(\cA)$ and the full modular characteristic is
+ $\kappa(\cA) = \kappa_{\mathrm{dp}}(\cA) + \dim(\fg)/2$. This is
+ the first entry of the shadow obstruction tower
  \textup{(}equation~\textup{\eqref{eq:intro-kappa-from-r}};
@@ -1264,8 +1268,5 @@
 \end{equation}
-At degree~$2$, this projection records only one number: the
-$\Sigma_2$-coinvariant of the residue of $r(z)$ at $z = 0$ is the
-modular characteristic
+At degree~$2$, this projection records only one scalar: the
+$\Sigma_2$-coinvariant of the residue of $r(z)$ at $z = 0$ is
 \begin{equation}\label{eq:intro-kappa-from-r}
-\kappa(\cA)
-\;=\;
 \operatorname{av}\bigl(r(z)\bigr)
@@ -1275,2 +1276,6 @@
 where the trace is the cyclic trace on $\End(V^{\otimes 2})$.
+For abelian and scalar families,
+\[
+\kappa(\cA) = \operatorname{av}\bigl(r(z)\bigr).
+\]
 For the affine Kac--Moody vacuum algebra $V_k(\mathfrak{g})$ at
M /Users/raeez/chiral-bar-cobar/chapters/theory/e1_modular_koszul.tex
@@ -2257,4 +2257,7 @@
  \textup{(}genus~$0$, degree~$2$\textup{)}. The coinvariant
- $\operatorname{av}(r(z)) = \kappa(\cA)$ recovers the scalar
- curvature.
+ $\operatorname{av}(r(z))$ recovers the scalar degree-$2$ shadow:
+ on abelian families $\operatorname{av}(r(z)) = \kappa(\cA)$,
+ while for non-abelian affine Kac--Moody
+ $\operatorname{av}(r(z)) = \kappa_{\mathrm{dp}}(\cA)$ and
+ $\kappa(\cA) = \kappa_{\mathrm{dp}}(\cA) + \dim(\fg)/2$.
 \item $(K_\cA^{E_1})_{0,3} = \Phi_{\mathrm{KZ}}(\cA)$, the
apply_patch(auto_approved=true) exited 0 in 38ms:
Success. Updated the following files:
M chapters/theory/e1_modular_koszul.tex
M chapters/theory/introduction.tex
M standalone/survey_track_a_compressed.tex
file update:
diff --git a/chapters/theory/e1_modular_koszul.tex b/chapters/theory/e1_modular_koszul.tex
index a8a83c93d1d8dc248f8f9f6309990c5a7602c6c4..041dea657991f4089b4f0404b429bf3fff9ad079
--- a/chapters/theory/e1_modular_koszul.tex
+++ b/chapters/theory/e1_modular_koszul.tex
@@ -2255,8 +2255,11 @@
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item $(K_\cA^{E_1})_{0,2} = r(z)$, the classical $r$-matrix
  \textup{(}genus~$0$, degree~$2$\textup{)}. The coinvariant
- $\operatorname{av}(r(z)) = \kappa(\cA)$ recovers the scalar
- curvature.
+ $\operatorname{av}(r(z))$ recovers the scalar degree-$2$ shadow:
+ on abelian families $\operatorname{av}(r(z)) = \kappa(\cA)$,
+ while for non-abelian affine Kac--Moody
+ $\operatorname{av}(r(z)) = \kappa_{\mathrm{dp}}(\cA)$ and
+ $\kappa(\cA) = \kappa_{\mathrm{dp}}(\cA) + \dim(\fg)/2$.
 \item $(K_\cA^{E_1})_{0,3} = \Phi_{\mathrm{KZ}}(\cA)$, the
  KZ\slash Drinfeld associator \textup{(}genus~$0$, degree~$3$,
  for affine algebras;
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 789ce9acf5b68f150a665afd1b7486e6b1256a16..f5fd9aa34b7bb56449ed56b583ce3f595c37ce5f
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -895,8 +895,12 @@
 
 \item \emph{Leading-order modular shadow.}
  The $\Sigma_2$-coinvariant projection
- $\operatorname{av}(r(z)) = \kappa(\cA)$ is the modular
- characteristic, the first entry of the shadow obstruction tower
+ $\operatorname{av}(r(z))$ is the leading scalar shadow: it equals
+ $\kappa(\cA)$ on abelian and scalar families, while for
+ non-abelian affine Kac--Moody it gives
+ $\kappa_{\mathrm{dp}}(\cA)$ and the full modular characteristic is
+ $\kappa(\cA) = \kappa_{\mathrm{dp}}(\cA) + \dim(\fg)/2$. This is
+ the first entry of the shadow obstruction tower
  \textup{(}equation~\textup{\eqref{eq:intro-kappa-from-r}};
  Theorem~\textup{\ref{thm:e1-primacy}}\textup{)}. The residue contains
  a matrix-valued refinement; averaging produces the scalar.
@@ -1262,17 +1266,18 @@
 \;=\;
 \Theta_\cA.
 \end{equation}
-At degree~$2$, this projection records only one number: the
-$\Sigma_2$-coinvariant of the residue of $r(z)$ at $z = 0$ is the
-modular characteristic
+At degree~$2$, this projection records only one scalar: the
+$\Sigma_2$-coinvariant of the residue of $r(z)$ at $z = 0$ is
 \begin{equation}\label{eq:intro-kappa-from-r}
-\kappa(\cA)
-\;=\;
 \operatorname{av}\bigl(r(z)\bigr)
 \;=\;
 \tfrac{1}{2}\,\operatorname{tr}\!\bigl[\Res_{z = 0} r(z)\bigr],
 \end{equation}
 where the trace is the cyclic trace on $\End(V^{\otimes 2})$.
+For abelian and scalar families,
+\[
+\kappa(\cA) = \operatorname{av}\bigl(r(z)\bigr).
+\]
 For the affine Kac--Moody vacuum algebra $V_k(\mathfrak{g})$ at
 non-critical level, the averaging formula
 \eqref{eq:intro-kappa-from-r} specializes to the Sugawara identity
diff --git a/standalone/survey_track_a_compressed.tex b/standalone/survey_track_a_compressed.tex
index cb62bb8b88937153678a962d34c4c5dac04b9700..084c11fb005499137646a882cff6cb86a1becc01
--- a/standalone/survey_track_a_compressed.tex
+++ b/standalone/survey_track_a_compressed.tex
@@ -361,11 +361,17 @@
 \]
 a matrix-valued rational function encoding the full binary OPE data.
 Applying $\mathrm{av}$ at degree~$2$ collapses the profile to a single
-scalar,
+scalar shadow:
 \begin{equation}\label{eq:av-organizing}
-\mathrm{av}\bigl(r(z)\bigr)\;=\;\kappa(\cA),
+\begin{aligned}
+\mathrm{av}\bigl(r(z)\bigr) &= \kappa(\cA)
+&& \text{for abelian and scalar families},\\
+\mathrm{av}\bigl(r(z)\bigr) &= \kappa_{\mathrm{dp}}(\cA), \qquad
+\kappa(\cA) = \kappa_{\mathrm{dp}}(\cA) + \dim(\fg)/2
+&& \text{for non-abelian affine Kac--Moody.}
+\end{aligned}
 \end{equation}
-the modular characteristic of Theorem~D. At degree~$3$ the KZ
+This is the modular characteristic package of Theorem~D. At degree~$3$ the KZ
 associator projects to the cubic shadow~$\mathfrak C$; at degree~$4$
 the Yangian higher coproduct projects to the quartic resonance
 class~$\mathfrak Q$. Each degree-$n$ component of the ordered

file update:
diff --git a/chapters/theory/e1_modular_koszul.tex b/chapters/theory/e1_modular_koszul.tex
index a8a83c93d1d8dc248f8f9f6309990c5a7602c6c4..041dea657991f4089b4f0404b429bf3fff9ad079
--- a/chapters/theory/e1_modular_koszul.tex
+++ b/chapters/theory/e1_modular_koszul.tex
@@ -2255,8 +2255,11 @@
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item $(K_\cA^{E_1})_{0,2} = r(z)$, the classical $r$-matrix
  \textup{(}genus~$0$, degree~$2$\textup{)}. The coinvariant
- $\operatorname{av}(r(z)) = \kappa(\cA)$ recovers the scalar
- curvature.
+ $\operatorname{av}(r(z))$ recovers the scalar degree-$2$ shadow:
+ on abelian families $\operatorname{av}(r(z)) = \kappa(\cA)$,
+ while for non-abelian affine Kac--Moody
+ $\operatorname{av}(r(z)) = \kappa_{\mathrm{dp}}(\cA)$ and
+ $\kappa(\cA) = \kappa_{\mathrm{dp}}(\cA) + \dim(\fg)/2$.
 \item $(K_\cA^{E_1})_{0,3} = \Phi_{\mathrm{KZ}}(\cA)$, the
  KZ\slash Drinfeld associator \textup{(}genus~$0$, degree~$3$,
  for affine algebras;
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 789ce9acf5b68f150a665afd1b7486e6b1256a16..f5fd9aa34b7bb56449ed56b583ce3f595c37ce5f
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -895,8 +895,12 @@
 
 \item \emph{Leading-order modular shadow.}
  The $\Sigma_2$-coinvariant projection
- $\operatorname{av}(r(z)) = \kappa(\cA)$ is the modular
- characteristic, the first entry of the shadow obstruction tower
+ $\operatorname{av}(r(z))$ is the leading scalar shadow: it equals
+ $\kappa(\cA)$ on abelian and scalar families, while for
+ non-abelian affine Kac--Moody it gives
+ $\kappa_{\mathrm{dp}}(\cA)$ and the full modular characteristic is
+ $\kappa(\cA) = \kappa_{\mathrm{dp}}(\cA) + \dim(\fg)/2$. This is
+ the first entry of the shadow obstruction tower
  \textup{(}equation~\textup{\eqref{eq:intro-kappa-from-r}};
  Theorem~\textup{\ref{thm:e1-primacy}}\textup{)}. The residue contains
  a matrix-valued refinement; averaging produces the scalar.
@@ -1262,17 +1266,18 @@
 \;=\;
 \Theta_\cA.
 \end{equation}
-At degree~$2$, this projection records only one number: the
-$\Sigma_2$-coinvariant of the residue of $r(z)$ at $z = 0$ is the
-modular characteristic
+At degree~$2$, this projection records only one scalar: the
+$\Sigma_2$-coinvariant of the residue of $r(z)$ at $z = 0$ is
 \begin{equation}\label{eq:intro-kappa-from-r}
-\kappa(\cA)
-\;=\;
 \operatorname{av}\bigl(r(z)\bigr)
 \;=\;
 \tfrac{1}{2}\,\operatorname{tr}\!\bigl[\Res_{z = 0} r(z)\bigr],
 \end{equation}
 where the trace is the cyclic trace on $\End(V^{\otimes 2})$.
+For abelian and scalar families,
+\[
+\kappa(\cA) = \operatorname{av}\bigl(r(z)\bigr).
+\]
 For the affine Kac--Moody vacuum algebra $V_k(\mathfrak{g})$ at
 non-critical level, the averaging formula
 \eqref{eq:intro-kappa-from-r} specializes to the Sugawara identity
diff --git a/standalone/survey_track_a_compressed.tex b/standalone/survey_track_a_compressed.tex
index cb62bb8b88937153678a962d34c4c5dac04b9700..084c11fb005499137646a882cff6cb86a1becc01
--- a/standalone/survey_track_a_compressed.tex
+++ b/standalone/survey_track_a_compressed.tex
@@ -361,11 +361,17 @@
 \]
 a matrix-valued rational function encoding the full binary OPE data.
 Applying $\mathrm{av}$ at degree~$2$ collapses the profile to a single
-scalar,
+scalar shadow:
 \begin{equation}\label{eq:av-organizing}
-\mathrm{av}\bigl(r(z)\bigr)\;=\;\kappa(\cA),
+\begin{aligned}
+\mathrm{av}\bigl(r(z)\bigr) &= \kappa(\cA)
+&& \text{for abelian and scalar families},\\
+\mathrm{av}\bigl(r(z)\bigr) &= \kappa_{\mathrm{dp}}(\cA), \qquad
+\kappa(\cA) = \kappa_{\mathrm{dp}}(\cA) + \dim(\fg)/2
+&& \text{for non-abelian affine Kac--Moody.}
+\end{aligned}
 \end{equation}
-the modular characteristic of Theorem~D. At degree~$3$ the KZ
+This is the modular characteristic package of Theorem~D. At degree~$3$ the KZ
 associator projects to the cubic shadow~$\mathfrak C$; at degree~$4$
 the Yangian higher coproduct projects to the quartic resonance
 class~$\mathfrak Q$. Each degree-$n$ component of the ordered


thinking
**Considering backups and patches**

I need to patch shadow_towers_v3 and make sure to back that up. It might be worth checking if survey_track_a_compressed has any additional backup lines, but it turns out it doesn’t. So, focusing on getting the patch done for shadow_towers_v3 is the priority. I’m just trying to stay organized and ensure everything is properly backed up, so nothing gets lost! It's a bit tricky, but I've got this covered.
file update
M /Users/raeez/chiral-bar-cobar/standalone/shadow_towers_v3.tex
@@ -1875,3 +1875,7 @@
 $r(z) \in \mathrm{End}(V \otimes V)((z))$ at degree~$2$,
-whose averaging produces~$\kappa$. The structure of $r(z)$
+whose averaging produces the scalar degree-$2$ shadow:
+for abelian families this is~$\kappa$, while for non-abelian
+affine Kac--Moody it is~$\kappa_{\mathrm{dp}}$ and the full
+modular characteristic is
+$\kappa = \kappa_{\mathrm{dp}} + \dim(\fg)/2$. The structure of $r(z)$
 varies by class.
M /Users/raeez/chiral-bar-cobar/chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix
@@ -3006,4 +3006,7 @@
 $\Omega = \sum_a J^a \otimes J_a$ in $\fg \otimes \fg$, but
-$\mathrm{av}(r(z)) = \kappa = \dim(\fg)\cdot(k + h^\vee)/(2h^\vee)$
-is a single scalar.  The Casimir tensor determines the braiding
+$\mathrm{av}(r(z)) = \kappa_{\mathrm{dp}}
+= k\,\dim(\fg)/(2h^\vee)$ and
+$\kappa = \kappa_{\mathrm{dp}} + \dim(\fg)/2
+= \dim(\fg)\cdot(k + h^\vee)/(2h^\vee)$
+is a single scalar shadow. The Casimir tensor determines the braiding
 on the category of representations; the modular
apply_patch(auto_approved=true) exited 0 in 43ms:
Success. Updated the following files:
M standalone/shadow_towers_v3.tex
M chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix
file update:
diff --git a/chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix b/chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix
index 65cee60eb99d11add7451146de7bb27f5f556dbe..bc2ffa2f7955916ee7be9f7eea55dce5d1e68f9c
--- a/chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix
+++ b/chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix
@@ -3004,8 +3004,11 @@
 is \emph{irrecoverable}: $r(z) = k\,\Omega/z$ carries the
 Casimir tensor
 $\Omega = \sum_a J^a \otimes J_a$ in $\fg \otimes \fg$, but
-$\mathrm{av}(r(z)) = \kappa = \dim(\fg)\cdot(k + h^\vee)/(2h^\vee)$
-is a single scalar.  The Casimir tensor determines the braiding
+$\mathrm{av}(r(z)) = \kappa_{\mathrm{dp}}
+= k\,\dim(\fg)/(2h^\vee)$ and
+$\kappa = \kappa_{\mathrm{dp}} + \dim(\fg)/2
+= \dim(\fg)\cdot(k + h^\vee)/(2h^\vee)$
+is a single scalar shadow. The Casimir tensor determines the braiding
 on the category of representations; the modular
 characteristic determines the genus-$1$ anomaly.  These are
 different structural data at different categorical depths.
diff --git a/chapters/theory/e1_modular_koszul.tex b/chapters/theory/e1_modular_koszul.tex
index a8a83c93d1d8dc248f8f9f6309990c5a7602c6c4..041dea657991f4089b4f0404b429bf3fff9ad079
--- a/chapters/theory/e1_modular_koszul.tex
+++ b/chapters/theory/e1_modular_koszul.tex
@@ -2255,8 +2255,11 @@
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item $(K_\cA^{E_1})_{0,2} = r(z)$, the classical $r$-matrix
  \textup{(}genus~$0$, degree~$2$\textup{)}. The coinvariant
- $\operatorname{av}(r(z)) = \kappa(\cA)$ recovers the scalar
- curvature.
+ $\operatorname{av}(r(z))$ recovers the scalar degree-$2$ shadow:
+ on abelian families $\operatorname{av}(r(z)) = \kappa(\cA)$,
+ while for non-abelian affine Kac--Moody
+ $\operatorname{av}(r(z)) = \kappa_{\mathrm{dp}}(\cA)$ and
+ $\kappa(\cA) = \kappa_{\mathrm{dp}}(\cA) + \dim(\fg)/2$.
 \item $(K_\cA^{E_1})_{0,3} = \Phi_{\mathrm{KZ}}(\cA)$, the
  KZ\slash Drinfeld associator \textup{(}genus~$0$, degree~$3$,
  for affine algebras;
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 789ce9acf5b68f150a665afd1b7486e6b1256a16..f5fd9aa34b7bb56449ed56b583ce3f595c37ce5f
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -895,8 +895,12 @@
 
 \item \emph{Leading-order modular shadow.}
  The $\Sigma_2$-coinvariant projection
- $\operatorname{av}(r(z)) = \kappa(\cA)$ is the modular
- characteristic, the first entry of the shadow obstruction tower
+ $\operatorname{av}(r(z))$ is the leading scalar shadow: it equals
+ $\kappa(\cA)$ on abelian and scalar families, while for
+ non-abelian affine Kac--Moody it gives
+ $\kappa_{\mathrm{dp}}(\cA)$ and the full modular characteristic is
+ $\kappa(\cA) = \kappa_{\mathrm{dp}}(\cA) + \dim(\fg)/2$. This is
+ the first entry of the shadow obstruction tower
  \textup{(}equation~\textup{\eqref{eq:intro-kappa-from-r}};
  Theorem~\textup{\ref{thm:e1-primacy}}\textup{)}. The residue contains
  a matrix-valued refinement; averaging produces the scalar.
@@ -1262,17 +1266,18 @@
 \;=\;
 \Theta_\cA.
 \end{equation}
-At degree~$2$, this projection records only one number: the
-$\Sigma_2$-coinvariant of the residue of $r(z)$ at $z = 0$ is the
-modular characteristic
+At degree~$2$, this projection records only one scalar: the
+$\Sigma_2$-coinvariant of the residue of $r(z)$ at $z = 0$ is
 \begin{equation}\label{eq:intro-kappa-from-r}
-\kappa(\cA)
-\;=\;
 \operatorname{av}\bigl(r(z)\bigr)
 \;=\;
 \tfrac{1}{2}\,\operatorname{tr}\!\bigl[\Res_{z = 0} r(z)\bigr],
 \end{equation}
 where the trace is the cyclic trace on $\End(V^{\otimes 2})$.
+For abelian and scalar families,
+\[
+\kappa(\cA) = \operatorname{av}\bigl(r(z)\bigr).
+\]
 For the affine Kac--Moody vacuum algebra $V_k(\mathfrak{g})$ at
 non-critical level, the averaging formula
 \eqref{eq:intro-kappa-from-r} specializes to the Sugawara identity
diff --git a/standalone/shadow_towers_v3.tex b/standalone/shadow_towers_v3.tex
index 3e3cf779de2c8653d94026ee31a290ce83cfcba7..a5a7647da40e9a191f1addc0af5dafd181ae7a1c
--- a/standalone/shadow_towers_v3.tex
+++ b/standalone/shadow_towers_v3.tex
@@ -1873,7 +1873,11 @@
 The $E_1$ convolution algebra
 $\mathfrak{g}^{E_1}_\cA$ carries a spectral $R$-matrix
 $r(z) \in \mathrm{End}(V \otimes V)((z))$ at degree~$2$,
-whose averaging produces~$\kappa$. The structure of $r(z)$
+whose averaging produces the scalar degree-$2$ shadow:
+for abelian families this is~$\kappa$, while for non-abelian
+affine Kac--Moody it is~$\kappa_{\mathrm{dp}}$ and the full
+modular characteristic is
+$\kappa = \kappa_{\mathrm{dp}} + \dim(\fg)/2$. The structure of $r(z)$
 varies by class.
 
 \begin{example}[Class $\mathbf{G}$:
diff --git a/standalone/survey_track_a_compressed.tex b/standalone/survey_track_a_compressed.tex
index cb62bb8b88937153678a962d34c4c5dac04b9700..084c11fb005499137646a882cff6cb86a1becc01
--- a/standalone/survey_track_a_compressed.tex
+++ b/standalone/survey_track_a_compressed.tex
@@ -361,11 +361,17 @@
 \]
 a matrix-valued rational function encoding the full binary OPE data.
 Applying $\mathrm{av}$ at degree~$2$ collapses the profile to a single
-scalar,
+scalar shadow:
 \begin{equation}\label{eq:av-organizing}
-\mathrm{av}\bigl(r(z)\bigr)\;=\;\kappa(\cA),
+\begin{aligned}
+\mathrm{av}\bigl(r(z)\bigr) &= \kappa(\cA)
+&& \text{for abelian and scalar families},\\
+\mathrm{av}\bigl(r(z)\bigr) &= \kappa_{\mathrm{dp}}(\cA), \qquad
+\kappa(\cA) = \kappa_{\mathrm{dp}}(\cA) + \dim(\fg)/2
+&& \text{for non-abelian affine Kac--Moody.}
+\end{aligned}
 \end{equation}
-the modular characteristic of Theorem~D. At degree~$3$ the KZ
+This is the modular characteristic package of Theorem~D. At degree~$3$ the KZ
 associator projects to the cubic shadow~$\mathfrak C$; at degree~$4$
 the Yangian higher coproduct projects to the quartic resonance
 class~$\mathfrak Q$. Each degree-$n$ component of the ordered

file update:
diff --git a/chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix b/chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix
index 65cee60eb99d11add7451146de7bb27f5f556dbe..bc2ffa2f7955916ee7be9f7eea55dce5d1e68f9c
--- a/chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix
+++ b/chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix
@@ -3004,8 +3004,11 @@
 is \emph{irrecoverable}: $r(z) = k\,\Omega/z$ carries the
 Casimir tensor
 $\Omega = \sum_a J^a \otimes J_a$ in $\fg \otimes \fg$, but
-$\mathrm{av}(r(z)) = \kappa = \dim(\fg)\cdot(k + h^\vee)/(2h^\vee)$
-is a single scalar.  The Casimir tensor determines the braiding
+$\mathrm{av}(r(z)) = \kappa_{\mathrm{dp}}
+= k\,\dim(\fg)/(2h^\vee)$ and
+$\kappa = \kappa_{\mathrm{dp}} + \dim(\fg)/2
+= \dim(\fg)\cdot(k + h^\vee)/(2h^\vee)$
+is a single scalar shadow. The Casimir tensor determines the braiding
 on the category of representations; the modular
 characteristic determines the genus-$1$ anomaly.  These are
 different structural data at different categorical depths.
diff --git a/chapters/theory/e1_modular_koszul.tex b/chapters/theory/e1_modular_koszul.tex
index a8a83c93d1d8dc248f8f9f6309990c5a7602c6c4..041dea657991f4089b4f0404b429bf3fff9ad079
--- a/chapters/theory/e1_modular_koszul.tex
+++ b/chapters/theory/e1_modular_koszul.tex
@@ -2255,8 +2255,11 @@
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item $(K_\cA^{E_1})_{0,2} = r(z)$, the classical $r$-matrix
  \textup{(}genus~$0$, degree~$2$\textup{)}. The coinvariant
- $\operatorname{av}(r(z)) = \kappa(\cA)$ recovers the scalar
- curvature.
+ $\operatorname{av}(r(z))$ recovers the scalar degree-$2$ shadow:
+ on abelian families $\operatorname{av}(r(z)) = \kappa(\cA)$,
+ while for non-abelian affine Kac--Moody
+ $\operatorname{av}(r(z)) = \kappa_{\mathrm{dp}}(\cA)$ and
+ $\kappa(\cA) = \kappa_{\mathrm{dp}}(\cA) + \dim(\fg)/2$.
 \item $(K_\cA^{E_1})_{0,3} = \Phi_{\mathrm{KZ}}(\cA)$, the
  KZ\slash Drinfeld associator \textup{(}genus~$0$, degree~$3$,
  for affine algebras;
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 789ce9acf5b68f150a665afd1b7486e6b1256a16..f5fd9aa34b7bb56449ed56b583ce3f595c37ce5f
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -895,8 +895,12 @@
 
 \item \emph{Leading-order modular shadow.}
  The $\Sigma_2$-coinvariant projection
- $\operatorname{av}(r(z)) = \kappa(\cA)$ is the modular
- characteristic, the first entry of the shadow obstruction tower
+ $\operatorname{av}(r(z))$ is the leading scalar shadow: it equals
+ $\kappa(\cA)$ on abelian and scalar families, while for
+ non-abelian affine Kac--Moody it gives
+ $\kappa_{\mathrm{dp}}(\cA)$ and the full modular characteristic is
+ $\kappa(\cA) = \kappa_{\mathrm{dp}}(\cA) + \dim(\fg)/2$. This is
+ the first entry of the shadow obstruction tower
  \textup{(}equation~\textup{\eqref{eq:intro-kappa-from-r}};
  Theorem~\textup{\ref{thm:e1-primacy}}\textup{)}. The residue contains
  a matrix-valued refinement; averaging produces the scalar.
@@ -1262,17 +1266,18 @@
 \;=\;
 \Theta_\cA.
 \end{equation}
-At degree~$2$, this projection records only one number: the
-$\Sigma_2$-coinvariant of the residue of $r(z)$ at $z = 0$ is the
-modular characteristic
+At degree~$2$, this projection records only one scalar: the
+$\Sigma_2$-coinvariant of the residue of $r(z)$ at $z = 0$ is
 \begin{equation}\label{eq:intro-kappa-from-r}
-\kappa(\cA)
-\;=\;
 \operatorname{av}\bigl(r(z)\bigr)
 \;=\;
 \tfrac{1}{2}\,\operatorname{tr}\!\bigl[\Res_{z = 0} r(z)\bigr],
 \end{equation}
 where the trace is the cyclic trace on $\End(V^{\otimes 2})$.
+For abelian and scalar families,
+\[
+\kappa(\cA) = \operatorname{av}\bigl(r(z)\bigr).
+\]
 For the affine Kac--Moody vacuum algebra $V_k(\mathfrak{g})$ at
 non-critical level, the averaging formula
 \eqref{eq:intro-kappa-from-r} specializes to the Sugawara identity
diff --git a/standalone/shadow_towers_v3.tex b/standalone/shadow_towers_v3.tex
index 3e3cf779de2c8653d94026ee31a290ce83cfcba7..a5a7647da40e9a191f1addc0af5dafd181ae7a1c
--- a/standalone/shadow_towers_v3.tex
+++ b/standalone/shadow_towers_v3.tex
@@ -1873,7 +1873,11 @@
 The $E_1$ convolution algebra
 $\mathfrak{g}^{E_1}_\cA$ carries a spectral $R$-matrix
 $r(z) \in \mathrm{End}(V \otimes V)((z))$ at degree~$2$,
-whose averaging produces~$\kappa$. The structure of $r(z)$
+whose averaging produces the scalar degree-$2$ shadow:
+for abelian families this is~$\kappa$, while for non-abelian
+affine Kac--Moody it is~$\kappa_{\mathrm{dp}}$ and the full
+modular characteristic is
+$\kappa = \kappa_{\mathrm{dp}} + \dim(\fg)/2$. The structure of $r(z)$
 varies by class.
 
 \begin{example}[Class $\mathbf{G}$:
diff --git a/standalone/survey_track_a_compressed.tex b/standalone/survey_track_a_compressed.tex
index cb62bb8b88937153678a962d34c4c5dac04b9700..084c11fb005499137646a882cff6cb86a1becc01
--- a/standalone/survey_track_a_compressed.tex
+++ b/standalone/survey_track_a_compressed.tex
@@ -361,11 +361,17 @@
 \]
 a matrix-valued rational function encoding the full binary OPE data.
 Applying $\mathrm{av}$ at degree~$2$ collapses the profile to a single
-scalar,
+scalar shadow:
 \begin{equation}\label{eq:av-organizing}
-\mathrm{av}\bigl(r(z)\bigr)\;=\;\kappa(\cA),
+\begin{aligned}
+\mathrm{av}\bigl(r(z)\bigr) &= \kappa(\cA)
+&& \text{for abelian and scalar families},\\
+\mathrm{av}\bigl(r(z)\bigr) &= \kappa_{\mathrm{dp}}(\cA), \qquad
+\kappa(\cA) = \kappa_{\mathrm{dp}}(\cA) + \dim(\fg)/2
+&& \text{for non-abelian affine Kac--Moody.}
+\end{aligned}
 \end{equation}
-the modular characteristic of Theorem~D. At degree~$3$ the KZ
+This is the modular characteristic package of Theorem~D. At degree~$3$ the KZ
 associator projects to the cubic shadow~$\mathfrak C$; at degree~$4$
 the Yangian higher coproduct projects to the quartic resonance
 class~$\mathfrak Q$. Each degree-$n$ component of the ordered


thinking
**Inspecting the repo**

I want to check if there’s anything problematic left in the current repository. It’s important to ensure everything’s in good shape. I’ll go ahead and run some checks to identify if there’s any bad code or remaining issues. That way, I can address them before moving forward. Let's make sure I'm covering all bases!
codex
The in-repo edits are in. I’m re-reading the touched passages and running grep for the old `av(r)=\kappa` surface so I can catch any remaining live or backup hits before I close.
exec
/bin/zsh -lc "sed -n '894,906p' chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1264,1286p' chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2254,2264p' chapters/theory/e1_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\noindent\textbf{Low-degree identifications.}
\begin{enumerate}[label=\textup{(\roman*)}]
\item $(K_\cA^{E_1})_{0,2} = r(z)$, the classical $r$-matrix
 \textup{(}genus~$0$, degree~$2$\textup{)}. The coinvariant
 $\operatorname{av}(r(z))$ recovers the scalar degree-$2$ shadow:
 on abelian families $\operatorname{av}(r(z)) = \kappa(\cA)$,
 while for non-abelian affine Kac--Moody
 $\operatorname{av}(r(z)) = \kappa_{\mathrm{dp}}(\cA)$ and
 $\kappa(\cA) = \kappa_{\mathrm{dp}}(\cA) + \dim(\fg)/2$.
\item $(K_\cA^{E_1})_{0,3} = \Phi_{\mathrm{KZ}}(\cA)$, the
 KZ\slash Drinfeld associator \textup{(}genus~$0$, degree~$3$,
 succeeded in 51ms:
 $(r(z), r_3, r_4, \ldots)$ is one object read at ascending degree.

\item \emph{Leading-order modular shadow.}
 The $\Sigma_2$-coinvariant projection
 $\operatorname{av}(r(z))$ is the leading scalar shadow: it equals
 $\kappa(\cA)$ on abelian and scalar families, while for
 non-abelian affine Kac--Moody it gives
 $\kappa_{\mathrm{dp}}(\cA)$ and the full modular characteristic is
 $\kappa(\cA) = \kappa_{\mathrm{dp}}(\cA) + \dim(\fg)/2$. This is
 the first entry of the shadow obstruction tower
 \textup{(}equation~\textup{\eqref{eq:intro-kappa-from-r}};
 Theorem~\textup{\ref{thm:e1-primacy}}\textup{)}. The residue contains
 a matrix-valued refinement; averaging produces the scalar.
 succeeded in 51ms:
\begin{equation}\label{eq:intro-av-theta}
\operatorname{av}\bigl(\Theta_\cA^{\Eone}\bigr)
\;=\;
\Theta_\cA.
\end{equation}
At degree~$2$, this projection records only one scalar: the
$\Sigma_2$-coinvariant of the residue of $r(z)$ at $z = 0$ is
\begin{equation}\label{eq:intro-kappa-from-r}
\operatorname{av}\bigl(r(z)\bigr)
\;=\;
\tfrac{1}{2}\,\operatorname{tr}\!\bigl[\Res_{z = 0} r(z)\bigr],
\end{equation}
where the trace is the cyclic trace on $\End(V^{\otimes 2})$.
For abelian and scalar families,
\[
\kappa(\cA) = \operatorname{av}\bigl(r(z)\bigr).
\]
For the affine Kac--Moody vacuum algebra $V_k(\mathfrak{g})$ at
non-critical level, the averaging formula
\eqref{eq:intro-kappa-from-r} specializes to the Sugawara identity
exec
/bin/zsh -lc "sed -n '360,376p' standalone/survey_track_a_compressed.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1872,1882p' standalone/shadow_towers_v3.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '3002,3012p' chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg --pcre2 -n -C 1 '\\\\(?:av|mathrm\\{av\\}|operatorname\\{av\\})\\s*\\(r(?:_0)?\\(z\\)\\)\\s*=\\s*\\\\kappa(?:\\(["'^)]*'"\\))?(?"'!_)|averag[a-z]*[''^'"\\n]{0,120}\\\\kappa(?:\\(["'^)]*'"\\))?(?"'!_)'"' chapters standalone" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
r(z)\;=\;\operatorname{Res}^{\mathrm{coll}}_{0,2}\bigl(\Theta^{E_1}_{\cA}\bigr),
\]
a matrix-valued rational function encoding the full binary OPE data.
Applying $\mathrm{av}$ at degree~$2$ collapses the profile to a single
scalar shadow:
\begin{equation}\label{eq:av-organizing}
\begin{aligned}
\mathrm{av}\bigl(r(z)\bigr) &= \kappa(\cA)
&& \text{for abelian and scalar families},\\
\mathrm{av}\bigl(r(z)\bigr) &= \kappa_{\mathrm{dp}}(\cA), \qquad
\kappa(\cA) = \kappa_{\mathrm{dp}}(\cA) + \dim(\fg)/2
&& \text{for non-abelian affine Kac--Moody.}
\end{aligned}
\end{equation}
This is the modular characteristic package of Theorem~D. At degree~$3$ the KZ
associator projects to the cubic shadow~$\mathfrak C$; at degree~$4$
the Yangian higher coproduct projects to the quartic resonance
 succeeded in 52ms:

The $E_1$ convolution algebra
$\mathfrak{g}^{E_1}_\cA$ carries a spectral $R$-matrix
$r(z) \in \mathrm{End}(V \otimes V)((z))$ at degree~$2$,
whose averaging produces the scalar degree-$2$ shadow:
for abelian families this is~$\kappa$, while for non-abelian
affine Kac--Moody it is~$\kappa_{\mathrm{dp}}$ and the full
modular characteristic is
$\kappa = \kappa_{\mathrm{dp}} + \dim(\fg)/2$. The structure of $r(z)$
varies by class.

 succeeded in 52ms:
the single scalar.
For affine $\widehat{\mathfrak{sl}}_2$ at level~$k$, the loss
is \emph{irrecoverable}: $r(z) = k\,\Omega/z$ carries the
Casimir tensor
$\Omega = \sum_a J^a \otimes J_a$ in $\fg \otimes \fg$, but
$\mathrm{av}(r(z)) = \kappa_{\mathrm{dp}}
= k\,\dim(\fg)/(2h^\vee)$ and
$\kappa = \kappa_{\mathrm{dp}} + \dim(\fg)/2
= \dim(\fg)\cdot(k + h^\vee)/(2h^\vee)$
is a single scalar shadow. The Casimir tensor determines the braiding
on the category of representations; the modular
 succeeded in 52ms:
standalone/en_chiral_operadic_circle.tex-2649-\label{rem:e-sugawara-shift}
standalone/en_chiral_operadic_circle.tex:2650:For the Heisenberg (abelian), $\mathrm{av}(r(z)) = \kappa$
standalone/en_chiral_operadic_circle.tex-2651-holds directly. For non-abelian Kac--Moody, the full
--
standalone/en_chiral_operadic_circle.tex-2656-fundamental difference between abelian and non-abelian
standalone/en_chiral_operadic_circle.tex:2657:averaging, and is the reason $\kappa(V_k(\fg)) \neq 0$ at
standalone/en_chiral_operadic_circle.tex-2658-$k = 0$ (the non-abelian Lie bracket persists).
--
standalone/e1_primacy_ordered_bar.tex-1200-opposite-duality, and satisfies
standalone/e1_primacy_ordered_bar.tex:1201:$\av(r_0(z)) = \kappa(\cA)$ on abelian families, while for
standalone/e1_primacy_ordered_bar.tex-1202-non-abelian affine Kac--Moody
--
standalone/e1_primacy_ordered_bar.tex-1234-function of a single variable, the collision coordinate~$z$. The
standalone/e1_primacy_ordered_bar.tex:1235:statement $\av(r(z)) = \kappa$ says this exactly for Heisenberg,
standalone/e1_primacy_ordered_bar.tex-1236-while for non-abelian affine Kac--Moody the same averaging recovers
--
standalone/e1_primacy_ordered_bar.tex-1426-chain-level datum on the ordered side that becomes trivial
standalone/e1_primacy_ordered_bar.tex:1427:($\Sigma_2$-average $\to \kappa$) on the symmetric side. The
standalone/e1_primacy_ordered_bar.tex-1428-Drinfeld associator $\Phi_{\mathrm{KZ}}$ is a chain-level datum at
--
file update:
diff --git a/chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix b/chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix
index 65cee60eb99d11add7451146de7bb27f5f556dbe..bc2ffa2f7955916ee7be9f7eea55dce5d1e68f9c
--- a/chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix
+++ b/chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix
@@ -3004,8 +3004,11 @@
 is \emph{irrecoverable}: $r(z) = k\,\Omega/z$ carries the
 Casimir tensor
 $\Omega = \sum_a J^a \otimes J_a$ in $\fg \otimes \fg$, but
-$\mathrm{av}(r(z)) = \kappa = \dim(\fg)\cdot(k + h^\vee)/(2h^\vee)$
-is a single scalar.  The Casimir tensor determines the braiding
+$\mathrm{av}(r(z)) = \kappa_{\mathrm{dp}}
+= k\,\dim(\fg)/(2h^\vee)$ and
+$\kappa = \kappa_{\mathrm{dp}} + \dim(\fg)/2
+= \dim(\fg)\cdot(k + h^\vee)/(2h^\vee)$
+is a single scalar shadow. The Casimir tensor determines the braiding
 on the category of representations; the modular
 characteristic determines the genus-$1$ anomaly.  These are
 different structural data at different categorical depths.
diff --git a/chapters/theory/e1_modular_koszul.tex b/chapters/theory/e1_modular_koszul.tex
index a8a83c93d1d8dc248f8f9f6309990c5a7602c6c4..041dea657991f4089b4f0404b429bf3fff9ad079
--- a/chapters/theory/e1_modular_koszul.tex
+++ b/chapters/theory/e1_modular_koszul.tex
@@ -2255,8 +2255,11 @@
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item $(K_\cA^{E_1})_{0,2} = r(z)$, the classical $r$-matrix
  \textup{(}genus~$0$, degree~$2$\textup{)}. The coinvariant
- $\operatorname{av}(r(z)) = \kappa(\cA)$ recovers the scalar
- curvature.
+ $\operatorname{av}(r(z))$ recovers the scalar degree-$2$ shadow:
+ on abelian families $\operatorname{av}(r(z)) = \kappa(\cA)$,
+ while for non-abelian affine Kac--Moody
+ $\operatorname{av}(r(z)) = \kappa_{\mathrm{dp}}(\cA)$ and
+ $\kappa(\cA) = \kappa_{\mathrm{dp}}(\cA) + \dim(\fg)/2$.
 \item $(K_\cA^{E_1})_{0,3} = \Phi_{\mathrm{KZ}}(\cA)$, the
  KZ\slash Drinfeld associator \textup{(}genus~$0$, degree~$3$,
  for affine algebras;
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 789ce9acf5b68f150a665afd1b7486e6b1256a16..f5fd9aa34b7bb56449ed56b583ce3f595c37ce5f
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -895,8 +895,12 @@
 
 \item \emph{Leading-order modular shadow.}
  The $\Sigma_2$-coinvariant projection
- $\operatorname{av}(r(z)) = \kappa(\cA)$ is the modular
- characteristic, the first entry of the shadow obstruction tower
+ $\operatorname{av}(r(z))$ is the leading scalar shadow: it equals
+ $\kappa(\cA)$ on abelian and scalar families, while for
+ non-abelian affine Kac--Moody it gives
+ $\kappa_{\mathrm{dp}}(\cA)$ and the full modular characteristic is
+ $\kappa(\cA) = \kappa_{\mathrm{dp}}(\cA) + \dim(\fg)/2$. This is
+ the first entry of the shadow obstruction tower
  \textup{(}equation~\textup{\eqref{eq:intro-kappa-from-r}};
  Theorem~\textup{\ref{thm:e1-primacy}}\textup{)}. The residue contains
  a matrix-valued refinement; averaging produces the scalar.
@@ -1262,17 +1266,18 @@
 \;=\;
 \Theta_\cA.
 \end{equation}
-At degree~$2$, this projection records only one number: the
-$\Sigma_2$-coinvariant of the residue of $r(z)$ at $z = 0$ is the
-modular characteristic
+At degree~$2$, this projection records only one scalar: the
+$\Sigma_2$-coinvariant of the residue of $r(z)$ at $z = 0$ is
 \begin{equation}\label{eq:intro-kappa-from-r}
-\kappa(\cA)
-\;=\;
 \operatorname{av}\bigl(r(z)\bigr)
 \;=\;
 \tfrac{1}{2}\,\operatorname{tr}\!\bigl[\Res_{z = 0} r(z)\bigr],
 \end{equation}
 where the trace is the cyclic trace on $\End(V^{\otimes 2})$.
+For abelian and scalar families,
+\[
+\kappa(\cA) = \operatorname{av}\bigl(r(z)\bigr).
+\]
 For the affine Kac--Moody vacuum algebra $V_k(\mathfrak{g})$ at
 non-critical level, the averaging formula
 \eqref{eq:intro-kappa-from-r} specializes to the Sugawara identity
diff --git a/standalone/shadow_towers_v3.tex b/standalone/shadow_towers_v3.tex
index 3e3cf779de2c8653d94026ee31a290ce83cfcba7..a5a7647da40e9a191f1addc0af5dafd181ae7a1c
--- a/standalone/shadow_towers_v3.tex
+++ b/standalone/shadow_towers_v3.tex
@@ -1873,7 +1873,11 @@
 The $E_1$ convolution algebra
 $\mathfrak{g}^{E_1}_\cA$ carries a spectral $R$-matrix
 $r(z) \in \mathrm{End}(V \otimes V)((z))$ at degree~$2$,
-whose averaging produces~$\kappa$. The structure of $r(z)$
+whose averaging produces the scalar degree-$2$ shadow:
+for abelian families this is~$\kappa$, while for non-abelian
+affine Kac--Moody it is~$\kappa_{\mathrm{dp}}$ and the full
+modular characteristic is
+$\kappa = \kappa_{\mathrm{dp}} + \dim(\fg)/2$. The structure of $r(z)$
 varies by class.
 
 \begin{example}[Class $\mathbf{G}$:
diff --git a/standalone/survey_track_a_compressed.tex b/standalone/survey_track_a_compressed.tex
index cb62bb8b88937153678a962d34c4c5dac04b9700..084c11fb005499137646a882cff6cb86a1becc01
--- a/standalone/survey_track_a_compressed.tex
+++ b/standalone/survey_track_a_compressed.tex
@@ -361,11 +361,17 @@
 \]
 a matrix-valued rational function encoding the full binary OPE data.
 Applying $\mathrm{av}$ at degree~$2$ collapses the profile to a single
-scalar,
+scalar shadow:
 \begin{equation}\label{eq:av-organizing}
-\mathrm{av}\bigl(r(z)\bigr)\;=\;\kappa(\cA),
+\begin{aligned}
+\mathrm{av}\bigl(r(z)\bigr) &= \kappa(\cA)
+&& \text{for abelian and scalar families},\\
+\mathrm{av}\bigl(r(z)\bigr) &= \kappa_{\mathrm{dp}}(\cA), \qquad
+\kappa(\cA) = \kappa_{\mathrm{dp}}(\cA) + \dim(\fg)/2
+&& \text{for non-abelian affine Kac--Moody.}
+\end{aligned}
 \end{equation}
-the modular characteristic of Theorem~D. At degree~$3$ the KZ
+This is the modular characteristic package of Theorem~D. At degree~$3$ the KZ
 associator projects to the cubic shadow~$\mathfrak C$; at degree~$4$
 the Yangian higher coproduct projects to the quartic resonance
 class~$\mathfrak Q$. Each degree-$n$ component of the ordered

exec
/bin/zsh -lc "sed -n '1652,1664p' chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
$\widehat{\mathfrak g}_k$ with $r(z) = k\,\Omega/z$ at level $k$,
Virasoro $\mathrm{Vir}_c$ with $r(z) = (c/2)/z^3 + 2T/z$,
the $\mathcal{W}_N$-algebras, the $\beta\gamma$ system, and the
lattice vertex algebras $V_\Lambda$. In every case the $R$-matrix is
\emph{derived} from the OPE by residue extraction; nothing new enters
at the $R$-matrix level beyond what the local OPE already carries.
Tier (b) is still $\Einf$-chiral in the three-leaps classification of
Volume~II: the algebra is commutative up to quasi-isomorphism, and
averaging recovers the modular shadow $\kappa$ without information
loss beyond the $\Sigma_n$-coinvariant step.

Tier (c) is the genuinely $\Eone$-primitive extreme. The Yangian
$Y(\mathfrak g)$ and the Etingof--Kazhdan quantum vertex algebras
file update:
diff --git a/chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix b/chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix
index 65cee60eb99d11add7451146de7bb27f5f556dbe..bc2ffa2f7955916ee7be9f7eea55dce5d1e68f9c
--- a/chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix
+++ b/chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix
@@ -3004,8 +3004,11 @@
 is \emph{irrecoverable}: $r(z) = k\,\Omega/z$ carries the
 Casimir tensor
 $\Omega = \sum_a J^a \otimes J_a$ in $\fg \otimes \fg$, but
-$\mathrm{av}(r(z)) = \kappa = \dim(\fg)\cdot(k + h^\vee)/(2h^\vee)$
-is a single scalar.  The Casimir tensor determines the braiding
+$\mathrm{av}(r(z)) = \kappa_{\mathrm{dp}}
+= k\,\dim(\fg)/(2h^\vee)$ and
+$\kappa = \kappa_{\mathrm{dp}} + \dim(\fg)/2
+= \dim(\fg)\cdot(k + h^\vee)/(2h^\vee)$
+is a single scalar shadow. The Casimir tensor determines the braiding
 on the category of representations; the modular
 characteristic determines the genus-$1$ anomaly.  These are
 different structural data at different categorical depths.
diff --git a/chapters/theory/e1_modular_koszul.tex b/chapters/theory/e1_modular_koszul.tex
index a8a83c93d1d8dc248f8f9f6309990c5a7602c6c4..041dea657991f4089b4f0404b429bf3fff9ad079
--- a/chapters/theory/e1_modular_koszul.tex
+++ b/chapters/theory/e1_modular_koszul.tex
@@ -2255,8 +2255,11 @@
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item $(K_\cA^{E_1})_{0,2} = r(z)$, the classical $r$-matrix
  \textup{(}genus~$0$, degree~$2$\textup{)}. The coinvariant
- $\operatorname{av}(r(z)) = \kappa(\cA)$ recovers the scalar
- curvature.
+ $\operatorname{av}(r(z))$ recovers the scalar degree-$2$ shadow:
+ on abelian families $\operatorname{av}(r(z)) = \kappa(\cA)$,
+ while for non-abelian affine Kac--Moody
+ $\operatorname{av}(r(z)) = \kappa_{\mathrm{dp}}(\cA)$ and
+ $\kappa(\cA) = \kappa_{\mathrm{dp}}(\cA) + \dim(\fg)/2$.
 \item $(K_\cA^{E_1})_{0,3} = \Phi_{\mathrm{KZ}}(\cA)$, the
  KZ\slash Drinfeld associator \textup{(}genus~$0$, degree~$3$,
  for affine algebras;
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 789ce9acf5b68f150a665afd1b7486e6b1256a16..f5fd9aa34b7bb56449ed56b583ce3f595c37ce5f
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -895,8 +895,12 @@
 
 \item \emph{Leading-order modular shadow.}
  The $\Sigma_2$-coinvariant projection
- $\operatorname{av}(r(z)) = \kappa(\cA)$ is the modular
- characteristic, the first entry of the shadow obstruction tower
+ $\operatorname{av}(r(z))$ is the leading scalar shadow: it equals
+ $\kappa(\cA)$ on abelian and scalar families, while for
+ non-abelian affine Kac--Moody it gives
+ $\kappa_{\mathrm{dp}}(\cA)$ and the full modular characteristic is
+ $\kappa(\cA) = \kappa_{\mathrm{dp}}(\cA) + \dim(\fg)/2$. This is
+ the first entry of the shadow obstruction tower
  \textup{(}equation~\textup{\eqref{eq:intro-kappa-from-r}};
  Theorem~\textup{\ref{thm:e1-primacy}}\textup{)}. The residue contains
  a matrix-valued refinement; averaging produces the scalar.
@@ -1262,17 +1266,18 @@
 \;=\;
 \Theta_\cA.
 \end{equation}
-At degree~$2$, this projection records only one number: the
-$\Sigma_2$-coinvariant of the residue of $r(z)$ at $z = 0$ is the
-modular characteristic
+At degree~$2$, this projection records only one scalar: the
+$\Sigma_2$-coinvariant of the residue of $r(z)$ at $z = 0$ is
 \begin{equation}\label{eq:intro-kappa-from-r}
-\kappa(\cA)
-\;=\;
 \operatorname{av}\bigl(r(z)\bigr)
 \;=\;
 \tfrac{1}{2}\,\operatorname{tr}\!\bigl[\Res_{z = 0} r(z)\bigr],
 \end{equation}
 where the trace is the cyclic trace on $\End(V^{\otimes 2})$.
+For abelian and scalar families,
+\[
+\kappa(\cA) = \operatorname{av}\bigl(r(z)\bigr).
+\]
 For the affine Kac--Moody vacuum algebra $V_k(\mathfrak{g})$ at
 non-critical level, the averaging formula
 \eqref{eq:intro-kappa-from-r} specializes to the Sugawara identity
diff --git a/standalone/shadow_towers_v3.tex b/standalone/shadow_towers_v3.tex
index 3e3cf779de2c8653d94026ee31a290ce83cfcba7..a5a7647da40e9a191f1addc0af5dafd181ae7a1c
--- a/standalone/shadow_towers_v3.tex
+++ b/standalone/shadow_towers_v3.tex
@@ -1873,7 +1873,11 @@
 The $E_1$ convolution algebra
 $\mathfrak{g}^{E_1}_\cA$ carries a spectral $R$-matrix
 $r(z) \in \mathrm{End}(V \otimes V)((z))$ at degree~$2$,
-whose averaging produces~$\kappa$. The structure of $r(z)$
+whose averaging produces the scalar degree-$2$ shadow:
+for abelian families this is~$\kappa$, while for non-abelian
+affine Kac--Moody it is~$\kappa_{\mathrm{dp}}$ and the full
+modular characteristic is
+$\kappa = \kappa_{\mathrm{dp}} + \dim(\fg)/2$. The structure of $r(z)$
 varies by class.
 
 \begin{example}[Class $\mathbf{G}$:
diff --git a/standalone/survey_track_a_compressed.tex b/standalone/survey_track_a_compressed.tex
index cb62bb8b88937153678a962d34c4c5dac04b9700..084c11fb005499137646a882cff6cb86a1becc01
--- a/standalone/survey_track_a_compressed.tex
+++ b/standalone/survey_track_a_compressed.tex
@@ -361,11 +361,17 @@
 \]
 a matrix-valued rational function encoding the full binary OPE data.
 Applying $\mathrm{av}$ at degree~$2$ collapses the profile to a single
-scalar,
+scalar shadow:
 \begin{equation}\label{eq:av-organizing}
-\mathrm{av}\bigl(r(z)\bigr)\;=\;\kappa(\cA),
+\begin{aligned}
+\mathrm{av}\bigl(r(z)\bigr) &= \kappa(\cA)
+&& \text{for abelian and scalar families},\\
+\mathrm{av}\bigl(r(z)\bigr) &= \kappa_{\mathrm{dp}}(\cA), \qquad
+\kappa(\cA) = \kappa_{\mathrm{dp}}(\cA) + \dim(\fg)/2
+&& \text{for non-abelian affine Kac--Moody.}
+\end{aligned}
 \end{equation}
-the modular characteristic of Theorem~D. At degree~$3$ the KZ
+This is the modular characteristic package of Theorem~D. At degree~$3$ the KZ
 associator projects to the cubic shadow~$\mathfrak C$; at degree~$4$
 the Yangian higher coproduct projects to the quartic resonance
 class~$\mathfrak Q$. Each degree-$n$ component of the ordered


thinking
**Patching and Searching**

I think it would be better to patch something. I should search for general terms like "averaging recovers modular shadow κ without information loss." It might be necessary to patch the current repo, especially lines 1660 and chiral_chern_weil 1216. Searching for "averaging produces the scalar" doesn't seem wrong. I might also want to check for the term `averaging.*modular characteristic` in a more generic way. I could use rg for additional findings too.
codex
A couple of generic prose lines are still too loose even though the displayed formulas are fixed. I’m tightening those last writable sentences so the remaining grep surface is either abelian-only, explicitly corrected, or family-specific.
exec
/bin/zsh -lc "sed -n '1214,1222p' standalone/chiral_chern_weil.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\section{The chiral curvature}\label{sec:chiral-cw}

The averaging map extracts~$\kappa$ from the $r$-matrix.
The question it forces is: what role does~$\kappa$ play
geometrically? The answer: $\kappa$ is the proportionality
constant of a curvature. The bar differential, which squares
to zero on~$\mathbb{P}^1$, fails to square to zero on
higher-genus curves; the failure is proportional to~$\kappa$.
This section derives that formula from the propagator on a
exec
/bin/zsh -lc "rg -n 'averaging recovers the modular shadow|extracts~\\\\kappa from the \\\\"'$r'"\\\\"'$-matrix|extracts the modular characteristic|average is the modular characteristic'"' chapters standalone" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
standalone/shadow_towers_v3.tex:1849:average is the modular characteristic~$\kappa$, with the
chapters/theory/introduction.tex:1660:averaging recovers the modular shadow $\kappa$ without information
file update:
diff --git a/chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix b/chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix
index 65cee60eb99d11add7451146de7bb27f5f556dbe..bc2ffa2f7955916ee7be9f7eea55dce5d1e68f9c
--- a/chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix
+++ b/chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix
@@ -3004,8 +3004,11 @@
 is \emph{irrecoverable}: $r(z) = k\,\Omega/z$ carries the
 Casimir tensor
 $\Omega = \sum_a J^a \otimes J_a$ in $\fg \otimes \fg$, but
-$\mathrm{av}(r(z)) = \kappa = \dim(\fg)\cdot(k + h^\vee)/(2h^\vee)$
-is a single scalar.  The Casimir tensor determines the braiding
+$\mathrm{av}(r(z)) = \kappa_{\mathrm{dp}}
+= k\,\dim(\fg)/(2h^\vee)$ and
+$\kappa = \kappa_{\mathrm{dp}} + \dim(\fg)/2
+= \dim(\fg)\cdot(k + h^\vee)/(2h^\vee)$
+is a single scalar shadow. The Casimir tensor determines the braiding
 on the category of representations; the modular
 characteristic determines the genus-$1$ anomaly.  These are
 different structural data at different categorical depths.
diff --git a/chapters/theory/e1_modular_koszul.tex b/chapters/theory/e1_modular_koszul.tex
index a8a83c93d1d8dc248f8f9f6309990c5a7602c6c4..041dea657991f4089b4f0404b429bf3fff9ad079
--- a/chapters/theory/e1_modular_koszul.tex
+++ b/chapters/theory/e1_modular_koszul.tex
@@ -2255,8 +2255,11 @@
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item $(K_\cA^{E_1})_{0,2} = r(z)$, the classical $r$-matrix
  \textup{(}genus~$0$, degree~$2$\textup{)}. The coinvariant
- $\operatorname{av}(r(z)) = \kappa(\cA)$ recovers the scalar
- curvature.
+ $\operatorname{av}(r(z))$ recovers the scalar degree-$2$ shadow:
+ on abelian families $\operatorname{av}(r(z)) = \kappa(\cA)$,
+ while for non-abelian affine Kac--Moody
+ $\operatorname{av}(r(z)) = \kappa_{\mathrm{dp}}(\cA)$ and
+ $\kappa(\cA) = \kappa_{\mathrm{dp}}(\cA) + \dim(\fg)/2$.
 \item $(K_\cA^{E_1})_{0,3} = \Phi_{\mathrm{KZ}}(\cA)$, the
  KZ\slash Drinfeld associator \textup{(}genus~$0$, degree~$3$,
  for affine algebras;
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 789ce9acf5b68f150a665afd1b7486e6b1256a16..f5fd9aa34b7bb56449ed56b583ce3f595c37ce5f
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -895,8 +895,12 @@
 
 \item \emph{Leading-order modular shadow.}
  The $\Sigma_2$-coinvariant projection
- $\operatorname{av}(r(z)) = \kappa(\cA)$ is the modular
- characteristic, the first entry of the shadow obstruction tower
+ $\operatorname{av}(r(z))$ is the leading scalar shadow: it equals
+ $\kappa(\cA)$ on abelian and scalar families, while for
+ non-abelian affine Kac--Moody it gives
+ $\kappa_{\mathrm{dp}}(\cA)$ and the full modular characteristic is
+ $\kappa(\cA) = \kappa_{\mathrm{dp}}(\cA) + \dim(\fg)/2$. This is
+ the first entry of the shadow obstruction tower
  \textup{(}equation~\textup{\eqref{eq:intro-kappa-from-r}};
  Theorem~\textup{\ref{thm:e1-primacy}}\textup{)}. The residue contains
  a matrix-valued refinement; averaging produces the scalar.
@@ -1262,17 +1266,18 @@
 \;=\;
 \Theta_\cA.
 \end{equation}
-At degree~$2$, this projection records only one number: the
-$\Sigma_2$-coinvariant of the residue of $r(z)$ at $z = 0$ is the
-modular characteristic
+At degree~$2$, this projection records only one scalar: the
+$\Sigma_2$-coinvariant of the residue of $r(z)$ at $z = 0$ is
 \begin{equation}\label{eq:intro-kappa-from-r}
-\kappa(\cA)
-\;=\;
 \operatorname{av}\bigl(r(z)\bigr)
 \;=\;
 \tfrac{1}{2}\,\operatorname{tr}\!\bigl[\Res_{z = 0} r(z)\bigr],
 \end{equation}
 where the trace is the cyclic trace on $\End(V^{\otimes 2})$.
+For abelian and scalar families,
+\[
+\kappa(\cA) = \operatorname{av}\bigl(r(z)\bigr).
+\]
 For the affine Kac--Moody vacuum algebra $V_k(\mathfrak{g})$ at
 non-critical level, the averaging formula
 \eqref{eq:intro-kappa-from-r} specializes to the Sugawara identity
diff --git a/standalone/shadow_towers_v3.tex b/standalone/shadow_towers_v3.tex
index 3e3cf779de2c8653d94026ee31a290ce83cfcba7..a5a7647da40e9a191f1addc0af5dafd181ae7a1c
--- a/standalone/shadow_towers_v3.tex
+++ b/standalone/shadow_towers_v3.tex
@@ -1873,7 +1873,11 @@
 The $E_1$ convolution algebra
 $\mathfrak{g}^{E_1}_\cA$ carries a spectral $R$-matrix
 $r(z) \in \mathrm{End}(V \otimes V)((z))$ at degree~$2$,
-whose averaging produces~$\kappa$. The structure of $r(z)$
+whose averaging produces the scalar degree-$2$ shadow:
+for abelian families this is~$\kappa$, while for non-abelian
+affine Kac--Moody it is~$\kappa_{\mathrm{dp}}$ and the full
+modular characteristic is
+$\kappa = \kappa_{\mathrm{dp}} + \dim(\fg)/2$. The structure of $r(z)$
 varies by class.
 
 \begin{example}[Class $\mathbf{G}$:
diff --git a/standalone/survey_track_a_compressed.tex b/standalone/survey_track_a_compressed.tex
index cb62bb8b88937153678a962d34c4c5dac04b9700..084c11fb005499137646a882cff6cb86a1becc01
--- a/standalone/survey_track_a_compressed.tex
+++ b/standalone/survey_track_a_compressed.tex
@@ -361,11 +361,17 @@
 \]
 a matrix-valued rational function encoding the full binary OPE data.
 Applying $\mathrm{av}$ at degree~$2$ collapses the profile to a single
-scalar,
+scalar shadow:
 \begin{equation}\label{eq:av-organizing}
-\mathrm{av}\bigl(r(z)\bigr)\;=\;\kappa(\cA),
+\begin{aligned}
+\mathrm{av}\bigl(r(z)\bigr) &= \kappa(\cA)
+&& \text{for abelian and scalar families},\\
+\mathrm{av}\bigl(r(z)\bigr) &= \kappa_{\mathrm{dp}}(\cA), \qquad
+\kappa(\cA) = \kappa_{\mathrm{dp}}(\cA) + \dim(\fg)/2
+&& \text{for non-abelian affine Kac--Moody.}
+\end{aligned}
 \end{equation}
-the modular characteristic of Theorem~D. At degree~$3$ the KZ
+This is the modular characteristic package of Theorem~D. At degree~$3$ the KZ
 associator projects to the cubic shadow~$\mathfrak C$; at degree~$4$
 the Yangian higher coproduct projects to the quartic resonance
 class~$\mathfrak Q$. Each degree-$n$ component of the ordered


thinking
**Inspecting corrections**

I’m thinking about the need to patch both elements and the chiral_chern_weil component. The Shadow_towers_v3 line already references a correction, but I wonder if I can improve the phrasing further. It feels like a good idea to take a closer look at the sections around lines 1846 to 1851 to make those improvements. Let's see what updates might enhance clarity and understanding. This could definitely make the overall output better!
exec
/bin/zsh -lc "sed -n '1846,1852p' standalone/shadow_towers_v3.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
$\Theta_\cA^{E_1}$ projects to~$\Theta_\cA$ under
$\mathrm{av}$. The degree-$2$ component of
$\Theta_\cA^{E_1}$ is the $R$-matrix $r(z)$, and its
average is the modular characteristic~$\kappa$, with the
Sugawara correction for non-abelian algebras arising from
the simple-pole self-contraction of the ordered two-point
function. The higher degrees follow by the same averaging
file update:
diff --git a/chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix b/chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix
index 65cee60eb99d11add7451146de7bb27f5f556dbe..bc2ffa2f7955916ee7be9f7eea55dce5d1e68f9c
--- a/chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix
+++ b/chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix
@@ -3004,8 +3004,11 @@
 is \emph{irrecoverable}: $r(z) = k\,\Omega/z$ carries the
 Casimir tensor
 $\Omega = \sum_a J^a \otimes J_a$ in $\fg \otimes \fg$, but
-$\mathrm{av}(r(z)) = \kappa = \dim(\fg)\cdot(k + h^\vee)/(2h^\vee)$
-is a single scalar.  The Casimir tensor determines the braiding
+$\mathrm{av}(r(z)) = \kappa_{\mathrm{dp}}
+= k\,\dim(\fg)/(2h^\vee)$ and
+$\kappa = \kappa_{\mathrm{dp}} + \dim(\fg)/2
+= \dim(\fg)\cdot(k + h^\vee)/(2h^\vee)$
+is a single scalar shadow. The Casimir tensor determines the braiding
 on the category of representations; the modular
 characteristic determines the genus-$1$ anomaly.  These are
 different structural data at different categorical depths.
diff --git a/chapters/theory/e1_modular_koszul.tex b/chapters/theory/e1_modular_koszul.tex
index a8a83c93d1d8dc248f8f9f6309990c5a7602c6c4..041dea657991f4089b4f0404b429bf3fff9ad079
--- a/chapters/theory/e1_modular_koszul.tex
+++ b/chapters/theory/e1_modular_koszul.tex
@@ -2255,8 +2255,11 @@
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item $(K_\cA^{E_1})_{0,2} = r(z)$, the classical $r$-matrix
  \textup{(}genus~$0$, degree~$2$\textup{)}. The coinvariant
- $\operatorname{av}(r(z)) = \kappa(\cA)$ recovers the scalar
- curvature.
+ $\operatorname{av}(r(z))$ recovers the scalar degree-$2$ shadow:
+ on abelian families $\operatorname{av}(r(z)) = \kappa(\cA)$,
+ while for non-abelian affine Kac--Moody
+ $\operatorname{av}(r(z)) = \kappa_{\mathrm{dp}}(\cA)$ and
+ $\kappa(\cA) = \kappa_{\mathrm{dp}}(\cA) + \dim(\fg)/2$.
 \item $(K_\cA^{E_1})_{0,3} = \Phi_{\mathrm{KZ}}(\cA)$, the
  KZ\slash Drinfeld associator \textup{(}genus~$0$, degree~$3$,
  for affine algebras;
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 789ce9acf5b68f150a665afd1b7486e6b1256a16..f5fd9aa34b7bb56449ed56b583ce3f595c37ce5f
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -895,8 +895,12 @@
 
 \item \emph{Leading-order modular shadow.}
  The $\Sigma_2$-coinvariant projection
- $\operatorname{av}(r(z)) = \kappa(\cA)$ is the modular
- characteristic, the first entry of the shadow obstruction tower
+ $\operatorname{av}(r(z))$ is the leading scalar shadow: it equals
+ $\kappa(\cA)$ on abelian and scalar families, while for
+ non-abelian affine Kac--Moody it gives
+ $\kappa_{\mathrm{dp}}(\cA)$ and the full modular characteristic is
+ $\kappa(\cA) = \kappa_{\mathrm{dp}}(\cA) + \dim(\fg)/2$. This is
+ the first entry of the shadow obstruction tower
  \textup{(}equation~\textup{\eqref{eq:intro-kappa-from-r}};
  Theorem~\textup{\ref{thm:e1-primacy}}\textup{)}. The residue contains
  a matrix-valued refinement; averaging produces the scalar.
@@ -1262,17 +1266,18 @@
 \;=\;
 \Theta_\cA.
 \end{equation}
-At degree~$2$, this projection records only one number: the
-$\Sigma_2$-coinvariant of the residue of $r(z)$ at $z = 0$ is the
-modular characteristic
+At degree~$2$, this projection records only one scalar: the
+$\Sigma_2$-coinvariant of the residue of $r(z)$ at $z = 0$ is
 \begin{equation}\label{eq:intro-kappa-from-r}
-\kappa(\cA)
-\;=\;
 \operatorname{av}\bigl(r(z)\bigr)
 \;=\;
 \tfrac{1}{2}\,\operatorname{tr}\!\bigl[\Res_{z = 0} r(z)\bigr],
 \end{equation}
 where the trace is the cyclic trace on $\End(V^{\otimes 2})$.
+For abelian and scalar families,
+\[
+\kappa(\cA) = \operatorname{av}\bigl(r(z)\bigr).
+\]
 For the affine Kac--Moody vacuum algebra $V_k(\mathfrak{g})$ at
 non-critical level, the averaging formula
 \eqref{eq:intro-kappa-from-r} specializes to the Sugawara identity
diff --git a/standalone/shadow_towers_v3.tex b/standalone/shadow_towers_v3.tex
index 3e3cf779de2c8653d94026ee31a290ce83cfcba7..a5a7647da40e9a191f1addc0af5dafd181ae7a1c
--- a/standalone/shadow_towers_v3.tex
+++ b/standalone/shadow_towers_v3.tex
@@ -1873,7 +1873,11 @@
 The $E_1$ convolution algebra
 $\mathfrak{g}^{E_1}_\cA$ carries a spectral $R$-matrix
 $r(z) \in \mathrm{End}(V \otimes V)((z))$ at degree~$2$,
-whose averaging produces~$\kappa$. The structure of $r(z)$
+whose averaging produces the scalar degree-$2$ shadow:
+for abelian families this is~$\kappa$, while for non-abelian
+affine Kac--Moody it is~$\kappa_{\mathrm{dp}}$ and the full
+modular characteristic is
+$\kappa = \kappa_{\mathrm{dp}} + \dim(\fg)/2$. The structure of $r(z)$
 varies by class.
 
 \begin{example}[Class $\mathbf{G}$:
diff --git a/standalone/survey_track_a_compressed.tex b/standalone/survey_track_a_compressed.tex
index cb62bb8b88937153678a962d34c4c5dac04b9700..084c11fb005499137646a882cff6cb86a1becc01
--- a/standalone/survey_track_a_compressed.tex
+++ b/standalone/survey_track_a_compressed.tex
@@ -361,11 +361,17 @@
 \]
 a matrix-valued rational function encoding the full binary OPE data.
 Applying $\mathrm{av}$ at degree~$2$ collapses the profile to a single
-scalar,
+scalar shadow:
 \begin{equation}\label{eq:av-organizing}
-\mathrm{av}\bigl(r(z)\bigr)\;=\;\kappa(\cA),
+\begin{aligned}
+\mathrm{av}\bigl(r(z)\bigr) &= \kappa(\cA)
+&& \text{for abelian and scalar families},\\
+\mathrm{av}\bigl(r(z)\bigr) &= \kappa_{\mathrm{dp}}(\cA), \qquad
+\kappa(\cA) = \kappa_{\mathrm{dp}}(\cA) + \dim(\fg)/2
+&& \text{for non-abelian affine Kac--Moody.}
+\end{aligned}
 \end{equation}
-the modular characteristic of Theorem~D. At degree~$3$ the KZ
+This is the modular characteristic package of Theorem~D. At degree~$3$ the KZ
 associator projects to the cubic shadow~$\mathfrak C$; at degree~$4$
 the Yangian higher coproduct projects to the quartic resonance
 class~$\mathfrak Q$. Each degree-$n$ component of the ordered


thinking
**Patching calculations**

I’m considering how to make my approach more precise. The average acts as a scalar shadow, which is equal to κ in abelian families. For the non-abelian affine case, the full κ incorporates the Sugawara correction. I need to address this by patching my computations. Also, I should revise the `introduction` line at 1660. So, it looks like I have a few key patches to handle here!
file update
M /Users/raeez/chiral-bar-cobar/standalone/shadow_towers_v3.tex
@@ -1848,6 +1848,8 @@
 $\Theta_\cA^{E_1}$ is the $R$-matrix $r(z)$, and its
-average is the modular characteristic~$\kappa$, with the
-Sugawara correction for non-abelian algebras arising from
-the simple-pole self-contraction of the ordered two-point
-function. The higher degrees follow by the same averaging
+average is the scalar degree-$2$ shadow: it equals the modular
+characteristic~$\kappa$ on abelian families, while for
+non-abelian affine Kac--Moody the average is
+$\kappa_{\mathrm{dp}}$ and the full~$\kappa$ adds the
+Sugawara correction from the simple-pole self-contraction of the
+ordered two-point function. The higher degrees follow by the same averaging
 applied to the degree-$r$ MC components.
M /Users/raeez/chiral-bar-cobar/chapters/theory/introduction.tex
@@ -1659,4 +1659,7 @@
 Volume~II: the algebra is commutative up to quasi-isomorphism, and
-averaging recovers the modular shadow $\kappa$ without information
-loss beyond the $\Sigma_n$-coinvariant step.
+averaging recovers the scalar degree-$2$ shadow without
+information loss beyond the $\Sigma_n$-coinvariant step: this is
+$\kappa$ on abelian and scalar families, while for non-abelian
+affine Kac--Moody it is $\kappa_{\mathrm{dp}}$ and the full
+modular characteristic adds the Sugawara shift $\dim(\fg)/2$.
 
M /Users/raeez/chiral-bar-cobar/standalone/chiral_chern_weil.tex
@@ -1215,3 +1215,7 @@
 
-The averaging map extracts~$\kappa$ from the $r$-matrix.
+The averaging map extracts the scalar degree-$2$ shadow from the
+$r$-matrix: this is~$\kappa$ on abelian and scalar families, while
+for non-abelian affine Kac--Moody the averaged scalar is
+$\kappa_{\mathrm{cl}}$ and the full modular characteristic is
+$\kappa = \kappa_{\mathrm{cl}} + \dim(\fg)/2$.
 The question it forces is: what role does~$\kappa$ play
apply_patch(auto_approved=true) exited 0 in 52ms:
Success. Updated the following files:
M standalone/chiral_chern_weil.tex
M standalone/shadow_towers_v3.tex
M chapters/theory/introduction.tex
file update:
diff --git a/chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix b/chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix
index 65cee60eb99d11add7451146de7bb27f5f556dbe..bc2ffa2f7955916ee7be9f7eea55dce5d1e68f9c
--- a/chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix
+++ b/chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix
@@ -3004,8 +3004,11 @@
 is \emph{irrecoverable}: $r(z) = k\,\Omega/z$ carries the
 Casimir tensor
 $\Omega = \sum_a J^a \otimes J_a$ in $\fg \otimes \fg$, but
-$\mathrm{av}(r(z)) = \kappa = \dim(\fg)\cdot(k + h^\vee)/(2h^\vee)$
-is a single scalar.  The Casimir tensor determines the braiding
+$\mathrm{av}(r(z)) = \kappa_{\mathrm{dp}}
+= k\,\dim(\fg)/(2h^\vee)$ and
+$\kappa = \kappa_{\mathrm{dp}} + \dim(\fg)/2
+= \dim(\fg)\cdot(k + h^\vee)/(2h^\vee)$
+is a single scalar shadow. The Casimir tensor determines the braiding
 on the category of representations; the modular
 characteristic determines the genus-$1$ anomaly.  These are
 different structural data at different categorical depths.
diff --git a/chapters/theory/e1_modular_koszul.tex b/chapters/theory/e1_modular_koszul.tex
index a8a83c93d1d8dc248f8f9f6309990c5a7602c6c4..041dea657991f4089b4f0404b429bf3fff9ad079
--- a/chapters/theory/e1_modular_koszul.tex
+++ b/chapters/theory/e1_modular_koszul.tex
@@ -2255,8 +2255,11 @@
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item $(K_\cA^{E_1})_{0,2} = r(z)$, the classical $r$-matrix
  \textup{(}genus~$0$, degree~$2$\textup{)}. The coinvariant
- $\operatorname{av}(r(z)) = \kappa(\cA)$ recovers the scalar
- curvature.
+ $\operatorname{av}(r(z))$ recovers the scalar degree-$2$ shadow:
+ on abelian families $\operatorname{av}(r(z)) = \kappa(\cA)$,
+ while for non-abelian affine Kac--Moody
+ $\operatorname{av}(r(z)) = \kappa_{\mathrm{dp}}(\cA)$ and
+ $\kappa(\cA) = \kappa_{\mathrm{dp}}(\cA) + \dim(\fg)/2$.
 \item $(K_\cA^{E_1})_{0,3} = \Phi_{\mathrm{KZ}}(\cA)$, the
  KZ\slash Drinfeld associator \textup{(}genus~$0$, degree~$3$,
  for affine algebras;
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 789ce9acf5b68f150a665afd1b7486e6b1256a16..09413d565658e9d71f63d7dd7327bf183c8a1ea7
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -895,8 +895,12 @@
 
 \item \emph{Leading-order modular shadow.}
  The $\Sigma_2$-coinvariant projection
- $\operatorname{av}(r(z)) = \kappa(\cA)$ is the modular
- characteristic, the first entry of the shadow obstruction tower
+ $\operatorname{av}(r(z))$ is the leading scalar shadow: it equals
+ $\kappa(\cA)$ on abelian and scalar families, while for
+ non-abelian affine Kac--Moody it gives
+ $\kappa_{\mathrm{dp}}(\cA)$ and the full modular characteristic is
+ $\kappa(\cA) = \kappa_{\mathrm{dp}}(\cA) + \dim(\fg)/2$. This is
+ the first entry of the shadow obstruction tower
  \textup{(}equation~\textup{\eqref{eq:intro-kappa-from-r}};
  Theorem~\textup{\ref{thm:e1-primacy}}\textup{)}. The residue contains
  a matrix-valued refinement; averaging produces the scalar.
@@ -1262,17 +1266,18 @@
 \;=\;
 \Theta_\cA.
 \end{equation}
-At degree~$2$, this projection records only one number: the
-$\Sigma_2$-coinvariant of the residue of $r(z)$ at $z = 0$ is the
-modular characteristic
+At degree~$2$, this projection records only one scalar: the
+$\Sigma_2$-coinvariant of the residue of $r(z)$ at $z = 0$ is
 \begin{equation}\label{eq:intro-kappa-from-r}
-\kappa(\cA)
-\;=\;
 \operatorname{av}\bigl(r(z)\bigr)
 \;=\;
 \tfrac{1}{2}\,\operatorname{tr}\!\bigl[\Res_{z = 0} r(z)\bigr],
 \end{equation}
 where the trace is the cyclic trace on $\End(V^{\otimes 2})$.
+For abelian and scalar families,
+\[
+\kappa(\cA) = \operatorname{av}\bigl(r(z)\bigr).
+\]
 For the affine Kac--Moody vacuum algebra $V_k(\mathfrak{g})$ at
 non-critical level, the averaging formula
 \eqref{eq:intro-kappa-from-r} specializes to the Sugawara identity
@@ -1652,8 +1657,11 @@
 at the $R$-matrix level beyond what the local OPE already carries.
 Tier (b) is still $\Einf$-chiral in the three-leaps classification of
 Volume~II: the algebra is commutative up to quasi-isomorphism, and
-averaging recovers the modular shadow $\kappa$ without information
-loss beyond the $\Sigma_n$-coinvariant step.
+averaging recovers the scalar degree-$2$ shadow without
+information loss beyond the $\Sigma_n$-coinvariant step: this is
+$\kappa$ on abelian and scalar families, while for non-abelian
+affine Kac--Moody it is $\kappa_{\mathrm{dp}}$ and the full
+modular characteristic adds the Sugawara shift $\dim(\fg)/2$.
 
 Tier (c) is the genuinely $\Eone$-primitive extreme. The Yangian
 $Y(\mathfrak g)$ and the Etingof--Kazhdan quantum vertex algebras
diff --git a/standalone/chiral_chern_weil.tex b/standalone/chiral_chern_weil.tex
index 264bc812bc756f693683ea49fffc92a69ba23fb8..e925297230a043684b2162d6eea950832e71b362
--- a/standalone/chiral_chern_weil.tex
+++ b/standalone/chiral_chern_weil.tex
@@ -1213,7 +1213,11 @@
 % ================================================================
 \section{The chiral curvature}\label{sec:chiral-cw}
 
-The averaging map extracts~$\kappa$ from the $r$-matrix.
+The averaging map extracts the scalar degree-$2$ shadow from the
+$r$-matrix: this is~$\kappa$ on abelian and scalar families, while
+for non-abelian affine Kac--Moody the averaged scalar is
+$\kappa_{\mathrm{cl}}$ and the full modular characteristic is
+$\kappa = \kappa_{\mathrm{cl}} + \dim(\fg)/2$.
 The question it forces is: what role does~$\kappa$ play
 geometrically? The answer: $\kappa$ is the proportionality
 constant of a curvature. The bar differential, which squares
diff --git a/standalone/shadow_towers_v3.tex b/standalone/shadow_towers_v3.tex
index 3e3cf779de2c8653d94026ee31a290ce83cfcba7..12a1cee9e29af47da9fba8082a62d08db7d85eb3
--- a/standalone/shadow_towers_v3.tex
+++ b/standalone/shadow_towers_v3.tex
@@ -1846,10 +1846,12 @@
 $\Theta_\cA^{E_1}$ projects to~$\Theta_\cA$ under
 $\mathrm{av}$. The degree-$2$ component of
 $\Theta_\cA^{E_1}$ is the $R$-matrix $r(z)$, and its
-average is the modular characteristic~$\kappa$, with the
-Sugawara correction for non-abelian algebras arising from
-the simple-pole self-contraction of the ordered two-point
-function. The higher degrees follow by the same averaging
+average is the scalar degree-$2$ shadow: it equals the modular
+characteristic~$\kappa$ on abelian families, while for
+non-abelian affine Kac--Moody the average is
+$\kappa_{\mathrm{dp}}$ and the full~$\kappa$ adds the
+Sugawara correction from the simple-pole self-contraction of the
+ordered two-point function. The higher degrees follow by the same averaging
 applied to the degree-$r$ MC components.
 \end{proof}
 
@@ -1873,7 +1875,11 @@
 The $E_1$ convolution algebra
 $\mathfrak{g}^{E_1}_\cA$ carries a spectral $R$-matrix
 $r(z) \in \mathrm{End}(V \otimes V)((z))$ at degree~$2$,
-whose averaging produces~$\kappa$. The structure of $r(z)$
+whose averaging produces the scalar degree-$2$ shadow:
+for abelian families this is~$\kappa$, while for non-abelian
+affine Kac--Moody it is~$\kappa_{\mathrm{dp}}$ and the full
+modular characteristic is
+$\kappa = \kappa_{\mathrm{dp}} + \dim(\fg)/2$. The structure of $r(z)$
 varies by class.
 
 \begin{example}[Class $\mathbf{G}$:
diff --git a/standalone/survey_track_a_compressed.tex b/standalone/survey_track_a_compressed.tex
index cb62bb8b88937153678a962d34c4c5dac04b9700..084c11fb005499137646a882cff6cb86a1becc01
--- a/standalone/survey_track_a_compressed.tex
+++ b/standalone/survey_track_a_compressed.tex
@@ -361,11 +361,17 @@
 \]
 a matrix-valued rational function encoding the full binary OPE data.
 Applying $\mathrm{av}$ at degree~$2$ collapses the profile to a single
-scalar,
+scalar shadow:
 \begin{equation}\label{eq:av-organizing}
-\mathrm{av}\bigl(r(z)\bigr)\;=\;\kappa(\cA),
+\begin{aligned}
+\mathrm{av}\bigl(r(z)\bigr) &= \kappa(\cA)
+&& \text{for abelian and scalar families},\\
+\mathrm{av}\bigl(r(z)\bigr) &= \kappa_{\mathrm{dp}}(\cA), \qquad
+\kappa(\cA) = \kappa_{\mathrm{dp}}(\cA) + \dim(\fg)/2
+&& \text{for non-abelian affine Kac--Moody.}
+\end{aligned}
 \end{equation}
-the modular characteristic of Theorem~D. At degree~$3$ the KZ
+This is the modular characteristic package of Theorem~D. At degree~$3$ the KZ
 associator projects to the cubic shadow~$\mathfrak C$; at degree~$4$
 the Yangian higher coproduct projects to the quartic resonance
 class~$\mathfrak Q$. Each degree-$n$ component of the ordered

file update:
diff --git a/chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix b/chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix
index 65cee60eb99d11add7451146de7bb27f5f556dbe..bc2ffa2f7955916ee7be9f7eea55dce5d1e68f9c
--- a/chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix
+++ b/chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix
@@ -3004,8 +3004,11 @@
 is \emph{irrecoverable}: $r(z) = k\,\Omega/z$ carries the
 Casimir tensor
 $\Omega = \sum_a J^a \otimes J_a$ in $\fg \otimes \fg$, but
-$\mathrm{av}(r(z)) = \kappa = \dim(\fg)\cdot(k + h^\vee)/(2h^\vee)$
-is a single scalar.  The Casimir tensor determines the braiding
+$\mathrm{av}(r(z)) = \kappa_{\mathrm{dp}}
+= k\,\dim(\fg)/(2h^\vee)$ and
+$\kappa = \kappa_{\mathrm{dp}} + \dim(\fg)/2
+= \dim(\fg)\cdot(k + h^\vee)/(2h^\vee)$
+is a single scalar shadow. The Casimir tensor determines the braiding
 on the category of representations; the modular
 characteristic determines the genus-$1$ anomaly.  These are
 different structural data at different categorical depths.
diff --git a/chapters/theory/e1_modular_koszul.tex b/chapters/theory/e1_modular_koszul.tex
index a8a83c93d1d8dc248f8f9f6309990c5a7602c6c4..041dea657991f4089b4f0404b429bf3fff9ad079
--- a/chapters/theory/e1_modular_koszul.tex
+++ b/chapters/theory/e1_modular_koszul.tex
@@ -2255,8 +2255,11 @@
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item $(K_\cA^{E_1})_{0,2} = r(z)$, the classical $r$-matrix
  \textup{(}genus~$0$, degree~$2$\textup{)}. The coinvariant
- $\operatorname{av}(r(z)) = \kappa(\cA)$ recovers the scalar
- curvature.
+ $\operatorname{av}(r(z))$ recovers the scalar degree-$2$ shadow:
+ on abelian families $\operatorname{av}(r(z)) = \kappa(\cA)$,
+ while for non-abelian affine Kac--Moody
+ $\operatorname{av}(r(z)) = \kappa_{\mathrm{dp}}(\cA)$ and
+ $\kappa(\cA) = \kappa_{\mathrm{dp}}(\cA) + \dim(\fg)/2$.
 \item $(K_\cA^{E_1})_{0,3} = \Phi_{\mathrm{KZ}}(\cA)$, the
  KZ\slash Drinfeld associator \textup{(}genus~$0$, degree~$3$,
  for affine algebras;
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 789ce9acf5b68f150a665afd1b7486e6b1256a16..09413d565658e9d71f63d7dd7327bf183c8a1ea7
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -895,8 +895,12 @@
 
 \item \emph{Leading-order modular shadow.}
  The $\Sigma_2$-coinvariant projection
- $\operatorname{av}(r(z)) = \kappa(\cA)$ is the modular
- characteristic, the first entry of the shadow obstruction tower
+ $\operatorname{av}(r(z))$ is the leading scalar shadow: it equals
+ $\kappa(\cA)$ on abelian and scalar families, while for
+ non-abelian affine Kac--Moody it gives
+ $\kappa_{\mathrm{dp}}(\cA)$ and the full modular characteristic is
+ $\kappa(\cA) = \kappa_{\mathrm{dp}}(\cA) + \dim(\fg)/2$. This is
+ the first entry of the shadow obstruction tower
  \textup{(}equation~\textup{\eqref{eq:intro-kappa-from-r}};
  Theorem~\textup{\ref{thm:e1-primacy}}\textup{)}. The residue contains
  a matrix-valued refinement; averaging produces the scalar.
@@ -1262,17 +1266,18 @@
 \;=\;
 \Theta_\cA.
 \end{equation}
-At degree~$2$, this projection records only one number: the
-$\Sigma_2$-coinvariant of the residue of $r(z)$ at $z = 0$ is the
-modular characteristic
+At degree~$2$, this projection records only one scalar: the
+$\Sigma_2$-coinvariant of the residue of $r(z)$ at $z = 0$ is
 \begin{equation}\label{eq:intro-kappa-from-r}
-\kappa(\cA)
-\;=\;
 \operatorname{av}\bigl(r(z)\bigr)
 \;=\;
 \tfrac{1}{2}\,\operatorname{tr}\!\bigl[\Res_{z = 0} r(z)\bigr],
 \end{equation}
 where the trace is the cyclic trace on $\End(V^{\otimes 2})$.
+For abelian and scalar families,
+\[
+\kappa(\cA) = \operatorname{av}\bigl(r(z)\bigr).
+\]
 For the affine Kac--Moody vacuum algebra $V_k(\mathfrak{g})$ at
 non-critical level, the averaging formula
 \eqref{eq:intro-kappa-from-r} specializes to the Sugawara identity
@@ -1652,8 +1657,11 @@
 at the $R$-matrix level beyond what the local OPE already carries.
 Tier (b) is still $\Einf$-chiral in the three-leaps classification of
 Volume~II: the algebra is commutative up to quasi-isomorphism, and
-averaging recovers the modular shadow $\kappa$ without information
-loss beyond the $\Sigma_n$-coinvariant step.
+averaging recovers the scalar degree-$2$ shadow without
+information loss beyond the $\Sigma_n$-coinvariant step: this is
+$\kappa$ on abelian and scalar families, while for non-abelian
+affine Kac--Moody it is $\kappa_{\mathrm{dp}}$ and the full
+modular characteristic adds the Sugawara shift $\dim(\fg)/2$.
 
 Tier (c) is the genuinely $\Eone$-primitive extreme. The Yangian
 $Y(\mathfrak g)$ and the Etingof--Kazhdan quantum vertex algebras
diff --git a/standalone/chiral_chern_weil.tex b/standalone/chiral_chern_weil.tex
index 264bc812bc756f693683ea49fffc92a69ba23fb8..e925297230a043684b2162d6eea950832e71b362
--- a/standalone/chiral_chern_weil.tex
+++ b/standalone/chiral_chern_weil.tex
@@ -1213,7 +1213,11 @@
 % ================================================================
 \section{The chiral curvature}\label{sec:chiral-cw}
 
-The averaging map extracts~$\kappa$ from the $r$-matrix.
+The averaging map extracts the scalar degree-$2$ shadow from the
+$r$-matrix: this is~$\kappa$ on abelian and scalar families, while
+for non-abelian affine Kac--Moody the averaged scalar is
+$\kappa_{\mathrm{cl}}$ and the full modular characteristic is
+$\kappa = \kappa_{\mathrm{cl}} + \dim(\fg)/2$.
 The question it forces is: what role does~$\kappa$ play
 geometrically? The answer: $\kappa$ is the proportionality
 constant of a curvature. The bar differential, which squares
diff --git a/standalone/shadow_towers_v3.tex b/standalone/shadow_towers_v3.tex
index 3e3cf779de2c8653d94026ee31a290ce83cfcba7..12a1cee9e29af47da9fba8082a62d08db7d85eb3
--- a/standalone/shadow_towers_v3.tex
+++ b/standalone/shadow_towers_v3.tex
@@ -1846,10 +1846,12 @@
 $\Theta_\cA^{E_1}$ projects to~$\Theta_\cA$ under
 $\mathrm{av}$. The degree-$2$ component of
 $\Theta_\cA^{E_1}$ is the $R$-matrix $r(z)$, and its
-average is the modular characteristic~$\kappa$, with the
-Sugawara correction for non-abelian algebras arising from
-the simple-pole self-contraction of the ordered two-point
-function. The higher degrees follow by the same averaging
+average is the scalar degree-$2$ shadow: it equals the modular
+characteristic~$\kappa$ on abelian families, while for
+non-abelian affine Kac--Moody the average is
+$\kappa_{\mathrm{dp}}$ and the full~$\kappa$ adds the
+Sugawara correction from the simple-pole self-contraction of the
+ordered two-point function. The higher degrees follow by the same averaging
 applied to the degree-$r$ MC components.
 \end{proof}
 
@@ -1873,7 +1875,11 @@
 The $E_1$ convolution algebra
 $\mathfrak{g}^{E_1}_\cA$ carries a spectral $R$-matrix
 $r(z) \in \mathrm{End}(V \otimes V)((z))$ at degree~$2$,
-whose averaging produces~$\kappa$. The structure of $r(z)$
+whose averaging produces the scalar degree-$2$ shadow:
+for abelian families this is~$\kappa$, while for non-abelian
+affine Kac--Moody it is~$\kappa_{\mathrm{dp}}$ and the full
+modular characteristic is
+$\kappa = \kappa_{\mathrm{dp}} + \dim(\fg)/2$. The structure of $r(z)$
 varies by class.
 
 \begin{example}[Class $\mathbf{G}$:
diff --git a/standalone/survey_track_a_compressed.tex b/standalone/survey_track_a_compressed.tex
index cb62bb8b88937153678a962d34c4c5dac04b9700..084c11fb005499137646a882cff6cb86a1becc01
--- a/standalone/survey_track_a_compressed.tex
+++ b/standalone/survey_track_a_compressed.tex
@@ -361,11 +361,17 @@
 \]
 a matrix-valued rational function encoding the full binary OPE data.
 Applying $\mathrm{av}$ at degree~$2$ collapses the profile to a single
-scalar,
+scalar shadow:
 \begin{equation}\label{eq:av-organizing}
-\mathrm{av}\bigl(r(z)\bigr)\;=\;\kappa(\cA),
+\begin{aligned}
+\mathrm{av}\bigl(r(z)\bigr) &= \kappa(\cA)
+&& \text{for abelian and scalar families},\\
+\mathrm{av}\bigl(r(z)\bigr) &= \kappa_{\mathrm{dp}}(\cA), \qquad
+\kappa(\cA) = \kappa_{\mathrm{dp}}(\cA) + \dim(\fg)/2
+&& \text{for non-abelian affine Kac--Moody.}
+\end{aligned}
 \end{equation}
-the modular characteristic of Theorem~D. At degree~$3$ the KZ
+This is the modular characteristic package of Theorem~D. At degree~$3$ the KZ
 associator projects to the cubic shadow~$\mathfrak C$; at degree~$4$
 the Yangian higher coproduct projects to the quartic resonance
 class~$\mathfrak Q$. Each degree-$n$ component of the ordered


thinking
**Executing a search command**

I need to re-run a grep command in the current repository. I might also want to search for any lingering generic wrong surfaces. To be thorough, I'll run a search using `rg` and look for the specific phrase `av(r(z)) = \kappa`, as well as more generic phrases. It's all about making sure I catch everything necessary!
codex
The last loose prose is patched. I’m running the final in-repo grep now; at this point, anything remaining should either be abelian-only, explicitly corrected, or not in the writable tree.
exec
/bin/zsh -lc "rg -n -i 'av.*r.*kappa|averaging.*kappa' /Users/raeez/calabi-yau-quantum-groups/chapters | head -30" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -i 'av.*r.*kappa|averaging.*kappa' /Users/raeez/chiral-bar-cobar-vol2/chapters /Users/raeez/chiral-bar-cobar-vol2/standalone | head -30" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg --pcre2 -n -C 1 '\\\\(?:av|mathrm\\{av\\}|operatorname\\{av\\})\\s*\\(r(?:_0)?\\(z\\)\\)\\s*=\\s*\\\\kappa(?:\\(["'^)]*'"\\))?(?"'!_)|averag[a-z]*[''^'"\\n]{0,120}\\\\kappa(?:\\(["'^)]*'"\\))?(?"'!_)|average is the modular characteristic|extracts~'"\\\\kappa from the \\\\"'$r'"\\\\"'$-matrix|averaging recovers the modular shadow '"\\\\kappa' chapters standalone" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:568:%: av is lossy. The R-matrix r(z) has more information than kappa.
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:5194:The identity $\DT = \mathrm{PT}$ for $K3 \times E$ means that the contribution of zero-dimensional sheaves (the MacMahon sector) is invisible. This is the enumerative counterpart of the vanishing $\chi(X) = 0$: the degree-$0$ virtual class is trivial. Note: the chiral algebra modular characteristic $\kappa_{\mathrm{ch}}(K3 \times E) = 3$ (Section~\ref{sec:k3e-cross-volume}, K3-1) does \emph{not} vanish; the vanishing $\chi/12 = 0$ is a virtual/enumerative statement, not a shadow tower statement. The nontrivial enumerative content resides entirely in curve-class contributions, organized by the Borcherds product (Theorem~\ref{thm:k3e-product}).
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/bar_cobar_bridge.tex:235:The following compact CY$_3$ families illustrate the range of shadow tower behaviour. In each case, the predicted modular characteristic is $\kappa_{\mathrm{ch}} = \chi_{\mathrm{top}} / 24$ (BCOV prediction); the shadow depth class, Hochschild data, and BKM structure vary.
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/bar_cobar_bridge.tex:517: \item \textbf{$\kappa_{\mathrm{ch}}$ integrality}: among the atlas families, $\mathbb{P}^5[3,3]$ ($\kappa_{\mathrm{ch}} = -6$), K3 $\times\, E$ ($\kappa_{\mathrm{BKM}} = 5$), Enriques $\times\, E$ ($\kappa_{\mathrm{BKM}} = 4$), and BV$(20,2,0)$ ($\kappa_{\mathrm{ch}} = 5$) have integral $\kappa_{\mathrm{ch}}$. For compact CICYs, $\kappa_{\mathrm{ch}} = \chi/24$ is integral only when $24 \mid \chi$; for K3-fibered geometries, $\kappa_{\mathrm{BKM}}$ (the automorphic weight) is always integral.
/Users/raeez/calabi-yau-quantum-groups/chapters/frame/preface.tex:460:structure via averaging $\mathrm{av}(r(z)) = \kappa_{\mathrm{ch}}$.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex:23:This averaging is \emph{lossy}: $\mathrm{av}(r(z)) = \kappa_{\mathrm{ch}}$ forgets the
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex:122:is a morphism of cochain complexes and sends the $E_1$ structure to the $E_\infty$ structure. It is lossy: the kernel contains the $R$-matrix data of the holomorphic factor, and on degree two $\mathrm{av}(r(z)) = \kappa_{\mathrm{ch}}$.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex:127:Averaging the degree-two generator $r(z)$ returns the scalar $\kappa_{\mathrm{ch}}$, the unique $S_2$-coinvariant of the collision residue. When the same $r(z)$ comes from the CY-to-chiral functor applied to $D^b(\Coh(K3 \times E))$, the scalar is $\kappa_{\mathrm{ch}} = 3$ by additivity: $\kappa_{\mathrm{ch}}(K3) + \kappa_{\mathrm{ch}}(E) = 2 + 1$. This differs from the categorical Euler characteristic $\kappa_{\mathrm{cat}} = 2$, the lattice-rank invariant $\kappa_{\mathrm{fiber}} = 24$, and the BKM weight $\kappa_{\mathrm{BKM}} = 5$. An unsubscripted symbol would conflate distinct invariants.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex:131:The CY-to-chiral functor $\Phi$ of Chapter~\ref{ch:cy-to-chiral} has three natural composites. $\Phi_{E_1}$ produces $B^{\mathrm{ord}}(A_C)$; this is the ordered bar sensed by the Yangian. $\mathrm{av} \circ \Phi_{E_1}$ produces $B^{\Sigma}(A_C)$; this is the symmetric bar sensed by the modular characteristic $\kappa_{\mathrm{ch}}$. The full $E_2$ enhancement $\Phi_{E_2}$ produces the Drinfeld-centered bar $B^{E_2}(A_C) = \cZ(B^{\mathrm{ord}}(A_C))$; this is the braided bar sensed by the quantum group. All three factor through $\Phi_{E_1}$. In this volume, the ordered bar is the primitive object.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex:202: ($\mathrm{av}(r(z)) = \kappa_{\mathrm{ch}}$) \\
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex:261: $\mathrm{av}(R(z))|_{z=0} = \kappa_{\mathrm{ch}} \cdot \mathrm{id}$.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex:316:The three volumes are three faces of a single $E_1$-$E_1$ operadic Koszul duality. Volume~I is the symmetric modular face: it develops $B^{\Sigma}$, the five theorems A-D+H, and the modular characteristic $\kappa_{\mathrm{ch}}$ in the uniform-weight setting. Volume~II is the $E_1$ open-colour face: it develops $B^{\mathrm{ord}}$, the Swiss-cheese operad, the $r(z)$-matrix with its seven faces, and the three-dimensional holomorphic-topological bridge to quantum gravity. Volume~III is the CY-geometric face: it develops the functor $\Phi$ that produces the input algebra from a Calabi-Yau category, identifies $\kappa_{\mathrm{ch}}$ within the kappa-spectrum, and traces the quantum group back to its geometric origin in BPS state counts.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex:345:The three volumes use different coalgebra conventions in their displayed formulas. Vol~I displays formulas in $B^{\Sigma}$ with the symmetric coproduct; Vol~II displays formulas in $B^{\mathrm{ord}}$ with deconcatenation; Vol~III displays formulas in whichever form the CY functor produces, which is always $B^{\mathrm{ord}}$ at the source but frequently $B^{\Sigma}$ after averaging to extract $\kappa_{\mathrm{ch}}$. The reader who cross-references a formula between volumes must convert between the three coalgebra structures: $B^{\mathrm{ord}} \to B^{\Sigma}$ by averaging (dividing by $n!$ and symmetrizing), and $B^{\Sigma} \to B^{\mathrm{Lie}}$ by taking the iterated commutator of the cofree tensor coalgebra. The three bars are NOT isomorphic even as complexes; they differ by $S_n$-coinvariant quotients, and the Euler characters diverge accordingly. See Vol~II for the three-bar sequence.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex:1087: $\mathrm{av}(r(z)) = \kappa_{\mathrm{ch}}$ (a scalar), so the full
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex:1355:$\mathrm{av}(r(z)) = \kappa_{\mathrm{ch}}$: the full
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex:1371:$R$-matrix & $r(z) = k\,\Omega/z + \cdots$ & $R^{E_2}(z)$ (half-braiding) & $\mathrm{av}(r(z)) = \kappa_{\mathrm{ch}}$ (scalar) \\
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex:1384:transition (averaging) collapses $r(z)$ to $\kappa_{\mathrm{ch}}$
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex:1598:Four facts control the later parts of Vol~III. First, factorization algebras on a complex curve are $E_2$ topologically but specialize to $E_1$ when holomorphy fixes an ordering, and the Swiss-cheese splitting $E_1(C) \times E_2(\mathrm{top})$ makes that specialization precise. Second, the ordered bar complex $B^{\mathrm{ord}}(A) = T^c(s^{-1}\bar A)$ with deconcatenation coproduct is the natural $E_1$ primitive, and averaging to the symmetric bar $B^{\Sigma}(A)$ is lossy because it kills the ordered $R$-matrix data. Third, the CY-to-chiral functor $\Phi$ at $d=2$ produces an ordered bar whose Euler character is the Borcherds denominator and whose first shadow invariant is $\kappa_{\mathrm{ch}}$, distinct from $\kappa_{\mathrm{BKM}}$, $\kappa_{\mathrm{cat}}$, and $\kappa_{\mathrm{fiber}}$. Fourth, the $E_2$ enhancement requires the Drinfeld center construction, the categorified averaging map $E_1\text{-Cat} \to E_2\text{-Cat}$; at $d=3$ the enhancement is conditional on the CY-A$_3$ programme.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/drinfeld_center.tex:702:$\mathrm{av}(r(z)) = \kappa_{\mathrm{ch}}$ extracts the scalar
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex:1770:\noindent Three remarks on the table entries. First, $K3 \times E$ does not have a quiver atlas in the strict sense of Definition~\ref{def:quiver-chart-atlas}: the derived category $D^b(\Coh(K3 \times E))$ does not admit a single tilting generator, and the fibration structure requires a different gluing mechanism (the relative Fourier--Mukai, see Chapter~\ref{ch:k3-times-e}). The table records $\kappa_{\mathrm{ch}} = 3$ by additivity ($\kappa_{\mathrm{ch}}(\mathrm{K3}) + \kappa_{\mathrm{ch}}(E) = 2 + 1$, Proposition~\ref{prop:categorical-euler}); the distinct Borcherds automorphic weight is $\kappa_{\mathrm{BKM}} = 5 = \mathrm{wt}(\Delta_5)$. Second, the quintic has $|I| = 2$ charts: one at large volume (a quiver chart from the Beilinson collection restricted to $X$) and one at the Gepner point (a matrix factorization category $\MF(W_{\mathrm{Fermat}})$, which is NOT a quiver chart; see Remark~\ref{rem:gepner-lv-dichotomy}). Third, the shadow class and depth $r_{\mathrm{max}}$ refer to the Heisenberg truncation ($s = 1$ channel). At the full spin tower, the classification may differ (Remark~\ref{rem:c3-per-channel}).
 succeeded in 51ms:
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/modular_pva_quantization_frontier.tex:387:auxiliary affine algebra, but it leaves the scalar~$\kappa$ undetermined.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:2248:(\S\ref{subsec:gravity-genus-tower}) uses $\kappa_{\mathrm{eff}}$;
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_core.tex:1338:$\operatorname{av}(r(z)) = \kappa(\cA)$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_holographic_reconstruction.tex:2367:deformation theory. The two algebras have different $\kappa$
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/modular_pva_quantization.tex:1557:auxiliary affine algebra, but it leaves the scalar~$\kappa$ undetermined.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_physical_origins.tex:981:The Lie-algebraic limit $c = 0$ gives the Witt algebra: the central extension vanishes, leaving a purely quadratic OPE and placing the theory on the uncurved scalar locus $\Theta_\cA^{\min} = 0$. This does not identify the full higher-degree shadow obstruction tower. The semiclassical limit $c \to \infty$ ($\epsilon_2 \to 0$ in AGT, $b^2 = \epsilon_1/\epsilon_2 \to \infty$) gives Poisson brackets on the Hitchin base ($\kappa \to \infty$, strongly curved $A_\infty$ structure). These are distinct limits: $c = 0$ is scalar-uncurved, $c \to \infty$ is maximally curved.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_perturbative_finiteness.tex:418:The shadow free energy $F_g(\cA)$ is the $(r,g) = (0,g)$ component of the shadow algebra $\cA^{\mathrm{sh}} = H_\bullet(\Defcyc^{\mathrm{mod}}(\cA))$ in the bigrading by degree~$r$ and genus~$g$. The higher-degree shadows at genus $g$ (the cubic shadow $\mathfrak{C}_g$ at $r = 3$, the quartic resonance class $\mathfrak{Q}_g$ at $r = 4$) encode the gravitational interactions beyond the free-energy level. The shadow free energy is the simplest invariant, controlled entirely by the modular characteristic $\kappa(\cA)$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_perturbative_finiteness.tex:794:\item \emph{Scalar partition function on the proved scalar lane.} If $\cA$ has generators of uniform conformal weight, then the series $\sum_{g=1}^{\infty} F_g(\cA)\,\hbar^g$ converges absolutely for $|\hbar| < 4\pi^2$, with the closed-form expression $Z_{\mathrm{grav}}^{\mathrm{scal}}(\cA;\,\hbar) = \kappa(\cA) \cdot \frac{\sqrt{\hbar}/2}{\sin(\sqrt{\hbar}/2)}$. For arbitrary modular Koszul algebras, the universal scalar statement is the finite genus-$1$ term $F_1(\cA)=\kappa(\cA)/24$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_perturbative_finiteness.tex:1198:The scalar gravitational partition function $Z^{\mathrm{scal}}_{\mathrm{grav}}(\cA;\,\hbar) = \kappa \cdot \frac{\sqrt{\hbar}/2}{\sin(\sqrt{\hbar}/2)}$ has:
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_perturbative_finiteness.tex:1539:The meromorphic function $Z^{\mathrm{scal}}_{\mathrm{grav}}(\hbar) = \kappa \cdot \frac{\sqrt{\hbar}/2}{\sin(\sqrt{\hbar}/2)}$ admits a non-perturbative completion satisfying:
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_perturbative_finiteness.tex:1572:$Z_{\mathrm{grav}}(\hbar) = \kappa \cdot \frac{\sqrt{\hbar}/2}{\sin(\sqrt{\hbar}/2)}$
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_perturbative_finiteness.tex:1657:For higher-spin gravity in AdS$_3$ with $\mathcal{W}_N$ symmetry, the boundary algebra is $\mathcal{W}_k(\mathfrak{sl}_N)$ at central charge $c = (N-1) - N(N^2-1)(k+N-1)^2/(k+N)$. The modular characteristic is $\kappa(\mathcal{W}_N) = c \cdot (H_N - 1)$ where $H_N = \sum_{j=1}^N 1/j$ is the $N$-th harmonic number ($\kappa = c/2$ for $N=2$, $\kappa = 5c/6$ for $N=3$). The perturbative partition function is
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_perturbative_finiteness.tex:1659:Z_{\mathrm{grav}}^{W_N}(\hbar) \;=\; \kappa(\mathcal{W}_N) \cdot \frac{\sqrt{\hbar}/2}{\sin(\sqrt{\hbar}/2)}\,,
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_perturbative_finiteness.tex:1692:$Z_{\mathrm{grav}}^{\mathrm{scal}} = \kappa \cdot x/(2\sin(x/2))$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_perturbative_finiteness.tex:2716:S_{\mathrm{sh}}(\cA;\,\hbar) \;:=\; \log Z^{\mathrm{scal}}_{\mathrm{grav}}(\cA;\,\hbar) \;=\; \log\kappa + \log\frac{\sqrt{\hbar}/2}{\sin(\sqrt{\hbar}/2)}\,.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_perturbative_finiteness.tex:2806: Z_{\mathrm{grav}}^{\mathrm{scal}}(\cA;\,\hbar) \;=\; \sum_{j=1}^m \kappa(\cA_j) \cdot \frac{\sqrt{\hbar}/2}{\sin(\sqrt{\hbar}/2)}.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_perturbative_finiteness.tex:3540: $Z_{\mathrm{grav}}^{\mathrm{scal}}(\cA;\,\hbar) = \kappa(\cA) \cdot
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_perturbative_finiteness.tex:3697:For practical computation of the gravitational partition function at $|\hbar| = 1$ and $\kappa = O(1)$, the genus expansion converges extremely rapidly: the $g$-th term is of order $1/(2\pi)^{2g} \approx (0.0253)^g$. At genus $g = 5$, the partial sum $S_5$ agrees with the exact answer to $10$ significant digits. At genus $g = 10$, the agreement is to $20$ digits. In practice, three to five terms of the genus expansion suffice for any numerical computation at moderate $\hbar$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/factorization_swiss_cheese.tex:955:\item $h \cdot R + R \cdot h$: the cross-term.  The residue of $h \cdot R$ at $z_1 = z_2$ extracts the OPE coefficient at the simple pole, leaving $R(z_2, z_3)$ evaluated at $z_2 = z_3$.  Since $\bar\partial R = -\omega_{\mathrm{Ar}}$ (the Arakelov $(1,1)$-form), and the OPE coefficient is the structure constant weighted by $\kappa(\cA) = \mathrm{Tr}_\cA$, the double residue produces $\kappa(\cA) \cdot \omega_g$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/frame/preface.tex:286:averaging (for abelian algebras $\kappa = \mathrm{av}(r(z))$;
 succeeded in 51ms:
standalone/holographic_datum.tex-385-$\kappa(\cA)$ is its $\Sigma_2$-coinvariant projection. For abelian
standalone/holographic_datum.tex:386:algebras, $\av(r(z)) = \kappa$ directly. For non-abelian affine
standalone/holographic_datum.tex-387-Kac--Moody algebras, the full modular characteristic includes the
--
standalone/e1_primacy_ordered_bar.tex-1200-opposite-duality, and satisfies
standalone/e1_primacy_ordered_bar.tex:1201:$\av(r_0(z)) = \kappa(\cA)$ on abelian families, while for
standalone/e1_primacy_ordered_bar.tex-1202-non-abelian affine Kac--Moody
--
standalone/e1_primacy_ordered_bar.tex-1234-function of a single variable, the collision coordinate~$z$. The
standalone/e1_primacy_ordered_bar.tex:1235:statement $\av(r(z)) = \kappa$ says this exactly for Heisenberg,
standalone/e1_primacy_ordered_bar.tex-1236-while for non-abelian affine Kac--Moody the same averaging recovers
--
standalone/e1_primacy_ordered_bar.tex-1426-chain-level datum on the ordered side that becomes trivial
standalone/e1_primacy_ordered_bar.tex:1427:($\Sigma_2$-average $\to \kappa$) on the symmetric side. The
standalone/e1_primacy_ordered_bar.tex-1428-Drinfeld associator $\Phi_{\mathrm{KZ}}$ is a chain-level datum at
--
standalone/e1_primacy_ordered_bar.tex-1649-\item $r(z) = k/z$ (equation~\eqref{eq:heis-r-matrix}).
standalone/e1_primacy_ordered_bar.tex:1650:\item $\av(r(z)) = \kappa(\cH_k) = k$
standalone/e1_primacy_ordered_bar.tex-1651-  (the $\Sigma_2$-average of $k/z$ against $d\log(z)$ extracts
--
file update:
diff --git a/chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix b/chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix
index 65cee60eb99d11add7451146de7bb27f5f556dbe..bc2ffa2f7955916ee7be9f7eea55dce5d1e68f9c
--- a/chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix
+++ b/chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix
@@ -3004,8 +3004,11 @@
 is \emph{irrecoverable}: $r(z) = k\,\Omega/z$ carries the
 Casimir tensor
 $\Omega = \sum_a J^a \otimes J_a$ in $\fg \otimes \fg$, but
-$\mathrm{av}(r(z)) = \kappa = \dim(\fg)\cdot(k + h^\vee)/(2h^\vee)$
-is a single scalar.  The Casimir tensor determines the braiding
+$\mathrm{av}(r(z)) = \kappa_{\mathrm{dp}}
+= k\,\dim(\fg)/(2h^\vee)$ and
+$\kappa = \kappa_{\mathrm{dp}} + \dim(\fg)/2
+= \dim(\fg)\cdot(k + h^\vee)/(2h^\vee)$
+is a single scalar shadow. The Casimir tensor determines the braiding
 on the category of representations; the modular
 characteristic determines the genus-$1$ anomaly.  These are
 different structural data at different categorical depths.
diff --git a/chapters/theory/e1_modular_koszul.tex b/chapters/theory/e1_modular_koszul.tex
index a8a83c93d1d8dc248f8f9f6309990c5a7602c6c4..041dea657991f4089b4f0404b429bf3fff9ad079
--- a/chapters/theory/e1_modular_koszul.tex
+++ b/chapters/theory/e1_modular_koszul.tex
@@ -2255,8 +2255,11 @@
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item $(K_\cA^{E_1})_{0,2} = r(z)$, the classical $r$-matrix
  \textup{(}genus~$0$, degree~$2$\textup{)}. The coinvariant
- $\operatorname{av}(r(z)) = \kappa(\cA)$ recovers the scalar
- curvature.
+ $\operatorname{av}(r(z))$ recovers the scalar degree-$2$ shadow:
+ on abelian families $\operatorname{av}(r(z)) = \kappa(\cA)$,
+ while for non-abelian affine Kac--Moody
+ $\operatorname{av}(r(z)) = \kappa_{\mathrm{dp}}(\cA)$ and
+ $\kappa(\cA) = \kappa_{\mathrm{dp}}(\cA) + \dim(\fg)/2$.
 \item $(K_\cA^{E_1})_{0,3} = \Phi_{\mathrm{KZ}}(\cA)$, the
  KZ\slash Drinfeld associator \textup{(}genus~$0$, degree~$3$,
  for affine algebras;
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 789ce9acf5b68f150a665afd1b7486e6b1256a16..09413d565658e9d71f63d7dd7327bf183c8a1ea7
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -895,8 +895,12 @@
 
 \item \emph{Leading-order modular shadow.}
  The $\Sigma_2$-coinvariant projection
- $\operatorname{av}(r(z)) = \kappa(\cA)$ is the modular
- characteristic, the first entry of the shadow obstruction tower
+ $\operatorname{av}(r(z))$ is the leading scalar shadow: it equals
+ $\kappa(\cA)$ on abelian and scalar families, while for
+ non-abelian affine Kac--Moody it gives
+ $\kappa_{\mathrm{dp}}(\cA)$ and the full modular characteristic is
+ $\kappa(\cA) = \kappa_{\mathrm{dp}}(\cA) + \dim(\fg)/2$. This is
+ the first entry of the shadow obstruction tower
  \textup{(}equation~\textup{\eqref{eq:intro-kappa-from-r}};
  Theorem~\textup{\ref{thm:e1-primacy}}\textup{)}. The residue contains
  a matrix-valued refinement; averaging produces the scalar.
@@ -1262,17 +1266,18 @@
 \;=\;
 \Theta_\cA.
 \end{equation}
-At degree~$2$, this projection records only one number: the
-$\Sigma_2$-coinvariant of the residue of $r(z)$ at $z = 0$ is the
-modular characteristic
+At degree~$2$, this projection records only one scalar: the
+$\Sigma_2$-coinvariant of the residue of $r(z)$ at $z = 0$ is
 \begin{equation}\label{eq:intro-kappa-from-r}
-\kappa(\cA)
-\;=\;
 \operatorname{av}\bigl(r(z)\bigr)
 \;=\;
 \tfrac{1}{2}\,\operatorname{tr}\!\bigl[\Res_{z = 0} r(z)\bigr],
 \end{equation}
 where the trace is the cyclic trace on $\End(V^{\otimes 2})$.
+For abelian and scalar families,
+\[
+\kappa(\cA) = \operatorname{av}\bigl(r(z)\bigr).
+\]
 For the affine Kac--Moody vacuum algebra $V_k(\mathfrak{g})$ at
 non-critical level, the averaging formula
 \eqref{eq:intro-kappa-from-r} specializes to the Sugawara identity
@@ -1652,8 +1657,11 @@
 at the $R$-matrix level beyond what the local OPE already carries.
 Tier (b) is still $\Einf$-chiral in the three-leaps classification of
 Volume~II: the algebra is commutative up to quasi-isomorphism, and
-averaging recovers the modular shadow $\kappa$ without information
-loss beyond the $\Sigma_n$-coinvariant step.
+averaging recovers the scalar degree-$2$ shadow without
+information loss beyond the $\Sigma_n$-coinvariant step: this is
+$\kappa$ on abelian and scalar families, while for non-abelian
+affine Kac--Moody it is $\kappa_{\mathrm{dp}}$ and the full
+modular characteristic adds the Sugawara shift $\dim(\fg)/2$.
 
 Tier (c) is the genuinely $\Eone$-primitive extreme. The Yangian
 $Y(\mathfrak g)$ and the Etingof--Kazhdan quantum vertex algebras
diff --git a/standalone/chiral_chern_weil.tex b/standalone/chiral_chern_weil.tex
index 264bc812bc756f693683ea49fffc92a69ba23fb8..e925297230a043684b2162d6eea950832e71b362
--- a/standalone/chiral_chern_weil.tex
+++ b/standalone/chiral_chern_weil.tex
@@ -1213,7 +1213,11 @@
 % ================================================================
 \section{The chiral curvature}\label{sec:chiral-cw}
 
-The averaging map extracts~$\kappa$ from the $r$-matrix.
+The averaging map extracts the scalar degree-$2$ shadow from the
+$r$-matrix: this is~$\kappa$ on abelian and scalar families, while
+for non-abelian affine Kac--Moody the averaged scalar is
+$\kappa_{\mathrm{cl}}$ and the full modular characteristic is
+$\kappa = \kappa_{\mathrm{cl}} + \dim(\fg)/2$.
 The question it forces is: what role does~$\kappa$ play
 geometrically? The answer: $\kappa$ is the proportionality
 constant of a curvature. The bar differential, which squares
diff --git a/standalone/shadow_towers_v3.tex b/standalone/shadow_towers_v3.tex
index 3e3cf779de2c8653d94026ee31a290ce83cfcba7..12a1cee9e29af47da9fba8082a62d08db7d85eb3
--- a/standalone/shadow_towers_v3.tex
+++ b/standalone/shadow_towers_v3.tex
@@ -1846,10 +1846,12 @@
 $\Theta_\cA^{E_1}$ projects to~$\Theta_\cA$ under
 $\mathrm{av}$. The degree-$2$ component of
 $\Theta_\cA^{E_1}$ is the $R$-matrix $r(z)$, and its
-average is the modular characteristic~$\kappa$, with the
-Sugawara correction for non-abelian algebras arising from
-the simple-pole self-contraction of the ordered two-point
-function. The higher degrees follow by the same averaging
+average is the scalar degree-$2$ shadow: it equals the modular
+characteristic~$\kappa$ on abelian families, while for
+non-abelian affine Kac--Moody the average is
+$\kappa_{\mathrm{dp}}$ and the full~$\kappa$ adds the
+Sugawara correction from the simple-pole self-contraction of the
+ordered two-point function. The higher degrees follow by the same averaging
 applied to the degree-$r$ MC components.
 \end{proof}
 
@@ -1873,7 +1875,11 @@
 The $E_1$ convolution algebra
 $\mathfrak{g}^{E_1}_\cA$ carries a spectral $R$-matrix
 $r(z) \in \mathrm{End}(V \otimes V)((z))$ at degree~$2$,
-whose averaging produces~$\kappa$. The structure of $r(z)$
+whose averaging produces the scalar degree-$2$ shadow:
+for abelian families this is~$\kappa$, while for non-abelian
+affine Kac--Moody it is~$\kappa_{\mathrm{dp}}$ and the full
+modular characteristic is
+$\kappa = \kappa_{\mathrm{dp}} + \dim(\fg)/2$. The structure of $r(z)$
 varies by class.
 
 \begin{example}[Class $\mathbf{G}$:
diff --git a/standalone/survey_track_a_compressed.tex b/standalone/survey_track_a_compressed.tex
index cb62bb8b88937153678a962d34c4c5dac04b9700..084c11fb005499137646a882cff6cb86a1becc01
--- a/standalone/survey_track_a_compressed.tex
+++ b/standalone/survey_track_a_compressed.tex
@@ -361,11 +361,17 @@
 \]
 a matrix-valued rational function encoding the full binary OPE data.
 Applying $\mathrm{av}$ at degree~$2$ collapses the profile to a single
-scalar,
+scalar shadow:
 \begin{equation}\label{eq:av-organizing}
-\mathrm{av}\bigl(r(z)\bigr)\;=\;\kappa(\cA),
+\begin{aligned}
+\mathrm{av}\bigl(r(z)\bigr) &= \kappa(\cA)
+&& \text{for abelian and scalar families},\\
+\mathrm{av}\bigl(r(z)\bigr) &= \kappa_{\mathrm{dp}}(\cA), \qquad
+\kappa(\cA) = \kappa_{\mathrm{dp}}(\cA) + \dim(\fg)/2
+&& \text{for non-abelian affine Kac--Moody.}
+\end{aligned}
 \end{equation}
-the modular characteristic of Theorem~D. At degree~$3$ the KZ
+This is the modular characteristic package of Theorem~D. At degree~$3$ the KZ
 associator projects to the cubic shadow~$\mathfrak C$; at degree~$4$
 the Yangian higher coproduct projects to the quartic resonance
 class~$\mathfrak Q$. Each degree-$n$ component of the ordered

codex
The grep-based falsifier passes for the writable tree: the remaining `av(r)=\kappa` hits are abelian-only, explicitly corrected with the Sugawara shift, or unrelated family-specific formulas. I’m pulling the final diff summary and exact blocked sibling-volume paths for the closeout.
exec
/bin/zsh -lc "rg -n '\\"'$'"\\\\operatorname\\{av\\}\\(r\\(z\\)\\) = \\\\kappa\\(\\\\cA\\)\\.|\\"'$'"\\\\mathrm\\{av\\}\\(r\\(z\\)\\) = \\\\kappa_\\{\\\\mathrm\\{ch\\}\\}|\\"'$'"\\\\operatorname\\{av\\}\\(r\\(z\\)\\) = \\\\kappa\\(\\\\cA\\)' /Users/raeez/chiral-bar-cobar-vol2/chapters /Users/raeez/calabi-yau-quantum-groups/chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'git diff --stat -- chapters/theory/e1_modular_koszul.tex chapters/theory/introduction.tex standalone/survey_track_a_compressed.tex standalone/shadow_towers_v3.tex standalone/chiral_chern_weil.tex chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
 chapters/theory/e1_modular_koszul.tex    |  7 +++++--
 chapters/theory/introduction.tex         | 26 +++++++++++++++++---------
 standalone/chiral_chern_weil.tex         |  6 +++++-
 standalone/shadow_towers_v3.tex          | 16 +++++++++++-----
 standalone/survey_track_a_compressed.tex | 12 +++++++++---
 5 files changed, 47 insertions(+), 20 deletions(-)
 succeeded in 52ms:
/Users/raeez/calabi-yau-quantum-groups/chapters/frame/preface.tex:460:structure via averaging $\mathrm{av}(r(z)) = \kappa_{\mathrm{ch}}$.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/drinfeld_center.tex:702:$\mathrm{av}(r(z)) = \kappa_{\mathrm{ch}}$ extracts the scalar
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/introduction.tex:392:$\mathrm{av}(r(z)) = \kappa_{\mathrm{ch}}$. The $E_1$-chiral
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex:23:This averaging is \emph{lossy}: $\mathrm{av}(r(z)) = \kappa_{\mathrm{ch}}$ forgets the
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex:122:is a morphism of cochain complexes and sends the $E_1$ structure to the $E_\infty$ structure. It is lossy: the kernel contains the $R$-matrix data of the holomorphic factor, and on degree two $\mathrm{av}(r(z)) = \kappa_{\mathrm{ch}}$.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex:202: ($\mathrm{av}(r(z)) = \kappa_{\mathrm{ch}}$) \\
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex:1087: $\mathrm{av}(r(z)) = \kappa_{\mathrm{ch}}$ (a scalar), so the full
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex:1355:$\mathrm{av}(r(z)) = \kappa_{\mathrm{ch}}$: the full
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex:1371:$R$-matrix & $r(z) = k\,\Omega/z + \cdots$ & $R^{E_2}(z)$ (half-braiding) & $\mathrm{av}(r(z)) = \kappa_{\mathrm{ch}}$ (scalar) \\
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/foundations_recast_draft.tex:302:The open colour of the Swiss-cheese pair $(A^{\mathrm{bulk}}, A^{\mathrm{bdy}})$ carries additional Hopf-algebraic structure formalized in Vol~III (\S7 of the $E_1$-chiral algebras chapter): the $E_1$-chiral bialgebra axioms~(H1)--(H5). The coproduct $\Delta_z \colon A \to A \otimes_{E_1,z} A$ lives on the open ($E_1$/topological) colour, not the closed ($E_2$/chiral) colour. The $E_\infty$ averaging map $\mathrm{av} \colon B^{\mathrm{ord}}(A) \to B^{\Sigma}(A)$ destroys the Hopf data: $\mathrm{av}(r(z)) = \kappa_{\mathrm{ch}}$, a scalar (Vol~III, Proposition~\texttt{prop:averaging-forgets-hopf}). The braided ($E_2$) structure is recovered via the Drinfeld center $\cZ(\Rep^{E_1}(A))$, not by direct construction on the closed colour. The universal coproduct at all spins is $\Delta_z(e_s) = \sum (-1)^k \binom{N_R - b}{k} z^k \, e_a^L \cdot e_b^R$ (Vol~III, Proposition~\texttt{prop:universal-coproduct}).
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd.tex:1277:$\operatorname{av}(r(z)) = \kappa(\cA)$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_core.tex:1338:$\operatorname{av}(r(z)) = \kappa(\cA)$.
file update:
diff --git a/chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix b/chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix
index 65cee60eb99d11add7451146de7bb27f5f556dbe..bc2ffa2f7955916ee7be9f7eea55dce5d1e68f9c
--- a/chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix
+++ b/chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix
@@ -3004,8 +3004,11 @@
 is \emph{irrecoverable}: $r(z) = k\,\Omega/z$ carries the
 Casimir tensor
 $\Omega = \sum_a J^a \otimes J_a$ in $\fg \otimes \fg$, but
-$\mathrm{av}(r(z)) = \kappa = \dim(\fg)\cdot(k + h^\vee)/(2h^\vee)$
-is a single scalar.  The Casimir tensor determines the braiding
+$\mathrm{av}(r(z)) = \kappa_{\mathrm{dp}}
+= k\,\dim(\fg)/(2h^\vee)$ and
+$\kappa = \kappa_{\mathrm{dp}} + \dim(\fg)/2
+= \dim(\fg)\cdot(k + h^\vee)/(2h^\vee)$
+is a single scalar shadow. The Casimir tensor determines the braiding
 on the category of representations; the modular
 characteristic determines the genus-$1$ anomaly.  These are
 different structural data at different categorical depths.
diff --git a/chapters/theory/e1_modular_koszul.tex b/chapters/theory/e1_modular_koszul.tex
index a8a83c93d1d8dc248f8f9f6309990c5a7602c6c4..041dea657991f4089b4f0404b429bf3fff9ad079
--- a/chapters/theory/e1_modular_koszul.tex
+++ b/chapters/theory/e1_modular_koszul.tex
@@ -2255,8 +2255,11 @@
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item $(K_\cA^{E_1})_{0,2} = r(z)$, the classical $r$-matrix
  \textup{(}genus~$0$, degree~$2$\textup{)}. The coinvariant
- $\operatorname{av}(r(z)) = \kappa(\cA)$ recovers the scalar
- curvature.
+ $\operatorname{av}(r(z))$ recovers the scalar degree-$2$ shadow:
+ on abelian families $\operatorname{av}(r(z)) = \kappa(\cA)$,
+ while for non-abelian affine Kac--Moody
+ $\operatorname{av}(r(z)) = \kappa_{\mathrm{dp}}(\cA)$ and
+ $\kappa(\cA) = \kappa_{\mathrm{dp}}(\cA) + \dim(\fg)/2$.
 \item $(K_\cA^{E_1})_{0,3} = \Phi_{\mathrm{KZ}}(\cA)$, the
  KZ\slash Drinfeld associator \textup{(}genus~$0$, degree~$3$,
  for affine algebras;
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 789ce9acf5b68f150a665afd1b7486e6b1256a16..09413d565658e9d71f63d7dd7327bf183c8a1ea7
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -895,8 +895,12 @@
 
 \item \emph{Leading-order modular shadow.}
  The $\Sigma_2$-coinvariant projection
- $\operatorname{av}(r(z)) = \kappa(\cA)$ is the modular
- characteristic, the first entry of the shadow obstruction tower
+ $\operatorname{av}(r(z))$ is the leading scalar shadow: it equals
+ $\kappa(\cA)$ on abelian and scalar families, while for
+ non-abelian affine Kac--Moody it gives
+ $\kappa_{\mathrm{dp}}(\cA)$ and the full modular characteristic is
+ $\kappa(\cA) = \kappa_{\mathrm{dp}}(\cA) + \dim(\fg)/2$. This is
+ the first entry of the shadow obstruction tower
  \textup{(}equation~\textup{\eqref{eq:intro-kappa-from-r}};
  Theorem~\textup{\ref{thm:e1-primacy}}\textup{)}. The residue contains
  a matrix-valued refinement; averaging produces the scalar.
@@ -1262,17 +1266,18 @@
 \;=\;
 \Theta_\cA.
 \end{equation}
-At degree~$2$, this projection records only one number: the
-$\Sigma_2$-coinvariant of the residue of $r(z)$ at $z = 0$ is the
-modular characteristic
+At degree~$2$, this projection records only one scalar: the
+$\Sigma_2$-coinvariant of the residue of $r(z)$ at $z = 0$ is
 \begin{equation}\label{eq:intro-kappa-from-r}
-\kappa(\cA)
-\;=\;
 \operatorname{av}\bigl(r(z)\bigr)
 \;=\;
 \tfrac{1}{2}\,\operatorname{tr}\!\bigl[\Res_{z = 0} r(z)\bigr],
 \end{equation}
 where the trace is the cyclic trace on $\End(V^{\otimes 2})$.
+For abelian and scalar families,
+\[
+\kappa(\cA) = \operatorname{av}\bigl(r(z)\bigr).
+\]
 For the affine Kac--Moody vacuum algebra $V_k(\mathfrak{g})$ at
 non-critical level, the averaging formula
 \eqref{eq:intro-kappa-from-r} specializes to the Sugawara identity
@@ -1652,8 +1657,11 @@
 at the $R$-matrix level beyond what the local OPE already carries.
 Tier (b) is still $\Einf$-chiral in the three-leaps classification of
 Volume~II: the algebra is commutative up to quasi-isomorphism, and
-averaging recovers the modular shadow $\kappa$ without information
-loss beyond the $\Sigma_n$-coinvariant step.
+averaging recovers the scalar degree-$2$ shadow without
+information loss beyond the $\Sigma_n$-coinvariant step: this is
+$\kappa$ on abelian and scalar families, while for non-abelian
+affine Kac--Moody it is $\kappa_{\mathrm{dp}}$ and the full
+modular characteristic adds the Sugawara shift $\dim(\fg)/2$.
 
 Tier (c) is the genuinely $\Eone$-primitive extreme. The Yangian
 $Y(\mathfrak g)$ and the Etingof--Kazhdan quantum vertex algebras
diff --git a/standalone/chiral_chern_weil.tex b/standalone/chiral_chern_weil.tex
index 264bc812bc756f693683ea49fffc92a69ba23fb8..e925297230a043684b2162d6eea950832e71b362
--- a/standalone/chiral_chern_weil.tex
+++ b/standalone/chiral_chern_weil.tex
@@ -1213,7 +1213,11 @@
 % ================================================================
 \section{The chiral curvature}\label{sec:chiral-cw}
 
-The averaging map extracts~$\kappa$ from the $r$-matrix.
+The averaging map extracts the scalar degree-$2$ shadow from the
+$r$-matrix: this is~$\kappa$ on abelian and scalar families, while
+for non-abelian affine Kac--Moody the averaged scalar is
+$\kappa_{\mathrm{cl}}$ and the full modular characteristic is
+$\kappa = \kappa_{\mathrm{cl}} + \dim(\fg)/2$.
 The question it forces is: what role does~$\kappa$ play
 geometrically? The answer: $\kappa$ is the proportionality
 constant of a curvature. The bar differential, which squares
diff --git a/standalone/shadow_towers_v3.tex b/standalone/shadow_towers_v3.tex
index 3e3cf779de2c8653d94026ee31a290ce83cfcba7..12a1cee9e29af47da9fba8082a62d08db7d85eb3
--- a/standalone/shadow_towers_v3.tex
+++ b/standalone/shadow_towers_v3.tex
@@ -1846,10 +1846,12 @@
 $\Theta_\cA^{E_1}$ projects to~$\Theta_\cA$ under
 $\mathrm{av}$. The degree-$2$ component of
 $\Theta_\cA^{E_1}$ is the $R$-matrix $r(z)$, and its
-average is the modular characteristic~$\kappa$, with the
-Sugawara correction for non-abelian algebras arising from
-the simple-pole self-contraction of the ordered two-point
-function. The higher degrees follow by the same averaging
+average is the scalar degree-$2$ shadow: it equals the modular
+characteristic~$\kappa$ on abelian families, while for
+non-abelian affine Kac--Moody the average is
+$\kappa_{\mathrm{dp}}$ and the full~$\kappa$ adds the
+Sugawara correction from the simple-pole self-contraction of the
+ordered two-point function. The higher degrees follow by the same averaging
 applied to the degree-$r$ MC components.
 \end{proof}
 
@@ -1873,7 +1875,11 @@
 The $E_1$ convolution algebra
 $\mathfrak{g}^{E_1}_\cA$ carries a spectral $R$-matrix
 $r(z) \in \mathrm{End}(V \otimes V)((z))$ at degree~$2$,
-whose averaging produces~$\kappa$. The structure of $r(z)$
+whose averaging produces the scalar degree-$2$ shadow:
+for abelian families this is~$\kappa$, while for non-abelian
+affine Kac--Moody it is~$\kappa_{\mathrm{dp}}$ and the full
+modular characteristic is
+$\kappa = \kappa_{\mathrm{dp}} + \dim(\fg)/2$. The structure of $r(z)$
 varies by class.
 
 \begin{example}[Class $\mathbf{G}$:
diff --git a/standalone/survey_track_a_compressed.tex b/standalone/survey_track_a_compressed.tex
index cb62bb8b88937153678a962d34c4c5dac04b9700..084c11fb005499137646a882cff6cb86a1becc01
--- a/standalone/survey_track_a_compressed.tex
+++ b/standalone/survey_track_a_compressed.tex
@@ -361,11 +361,17 @@
 \]
 a matrix-valued rational function encoding the full binary OPE data.
 Applying $\mathrm{av}$ at degree~$2$ collapses the profile to a single
-scalar,
+scalar shadow:
 \begin{equation}\label{eq:av-organizing}
-\mathrm{av}\bigl(r(z)\bigr)\;=\;\kappa(\cA),
+\begin{aligned}
+\mathrm{av}\bigl(r(z)\bigr) &= \kappa(\cA)
+&& \text{for abelian and scalar families},\\
+\mathrm{av}\bigl(r(z)\bigr) &= \kappa_{\mathrm{dp}}(\cA), \qquad
+\kappa(\cA) = \kappa_{\mathrm{dp}}(\cA) + \dim(\fg)/2
+&& \text{for non-abelian affine Kac--Moody.}
+\end{aligned}
 \end{equation}
-the modular characteristic of Theorem~D. At degree~$3$ the KZ
+This is the modular characteristic package of Theorem~D. At degree~$3$ the KZ
 associator projects to the cubic shadow~$\mathfrak C$; at degree~$4$
 the Yangian higher coproduct projects to the quartic resonance
 class~$\mathfrak Q$. Each degree-$n$ component of the ordered


thinking
**Investigating git backup issues**

I'm looking at why the git diff stat didn't include the backup file. It might be untracked or ignored, especially since we specified the file path but it didn't show up. The backup file could be unchanged because it's not tracked. I wonder if I should mention that? Maybe I could check the patch we did. I think using `git status --short` on touched files could help me see which ones are tracked or untracked.
exec
/bin/zsh -lc 'git status --short -- chapters/theory/e1_modular_koszul.tex chapters/theory/introduction.tex standalone/survey_track_a_compressed.tex standalone/shadow_towers_v3.tex standalone/chiral_chern_weil.tex chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
 M chapters/theory/e1_modular_koszul.tex
 M chapters/theory/introduction.tex
 M standalone/chiral_chern_weil.tex
 M standalone/shadow_towers_v3.tex
 M standalone/survey_track_a_compressed.tex
file update:
diff --git a/chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix b/chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix
index 65cee60eb99d11add7451146de7bb27f5f556dbe..bc2ffa2f7955916ee7be9f7eea55dce5d1e68f9c
--- a/chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix
+++ b/chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix
@@ -3004,8 +3004,11 @@
 is \emph{irrecoverable}: $r(z) = k\,\Omega/z$ carries the
 Casimir tensor
 $\Omega = \sum_a J^a \otimes J_a$ in $\fg \otimes \fg$, but
-$\mathrm{av}(r(z)) = \kappa = \dim(\fg)\cdot(k + h^\vee)/(2h^\vee)$
-is a single scalar.  The Casimir tensor determines the braiding
+$\mathrm{av}(r(z)) = \kappa_{\mathrm{dp}}
+= k\,\dim(\fg)/(2h^\vee)$ and
+$\kappa = \kappa_{\mathrm{dp}} + \dim(\fg)/2
+= \dim(\fg)\cdot(k + h^\vee)/(2h^\vee)$
+is a single scalar shadow. The Casimir tensor determines the braiding
 on the category of representations; the modular
 characteristic determines the genus-$1$ anomaly.  These are
 different structural data at different categorical depths.
diff --git a/chapters/theory/e1_modular_koszul.tex b/chapters/theory/e1_modular_koszul.tex
index a8a83c93d1d8dc248f8f9f6309990c5a7602c6c4..041dea657991f4089b4f0404b429bf3fff9ad079
--- a/chapters/theory/e1_modular_koszul.tex
+++ b/chapters/theory/e1_modular_koszul.tex
@@ -2255,8 +2255,11 @@
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item $(K_\cA^{E_1})_{0,2} = r(z)$, the classical $r$-matrix
  \textup{(}genus~$0$, degree~$2$\textup{)}. The coinvariant
- $\operatorname{av}(r(z)) = \kappa(\cA)$ recovers the scalar
- curvature.
+ $\operatorname{av}(r(z))$ recovers the scalar degree-$2$ shadow:
+ on abelian families $\operatorname{av}(r(z)) = \kappa(\cA)$,
+ while for non-abelian affine Kac--Moody
+ $\operatorname{av}(r(z)) = \kappa_{\mathrm{dp}}(\cA)$ and
+ $\kappa(\cA) = \kappa_{\mathrm{dp}}(\cA) + \dim(\fg)/2$.
 \item $(K_\cA^{E_1})_{0,3} = \Phi_{\mathrm{KZ}}(\cA)$, the
  KZ\slash Drinfeld associator \textup{(}genus~$0$, degree~$3$,
  for affine algebras;
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 789ce9acf5b68f150a665afd1b7486e6b1256a16..09413d565658e9d71f63d7dd7327bf183c8a1ea7
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -895,8 +895,12 @@
 
 \item \emph{Leading-order modular shadow.}
  The $\Sigma_2$-coinvariant projection
- $\operatorname{av}(r(z)) = \kappa(\cA)$ is the modular
- characteristic, the first entry of the shadow obstruction tower
+ $\operatorname{av}(r(z))$ is the leading scalar shadow: it equals
+ $\kappa(\cA)$ on abelian and scalar families, while for
+ non-abelian affine Kac--Moody it gives
+ $\kappa_{\mathrm{dp}}(\cA)$ and the full modular characteristic is
+ $\kappa(\cA) = \kappa_{\mathrm{dp}}(\cA) + \dim(\fg)/2$. This is
+ the first entry of the shadow obstruction tower
  \textup{(}equation~\textup{\eqref{eq:intro-kappa-from-r}};
  Theorem~\textup{\ref{thm:e1-primacy}}\textup{)}. The residue contains
  a matrix-valued refinement; averaging produces the scalar.
@@ -1262,17 +1266,18 @@
 \;=\;
 \Theta_\cA.
 \end{equation}
-At degree~$2$, this projection records only one number: the
-$\Sigma_2$-coinvariant of the residue of $r(z)$ at $z = 0$ is the
-modular characteristic
+At degree~$2$, this projection records only one scalar: the
+$\Sigma_2$-coinvariant of the residue of $r(z)$ at $z = 0$ is
 \begin{equation}\label{eq:intro-kappa-from-r}
-\kappa(\cA)
-\;=\;
 \operatorname{av}\bigl(r(z)\bigr)
 \;=\;
 \tfrac{1}{2}\,\operatorname{tr}\!\bigl[\Res_{z = 0} r(z)\bigr],
 \end{equation}
 where the trace is the cyclic trace on $\End(V^{\otimes 2})$.
+For abelian and scalar families,
+\[
+\kappa(\cA) = \operatorname{av}\bigl(r(z)\bigr).
+\]
 For the affine Kac--Moody vacuum algebra $V_k(\mathfrak{g})$ at
 non-critical level, the averaging formula
 \eqref{eq:intro-kappa-from-r} specializes to the Sugawara identity
@@ -1652,8 +1657,11 @@
 at the $R$-matrix level beyond what the local OPE already carries.
 Tier (b) is still $\Einf$-chiral in the three-leaps classification of
 Volume~II: the algebra is commutative up to quasi-isomorphism, and
-averaging recovers the modular shadow $\kappa$ without information
-loss beyond the $\Sigma_n$-coinvariant step.
+averaging recovers the scalar degree-$2$ shadow without
+information loss beyond the $\Sigma_n$-coinvariant step: this is
+$\kappa$ on abelian and scalar families, while for non-abelian
+affine Kac--Moody it is $\kappa_{\mathrm{dp}}$ and the full
+modular characteristic adds the Sugawara shift $\dim(\fg)/2$.
 
 Tier (c) is the genuinely $\Eone$-primitive extreme. The Yangian
 $Y(\mathfrak g)$ and the Etingof--Kazhdan quantum vertex algebras
diff --git a/standalone/chiral_chern_weil.tex b/standalone/chiral_chern_weil.tex
index 264bc812bc756f693683ea49fffc92a69ba23fb8..e925297230a043684b2162d6eea950832e71b362
--- a/standalone/chiral_chern_weil.tex
+++ b/standalone/chiral_chern_weil.tex
@@ -1213,7 +1213,11 @@
 % ================================================================
 \section{The chiral curvature}\label{sec:chiral-cw}
 
-The averaging map extracts~$\kappa$ from the $r$-matrix.
+The averaging map extracts the scalar degree-$2$ shadow from the
+$r$-matrix: this is~$\kappa$ on abelian and scalar families, while
+for non-abelian affine Kac--Moody the averaged scalar is
+$\kappa_{\mathrm{cl}}$ and the full modular characteristic is
+$\kappa = \kappa_{\mathrm{cl}} + \dim(\fg)/2$.
 The question it forces is: what role does~$\kappa$ play
 geometrically? The answer: $\kappa$ is the proportionality
 constant of a curvature. The bar differential, which squares
diff --git a/standalone/shadow_towers_v3.tex b/standalone/shadow_towers_v3.tex
index 3e3cf779de2c8653d94026ee31a290ce83cfcba7..12a1cee9e29af47da9fba8082a62d08db7d85eb3
--- a/standalone/shadow_towers_v3.tex
+++ b/standalone/shadow_towers_v3.tex
@@ -1846,10 +1846,12 @@
 $\Theta_\cA^{E_1}$ projects to~$\Theta_\cA$ under
 $\mathrm{av}$. The degree-$2$ component of
 $\Theta_\cA^{E_1}$ is the $R$-matrix $r(z)$, and its
-average is the modular characteristic~$\kappa$, with the
-Sugawara correction for non-abelian algebras arising from
-the simple-pole self-contraction of the ordered two-point
-function. The higher degrees follow by the same averaging
+average is the scalar degree-$2$ shadow: it equals the modular
+characteristic~$\kappa$ on abelian families, while for
+non-abelian affine Kac--Moody the average is
+$\kappa_{\mathrm{dp}}$ and the full~$\kappa$ adds the
+Sugawara correction from the simple-pole self-contraction of the
+ordered two-point function. The higher degrees follow by the same averaging
 applied to the degree-$r$ MC components.
 \end{proof}
 
@@ -1873,7 +1875,11 @@
 The $E_1$ convolution algebra
 $\mathfrak{g}^{E_1}_\cA$ carries a spectral $R$-matrix
 $r(z) \in \mathrm{End}(V \otimes V)((z))$ at degree~$2$,
-whose averaging produces~$\kappa$. The structure of $r(z)$
+whose averaging produces the scalar degree-$2$ shadow:
+for abelian families this is~$\kappa$, while for non-abelian
+affine Kac--Moody it is~$\kappa_{\mathrm{dp}}$ and the full
+modular characteristic is
+$\kappa = \kappa_{\mathrm{dp}} + \dim(\fg)/2$. The structure of $r(z)$
 varies by class.
 
 \begin{example}[Class $\mathbf{G}$:
diff --git a/standalone/survey_track_a_compressed.tex b/standalone/survey_track_a_compressed.tex
index cb62bb8b88937153678a962d34c4c5dac04b9700..084c11fb005499137646a882cff6cb86a1becc01
--- a/standalone/survey_track_a_compressed.tex
+++ b/standalone/survey_track_a_compressed.tex
@@ -361,11 +361,17 @@
 \]
 a matrix-valued rational function encoding the full binary OPE data.
 Applying $\mathrm{av}$ at degree~$2$ collapses the profile to a single
-scalar,
+scalar shadow:
 \begin{equation}\label{eq:av-organizing}
-\mathrm{av}\bigl(r(z)\bigr)\;=\;\kappa(\cA),
+\begin{aligned}
+\mathrm{av}\bigl(r(z)\bigr) &= \kappa(\cA)
+&& \text{for abelian and scalar families},\\
+\mathrm{av}\bigl(r(z)\bigr) &= \kappa_{\mathrm{dp}}(\cA), \qquad
+\kappa(\cA) = \kappa_{\mathrm{dp}}(\cA) + \dim(\fg)/2
+&& \text{for non-abelian affine Kac--Moody.}
+\end{aligned}
 \end{equation}
-the modular characteristic of Theorem~D. At degree~$3$ the KZ
+This is the modular characteristic package of Theorem~D. At degree~$3$ the KZ
 associator projects to the cubic shadow~$\mathfrak C$; at degree~$4$
 the Yangian higher coproduct projects to the quartic resonance
 class~$\mathfrak Q$. Each degree-$n$ component of the ordered

codex
**Status**

Vol I is `FIXED`. Vol II and Vol III are `BLOCKED` by sandbox write scope.

I patched the writable search surface so the generic `av(r(z)) = \kappa` claim no longer outclaims the non-abelian affine KM case. The affected in-repo files are [e1_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/e1_modular_koszul.tex), [introduction.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/introduction.tex), [survey_track_a_compressed.tex](/Users/raeez/chiral-bar-cobar/standalone/survey_track_a_compressed.tex), [shadow_towers_v3.tex](/Users/raeez/chiral-bar-cobar/standalone/shadow_towers_v3.tex), and [chiral_chern_weil.tex](/Users/raeez/chiral-bar-cobar/standalone/chiral_chern_weil.tex). I also cleaned the stale grep surface in `chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix`.

Verification was grep-based on `chapters/` and `standalone/`: the remaining hits are abelian-only, already carry the Sugawara correction, or are family-specific non-KM statements. I did not run a full TeX build.

**Blocked**

`apply_patch` outside `/Users/raeez/chiral-bar-cobar` was rejected by approval settings, so I could not patch the sibling volume trees. The remaining external fixes are at [ordered_associative_chiral_kd.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd.tex:1277), [ordered_associative_chiral_kd_core.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_core.tex:1338), [foundations_recast_draft.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/foundations_recast_draft.tex:302), [preface.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/frame/preface.tex:460), [introduction.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/introduction.tex:392), [drinfeld_center.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/drinfeld_center.tex:702), and [e1_chiral_algebras.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex:23). The same Vol III file also has repeated instances at lines 122, 202, 1087, 1355, and 1371.
file update:
diff --git a/chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix b/chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix
index 65cee60eb99d11add7451146de7bb27f5f556dbe..bc2ffa2f7955916ee7be9f7eea55dce5d1e68f9c
--- a/chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix
+++ b/chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix
@@ -3004,8 +3004,11 @@
 is \emph{irrecoverable}: $r(z) = k\,\Omega/z$ carries the
 Casimir tensor
 $\Omega = \sum_a J^a \otimes J_a$ in $\fg \otimes \fg$, but
-$\mathrm{av}(r(z)) = \kappa = \dim(\fg)\cdot(k + h^\vee)/(2h^\vee)$
-is a single scalar.  The Casimir tensor determines the braiding
+$\mathrm{av}(r(z)) = \kappa_{\mathrm{dp}}
+= k\,\dim(\fg)/(2h^\vee)$ and
+$\kappa = \kappa_{\mathrm{dp}} + \dim(\fg)/2
+= \dim(\fg)\cdot(k + h^\vee)/(2h^\vee)$
+is a single scalar shadow. The Casimir tensor determines the braiding
 on the category of representations; the modular
 characteristic determines the genus-$1$ anomaly.  These are
 different structural data at different categorical depths.
diff --git a/chapters/theory/e1_modular_koszul.tex b/chapters/theory/e1_modular_koszul.tex
index a8a83c93d1d8dc248f8f9f6309990c5a7602c6c4..041dea657991f4089b4f0404b429bf3fff9ad079
--- a/chapters/theory/e1_modular_koszul.tex
+++ b/chapters/theory/e1_modular_koszul.tex
@@ -2255,8 +2255,11 @@
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item $(K_\cA^{E_1})_{0,2} = r(z)$, the classical $r$-matrix
  \textup{(}genus~$0$, degree~$2$\textup{)}. The coinvariant
- $\operatorname{av}(r(z)) = \kappa(\cA)$ recovers the scalar
- curvature.
+ $\operatorname{av}(r(z))$ recovers the scalar degree-$2$ shadow:
+ on abelian families $\operatorname{av}(r(z)) = \kappa(\cA)$,
+ while for non-abelian affine Kac--Moody
+ $\operatorname{av}(r(z)) = \kappa_{\mathrm{dp}}(\cA)$ and
+ $\kappa(\cA) = \kappa_{\mathrm{dp}}(\cA) + \dim(\fg)/2$.
 \item $(K_\cA^{E_1})_{0,3} = \Phi_{\mathrm{KZ}}(\cA)$, the
  KZ\slash Drinfeld associator \textup{(}genus~$0$, degree~$3$,
  for affine algebras;
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 789ce9acf5b68f150a665afd1b7486e6b1256a16..09413d565658e9d71f63d7dd7327bf183c8a1ea7
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -895,8 +895,12 @@
 
 \item \emph{Leading-order modular shadow.}
  The $\Sigma_2$-coinvariant projection
- $\operatorname{av}(r(z)) = \kappa(\cA)$ is the modular
- characteristic, the first entry of the shadow obstruction tower
+ $\operatorname{av}(r(z))$ is the leading scalar shadow: it equals
+ $\kappa(\cA)$ on abelian and scalar families, while for
+ non-abelian affine Kac--Moody it gives
+ $\kappa_{\mathrm{dp}}(\cA)$ and the full modular characteristic is
+ $\kappa(\cA) = \kappa_{\mathrm{dp}}(\cA) + \dim(\fg)/2$. This is
+ the first entry of the shadow obstruction tower
  \textup{(}equation~\textup{\eqref{eq:intro-kappa-from-r}};
  Theorem~\textup{\ref{thm:e1-primacy}}\textup{)}. The residue contains
  a matrix-valued refinement; averaging produces the scalar.
@@ -1262,17 +1266,18 @@
 \;=\;
 \Theta_\cA.
 \end{equation}
-At degree~$2$, this projection records only one number: the
-$\Sigma_2$-coinvariant of the residue of $r(z)$ at $z = 0$ is the
-modular characteristic
+At degree~$2$, this projection records only one scalar: the
+$\Sigma_2$-coinvariant of the residue of $r(z)$ at $z = 0$ is
 \begin{equation}\label{eq:intro-kappa-from-r}
-\kappa(\cA)
-\;=\;
 \operatorname{av}\bigl(r(z)\bigr)
 \;=\;
 \tfrac{1}{2}\,\operatorname{tr}\!\bigl[\Res_{z = 0} r(z)\bigr],
 \end{equation}
 where the trace is the cyclic trace on $\End(V^{\otimes 2})$.
+For abelian and scalar families,
+\[
+\kappa(\cA) = \operatorname{av}\bigl(r(z)\bigr).
+\]
 For the affine Kac--Moody vacuum algebra $V_k(\mathfrak{g})$ at
 non-critical level, the averaging formula
 \eqref{eq:intro-kappa-from-r} specializes to the Sugawara identity
@@ -1652,8 +1657,11 @@
 at the $R$-matrix level beyond what the local OPE already carries.
 Tier (b) is still $\Einf$-chiral in the three-leaps classification of
 Volume~II: the algebra is commutative up to quasi-isomorphism, and
-averaging recovers the modular shadow $\kappa$ without information
-loss beyond the $\Sigma_n$-coinvariant step.
+averaging recovers the scalar degree-$2$ shadow without
+information loss beyond the $\Sigma_n$-coinvariant step: this is
+$\kappa$ on abelian and scalar families, while for non-abelian
+affine Kac--Moody it is $\kappa_{\mathrm{dp}}$ and the full
+modular characteristic adds the Sugawara shift $\dim(\fg)/2$.
 
 Tier (c) is the genuinely $\Eone$-primitive extreme. The Yangian
 $Y(\mathfrak g)$ and the Etingof--Kazhdan quantum vertex algebras
diff --git a/standalone/chiral_chern_weil.tex b/standalone/chiral_chern_weil.tex
index 264bc812bc756f693683ea49fffc92a69ba23fb8..e925297230a043684b2162d6eea950832e71b362
--- a/standalone/chiral_chern_weil.tex
+++ b/standalone/chiral_chern_weil.tex
@@ -1213,7 +1213,11 @@
 % ================================================================
 \section{The chiral curvature}\label{sec:chiral-cw}
 
-The averaging map extracts~$\kappa$ from the $r$-matrix.
+The averaging map extracts the scalar degree-$2$ shadow from the
+$r$-matrix: this is~$\kappa$ on abelian and scalar families, while
+for non-abelian affine Kac--Moody the averaged scalar is
+$\kappa_{\mathrm{cl}}$ and the full modular characteristic is
+$\kappa = \kappa_{\mathrm{cl}} + \dim(\fg)/2$.
 The question it forces is: what role does~$\kappa$ play
 geometrically? The answer: $\kappa$ is the proportionality
 constant of a curvature. The bar differential, which squares
diff --git a/standalone/shadow_towers_v3.tex b/standalone/shadow_towers_v3.tex
index 3e3cf779de2c8653d94026ee31a290ce83cfcba7..12a1cee9e29af47da9fba8082a62d08db7d85eb3
--- a/standalone/shadow_towers_v3.tex
+++ b/standalone/shadow_towers_v3.tex
@@ -1846,10 +1846,12 @@
 $\Theta_\cA^{E_1}$ projects to~$\Theta_\cA$ under
 $\mathrm{av}$. The degree-$2$ component of
 $\Theta_\cA^{E_1}$ is the $R$-matrix $r(z)$, and its
-average is the modular characteristic~$\kappa$, with the
-Sugawara correction for non-abelian algebras arising from
-the simple-pole self-contraction of the ordered two-point
-function. The higher degrees follow by the same averaging
+average is the scalar degree-$2$ shadow: it equals the modular
+characteristic~$\kappa$ on abelian families, while for
+non-abelian affine Kac--Moody the average is
+$\kappa_{\mathrm{dp}}$ and the full~$\kappa$ adds the
+Sugawara correction from the simple-pole self-contraction of the
+ordered two-point function. The higher degrees follow by the same averaging
 applied to the degree-$r$ MC components.
 \end{proof}
 
@@ -1873,7 +1875,11 @@
 The $E_1$ convolution algebra
 $\mathfrak{g}^{E_1}_\cA$ carries a spectral $R$-matrix
 $r(z) \in \mathrm{End}(V \otimes V)((z))$ at degree~$2$,
-whose averaging produces~$\kappa$. The structure of $r(z)$
+whose averaging produces the scalar degree-$2$ shadow:
+for abelian families this is~$\kappa$, while for non-abelian
+affine Kac--Moody it is~$\kappa_{\mathrm{dp}}$ and the full
+modular characteristic is
+$\kappa = \kappa_{\mathrm{dp}} + \dim(\fg)/2$. The structure of $r(z)$
 varies by class.
 
 \begin{example}[Class $\mathbf{G}$:
diff --git a/standalone/survey_track_a_compressed.tex b/standalone/survey_track_a_compressed.tex
index cb62bb8b88937153678a962d34c4c5dac04b9700..084c11fb005499137646a882cff6cb86a1becc01
--- a/standalone/survey_track_a_compressed.tex
+++ b/standalone/survey_track_a_compressed.tex
@@ -361,11 +361,17 @@
 \]
 a matrix-valued rational function encoding the full binary OPE data.
 Applying $\mathrm{av}$ at degree~$2$ collapses the profile to a single
-scalar,
+scalar shadow:
 \begin{equation}\label{eq:av-organizing}
-\mathrm{av}\bigl(r(z)\bigr)\;=\;\kappa(\cA),
+\begin{aligned}
+\mathrm{av}\bigl(r(z)\bigr) &= \kappa(\cA)
+&& \text{for abelian and scalar families},\\
+\mathrm{av}\bigl(r(z)\bigr) &= \kappa_{\mathrm{dp}}(\cA), \qquad
+\kappa(\cA) = \kappa_{\mathrm{dp}}(\cA) + \dim(\fg)/2
+&& \text{for non-abelian affine Kac--Moody.}
+\end{aligned}
 \end{equation}
-the modular characteristic of Theorem~D. At degree~$3$ the KZ
+This is the modular characteristic package of Theorem~D. At degree~$3$ the KZ
 associator projects to the cubic shadow~$\mathfrak C$; at degree~$4$
 the Yangian higher coproduct projects to the quartic resonance
 class~$\mathfrak Q$. Each degree-$n$ component of the ordered

tokens used
111,636
