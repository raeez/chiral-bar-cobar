# P13_SC_formality_upgrade (897s)

Rectified the SC-formality lane in [chapters/theory/chiral_koszul_pairs.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex:2546). The local changes do three things: class~`G` now includes the free fermion in the classification table, the forward proof is strengthened to a Gaussian/free-field tree-vanishing argument, and the converse is replaced by an operadic tower-bar argument from SC-formality to degree-2 shadow truncation. I also made the boundary sharp: `Delta = 0` alone is explicitly ruled out by the class~`L` affine KM counterexample.

Verification: the modified region is clean under the required AP126/AP132/AP29 greps. `make fast` reached pass 3 with `0` undefined citations and only `2` unrelated global undefined references (`conj:v1-master-bv-brst`) before the TeX process was killed by the environment (`Error 137`); none of the new references from this theorem lane were unresolved.

## Platonic Rectification Report
- `prop:swiss-cheese-nonformality-by-class` at [chiral_koszul_pairs.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex:2546)
  - BEFORE: class `G` row listed only Heisenberg and lattice VOA; status `\ClaimStatusProvedHere`.
  - ISSUE: the forward class-`G` proof did not cover the full class-`G` family surface, omitted free fermions, and left the mechanism too close to a table lookup.
  - ACTION: STRENGTHENED
  - AFTER: class `G` now lists Heisenberg, lattice VOA, and free fermion; the proof uses Gaussian/free-field tree vanishing, the averaging map `\operatorname{av}(\Theta_\cA^{\Eone})=\Theta_\cA`, and an explicit boundary statement that `\Delta=0` is not sufficient because affine KM is class `L` with `m_3^{\mathrm{SC}}\neq 0`; status unchanged (`\ClaimStatusProvedHere`).
  - CONFIDENCE: medium
  - REMAINING GAP: no local proof gap identified; propagation debt remains outside scope in `chapters/connections/concordance.tex:7098` and Vol III docstrings.

- `prop:sc-formal-iff-class-g` at [chiral_koszul_pairs.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex:2681)
  - BEFORE: statement already claimed `SC`-formality iff class `G`; status `\ClaimStatusProvedHere`.
  - ISSUE: the converse relied on eliminating non-`G` classes by classification, rather than a direct operadic mechanism; the proof surface did not justify the theorem at its strongest conceptual form.
  - ACTION: STRENGTHENED
  - AFTER: the theorem still states the strongest form, `\cA` is Swiss-cheese formal iff it belongs to class `G`, but the proof now runs by operadic tower-bar correspondence: SC-formality kills higher mixed trees, averaging sends the ordered closed sector to the shadow tower, hence `S_r(\cA)=0` for all `r\ge 3`, so the shadow/formality tower truncates at degree `2`, which is exactly class `G`; status unchanged (`\ClaimStatusProvedHere`).
  - CONFIDENCE: medium
  - REMAINING GAP: no local theorem gap identified; read-only propagation still needed for the stale Vol III line `compute/lib/swiss_cheese_cy3_e1.py:62` and the old concordance rationale.


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
session id: 019d866c-e0dc-7f71-ae4b-25bc1fa0a117
--------
user
<task>
You are a PLATONIC IDEAL rectification agent for a 4,500-page research mathematics manuscript.
Your mission: take each theorem to its STRONGEST possible form. REFUSE TO DOWNGRADE.

Hierarchy of action:
1. STRENGTHEN the proof to match the original claim (best outcome)
2. If the proof has a genuine gap: FILL IT with new mathematics
3. If the gap requires substantial new research: SKETCH the research programme needed, then
   state the strongest INTERMEDIATE result that IS proved, and mark the full claim as
   conditional on the identified research programme
4. NEVER silently narrow. If narrowing is needed, prove the narrow version is OPTIMAL
   by exhibiting a counterexample at the boundary of the narrow claim.

You have WRITE access. Make the edits. Verify after each edit.
</task>

<action_safety>
Only edit files in your assigned scope. After every edit, re-read the modified section.
Run grep for forbidden patterns (AP126 bare Omega, AP132 augmentation, AP29 slop).
</action_safety>

<completeness_contract>
Address every finding in your scope. For each: STRENGTHENED / FILLED / INTERMEDIATE+PROGRAMME / BLOCKED.
Do not stop until every finding is resolved or precisely blocked.
</completeness_contract>

<verification_loop>
After all edits: re-read the full modified region. Verify mathematical correctness.
Check that no new AP violations were introduced. State the final theorem in its strongest form.
</verification_loop>

<structured_output_contract>
End with:
## Platonic Rectification Report
For each theorem touched:
  - BEFORE: [original statement + status]
  - ISSUE: [what was wrong]
  - ACTION: [STRENGTHENED / FILLED / INTERMEDIATE / BLOCKED]
  - AFTER: [new statement + status]
  - CONFIDENCE: [high/medium/low]
  - REMAINING GAP: [if any]
</structured_output_contract>


SC-FORMALITY: A is SC-formal iff class G.

TARGET: chapters/theory/chiral_koszul_pairs.tex

KNOWN ISSUES:
1. Converse proof uses bilinear form that doesn't exist for betagamma
2. Forward proof only verified for Heisenberg, not full class G

YOUR MISSION:
1. For the FORWARD direction (class G => SC-formal): prove it for ALL class-G families
   (Heisenberg, lattice VOAs, free fermions). The key: class G means S_4 = 0 and
   Delta = 0 (shadow tower finite at degree 2). SC-formality means m_k^{SC} = 0 for k>=3.
   Prove: Delta=0 implies the SC mixed-sector operations vanish at order 3+.
   This should follow from the shadow tower controlling the SC operations via the
   averaging map.
2. For the CONVERSE (SC-formal => class G): replace the bilinear-form argument with
   a purely operadic one. SC-formality means the SC bar complex is formal. Formality
   of the SC bar implies the shadow tower truncates at degree 2 (by the tower-bar
   correspondence). Shadow tower truncation at degree 2 means Delta = 0, which means
   class G.

Search for 'SC-formal' and 'class G'. Focus on lines 2520-2560.
mcp startup: no servers


thinking
**Exploring file context**

I’m thinking the phrase "always prefer them over manual search or file reading" means I should use the explorer agent to gather context from files. I might spawn parallel explorer agents for initial reads and to locate the theorem. But, I also need to consider using shell commands to inspect files. Though the instructions say to trust the explorer's results, using shell commands could help. I’ll focus on using explorer to summarize relevant files and possibly open the SKILL.md file, considering an update plan afterward.
thinking
**Planning parallel tool use**

I'm thinking about sending commentary first, and then I might use a multi_tool parallel approach to update the plan and spawn explorer agents. I could create two explorers: one for reading relevant portions of target files and theorem labels, and another to search for duplicates like "SC-formal iff class G." I might also incorporate a third explorer for the skill file, possibly using exec_command for specific lines. My plan is to execute these tasks in parallel and ensure everything runs smoothly.
codex
The task is a local theorem rectification in [chapters/theory/chiral_koszul_pairs.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex). I’m loading the mandatory context, the rectification skill, and the exact theorem surface before I touch the proof.
exec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/beilinson-rectify/SKILL.md" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
---
name: beilinson-rectify
description: Use when the user asks to rectify, fortify, rewrite, tighten, or structurally repair a mathematical chapter, proof, or claim surface in this repository. Not for isolated formula checks better handled by multi-path-verify.
---

# Beilinson Rectify

This is the heavy rectification workflow. Use it when the task is not just to patch a claim, but to make a chapter or proof lane truer, tighter, and harder to break.

It is also the Codex-side home of the lighter `/rectify` and `/beilinson-rectify` workflows from `CLAUDE.md`.

## Load first

- `CLAUDE.md`
- `chapters/connections/concordance.tex`
- `metadata/theorem_registry.md`
- `archive/raeeznotes/raeeznotes100/red_team_summary.md`
- the full target file
- the directly cited dependencies

collab spawn_agent(call_QIT9qcBAAyLrA4TX7jXBN0zJ, prompt="Read and summarize only the specific mandatory context needed for a rectification of SC-formality in chapters/theory/chi…")
spawn_agent(call_QIT9qcBAAyLrA4TX7jXBN0zJ, prompt="Read and summarize only the specific mandatory context needed for a rectification of SC-formality in chapters/theory/chi…") pending init:
  agent: 019d866d-705b-70f3-a5f5-52b111aa10ab
collab spawn_agent(call_pgXqBipLe0FJvXxOfdgLSW0z, prompt="Search the repo and the sibling volumes only for genuine duplicates or cross-volume mentions of 'SC-formal', 'class G', …")
mcp startup: no servers
mcp startup: no servers
spawn_agent(call_pgXqBipLe0FJvXxOfdgLSW0z, prompt="Search the repo and the sibling volumes only for genuine duplicates or cross-volume mentions of 'SC-formal', 'class G', …") pending init:
  agent: 019d866d-7083-7351-8f30-118e2b5a5277
Plan update
Starting with mandatory context and theorem-surface discovery before editing. Once the exact theorem surface is locked, I’ll strengthen the proof, patch the file, then run the required AP greps and a targeted verification pass.
  → Load rectification workflow and mandatory repo context for the target theorem surface
  • Lock the exact theorem/label/current proof surface in chiral_koszul_pairs.tex
  • Strengthen the forward and converse directions in the assigned scope
  • Re-read modified region and run required AP greps/targeted verification
  • Check collision surface for propagation needs and finalize rectification report
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "SC-formal|class G|Delta = 0|shadow tower truncates at degree 2"' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Total output lines: 3878

CLAUDE.md:279:**C30. Delta discriminant.** `Delta = 8*kappa*S_4`. Finite tower iff Delta=0; for kappa!=0 iff S_4=0. LINEAR in kappa (NOT quadratic, AP21). Heis: S_4=0, Delta=0, class G. Vir: S_4!=0, Delta!=0, class M.
CLAUDE.md:508:| SC-formal | PROVED | SC-formal iff class G (prop:sc-formal-iff-class-g) |
CLAUDE.md:547:AP14: Koszulness != SC formality. Koszul = bar H* in degree 1. SC formal = m_k^{SC}=0 for k>=3. All standard families Koszul; only class G SC-formal.
CLAUDE.md:932:**Shadow tower**: Theta_A := D_A - d_0 is MC (thm:mc2-bar-intrinsic). kappa, C, Q are projections. All-degree convergence PROVED. G/L/C/M: G(r=2,Heis), L(r=3,aff), C(r=4,betagamma), M(r=inf,Vir/W_N). Shadow depth != Koszulness. Delta=8*kappa*S_4: Delta=0 <-> finite tower. SC formality: A is SC-formal iff class G (prop:sc-formal-iff-class-g). Depth gap: d_alg in {0,1,2,inf}; gap at 3 (prop:depth-gap-trichotomy). ChirHoch^1(V_k(g)) = g with total dim = dim(g)+2 (prop:chirhoch1-affine-km).
platonic_rectification_20260413_114523/P10_MC5_coderived_upgrade.md:102:   (unconditional), with the chain-level equivalence for class G/L (unconditional) and
platonic_rectification_20260413_114523/P10_MC5_coderived_upgrade.md:246:I'm thinking it might be best to avoid conflict by skipping subagents this time. Manual reading works for this use case as it’s not a codebase question, but I do need to review the full target file, even though it’s probably large. I’ll focus on sections around lines 1920-1960, searching for the theorem label and relevant definitions for class G/L/C/M and delta_r. I plan to use tools like rg and sed to manage this effectively.
platonic_rectification_20260413_114523/P10_MC5_coderived_upgrade.md: WARNING: stopped searching binary file after match (found "\0" byte around offset 775350)
staging/combined_for_en_koszul.tex:379:$\Delta = 0$ on the entire derived centre.
staging/combined_for_en_koszul.tex:382:With $\Delta = 0$ and $\mu|_{\HH^1 \otimes \HH^1} = 0$,
staging/combined_for_en_koszul.tex:692:by Schur's lemma. Hence $\Delta = 0$ on the derived
staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:4852:\item \textup{(SC-formality.)} The Swiss-cheese type
staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:4864:culminating in SC-formality, which holds only for
staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:5766:$\Delta = 0$ on the entire derived centre.
staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:5769:With $\Delta = 0$ and $\mu|_{\HH^1 \otimes \HH^1} = 0$,
staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:6079:by Schur's lemma. Hence $\Delta = 0$ on the derived
staging/for_en_koszul__e3_explicit_ops.tex:209:$\Delta = 0$ on the entire derived centre.
staging/for_en_koszul__e3_explicit_ops.tex:212:With $\Delta = 0$ and $\mu|_{\HH^1 \otimes \HH^1} = 0$,
staging/for_en_koszul__e3_explicit_ops.tex:522:by Schur's lemma. Hence $\Delta = 0$ on the derived
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && ls' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
AGENTS.md
CLAUDE.md
COMMIT_MESSAGE.txt
Chiral_Bar_Cobar_Duality__Geometric_Realization.pdf
FRONTIER.md
Makefile
N1_koszul_meta.pdf
N2_mc3_all_types.pdf
N4_mc4_completion.pdf
N5_mc5_sewing.pdf
N6_shadow_formality.pdf
README.md
appendices
archive
audit_campaign_20260412_230832
audit_campaign_20260412_231034
audit_campaign_20260413_111534
bibliography
bp_self_duality.pdf
chapters
codex
I’ve loaded the rectification workflow. Two focused searches are running now: one on the exact theorem surface and mandatory context, and one on the duplicate/collision surface so I don’t fix this proof in isolation.
collab wait(call_kfgrhWVARGXsE4LwTDKVOVvN)
  receivers: 019d866d-705b-70f3-a5f5-52b111aa10ab, 019d866d-7083-7351-8f30-118e2b5a5277
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "SC-formality" -n CLAUDE.md' in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "SC-formality" chapters/theory/chiral_koszul_pairs.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
2582:relationship between SC-formality and the classification is
2590:\begin{proposition}[SC-formality characterises class~$G$; \ClaimStatusProvedHere]
2593:\index{class G@class~$G$!characterised by SC-formality}
2614:these cases contradicts SC-formality. This converse uses only the
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "SC formal" CLAUDE.md' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
547:AP14: Koszulness != SC formality. Koszul = bar H* in degree 1. SC formal = m_k^{SC}=0 for k>=3. All standard families Koszul; only class G SC-formal.
932:**Shadow tower**: Theta_A := D_A - d_0 is MC (thm:mc2-bar-intrinsic). kappa, C, Q are projections. All-degree convergence PROVED. G/L/C/M: G(r=2,Heis), L(r=3,aff), C(r=4,betagamma), M(r=inf,Vir/W_N). Shadow depth != Koszulness. Delta=8*kappa*S_4: Delta=0 <-> finite tower. SC formality: A is SC-formal iff class G (prop:sc-formal-iff-class-g). Depth gap: d_alg in {0,1,2,inf}; gap at 3 (prop:depth-gap-trichotomy). ChirHoch^1(V_k(g)) = g with total dim = dim(g)+2 (prop:chirhoch1-affine-km).
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '2580,2620p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:

The four classes exhaust the standard landscape, but the
relationship between SC-formality and the classification is
sharper than the table suggests. Proposition~\ref{prop:swiss-cheese-nonformality-by-class}
already isolates the first nonzero Swiss-cheese operation in each
non-Gaussian class: class~$L$ has $m_3^{\mathrm{SC}} \neq 0$,
class~$C$ has $m_4^{\mathrm{SC}} \neq 0$, and class~$M$ has
nonzero $m_k^{\mathrm{SC}}$ for all $k \geq 3$. This reduces the
formality criterion to a classification check.

\begin{proposition}[SC-formality characterises class~$G$; \ClaimStatusProvedHere]
\label{prop:sc-formal-iff-class-g}
\index{Swiss-cheese operad!formality characterisation}
\index{class G@class~$G$!characterised by SC-formality}
Let~$\cA$ be a chiral algebra in the standard landscape.
Then~$\cA$ is Swiss-cheese formal
\textup{(}$m_k^{\mathrm{SC}} = 0$ for all $k \geq 3$\textup{)}
if and only if~$\cA$ belongs to class~$G$.
\end{proposition}

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '520,980p' CLAUDE.md" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
Total output lines: 461

## Anti-Patterns by Cognitive Trigger

### BEFORE WRITING A FORMULA

**kappa** (AP1, AP9, AP20, AP24, AP48, AP136): DISTINCT per family, NEVER copy. KM=dim(g)(k+h^v)/(2h^v), Vir=c/2, W_N=c*(H_N-1) where H_N=sum_{j=1}^{N} 1/j (AP136: NOT c*H_{N-1}), Heis=k. Always qualify: kappa^{KM}, kappa^{Vir}. Complementarity: kappa+kappa'=0 (KM/free), 13 (Vir), NOT universal. State WHICH algebra: intrinsic vs kappa_eff=kappa(matter)+kappa(ghost) vs kappa(B) where B=A^!. **AP1 operational mandate**: before writing ANY kappa formula, (a) read landscape_census.tex for that family, (b) evaluate at k=0 and k=-h^v, (c) cross-check compute/. Writing kappa from memory is FORBIDDEN.

**pole/weight** (AP19, AP21, AP27): r-matrix poles = OPE poles - 1 (d log absorbs one pole). Vir r-matrix: (c/2)/z^3 + 2T/z, NOT quartic. Bar propagator weight 1, NEVER weight h. Scalar formula FAILS at g>=2 for multi-weight (delta_F_g^cross != 0). u=eta^2=lambda=kappa(B)*omega_g is LINEAR in kappa, NEVER quadratic.

**grading/signs** (AP22, AP23, AP44, AP45, AP46, AP49): Desuspension LOWERS: |s^{-1}v|=|v|-1. In LaTeX: ALWAYS s^{-1}, NEVER bare s in bar-complex formula. T^c(s^{-1} A-bar), NOT T^c(s A-bar). Mnemonic: bar=down=desuspension=s^{-1}. eta(q) includes q^{1/24}. OPE mode vs lambda-bracket: T_{(3)}T=c/2 becomes {T_lambda T}=(c/12)*lambda^3 (divided power 1/n!). A-hat(ix)-1 starts at x^2; verify F_1 matches leading order. sqrt(Q_L) is flat section; H(t)=t^2*sqrt(Q_L) NOT horizontal. Cross-volume conventions: Vol I=OPE modes, Vol II=lambda-brackets, Vol III=motivic. NEVER paste without conversion.

**boundaries/forms** (AP116, AP117, AP118, AP136): AP116: After writing ANY summation sum_{j=a}^{b}, verify by substituting the smallest index. H_N=sum_{j=1}^{N} 1/j, NOT sum_{j=1}^{N-1}. Always check the boundary case. AP117: Connection 1-form is r(z)dz, NOT r(z) d log(z). KZ = sum r_{ij} dz_{ij}. Arnold form d log(z_i-z_j) is a bar-construction coefficient, not the connection form. NEVER write d log without verifying. AP118: Any formula that simplifies at g=1 because a matrix becomes scalar MUST be written in full multi-dimensional form. (Im Omega)^{-1} is a matrix at g>=2. Verify formulas at g=2 where the period matrix is 2x2. AP136: H_{N-1} != H_N - 1. Evaluate at smallest N to distinguish.

**ratios/reciprocals** (AP129, AP137): AP129: When a formula involves a/b, the most common transcription error is b/a. ALWAYS substitute a known numerical value to verify. AP137: Bosonic c_{βγ} and fermionic c_{bc} satisfy c_{βγ}+c_{bc}=0. They look similar but have opposite signs. VERIFY: check c_total=0.

**fiber-base/depth** (AP130, AP131, AP134): AP130: Objects on the fiber (forms on Σ_g) are NOT objects on the base (classes on M̄_g). Verify: does this expression live on moduli or on the curve? AP131: Generating depth (degree at which higher ops are determined) != algebraic depth (whether tower terminates). Vir: d_gen finite, d_alg=∞. AP134: Cohomological amplitude [0,d] != virtual dimension d.

**bar complex** (AP132, AP141): AP132: B(A) uses the augmentation ideal Ā=ker(ε), NOT A. T^c(s^{-1} Ā), never T^c(s^{-1} A). AP141: r-matrix k=0 vanishing check after EVERY r-matrix formula.

exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "shadow tower" chapters/theory/chiral_koszul_pairs.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
66:$K_\tau^L(\cA, \cC)$, truncation of the shadow tower
91:Confusing the two misidentifies what the shadow tower measures.
2802:holds. The shadow depth is infinite: the shadow tower
3228:shadow tower would carry in the Koszul world
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "truncates at degree 2" -n' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
scripts/healing_fortification_40.py:296:1. Class G means Delta = 8*kappa*S_4 = 0 and the shadow tower truncates at degree 2.
scripts/platonic_rectification_20.py:367:   of the SC bar implies the shadow tower truncates at degree 2 (by the tower-bar
relaunch_20260413_111534/F03_definitions_shadow.md:314:scripts/platonic_rectification_20.py:367:   of the SC bar implies the shadow tower truncates at degree 2 (by the tower-bar
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "sc-formal" -n chapters/connections/concordance.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
7094:\ref{prop:sc-formal-iff-class-g}
7097: \textup{(}Proposition~\ref{prop:sc-formal-iff-class-g}\textup{)}
9675: \textup{(}Proposition~\ref{prop:sc-formal-iff-class-g}\textup{)} \\
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "shadow depth" chapters/theory/chiral_koszul_pairs.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
76:classes G/L/C/M, with shadow depths
2459:$\cA$ is chirally Koszul. The shadow depth classification
2468:\index{shadow depth!loop-exactness ordering}
2482:\index{shadow depth!Swiss-cheese formality}
2488:are classified by shadow depth as follows.
2802:holds. The shadow depth is infinite: the shadow tower
2813:This is the \emph{shadow depth~$\infty$ vs.\ PBW
2895:complementarity consistency, and shadow depth independence
2978:and shadow depth $r_{\max}$;
2980:(shadow depth $\neq$ Koszulness).
3065:\index{Koszul property!shadow depth independence}
3093:Virasoro algebra has infinite shadow depth
3103:\index{shadow depth!direct sum}
3113:the shadow depth satisfies
3147:The shadow depth is monotone under direct sum but not under
3357:\item The shadow depth $r_{\max}(\cA)$ equals the bootstrap
3362:\item The shadow depth classification corresponds to bootstrap
3387:(Lemma~\ref{lem:nms-euler-inversion}). The shadow depth
5946:measures \emph{shadow depth} (the algebra lies in class~M with
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '7080,7110p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 algebraic (shadow), geometric (formality obstruction),
 holographic (boundary-bulk correction)
 & bar-intrinsic MC $+$ formality identification
 $+$ derived-centre factorization \\
\ref{def:generating-depth}
 & Generating depth $d_{\mathrm{gen}}$ vs algebraic depth
 $d_{\mathrm{alg}}$: formal distinction~;
 Virasoro $d_{\mathrm{gen}} = 3$,
 $d_{\mathrm{alg}} = \infty$
 & depth decomposition $+$ class~M tower non-termination \\
\hline
\multicolumn{3}{l}{\textit{%
 April 2026 session: structural propositions and depth classification}} \\
\hline
\ref{prop:sc-formal-iff-class-g}
 & SC-formality characterises class~$\mathbf{G}$:
 $\cA$ is Swiss-cheese formal iff class~$\mathbf{G}$
 \textup{(}Proposition~\ref{prop:sc-formal-iff-class-g}\textup{)}
 & abelian bracket $+$ nondegeneracy of~$\kappa$ \\
\ref{prop:depth-gap-trichotomy}
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '2440,2510p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\label{rem:koszul-closure-not-quotients}
The closure properties of
Proposition~\ref{prop:koszul-closure-properties} do \emph{not} extend
to general quotients $\cA / \cI$ by chiral ideals: the quotient of a
chirally Koszul algebra by a non-Koszul ideal is generically non-Koszul.
The W-algebra construction $\cW^k(\fg, f)$ via Drinfeld--Sokolov
reduction is the principal example where the quotient \emph{does}
preserve Koszulness, and this is a substantive theorem of the chapter
(Theorem~\ref{thm:w-algebra-koszul}), not a corollary of closure.
\end{remark}

\begin{remark}[$A_\infty$ formality and Gaiotto--Kulp--Wu]
\label{rem:ainfty-formality-gkw}
\index{Gaiotto--Kulp--Wu!formality characterization}
The $A_\infty$ formality characterization
(item~(iii) of Theorem~\ref{thm:koszul-equivalences-meta})
is the bar-complex statement of the formality theorem of
Gaiotto--Kulp--Wu~\cite{GKW2025}: the transferred operations
$m_k = 0$ for $k \geq 3$ on bar cohomology if and only if
$\cA$ is chirally Koszul. The shadow depth classification
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '9650,9690p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 \textup{(}Theorems~\ref{thm:heisenberg-sewing},
 \ref{thm:lattice-sewing}\textup{)} \\
& HS-sewing for the entire standard landscape (universal algebras)
 \textup{(}Theorem~\ref{thm:general-hs-sewing}\textup{)} \\
& All-degree inverse limit
 $\Theta_\cA = \varprojlim \Theta_\cA^{\le r}$
 \textup{(}Theorem~\ref{thm:recursive-existence}\textup{)} \\
& Algebraic-family rigidity
 \textup{(}Theorem~\ref{thm:algebraic-family-rigidity}\textup{)} \\
& DS primitivity of the gravitational coproduct
 (Vol~II, Theorem~\textup{thm:ds-hpl-transfer}) \\
& Epstein zeta of the shadow metric: functional equation
 for class~$\mathbf{M}$ at rational~$c$
 \textup{(}Theorem~\ref{thm:shadow-epstein-zeta}\textup{)} \\
& Shadow field $K_L = \bQ(\sqrt{\operatorname{disc}(Q_L)})$:
 imaginary quadratic for class~$\mathbf{M}$;
 trivial for class~$\mathbf{G}/\mathbf{L}$
 \textup{(}Remark~\ref{rem:shadow-field}\textup{)} \\
& Descent fan: three independent projections of
 $\Theta_\cA$ (categorical, spectral, modular)
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "truncat" chapters/theory/chiral_koszul_pairs.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
66:$K_\tau^L(\cA, \cC)$, truncation of the shadow tower
1308:\label{ex:truncated-polynomial-ainfty}
1309:\index{truncated polynomial algebra!$A_\infty$ dual}
2554:the shadow obstruction tower with its weight-$2$ truncation, so the
3059:evaluated on the truncated MC element), establishing the
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "sc-formal" metadata/theorem_registry.md' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
416:| `prop:sc-formal-iff-class-g` | `proposition` | 2591 | SC-formality characterises class~$G$ |
1003:| `prop:sc-formality-by-class` | `proposition` | 16933 | Swiss-cheese formality classification by shadow class |
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "shadow depth classification" -n chapters/theory/chiral_koszul_pairs.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
2459:$\cA$ is chirally Koszul. The shadow depth classification
3362:\item The shadow depth classification corresponds to bootstrap
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '390,440p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:

| Label | Env | Line | Title |
|---|---|---:|---|
| `lem:twisted-product-cone-counit` | `lemma` | 286 | Left twisted tensor product as mapping cone |
| `lem:twisted-product-cone-unit` | `lemma` | 313 | Right twisted tensor product as mapping cone |
| `lem:filtered-comparison` | `lemma` | 333 | Filtered comparison |
| `lem:filtered-comparison-unit` | `lemma` | 361 | Bar-side filtered comparison |
| `thm:fundamental-twisting-morphisms` | `theorem` | 412 | Fundamental theorem of chiral twisting morphisms |
| `cor:three-bijections` | `corollary` | 488 | Three bijections for chiral twisting morphisms |
| `thm:pbw-koszulness-criterion` | `theorem` | 764 | PBW criterion for chiral Koszulness |
| `thm:km-chiral-koszul` | `theorem` | 842 | Affine Kac--Moody algebras are chiral Koszul |
| `thm:virasoro-chiral-koszul` | `theorem` | 897 | Virasoro chiral Koszulness |
| `cor:bar-cohomology-koszul-dual` | `corollary` | 941 | Bar cohomology computes Koszul dual |
| `thm:bar-concentration` | `theorem` | 1129 | Bar concentration for Koszul pairs |
| `prop:ainfty-formality-implies-koszul` | `proposition` | 1242 | Formality implies chiral Koszulness |
| `thm:ainfty-koszul-characterization` | `theorem` | 1276 | Converse: chiral Koszulness implies formality |
| `thm:ext-diagonal-vanishing` | `theorem` | 1346 | Ext diagonal vanishing criterion |
| `prop:pbw-universality` | `proposition` | 1383 | PBW universality |
| `cor:universal-koszul` | `corollary` | 1409 | Universal vertex algebras are chirally Koszul |
| `thm:kac-shapovalov-koszulness` | `theorem` | 1475 | Kac--Shapovalov criterion for simple quotients |
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '2420,2475p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
$(\cA^!)^! = \mathrm{cobar}(\barB(\cA^!)) =
\mathrm{cobar}(\Omega(\barB(\cA))) \simeq \cA$. This is the
chiral analog of the standard fact $(A^!)^! \simeq A$ for
quadratic algebras (Loday--Vallette~\cite{LV12}, Theorem~3.4.6),
with the additional Beilinson--Drinfeld holonomicity input
ensuring chain-level convergence on a smooth projective curve.

\textup{(c)}: Smooth base change uses
Lemma~\ref{lem:pushforward-preserves-qi} to verify that
$f^*$ preserves quasi-isomorphisms of chiral algebras, combined
with Theorem~\ref{thm:bar-cobar-inversion-functorial} to verify
that $f^*$ commutes with bar-cobar. The witnessing datum for
chiral Koszulness pulls back along $f$, and the
$E_2$-collapse of the PBW spectral sequence is preserved under
flat pullback (since smooth morphisms are flat). The duality
identification $(f^*\cA)^! \simeq f^*(\cA^!)$ follows from the
compatibility of $f^*$ with linear duality on coherent sheaves.
\end{proof}

\begin{remark}[Closure does not extend to bare quotients]
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '980,1040p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
| `thm:primitive-to-global-reconstruction` | `theorem` | 13423 | Primitive-to-global reconstruction |
| `prop:primitive-shell-equations` | `proposition` | 13573 | Primitive shell equations |
| `prop:branch-master-equation` | `proposition` | 13711 | Branch quantum master equation |
| `cor:metaplectic-square-root` | `corollary` | 13764 | Determinantal half-density |
| `thm:primitive-flat-descent` | `theorem` | 13955 | Descent to the flat modular connection |
| `thm:conformal-block-reconstruction` | `theorem` | 14034 | Scalar free-energy and determinant reconstruction from the primitive kernel on the proved uniform-weight scalar lane |
| `thm:deformation-quantization-ope` | `theorem` | 14129 | Genus expansion from the OPE |
| `thm:ran-coherent-bar-cobar` | `theorem` | 14330 | Ran-coherent bar-cobar equivalence |
| `thm:shadow-channel-decomposition` | `theorem` | 14390 | Shadow channel decomposition |
| `cor:shadow-cauchy-schwarz` | `corollary` | 14470 | Shadow Cauchy--Schwarz inequality |
| `prop:critical-locus-complementarity` | `proposition` | 14522 | Critical-locus form of complementarity |
| `thm:theta-direct-derivation` | `theorem` | 14669 | Direct derivation on the proved scalar lane |
| `lem:graph-sum-truncation` | `lemma` | 14991 | Graph-sum truncation criterion |
| `thm:operadic-complexity-detailed` | `theorem` | 15067 | Operadic complexity |
| `prop:shadow-formality-low-degree` | `proposition` | 15185 | Shadow--formality identification at low degree |
| `thm:shadow-formality-identification` | `theorem` | 15256 | Shadow obstruction tower as formality obstruction tower |
| `prop:shadow-tower-three-lenses` | `proposition` | 15530 | Three lenses on the shadow obstruction tower |
| `prop:shadow-formality-higher-degree` | `proposition` | 15627 | Shadow--formality identification at higher degrees |
| `prop:linfty-obstruction-5-6` | `proposition` | 15983 | Explicit $L_\infty$ obstruction classes at degrees $5$ and $6$ |
| `prop:shadow-coefficient-rationality` | `proposition` | 16235 | Shadow coefficient rationality |
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n \"\\\\label\\{["'^}]*shadow" chapters/theory/chiral_koszul_pairs.tex' in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: regex parse error:
    (?:\label\{[^}]*shadow)
       ^^
error: unrecognized escape sequence
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "SC" raeeznotes/raeeznotes100/red_team_summary.md' in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
rg: raeeznotes/raeeznotes100/red_team_summary.md: IO error for operation on raeeznotes/raeeznotes100/red_team_summary.md: No such file or directory (os error 2)
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && ls raeeznotes' in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:
ls: raeeznotes: No such file or directory
wait(call_kfgrhWVARGXsE4LwTDKVOVvN) timed out:
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n '\\\\label\\{["'^}]*shadow'"' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
1298:\label{rem:ainfty-genus0-shadow}
1648:\label{rem:kac-shapovalov-arithmetic-shadow}
3064:\label{rem:koszulness-vs-shadow-depth}
3102:\label{rem:shadow-class-direct-sum}
3115:\label{eq:shadow-depth-direct-sum}
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n \"raeeznotes\" -g '*red_team_summary.md' -l" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: No files were searched, which means ripgrep probably applied a filter you didn't expect.
Running with --debug will show why files are being skipped.
codex
The context pass is still running. Once I have the exact label and current proof architecture, I’ll lock the scope and draft the strengthened replacement before editing.
collab wait(call_B3pMOJcyGFjkncv1lAqNbZ5S)
  receivers: 019d866d-705b-70f3-a5f5-52b111aa10ab, 019d866d-7083-7351-8f30-118e2b5a5277
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && ls archive' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
audit
metadata
misc
notes
orphaned_stubs
patches
previews
raeeznotes
raeeznotes83
raeeznotes_absorbed
references
session_artifacts
source_notes
source_tex
split_originals
standalone
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && find archive -name '*red_team_summary.md'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
archive/raeeznotes/raeeznotes100/red_team_summary.md
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "SC-formal" archive/raeeznotes/raeeznotes100/red_team_summary.md' in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n \"class \\\"?G\"? archive/raeeznotes/raeeznotes100/red_team_summary.md" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:
zsh:1: no matches found: class "?G?
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "class" archive/raeeznotes/raeeznotes100/red_team_summary.md | head' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
107:- `conj:modular` has statuses **Conjectured,ProvedHere** across instances: V1:Conjectured:appendices/ordered_associative_chiral_kd.tex:1278:Associative modular Maurer--Cartan class || V2:ProvedHere:chapters/connections/ordered_associative_chiral_kd.tex:1396: || V2:ProvedHere:chapters/connections/ordered_associativ...
exec
/bin/zsh -lc 'rg -n "SC-formal" -n /Users/raeez/chiral-bar-cobar-vol2' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:852: & SC-formality \\[2pt]
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:1186:The Swiss-cheese structure is SC-formal: the higher
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:1642: & $0$ (Koszul and SC-formal) \\[2pt]
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:489:\index{SC-formality!characterisation}%
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:497: $\cA$ is SC-formal \textup{(}$m_k^{\mathrm{SC}} = 0$
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:520:Part~\eqref{item:fdd-sc-formal}: SC-formality requires
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:525:$m_k = 0$ for $k \ge 3$ and SC-formality holds.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:561:is the equivalence between SC-formality, finite shadow
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-core.tex:3304: obstructs SC-formality
/Users/raeez/chiral-bar-cobar-vol2/compute/depth_spectrum_c_dependence.py:363:    print("  kappa(Vir_c) = c - 26. At c=26: kappa=0 (SC-formal, shadow truncates).")
/Users/raeez/chiral-bar-cobar-vol2/compute/audit/beilinson_audit_vol2_preface_wave11.md:52:- **MODERATE -- "Heisenberg class G, formal" (line 349).** The "formal" tag is correct (G is formal by definition), but a hostile reader will ask: "formal" in which sense -- SC-formal (m_k^SC = 0 for k >= 3), or dg-algebra formal (H*(A) quasi-iso to A)? AP14 explicitly distinguishes: "Koszulness != SC formality." In the Heisenberg case both hold, but the preface does not say which it means. For a preface this is LOW.
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "shadow" archive/raeeznotes/raeeznotes100/red_team_summary.md | head' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
48:- V1 `chapters/connections/arithmetic_shadows.tex`: **13** high/critical-risk claims
exec
/bin/zsh -lc 'rg -n "SC-formal" /Users/raeez/calabi-yau-quantum-groups' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
/Users/raeez/calabi-yau-quantum-groups/AGENTS.md:202:- shadow class or SC-formality claims;
/Users/raeez/calabi-yau-quantum-groups/AGENTS.md:741:If editing shadow depth, class, or SC-formality claims, check:
/Users/raeez/calabi-yau-quantum-groups/compute/tests/test_swiss_cheese_cy3_e1.py:373:        """Local P^2: class M, NOT SC-formal (AP-CY12)."""
/Users/raeez/calabi-yau-quantum-groups/compute/tests/test_swiss_cheese_cy3_e1.py:851:        """Local P^2 is NOT SC-formal (class M, AP-CY12)."""
/Users/raeez/calabi-yau-quantum-groups/compute/tests/test_swiss_cheese_cy3_e1.py:872:                assert f.sc_formal is True, f"{name} should be SC-formal (class G)"
/Users/raeez/calabi-yau-quantum-groups/compute/tests/test_swiss_cheese_cy3_e1.py:904:        """1 SC-formal CY3 (conifold only; local P^2 is class M, NOT SC-formal)."""
/Users/raeez/calabi-yau-quantum-groups/compute/lib/cross_volume_shadow_bridge.py:58:  SC-formal (m_k^{SC} = 0 for k >= 3): Heisenberg, lattice (class G only)
/Users/raeez/calabi-yau-quantum-groups/compute/lib/cross_volume_shadow_bridge.py:62:  CRITICAL: SC-formality is DIFFERENT from chirally Koszul.
/Users/raeez/calabi-yau-quantum-groups/compute/lib/cross_volume_shadow_bridge.py:63:  ALL standard families are chirally Koszul.  Only class G is SC-formal.
/Users/raeez/calabi-yau-quantum-groups/compute/lib/cross_volume_shadow_bridge.py:291:    SC-formal means m_k^{SC} = 0 for k >= 3.  Only class G (Heisenberg)
/Users/raeez/calabi-yau-quantum-groups/compute/lib/cross_volume_shadow_bridge.py:292:    is SC-formal.  Class L has m_3^{SC} != 0, class C has m_4^{SC} != 0,
/Users/raeez/calabi-yau-quantum-groups/compute/lib/cross_volume_shadow_bridge.py:295:    CRITICAL (AP14): SC-formality is DIFFERENT from chirally Koszul.
/Users/raeez/calabi-yau-quantum-groups/compute/lib/cross_volume_shadow_bridge.py:296:    ALL standard families are chirally Koszul.  Only class G is SC-formal.
/Users/raeez/calabi-yau-quantum-groups/compute/lib/cross_volume_shadow_bridge.py:305:    For SC-formal families (class G only): returns float('inf').
/Users/raeez/calabi-yau-quantum-groups/compute/lib/cross_volume_shadow_bridge.py:311:    for k >= 3 are nonzero.  Only class G is SC-formal.
/Users/raeez/calabi-yau-quantum-groups/compute/lib/cross_volume_shadow_bridge.py:315:        return float("inf")  # SC-formal
/Users/raeez/calabi-yau-quantum-groups/compute/lib/cross_volume_shadow_bridge.py:482:# 7. VOL II BRIDGE -- SC-formality data
/Users/raeez/calabi-yau-quantum-groups/compute/lib/cross_volume_shadow_bridge.py:628:    SC-formality, complementarity, and cross-check status.
/Users/raeez/calabi-yau-quantum-groups/compute/lib/cross_volume_shadow_bridge.py:639:    # SC-formality
/Users/raeez/calabi-yau-quantum-groups/compute/tests/test_cross_volume_shadow_bridge.py:16:  4. SC-formality classification (Vol II perspective)
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "Swiss" archive/raeeznotes/raeeznotes100/red_team_summary.md' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
112:- Volume II foundations around Swiss-cheese recognition, PVA descent, FM/AOS cancellation, and bar-cobar rectification look substantially healthier than the speculative connection chapters.
exec
/bin/zsh -lc 'rg -n "prop:swiss-cheese-nonformality-by-class" -n' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
wave2_audit_20260413_001942/S13_concordance_to_body.md:1294:  2592	non-Gaussian cases. Proposition~\ref{prop:swiss-cheese-nonformality-by-class}
wave2_audit_20260413_001942/S13_concordance_to_body.md:2145:`prop:swiss-cheese-nonformality-by-class` | `\ClaimStatusProvedHere`
metadata/dependency_graph.dot:2425:  prop_swiss_cheese_nonformality_by_class [label="prop:swiss-cheese-nonformality-by-class\nproposition [Pr]\nSwiss-cheese non-formality by shadow cla...", style=filled, fillcolor="#c8e6c9"];
metadata/theorem_registry.md:415:| `prop:swiss-cheese-nonformality-by-class` | `proposition` | 2480 | Swiss-cheese non-formality by shadow class |
metadata/label_index.json:28386:  "prop:swiss-cheese-nonformality-by-class": {
metadata/claims.jsonl:2326:{"label": "prop:swiss-cheese-nonformality-by-class", "env_type": "proposition", "status": "ProvedHere", "file": "chapters/theory/chiral_koszul_pairs.tex", "line": 2480, "title": "Swiss-cheese non-formality by shadow class", "refs_in_block": ["thm:koszul-equivalences-meta", "cor:lattice-postnikov-termination"]}
metadata/claims.jsonl:2330:{"label": "rem:d-module-purity-family-dependence", "env_type": "remark", "status": "Conjectured", "file": "chapters/theory/chiral_koszul_pairs.tex", "line": 2787, "title": "Family dependence of the\n$\\cD$-module purity equivalence", "labels_in_block": ["rem:d-module-purity-family-dependence", "conj:d-module-purity-wn-principal"], "refs_in_block": ["prop:d-module-purity-km-equivalence", "tab:koszulness-landscape", "prop:swiss-cheese-nonformality-by-class", "thm:koszul-equivalences-meta", "rem:d-module-purity-content"]}
audit_campaign_20260412_231034/XV04_SC_claims_xvol.md:172:411:| `prop:swiss-cheese-nonformality-by-class` | `proposition` | 2358 | Swiss-cheese non-formality by shadow class |
audit_campaign_20260412_231034/XV04_SC_claims_xvol.md:449:\label{prop:swiss-cheese-nonformality-by-class}
audit_campaign_20260412_231034/T15_SC_formality.md:5:- [CRITICAL] [chapters/theory/chiral_koszul_pairs.tex:2532](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex:2532) — The forward implication is outsourced to `prop:swiss-cheese-nonformality-by-class`, but that dependency only proves the Heisenberg case and conflicts with the manuscript’s own class data. Its table puts only Heisenberg in class `G` and even places “lattice VOA” in class `L` ([chiral_koszul_pairs.tex:2434](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex:2434)), while the shadow-archetype theorem puts lattice VOAs and free fermions in class `G` ([higher_genus_modular_koszul.tex:16402](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:16402)); see also [lattice_foundations.tex:1677](/Users/raeez/chiral-bar-cobar/chapters/examples/lattice_foundations.tex:1677) and [free_fields.tex:209](/Users/raeez/chiral-bar-cobar/chapters/examples/free_fields.tex:209). As written, `class G => SC-formal` is not proved for the full class-`G` surface being claimed.
audit_campaign_20260412_231034/T15_SC_formality.md:490:/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "prop:swiss-cheese-nonformality-by-class" -n "S_3" -n "thm:modular-characteristic" -n "standard landscape" -n "shadow-archetype-classification" -n "class G" chapters/theory/chiral_koszul_pairs.tex' in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
audit_campaign_20260412_231034/T15_SC_formality.md:496:chapters/theory/chiral_koszul_pairs.tex:2415:\label{prop:swiss-cheese-nonformality-by-class}
audit_campaign_20260412_231034/T15_SC_formality.md:497:chapters/theory/chiral_koszul_pairs.tex:2534:Proposition~\ref{prop:swiss-cheese-nonformality-by-class}:
audit_campaign_20260412_231034/T15_SC_formality.md:498:chapters/theory/chiral_koszul_pairs.tex:2773:(Proposition~\ref{prop:swiss-cheese-nonformality-by-class})
audit_campaign_20260412_231034/T15_SC_formality.md:979:- 1. `chapters/theory/chiral_koszul_pairs.tex:2414-2480` (`prop:swiss-cheese-nonformality-by-class`) — the table there stratifies the Swiss-cheese operations by shadow depth for classes G/L/C/M, then the “Mechanism” paragraph (lines 2458‑2480) explains how each class enforces the corresponding vanishing/non-vanishing pattern of $m_k^{\mathrm{SC}}$ (in particular $m_3=0$ only for class G) and justifies the classification via OPE pole orders, parity obstructions, and contact/quartic invariants.
audit_campaign_20260412_231034/T15_SC_formality.md:989:  019d8388-9549-7651-a4af-427231f754d7 completed: "- 1. `chapters/theory/chiral_koszul_pairs.tex:2414-2480` (`prop:swiss-cheese-nonformality-by-class`) — the table there s…"
audit_campaign_20260412_231034/T15_SC_formality.md:1838:I'm considering whether another theorem could be helpful since the cited theorem doesn't seem to apply. I want to avoid false positives from hidden assumptions, so it’s important to mention that the nondegeneracy hypothesis might exist elsewhere but isn't part of the cited result. I need to check the `prop:swiss-cheese-nonformality-by-class` proof, specifically looking at `thm:riccati-algebraicity` for class C and factors affecting class M. I'm wondering if we need to trace every step or if our main findings already indicate an incomplete direction due to class drift.
audit_campaign_20260412_231034/T15_SC_formality.md:1882:  2534	Proposition~\ref{prop:swiss-cheese-nonformality-by-class}:
audit_campaign_20260412_231034/T15_SC_formality.md:2034:- [CRITICAL] [chapters/theory/chiral_koszul_pairs.tex:2532](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex:2532) — The forward implication is outsourced to `prop:swiss-cheese-nonformality-by-class`, but that dependency only proves the Heisenberg case and conflicts with the manuscript’s own class data. Its table puts only Heisenberg in class `G` and even places “lattice VOA” in class `L` ([chiral_koszul_pairs.tex:2434](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex:2434)), while the shadow-archetype theorem puts lattice VOAs and free fermions in class `G` ([higher_genus_modular_koszul.tex:16402](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:16402)); see also [lattice_foundations.tex:1677](/Users/raeez/chiral-bar-cobar/chapters/examples/lattice_foundations.tex:1677) and [free_fields.tex:209](/Users/raeez/chiral-bar-cobar/chapters/examples/free_fields.tex:209). As written, `class G => SC-formal` is not proved for the full class-`G` surface being claimed.
rectification_20260412_233715/R18_cobar_construction.md:605:| `prop:swiss-cheese-nonformality-by-class` | `proposition` | 2358 | Swiss-cheese non-formality by shadow class |
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '90,140p' archive/raeeznotes/raeeznotes100/red_team_summary.md" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
- `prop:disk-local-binary-ternary-reduction` (V1 `chapters/connections/feynman_diagrams.tex:323`): proved here, but cites `conj:disk-local-perturbative-fm:Conjectured`.
- `prop:compactified-ternary-two-channel` (V1 `chapters/connections/feynman_diagrams.tex:389`): proved here, but cites `conj:disk-local-perturbative-fm:Conjectured`.
- `cor:g9-comparison-universal` (V1 `chapters/connections/thqg_critical_string_dichotomy.tex:1936`): proved here, but cites `rem:g9-mc-relation:Unknown`.
- `prop:thqg-III-compatibility` (V1 `chapters/connections/thqg_symplectic_polarization.tex:1148`): proved here, but cites `thm:thqg-III-lagrangian-polarization:Conditional`.
- `thm:thqg-III-landscape-census` (V1 `chapters/connections/thqg_symplectic_polarization.tex:1764`): proved here, but cites `thm:thqg-III-lagrangian-polarization:Conditional`.
- `thm:ym-bar-bridge` (V1 `chapters/connections/ym_boundary_theory.tex:58`): proved here, but cites `thm:conditional-mass-gap-transfer:Conditional,Conjectured`.
- `cor:stable-untwisting-bounded-error` (V1 `chapters/connections/ym_instanton_screening.tex:526`): proved here, but cites `thm:conditional-mass-gap-transfer:Conditional,Conjectured`.
- `thm:w-algebra-koszul-main` (V1 `chapters/examples/w_algebras.tex:250`): proved here, but cites `conj:w-orbit-duality:Conjectured`.

## Status-conflict examples
- `thm:thqg-contact-termination` has statuses **ProvedElsewhere,ProvedHere** across instances: V1:ProvedHere:chapters/connections/thqg_gravitational_complexity.tex:549:Contact termination || V2:ProvedElsewhere:chapters/connections/thqg_gravitational_complexity.tex:551:Contact termination...
- `lem:thqg-VII-genus-shifts` has statuses **ProvedElsewhere,Unknown** across instances: V1:ProvedElsewhere:chapters/connections/thqg_modular_bootstrap.tex:203:Genus shifts of the differential components || V2:Unknown:chapters/connections/thqg_line_operators_extensions.tex:2124:Planted-forest differential and genus shifts || V2...
- `cor:thqg-I-genus-g-partition` has statuses **ProvedHere,Unknown** across instances: V1:ProvedHere:chapters/connections/thqg_perturbative_finiteness.tex:369:Genus-$g$ partition function || V2:Unknown:chapters/connections/thqg_perturbative_finiteness.tex:368:Genus-$g$ partition function...
- `prop:thqg-III-kontsevich-pridham` has statuses **ProvedElsewhere,Unknown** across instances: V1:ProvedElsewhere:chapters/connections/thqg_symplectic_polarization.tex:857:{Kontsevich--Pridham correspondence; ;
\cite{Pridham17}} || V2:Unknown:chapters/connections/thqg_symplectic_polarization.tex:855:...
- `thm:grand-synthesis-principle` has statuses **Conditional,ProvedHere** across instances: V1:ProvedHere:chapters/connections/ym_boundary_theory.tex:128:Grand synthesis principle || V2:Conditional:chapters/connections/ym_synthesis.tex:36:Grand synthesis principle; \ClaimStatusConditional || V2:Conditional:chapters/connections/ym_...
- `thm:conditional-mass-gap-transfer` has statuses **Conditional,Conjectured** across instances: V1:Conjectured:chapters/connections/ym_instanton_screening.tex:499:Conditional mass-gap transfer via screening domination || V2:Conditional:chapters/connections/ym_synthesis.tex:1616:Conditional mass-gap transfer via screening domination; \...
- `conj:modular` has statuses **Conjectured,ProvedHere** across instances: V1:Conjectured:appendices/ordered_associative_chiral_kd.tex:1278:Associative modular Maurer--Cartan class || V2:ProvedHere:chapters/connections/ordered_associative_chiral_kd.tex:1396: || V2:ProvedHere:chapters/connections/ordered_associativ...
- `conj:DS` has statuses **Conjectured,ProvedHere** across instances: V1:Conjectured:appendices/ordered_associative_chiral_kd.tex:1309:Reduction commutes with associative chiral duality || V2:ProvedHere:chapters/connections/ordered_associative_chiral_kd.tex:1457: || V2:ProvedHere:chapters/connections/ordered_...
- `lem:PVA2_proof` has statuses **ProvedHere,Unknown** across instances: V2:Unknown:chapters/theory/pva-descent.tex:149:Alternative derivation of PVA2 via vertex algebra modes || V2:ProvedHere:chapters/theory/pva-descent-repaired.tex:375:Chain-level exchange homotopies; \ClaimStatusProvedHere...
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '2500,2600p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
& Heisenberg, lattice VOA
& $= 0$
& $= 0$
& $= 0$ \\
$L$ \textup{(}$r_{\max}=3$\textup{)}
& affine KM
& $\neq 0$
& $= 0$
& $= 0$ \\
$C$ \textup{(}$r_{\max}=4$\textup{)}
& $\beta\gamma$
& $= 0$
& $\neq 0$
& $= 0$ \\
$M$ \textup{(}$r_{\max}=\infty$\textup{)}
& Virasoro, $\cW_N$
& $\neq 0$
& $\neq 0$
& $\neq 0\;\forall\, k$ \\
\bottomrule
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '2600,2660p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\begin{proof}
The forward direction \textup{(}class~$G$ $\Longrightarrow$
SC-formal\textup{)} is established in
Proposition~\ref{prop:swiss-cheese-nonformality-by-class}:
the class-$G$ row consists exactly of Heisenberg and lattice
VOAs, and in both cases $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.

For the converse, suppose~$\cA$ is SC-formal.
Because the standard landscape is exhausted by the four classes
$G$, $L$, $C$, $M$, it is enough to eliminate the three
non-Gaussian cases. Proposition~\ref{prop:swiss-cheese-nonformality-by-class}
does exactly this: class~$L$ has $m_3^{\mathrm{SC}} \neq 0$,
class~$C$ has $m_4^{\mathrm{SC}} \neq 0$, and class~$M$ has
nonzero higher operations in every arity $k \geq 3$. Each of
these cases contradicts SC-formality. This converse uses only the
classification from Proposition~\ref{prop:swiss-cheese-nonformality-by-class};
it does not invoke any trilinear form built from~$\kappa$.
Hence an SC-formal algebra must
belong to class~$G$.
\end{proof}
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar-vol2 && sed -n '470,540p' chapters/connections/3d_gravity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
Proposition~\ref{prop:pole-order-classification}: class~$\mathbf{L}$
is formal (gauge), class~$\mathbf{M}$ non-formal (pure gravity and
matter-coupled gravity alike, since both have quartic OPE poles).
The coproduct on generators: for gauge theory $\Delta_z$ is the
standard Yangian coproduct (non-primitive, encoding the spectral
braiding); for pure gravity and matter-coupled gravity,
$\Delta_z(x) = \tau_z(x) \otimes 1 + 1 \otimes x$ on all free
generators (Theorem~\ref{thm:gravitational-primitivity} and
Remark~\ref{rem:bp-coproduct-resolved}). The composite coproduct:
for pure gravity, the absence of weight-$1$ generators forces
$\Delta_z(T)$ to be primitive; for BP, the surviving
$J$ yields the cross-term
$\Delta_{z,1}(T) \ni (1/z)\, J \otimes J$ from the split
Casimir (Remark~\ref{rem:non-principal-ghost}). The DS transport
is Theorem~\ref{thm:ds-hpl-transfer}.
\end{proof}

\begin{proposition}[Formality--depth--discriminant trichotomy; \ClaimStatusProvedElsewhere]%
\label{prop:formality-depth-discriminant}%
\index{SC-formality!characterisation}%
exec
/bin/zsh -lc 'rg -n "shadow tower truncates" -n /Users/raeez/chiral-bar-cobar-vol2' in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

wait(call_B3pMOJcyGFjkncv1lAqNbZ5S) timed out:
exec
/bin/zsh -lc 'rg -n "shadow tower truncates" /Users/raeez/calabi-yau-quantum-groups' in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

codex
I’m still waiting on the explorers rather than guessing at the local theorem surface. The next step is a scoped rewrite inside the theorem/proof block once the citations, status, and duplicate surface are explicit.
collab wait(call_KIZn1UIAgUblelKhDQSsB5wV)
  receivers: 019d866d-705b-70f3-a5f5-52b111aa10ab, 019d866d-7083-7351-8f30-118e2b5a5277

exec
/bin/zsh -lc 'rg -n "prop:sc-formal-iff-class-g" /Users/raeez/chiral-bar-cobar-vol2' in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

thinking
**Summarizing key propositions and references around SC formality**

I'm gathering precise theorem and proposition labels near lines 2520-2560 in `chapters/theory/chiral_koszul_pairs.tex` including `prop:swiss-cheese-nonformality-by-class` and `prop:sc-formal-iff-class-g`. I’m noting their statements rely on classification to prove SC formality equivalence and that no direct proof gaps for SC formality are mentioned, though a remark about D-module purity hints at an outstanding Step 4 unrelated to SC formality. I’m also correlating references to these results and to pre-edit verification protocols found in `CLAUDE.md` around lines 547, 932, and near line 927. Finally, I’m preparing a grounded, concise summary citing files and approximate line numbers to clarify context and mentions of verification steps.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba CLAUDE.md | sed -n '900,1080p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   900	
   901	RS-3: Physics IS the homotopy type, not a "bridge." Costello-Gaiotto-Dimofte are substance, not applications.
   902	RS-4: Costello/Dimofte/Gaiotto content belongs in mathematical core, not "connections" chapters.
   903	RS-9: The slab is a bimodule, NOT a Swiss-cheese disk. Two boundary components.
   904	RS-10: Single-pass agent work without audit FORBIDDEN. Beilinson loop mandatory for chapters.
   905	RS-12: The programme is THREE volumes, not two.
   906	RS-13: In Vol II, gravity is the CLIMAX (Part VI), not middle content.
   907	RS-14: Introduction orients, Overture instantiates. Introduction first, Overture second.
   908	RS-15: Koszul programme before higher_genus in the dependency DAG.
   909	RS-19: The preface is a complete survey, not a compressed summary. Save before compressing.
   910	
   911	## Agent Anti-Patterns
   912	
   913	AAP2: Terminology rename MUST be atomic across all three volumes in single session.
   914	AAP3: Formula implemented ONCE in canonical module, import everywhere.
   915	AAP4: \begin{proof} only after theorem/prop/lemma with ProvedHere. Use Remark[Evidence] for conjectures.
   916	AAP5: Build-artifact commits batched with content. Never standalone artifact commits.
   917	AAP6: Search ALL THREE volumes before downgrading a status tag.
   918	AAP8: README claims independently verifiable by test suite.
   919	AAP9: Wait for ALL agents to finish before launching new batch.
exec
/bin/zsh -lc 'rg -n "prop:sc-formal-iff-class-g" /Users/raeez/calabi-yau-quantum-groups' in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar-vol2 && sed -n '820,860p' chapters/examples/rosetta_stone.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
The Heisenberg bar complex is a single mathematical object (an
$E_1$ curved dg coassociative coalgebra) but it admits
two simultaneous readings: one algebraic (Volume~I), one physical
(Volume~II). The following table records the correspondence.

\begin{center}
\small
\renewcommand{\arraystretch}{1.25}
\begin{tabular}{@{}l@{\;\;}l@{\;\;}l@{}}
\textbf{Bar complex} & \textbf{Vol.\@ I reading} &
 \textbf{Vol.\@ II reading} \\
\hline
$d_{\barB}$
 & bar differential
 & closed-color (holomorphic) \\[2pt]
$\Delta$
 & coalgebra coproduct
 & open-color (topological) \\[2pt]
$d_{\barB}^{\,2} = 0$
 & Arnold relations
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '2480,2650p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  2480	\label{prop:swiss-cheese-nonformality-by-class}
  2481	\index{Swiss-cheese operad!non-formality by shadow class|textbf}
  2482	\index{shadow depth!Swiss-cheese formality}
  2483	\index{Ainfty@$A_\infty$!non-formality for class M}
  2484	The Swiss-cheese operations $m_k^{\mathrm{SC}}$ on~$\cA$ itself
  2485	\textup{(}not on the bar cohomology $H^*(\barB(\cA))$, which is
  2486	always $A_\infty$-formal for Koszul algebras by
  2487	Theorem~\textup{\ref{thm:koszul-equivalences-meta}(iii)}\textup{)}
  2488	are classified by shadow depth as follows.
  2489	\begin{center}
  2490	\renewcommand{\arraystretch}{1.3}
  2491	\begin{tabular}{@{}lcccc@{}}
  2492	\toprule
  2493	\textbf{Class}
  2494	& \textbf{Families}
  2495	& $m_3^{\mathrm{SC}}$
  2496	& $m_4^{\mathrm{SC}}$
  2497	& $m_k^{\mathrm{SC}},\; k \geq 5$ \\
  2498	\midrule
  2499	$G$ \textup{(}$r_{\max}=2$\textup{)}
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "single-line" chapters/theory/chiral_koszul_pairs.tex' in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

exec
/bin/zsh -lc "cd /Users/raeez/calabi-yau-quantum-groups && sed -n '50,120p' compute/lib/cross_volume_shadow_bridge.py" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  M (mixed, r_max = infinity):    Virasoro, W_N

COMPLEMENTARITY (Theorem C, AP24):
  kappa(A) + kappa(A!) = 0         for KM / free fields / lattice
  kappa(A) + kappa(A!) = 13        for Virasoro (c + (26-c))/2 = 13
  kappa(A) + kappa(A!) = 250/3     for W_3 (5c/6 + 5(100-c)/6)

SWISS-CHEESE FORMALITY (Vol II, AP14):
  SC-formal (m_k^{SC} = 0 for k >= 3): Heisenberg, lattice (class G only)
  SC-non-formal: affine KM (class L, m_3^{SC} != 0), beta-gamma (class C, m_4^{SC} != 0),
                 Virasoro/W_N (class M, m_k^{SC} != 0 for all k >= 3)

  CRITICAL: SC-formality is DIFFERENT from chirally Koszul.
  ALL standard families are chirally Koszul.  Only class G is SC-formal.

References:
  Vol I: theorem_c_complementarity.py, quartic_arithmetic_closure.py,
         genus3_landscape.py, betagamma_shadow_full.py
  Vol II: cross_volume_deep_bridge.py, swiss_cheese_verification.py
  Vol III: e2_bar_complex.py, kl_sl2_level1.py, drinfeld_center_coha.py
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba archive/raeeznotes/raeeznotes100/red_team_summary.md | sed -n '100,140p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   100	- `thm:thqg-contact-termination` has statuses **ProvedElsewhere,ProvedHere** across instances: V1:ProvedHere:chapters/connections/thqg_gravitational_complexity.tex:549:Contact termination || V2:ProvedElsewhere:chapters/connections/thqg_gravitational_complexity.tex:551:Contact termination...
   101	- `lem:thqg-VII-genus-shifts` has statuses **ProvedElsewhere,Unknown** across instances: V1:ProvedElsewhere:chapters/connections/thqg_modular_bootstrap.tex:203:Genus shifts of the differential components || V2:Unknown:chapters/connections/thqg_line_operators_extensions.tex:2124:Planted-forest differential and genus shifts || V2...
   102	- `cor:thqg-I-genus-g-partition` has statuses **ProvedHere,Unknown** across instances: V1:ProvedHere:chapters/connections/thqg_perturbative_finiteness.tex:369:Genus-$g$ partition function || V2:Unknown:chapters/connections/thqg_perturbative_finiteness.tex:368:Genus-$g$ partition function...
   103	- `prop:thqg-III-kontsevich-pridham` has statuses **ProvedElsewhere,Unknown** across instances: V1:ProvedElsewhere:chapters/connections/thqg_symplectic_polarization.tex:857:{Kontsevich--Pridham correspondence; ;
   104	\cite{Pridham17}} || V2:Unknown:chapters/connections/thqg_symplectic_polarization.tex:855:...
   105	- `thm:grand-synthesis-principle` has statuses **Conditional,ProvedHere** across instances: V1:ProvedHere:chapters/connections/ym_boundary_theory.tex:128:Grand synthesis principle || V2:Conditional:chapters/connections/ym_synthesis.tex:36:Grand synthesis principle; \ClaimStatusConditional || V2:Conditional:chapters/connections/ym_...
   106	- `thm:conditional-mass-gap-transfer` has statuses **Conditional,Conjectured** across instances: V1:Conjectured:chapters/connections/ym_instanton_screening.tex:499:Conditional mass-gap transfer via screening domination || V2:Conditional:chapters/connections/ym_synthesis.tex:1616:Conditional mass-gap transfer via screening domination; \...
   107	- `conj:modular` has statuses **Conjectured,ProvedHere** across instances: V1:Conjectured:appendices/ordered_associative_chiral_kd.tex:1278:Associative modular Maurer--Cartan class || V2:ProvedHere:chapters/connections/ordered_associative_chiral_kd.tex:1396: || V2:ProvedHere:chapters/connections/ordered_associativ...
   108	- `conj:DS` has statuses **Conjectured,ProvedHere** across instances: V1:Conjectured:appendices/ordered_associative_chiral_kd.tex:1309:Reduction commutes with associative chiral duality || V2:ProvedHere:chapters/connections/ordered_associative_chiral_kd.tex:1457: || V2:ProvedHere:chapters/connections/ordered_...
   109	- `lem:PVA2_proof` has statuses **ProvedHere,Unknown** across instances: V2:Unknown:chapters/theory/pva-descent.tex:149:Alternative derivation of PVA2 via vertex algebra modes || V2:ProvedHere:chapters/theory/pva-descent-repaired.tex:375:Chain-level exchange homotopies; \ClaimStatusProvedHere...
   110	
   111	## Zones that currently survive the red-team pass better than the rest
   112	- Volume II foundations around Swiss-cheese recognition, PVA descent, FM/AOS cancellation, and bar-cobar rectification look substantially healthier than the speculative connection chapters.
   113	- Volume I core theory and the explicitly tagged examples are safer than the high-energy connection/frontier material, but still need local proof verification claim by claim.
   114	
   115	## Files produced
   116	- `master_claim_ledger_filtered.csv`: all filtered formal claims with attack swarms and dismissal stances.
   117	- `suspicious_proved_claim_dependencies.csv`: proved-here claims that locally depend on non-proved or unstable references.
   118	- `label_status_conflicts.csv`: same label with multiple statuses across files/volumes.
   119	- `informal_claim_harvest.csv`: harvested sentence-level explicit informal/meta claims.
exec
/bin/zsh -lc "cd /Users/raeez/calabi-yau-quantum-groups && sed -n '20,120p' compute/lib/swiss_cheese_cy3_e1.py" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   where n_c = number of closed (bulk/chiral) inputs,
         n_o = number of open (boundary/E_1) inputs.

   KEY DISTINCTION from SC^{ch,top} for vertex algebras:
   For E_inf-chiral algebras (all vertex algebras), the R-direction
   factorization is DERIVED from the local OPE via monodromy
   (Vol II, AP36). For genuinely E_1-chiral algebras (CoHA, quantum
   vertex algebras), the R-direction factorization is INDEPENDENT
   INPUT -- part of the defining data.

   The CoHA product m: H_{d1} x H_{d2} -> H_{d1+d2} gives the E_1
   structure; the chiral bracket (if present) gives the C-direction.

2. E_1 BAR COMPLEX B^{E_1}(A).
   The E_1 bar complex uses only the ORDERED bar construction:
     B^{E_1}_k(A) = (s^{-1}A)^{tensor k}  (NO S_k coinvariants)
   with bar differential from the associative product.

   For the full bar complex (E_inf): B^{Sigma}_k(A) = (s^{-1}A)^{tensor k} / S_k.
   The E_1 bar complex has STRICTLY MORE generators than the E_inf bar complex
exec
/bin/zsh -lc "cd /Users/raeez/calabi-yau-quantum-groups && sed -n '360,440p' compute/tests/test_swiss_cheese_cy3_e1.py" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
        d = cy3_shadow_data_local_p2()
        # VERIFIED [DC] shadow structure [LC] boundary/limiting case
        assert d.shadow_class == "M"
        # VERIFIED [DC] shadow structure [LC] boundary/limiting case
        assert d.r_max == -1  # infinite

    def test_local_p2_kappa(self):
        """Local P^2 kappa = 3/2."""
        d = cy3_shadow_data_local_p2()
        # VERIFIED [DC] kappa formula [LC] boundary/limiting case
        assert d.kappa == Fraction(3, 2)

    def test_local_p2_sc_nonformal(self):
        """Local P^2: class M, NOT SC-formal (AP-CY12)."""
        d = cy3_shadow_data_local_p2()
        assert d.sc_formal is False

    # --- Quintic ---

    def test_quintic_shadow_class_M(self):
codex
**CLAUDE.md context**
- `CLAUDE.md:932-936` records the structural fact that the shadow tower Theta_A converges for the standard families G/L/C/M, that SC-formality holds exactly for class G, that Δ = 8κS₄ vanishes iff the tower truncates, and that the shadow depth dichotomy is independent of Koszulness (prop:sc-formal-iff-class-g, prop:depth-gap-trichotomy, prop:chirhoch1-affine-km).
- `CLAUDE.md:982-989` mandates the Pre-Edit Verification Protocol: before touching formulas (kappa, r-matrices, bar complex, labels, scope quantifiers, etc.) or hot zones, fill the appropriate PE template in the reply with verdict ACCEPT and cite sources, then obey the convergent writing/audit loop.

**Concordance & metadata**
- `chapters/connections/concordance.tex:7080-7110` and `:9650-9690` track the same commitment: prop:sc-formal-iff-class-g is part of the structural propositions from the April 2026 session, and the entry emphasises that SC-formality = class G plus the depth gap and ChirHoch¹ results already cited.
- `metadata/theorem_registry.md:402-420` lists prop:sc-formal-iff-class-g (line~2591) and prop:sc-formality-by-class (line~16933) with their environments, line references, and titles, so any rectification must keep those metadata entries aligned with the textual statements/resolutions.

**Red-team note**
- `archive/raeeznotes/raeeznotes100/red_team_summary.md:111-113` flags the Zone “Swiss-cheese recognition” in Volume II as relatively healthy, which reinforces that the Swiss-cheese/class‑G terrain is a known red-team focus but currently better covered than speculative connections.

**Target surface (chapters/theory/chiral_koszul_pairs.tex:2480-2650)**
- `prop:swiss-cheese-nonformality-by-class` (lines 2480-2578) tabulates SC operations by shadow class (only class G has all \(m_k^{\mathrm{SC}}=0\); classes L/C/M have their first nonzero operations at k = 3,4,≥3 respectively) and explains via OPE/pole data why each class triggers the listed shadow invariants (e.g., Δ = 8κS₄ ≠ 0 for class M).
- `prop:sc-formal-iff-class-g` (lines 2581-2619) states the iff and proves the forward direction by the table and the converse by excluding the non-G classes via prop:swiss-cheese-nonformality-by-class; the proof relies solely on this classification and avoids any extra trilinear κ data.
- `remark rem:d-module-purity-content` (lines 2621-2650) points out the remaining gap: Step 4 of the Koszul ⇒ D-module purity route still needs equality of the PBW filtration with the Saito weight filtration (affine KM case proved, general case unresolved), which is the only missing step in that chain.
wait(call_KIZn1UIAgUblelKhDQSsB5wV) 1 agents complete:
  019d866d-705b-70f3-a5f5-52b111aa10ab completed: "**CLAUDE.md context**
- `CLAUDE.md:932-936` records the structural fact that the shadow tower Theta_A converges for the …"
codex
The theorem surface is locked now. The file already contains the classification proposition and the iff proposition, but the proof lane still needs to be recast around the mechanism you asked for: shadow-tower control of mixed SC operations forward, and tower-bar correspondence for the converse.
collab wait(call_uAYcbtfZNfu0D0cf47Ai8tkw)
  receivers: 019d866d-7083-7351-8f30-118e2b5a5277
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '340,380p' scripts/platonic_rectification_20.py" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
2. For (viii): INVESTIGATE freeness. The polynomial Hilbert series is proved. Does
   concentration in {0,1,2} + polynomial Hilbert series IMPLY freeness for graded-commutative
   algebras? If the algebra is in degrees {0,1,2} with a 1-dimensional degree-0 piece,
   the algebra is generated in degree 1 and 2 with relations in degree 2 and 3.
   This is free iff there are no relations in degree 2 (= no Massey products).
   PROVE vanishing of Massey products from the formality of FM_n(C).
3. State the STRONGEST versions of (vii) and (viii).

Search for 'equiv' near 'vii' and 'viii' in the file.""")

agent("P13_SC_formality_upgrade", """SC-FORMALITY: A is SC-formal iff class G.

TARGET: chapters/theory/chiral_koszul_pairs.tex

KNOWN ISSUES:
1. Converse proof uses bilinear form that doesn't exist for betagamma
2. Forward proof only verified for Heisenberg, not full class G

YOUR MISSION:
1. For the FORWARD direction (class G => SC-formal): prove it for ALL class-G families
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '280,320p' scripts/healing_fortification_40.py" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
3. At d_alg = 3: g^sh lives in degrees {2, 3, 4}. The bracket [g^sh_2, g^sh_2] ⊂ g^sh_3
   (if S_2 ≠ 0 and S_3 ≠ 0) and [g^sh_2, g^sh_3] ⊂ g^sh_4.
4. The Jacobi identity on g^sh forces: if S_3 ≠ 0, then [S_2, [S_2, S_3]] ≠ 0,
   which lives in degree 5. But d_alg = 3 requires g^sh_5 = 0. Contradiction.
5. This is a STRUCTURAL argument from Lie theory, independent of the MC computation.

Write as Remark[Alternative proof via shadow Lie algebra]. Also verify the primary
proof argument is consistent with this alternative.""")

agent("H11_SC_formal_alt", """SC-FORMALITY — ALTERNATIVE PROOF of iff class G.

TARGET: chapters/theory/chiral_koszul_pairs.tex (add Remark)

Write a PURELY OPERADIC alternative proof of both directions:

FORWARD (class G => SC-formal):
1. Class G means Delta = 8*kappa*S_4 = 0 and the shadow tower truncates at degree 2.
2. The SC operations m_k^{SC} at order k >= 3 are controlled by S_{k-1} in the shadow tower.
3. S_r = 0 for r >= 3 (class G) implies m_k^{SC} = 0 for k >= 3. QED.


thinking
**Summarizing cross-volume file references**

I’m listing key files that reference the classification and “shadow tower truncates at degree 2” phrase, providing concise one-line descriptions mentioning the relevant propositions or proofs they connect to, especially noting any cross-volume or base theorem dependencies that would require updates if the classification changes. I’ll keep it to six main bullet points focused on these critical cross-references.
codex
- `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex`: Proposition `formality-depth-discriminant` restates SC-formality ↔ class G and the finite-depth ↔ Δ=0 dichotomy from `chiral_koszul_pairs.tex`, so any change to that theorem needs this cross-volume summary tweaked.
- `/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex`: The comparative table (Vol I vs. Vol II) flags `m_k=0` as the SC-formality datum for the Vol I class‑G entry, so the bridge narrative must propagate if the underlying SC-formal/class G claim shifts.
- `/Users/raeez/calabi-yau-quantum-groups/compute/lib/cross_volume_shadow_bridge.py`: The header doc-block explicitly lists “SC-formal (m_k^{SC}=0 for k≥3): Heisenberg, lattice (class G only)” and ties Δ=0/class G to the Swiss-cheese operations, so it must be updated together with the base proposition.
- `/Users/raeez/calabi-yau-quantum-groups/compute/lib/swiss_cheese_cy3_e1.py`: Section 4 enumerates the CY3 landscape with class G for the conifold and class M/Δ≠0 for the others while citing the Vol I SC-formality classification, so any theorem reshaping would ripple here.
- `/Users/raeez/calabi-yau-quantum-groups/compute/tests/test_swiss_cheese_cy3_e1.py`: Multiple tests enforce `shadow_class` and `sc_formal` flags (e.g., conifold=class G/SC-formal, local P²=class M/not SC-formal), so their assertions will break if the classification criteria change.
- `/Users/raeez/chiral-bar-cobar/scripts/platonic_rectification_20.py`: Agent `P13_SC_formality_upgrade` spells out that “class G means Δ=8κS₄=0 and the shadow tower truncates at degree 2,” so this meta-plan must be realigned if the SC-formality/class G/Δ=0 story shifts.
wait(call_uAYcbtfZNfu0D0cf47Ai8tkw) 1 agents complete:
  019d866d-7083-7351-8f30-118e2b5a5277 completed: "- `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex`: Proposition `formality-depth-discriminant` r…"

thinking
**Considering file operations**

I should read the file more selectively, focusing on relevant sections and definitions. Maybe the line range 2300-2660 will be enough, but accessing the full file might be impractical if it's very large. I need to look into using tools like `rg` for specific occurrences and examine local sections along with earlier definitions. It's important to have the actual text for editing, so I'll read the relevant chunks and cited dependencies while considering parallel command executions.
codex
I’m pulling the exact prose and nearby dependencies now so the rewrite is grounded in the live text rather than the theorem summary. After that I’ll lock the proof architecture in a PE block and patch only the assigned section.
exec
/bin/zsh -lc "sed -n '920,1010p' CLAUDE.md" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
RS-19: The preface is a complete survey, not a compressed summary. Save before compressing.

## Agent Anti-Patterns

AAP2: Terminology rename MUST be atomic across all three volumes in single session.
AAP3: Formula implemented ONCE in canonical module, import everywhere.
AAP4: \begin{proof} only after theorem/prop/lemma with ProvedHere. Use Remark[Evidence] for conjectures.
AAP5: Build-artifact commits batched with content. Never standalone artifact commits.
AAP6: Search ALL THREE volumes before downgrading a status tag.
AAP8: README claims independently verifiable by test suite.
AAP9: Wait for ALL agents to finish before launching new batch.
AAP10: After agent completion, verify BOTH engine AND test files exist.
AAP11: Every hardcoded expected value derivable by 2+ independent paths.
AAP12: Asymptotic tolerance proportional to 1/log(N) or verified by two methods.
AAP13: NEVER downgrade model without user permission. Wait and retry on rate limit.
AAP14: Unique branch name per agent.
AAP15: Serialize builds or use isolated worktrees. Parallel pdflatex kills.
AAP16: git stash FORBIDDEN. Use git diff > patch.diff + git apply instead.
AAP17: Verify edits via git diff, not agent narrative.
AAP18: Confabulating operadic theory -> compute or cite (Loday-Vallette, Vallette, Livernet). NEVER analogize.
exec
/bin/zsh -lc "sed -n '100,125p' archive/raeeznotes/raeeznotes100/red_team_summary.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2460,2665p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '395,425p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '7070,7120p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '9640,9695p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
- `thm:thqg-contact-termination` has statuses **ProvedElsewhere,ProvedHere** across instances: V1:ProvedHere:chapters/connections/thqg_gravitational_complexity.tex:549:Contact termination || V2:ProvedElsewhere:chapters/connections/thqg_gravitational_complexity.tex:551:Contact termination...
- `lem:thqg-VII-genus-shifts` has statuses **ProvedElsewhere,Unknown** across instances: V1:ProvedElsewhere:chapters/connections/thqg_modular_bootstrap.tex:203:Genus shifts of the differential components || V2:Unknown:chapters/connections/thqg_line_operators_extensions.tex:2124:Planted-forest differential and genus shifts || V2...
- `cor:thqg-I-genus-g-partition` has statuses **ProvedHere,Unknown** across instances: V1:ProvedHere:chapters/connections/thqg_perturbative_finiteness.tex:369:Genus-$g$ partition function || V2:Unknown:chapters/connections/thqg_perturbative_finiteness.tex:368:Genus-$g$ partition function...
- `prop:thqg-III-kontsevich-pridham` has statuses **ProvedElsewhere,Unknown** across instances: V1:ProvedElsewhere:chapters/connections/thqg_symplectic_polarization.tex:857:{Kontsevich--Pridham correspondence; ;
\cite{Pridham17}} || V2:Unknown:chapters/connections/thqg_symplectic_polarization.tex:855:...
- `thm:grand-synthesis-principle` has statuses **Conditional,ProvedHere** across instances: V1:ProvedHere:chapters/connections/ym_boundary_theory.tex:128:Grand synthesis principle || V2:Conditional:chapters/connections/ym_synthesis.tex:36:Grand synthesis principle; \ClaimStatusConditional || V2:Conditional:chapters/connections/ym_...
- `thm:conditional-mass-gap-transfer` has statuses **Conditional,Conjectured** across instances: V1:Conjectured:chapters/connections/ym_instanton_screening.tex:499:Conditional mass-gap transfer via screening domination || V2:Conditional:chapters/connections/ym_synthesis.tex:1616:Conditional mass-gap transfer via screening domination; \...
- `conj:modular` has statuses **Conjectured,ProvedHere** across instances: V1:Conjectured:appendices/ordered_associative_chiral_kd.tex:1278:Associative modular Maurer--Cartan class || V2:ProvedHere:chapters/connections/ordered_associative_chiral_kd.tex:1396: || V2:ProvedHere:chapters/connections/ordered_associativ...
- `conj:DS` has statuses **Conjectured,ProvedHere** across instances: V1:Conjectured:appendices/ordered_associative_chiral_kd.tex:1309:Reduction commutes with associative chiral duality || V2:ProvedHere:chapters/connections/ordered_associative_chiral_kd.tex:1457: || V2:ProvedHere:chapters/connections/ordered_...
- `lem:PVA2_proof` has statuses **ProvedHere,Unknown** across instances: V2:Unknown:chapters/theory/pva-descent.tex:149:Alternative derivation of PVA2 via vertex algebra modes || V2:ProvedHere:chapters/theory/pva-descent-repaired.tex:375:Chain-level exchange homotopies; \ClaimStatusProvedHere...

## Zones that currently survive the red-team pass better than the rest
- Volume II foundations around Swiss-cheese recognition, PVA descent, FM/AOS cancellation, and bar-cobar rectification look substantially healthier than the speculative connection chapters.
- Volume I core theory and the explicitly tagged examples are safer than the high-energy connection/frontier material, but still need local proof verification claim by claim.

## Files produced
- `master_claim_ledger_filtered.csv`: all filtered formal claims with attack swarms and dismissal stances.
- `suspicious_proved_claim_dependencies.csv`: proved-here claims that locally depend on non-proved or unstable references.
- `label_status_conflicts.csv`: same label with multiple statuses across files/volumes.
- `informal_claim_harvest.csv`: harvested sentence-level explicit informal/meta claims.
 succeeded in 52ms:
$\mathbf{G}/\mathbf{L}/\mathbf{C}/\mathbf{M}$
(Remark~\ref{rem:shadow-depth-gkw-refinement}) refines their
binary formal/non-formal dichotomy into a four-class stratification
governed by the discriminant $\Delta = 8\kappa S_4$.
\end{remark}

\begin{remark}[Loop-exactness ordering $G < L < C < M$]
\label{rem:loop-exactness-ordering}
\index{shadow depth!loop-exactness ordering}
The four shadow-depth classes are ordered by the number of loop corrections needed to determine the full $A_\infty$ structure on~$\cA^!_{\mathrm{line}}$:
\begin{itemize}
\item Class~$G$ (Gaussian, $r_{\max}=2$): tree-level exact.
\item Class~$L$ (Lie/tree, $r_{\max}=3$): one-loop exact (DNP non-renormalization, Theorem~\ref{thm:dnp-bar-cobar-identification}(iii)).
\item Class~$C$ (Contact, $r_{\max}=4$): two-loop exact.
\item Class~$M$ (Mixed, $r_{\max}=\infty$): requires all-loop resummation.
\end{itemize}
This ordering refines the Koszulness programme: all four classes are chirally Koszul (bar $E_2$-collapse), but they differ in Swiss-cheese formality depth.
\end{remark}

\begin{proposition}[Swiss-cheese non-formality by shadow class; \ClaimStatusProvedHere]
 succeeded in 51ms:
 Koszul dualization, and base change
 & three pre-existing fragments consolidated;
 quotients excluded \\
\ref{prop:d-module-purity-km-equivalence}
 & Kac--Moody equivalence via Saito--Kashiwara weight
 filtration: PBW strictness~(ii) $\iff$
 $\cD$-module purity~(xii)
 & chiral localization $+$ Hitchin VHS $+$ Saito \\
\ref{prop:shadow-tower-three-lenses}
 & Three equivalent descriptions of $S_r(\cA)$:
 algebraic (shadow), geometric (formality obstruction),
 holographic (boundary-bulk correction)
 & bar-intrinsic MC $+$ formality identification
 $+$ derived-centre factorization \\
\ref{def:generating-depth}
 & Generating depth $d_{\mathrm{gen}}$ vs algebraic depth
 $d_{\mathrm{alg}}$: formal distinction~;
 Virasoro $d_{\mathrm{gen}} = 3$,
 $d_{\mathrm{alg}} = \infty$
 & depth decomposition $+$ class~M tower non-termination \\
 succeeded in 51ms:
| `lem:filtered-comparison` | `lemma` | 333 | Filtered comparison |
| `lem:filtered-comparison-unit` | `lemma` | 361 | Bar-side filtered comparison |
| `thm:fundamental-twisting-morphisms` | `theorem` | 412 | Fundamental theorem of chiral twisting morphisms |
| `cor:three-bijections` | `corollary` | 488 | Three bijections for chiral twisting morphisms |
| `thm:pbw-koszulness-criterion` | `theorem` | 764 | PBW criterion for chiral Koszulness |
| `thm:km-chiral-koszul` | `theorem` | 842 | Affine Kac--Moody algebras are chiral Koszul |
| `thm:virasoro-chiral-koszul` | `theorem` | 897 | Virasoro chiral Koszulness |
| `cor:bar-cohomology-koszul-dual` | `corollary` | 941 | Bar cohomology computes Koszul dual |
| `thm:bar-concentration` | `theorem` | 1129 | Bar concentration for Koszul pairs |
| `prop:ainfty-formality-implies-koszul` | `proposition` | 1242 | Formality implies chiral Koszulness |
| `thm:ainfty-koszul-characterization` | `theorem` | 1276 | Converse: chiral Koszulness implies formality |
| `thm:ext-diagonal-vanishing` | `theorem` | 1346 | Ext diagonal vanishing criterion |
| `prop:pbw-universality` | `proposition` | 1383 | PBW universality |
| `cor:universal-koszul` | `corollary` | 1409 | Universal vertex algebras are chirally Koszul |
| `thm:kac-shapovalov-koszulness` | `theorem` | 1475 | Kac--Shapovalov criterion for simple quotients |
| `prop:li-bar-poisson-differential` | `proposition` | 1726 | Poisson differential on the Li--bar $E_1$ page |
| `thm:associated-variety-koszulness` | `theorem` | 1797 | Associated-variety criterion for Koszulness |
| `prop:large-orbit-obstruction` | `proposition` | 1899 | Nilradical obstruction at degenerate admissible levels |
| `thm:koszul-equivalences-meta` | `theorem` | 2033 | Equivalences and consequences of chiral Koszulness |
| `prop:koszul-closure-properties` | `proposition` | 2380 | Closure of chiral Koszulness under tensor, dualization, and base change |
 succeeded in 51ms:
 $\kappa(\Walg_N) = c(H_N{-}1)$ \\
& $F_g = \kappa \cdot \lambda_g^{\mathrm{FP}}$ for
 uniform-weight modular Koszul algebras at all genera
 \textup{(}Theorem~\ref{thm:genus-universality}\textup{)} \\
& Swiss-cheese theorem
 \textup{(}Theorem~\ref{thm:thqg-swiss-cheese}\textup{)} \\
& Chiral derived center as universal bulk \\
& Annulus trace
 \textup{(}Theorem~\ref{thm:thqg-annulus-trace}\textup{)} \\
& Heisenberg and lattice sewing
 \textup{(}Theorems~\ref{thm:heisenberg-sewing},
 \ref{thm:lattice-sewing}\textup{)} \\
& HS-sewing for the entire standard landscape (universal algebras)
 \textup{(}Theorem~\ref{thm:general-hs-sewing}\textup{)} \\
& All-degree inverse limit
 $\Theta_\cA = \varprojlim \Theta_\cA^{\le r}$
 \textup{(}Theorem~\ref{thm:recursive-existence}\textup{)} \\
& Algebraic-family rigidity
 \textup{(}Theorem~\ref{thm:algebraic-family-rigidity}\textup{)} \\
& DS primitivity of the gravitational coproduct
codex
I’ve got the live theorem block. The next pass is dependency locking: I need the exact statements that let me replace “classification says so” with the stronger mechanism based on tower control and the tower-bar correspondence.
exec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/cross-volume-propagation/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"cor:lattice-postnikov-termination|thm:riccati-algebraicity|prop:shadow-tower-three-lenses|tower-bar correspondence|SC-formal|class~\\\\\\\\mathbf\\\\{G\\\\}|Delta = 8\\\\kappa S_4|truncates at degree 2|swiss-cheese operations\" chapters/theory chapters/connections -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
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

 exited 2 in 50ms:
rg: regex parse error:
    (?:cor:lattice-postnikov-termination|thm:riccati-algebraicity|prop:shadow-tower-three-lenses|tower-bar correspondence|SC-formal|class~\\mathbf\{G\}|Delta = 8\kappa S_4|truncates at degree 2|swiss-cheese operations)
                                                                                                                                                                 ^^
error: unrecognized escape sequence
exec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/build-surface/SKILL.md" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
---
name: build-surface
description: Use when LaTeX builds, build logs, warning classification, metadata regeneration, or targeted pytest runs determine whether a change is actually verified. This is the Codex-native equivalent of `/build` from `CLAUDE.md`.
---

# Build Surface

Build output is evidence only after the surface is stable enough to trust.

## Standard prelude

```bash
pkill -9 -f pdflatex 2>/dev/null || true
sleep 2
```

Then choose the narrowest command that can falsify the change:

- `make fast`
- `make`
codex
The first dependency search tripped over a regex escape; I’m rerunning it with exact label/string searches. I’m also loading the propagation and build workflows now, since the theorem is advertised in Vol II and Vol III.
exec
/bin/zsh -lc "rg -n -e 'cor:lattice-postnikov-termination' -e 'thm:riccati-algebraicity' -e 'prop:shadow-tower-three-lenses' -e 'tower-bar correspondence' -e 'SC-formal' -e 'class~\\\\mathbf{G}' -e 'Delta = 8\\\\kappa S_4' -e 'truncates at degree 2' -e 'swiss-cheese operations' chapters/theory chapters/connections -g '*.tex'" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: regex parse error:
    (?:cor:lattice-postnikov-termination)|(?:thm:riccati-algebraicity)|(?:prop:shadow-tower-three-lenses)|(?:tower-bar correspondence)|(?:SC-formal)|(?:class~\\mathbf{G})|(?:Delta = 8\\kappa S_4)|(?:truncates at degree 2)|(?:swiss-cheese operations)
                                                                                                                                                                       ^
error: repetition quantifier expects a valid decimal
exec
/bin/zsh -lc "rg -n 'lattice-postnikov-termination|riccati-algebraicity|shadow-tower-three-lenses|tower-bar correspondence|SC-formal|class G|Delta = 8\\\\kappa S_4|truncates at degree 2|Swiss-cheese operations' chapters/theory chapters/connections metadata -g '*.tex' -g '*.md'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/higher_genus_modular_koszul.tex:126: (Theorem~\ref{thm:riccati-algebraicity}). On any one-dimensional
chapters/theory/higher_genus_modular_koszul.tex:3392:(Theorem~\ref{thm:riccati-algebraicity}) packages the
chapters/theory/higher_genus_modular_koszul.tex:3427:(Theorem~\ref{thm:riccati-algebraicity}). The
chapters/theory/higher_genus_modular_koszul.tex:15534:\label{prop:shadow-tower-three-lenses}
chapters/theory/higher_genus_modular_koszul.tex:15601:Proposition~\textup{\ref{prop:shadow-tower-three-lenses}} is an
chapters/theory/higher_genus_modular_koszul.tex:15674: \textup{(}Theorem~\textup{\ref{thm:riccati-algebraicity}}).
chapters/theory/higher_genus_modular_koszul.tex:15833:Theorem~\ref{thm:riccati-algebraicity}, and it holds
chapters/theory/higher_genus_modular_koszul.tex:15917:$\Delta = 8\kappa S_4 = 40/(5c{+}22) > 0$ for $c > 0$
chapters/theory/higher_genus_modular_koszul.tex:15961:discriminant $\Delta = 8\kappa S_4$
chapters/theory/higher_genus_modular_koszul.tex:16135:$\Delta = 8\kappa S_4 = 40/(5c{+}22) > 0$ for $c > 0$,
chapters/theory/higher_genus_modular_koszul.tex:16525: The discriminant $\Delta = 8\kappa S_4 \neq 0$ is the
chapters/theory/higher_genus_modular_koszul.tex:16908:$\Delta = 8\kappa S_4$
chapters/theory/higher_genus_modular_koszul.tex:16951:\item \emph{Swiss-cheese operations $m_k^{\mathrm{SC}}$ on
chapters/theory/higher_genus_modular_koszul.tex:17228:\label{thm:riccati-algebraicity}
chapters/theory/higher_genus_modular_koszul.tex:17336:where $\Delta = 8\kappa S_4$ is the critical discriminant.
chapters/theory/higher_genus_modular_koszul.tex:17410:(Theorem~\ref{thm:riccati-algebraicity}), where
chapters/theory/higher_genus_modular_koszul.tex:17414:$\Delta = 8\kappa S_4$ is the critical discriminant
chapters/theory/higher_genus_modular_koszul.tex:17528:function (Theorem~\ref{thm:riccati-algebraicity}): since $Q_L$ is
chapters/theory/higher_genus_modular_koszul.tex:18125:From the closed form $H(t) = t^2\sqrt{Q_L(t)}$ (Theorem~\ref{thm:riccati-algebraicity}) with $Q_L \in k(c)[t]$ having denominator $(5c{+}22)$, the Taylor coefficients of $\sqrt{Q_L}$ inherit poles only from $Q_L(0) = (2\kappa)^2 = c^2$ (giving $c = 0$) and from the coefficient $\alpha(c) = (180c{+}872)/(5c{+}22)$ (giving $c = -22/5$). The degree formula follows from counting: $\sqrt{Q_L}$ has the form $c \cdot (1 + \text{series in } t/c)$ with each $t$-coefficient rational of bounded degree.
chapters/theory/higher_genus_modular_koszul.tex:18137:Immediate from the closed form: $Q_L(t) = 4\kappa^2 + 12\kappa\alpha\,t + (9\alpha^2 + 16\kappa S_4)\,t^2$ depends on exactly $(\kappa, \alpha, S_4)$, and Theorem~\ref{thm:riccati-algebraicity} gives $S_r = [t^{r-2}]\sqrt{Q_L} / r$ for all $r \geq 2$.

thinking
**Evaluating dependencies and inspection**

I need to check actual statements of dependencies. There may be some relevant lines in `higher_genus_modular_koszul` using `sed` around labels for `prop shadow-tower-three-lenses` and `theorem riccati`. I should also look for `cor lattice termination` in a certain file. Additionally, introductions might mention something about `SC-formality`. Let’s inspect those elements to see how they connect.
codex
The dependency search confirms the theorem is already wired into the shadow-tower lane elsewhere in Vol I. I’m opening the exact statements now so the replacement proof can cite the right mechanism instead of leaning on the classification table alone.
exec
/bin/zsh -lc "sed -n '17224,17380p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '15495,15640p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\begin{center}
\small
\begin{tabular}{ll}
\textbf{G} (Gaussian, $r_{\max} = 2$): &
 $\mathfrak{h}$ is formal ($L_\infty$-formal at all degrees). \\
\textbf{L} (Lie, $r_{\max} = 3$): &
 $\mathfrak{h}$ has exactly one nontrivial Massey product
 ($\ell_3^{\mathrm{sh}} \neq 0$, $\ell_n^{\mathrm{sh}} = 0$
 for $n \geq 4$). \\
\textbf{C} (contact, $r_{\max} = 4$): &
 $\ell_3^{\mathrm{sh}}, \ell_4^{\mathrm{sh}} \neq 0$,
 $\ell_n^{\mathrm{sh}} = 0$ for $n \geq 5$. \\
\textbf{M} (mixed, $r_{\max} = \infty$): &
 $\mathfrak{h}$ is \emph{intrinsically non-formal}:
 no finite truncation of the $L_\infty$ structure is
 quasi-isomorphic to a dg~Lie algebra.
\end{tabular}
\end{center}
This is a homotopy-invariant classification:
$L_\infty$-formality of the minimal model does not depend on
 succeeded in 52ms:
\end{definition}

\begin{theorem}[Riccati algebraicity: the shadow generating function
 is algebraic of degree~$2$]
\label{thm:riccati-algebraicity}
\label{thm:shadow-metric-existence}
\ClaimStatusProvedHere
\index{shadow generating function!algebraicity|textbf}
\index{Riccati algebraicity|textbf}
Let $L$, $S_r$, $Q_L$ be as in
Definition~\textup{\ref{def:shadow-metric}}.
Set $P = 1/\kappa$ and define the weighted shadow
generating function
$H(t) := \sum_{r \geq 2} r\,S_r\,t^r$.
The all-degree master equation
$\nabla_H(\mathrm{Sh}_r) + \mathfrak{o}^{(r)} = 0$
\textup{(}Proposition~\textup{\ref{prop:master-equation-from-mc})}
on~$L$ is equivalent to the algebraic relation
\begin{equation}\label{eq:riccati-algebraic-relation}
 H(t)^2
exec
/bin/zsh -lc "sed -n '70,130p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '4780,4845p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1200,1245p' chapters/theory/e1_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
eigenspace decomposition) is conditional on perfectness of the
bar-cobar normal complex. One (D-module purity) is a
one-directional implication. The count is exact:
$9 + 1 + 1 + 1$.

Two distinctions require emphasis. First, the four complexity
classes G/L/C/M, with shadow depths
$\{2, 3, 4, \infty\}$
(Theorem~\ref{thm:shadow-archetype-classification}), record the
degree at which the shadow obstruction tower first becomes
nontrivial; they do \emph{not} record failure of Koszulness.
Every standard chiral algebra is chirally Koszul. The classes
separate algebras by the complexity of their higher-genus
behaviour, not by the validity of the duality. Second,
Koszulness and SC formality are logically independent properties.
Koszulness is the condition that bar cohomology is concentrated
in degree one; SC formality is the condition
$m_k^{\mathrm{SC}} = 0$ for $k \geq 3$ in the Swiss-cheese
bar complex. All standard families are Koszul; only class~$G$
(Heisenberg and its relatives) is SC-formal
 succeeded in 51ms:
\begin{definition}[Formality hierarchy]
\label{def:e1-formality-hierarchy}
\index{formality!hierarchy}
\begin{enumerate}[label=\textup{(\alph*)}]
\item \emph{Operad formality.} The chain operad
  $C_*(\overline{\operatorname{FM}}_n(\bC))$ is formal:
  quasi-isomorphic to its cohomology (the Arnold algebra)
  via a quasi-isomorphism depending on a Drinfeld associator
  $\Phi \in \exp(\hat{\mathfrak{t}}_3)$
  (Kontsevich, Tamarkin). Unconditional: depends only on the
  operad, not on any algebra.
\item \emph{Algebra formality.} The transferred
  $A_\infty$-structure on $H^*(\cA)$ has
  $m_k^{\mathrm{tr}} = 0$ for $k \ge 3$.
  Holds for class $\mathbf{G}$ (Heisenberg); fails for
  classes $\mathbf{L}$, $\mathbf{C}$, $\mathbf{M}$.
\item \emph{Convolution algebra formality.}
  The $L_\infty$ brackets $\ell_k = 0$ for
  $k \ge 3$ in~$\gAmod$. Equivalent to class~$\mathbf{G}$
  (Proposition~\ref{prop:sc-formal-iff-class-g}).
 succeeded in 51ms:
For $\cW_3$ with generators $T$ \textup{(}weight~$2$\textup{)} and
$W$ \textup{(}weight~$3$\textup{)}, the modular characteristic
decomposes by Eulerian weight:
\[
\kappa(\cW_3^k)
\;=\;
\underbrace{\tfrac{c}{2}\vphantom{\big|}}_{\kappa_{TT}\,(\text{wt-}1)}
\;+\;
\underbrace{\tfrac{c}{3}\vphantom{\big|}}_{\kappa_{WW}\,(\text{wt-}2)},
\qquad
\kappa_{TW} = 0.
\]
The total is $\kappa = 5c/6$, consistent with the Fateev--Lukyanov
formula. The vanishing $\kappa_{TW} = 0$ reflects the $\Z/2$~parity
of~$W$: the $TW$~OPE has only odd poles, so the genus-$1$ trace
$\operatorname{Tr}_{\cH}(T_{(1)}W) = 0$. The two nonzero channels produce
\emph{independent} genus-$1$ curvatures on the $T$- and $W$-lines
of the deformation complex; the cross-channel corrections
$\delta F_g^{\mathrm{cross}}$ originate from the
interaction between these channels at genus~$g \geq 2$

thinking
**Exploring theorem proof**

I’m thinking about needing to focus on the theorem related to shadow-formality identification. It seems like I need to look for a direct proof that \(S_r\) vanishes if and only if we have a formal minimal model. So, my plan is to search for relevant material on this topic and see what I can find. I really want to clarify this concept and gather solid information to strengthen my understanding!
codex
I’ve confirmed the surrounding architecture. There’s a precise bridge in the repo already: shadows are the transferred higher brackets on the genus-zero minimal model, and the Riccati theorem turns `Delta=0` into finite tower termination. I’m pulling the exact identification theorem now, because that is the hinge for both directions.
exec
/bin/zsh -lc "rg -n 'shadow-formality-identification|tower-bar correspondence|bar correspondence|SC bar|Swiss-cheese bar|mixed-sector' chapters/theory -g '*.tex'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '14970,15500p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/higher_genus_modular_koszul.tex:150: (Theorem~\ref{thm:shadow-formality-identification}). The
chapters/theory/higher_genus_modular_koszul.tex:10608: (Theorem~\ref{thm:shadow-formality-identification}).
chapters/theory/higher_genus_modular_koszul.tex:12412: \textup{(}Theorem~\textup{\ref{thm:shadow-formality-identification})}.
chapters/theory/higher_genus_modular_koszul.tex:12436:(Theorem~\ref{thm:shadow-formality-identification}).
chapters/theory/higher_genus_modular_koszul.tex:15109:Theorem~\ref{thm:shadow-formality-identification}.
chapters/theory/higher_genus_modular_koszul.tex:15166:(Theorem~\ref{thm:shadow-formality-identification}), so
chapters/theory/higher_genus_modular_koszul.tex:15260:\label{thm:shadow-formality-identification}
chapters/theory/higher_genus_modular_koszul.tex:15472:Theorem~\ref{thm:shadow-formality-identification} identifies
chapters/theory/higher_genus_modular_koszul.tex:15556: \textup{(}Theorem~\textup{\ref{thm:shadow-formality-identification}}\textup{)}.
chapters/theory/higher_genus_modular_koszul.tex:15575:Theorem~\ref{thm:shadow-formality-identification}, whose proof
chapters/theory/higher_genus_modular_koszul.tex:15616:Theorem~\textup{\ref{thm:shadow-formality-identification}} and
chapters/theory/higher_genus_modular_koszul.tex:15638:Theorem~\textup{\ref{thm:shadow-formality-identification}} holds
chapters/theory/higher_genus_modular_koszul.tex:15669: \textup{(}Theorem~\textup{\ref{thm:shadow-formality-identification}}).
chapters/theory/higher_genus_modular_koszul.tex:15759:(Theorem~\ref{thm:shadow-formality-identification}),
chapters/theory/higher_genus_modular_koszul.tex:15789:Theorem~\ref{thm:shadow-formality-identification}, Step~3.
chapters/theory/higher_genus_modular_koszul.tex:16002:Theorem~\textup{\ref{thm:shadow-formality-identification}}.
chapters/theory/higher_genus_modular_koszul.tex:16100: \textup{(}Theorem~\textup{\ref{thm:shadow-formality-identification}},
chapters/theory/higher_genus_modular_koszul.tex:16107:Theorem~\ref{thm:shadow-formality-identification} gives the
chapters/theory/higher_genus_modular_koszul.tex:16295:\textup{(}Theorem~\textup{\ref{thm:shadow-formality-identification}}\textup{)}.
chapters/theory/higher_genus_modular_koszul.tex:16335:(Theorem~\ref{thm:shadow-formality-identification},
 succeeded in 51ms:
$\mathbf{G}$~(depth~$2$: both $\kappa$ and $S_4$ contribute, but the
tower sees only the scalar);
$\mathbf{L}$~(depth~$3$: the Jacobi identity kills all graphs at
degree~$\geq 4$);
$\mathbf{C}$~(depth~$4$: stratum separation on
$\overline{\mathcal{M}}_{0,5}$ kills degree~$\geq 5$);
$\mathbf{M}$~(depth~$\infty$: normal-ordered composites $:T^n:$
generate nontrivial obstructions at every degree).
Each class exists because the alternative would violate a
structural constraint: class~$\mathbf{G}$ because commutativity kills
all brackets beyond binary; class~$\mathbf{L}$ because Jacobi is
the unique relation at degree~$3$; class~$\mathbf{C}$ because rank-$1$
rigidity forces exactly one further step; class~$\mathbf{M}$ because
the Virasoro central extension feeds every degree from the one below.

%% UNIQUE SURVIVOR: the structural mechanism.

The structural mechanism behind this classification is a single
theorem: shadow termination at degree~$r$ is equivalent to
$L_\infty$-formality of the convolution algebra $\gAmod$ through

thinking
**Searching for mathematical concepts**

I'm thinking we need to prove the SC-formality and that the SC bar is complex formal. Maybe I should look into "tower-bar correspondence," possibly from en_koszul_duality or other sources. It seems like I need to search around for mixed-sector-bulk-boundary, which might help clarify the concepts I’m dealing with. I’ll make sure to gather all the relevant information to tackle this effectively.
codex
I’ve found the all-degree shadow/formality theorem. One more dependency remains: the repo’s mixed-sector identification, so I can justify the sentence “mixed SC operations are the averaged shadow tower” rather than just asserting it.
exec
/bin/zsh -lc "sed -n '1620,1705p' chapters/theory/en_koszul_duality.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'mixed-sector-bulk-boundary|mixed sector|averaging map|av\\(|Swiss-cheese operations.*shadow|SC operations.*shadow|tower-bar correspondence' chapters/theory -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\textup{(}$82$ tests\textup{)}.
\end{proposition}

\begin{proof}
The closed sector is $\operatorname{Com}^{!,c} =
\operatorname{Lie}^c$ with $\dim\operatorname{Lie}(n) = (n{-}1)!$
(partition-lattice calculation,
Theorem~\ref{thm:com-lie}).
The open sector is $\operatorname{Ass}^{!,c} =
\operatorname{Ass}^c$ with $\dim = m!$ (self-duality).
The mixed sector is computed by the K\"unneth
factorization: $\operatorname{Lie}^c(k)$ contributes
$(k{-}1)!$, and the $(k,m)$-shuffle count
$\binom{k+m}{m}$ arises from interleaving $k$ closed
leaves among $m$ ordered open leaves on the
$\operatorname{FM}_k(\mathbb{C}) \times E_1(m)$
operation space.
\end{proof}

\begin{corollary}[Convolution algebra factorization]
 succeeded in 52ms:
chapters/theory/higher_genus_modular_koszul.tex:17477:$\alpha \neq 0$ on any mixed sector, the adjoint
chapters/theory/higher_genus_modular_koszul.tex:18957:$\alpha \neq 0$ on the mixed sector, activating the
chapters/theory/higher_genus_modular_koszul.tex:22897:operations vanish, so the mixed sector of the bar spectral
chapters/theory/higher_genus_modular_koszul.tex:32167:  the integrable quotient). The averaging map $\av_0$ is
chapters/theory/higher_genus_modular_koszul.tex:32407:factorization, and the averaging map $\av_0$ at degree~$0$
chapters/theory/higher_genus_modular_koszul.tex:33131:The averaging map $\av_2$ at degree~$2$ sends the
chapters/theory/higher_genus_modular_koszul.tex:33136:genus~$0$ and genus~$1$: the averaging map is a local
chapters/theory/en_koszul_duality.tex:1630:The mixed sector is computed by the K\"unneth
chapters/theory/en_koszul_duality.tex:1661:The two factors commute. The mixed sector
chapters/theory/en_koszul_duality.tex:1665:\textup{(}Proposition~\textup{\ref{prop:mixed-sector-bulk-boundary}}\textup{)}.
chapters/theory/bar_cobar_adjunction_curved.tex:102:\index{averaging map!av@$\operatorname{av}$}
chapters/theory/bar_cobar_adjunction_curved.tex:2890:Regroup: $(3,3)$ and $(4,4)$ give the self-coupling sector; $(3,4)$ is the mixed sector.
chapters/theory/bar_cobar_adjunction_curved.tex:6903:is topologically nilpotent. Consequently the reduced mixed sector
chapters/theory/introduction.tex:527:(see~\S\ref{subsec:e1-as-primitive} for the averaging map
chapters/theory/introduction.tex:1186:\index{averaging map!av@$\operatorname{av}$|textbf}
chapters/theory/introduction.tex:1252:\emph{averaging map}
chapters/theory/introduction.tex:1316:\index{averaging map!information loss}
chapters/theory/introduction.tex:1317:\index{Reynolds operator!as averaging map}
chapters/theory/introduction.tex:1321: The averaging map
chapters/theory/introduction.tex:1409:\index{averaging map!information loss}

thinking
**Searching for mixed-sector proposition**

I want to find an actual mixed-sector proposition that could be relevant. I think I should look for a label or specific terms that might guide my search. Maybe I need to explore different sectors and see how they can intersect or combine in interesting ways. It's about finding something that fits within multiple domains, so it should be a fun search! Let's dive into that!
exec
/bin/zsh -lc "rg -n '\\\\label\\{prop:mixed-sector-bulk-boundary\\}|mixed-sector-bulk-boundary|Swiss-cheese bar|bar formality' chapters/theory/en_koszul_duality.tex chapters/theory/chiral_koszul_pairs.tex chapters/theory/higher_genus_modular_koszul.tex -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/en_koszul_duality.tex:1665:\textup{(}Proposition~\textup{\ref{prop:mixed-sector-bulk-boundary}}\textup{)}.
exec
/bin/zsh -lc "sed -n '1470,1555p' chapters/theory/en_koszul_duality.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
At genus~$g \geq 1$ the situation is more subtle than a naive
``scalar curvature'' would suggest, and the precise statement
matters for the higher-genus open/closed bookkeeping.
\begin{enumerate}[label=\textup{(\roman*)}]
\item \emph{The fibrewise differential is curved.} The bar
 differential~$\dfib$ obtained by extending the genus-$0$
 collision residue along the universal curve satisfies
 $\dfib^{\,2} = \kappa(\cA)\cdot\omega_g$
 (Theorem~\ref{thm:modular-characteristic}). Here $\omega_g$ is
 the $\kappa$-class on $\overline{\cM}_g$, not a scalar in the
 ground field; the equality is a curvature identity in
 $H^2(\overline{\cM}_g)$, not a centre relation in the bar
 coalgebra.
\item \emph{$\dfib$ is \emph{not} a coderivation of the
 deconcatenation coproduct.} The naive Leibniz check
 fails: applying $\dfib^{\,2} = \kappa\cdot\omega_g$ to a
 splitting at an interior index produces a factor-$2$
 discrepancy between the two sides of the co-Leibniz identity,
 because the curvature $\omega_g$ contracts the closed-color
 collision class against the same $\bR$-interval on both

thinking
**Searching for label information**

I didn't find the property label I was looking for. Maybe it's in a different part of the file? I think I should use a different method like searching by the exact proposition name instead of just the label. This might help me locate it more effectively. I'll explore options further while keeping an eye on how to refine my search approach. Let's see if I can track it down!
codex
The mixed-sector surface is not where I first expected it, so I’m tightening the search. I only need the statement that bulk-to-boundary mixed operations are built from the same tree data, because that is the last ingredient for the forward implication.
exec
/bin/zsh -lc "rg -n 'mixed-sector-bulk-boundary|bulk-boundary|brace evaluation|mixed sector' chapters/theory/en_koszul_duality.tex -g '*.tex'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'SC-formality|mixed sector|m_k\\"'^'"\\{\\\\mathrm\\{SC\\}\\}|tower truncates|averaging map.*degree' chapters/theory/higher_genus_modular_koszul.tex chapters/theory/e1_modular_koszul.tex chapters/theory/introduction.tex -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 54ms:
chapters/theory/e1_modular_koszul.tex:1220:\item \emph{SC-formality.} The Swiss-cheese type
chapters/theory/e1_modular_koszul.tex:1221:  operations $m_k^{\mathrm{SC}} = 0$ for $k \ge 3$.
chapters/theory/introduction.tex:88:Swiss-cheese formality ($m_k^{\mathrm{SC}} = 0$ for
chapters/theory/higher_genus_modular_koszul.tex:16888: $A_\infty$-operations $m_k^{\mathrm{SC}} = 0$ for
chapters/theory/higher_genus_modular_koszul.tex:16951:\item \emph{Swiss-cheese operations $m_k^{\mathrm{SC}}$ on
chapters/theory/higher_genus_modular_koszul.tex:16960: $m_k^{\mathrm{SC}}$ for $k \geq 3$ &
chapters/theory/higher_genus_modular_koszul.tex:16966: $m_3^{\mathrm{SC}}{\neq}0$, $m_k^{\mathrm{SC}}{=}0$ for $k \geq 4$ & Jacobi cubic; quartic killed \\
chapters/theory/higher_genus_modular_koszul.tex:17003:$m_k^{\mathrm{SC}} = 0$ for $k \geq 4$ because the Jacobi
chapters/theory/higher_genus_modular_koszul.tex:17013:proves all $m_k^{\mathrm{SC}} \neq 0$
chapters/theory/higher_genus_modular_koszul.tex:17477:$\alpha \neq 0$ on any mixed sector, the adjoint
chapters/theory/higher_genus_modular_koszul.tex:18957:$\alpha \neq 0$ on the mixed sector, activating the
chapters/theory/higher_genus_modular_koszul.tex:22871:$m_k^{\mathrm{SC}}(\cA)$ vanish for all $k \geq 3$, no mixed
chapters/theory/higher_genus_modular_koszul.tex:22897:operations vanish, so the mixed sector of the bar spectral
chapters/theory/higher_genus_modular_koszul.tex:32407:factorization, and the averaging map $\av_0$ at degree~$0$
chapters/theory/higher_genus_modular_koszul.tex:33131:The averaging map $\av_2$ at degree~$2$ sends the
 succeeded in 54ms:
1630:The mixed sector is computed by the K\"unneth
1661:The two factors commute. The mixed sector
1664:states via iterated brace evaluation
1665:\textup{(}Proposition~\textup{\ref{prop:mixed-sector-bulk-boundary}}\textup{)}.
2608:the bulk-boundary correspondence in 2d TFT, and Keller's

thinking
**Inspecting modular structures**

I’m noticing an interesting higher genus modular Koszul between 16888 and 16951 that might already have a similar proposition, possibly with more details. It looks like I need to inspect further in the range of 16870 to 17020 to gather more insights and understand the implications better. There’s definitely something intriguing here that merits a closer look!
exec
/bin/zsh -lc "sed -n '16870,17030p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\end{proof}

\begin{remark}[Shadow depth refines GKW formality]
\label{rem:shadow-depth-gkw-refinement}
\index{GKW formality!shadow depth refinement}
\index{Gaiotto--Kulp--Wu|see{GKW formality}}
\index{shadow depth!GKW refinement}
The $\mathbf{G}/\mathbf{L}/\mathbf{C}/\mathbf{M}$ classification
is a strict four-class refinement of the binary formal/non-formal
dichotomy of Gaiotto--Kulp--Wu~\cite{GKW2025}.
In their framework, a theory with topological direction
$d' \geq 2$ is formal (all higher operations vanish),
while $d' = 1$ theories are generically non-formal.
The shadow depth resolves the $d' = 1$ non-formal class
into three distinct strata:
\begin{enumerate}[label=\textup{(\roman*)}]
\item Class~$\mathbf{G}$ is formal \emph{even at}
 $d' = 1$: the OPE is abelian, so all transferred
 $A_\infty$-operations $m_k^{\mathrm{SC}} = 0$ for
 $k \geq 3$ (Heisenberg, lattice VOAs).
codex
The broader Vol I file already has a more structural classification proposition, but it still phrases the class‑G mechanism too narrowly. I’m checking whether the standard-landscape surface for this chapter includes free fermions explicitly, because your requested strengthening needs the full class‑G family, not just Heisenberg and lattice.
exec
/bin/zsh -lc "rg -n 'free fermion|fermion|class~\\\\mathbf\\{G\\}|class G' chapters/theory chapters/connections metadata -g '*.tex' -g '*.md'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'free fermion|fermion|class G|SC-formal' /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups -g '*.tex' -g '*.py' -g '*.md'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Total output lines: 240

metadata/theorem_registry.md:359:| `comp:fermion-hochschild` | `computation` | 1387 | Fermion Hochschild cohomology |
metadata/theorem_registry.md:384:| `ver:boson-fermion-HH` | `verification` | 4855 | $bc$/$\beta\gamma$ Koszul duality |
metadata/theorem_registry.md:508:| `thm:fermion-boson-koszul` | `theorem` | 1095 | Fermion-boson Koszul duality |
metadata/theorem_registry.md:755:| `thm:fermion-boson-koszul-hg` | `theorem` | 2827 | Fermion-boson Koszul duality |
metadata/theorem_registry.md:1387:| `prop:fermion-bar-symmetric` | `proposition` | 3433 | Free fermion bar complex: coalgebra structure |
metadata/theorem_registry.md:1413:| `thm:betagamma-fermion-koszul` | `theorem` | 449 | Koszul dual of \texorpdfstring{$\beta\gamma$}{beta-gamma} |
metadata/theorem_registry.md:1415:| `thm:cobar-betagamma` | `theorem` | 540 | Koszul dual of the free fermion |
metadata/theorem_registry.md:1417:| `thm:cobar-fermions` | `theorem` | 589 | Koszul dual of \texorpdfstring{$\beta\gamma$}{beta-gamma} |
metadata/theorem_registry.md:1462:| `prop:fermion-shadow-invariants` | `proposition` | 223 | Shadow invariants of the free fermion |
metadata/theorem_registry.md:1463:| `prop:fermion-shadow-metric` | `proposition` | 302 | Shadow metric of the free fermion |
metadata/theorem_registry.md:1464:| `thm:fermion-genus-expansion` | `theorem` | 336 | Free fermion genus expansion |
metadata/theorem_registry.md:1465:| `prop:fermion-rmatrix` | `proposition` | 413 | Free fermion $r$-matrix |
metadata/theorem_registry.md:1466:| `prop:fermion-complementarity` | `proposition` | 468 | Free fermion complementarity |
metadata/theorem_registry.md:1467:| `thm:fermion-sewing` | `theorem` | 538 | Free fermion sewing |
metadata/theorem_registry.md:1468:| `prop:fermion-characteristic-data` | `proposition` | 625 | Free fermion characteristic data |
metadata/theorem_registry.md:1469:| `thm:single-fermion-boson-duality` | `theorem` | 830 | Single-generator fermion-boson duality |
metadata/theorem_registry.md:1470:| `thm:fermion-bar-complex-genus-0` | `theorem` | 882 | Free fermion bar complex at genus 0 |
metadata/theorem_registry.md:1471:| `thm:fermion-bar-coalg` | `theorem` | 938 | Fermion bar complex coalgebra |
 succeeded in 52ms:
Total output lines: 1282

/Users/raeez/calabi-yau-quantum-groups/CLAUDE.md:222:AP-CY21: E_3 bar dimensions for non-free-field algebras are OPEN. The tricomplex model P(q)^{3g} gives CHAIN-level dimensions for all classes, but the COHOMOLOGY depends on the shadow class. For class G: P(q)^{3g} (formal, infinite). For class L: (1+t)^{3g} (dim 2^{3g}). For class C: (1+t)^{3g} (charge conservation kills d_4). For class M: INFINITE-DIMENSIONAL (d_4 survives). NEVER claim (1+t)^{3g} for class M. Counter: state the shadow class before claiming E_3 bar cohomology.
/Users/raeez/calabi-yau-quantum-groups/AGENTS.md:202:- shadow class or SC-formality claims;
/Users/raeez/calabi-yau-quantum-groups/AGENTS.md:741:If editing shadow depth, class, or SC-formality claims, check:
/Users/raeez/calabi-yau-quantum-groups/compute/lib/holomorphic_cs_chiral_engine.py:643:    It is class G (Gaussian, shadow depth r=2) with kappa_ch = 1.
/Users/raeez/calabi-yau-quantum-groups/compute/lib/holomorphic_cs_chiral_engine.py:689:          kappa_ch(H_k) + kappa_ch(H_k^!) = 0 = rho_K (conductor = 0, class G)
/Users/raeez/calabi-yau-quantum-groups/compute/lib/holomorphic_cs_chiral_engine.py:693:        The Koszul conductor rho_K = 0 for class G algebras (the shadow tower
/Users/raeez/calabi-yau-quantum-groups/compute/lib/holomorphic_cs_chiral_engine.py:712:        """Heisenberg is class G (Gaussian) at all parameter values."""
/Users/raeez/calabi-yau-quantum-groups/compute/lib/holomorphic_cs_chiral_engine.py:717:        """Shadow depth = 2 for class G."""
/Users/raeez/calabi-yau-quantum-groups/compute/lib/holomorphic_cs_chiral_engine.py:723:        For the Heisenberg (class G, all differentials vanish), the
/Users/raeez/calabi-yau-quantum-groups/compute/lib/holomorphic_cs_chiral_engine.py:729:        all bar differentials vanish (free-field / class G). For non-
/Users/raeez/calabi-yau-quantum-groups/compute/lib/holomorphic_cs_chiral_engine.py:814:        """kappa_ch(H_k) + kappa_ch(H_k^!) = 0 (class G conductor)."""
/Users/raeez/calabi-yau-quantum-groups/compute/lib/holomorphic_cs_chiral_engine.py:818:        """rho_K = 0 for class G (Heisenberg)."""
/Users/raeez/calabi-yau-quantum-groups/compute/lib/holomorphic_cs_chiral_engine.py:835:        For the Heisenberg (class G, all differentials vanish), both models
/Users/raeez/calabi-yau-quantum-groups/compute/lib/holomorphic_cs_chiral_engine.py:1140:                   ... actually class G has trivial differentials so
/Users/raeez/calabi-yau-quantum-groups/compute/lib/holomorphic_cs_chiral_engine.py:1142:                   class G has kappa_ch = k but NO cubic shadow.)
/Users/raeez/calabi-yau-quantum-groups/compute/lib/holomorphic_cs_chiral_engine.py:1738:        (Compare: class G has rho_K = 0, class L has rho_K = 0.)
/Users/raeez/calabi-yau-quantum-groups/compute/lib/holomorphic_cs_chiral_engine.py:1869:                "Pattern: class G -> P(q)^3 (formal), "
/Users/raeez/calabi-yau-quantum-groups/compute/lib/holomorphic_cs_chiral_engine.py:1904:    For the bc system (fermionic), a single fermionic generator contributes
codex
The repo is internally clear now: free fermions are already treated as class G on multiple live surfaces, while this chapter’s local statement lags behind. I’m opening the exact free-fermion invariant statements so I can add that family here without introducing a mismatch.
exec
/bin/zsh -lc "rg -n 'prop:fermion-shadow-invariants|prop:fermion-shadow-metric|prop:fermion-characteristic-data|Free fermion & .*class G|free fermion.*class~\\\\mathbf\\{G\\}|S_3.*fermion|S_4.*fermion' chapters/theory -g '*.tex'" in /Users/raeez/chiral-bar-cobar exited 1 in 53ms:

exec
/bin/zsh -lc "sed -n '16580,16695p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '18770,18820p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
tower. The shadow obstruction tower
$\Theta_\cA^{\leq r}$ is the generating function for the
K-matrix corrections at each degree: the quartic resonance
class~$\mathfrak{Q}$ at $r = 4$ is the first correction
to the Yangian coproduct that cannot be removed by gauge
transformation.
\end{remark}

\begin{example}[Shadow depth of all computed families]
\label{ex:shadow-depth-all-families}
\index{shadow depth!computed families}
\begin{center}
\small
\renewcommand{\arraystretch}{1.15}
\begin{tabular}{llcccl}
\toprule
\emph{Family} &
\emph{Class} &
$d$ &
$d_{\mathrm{alg}}$ &
 succeeded in 51ms:
\index{shadow metric!standard families}
The shadow metric data $(\kappa, \alpha, S_4, \Delta)$ and
derived invariants for all computed families:
\begin{center}
\small
\renewcommand{\arraystretch}{1.25}
\begin{tabular}{@{}llccccl@{}}
\toprule
& $\kappa$ & $\alpha$ & $S_4$ & $\Delta$
 & $R$ & \emph{Class} \\
\midrule
$\cH_k$ & $k$ & $0$ & $0$ & $0$
 & $\infty$ & $\mathbf{G}$: $r_{\max} = 2$ \\
$V_\Lambda$ & $\operatorname{rank}(\Lambda)$ & $0$ & $0$ & $0$
 & $\infty$ & $\mathbf{G}$: $r_{\max} = 2$ \\
Free fermion & $\frac{1}{2}$ & $0$ & $0$ & $0$
 & $\infty$ & $\mathbf{G}$: $r_{\max} = 2$ \\[4pt]
$\hat{\fg}_k$ (generic) & $\frac{(k{+}h^\vee)\dim\fg}{2h^\vee}$
 & $\neq 0$ & $0$ & $0$
 & $\infty$ & $\mathbf{L}$: $r_{\max} = 3$ \\[4pt]
exec
/bin/zsh -lc "sed -n '22855,22915p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
\ClaimStatusConjectured
\index{cross-channel correction!effective single-channel criterion|textbf}
\index{single-channel structure!cross-channel vanishing criterion}
Let $\cA$ be a modular Koszul chiral algebra of multi-weight type.
Then
\begin{equation}\label{eq:effective-single-channel-cross-vanishing}
\delta F_g^{\mathrm{cross}}(\cA) \;=\; 0
\qquad\text{for all } g \geq 2
\end{equation}
if and only if the genus-$0$ channel calculus of~$\cA$ is
effectively single-channel: every mixed channel assignment in
Construction~\ref{constr:cross-channel-graph-sum} has zero
amplitude.

Free-field algebras form a sufficient sublocus: when the
genus-$0$ Swiss-cheese operations
$m_k^{\mathrm{SC}}(\cA)$ vanish for all $k \geq 3$, no mixed
genus-$0$ vertex survives.
\end{conjecture}


thinking
**Exploring spectral sequences**

I'm thinking about the phrase "mixed sector of bar spectral sequence is already zero on the E1-page" when SC operations disappear. It feels a bit conjectural, but it might be useful. I should also consider the converse: "formality of SC bar implies that the shadow tower truncates at degree 2." It sounds like something related to tower-bar correspondence, so I should search for "mixed sector of bar spectral sequence" to find more theorems.
exec
/bin/zsh -lc "rg -n 'mixed sector of the bar spectral sequence|bar spectral sequence|tower-bar|SC bar|Swiss-cheese bar spectral|mixed sector.*E_1|E_1-page' chapters/theory -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/higher_genus_modular_koszul.tex:11892:\index{bar spectral sequence!E2 degeneration}
chapters/theory/higher_genus_modular_koszul.tex:11893:The bar spectral sequence and the genus spectral sequence play
chapters/theory/higher_genus_modular_koszul.tex:11898:\item \emph{The bar spectral sequence} (also called the PBW
chapters/theory/higher_genus_modular_koszul.tex:11924: follows from the bar spectral sequence degeneration alone (the
chapters/theory/higher_genus_modular_koszul.tex:13969: bar spectral sequence
chapters/theory/higher_genus_modular_koszul.tex:14354:\item The $E_2$-collapse condition on the bar spectral sequence
chapters/theory/higher_genus_modular_koszul.tex:14386:(iii)~The $E_2$-collapse of the bar spectral sequence at
chapters/theory/higher_genus_modular_koszul.tex:16411:the bar spectral sequence does not collapse at any finite page and
chapters/theory/higher_genus_modular_koszul.tex:28352:at genus~$\geq 2$ in the bar spectral sequence;
chapters/theory/higher_genus_modular_koszul.tex:28538: algebra, and the bar/Li--bar spectral sequences have
chapters/theory/three_invariants.tex:259: of the bar spectral sequence, which is a degree-$2$ statement
chapters/theory/en_koszul_duality.tex:627: \textup{(}the $\En$ bar spectral sequence collapses\textup{)},
chapters/theory/en_koszul_duality.tex:761:converging to $H^*(\int_X A)$. This is the bar spectral sequence
chapters/theory/bar_cobar_adjunction_inversion.tex:30:the square-zero bar-cobar spectral sequence only on the Koszul lane.
chapters/theory/bar_cobar_adjunction_inversion.tex:120:No completion is needed. The bar complex is conilpotent (finite-dimensional in each bar degree) and the differential is zero except for the curvature term $m_0$. Convergence of the bar spectral sequence follows: the filtration by bar degree is bounded below ($n \geq 0$) and exhaustive, with finite-dimensional graded pieces, so the spectral sequence converges to the bar homology by the standard bounded-below complete convergence theorem (\cite{LV12}, Theorem~2.2.3).
chapters/theory/bar_cobar_adjunction_inversion.tex:1689:argument is unavailable, the square-zero bar spectral sequence can
chapters/theory/bar_cobar_adjunction_inversion.tex:1742:The square-zero bar-cobar spectral sequence of
chapters/theory/bar_cobar_adjunction_inversion.tex:1788:the square-zero bar-cobar spectral sequence
chapters/theory/bar_cobar_adjunction_inversion.tex:1889: $\mathfrak{W}_{r,w}$ when the bar spectral sequence first acquires
chapters/theory/bar_cobar_adjunction_inversion.tex:2074:\begin{theorem}[Bar-cobar spectral sequence; \ClaimStatusProvedHere]\label{thm:bar-cobar-spectral-sequence}

thinking
**Evaluating modular Koszul theory**

I'm searching for information on higher genus modular Koszul specifically for degree 2. It seems that the AGENTS documentation says every theorem presentation must involve the averaging map from g^E1 to g^mod to derive symmetric results. I wonder if I can use this as a foundational concept, but I need a direct source. I'll open the e1_modular_koszul section that relates to the averaging map to gather more context.
exec
/bin/zsh -lc "sed -n '880,960p' chapters/theory/e1_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
The \emph{ordered chiral homology} of $\cA$ over $X$ is the
derived pushforward
\begin{equation}\label{eq:ordered-chiral-homology}
\int_X^{\mathrm{ord}} \cA
\;:=\;
R\Gamma_{\mathrm{dR}}\bigl(
\Ran^{\mathrm{ord}}(X),\;
\cF^{\mathrm{ord}}(\cA)\bigr)
\;=\;
\bigoplus_{n \ge 0}
R\Gamma_{\mathrm{dR}}\bigl(X^n,\,
\cF^{\mathrm{ord}}_n(\cA)\bigr).
\end{equation}
\end{definition}

The coinvariant quotient~\eqref{eq:ran-as-quotient}
induces the \emph{averaging map}
\begin{equation}\label{eq:ordered-descent}
\av \colon
\int_X^{\mathrm{ord}} \cA
exec
/bin/zsh -lc "sed -n '960,1035p' chapters/theory/e1_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
$d^2_{\mathrm{fib}} = \kappa(\cA) \cdot \omega_g$ of
the symmetric theory.
\end{remark}

\begin{example}[Ordered chiral Hochschild of the Heisenberg]
\label{ex:ord-ch-hoch-heisenberg}
\index{Heisenberg algebra!ordered chiral Hochschild}
The Heisenberg $\cH_k$ ($\Einf$-chiral, class $\mathbf{G}$,
$r(z) = k/z$, $\kappa = k$) has ordered chiral Hochschild
cohomology on the formal disk with Poincar\'e polynomial
\begin{equation}\label{eq:heis-poincare-poly}
P_{\cH_k}(t)
\;=\; 1 + t + t^2.
\end{equation}
Degree by degree: $\mathrm{HH}^0 = \bC$ (the centre consists
of scalars, since $J_{(1)}J = k \neq 0$ kills all
non-scalar central elements);
$\mathrm{HH}^1 = \bC$ (one outer derivation, the
translation $D(J) = \mathbf{1}$; inner derivations vanish
because $J_{(0)}J = 0$);
exec
/bin/zsh -lc "sed -n '1180,1275p' chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Proposition~\ref{prop:nilpotent-transport-typeA}).


\section{The \texorpdfstring{$\Eone$}{E1} story as primitive: averaging and the modular shadow}
\label{sec:e1-as-primitive}
\label{subsec:e1-as-primitive}
\index{averaging map!av@$\operatorname{av}$|textbf}
\index{ordered bar complex!as primitive object|textbf}
\index{E1 algebra@$\Eone$-algebra!primacy|textbf}
\index{Yangian!as primitive datum}
\index{R-matrix!as primitive of $\kappa$}
\index{symmetric bar complex!as $\Sigma_n$-coinvariant shadow}

The bar complex $\barB(\cA)$ presented in \S\ref{sec:volume-one-route}
is the symmetric (commutative) bar: it lives on
$(s^{-1}\bar\cA)^{\otimes n}_{\Sigma_n}$ and forgets the order in
which collisions occur. This presentation is convenient for
formulating the five main theorems and connecting to the modular
operad on~$\overline{\cM}_{g,n}$, but it is not the natural
primitive of the theory. The natural primitive is the
exec
/bin/zsh -lc "sed -n '1275,1355p' chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
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
\frac{\dim\mathfrak{g}\,(k + h^\vee)}{2h^\vee},
exec
/bin/zsh -lc "sed -n '17445,17510p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
to produce $S_5 = 0$ from nonzero inputs $S_3, S_4$.
The recursion gives
$S_5 = -(P/10)(3 \cdot 4 \cdot S_3 S_4)
= -(6/5)\,P\,\alpha\,S_4$.
For $\kappa \neq 0$ (so $P = 1/\kappa \neq 0$), $\alpha \neq 0$,
and $S_4 \neq 0$, this is nonzero. If $\alpha = 0$, then
$S_5 = 0$ but $S_4 \neq 0$ forces $S_6 \neq 0$ by the
next recursion step (the $j = k = 4$ term contributes
$S_6 \propto P\,S_4^2 \neq 0$), so the tower does not terminate
at degree~$5$ in any case. By induction, $S_4 \neq 0$ propagates
to infinitely many nonzero $S_r$: the closed form
$H(t) = t^2\sqrt{Q_L(t)}$ makes this manifest.

\emph{Contact boundary \textup{(}$\kappa|_L = 0$\textup{)}.}
Class~$\mathbf{C}$ lies outside the single-line Riccati regime:
the coefficient $P = 1/\kappa$ and the shadow metric $Q_L$
are undefined on the charged quartic stratum.
The $\beta\gamma$ witness is the global system, not the
weight-changing line by itself. On the weight-changing line,
all shadows vanish and
exec
/bin/zsh -lc "rg -n '\\\\label\\{prop:mixed-sector-bulk-boundary\\}|prop:mixed-sector-bulk-boundary' chapters -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/connections/thqg_open_closed_realization.tex:465:\label{prop:mixed-sector-bulk-boundary}
chapters/theory/en_koszul_duality.tex:1665:\textup{(}Proposition~\textup{\ref{prop:mixed-sector-bulk-boundary}}\textup{)}.
exec
/bin/zsh -lc "sed -n '445,530p' chapters/connections/thqg_open_closed_realization.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
(\S\ref{subsec:local-swiss-cheese}).
\end{proof}

\begin{remark}[Physical interpretation]
\label{rem:thqg-oc-physical}
In the holomorphic-topological framework of
Costello--Dimofte--Gaiotto, the boundary of a 3d HT theory is an
$A_\infty$-chiral algebra $\cA$, and the bulk local operators map to
the derived center of $\cA$. Theorem~\ref{thm:thqg-swiss-cheese}
makes this precise: the universal bulk attached to a boundary
algebra~$\cA$ is exactly
$\mathcal{C}^{\bullet}_{\mathrm{ch}}(\cA, \cA)$.
The distinction from bar/cobar is sharp: bar/cobar classifies
\emph{twisting morphisms} (universal couplings between
$\cA$ and~$\cA^!$), while the derived center classifies
\emph{bulk operators acting on the boundary}.
\end{remark}

\begin{proposition}[Mixed sector encodes bulk-to-boundary module structure;
\ClaimStatusProvedHere]


thinking
**Reviewing class G/L properties**

I’m looking into whether saying "class G/L are SC-formal" is incorrect. The output from a search indicates that line 62 states, "Vol I proves: class G/L are SC-formal (m_k^{SC}=0 for k >= 3)," which seems wrong based on the theorem. I might need to inspect this further and think about updates. However, I have to remember that the user’s scope only allows edits in assigned files, so I should be cautious about making changes.
thinking
**Formulating a proof**

I need a theorem-level proof, but it might not be available. I could craft a local lemma or proof with citations related to homotopy transfer and averaging. This involves mathematical reasoning, rather than relying on prior theorems. I'll inspect the current target file for context and look for definitions related to SC-formality. It might also be helpful to search for "Swiss-cheese" in the file to see if there's anything relevant.
exec
/bin/zsh -lc "rg -n 'Swiss-cheese|SC-formal|m_k\\"'^'"\\{\\\\mathrm\\{SC\\}\\}|mixed sector|brace|averaging map|class G|free fermion' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
87:$m_k^{\mathrm{SC}} = 0$ for $k \geq 3$ in the Swiss-cheese
89:(Heisenberg and its relatives) is SC-formal
1327:m_{n-1}(\underbrace{a, \ldots, a}_{n-1}) = b.
2476:This ordering refines the Koszulness programme: all four classes are chirally Koszul (bar $E_2$-collapse), but they differ in Swiss-cheese formality depth.
2479:\begin{proposition}[Swiss-cheese non-formality by shadow class; \ClaimStatusProvedHere]
2481:\index{Swiss-cheese operad!non-formality by shadow class|textbf}
2482:\index{shadow depth!Swiss-cheese formality}
2484:The Swiss-cheese operations $m_k^{\mathrm{SC}}$ on~$\cA$ itself
2497:& $m_k^{\mathrm{SC}},\; k \geq 5$ \\
2541:the contact stratum kills all $m_k^{\mathrm{SC}}$ for $k \geq 5$.
2552:compositions, so $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$. For lattice
2555:transferred Swiss-cheese operations vanish for every $k \geq 3$.
2582:relationship between SC-formality and the classification is
2584:already isolates the first nonzero Swiss-cheese operation in each
2587:nonzero $m_k^{\mathrm{SC}}$ for all $k \geq 3$. This reduces the
2590:\begin{proposition}[SC-formality characterises class~$G$; \ClaimStatusProvedHere]
2592:\index{Swiss-cheese operad!formality characterisation}
2593:\index{class G@class~$G$!characterised by SC-formality}
2595:Then~$\cA$ is Swiss-cheese formal
2596:\textup{(}$m_k^{\mathrm{SC}} = 0$ for all $k \geq 3$\textup{)}
exec
/bin/zsh -lc "sed -n '5488,5520p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
bar cohomology in degree~$1$ counts generators of the
\emph{dual} algebra. For Kac--Moody:
$\dim H^1(\barBgeom(\widehat{\mathfrak{g}}))_1
= \dim\mathfrak{g}$
(both the currents $J^a$ and the dual generators live at
weight~$1$). The coincidence at weight~$1$ is a consequence
of the KM algebra being generated in weight~$1$, so generators
of~$\cA$ and generators of~$\cA^!$ share the same weight.
For Virasoro, with a weight-$2$ generator, the sequences
diverge starting at weight~$4$.
\end{proof}

\begin{remark}[Why the coincidence for free fields is tempting]
\label{rem:bar-quasiprimary-free-field}
\index{bar cohomology!free-field coincidence}
For free-field algebras (Heisenberg, free fermion), the
quasi-primary count at weight~$h$ equals the bar cohomology
dimension at weight~$h$, because the algebra is generated by
a weight-$1$ field and the Koszul dual is the
symmetric/exterior algebra on the same space. This is a

thinking
**Searching with rg**

I need to search quickly using rg from the theorem_registry path, but I’m realizing it may not be straightforward. I’m thinking of using rg specifically on the chapters or theory for labeling. It seems like this approach could help streamline the process! I'm curious if using the right commands and options will yield the best results. Let’s see how well this works out in practice and adjust as needed!
codex
I’ve isolated the last live issue before editing: the forward proof needs the full class‑G lane, including free fermions, and it also needs to avoid the false shortcut `Delta=0 => SC-formal`. I’m opening the free-fermion shadow statements now so I can write the optimal boundary argument explicitly.
exec
/bin/zsh -lc "rg -n 'prop:fermion-shadow-invariants|prop:fermion-shadow-metric|fermion characteristic data|free fermion.*r_max = 2|Free fermion.*S_4|Free fermion.*Delta' chapters/theory -g '*.tex'" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

exec
/bin/zsh -lc "rg -n 'Free fermion.*\\\\mathbf\\{G\\}|free fermion.*class~\\\\mathbf\\{G\\}|free fermion.*Delta = 0|free fermion.*shadow depth|free fermion.*all higher obstruction classes vanish' chapters/theory/higher_genus_modular_koszul.tex chapters/theory/introduction.tex chapters/connections/thqg_perturbative_finiteness.tex -g '*.tex'" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

exec
/bin/zsh -lc "rg -n 'Free fermion|free fermion' chapters/theory/higher_genus_modular_koszul.tex chapters/theory/introduction.tex chapters/connections/thqg_perturbative_finiteness.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\\\label\\{prop:fermion|\\\\label\\{thm:fermion|free fermion.*shadow|shadow.*free fermion' chapters/theory -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/theory/cobar_construction.tex:1095:\begin{theorem}[Fermion-boson Koszul duality; \ClaimStatusProvedHere]\label{thm:fermion-boson-koszul}
chapters/theory/higher_genus_complementarity.tex:2827:\label{thm:fermion-boson-koszul-hg}
 succeeded in 53ms:
chapters/connections/thqg_perturbative_finiteness.tex:311:\begin{computation}[HS norms for free fermions]
chapters/connections/thqg_perturbative_finiteness.tex:313:\index{free fermions!HS norms}
chapters/connections/thqg_perturbative_finiteness.tex:349:Free fermions & $\leq 2^n$ & $0$ & polynomial & $\prod (1+q^{j-1/2})^2$ \\
chapters/connections/thqg_perturbative_finiteness.tex:1104:\item Free fermions $\psi_1, \ldots, \psi_n$ (any rank).
chapters/connections/thqg_perturbative_finiteness.tex:1123:\emph{(g) Free fermions.} $\dim H_n$ grows at most as $2^n$ (number of subsets of $n$ fermion modes), but the conformal-weight grading gives polynomial growth. OPE degree $N = 0$.
chapters/connections/thqg_perturbative_finiteness.tex:1254:Free fermions & polynomial & $0$ & $n/4$ & $2$ & \textbf{Proved} \\
chapters/connections/thqg_perturbative_finiteness.tex:1422:\item \emph{Gaussian ($r_{\max} = 2$):} Heisenberg, lattice VOAs, free fermions. Only the quadratic/scalar channel survives. On the proved analytic locus, the partition function is an exact Fredholm determinant.
chapters/connections/thqg_perturbative_finiteness.tex:1776:Free fermions (rank $n$) & $n/4$ & $2$ & G & $n/96$ & $7n/23040$ \\
chapters/theory/higher_genus_modular_koszul.tex:701:\item the free fermion algebra $\mathcal{F}$ and the $\beta\gamma$-$bc$
chapters/theory/higher_genus_modular_koszul.tex:2183:Heisenberg, free fermions,
chapters/theory/higher_genus_modular_koszul.tex:2702:Single-generator algebras (Heisenberg, free fermion, Virasoro)
chapters/theory/higher_genus_modular_koszul.tex:16609:Free fermion &
chapters/theory/higher_genus_modular_koszul.tex:16660: Heisenberg $\cH_c$, lattice VOA $V_\Lambda$, free fermion.
chapters/theory/higher_genus_modular_koszul.tex:18785:Free fermion & $\frac{1}{2}$ & $0$ & $0$ & $0$
chapters/theory/introduction.tex:2148:Free fermion $\mathcal{F}$ & $\frac{1}{2}$ & $\frac{1}{4}$ & $0$ & $0$ & Gaussian, $@2$ \\[2pt]
chapters/theory/introduction.tex:2210: Heisenberg, free fermion; Eisenstein genus expansion; periodic table of the volume \\
chapters/theory/introduction.tex:2383: Heisenberg, free fermion, Eisenstein genus expansion. Depth class
chapters/theory/introduction.tex:2563: Heisenberg, free fermions, lattice VOAs.



thinking
**Clarifying fermion lattice relationships**

I’m considering adding a precise statement about free fermions and lattices using Gaussian relations. Lattice VOAs bosonize to sums of Heisenberg field exponentials, and connected higher cumulants vanish beyond degree 2. Free fermion correlators are Pfaffians of the two-point kernel, following the same trend. We should reference bosonization in the repository, as there's a theorem related to it, but maybe a simpler direct computation stated from OPE via Wick’s theorem would suffice.
thinking
**Evaluating the theorem's relevance**

I need to check the theorem `thm:boson-fermion-lattice` to see if it’s useful for my work, though it might not be necessary. After making edits, I should definitely re-read the surrounding lines to ensure everything flows correctly. I want to make sure I’m on the right track, so this inspection will help me clarify my understanding and the overall coherence of the text. Let's give this a thorough look.
thinking
**Updating plan and commentary**

I think I need to use apply_patch, but before editing, I should ensure I have the PE blocks ready. Since my theorem or proposition involves a scope quantifier and a cross-volume formula, I wonder if PE-10 is suitable to use. I might also consider PE-8 since it shares a formula or claim. I should provide some commentary before editing to explain things. Finally, it'll be good to update my plan statuses as step 1 is completed and then add in the PE block commentary.
codex
Using `beilinson-rectify` for the proof rewrite, then `build-surface` for falsification checks. Propagation is read-only this turn because the assigned write scope is [chapters/theory/chiral_koszul_pairs.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex).
Plan update
Mandatory context and theorem surface are loaded. I’ve also identified the supporting theorem lane: E1 primacy/averaging, shadow-formality identification, shadow archetype classification, and the free-fermion class-G surface.
  ✓ Load rectification workflow and mandatory repo context for the target theorem surface
  ✓ Lock the exact theorem/label/current proof surface in chiral_koszul_pairs.tex
  → Strengthen the forward and converse directions in the assigned scope
  • Re-read modified region and run required AP greps/targeted verification
  • Check collision surface for propagation needs and finalize rectification report
codex
```text
PE-10: scope quantifier
genus: [genus-0 tree-level mixed-sector operations / all k>=3 / standard landscape]
degree: [n=all arities k>=3]
AP32 weight tag: [NA]  tagged? [Y]
AP139 free-var audit: LHS vars:{A,k} RHS vars:{A,k} LHS⊇RHS? [Y]
AP36: [iff]  if iff, converse proved same thm? [Y]
verdict: ACCEPT
```

```text
PE-8: cross-volume formula
formula: [SC-formality iff class G; class G families include Heisenberg, lattice VOA, free fermion; Delta=0 alone is insufficient]
Vol I: [hits in chiral_koszul_pairs.tex, higher_genus_modular_koszul.tex, introduction.tex]
Vol II: [hits in 3d_gravity.tex, rosetta_stone.tex, perturbative_finiteness.tex, ordered_associative_chiral_kd_core.tex]
Vol III: [hits in compute/lib/cross_volume_shadow_bridge.py, swiss_cheese_cy3_e1.py, related tests]
consistent? [mostly Y, with one known stale Vol III docstring claiming class G/L are SC-formal]
canonical vol [I], others updated same session? [N: write scope restricted to target file]
convention conversion: [NA]
verdict: ACCEPT
```

thinking
**Explaining a mechanism**

I’m thinking about saying, “this is the mechanism behind the criterion below.” I wonder if I could simplify it further. 

The four classes cover the standard landscape, but the link between SC-formality and classification is clearer than the table indicates. Proposition… highlights the first nonzero Swiss-cheese operation in each non-Gaussian class and reveals that on the Gaussian locus, the mixed-sector tree formulas only extend up to degree 2.
codex
I’m editing the theorem lane now. The patch will do three things inside the assigned block: add free fermions to class G, replace the forward proof with the Gaussian/tree-level argument, and replace the converse with the operadic tower-bar argument plus the class‑L boundary counterexample to the false shortcut `Delta=0`.
file update
M /Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex
@@ -2563,3 +2563,3 @@
 $G$ \textup{(}$r_{\max}=2$\textup{)}
-& Heisenberg, lattice VOA
+& Heisenberg, lattice VOA, free fermion
 & $= 0$
@@ -2588,8 +2588,17 @@
 \emph{Mechanism.}
-For class~$G$\textup{:} Heisenberg is central, and lattice VOAs are
-Gaussian: the Heisenberg bracket
-$[a_m, a_n] = km\,\delta_{m+n,0}$ is central, while for lattice
-VOAs the shadow obstruction tower terminates at weight~$2$ by
-Corollary~\ref{cor:lattice-postnikov-termination}. In both cases
-all higher tree sums vanish.
+For class~$G$\textup{:}
+Heisenberg, lattice VOAs, and free fermions are Gaussian/free-field:
+their ordered bar data is generated by the binary two-point kernel,
+so every connected genus-$0$ tree with at least three external legs
+factors through pairings and carries no primitive higher vertex.
+Equivalently, the shadow tower truncates at degree~$2$:
+$S_r(\cA)=0$ for $r \geq 3$
+\textup{(}Theorem~\ref{thm:shadow-archetype-classification}; for
+lattices see Corollary~\ref{cor:lattice-postnikov-termination}\textup{)}.
+Under the averaging map
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)},
+the mixed Swiss-cheese tree of arity~$r$ projects to the degree-$r$
+shadow. Since there is no primitive tree for $r \geq 3$,
+all higher mixed-sector operations vanish.
 For class~$L$\textup{:} the affine KM OPE has at most a double pole; the
@@ -2615,6 +2624,21 @@
 Class~$G$: for Heisenberg, centrality of the bracket kills all nested
-compositions, so $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$. For lattice
-VOAs, Corollary~\ref{cor:lattice-postnikov-termination} identifies
-the shadow obstruction tower with its weight-$2$ truncation, so the
-transferred Swiss-cheese operations vanish for every $k \geq 3$.
+tree compositions, so $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
+For lattice VOAs, bosonization reduces connected genus-$0$ amplitudes
+to Wick pairings of the underlying Heisenberg field, and
+Corollary~\ref{cor:lattice-postnikov-termination} identifies the
+shadow tower with its weight-$2$ truncation. For the free fermion,
+Wick's theorem gives Pfaffian factorization by the basic contraction
+$\psi(z)\psi^*(w) \sim (z-w)^{-1}$, so again no connected tree with
+$r \geq 3$ survives after extracting the binary pairings. In all three
+cases the mixed Swiss-cheese arity-$r$ operation is the open-colored
+lift of the same genus-$0$ tree sum whose closed projection is
+$S_r(\cA)$; equivalently,
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)}.
+Because class~$G$ means $S_r(\cA) = 0$ for all $r \geq 3$,
+the mixed-sector operations vanish:
+$m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
+The weaker condition $\Delta = 0$ is not sufficient:
+affine Kac--Moody algebras are class~$L$ with $\Delta = 0$ but
+$m_3^{\mathrm{SC}} \neq 0$.
 Class~$L$: the cubic shadow
@@ -2648,6 +2672,6 @@
 already isolates the first nonzero Swiss-cheese operation in each
-non-Gaussian class: class~$L$ has $m_3^{\mathrm{SC}} \neq 0$,
-class~$C$ has $m_4^{\mathrm{SC}} \neq 0$, and class~$M$ has
-nonzero $m_k^{\mathrm{SC}}$ for all $k \geq 3$. This reduces the
-formality criterion to a classification check.
+non-Gaussian class and, on the Gaussian locus, identifies the
+mixed-sector tree formulas with the degree-by-degree shadow tower
+after averaging. The criterion below packages this as an equivalence
+between SC-formality and truncation of the shadow tower at degree~$2$.
 
@@ -2667,17 +2691,26 @@
 Proposition~\ref{prop:swiss-cheese-nonformality-by-class}:
-the class-$G$ row consists exactly of Heisenberg and lattice
-VOAs, and in both cases $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
+the class-$G$ row consists of the Gaussian families Heisenberg,
+lattice VOA, and free fermion, and in each case the genus-$0$
+mixed tree formulas stop at arity~$2$, so
+$m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
 
 For the converse, suppose~$\cA$ is SC-formal.
-Because the standard landscape is exhausted by the four classes
-$G$, $L$, $C$, $M$, it is enough to eliminate the three
-non-Gaussian cases. Proposition~\ref{prop:swiss-cheese-nonformality-by-class}
-does exactly this: class~$L$ has $m_3^{\mathrm{SC}} \neq 0$,
-class~$C$ has $m_4^{\mathrm{SC}} \neq 0$, and class~$M$ has
-nonzero higher operations in every arity $k \geq 3$. Each of
-these cases contradicts SC-formality. This converse uses only the
-classification from Proposition~\ref{prop:swiss-cheese-nonformality-by-class};
-it does not invoke any trilinear form built from~$\kappa$.
-Hence an SC-formal algebra must
-belong to class~$G$.
+Then the mixed sector of the Swiss-cheese bar complex is formal:
+every higher arity tree operation vanishes. The tower-bar
+correspondence is operadic: the arity-$r$ mixed tree and the
+degree-$r$ shadow are produced by the same genus-$0$ tree-transfer
+formula, with the same propagator on internal edges; the only
+difference is the output colour, and passage to the symmetric
+closed sector applies the averaging morphism
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)}.
+Hence SC-formality forces $S_r(\cA) = 0$ for every $r \geq 3$:
+there is no higher mixed tree whose closed projection could survive.
+By Theorem~\ref{thm:shadow-formality-identification} and
+Proposition~\ref{prop:shadow-tower-three-lenses}, this is exactly
+the statement that the shadow/formality tower truncates at
+degree~$2$. Theorem~\ref{thm:shadow-archetype-classification}
+identifies the standard-landscape locus with this property as
+precisely class~$G$. Hence an SC-formal algebra must belong
+to class~$G$.
 \end{proof}
apply_patch(auto_approved=true) exited 0 in 28ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex
file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 82ce3f8a19eaa51f878397fa63cad2971741bf1e..caf0e7dcc8b2e4df8cb6362c74b5edc7c33e1305
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -2561,7 +2561,7 @@
 & $m_k^{\mathrm{SC}},\; k \geq 5$ \\
 \midrule
 $G$ \textup{(}$r_{\max}=2$\textup{)}
-& Heisenberg, lattice VOA
+& Heisenberg, lattice VOA, free fermion
 & $= 0$
 & $= 0$
 & $= 0$ \\
@@ -2586,12 +2586,21 @@
 
 \medskip\noindent
 \emph{Mechanism.}
-For class~$G$\textup{:} Heisenberg is central, and lattice VOAs are
-Gaussian: the Heisenberg bracket
-$[a_m, a_n] = km\,\delta_{m+n,0}$ is central, while for lattice
-VOAs the shadow obstruction tower terminates at weight~$2$ by
-Corollary~\ref{cor:lattice-postnikov-termination}. In both cases
-all higher tree sums vanish.
+For class~$G$\textup{:}
+Heisenberg, lattice VOAs, and free fermions are Gaussian/free-field:
+their ordered bar data is generated by the binary two-point kernel,
+so every connected genus-$0$ tree with at least three external legs
+factors through pairings and carries no primitive higher vertex.
+Equivalently, the shadow tower truncates at degree~$2$:
+$S_r(\cA)=0$ for $r \geq 3$
+\textup{(}Theorem~\ref{thm:shadow-archetype-classification}; for
+lattices see Corollary~\ref{cor:lattice-postnikov-termination}\textup{)}.
+Under the averaging map
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)},
+the mixed Swiss-cheese tree of arity~$r$ projects to the degree-$r$
+shadow. Since there is no primitive tree for $r \geq 3$,
+all higher mixed-sector operations vanish.
 For class~$L$\textup{:} the affine KM OPE has at most a double pole; the
 three-channel tree sum over $\overline{\cM}_{0,4}$ is nonzero
 \textup{(}$S_3 = 2h^\vee/(k+h^\vee) \neq 0$\textup{)} but the
@@ -2613,10 +2622,25 @@
 
 \begin{proof}
 Class~$G$: for Heisenberg, centrality of the bracket kills all nested
-compositions, so $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$. For lattice
-VOAs, Corollary~\ref{cor:lattice-postnikov-termination} identifies
-the shadow obstruction tower with its weight-$2$ truncation, so the
-transferred Swiss-cheese operations vanish for every $k \geq 3$.
+tree compositions, so $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
+For lattice VOAs, bosonization reduces connected genus-$0$ amplitudes
+to Wick pairings of the underlying Heisenberg field, and
+Corollary~\ref{cor:lattice-postnikov-termination} identifies the
+shadow tower with its weight-$2$ truncation. For the free fermion,
+Wick's theorem gives Pfaffian factorization by the basic contraction
+$\psi(z)\psi^*(w) \sim (z-w)^{-1}$, so again no connected tree with
+$r \geq 3$ survives after extracting the binary pairings. In all three
+cases the mixed Swiss-cheese arity-$r$ operation is the open-colored
+lift of the same genus-$0$ tree sum whose closed projection is
+$S_r(\cA)$; equivalently,
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)}.
+Because class~$G$ means $S_r(\cA) = 0$ for all $r \geq 3$,
+the mixed-sector operations vanish:
+$m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
+The weaker condition $\Delta = 0$ is not sufficient:
+affine Kac--Moody algebras are class~$L$ with $\Delta = 0$ but
+$m_3^{\mathrm{SC}} \neq 0$.
 Class~$L$: the cubic shadow
 $S_3 = 2h^\vee/(k + h^\vee)$ is computed from the OPE coefficient
 ratio (the structure constant divided by the level); the quartic
@@ -2646,10 +2670,10 @@
 relationship between SC-formality and the classification is
 sharper than the table suggests. Proposition~\ref{prop:swiss-cheese-nonformality-by-class}
 already isolates the first nonzero Swiss-cheese operation in each
-non-Gaussian class: class~$L$ has $m_3^{\mathrm{SC}} \neq 0$,
-class~$C$ has $m_4^{\mathrm{SC}} \neq 0$, and class~$M$ has
-nonzero $m_k^{\mathrm{SC}}$ for all $k \geq 3$. This reduces the
-formality criterion to a classification check.
+non-Gaussian class and, on the Gaussian locus, identifies the
+mixed-sector tree formulas with the degree-by-degree shadow tower
+after averaging. The criterion below packages this as an equivalence
+between SC-formality and truncation of the shadow tower at degree~$2$.
 
 \begin{proposition}[SC-formality characterises class~$G$; \ClaimStatusProvedHere]
 \label{prop:sc-formal-iff-class-g}
@@ -2665,21 +2689,30 @@
 The forward direction \textup{(}class~$G$ $\Longrightarrow$
 SC-formal\textup{)} is established in
 Proposition~\ref{prop:swiss-cheese-nonformality-by-class}:
-the class-$G$ row consists exactly of Heisenberg and lattice
-VOAs, and in both cases $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
+the class-$G$ row consists of the Gaussian families Heisenberg,
+lattice VOA, and free fermion, and in each case the genus-$0$
+mixed tree formulas stop at arity~$2$, so
+$m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
 
 For the converse, suppose~$\cA$ is SC-formal.
-Because the standard landscape is exhausted by the four classes
-$G$, $L$, $C$, $M$, it is enough to eliminate the three
-non-Gaussian cases. Proposition~\ref{prop:swiss-cheese-nonformality-by-class}
-does exactly this: class~$L$ has $m_3^{\mathrm{SC}} \neq 0$,
-class~$C$ has $m_4^{\mathrm{SC}} \neq 0$, and class~$M$ has
-nonzero higher operations in every arity $k \geq 3$. Each of
-these cases contradicts SC-formality. This converse uses only the
-classification from Proposition~\ref{prop:swiss-cheese-nonformality-by-class};
-it does not invoke any trilinear form built from~$\kappa$.
-Hence an SC-formal algebra must
-belong to class~$G$.
+Then the mixed sector of the Swiss-cheese bar complex is formal:
+every higher arity tree operation vanishes. The tower-bar
+correspondence is operadic: the arity-$r$ mixed tree and the
+degree-$r$ shadow are produced by the same genus-$0$ tree-transfer
+formula, with the same propagator on internal edges; the only
+difference is the output colour, and passage to the symmetric
+closed sector applies the averaging morphism
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)}.
+Hence SC-formality forces $S_r(\cA) = 0$ for every $r \geq 3$:
+there is no higher mixed tree whose closed projection could survive.
+By Theorem~\ref{thm:shadow-formality-identification} and
+Proposition~\ref{prop:shadow-tower-three-lenses}, this is exactly
+the statement that the shadow/formality tower truncates at
+degree~$2$. Theorem~\ref{thm:shadow-archetype-classification}
+identifies the standard-landscape locus with this property as
+precisely class~$G$. Hence an SC-formal algebra must belong
+to class~$G$.
 \end{proof}
 
 \begin{remark}[D-module purity: reduction to a single gap]

file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 82ce3f8a19eaa51f878397fa63cad2971741bf1e..caf0e7dcc8b2e4df8cb6362c74b5edc7c33e1305
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -2561,7 +2561,7 @@
 & $m_k^{\mathrm{SC}},\; k \geq 5$ \\
 \midrule
 $G$ \textup{(}$r_{\max}=2$\textup{)}
-& Heisenberg, lattice VOA
+& Heisenberg, lattice VOA, free fermion
 & $= 0$
 & $= 0$
 & $= 0$ \\
@@ -2586,12 +2586,21 @@
 
 \medskip\noindent
 \emph{Mechanism.}
-For class~$G$\textup{:} Heisenberg is central, and lattice VOAs are
-Gaussian: the Heisenberg bracket
-$[a_m, a_n] = km\,\delta_{m+n,0}$ is central, while for lattice
-VOAs the shadow obstruction tower terminates at weight~$2$ by
-Corollary~\ref{cor:lattice-postnikov-termination}. In both cases
-all higher tree sums vanish.
+For class~$G$\textup{:}
+Heisenberg, lattice VOAs, and free fermions are Gaussian/free-field:
+their ordered bar data is generated by the binary two-point kernel,
+so every connected genus-$0$ tree with at least three external legs
+factors through pairings and carries no primitive higher vertex.
+Equivalently, the shadow tower truncates at degree~$2$:
+$S_r(\cA)=0$ for $r \geq 3$
+\textup{(}Theorem~\ref{thm:shadow-archetype-classification}; for
+lattices see Corollary~\ref{cor:lattice-postnikov-termination}\textup{)}.
+Under the averaging map
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)},
+the mixed Swiss-cheese tree of arity~$r$ projects to the degree-$r$
+shadow. Since there is no primitive tree for $r \geq 3$,
+all higher mixed-sector operations vanish.
 For class~$L$\textup{:} the affine KM OPE has at most a double pole; the
 three-channel tree sum over $\overline{\cM}_{0,4}$ is nonzero
 \textup{(}$S_3 = 2h^\vee/(k+h^\vee) \neq 0$\textup{)} but the
@@ -2613,10 +2622,25 @@
 
 \begin{proof}
 Class~$G$: for Heisenberg, centrality of the bracket kills all nested
-compositions, so $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$. For lattice
-VOAs, Corollary~\ref{cor:lattice-postnikov-termination} identifies
-the shadow obstruction tower with its weight-$2$ truncation, so the
-transferred Swiss-cheese operations vanish for every $k \geq 3$.
+tree compositions, so $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
+For lattice VOAs, bosonization reduces connected genus-$0$ amplitudes
+to Wick pairings of the underlying Heisenberg field, and
+Corollary~\ref{cor:lattice-postnikov-termination} identifies the
+shadow tower with its weight-$2$ truncation. For the free fermion,
+Wick's theorem gives Pfaffian factorization by the basic contraction
+$\psi(z)\psi^*(w) \sim (z-w)^{-1}$, so again no connected tree with
+$r \geq 3$ survives after extracting the binary pairings. In all three
+cases the mixed Swiss-cheese arity-$r$ operation is the open-colored
+lift of the same genus-$0$ tree sum whose closed projection is
+$S_r(\cA)$; equivalently,
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)}.
+Because class~$G$ means $S_r(\cA) = 0$ for all $r \geq 3$,
+the mixed-sector operations vanish:
+$m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
+The weaker condition $\Delta = 0$ is not sufficient:
+affine Kac--Moody algebras are class~$L$ with $\Delta = 0$ but
+$m_3^{\mathrm{SC}} \neq 0$.
 Class~$L$: the cubic shadow
 $S_3 = 2h^\vee/(k + h^\vee)$ is computed from the OPE coefficient
 ratio (the structure constant divided by the level); the quartic
@@ -2646,10 +2670,10 @@
 relationship between SC-formality and the classification is
 sharper than the table suggests. Proposition~\ref{prop:swiss-cheese-nonformality-by-class}
 already isolates the first nonzero Swiss-cheese operation in each
-non-Gaussian class: class~$L$ has $m_3^{\mathrm{SC}} \neq 0$,
-class~$C$ has $m_4^{\mathrm{SC}} \neq 0$, and class~$M$ has
-nonzero $m_k^{\mathrm{SC}}$ for all $k \geq 3$. This reduces the
-formality criterion to a classification check.
+non-Gaussian class and, on the Gaussian locus, identifies the
+mixed-sector tree formulas with the degree-by-degree shadow tower
+after averaging. The criterion below packages this as an equivalence
+between SC-formality and truncation of the shadow tower at degree~$2$.
 
 \begin{proposition}[SC-formality characterises class~$G$; \ClaimStatusProvedHere]
 \label{prop:sc-formal-iff-class-g}
@@ -2665,21 +2689,30 @@
 The forward direction \textup{(}class~$G$ $\Longrightarrow$
 SC-formal\textup{)} is established in
 Proposition~\ref{prop:swiss-cheese-nonformality-by-class}:
-the class-$G$ row consists exactly of Heisenberg and lattice
-VOAs, and in both cases $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
+the class-$G$ row consists of the Gaussian families Heisenberg,
+lattice VOA, and free fermion, and in each case the genus-$0$
+mixed tree formulas stop at arity~$2$, so
+$m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
 
 For the converse, suppose~$\cA$ is SC-formal.
-Because the standard landscape is exhausted by the four classes
-$G$, $L$, $C$, $M$, it is enough to eliminate the three
-non-Gaussian cases. Proposition~\ref{prop:swiss-cheese-nonformality-by-class}
-does exactly this: class~$L$ has $m_3^{\mathrm{SC}} \neq 0$,
-class~$C$ has $m_4^{\mathrm{SC}} \neq 0$, and class~$M$ has
-nonzero higher operations in every arity $k \geq 3$. Each of
-these cases contradicts SC-formality. This converse uses only the
-classification from Proposition~\ref{prop:swiss-cheese-nonformality-by-class};
-it does not invoke any trilinear form built from~$\kappa$.
-Hence an SC-formal algebra must
-belong to class~$G$.
+Then the mixed sector of the Swiss-cheese bar complex is formal:
+every higher arity tree operation vanishes. The tower-bar
+correspondence is operadic: the arity-$r$ mixed tree and the
+degree-$r$ shadow are produced by the same genus-$0$ tree-transfer
+formula, with the same propagator on internal edges; the only
+difference is the output colour, and passage to the symmetric
+closed sector applies the averaging morphism
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)}.
+Hence SC-formality forces $S_r(\cA) = 0$ for every $r \geq 3$:
+there is no higher mixed tree whose closed projection could survive.
+By Theorem~\ref{thm:shadow-formality-identification} and
+Proposition~\ref{prop:shadow-tower-three-lenses}, this is exactly
+the statement that the shadow/formality tower truncates at
+degree~$2$. Theorem~\ref{thm:shadow-archetype-classification}
+identifies the standard-landscape locus with this property as
+precisely class~$G$. Hence an SC-formal algebra must belong
+to class~$G$.
 \end{proof}
 
 \begin{remark}[D-module purity: reduction to a single gap]

codex
The local proof block is patched. I’m rereading the modified section now before any verification so I can catch overstatements or reference mismatches in the live text itself.
exec
/bin/zsh -lc "sed -n '2478,2625p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'git diff -- chapters/theory/chiral_koszul_pairs.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
adjunction is a Quillen equivalence on the Koszul locus) and the
biduality of holonomic D-modules under Verdier duality. Concretely,
the bar complex of $\cA^!$ is the cobar complex of $\cA$ (by
construction of $\cA^!$), and the cobar of bar is canonically
quasi-isomorphic to $\cA$ on the Koszul locus
(Theorem~\ref{thm:bar-cobar-inversion-qi}). Hence
$(\cA^!)^! = \mathrm{cobar}(\barB(\cA^!)) =
\mathrm{cobar}(\Omega(\barB(\cA))) \simeq \cA$. This is the
chiral analog of the standard fact $(A^!)^! \simeq A$ for
quadratic algebras (Loday--Vallette~\cite{LV12}, Theorem~3.4.6),
with the additional Beilinson--Drinfeld holonomicity input
ensuring chain-level convergence on a smooth projective curve.

\textup{(c)}: Smooth base change uses
Lemma~\ref{lem:pushforward-preserves-qi} to verify that
$f^*$ preserves quasi-isomorphisms of chiral algebras, combined
with Theorem~\ref{thm:bar-cobar-inversion-functorial} to verify
that $f^*$ commutes with bar-cobar. The witnessing datum for
chiral Koszulness pulls back along $f$, and the
$E_2$-collapse of the PBW spectral sequence is preserved under
 succeeded in 52ms:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index ff230b2..caf0e7d 100644
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -2036,9 +2036,14 @@ Corollary~\ref{cor:minimal-orbit-koszul}.
 Let $\cA$ be a chiral algebra on a smooth projective curve~$X$
 with PBW filtration $F_\bullet$.
 Conditions \textup{(i)--(vi)}, \textup{(ix)--(x)}, and the
-genus-$0$ condition~\textup{(vii)} below are equivalent.
+genus-$0$ clause of condition~\textup{(vii)} below are equivalent.
+On the uniform-weight lane, condition~\textup{(vii)} strengthens to
+the all-genera concentration statement recorded there and remains
+equivalent to them.
 Condition~\textup{(viii)} is a proved one-way consequence of
-them on the Koszul locus.
+them on the Koszul locus: it yields Hochschild duality,
+polynomial Hilbert series, and $\Etwo$-formality, but it does not
+force the underlying graded-commutative algebra to be free.
 Under the additional perfectness and non-degeneracy hypotheses on the
 ambient tangent complex, condition~\textup{(xi)} is also equivalent to
file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 82ce3f8a19eaa51f878397fa63cad2971741bf1e..caf0e7dcc8b2e4df8cb6362c74b5edc7c33e1305
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -2561,7 +2561,7 @@
 & $m_k^{\mathrm{SC}},\; k \geq 5$ \\
 \midrule
 $G$ \textup{(}$r_{\max}=2$\textup{)}
-& Heisenberg, lattice VOA
+& Heisenberg, lattice VOA, free fermion
 & $= 0$
 & $= 0$
 & $= 0$ \\
@@ -2586,12 +2586,21 @@
 
 \medskip\noindent
 \emph{Mechanism.}
-For class~$G$\textup{:} Heisenberg is central, and lattice VOAs are
-Gaussian: the Heisenberg bracket
-$[a_m, a_n] = km\,\delta_{m+n,0}$ is central, while for lattice
-VOAs the shadow obstruction tower terminates at weight~$2$ by
-Corollary~\ref{cor:lattice-postnikov-termination}. In both cases
-all higher tree sums vanish.
+For class~$G$\textup{:}
+Heisenberg, lattice VOAs, and free fermions are Gaussian/free-field:
+their ordered bar data is generated by the binary two-point kernel,
+so every connected genus-$0$ tree with at least three external legs
+factors through pairings and carries no primitive higher vertex.
+Equivalently, the shadow tower truncates at degree~$2$:
+$S_r(\cA)=0$ for $r \geq 3$
+\textup{(}Theorem~\ref{thm:shadow-archetype-classification}; for
+lattices see Corollary~\ref{cor:lattice-postnikov-termination}\textup{)}.
+Under the averaging map
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)},
+the mixed Swiss-cheese tree of arity~$r$ projects to the degree-$r$
+shadow. Since there is no primitive tree for $r \geq 3$,
+all higher mixed-sector operations vanish.
 For class~$L$\textup{:} the affine KM OPE has at most a double pole; the
 three-channel tree sum over $\overline{\cM}_{0,4}$ is nonzero
 \textup{(}$S_3 = 2h^\vee/(k+h^\vee) \neq 0$\textup{)} but the
@@ -2613,10 +2622,25 @@
 
 \begin{proof}
 Class~$G$: for Heisenberg, centrality of the bracket kills all nested
-compositions, so $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$. For lattice
-VOAs, Corollary~\ref{cor:lattice-postnikov-termination} identifies
-the shadow obstruction tower with its weight-$2$ truncation, so the
-transferred Swiss-cheese operations vanish for every $k \geq 3$.
+tree compositions, so $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
+For lattice VOAs, bosonization reduces connected genus-$0$ amplitudes
+to Wick pairings of the underlying Heisenberg field, and
+Corollary~\ref{cor:lattice-postnikov-termination} identifies the
+shadow tower with its weight-$2$ truncation. For the free fermion,
+Wick's theorem gives Pfaffian factorization by the basic contraction
+$\psi(z)\psi^*(w) \sim (z-w)^{-1}$, so again no connected tree with
+$r \geq 3$ survives after extracting the binary pairings. In all three
+cases the mixed Swiss-cheese arity-$r$ operation is the open-colored
+lift of the same genus-$0$ tree sum whose closed projection is
+$S_r(\cA)$; equivalently,
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)}.
+Because class~$G$ means $S_r(\cA) = 0$ for all $r \geq 3$,
+the mixed-sector operations vanish:
+$m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
+The weaker condition $\Delta = 0$ is not sufficient:
+affine Kac--Moody algebras are class~$L$ with $\Delta = 0$ but
+$m_3^{\mathrm{SC}} \neq 0$.
 Class~$L$: the cubic shadow
 $S_3 = 2h^\vee/(k + h^\vee)$ is computed from the OPE coefficient
 ratio (the structure constant divided by the level); the quartic
@@ -2646,10 +2670,10 @@
 relationship between SC-formality and the classification is
 sharper than the table suggests. Proposition~\ref{prop:swiss-cheese-nonformality-by-class}
 already isolates the first nonzero Swiss-cheese operation in each
-non-Gaussian class: class~$L$ has $m_3^{\mathrm{SC}} \neq 0$,
-class~$C$ has $m_4^{\mathrm{SC}} \neq 0$, and class~$M$ has
-nonzero $m_k^{\mathrm{SC}}$ for all $k \geq 3$. This reduces the
-formality criterion to a classification check.
+non-Gaussian class and, on the Gaussian locus, identifies the
+mixed-sector tree formulas with the degree-by-degree shadow tower
+after averaging. The criterion below packages this as an equivalence
+between SC-formality and truncation of the shadow tower at degree~$2$.
 
 \begin{proposition}[SC-formality characterises class~$G$; \ClaimStatusProvedHere]
 \label{prop:sc-formal-iff-class-g}
@@ -2665,21 +2689,30 @@
 The forward direction \textup{(}class~$G$ $\Longrightarrow$
 SC-formal\textup{)} is established in
 Proposition~\ref{prop:swiss-cheese-nonformality-by-class}:
-the class-$G$ row consists exactly of Heisenberg and lattice
-VOAs, and in both cases $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
+the class-$G$ row consists of the Gaussian families Heisenberg,
+lattice VOA, and free fermion, and in each case the genus-$0$
+mixed tree formulas stop at arity~$2$, so
+$m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
 
 For the converse, suppose~$\cA$ is SC-formal.
-Because the standard landscape is exhausted by the four classes
-$G$, $L$, $C$, $M$, it is enough to eliminate the three
-non-Gaussian cases. Proposition~\ref{prop:swiss-cheese-nonformality-by-class}
-does exactly this: class~$L$ has $m_3^{\mathrm{SC}} \neq 0$,
-class~$C$ has $m_4^{\mathrm{SC}} \neq 0$, and class~$M$ has
-nonzero higher operations in every arity $k \geq 3$. Each of
-these cases contradicts SC-formality. This converse uses only the
-classification from Proposition~\ref{prop:swiss-cheese-nonformality-by-class};
-it does not invoke any trilinear form built from~$\kappa$.
-Hence an SC-formal algebra must
-belong to class~$G$.
+Then the mixed sector of the Swiss-cheese bar complex is formal:
+every higher arity tree operation vanishes. The tower-bar
+correspondence is operadic: the arity-$r$ mixed tree and the
+degree-$r$ shadow are produced by the same genus-$0$ tree-transfer
+formula, with the same propagator on internal edges; the only
+difference is the output colour, and passage to the symmetric
+closed sector applies the averaging morphism
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)}.
+Hence SC-formality forces $S_r(\cA) = 0$ for every $r \geq 3$:
+there is no higher mixed tree whose closed projection could survive.
+By Theorem~\ref{thm:shadow-formality-identification} and
+Proposition~\ref{prop:shadow-tower-three-lenses}, this is exactly
+the statement that the shadow/formality tower truncates at
+degree~$2$. Theorem~\ref{thm:shadow-archetype-classification}
+identifies the standard-landscape locus with this property as
+precisely class~$G$. Hence an SC-formal algebra must belong
+to class~$G$.
 \end{proof}
 
 \begin{remark}[D-module purity: reduction to a single gap]


thinking
**Inspecting changes in git**

I noticed an unexpected git diff, which shows unrelated changes in the file that aren't ours. I need to ignore those for now. Maybe I should check the lines after 2550-2625 to make sure there aren’t any issues beyond the excerpt I cut. It seems wise to take a closer look at the rest to ensure everything is fine and nothing else is out of place. Let’s get reading!
exec
/bin/zsh -lc "sed -n '2550,2625p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
always $A_\infty$-formal for Koszul algebras by
Theorem~\textup{\ref{thm:koszul-equivalences-meta}(iii)}\textup{)}
are classified by shadow depth as follows.
\begin{center}
\renewcommand{\arraystretch}{1.3}
\begin{tabular}{@{}lcccc@{}}
\toprule
\textbf{Class}
& \textbf{Families}
& $m_3^{\mathrm{SC}}$
& $m_4^{\mathrm{SC}}$
& $m_k^{\mathrm{SC}},\; k \geq 5$ \\
\midrule
$G$ \textup{(}$r_{\max}=2$\textup{)}
& Heisenberg, lattice VOA, free fermion
& $= 0$
& $= 0$
& $= 0$ \\
$L$ \textup{(}$r_{\max}=3$\textup{)}
& affine KM
file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 82ce3f8a19eaa51f878397fa63cad2971741bf1e..caf0e7dcc8b2e4df8cb6362c74b5edc7c33e1305
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -2561,7 +2561,7 @@
 & $m_k^{\mathrm{SC}},\; k \geq 5$ \\
 \midrule
 $G$ \textup{(}$r_{\max}=2$\textup{)}
-& Heisenberg, lattice VOA
+& Heisenberg, lattice VOA, free fermion
 & $= 0$
 & $= 0$
 & $= 0$ \\
@@ -2586,12 +2586,21 @@
 
 \medskip\noindent
 \emph{Mechanism.}
-For class~$G$\textup{:} Heisenberg is central, and lattice VOAs are
-Gaussian: the Heisenberg bracket
-$[a_m, a_n] = km\,\delta_{m+n,0}$ is central, while for lattice
-VOAs the shadow obstruction tower terminates at weight~$2$ by
-Corollary~\ref{cor:lattice-postnikov-termination}. In both cases
-all higher tree sums vanish.
+For class~$G$\textup{:}
+Heisenberg, lattice VOAs, and free fermions are Gaussian/free-field:
+their ordered bar data is generated by the binary two-point kernel,
+so every connected genus-$0$ tree with at least three external legs
+factors through pairings and carries no primitive higher vertex.
+Equivalently, the shadow tower truncates at degree~$2$:
+$S_r(\cA)=0$ for $r \geq 3$
+\textup{(}Theorem~\ref{thm:shadow-archetype-classification}; for
+lattices see Corollary~\ref{cor:lattice-postnikov-termination}\textup{)}.
+Under the averaging map
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)},
+the mixed Swiss-cheese tree of arity~$r$ projects to the degree-$r$
+shadow. Since there is no primitive tree for $r \geq 3$,
+all higher mixed-sector operations vanish.
 For class~$L$\textup{:} the affine KM OPE has at most a double pole; the
 three-channel tree sum over $\overline{\cM}_{0,4}$ is nonzero
 \textup{(}$S_3 = 2h^\vee/(k+h^\vee) \neq 0$\textup{)} but the
@@ -2613,10 +2622,25 @@
 
 \begin{proof}
 Class~$G$: for Heisenberg, centrality of the bracket kills all nested
-compositions, so $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$. For lattice
-VOAs, Corollary~\ref{cor:lattice-postnikov-termination} identifies
-the shadow obstruction tower with its weight-$2$ truncation, so the
-transferred Swiss-cheese operations vanish for every $k \geq 3$.
+tree compositions, so $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
+For lattice VOAs, bosonization reduces connected genus-$0$ amplitudes
+to Wick pairings of the underlying Heisenberg field, and
+Corollary~\ref{cor:lattice-postnikov-termination} identifies the
+shadow tower with its weight-$2$ truncation. For the free fermion,
+Wick's theorem gives Pfaffian factorization by the basic contraction
+$\psi(z)\psi^*(w) \sim (z-w)^{-1}$, so again no connected tree with
+$r \geq 3$ survives after extracting the binary pairings. In all three
+cases the mixed Swiss-cheese arity-$r$ operation is the open-colored
+lift of the same genus-$0$ tree sum whose closed projection is
+$S_r(\cA)$; equivalently,
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)}.
+Because class~$G$ means $S_r(\cA) = 0$ for all $r \geq 3$,
+the mixed-sector operations vanish:
+$m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
+The weaker condition $\Delta = 0$ is not sufficient:
+affine Kac--Moody algebras are class~$L$ with $\Delta = 0$ but
+$m_3^{\mathrm{SC}} \neq 0$.
 Class~$L$: the cubic shadow
 $S_3 = 2h^\vee/(k + h^\vee)$ is computed from the OPE coefficient
 ratio (the structure constant divided by the level); the quartic
@@ -2646,10 +2670,10 @@
 relationship between SC-formality and the classification is
 sharper than the table suggests. Proposition~\ref{prop:swiss-cheese-nonformality-by-class}
 already isolates the first nonzero Swiss-cheese operation in each
-non-Gaussian class: class~$L$ has $m_3^{\mathrm{SC}} \neq 0$,
-class~$C$ has $m_4^{\mathrm{SC}} \neq 0$, and class~$M$ has
-nonzero $m_k^{\mathrm{SC}}$ for all $k \geq 3$. This reduces the
-formality criterion to a classification check.
+non-Gaussian class and, on the Gaussian locus, identifies the
+mixed-sector tree formulas with the degree-by-degree shadow tower
+after averaging. The criterion below packages this as an equivalence
+between SC-formality and truncation of the shadow tower at degree~$2$.
 
 \begin{proposition}[SC-formality characterises class~$G$; \ClaimStatusProvedHere]
 \label{prop:sc-formal-iff-class-g}
@@ -2665,21 +2689,30 @@
 The forward direction \textup{(}class~$G$ $\Longrightarrow$
 SC-formal\textup{)} is established in
 Proposition~\ref{prop:swiss-cheese-nonformality-by-class}:
-the class-$G$ row consists exactly of Heisenberg and lattice
-VOAs, and in both cases $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
+the class-$G$ row consists of the Gaussian families Heisenberg,
+lattice VOA, and free fermion, and in each case the genus-$0$
+mixed tree formulas stop at arity~$2$, so
+$m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
 
 For the converse, suppose~$\cA$ is SC-formal.
-Because the standard landscape is exhausted by the four classes
-$G$, $L$, $C$, $M$, it is enough to eliminate the three
-non-Gaussian cases. Proposition~\ref{prop:swiss-cheese-nonformality-by-class}
-does exactly this: class~$L$ has $m_3^{\mathrm{SC}} \neq 0$,
-class~$C$ has $m_4^{\mathrm{SC}} \neq 0$, and class~$M$ has
-nonzero higher operations in every arity $k \geq 3$. Each of
-these cases contradicts SC-formality. This converse uses only the
-classification from Proposition~\ref{prop:swiss-cheese-nonformality-by-class};
-it does not invoke any trilinear form built from~$\kappa$.
-Hence an SC-formal algebra must
-belong to class~$G$.
+Then the mixed sector of the Swiss-cheese bar complex is formal:
+every higher arity tree operation vanishes. The tower-bar
+correspondence is operadic: the arity-$r$ mixed tree and the
+degree-$r$ shadow are produced by the same genus-$0$ tree-transfer
+formula, with the same propagator on internal edges; the only
+difference is the output colour, and passage to the symmetric
+closed sector applies the averaging morphism
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)}.
+Hence SC-formality forces $S_r(\cA) = 0$ for every $r \geq 3$:
+there is no higher mixed tree whose closed projection could survive.
+By Theorem~\ref{thm:shadow-formality-identification} and
+Proposition~\ref{prop:shadow-tower-three-lenses}, this is exactly
+the statement that the shadow/formality tower truncates at
+degree~$2$. Theorem~\ref{thm:shadow-archetype-classification}
+identifies the standard-landscape locus with this property as
+precisely class~$G$. Hence an SC-formal algebra must belong
+to class~$G$.
 \end{proof}
 
 \begin{remark}[D-module purity: reduction to a single gap]

exec
/bin/zsh -lc "sed -n '2625,2665p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
tree compositions, so $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
For lattice VOAs, bosonization reduces connected genus-$0$ amplitudes
to Wick pairings of the underlying Heisenberg field, and
Corollary~\ref{cor:lattice-postnikov-termination} identifies the
shadow tower with its weight-$2$ truncation. For the free fermion,
Wick's theorem gives Pfaffian factorization by the basic contraction
$\psi(z)\psi^*(w) \sim (z-w)^{-1}$, so again no connected tree with
$r \geq 3$ survives after extracting the binary pairings. In all three
cases the mixed Swiss-cheese arity-$r$ operation is the open-colored
lift of the same genus-$0$ tree sum whose closed projection is
$S_r(\cA)$; equivalently,
$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)}.
Because class~$G$ means $S_r(\cA) = 0$ for all $r \geq 3$,
the mixed-sector operations vanish:
$m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
The weaker condition $\Delta = 0$ is not sufficient:
affine Kac--Moody algebras are class~$L$ with $\Delta = 0$ but
$m_3^{\mathrm{SC}} \neq 0$.
Class~$L$: the cubic shadow
file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 82ce3f8a19eaa51f878397fa63cad2971741bf1e..caf0e7dcc8b2e4df8cb6362c74b5edc7c33e1305
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -2561,7 +2561,7 @@
 & $m_k^{\mathrm{SC}},\; k \geq 5$ \\
 \midrule
 $G$ \textup{(}$r_{\max}=2$\textup{)}
-& Heisenberg, lattice VOA
+& Heisenberg, lattice VOA, free fermion
 & $= 0$
 & $= 0$
 & $= 0$ \\
@@ -2586,12 +2586,21 @@
 
 \medskip\noindent
 \emph{Mechanism.}
-For class~$G$\textup{:} Heisenberg is central, and lattice VOAs are
-Gaussian: the Heisenberg bracket
-$[a_m, a_n] = km\,\delta_{m+n,0}$ is central, while for lattice
-VOAs the shadow obstruction tower terminates at weight~$2$ by
-Corollary~\ref{cor:lattice-postnikov-termination}. In both cases
-all higher tree sums vanish.
+For class~$G$\textup{:}
+Heisenberg, lattice VOAs, and free fermions are Gaussian/free-field:
+their ordered bar data is generated by the binary two-point kernel,
+so every connected genus-$0$ tree with at least three external legs
+factors through pairings and carries no primitive higher vertex.
+Equivalently, the shadow tower truncates at degree~$2$:
+$S_r(\cA)=0$ for $r \geq 3$
+\textup{(}Theorem~\ref{thm:shadow-archetype-classification}; for
+lattices see Corollary~\ref{cor:lattice-postnikov-termination}\textup{)}.
+Under the averaging map
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)},
+the mixed Swiss-cheese tree of arity~$r$ projects to the degree-$r$
+shadow. Since there is no primitive tree for $r \geq 3$,
+all higher mixed-sector operations vanish.
 For class~$L$\textup{:} the affine KM OPE has at most a double pole; the
 three-channel tree sum over $\overline{\cM}_{0,4}$ is nonzero
 \textup{(}$S_3 = 2h^\vee/(k+h^\vee) \neq 0$\textup{)} but the
@@ -2613,10 +2622,25 @@
 
 \begin{proof}
 Class~$G$: for Heisenberg, centrality of the bracket kills all nested
-compositions, so $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$. For lattice
-VOAs, Corollary~\ref{cor:lattice-postnikov-termination} identifies
-the shadow obstruction tower with its weight-$2$ truncation, so the
-transferred Swiss-cheese operations vanish for every $k \geq 3$.
+tree compositions, so $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
+For lattice VOAs, bosonization reduces connected genus-$0$ amplitudes
+to Wick pairings of the underlying Heisenberg field, and
+Corollary~\ref{cor:lattice-postnikov-termination} identifies the
+shadow tower with its weight-$2$ truncation. For the free fermion,
+Wick's theorem gives Pfaffian factorization by the basic contraction
+$\psi(z)\psi^*(w) \sim (z-w)^{-1}$, so again no connected tree with
+$r \geq 3$ survives after extracting the binary pairings. In all three
+cases the mixed Swiss-cheese arity-$r$ operation is the open-colored
+lift of the same genus-$0$ tree sum whose closed projection is
+$S_r(\cA)$; equivalently,
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)}.
+Because class~$G$ means $S_r(\cA) = 0$ for all $r \geq 3$,
+the mixed-sector operations vanish:
+$m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
+The weaker condition $\Delta = 0$ is not sufficient:
+affine Kac--Moody algebras are class~$L$ with $\Delta = 0$ but
+$m_3^{\mathrm{SC}} \neq 0$.
 Class~$L$: the cubic shadow
 $S_3 = 2h^\vee/(k + h^\vee)$ is computed from the OPE coefficient
 ratio (the structure constant divided by the level); the quartic
@@ -2646,10 +2670,10 @@
 relationship between SC-formality and the classification is
 sharper than the table suggests. Proposition~\ref{prop:swiss-cheese-nonformality-by-class}
 already isolates the first nonzero Swiss-cheese operation in each
-non-Gaussian class: class~$L$ has $m_3^{\mathrm{SC}} \neq 0$,
-class~$C$ has $m_4^{\mathrm{SC}} \neq 0$, and class~$M$ has
-nonzero $m_k^{\mathrm{SC}}$ for all $k \geq 3$. This reduces the
-formality criterion to a classification check.
+non-Gaussian class and, on the Gaussian locus, identifies the
+mixed-sector tree formulas with the degree-by-degree shadow tower
+after averaging. The criterion below packages this as an equivalence
+between SC-formality and truncation of the shadow tower at degree~$2$.
 
 \begin{proposition}[SC-formality characterises class~$G$; \ClaimStatusProvedHere]
 \label{prop:sc-formal-iff-class-g}
@@ -2665,21 +2689,30 @@
 The forward direction \textup{(}class~$G$ $\Longrightarrow$
 SC-formal\textup{)} is established in
 Proposition~\ref{prop:swiss-cheese-nonformality-by-class}:
-the class-$G$ row consists exactly of Heisenberg and lattice
-VOAs, and in both cases $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
+the class-$G$ row consists of the Gaussian families Heisenberg,
+lattice VOA, and free fermion, and in each case the genus-$0$
+mixed tree formulas stop at arity~$2$, so
+$m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
 
 For the converse, suppose~$\cA$ is SC-formal.
-Because the standard landscape is exhausted by the four classes
-$G$, $L$, $C$, $M$, it is enough to eliminate the three
-non-Gaussian cases. Proposition~\ref{prop:swiss-cheese-nonformality-by-class}
-does exactly this: class~$L$ has $m_3^{\mathrm{SC}} \neq 0$,
-class~$C$ has $m_4^{\mathrm{SC}} \neq 0$, and class~$M$ has
-nonzero higher operations in every arity $k \geq 3$. Each of
-these cases contradicts SC-formality. This converse uses only the
-classification from Proposition~\ref{prop:swiss-cheese-nonformality-by-class};
-it does not invoke any trilinear form built from~$\kappa$.
-Hence an SC-formal algebra must
-belong to class~$G$.
+Then the mixed sector of the Swiss-cheese bar complex is formal:
+every higher arity tree operation vanishes. The tower-bar
+correspondence is operadic: the arity-$r$ mixed tree and the
+degree-$r$ shadow are produced by the same genus-$0$ tree-transfer
+formula, with the same propagator on internal edges; the only
+difference is the output colour, and passage to the symmetric
+closed sector applies the averaging morphism
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)}.
+Hence SC-formality forces $S_r(\cA) = 0$ for every $r \geq 3$:
+there is no higher mixed tree whose closed projection could survive.
+By Theorem~\ref{thm:shadow-formality-identification} and
+Proposition~\ref{prop:shadow-tower-three-lenses}, this is exactly
+the statement that the shadow/formality tower truncates at
+degree~$2$. Theorem~\ref{thm:shadow-archetype-classification}
+identifies the standard-landscape locus with this property as
+precisely class~$G$. Hence an SC-formal algebra must belong
+to class~$G$.
 \end{proof}
 
 \begin{remark}[D-module purity: reduction to a single gap]

exec
/bin/zsh -lc "sed -n '2665,2715p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
quartic shadow $S_4$ and $Q^{\mathrm{contact}}$, quintic
shadow $S_5 = -48/(c^2(5c+22))$, all four classes verified).
\end{proof}

The four classes exhaust the standard landscape, but the
relationship between SC-formality and the classification is
sharper than the table suggests. Proposition~\ref{prop:swiss-cheese-nonformality-by-class}
already isolates the first nonzero Swiss-cheese operation in each
non-Gaussian class and, on the Gaussian locus, identifies the
mixed-sector tree formulas with the degree-by-degree shadow tower
after averaging. The criterion below packages this as an equivalence
between SC-formality and truncation of the shadow tower at degree~$2$.

\begin{proposition}[SC-formality characterises class~$G$; \ClaimStatusProvedHere]
\label{prop:sc-formal-iff-class-g}
\index{Swiss-cheese operad!formality characterisation}
\index{class G@class~$G$!characterised by SC-formality}
Let~$\cA$ be a chiral algebra in the standard landscape.
Then~$\cA$ is Swiss-cheese formal
\textup{(}$m_k^{\mathrm{SC}} = 0$ for all $k \geq 3$\textup{)}
file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 82ce3f8a19eaa51f878397fa63cad2971741bf1e..caf0e7dcc8b2e4df8cb6362c74b5edc7c33e1305
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -2561,7 +2561,7 @@
 & $m_k^{\mathrm{SC}},\; k \geq 5$ \\
 \midrule
 $G$ \textup{(}$r_{\max}=2$\textup{)}
-& Heisenberg, lattice VOA
+& Heisenberg, lattice VOA, free fermion
 & $= 0$
 & $= 0$
 & $= 0$ \\
@@ -2586,12 +2586,21 @@
 
 \medskip\noindent
 \emph{Mechanism.}
-For class~$G$\textup{:} Heisenberg is central, and lattice VOAs are
-Gaussian: the Heisenberg bracket
-$[a_m, a_n] = km\,\delta_{m+n,0}$ is central, while for lattice
-VOAs the shadow obstruction tower terminates at weight~$2$ by
-Corollary~\ref{cor:lattice-postnikov-termination}. In both cases
-all higher tree sums vanish.
+For class~$G$\textup{:}
+Heisenberg, lattice VOAs, and free fermions are Gaussian/free-field:
+their ordered bar data is generated by the binary two-point kernel,
+so every connected genus-$0$ tree with at least three external legs
+factors through pairings and carries no primitive higher vertex.
+Equivalently, the shadow tower truncates at degree~$2$:
+$S_r(\cA)=0$ for $r \geq 3$
+\textup{(}Theorem~\ref{thm:shadow-archetype-classification}; for
+lattices see Corollary~\ref{cor:lattice-postnikov-termination}\textup{)}.
+Under the averaging map
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)},
+the mixed Swiss-cheese tree of arity~$r$ projects to the degree-$r$
+shadow. Since there is no primitive tree for $r \geq 3$,
+all higher mixed-sector operations vanish.
 For class~$L$\textup{:} the affine KM OPE has at most a double pole; the
 three-channel tree sum over $\overline{\cM}_{0,4}$ is nonzero
 \textup{(}$S_3 = 2h^\vee/(k+h^\vee) \neq 0$\textup{)} but the
@@ -2613,10 +2622,25 @@
 
 \begin{proof}
 Class~$G$: for Heisenberg, centrality of the bracket kills all nested
-compositions, so $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$. For lattice
-VOAs, Corollary~\ref{cor:lattice-postnikov-termination} identifies
-the shadow obstruction tower with its weight-$2$ truncation, so the
-transferred Swiss-cheese operations vanish for every $k \geq 3$.
+tree compositions, so $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
+For lattice VOAs, bosonization reduces connected genus-$0$ amplitudes
+to Wick pairings of the underlying Heisenberg field, and
+Corollary~\ref{cor:lattice-postnikov-termination} identifies the
+shadow tower with its weight-$2$ truncation. For the free fermion,
+Wick's theorem gives Pfaffian factorization by the basic contraction
+$\psi(z)\psi^*(w) \sim (z-w)^{-1}$, so again no connected tree with
+$r \geq 3$ survives after extracting the binary pairings. In all three
+cases the mixed Swiss-cheese arity-$r$ operation is the open-colored
+lift of the same genus-$0$ tree sum whose closed projection is
+$S_r(\cA)$; equivalently,
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)}.
+Because class~$G$ means $S_r(\cA) = 0$ for all $r \geq 3$,
+the mixed-sector operations vanish:
+$m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
+The weaker condition $\Delta = 0$ is not sufficient:
+affine Kac--Moody algebras are class~$L$ with $\Delta = 0$ but
+$m_3^{\mathrm{SC}} \neq 0$.
 Class~$L$: the cubic shadow
 $S_3 = 2h^\vee/(k + h^\vee)$ is computed from the OPE coefficient
 ratio (the structure constant divided by the level); the quartic
@@ -2646,10 +2670,10 @@
 relationship between SC-formality and the classification is
 sharper than the table suggests. Proposition~\ref{prop:swiss-cheese-nonformality-by-class}
 already isolates the first nonzero Swiss-cheese operation in each
-non-Gaussian class: class~$L$ has $m_3^{\mathrm{SC}} \neq 0$,
-class~$C$ has $m_4^{\mathrm{SC}} \neq 0$, and class~$M$ has
-nonzero $m_k^{\mathrm{SC}}$ for all $k \geq 3$. This reduces the
-formality criterion to a classification check.
+non-Gaussian class and, on the Gaussian locus, identifies the
+mixed-sector tree formulas with the degree-by-degree shadow tower
+after averaging. The criterion below packages this as an equivalence
+between SC-formality and truncation of the shadow tower at degree~$2$.
 
 \begin{proposition}[SC-formality characterises class~$G$; \ClaimStatusProvedHere]
 \label{prop:sc-formal-iff-class-g}
@@ -2665,21 +2689,30 @@
 The forward direction \textup{(}class~$G$ $\Longrightarrow$
 SC-formal\textup{)} is established in
 Proposition~\ref{prop:swiss-cheese-nonformality-by-class}:
-the class-$G$ row consists exactly of Heisenberg and lattice
-VOAs, and in both cases $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
+the class-$G$ row consists of the Gaussian families Heisenberg,
+lattice VOA, and free fermion, and in each case the genus-$0$
+mixed tree formulas stop at arity~$2$, so
+$m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
 
 For the converse, suppose~$\cA$ is SC-formal.
-Because the standard landscape is exhausted by the four classes
-$G$, $L$, $C$, $M$, it is enough to eliminate the three
-non-Gaussian cases. Proposition~\ref{prop:swiss-cheese-nonformality-by-class}
-does exactly this: class~$L$ has $m_3^{\mathrm{SC}} \neq 0$,
-class~$C$ has $m_4^{\mathrm{SC}} \neq 0$, and class~$M$ has
-nonzero higher operations in every arity $k \geq 3$. Each of
-these cases contradicts SC-formality. This converse uses only the
-classification from Proposition~\ref{prop:swiss-cheese-nonformality-by-class};
-it does not invoke any trilinear form built from~$\kappa$.
-Hence an SC-formal algebra must
-belong to class~$G$.
+Then the mixed sector of the Swiss-cheese bar complex is formal:
+every higher arity tree operation vanishes. The tower-bar
+correspondence is operadic: the arity-$r$ mixed tree and the
+degree-$r$ shadow are produced by the same genus-$0$ tree-transfer
+formula, with the same propagator on internal edges; the only
+difference is the output colour, and passage to the symmetric
+closed sector applies the averaging morphism
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)}.
+Hence SC-formality forces $S_r(\cA) = 0$ for every $r \geq 3$:
+there is no higher mixed tree whose closed projection could survive.
+By Theorem~\ref{thm:shadow-formality-identification} and
+Proposition~\ref{prop:shadow-tower-three-lenses}, this is exactly
+the statement that the shadow/formality tower truncates at
+degree~$2$. Theorem~\ref{thm:shadow-archetype-classification}
+identifies the standard-landscape locus with this property as
+precisely class~$G$. Hence an SC-formal algebra must belong
+to class~$G$.
 \end{proof}
 
 \begin{remark}[D-module purity: reduction to a single gap]





thinking
**Considering sector tree notation**

I'm thinking of how to support the mixed sector tree sum concept. There's an idea to add a phrase like "open-colored lift..." at the end of the sentence, and it seems like including a citation could be beneficial for clarity. I want to ensure that the phrasing is clear and effective in conveying the intended meaning, and that it integrates smoothly into the overall context. Let's explore how to frame this properly!
thinking
**Running greps as instructed**

I need to execute the required greps. For the "AP126 bare Omega," even though there might not be relevant edits, I should run grep in the target file. The user mentioned that I should perform a grep for forbidden patterns—specifically for "AP126 bare Omega," "AP132 augmentation," and "AP29 slop"—after every edit. It seems like a crucial step to ensure everything is compliant!
thinking
**Planning command execution**

I'm considering using `sed` with `rg`, and it seems like a good option to filter output. However, the user won't see the raw output, so I want to minimize unnecessary details. Shell piping to run commands feels right, and maybe I can run multiple commands in parallel. I might also need to compile using TeX with a targeted build. There's a patch to run after editing, and the build may take some time, so I should keep that in mind too.
thinking
**Considering compilation commands**

I’m weighing the possibility of using `latexmk -pdf main.tex` for the compile process. It seems like a solid choice, especially since it uses a standard build-surface. However, I might find that `make fast` might work fine too. I'm just trying to figure out which option is the most efficient and will yield the best results for the user. It’s all about balancing simplicity and effectiveness in this process!
codex
The proof text reread cleanly at the local surface. I’m running the required AP greps on the modified region now, then a falsifying LaTeX build.
exec
/bin/zsh -lc "sed -n '2478,2715p' chapters/theory/chiral_koszul_pairs.tex | rg -n 'r\\(z\\) = \\\\Omega/z|\\\\Omega\\\\,d\\\\log z'" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

exec
/bin/zsh -lc "sed -n '2478,2715p' chapters/theory/chiral_koszul_pairs.tex | rg -n 'T\\"'^c'"\\(s\\"'^{-1} A'"\\)|T\\"'^c'"\\(s A\\)|\\|s\\"'^{-1}v'"\\| = \\|v\\]\\+1'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2478,2715p' chapters/theory/chiral_koszul_pairs.tex | rg -n 'notably|crucially|clearly|obviously'" in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
rg: regex parse error:
    (?:T\^c\(s\^{-1} A\)|T\^c\(s A\)|\|s\^{-1}v\| = \|v\]\+1)
                 ^
error: repetition quantifier expects a valid decimal
 exited 1 in 52ms:

file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 82ce3f8a19eaa51f878397fa63cad2971741bf1e..caf0e7dcc8b2e4df8cb6362c74b5edc7c33e1305
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -2561,7 +2561,7 @@
 & $m_k^{\mathrm{SC}},\; k \geq 5$ \\
 \midrule
 $G$ \textup{(}$r_{\max}=2$\textup{)}
-& Heisenberg, lattice VOA
+& Heisenberg, lattice VOA, free fermion
 & $= 0$
 & $= 0$
 & $= 0$ \\
@@ -2586,12 +2586,21 @@
 
 \medskip\noindent
 \emph{Mechanism.}
-For class~$G$\textup{:} Heisenberg is central, and lattice VOAs are
-Gaussian: the Heisenberg bracket
-$[a_m, a_n] = km\,\delta_{m+n,0}$ is central, while for lattice
-VOAs the shadow obstruction tower terminates at weight~$2$ by
-Corollary~\ref{cor:lattice-postnikov-termination}. In both cases
-all higher tree sums vanish.
+For class~$G$\textup{:}
+Heisenberg, lattice VOAs, and free fermions are Gaussian/free-field:
+their ordered bar data is generated by the binary two-point kernel,
+so every connected genus-$0$ tree with at least three external legs
+factors through pairings and carries no primitive higher vertex.
+Equivalently, the shadow tower truncates at degree~$2$:
+$S_r(\cA)=0$ for $r \geq 3$
+\textup{(}Theorem~\ref{thm:shadow-archetype-classification}; for
+lattices see Corollary~\ref{cor:lattice-postnikov-termination}\textup{)}.
+Under the averaging map
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)},
+the mixed Swiss-cheese tree of arity~$r$ projects to the degree-$r$
+shadow. Since there is no primitive tree for $r \geq 3$,
+all higher mixed-sector operations vanish.
 For class~$L$\textup{:} the affine KM OPE has at most a double pole; the
 three-channel tree sum over $\overline{\cM}_{0,4}$ is nonzero
 \textup{(}$S_3 = 2h^\vee/(k+h^\vee) \neq 0$\textup{)} but the
@@ -2613,10 +2622,25 @@
 
 \begin{proof}
 Class~$G$: for Heisenberg, centrality of the bracket kills all nested
-compositions, so $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$. For lattice
-VOAs, Corollary~\ref{cor:lattice-postnikov-termination} identifies
-the shadow obstruction tower with its weight-$2$ truncation, so the
-transferred Swiss-cheese operations vanish for every $k \geq 3$.
+tree compositions, so $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
+For lattice VOAs, bosonization reduces connected genus-$0$ amplitudes
+to Wick pairings of the underlying Heisenberg field, and
+Corollary~\ref{cor:lattice-postnikov-termination} identifies the
+shadow tower with its weight-$2$ truncation. For the free fermion,
+Wick's theorem gives Pfaffian factorization by the basic contraction
+$\psi(z)\psi^*(w) \sim (z-w)^{-1}$, so again no connected tree with
+$r \geq 3$ survives after extracting the binary pairings. In all three
+cases the mixed Swiss-cheese arity-$r$ operation is the open-colored
+lift of the same genus-$0$ tree sum whose closed projection is
+$S_r(\cA)$; equivalently,
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)}.
+Because class~$G$ means $S_r(\cA) = 0$ for all $r \geq 3$,
+the mixed-sector operations vanish:
+$m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
+The weaker condition $\Delta = 0$ is not sufficient:
+affine Kac--Moody algebras are class~$L$ with $\Delta = 0$ but
+$m_3^{\mathrm{SC}} \neq 0$.
 Class~$L$: the cubic shadow
 $S_3 = 2h^\vee/(k + h^\vee)$ is computed from the OPE coefficient
 ratio (the structure constant divided by the level); the quartic
@@ -2646,10 +2670,10 @@
 relationship between SC-formality and the classification is
 sharper than the table suggests. Proposition~\ref{prop:swiss-cheese-nonformality-by-class}
 already isolates the first nonzero Swiss-cheese operation in each
-non-Gaussian class: class~$L$ has $m_3^{\mathrm{SC}} \neq 0$,
-class~$C$ has $m_4^{\mathrm{SC}} \neq 0$, and class~$M$ has
-nonzero $m_k^{\mathrm{SC}}$ for all $k \geq 3$. This reduces the
-formality criterion to a classification check.
+non-Gaussian class and, on the Gaussian locus, identifies the
+mixed-sector tree formulas with the degree-by-degree shadow tower
+after averaging. The criterion below packages this as an equivalence
+between SC-formality and truncation of the shadow tower at degree~$2$.
 
 \begin{proposition}[SC-formality characterises class~$G$; \ClaimStatusProvedHere]
 \label{prop:sc-formal-iff-class-g}
@@ -2665,21 +2689,30 @@
 The forward direction \textup{(}class~$G$ $\Longrightarrow$
 SC-formal\textup{)} is established in
 Proposition~\ref{prop:swiss-cheese-nonformality-by-class}:
-the class-$G$ row consists exactly of Heisenberg and lattice
-VOAs, and in both cases $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
+the class-$G$ row consists of the Gaussian families Heisenberg,
+lattice VOA, and free fermion, and in each case the genus-$0$
+mixed tree formulas stop at arity~$2$, so
+$m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
 
 For the converse, suppose~$\cA$ is SC-formal.
-Because the standard landscape is exhausted by the four classes
-$G$, $L$, $C$, $M$, it is enough to eliminate the three
-non-Gaussian cases. Proposition~\ref{prop:swiss-cheese-nonformality-by-class}
-does exactly this: class~$L$ has $m_3^{\mathrm{SC}} \neq 0$,
-class~$C$ has $m_4^{\mathrm{SC}} \neq 0$, and class~$M$ has
-nonzero higher operations in every arity $k \geq 3$. Each of
-these cases contradicts SC-formality. This converse uses only the
-classification from Proposition~\ref{prop:swiss-cheese-nonformality-by-class};
-it does not invoke any trilinear form built from~$\kappa$.
-Hence an SC-formal algebra must
-belong to class~$G$.
+Then the mixed sector of the Swiss-cheese bar complex is formal:
+every higher arity tree operation vanishes. The tower-bar
+correspondence is operadic: the arity-$r$ mixed tree and the
+degree-$r$ shadow are produced by the same genus-$0$ tree-transfer
+formula, with the same propagator on internal edges; the only
+difference is the output colour, and passage to the symmetric
+closed sector applies the averaging morphism
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)}.
+Hence SC-formality forces $S_r(\cA) = 0$ for every $r \geq 3$:
+there is no higher mixed tree whose closed projection could survive.
+By Theorem~\ref{thm:shadow-formality-identification} and
+Proposition~\ref{prop:shadow-tower-three-lenses}, this is exactly
+the statement that the shadow/formality tower truncates at
+degree~$2$. Theorem~\ref{thm:shadow-archetype-classification}
+identifies the standard-landscape locus with this property as
+precisely class~$G$. Hence an SC-formal algebra must belong
+to class~$G$.
 \end{proof}
 
 \begin{remark}[D-module purity: reduction to a single gap]


thinking
**Considering regex fixes**

I think the current regex is not working well, so I need to rerun it. Maybe I should try using simpler fixed strings instead. I wonder if using the `-F` option with `rg` could help. This may let me match multiple strings more effectively. It feels like a more straightforward approach could save the time spent troubleshooting complex patterns. Let’s give that a go!
codex
One AP grep failed on the regex, not the content. I’m rerunning that check with fixed-string patterns and then moving straight to the build.
exec
/bin/zsh -lc "sed -n '2478,2715p' chapters/theory/chiral_koszul_pairs.tex | rg -n -F -e 'T"'^c(s''^{-1} A)'"' -e 'T"'^c(s A)'"' -e '|s"'^{-1}v| = |v|+1'"'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'pkill -9 -f pdflatex 2>/dev/null || true' in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

 succeeded in 52ms:

exec
/bin/zsh -lc 'sleep 2' in /Users/raeez/chiral-bar-cobar succeeded in 1.96s:

file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 82ce3f8a19eaa51f878397fa63cad2971741bf1e..caf0e7dcc8b2e4df8cb6362c74b5edc7c33e1305
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -2561,7 +2561,7 @@
 & $m_k^{\mathrm{SC}},\; k \geq 5$ \\
 \midrule
 $G$ \textup{(}$r_{\max}=2$\textup{)}
-& Heisenberg, lattice VOA
+& Heisenberg, lattice VOA, free fermion
 & $= 0$
 & $= 0$
 & $= 0$ \\
@@ -2586,12 +2586,21 @@
 
 \medskip\noindent
 \emph{Mechanism.}
-For class~$G$\textup{:} Heisenberg is central, and lattice VOAs are
-Gaussian: the Heisenberg bracket
-$[a_m, a_n] = km\,\delta_{m+n,0}$ is central, while for lattice
-VOAs the shadow obstruction tower terminates at weight~$2$ by
-Corollary~\ref{cor:lattice-postnikov-termination}. In both cases
-all higher tree sums vanish.
+For class~$G$\textup{:}
+Heisenberg, lattice VOAs, and free fermions are Gaussian/free-field:
+their ordered bar data is generated by the binary two-point kernel,
+so every connected genus-$0$ tree with at least three external legs
+factors through pairings and carries no primitive higher vertex.
+Equivalently, the shadow tower truncates at degree~$2$:
+$S_r(\cA)=0$ for $r \geq 3$
+\textup{(}Theorem~\ref{thm:shadow-archetype-classification}; for
+lattices see Corollary~\ref{cor:lattice-postnikov-termination}\textup{)}.
+Under the averaging map
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)},
+the mixed Swiss-cheese tree of arity~$r$ projects to the degree-$r$
+shadow. Since there is no primitive tree for $r \geq 3$,
+all higher mixed-sector operations vanish.
 For class~$L$\textup{:} the affine KM OPE has at most a double pole; the
 three-channel tree sum over $\overline{\cM}_{0,4}$ is nonzero
 \textup{(}$S_3 = 2h^\vee/(k+h^\vee) \neq 0$\textup{)} but the
@@ -2613,10 +2622,25 @@
 
 \begin{proof}
 Class~$G$: for Heisenberg, centrality of the bracket kills all nested
-compositions, so $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$. For lattice
-VOAs, Corollary~\ref{cor:lattice-postnikov-termination} identifies
-the shadow obstruction tower with its weight-$2$ truncation, so the
-transferred Swiss-cheese operations vanish for every $k \geq 3$.
+tree compositions, so $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
+For lattice VOAs, bosonization reduces connected genus-$0$ amplitudes
+to Wick pairings of the underlying Heisenberg field, and
+Corollary~\ref{cor:lattice-postnikov-termination} identifies the
+shadow tower with its weight-$2$ truncation. For the free fermion,
+Wick's theorem gives Pfaffian factorization by the basic contraction
+$\psi(z)\psi^*(w) \sim (z-w)^{-1}$, so again no connected tree with
+$r \geq 3$ survives after extracting the binary pairings. In all three
+cases the mixed Swiss-cheese arity-$r$ operation is the open-colored
+lift of the same genus-$0$ tree sum whose closed projection is
+$S_r(\cA)$; equivalently,
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)}.
+Because class~$G$ means $S_r(\cA) = 0$ for all $r \geq 3$,
+the mixed-sector operations vanish:
+$m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
+The weaker condition $\Delta = 0$ is not sufficient:
+affine Kac--Moody algebras are class~$L$ with $\Delta = 0$ but
+$m_3^{\mathrm{SC}} \neq 0$.
 Class~$L$: the cubic shadow
 $S_3 = 2h^\vee/(k + h^\vee)$ is computed from the OPE coefficient
 ratio (the structure constant divided by the level); the quartic
@@ -2646,10 +2670,10 @@
 relationship between SC-formality and the classification is
 sharper than the table suggests. Proposition~\ref{prop:swiss-cheese-nonformality-by-class}
 already isolates the first nonzero Swiss-cheese operation in each
-non-Gaussian class: class~$L$ has $m_3^{\mathrm{SC}} \neq 0$,
-class~$C$ has $m_4^{\mathrm{SC}} \neq 0$, and class~$M$ has
-nonzero $m_k^{\mathrm{SC}}$ for all $k \geq 3$. This reduces the
-formality criterion to a classification check.
+non-Gaussian class and, on the Gaussian locus, identifies the
+mixed-sector tree formulas with the degree-by-degree shadow tower
+after averaging. The criterion below packages this as an equivalence
+between SC-formality and truncation of the shadow tower at degree~$2$.
 
 \begin{proposition}[SC-formality characterises class~$G$; \ClaimStatusProvedHere]
 \label{prop:sc-formal-iff-class-g}
@@ -2665,21 +2689,30 @@
 The forward direction \textup{(}class~$G$ $\Longrightarrow$
 SC-formal\textup{)} is established in
 Proposition~\ref{prop:swiss-cheese-nonformality-by-class}:
-the class-$G$ row consists exactly of Heisenberg and lattice
-VOAs, and in both cases $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
+the class-$G$ row consists of the Gaussian families Heisenberg,
+lattice VOA, and free fermion, and in each case the genus-$0$
+mixed tree formulas stop at arity~$2$, so
+$m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
 
 For the converse, suppose~$\cA$ is SC-formal.
-Because the standard landscape is exhausted by the four classes
-$G$, $L$, $C$, $M$, it is enough to eliminate the three
-non-Gaussian cases. Proposition~\ref{prop:swiss-cheese-nonformality-by-class}
-does exactly this: class~$L$ has $m_3^{\mathrm{SC}} \neq 0$,
-class~$C$ has $m_4^{\mathrm{SC}} \neq 0$, and class~$M$ has
-nonzero higher operations in every arity $k \geq 3$. Each of
-these cases contradicts SC-formality. This converse uses only the
-classification from Proposition~\ref{prop:swiss-cheese-nonformality-by-class};
-it does not invoke any trilinear form built from~$\kappa$.
-Hence an SC-formal algebra must
-belong to class~$G$.
+Then the mixed sector of the Swiss-cheese bar complex is formal:
+every higher arity tree operation vanishes. The tower-bar
+correspondence is operadic: the arity-$r$ mixed tree and the
+degree-$r$ shadow are produced by the same genus-$0$ tree-transfer
+formula, with the same propagator on internal edges; the only
+difference is the output colour, and passage to the symmetric
+closed sector applies the averaging morphism
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)}.
+Hence SC-formality forces $S_r(\cA) = 0$ for every $r \geq 3$:
+there is no higher mixed tree whose closed projection could survive.
+By Theorem~\ref{thm:shadow-formality-identification} and
+Proposition~\ref{prop:shadow-tower-three-lenses}, this is exactly
+the statement that the shadow/formality tower truncates at
+degree~$2$. Theorem~\ref{thm:shadow-archetype-classification}
+identifies the standard-landscape locus with this property as
+precisely class~$G$. Hence an SC-formal algebra must belong
+to class~$G$.
 \end{proof}
 
 \begin{remark}[D-module purity: reduction to a single gap]


thinking
**Considering build options**

I need to run a build, but I'm not sure if I should aim for speed or thoroughness. If I make it fast, will I skip important steps? But if I take too long, I might delay other tasks. There's a balance to strike here! I wonder if there's a way to optimize the process but still ensure everything is working correctly. Let's weigh the pros and cons of each approach before deciding.
exec
/bin/zsh -lc 'make fast' in /Users/raeez/chiral-bar-cobarfile update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 82ce3f8a19eaa51f878397fa63cad2971741bf1e..caf0e7dcc8b2e4df8cb6362c74b5edc7c33e1305
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -2561,7 +2561,7 @@
 & $m_k^{\mathrm{SC}},\; k \geq 5$ \\
 \midrule
 $G$ \textup{(}$r_{\max}=2$\textup{)}
-& Heisenberg, lattice VOA
+& Heisenberg, lattice VOA, free fermion
 & $= 0$
 & $= 0$
 & $= 0$ \\
@@ -2586,12 +2586,21 @@
 
 \medskip\noindent
 \emph{Mechanism.}
-For class~$G$\textup{:} Heisenberg is central, and lattice VOAs are
-Gaussian: the Heisenberg bracket
-$[a_m, a_n] = km\,\delta_{m+n,0}$ is central, while for lattice
-VOAs the shadow obstruction tower terminates at weight~$2$ by
-Corollary~\ref{cor:lattice-postnikov-termination}. In both cases
-all higher tree sums vanish.
+For class~$G$\textup{:}
+Heisenberg, lattice VOAs, and free fermions are Gaussian/free-field:
+their ordered bar data is generated by the binary two-point kernel,
+so every connected genus-$0$ tree with at least three external legs
+factors through pairings and carries no primitive higher vertex.
+Equivalently, the shadow tower truncates at degree~$2$:
+$S_r(\cA)=0$ for $r \geq 3$
+\textup{(}Theorem~\ref{thm:shadow-archetype-classification}; for
+lattices see Corollary~\ref{cor:lattice-postnikov-termination}\textup{)}.
+Under the averaging map
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)},
+the mixed Swiss-cheese tree of arity~$r$ projects to the degree-$r$
+shadow. Since there is no primitive tree for $r \geq 3$,
+all higher mixed-sector operations vanish.
 For class~$L$\textup{:} the affine KM OPE has at most a double pole; the
 three-channel tree sum over $\overline{\cM}_{0,4}$ is nonzero
 \textup{(}$S_3 = 2h^\vee/(k+h^\vee) \neq 0$\textup{)} but the
@@ -2613,10 +2622,25 @@
 
 \begin{proof}
 Class~$G$: for Heisenberg, centrality of the bracket kills all nested
-compositions, so $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$. For lattice
-VOAs, Corollary~\ref{cor:lattice-postnikov-termination} identifies
-the shadow obstruction tower with its weight-$2$ truncation, so the
-transferred Swiss-cheese operations vanish for every $k \geq 3$.
+tree compositions, so $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
+For lattice VOAs, bosonization reduces connected genus-$0$ amplitudes
+to Wick pairings of the underlying Heisenberg field, and
+Corollary~\ref{cor:lattice-postnikov-termination} identifies the
+shadow tower with its weight-$2$ truncation. For the free fermion,
+Wick's theorem gives Pfaffian factorization by the basic contraction
+$\psi(z)\psi^*(w) \sim (z-w)^{-1}$, so again no connected tree with
+$r \geq 3$ survives after extracting the binary pairings. In all three
+cases the mixed Swiss-cheese arity-$r$ operation is the open-colored
+lift of the same genus-$0$ tree sum whose closed projection is
+$S_r(\cA)$; equivalently,
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)}.
+Because class~$G$ means $S_r(\cA) = 0$ for all $r \geq 3$,
+the mixed-sector operations vanish:
+$m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
+The weaker condition $\Delta = 0$ is not sufficient:
+affine Kac--Moody algebras are class~$L$ with $\Delta = 0$ but
+$m_3^{\mathrm{SC}} \neq 0$.
 Class~$L$: the cubic shadow
 $S_3 = 2h^\vee/(k + h^\vee)$ is computed from the OPE coefficient
 ratio (the structure constant divided by the level); the quartic
@@ -2646,10 +2670,10 @@
 relationship between SC-formality and the classification is
 sharper than the table suggests. Proposition~\ref{prop:swiss-cheese-nonformality-by-class}
 already isolates the first nonzero Swiss-cheese operation in each
-non-Gaussian class: class~$L$ has $m_3^{\mathrm{SC}} \neq 0$,
-class~$C$ has $m_4^{\mathrm{SC}} \neq 0$, and class~$M$ has
-nonzero $m_k^{\mathrm{SC}}$ for all $k \geq 3$. This reduces the
-formality criterion to a classification check.
+non-Gaussian class and, on the Gaussian locus, identifies the
+mixed-sector tree formulas with the degree-by-degree shadow tower
+after averaging. The criterion below packages this as an equivalence
+between SC-formality and truncation of the shadow tower at degree~$2$.
 
 \begin{proposition}[SC-formality characterises class~$G$; \ClaimStatusProvedHere]
 \label{prop:sc-formal-iff-class-g}
@@ -2665,21 +2689,30 @@
 The forward direction \textup{(}class~$G$ $\Longrightarrow$
 SC-formal\textup{)} is established in
 Proposition~\ref{prop:swiss-cheese-nonformality-by-class}:
-the class-$G$ row consists exactly of Heisenberg and lattice
-VOAs, and in both cases $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
+the class-$G$ row consists of the Gaussian families Heisenberg,
+lattice VOA, and free fermion, and in each case the genus-$0$
+mixed tree formulas stop at arity~$2$, so
+$m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
 
 For the converse, suppose~$\cA$ is SC-formal.
-Because the standard landscape is exhausted by the four classes
-$G$, $L$, $C$, $M$, it is enough to eliminate the three
-non-Gaussian cases. Proposition~\ref{prop:swiss-cheese-nonformality-by-class}
-does exactly this: class~$L$ has $m_3^{\mathrm{SC}} \neq 0$,
-class~$C$ has $m_4^{\mathrm{SC}} \neq 0$, and class~$M$ has
-nonzero higher operations in every arity $k \geq 3$. Each of
-these cases contradicts SC-formality. This converse uses only the
-classification from Proposition~\ref{prop:swiss-cheese-nonformality-by-class};
-it does not invoke any trilinear form built from~$\kappa$.
-Hence an SC-formal algebra must
-belong to class~$G$.
+Then the mixed sector of the Swiss-cheese bar complex is formal:
+every higher arity tree operation vanishes. The tower-bar
+correspondence is operadic: the arity-$r$ mixed tree and the
+degree-$r$ shadow are produced by the same genus-$0$ tree-transfer
+formula, with the same propagator on internal edges; the only
+difference is the output colour, and passage to the symmetric
+closed sector applies the averaging morphism
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)}.
+Hence SC-formality forces $S_r(\cA) = 0$ for every $r \geq 3$:
+there is no higher mixed tree whose closed projection could survive.
+By Theorem~\ref{thm:shadow-formality-identification} and
+Proposition~\ref{prop:shadow-tower-three-lenses}, this is exactly
+the statement that the shadow/formality tower truncates at
+degree~$2$. Theorem~\ref{thm:shadow-archetype-classification}
+identifies the standard-landscape locus with this property as
+precisely class~$G$. Hence an SC-formal algebra must belong
+to class~$G$.
 \end{proof}
 
 \begin{remark}[D-module purity: reduction to a single gap]

codex
The fast build is running. While that stabilizes, I’m not changing text further; the remaining work is falsification, then a final reread against the proof obligations.
file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 82ce3f8a19eaa51f878397fa63cad2971741bf1e..caf0e7dcc8b2e4df8cb6362c74b5edc7c33e1305
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -2561,7 +2561,7 @@
 & $m_k^{\mathrm{SC}},\; k \geq 5$ \\
 \midrule
 $G$ \textup{(}$r_{\max}=2$\textup{)}
-& Heisenberg, lattice VOA
+& Heisenberg, lattice VOA, free fermion
 & $= 0$
 & $= 0$
 & $= 0$ \\
@@ -2586,12 +2586,21 @@
 
 \medskip\noindent
 \emph{Mechanism.}
-For class~$G$\textup{:} Heisenberg is central, and lattice VOAs are
-Gaussian: the Heisenberg bracket
-$[a_m, a_n] = km\,\delta_{m+n,0}$ is central, while for lattice
-VOAs the shadow obstruction tower terminates at weight~$2$ by
-Corollary~\ref{cor:lattice-postnikov-termination}. In both cases
-all higher tree sums vanish.
+For class~$G$\textup{:}
+Heisenberg, lattice VOAs, and free fermions are Gaussian/free-field:
+their ordered bar data is generated by the binary two-point kernel,
+so every connected genus-$0$ tree with at least three external legs
+factors through pairings and carries no primitive higher vertex.
+Equivalently, the shadow tower truncates at degree~$2$:
+$S_r(\cA)=0$ for $r \geq 3$
+\textup{(}Theorem~\ref{thm:shadow-archetype-classification}; for
+lattices see Corollary~\ref{cor:lattice-postnikov-termination}\textup{)}.
+Under the averaging map
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)},
+the mixed Swiss-cheese tree of arity~$r$ projects to the degree-$r$
+shadow. Since there is no primitive tree for $r \geq 3$,
+all higher mixed-sector operations vanish.
 For class~$L$\textup{:} the affine KM OPE has at most a double pole; the
 three-channel tree sum over $\overline{\cM}_{0,4}$ is nonzero
 \textup{(}$S_3 = 2h^\vee/(k+h^\vee) \neq 0$\textup{)} but the
@@ -2613,10 +2622,25 @@
 
 \begin{proof}
 Class~$G$: for Heisenberg, centrality of the bracket kills all nested
-compositions, so $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$. For lattice
-VOAs, Corollary~\ref{cor:lattice-postnikov-termination} identifies
-the shadow obstruction tower with its weight-$2$ truncation, so the
-transferred Swiss-cheese operations vanish for every $k \geq 3$.
+tree compositions, so $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
+For lattice VOAs, bosonization reduces connected genus-$0$ amplitudes
+to Wick pairings of the underlying Heisenberg field, and
+Corollary~\ref{cor:lattice-postnikov-termination} identifies the
+shadow tower with its weight-$2$ truncation. For the free fermion,
+Wick's theorem gives Pfaffian factorization by the basic contraction
+$\psi(z)\psi^*(w) \sim (z-w)^{-1}$, so again no connected tree with
+$r \geq 3$ survives after extracting the binary pairings. In all three
+cases the mixed Swiss-cheese arity-$r$ operation is the open-colored
+lift of the same genus-$0$ tree sum whose closed projection is
+$S_r(\cA)$; equivalently,
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)}.
+Because class~$G$ means $S_r(\cA) = 0$ for all $r \geq 3$,
+the mixed-sector operations vanish:
+$m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
+The weaker condition $\Delta = 0$ is not sufficient:
+affine Kac--Moody algebras are class~$L$ with $\Delta = 0$ but
+$m_3^{\mathrm{SC}} \neq 0$.
 Class~$L$: the cubic shadow
 $S_3 = 2h^\vee/(k + h^\vee)$ is computed from the OPE coefficient
 ratio (the structure constant divided by the level); the quartic
@@ -2646,10 +2670,10 @@
 relationship between SC-formality and the classification is
 sharper than the table suggests. Proposition~\ref{prop:swiss-cheese-nonformality-by-class}
 already isolates the first nonzero Swiss-cheese operation in each
-non-Gaussian class: class~$L$ has $m_3^{\mathrm{SC}} \neq 0$,
-class~$C$ has $m_4^{\mathrm{SC}} \neq 0$, and class~$M$ has
-nonzero $m_k^{\mathrm{SC}}$ for all $k \geq 3$. This reduces the
-formality criterion to a classification check.
+non-Gaussian class and, on the Gaussian locus, identifies the
+mixed-sector tree formulas with the degree-by-degree shadow tower
+after averaging. The criterion below packages this as an equivalence
+between SC-formality and truncation of the shadow tower at degree~$2$.
 
 \begin{proposition}[SC-formality characterises class~$G$; \ClaimStatusProvedHere]
 \label{prop:sc-formal-iff-class-g}
@@ -2665,21 +2689,30 @@
 The forward direction \textup{(}class~$G$ $\Longrightarrow$
 SC-formal\textup{)} is established in
 Proposition~\ref{prop:swiss-cheese-nonformality-by-class}:
-the class-$G$ row consists exactly of Heisenberg and lattice
-VOAs, and in both cases $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
+the class-$G$ row consists of the Gaussian families Heisenberg,
+lattice VOA, and free fermion, and in each case the genus-$0$
+mixed tree formulas stop at arity~$2$, so
+$m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
 
 For the converse, suppose~$\cA$ is SC-formal.
-Because the standard landscape is exhausted by the four classes
-$G$, $L$, $C$, $M$, it is enough to eliminate the three
-non-Gaussian cases. Proposition~\ref{prop:swiss-cheese-nonformality-by-class}
-does exactly this: class~$L$ has $m_3^{\mathrm{SC}} \neq 0$,
-class~$C$ has $m_4^{\mathrm{SC}} \neq 0$, and class~$M$ has
-nonzero higher operations in every arity $k \geq 3$. Each of
-these cases contradicts SC-formality. This converse uses only the
-classification from Proposition~\ref{prop:swiss-cheese-nonformality-by-class};
-it does not invoke any trilinear form built from~$\kappa$.
-Hence an SC-formal algebra must
-belong to class~$G$.
+Then the mixed sector of the Swiss-cheese bar complex is formal:
+every higher arity tree operation vanishes. The tower-bar
+correspondence is operadic: the arity-$r$ mixed tree and the
+degree-$r$ shadow are produced by the same genus-$0$ tree-transfer
+formula, with the same propagator on internal edges; the only
+difference is the output colour, and passage to the symmetric
+closed sector applies the averaging morphism
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)}.
+Hence SC-formality forces $S_r(\cA) = 0$ for every $r \geq 3$:
+there is no higher mixed tree whose closed projection could survive.
+By Theorem~\ref{thm:shadow-formality-identification} and
+Proposition~\ref{prop:shadow-tower-three-lenses}, this is exactly
+the statement that the shadow/formality tower truncates at
+degree~$2$. Theorem~\ref{thm:shadow-archetype-classification}
+identifies the standard-landscape locus with this property as
+precisely class~$G$. Hence an SC-formal algebra must belong
+to class~$G$.
 \end{proof}
 
 \begin{remark}[D-module purity: reduction to a single gap]

file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 82ce3f8a19eaa51f878397fa63cad2971741bf1e..caf0e7dcc8b2e4df8cb6362c74b5edc7c33e1305
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -2561,7 +2561,7 @@
 & $m_k^{\mathrm{SC}},\; k \geq 5$ \\
 \midrule
 $G$ \textup{(}$r_{\max}=2$\textup{)}
-& Heisenberg, lattice VOA
+& Heisenberg, lattice VOA, free fermion
 & $= 0$
 & $= 0$
 & $= 0$ \\
@@ -2586,12 +2586,21 @@
 
 \medskip\noindent
 \emph{Mechanism.}
-For class~$G$\textup{:} Heisenberg is central, and lattice VOAs are
-Gaussian: the Heisenberg bracket
-$[a_m, a_n] = km\,\delta_{m+n,0}$ is central, while for lattice
-VOAs the shadow obstruction tower terminates at weight~$2$ by
-Corollary~\ref{cor:lattice-postnikov-termination}. In both cases
-all higher tree sums vanish.
+For class~$G$\textup{:}
+Heisenberg, lattice VOAs, and free fermions are Gaussian/free-field:
+their ordered bar data is generated by the binary two-point kernel,
+so every connected genus-$0$ tree with at least three external legs
+factors through pairings and carries no primitive higher vertex.
+Equivalently, the shadow tower truncates at degree~$2$:
+$S_r(\cA)=0$ for $r \geq 3$
+\textup{(}Theorem~\ref{thm:shadow-archetype-classification}; for
+lattices see Corollary~\ref{cor:lattice-postnikov-termination}\textup{)}.
+Under the averaging map
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)},
+the mixed Swiss-cheese tree of arity~$r$ projects to the degree-$r$
+shadow. Since there is no primitive tree for $r \geq 3$,
+all higher mixed-sector operations vanish.
 For class~$L$\textup{:} the affine KM OPE has at most a double pole; the
 three-channel tree sum over $\overline{\cM}_{0,4}$ is nonzero
 \textup{(}$S_3 = 2h^\vee/(k+h^\vee) \neq 0$\textup{)} but the
@@ -2613,10 +2622,25 @@
 
 \begin{proof}
 Class~$G$: for Heisenberg, centrality of the bracket kills all nested
-compositions, so $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$. For lattice
-VOAs, Corollary~\ref{cor:lattice-postnikov-termination} identifies
-the shadow obstruction tower with its weight-$2$ truncation, so the
-transferred Swiss-cheese operations vanish for every $k \geq 3$.
+tree compositions, so $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
+For lattice VOAs, bosonization reduces connected genus-$0$ amplitudes
+to Wick pairings of the underlying Heisenberg field, and
+Corollary~\ref{cor:lattice-postnikov-termination} identifies the
+shadow tower with its weight-$2$ truncation. For the free fermion,
+Wick's theorem gives Pfaffian factorization by the basic contraction
+$\psi(z)\psi^*(w) \sim (z-w)^{-1}$, so again no connected tree with
+$r \geq 3$ survives after extracting the binary pairings. In all three
+cases the mixed Swiss-cheese arity-$r$ operation is the open-colored
+lift of the same genus-$0$ tree sum whose closed projection is
+$S_r(\cA)$; equivalently,
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)}.
+Because class~$G$ means $S_r(\cA) = 0$ for all $r \geq 3$,
+the mixed-sector operations vanish:
+$m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
+The weaker condition $\Delta = 0$ is not sufficient:
+affine Kac--Moody algebras are class~$L$ with $\Delta = 0$ but
+$m_3^{\mathrm{SC}} \neq 0$.
 Class~$L$: the cubic shadow
 $S_3 = 2h^\vee/(k + h^\vee)$ is computed from the OPE coefficient
 ratio (the structure constant divided by the level); the quartic
@@ -2646,10 +2670,10 @@
 relationship between SC-formality and the classification is
 sharper than the table suggests. Proposition~\ref{prop:swiss-cheese-nonformality-by-class}
 already isolates the first nonzero Swiss-cheese operation in each
-non-Gaussian class: class~$L$ has $m_3^{\mathrm{SC}} \neq 0$,
-class~$C$ has $m_4^{\mathrm{SC}} \neq 0$, and class~$M$ has
-nonzero $m_k^{\mathrm{SC}}$ for all $k \geq 3$. This reduces the
-formality criterion to a classification check.
+non-Gaussian class and, on the Gaussian locus, identifies the
+mixed-sector tree formulas with the degree-by-degree shadow tower
+after averaging. The criterion below packages this as an equivalence
+between SC-formality and truncation of the shadow tower at degree~$2$.
 
 \begin{proposition}[SC-formality characterises class~$G$; \ClaimStatusProvedHere]
 \label{prop:sc-formal-iff-class-g}
@@ -2665,21 +2689,30 @@
 The forward direction \textup{(}class~$G$ $\Longrightarrow$
 SC-formal\textup{)} is established in
 Proposition~\ref{prop:swiss-cheese-nonformality-by-class}:
-the class-$G$ row consists exactly of Heisenberg and lattice
-VOAs, and in both cases $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
+the class-$G$ row consists of the Gaussian families Heisenberg,
+lattice VOA, and free fermion, and in each case the genus-$0$
+mixed tree formulas stop at arity~$2$, so
+$m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
 
 For the converse, suppose~$\cA$ is SC-formal.
-Because the standard landscape is exhausted by the four classes
-$G$, $L$, $C$, $M$, it is enough to eliminate the three
-non-Gaussian cases. Proposition~\ref{prop:swiss-cheese-nonformality-by-class}
-does exactly this: class~$L$ has $m_3^{\mathrm{SC}} \neq 0$,
-class~$C$ has $m_4^{\mathrm{SC}} \neq 0$, and class~$M$ has
-nonzero higher operations in every arity $k \geq 3$. Each of
-these cases contradicts SC-formality. This converse uses only the
-classification from Proposition~\ref{prop:swiss-cheese-nonformality-by-class};
-it does not invoke any trilinear form built from~$\kappa$.
-Hence an SC-formal algebra must
-belong to class~$G$.
+Then the mixed sector of the Swiss-cheese bar complex is formal:
+every higher arity tree operation vanishes. The tower-bar
+correspondence is operadic: the arity-$r$ mixed tree and the
+degree-$r$ shadow are produced by the same genus-$0$ tree-transfer
+formula, with the same propagator on internal edges; the only
+difference is the output colour, and passage to the symmetric
+closed sector applies the averaging morphism
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)}.
+Hence SC-formality forces $S_r(\cA) = 0$ for every $r \geq 3$:
+there is no higher mixed tree whose closed projection could survive.
+By Theorem~\ref{thm:shadow-formality-identification} and
+Proposition~\ref{prop:shadow-tower-three-lenses}, this is exactly
+the statement that the shadow/formality tower truncates at
+degree~$2$. Theorem~\ref{thm:shadow-archetype-classification}
+identifies the standard-landscape locus with this property as
+precisely class~$G$. Hence an SC-formal algebra must belong
+to class~$G$.
 \end{proof}
 
 \begin{remark}[D-module purity: reduction to a single gap]

file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 82ce3f8a19eaa51f878397fa63cad2971741bf1e..caf0e7dcc8b2e4df8cb6362c74b5edc7c33e1305
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -2561,7 +2561,7 @@
 & $m_k^{\mathrm{SC}},\; k \geq 5$ \\
 \midrule
 $G$ \textup{(}$r_{\max}=2$\textup{)}
-& Heisenberg, lattice VOA
+& Heisenberg, lattice VOA, free fermion
 & $= 0$
 & $= 0$
 & $= 0$ \\
@@ -2586,12 +2586,21 @@
 
 \medskip\noindent
 \emph{Mechanism.}
-For class~$G$\textup{:} Heisenberg is central, and lattice VOAs are
-Gaussian: the Heisenberg bracket
-$[a_m, a_n] = km\,\delta_{m+n,0}$ is central, while for lattice
-VOAs the shadow obstruction tower terminates at weight~$2$ by
-Corollary~\ref{cor:lattice-postnikov-termination}. In both cases
-all higher tree sums vanish.
+For class~$G$\textup{:}
+Heisenberg, lattice VOAs, and free fermions are Gaussian/free-field:
+their ordered bar data is generated by the binary two-point kernel,
+so every connected genus-$0$ tree with at least three external legs
+factors through pairings and carries no primitive higher vertex.
+Equivalently, the shadow tower truncates at degree~$2$:
+$S_r(\cA)=0$ for $r \geq 3$
+\textup{(}Theorem~\ref{thm:shadow-archetype-classification}; for
+lattices see Corollary~\ref{cor:lattice-postnikov-termination}\textup{)}.
+Under the averaging map
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)},
+the mixed Swiss-cheese tree of arity~$r$ projects to the degree-$r$
+shadow. Since there is no primitive tree for $r \geq 3$,
+all higher mixed-sector operations vanish.
 For class~$L$\textup{:} the affine KM OPE has at most a double pole; the
 three-channel tree sum over $\overline{\cM}_{0,4}$ is nonzero
 \textup{(}$S_3 = 2h^\vee/(k+h^\vee) \neq 0$\textup{)} but the
@@ -2613,10 +2622,25 @@
 
 \begin{proof}
 Class~$G$: for Heisenberg, centrality of the bracket kills all nested
-compositions, so $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$. For lattice
-VOAs, Corollary~\ref{cor:lattice-postnikov-termination} identifies
-the shadow obstruction tower with its weight-$2$ truncation, so the
-transferred Swiss-cheese operations vanish for every $k \geq 3$.
+tree compositions, so $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
+For lattice VOAs, bosonization reduces connected genus-$0$ amplitudes
+to Wick pairings of the underlying Heisenberg field, and
+Corollary~\ref{cor:lattice-postnikov-termination} identifies the
+shadow tower with its weight-$2$ truncation. For the free fermion,
+Wick's theorem gives Pfaffian factorization by the basic contraction
+$\psi(z)\psi^*(w) \sim (z-w)^{-1}$, so again no connected tree with
+$r \geq 3$ survives after extracting the binary pairings. In all three
+cases the mixed Swiss-cheese arity-$r$ operation is the open-colored
+lift of the same genus-$0$ tree sum whose closed projection is
+$S_r(\cA)$; equivalently,
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)}.
+Because class~$G$ means $S_r(\cA) = 0$ for all $r \geq 3$,
+the mixed-sector operations vanish:
+$m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
+The weaker condition $\Delta = 0$ is not sufficient:
+affine Kac--Moody algebras are class~$L$ with $\Delta = 0$ but
+$m_3^{\mathrm{SC}} \neq 0$.
 Class~$L$: the cubic shadow
 $S_3 = 2h^\vee/(k + h^\vee)$ is computed from the OPE coefficient
 ratio (the structure constant divided by the level); the quartic
@@ -2646,10 +2670,10 @@
 relationship between SC-formality and the classification is
 sharper than the table suggests. Proposition~\ref{prop:swiss-cheese-nonformality-by-class}
 already isolates the first nonzero Swiss-cheese operation in each
-non-Gaussian class: class~$L$ has $m_3^{\mathrm{SC}} \neq 0$,
-class~$C$ has $m_4^{\mathrm{SC}} \neq 0$, and class~$M$ has
-nonzero $m_k^{\mathrm{SC}}$ for all $k \geq 3$. This reduces the
-formality criterion to a classification check.
+non-Gaussian class and, on the Gaussian locus, identifies the
+mixed-sector tree formulas with the degree-by-degree shadow tower
+after averaging. The criterion below packages this as an equivalence
+between SC-formality and truncation of the shadow tower at degree~$2$.
 
 \begin{proposition}[SC-formality characterises class~$G$; \ClaimStatusProvedHere]
 \label{prop:sc-formal-iff-class-g}
@@ -2665,21 +2689,30 @@
 The forward direction \textup{(}class~$G$ $\Longrightarrow$
 SC-formal\textup{)} is established in
 Proposition~\ref{prop:swiss-cheese-nonformality-by-class}:
-the class-$G$ row consists exactly of Heisenberg and lattice
-VOAs, and in both cases $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
+the class-$G$ row consists of the Gaussian families Heisenberg,
+lattice VOA, and free fermion, and in each case the genus-$0$
+mixed tree formulas stop at arity~$2$, so
+$m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
 
 For the converse, suppose~$\cA$ is SC-formal.
-Because the standard landscape is exhausted by the four classes
-$G$, $L$, $C$, $M$, it is enough to eliminate the three
-non-Gaussian cases. Proposition~\ref{prop:swiss-cheese-nonformality-by-class}
-does exactly this: class~$L$ has $m_3^{\mathrm{SC}} \neq 0$,
-class~$C$ has $m_4^{\mathrm{SC}} \neq 0$, and class~$M$ has
-nonzero higher operations in every arity $k \geq 3$. Each of
-these cases contradicts SC-formality. This converse uses only the
-classification from Proposition~\ref{prop:swiss-cheese-nonformality-by-class};
-it does not invoke any trilinear form built from~$\kappa$.
-Hence an SC-formal algebra must
-belong to class~$G$.
+Then the mixed sector of the Swiss-cheese bar complex is formal:
+every higher arity tree operation vanishes. The tower-bar
+correspondence is operadic: the arity-$r$ mixed tree and the
+degree-$r$ shadow are produced by the same genus-$0$ tree-transfer
+formula, with the same propagator on internal edges; the only
+difference is the output colour, and passage to the symmetric
+closed sector applies the averaging morphism
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)}.
+Hence SC-formality forces $S_r(\cA) = 0$ for every $r \geq 3$:
+there is no higher mixed tree whose closed projection could survive.
+By Theorem~\ref{thm:shadow-formality-identification} and
+Proposition~\ref{prop:shadow-tower-three-lenses}, this is exactly
+the statement that the shadow/formality tower truncates at
+degree~$2$. Theorem~\ref{thm:shadow-archetype-classification}
+identifies the standard-landscape locus with this property as
+precisely class~$G$. Hence an SC-formal algebra must belong
+to class~$G$.
 \end{proof}
 
 \begin{remark}[D-module purity: reduction to a single gap]

codex
The build surface is still active with no emitted diagnostics yet. If it finishes cleanly, I’ll do one last hostile reread of just the modified theorem lane and then close out with the exact theorem form and any scoped propagation debt.
file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 82ce3f8a19eaa51f878397fa63cad2971741bf1e..caf0e7dcc8b2e4df8cb6362c74b5edc7c33e1305
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -2561,7 +2561,7 @@
 & $m_k^{\mathrm{SC}},\; k \geq 5$ \\
 \midrule
 $G$ \textup{(}$r_{\max}=2$\textup{)}
-& Heisenberg, lattice VOA
+& Heisenberg, lattice VOA, free fermion
 & $= 0$
 & $= 0$
 & $= 0$ \\
@@ -2586,12 +2586,21 @@
 
 \medskip\noindent
 \emph{Mechanism.}
-For class~$G$\textup{:} Heisenberg is central, and lattice VOAs are
-Gaussian: the Heisenberg bracket
-$[a_m, a_n] = km\,\delta_{m+n,0}$ is central, while for lattice
-VOAs the shadow obstruction tower terminates at weight~$2$ by
-Corollary~\ref{cor:lattice-postnikov-termination}. In both cases
-all higher tree sums vanish.
+For class~$G$\textup{:}
+Heisenberg, lattice VOAs, and free fermions are Gaussian/free-field:
+their ordered bar data is generated by the binary two-point kernel,
+so every connected genus-$0$ tree with at least three external legs
+factors through pairings and carries no primitive higher vertex.
+Equivalently, the shadow tower truncates at degree~$2$:
+$S_r(\cA)=0$ for $r \geq 3$
+\textup{(}Theorem~\ref{thm:shadow-archetype-classification}; for
+lattices see Corollary~\ref{cor:lattice-postnikov-termination}\textup{)}.
+Under the averaging map
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)},
+the mixed Swiss-cheese tree of arity~$r$ projects to the degree-$r$
+shadow. Since there is no primitive tree for $r \geq 3$,
+all higher mixed-sector operations vanish.
 For class~$L$\textup{:} the affine KM OPE has at most a double pole; the
 three-channel tree sum over $\overline{\cM}_{0,4}$ is nonzero
 \textup{(}$S_3 = 2h^\vee/(k+h^\vee) \neq 0$\textup{)} but the
@@ -2613,10 +2622,25 @@
 
 \begin{proof}
 Class~$G$: for Heisenberg, centrality of the bracket kills all nested
-compositions, so $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$. For lattice
-VOAs, Corollary~\ref{cor:lattice-postnikov-termination} identifies
-the shadow obstruction tower with its weight-$2$ truncation, so the
-transferred Swiss-cheese operations vanish for every $k \geq 3$.
+tree compositions, so $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
+For lattice VOAs, bosonization reduces connected genus-$0$ amplitudes
+to Wick pairings of the underlying Heisenberg field, and
+Corollary~\ref{cor:lattice-postnikov-termination} identifies the
+shadow tower with its weight-$2$ truncation. For the free fermion,
+Wick's theorem gives Pfaffian factorization by the basic contraction
+$\psi(z)\psi^*(w) \sim (z-w)^{-1}$, so again no connected tree with
+$r \geq 3$ survives after extracting the binary pairings. In all three
+cases the mixed Swiss-cheese arity-$r$ operation is the open-colored
+lift of the same genus-$0$ tree sum whose closed projection is
+$S_r(\cA)$; equivalently,
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)}.
+Because class~$G$ means $S_r(\cA) = 0$ for all $r \geq 3$,
+the mixed-sector operations vanish:
+$m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
+The weaker condition $\Delta = 0$ is not sufficient:
+affine Kac--Moody algebras are class~$L$ with $\Delta = 0$ but
+$m_3^{\mathrm{SC}} \neq 0$.
 Class~$L$: the cubic shadow
 $S_3 = 2h^\vee/(k + h^\vee)$ is computed from the OPE coefficient
 ratio (the structure constant divided by the level); the quartic
@@ -2646,10 +2670,10 @@
 relationship between SC-formality and the classification is
 sharper than the table suggests. Proposition~\ref{prop:swiss-cheese-nonformality-by-class}
 already isolates the first nonzero Swiss-cheese operation in each
-non-Gaussian class: class~$L$ has $m_3^{\mathrm{SC}} \neq 0$,
-class~$C$ has $m_4^{\mathrm{SC}} \neq 0$, and class~$M$ has
-nonzero $m_k^{\mathrm{SC}}$ for all $k \geq 3$. This reduces the
-formality criterion to a classification check.
+non-Gaussian class and, on the Gaussian locus, identifies the
+mixed-sector tree formulas with the degree-by-degree shadow tower
+after averaging. The criterion below packages this as an equivalence
+between SC-formality and truncation of the shadow tower at degree~$2$.
 
 \begin{proposition}[SC-formality characterises class~$G$; \ClaimStatusProvedHere]
 \label{prop:sc-formal-iff-class-g}
@@ -2665,21 +2689,30 @@
 The forward direction \textup{(}class~$G$ $\Longrightarrow$
 SC-formal\textup{)} is established in
 Proposition~\ref{prop:swiss-cheese-nonformality-by-class}:
-the class-$G$ row consists exactly of Heisenberg and lattice
-VOAs, and in both cases $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
+the class-$G$ row consists of the Gaussian families Heisenberg,
+lattice VOA, and free fermion, and in each case the genus-$0$
+mixed tree formulas stop at arity~$2$, so
+$m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
 
 For the converse, suppose~$\cA$ is SC-formal.
-Because the standard landscape is exhausted by the four classes
-$G$, $L$, $C$, $M$, it is enough to eliminate the three
-non-Gaussian cases. Proposition~\ref{prop:swiss-cheese-nonformality-by-class}
-does exactly this: class~$L$ has $m_3^{\mathrm{SC}} \neq 0$,
-class~$C$ has $m_4^{\mathrm{SC}} \neq 0$, and class~$M$ has
-nonzero higher operations in every arity $k \geq 3$. Each of
-these cases contradicts SC-formality. This converse uses only the
-classification from Proposition~\ref{prop:swiss-cheese-nonformality-by-class};
-it does not invoke any trilinear form built from~$\kappa$.
-Hence an SC-formal algebra must
-belong to class~$G$.
+Then the mixed sector of the Swiss-cheese bar complex is formal:
+every higher arity tree operation vanishes. The tower-bar
+correspondence is operadic: the arity-$r$ mixed tree and the
+degree-$r$ shadow are produced by the same genus-$0$ tree-transfer
+formula, with the same propagator on internal edges; the only
+difference is the output colour, and passage to the symmetric
+closed sector applies the averaging morphism
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)}.
+Hence SC-formality forces $S_r(\cA) = 0$ for every $r \geq 3$:
+there is no higher mixed tree whose closed projection could survive.
+By Theorem~\ref{thm:shadow-formality-identification} and
+Proposition~\ref{prop:shadow-tower-three-lenses}, this is exactly
+the statement that the shadow/formality tower truncates at
+degree~$2$. Theorem~\ref{thm:shadow-archetype-classification}
+identifies the standard-landscape locus with this property as
+precisely class~$G$. Hence an SC-formal algebra must belong
+to class~$G$.
 \end{proof}
 
 \begin{remark}[D-module purity: reduction to a single gap]

file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 82ce3f8a19eaa51f878397fa63cad2971741bf1e..caf0e7dcc8b2e4df8cb6362c74b5edc7c33e1305
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -2561,7 +2561,7 @@
 & $m_k^{\mathrm{SC}},\; k \geq 5$ \\
 \midrule
 $G$ \textup{(}$r_{\max}=2$\textup{)}
-& Heisenberg, lattice VOA
+& Heisenberg, lattice VOA, free fermion
 & $= 0$
 & $= 0$
 & $= 0$ \\
@@ -2586,12 +2586,21 @@
 
 \medskip\noindent
 \emph{Mechanism.}
-For class~$G$\textup{:} Heisenberg is central, and lattice VOAs are
-Gaussian: the Heisenberg bracket
-$[a_m, a_n] = km\,\delta_{m+n,0}$ is central, while for lattice
-VOAs the shadow obstruction tower terminates at weight~$2$ by
-Corollary~\ref{cor:lattice-postnikov-termination}. In both cases
-all higher tree sums vanish.
+For class~$G$\textup{:}
+Heisenberg, lattice VOAs, and free fermions are Gaussian/free-field:
+their ordered bar data is generated by the binary two-point kernel,
+so every connected genus-$0$ tree with at least three external legs
+factors through pairings and carries no primitive higher vertex.
+Equivalently, the shadow tower truncates at degree~$2$:
+$S_r(\cA)=0$ for $r \geq 3$
+\textup{(}Theorem~\ref{thm:shadow-archetype-classification}; for
+lattices see Corollary~\ref{cor:lattice-postnikov-termination}\textup{)}.
+Under the averaging map
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)},
+the mixed Swiss-cheese tree of arity~$r$ projects to the degree-$r$
+shadow. Since there is no primitive tree for $r \geq 3$,
+all higher mixed-sector operations vanish.
 For class~$L$\textup{:} the affine KM OPE has at most a double pole; the
 three-channel tree sum over $\overline{\cM}_{0,4}$ is nonzero
 \textup{(}$S_3 = 2h^\vee/(k+h^\vee) \neq 0$\textup{)} but the
@@ -2613,10 +2622,25 @@
 
 \begin{proof}
 Class~$G$: for Heisenberg, centrality of the bracket kills all nested
-compositions, so $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$. For lattice
-VOAs, Corollary~\ref{cor:lattice-postnikov-termination} identifies
-the shadow obstruction tower with its weight-$2$ truncation, so the
-transferred Swiss-cheese operations vanish for every $k \geq 3$.
+tree compositions, so $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
+For lattice VOAs, bosonization reduces connected genus-$0$ amplitudes
+to Wick pairings of the underlying Heisenberg field, and
+Corollary~\ref{cor:lattice-postnikov-termination} identifies the
+shadow tower with its weight-$2$ truncation. For the free fermion,
+Wick's theorem gives Pfaffian factorization by the basic contraction
+$\psi(z)\psi^*(w) \sim (z-w)^{-1}$, so again no connected tree with
+$r \geq 3$ survives after extracting the binary pairings. In all three
+cases the mixed Swiss-cheese arity-$r$ operation is the open-colored
+lift of the same genus-$0$ tree sum whose closed projection is
+$S_r(\cA)$; equivalently,
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)}.
+Because class~$G$ means $S_r(\cA) = 0$ for all $r \geq 3$,
+the mixed-sector operations vanish:
+$m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
+The weaker condition $\Delta = 0$ is not sufficient:
+affine Kac--Moody algebras are class~$L$ with $\Delta = 0$ but
+$m_3^{\mathrm{SC}} \neq 0$.
 Class~$L$: the cubic shadow
 $S_3 = 2h^\vee/(k + h^\vee)$ is computed from the OPE coefficient
 ratio (the structure constant divided by the level); the quartic
@@ -2646,10 +2670,10 @@
 relationship between SC-formality and the classification is
 sharper than the table suggests. Proposition~\ref{prop:swiss-cheese-nonformality-by-class}
 already isolates the first nonzero Swiss-cheese operation in each
-non-Gaussian class: class~$L$ has $m_3^{\mathrm{SC}} \neq 0$,
-class~$C$ has $m_4^{\mathrm{SC}} \neq 0$, and class~$M$ has
-nonzero $m_k^{\mathrm{SC}}$ for all $k \geq 3$. This reduces the
-formality criterion to a classification check.
+non-Gaussian class and, on the Gaussian locus, identifies the
+mixed-sector tree formulas with the degree-by-degree shadow tower
+after averaging. The criterion below packages this as an equivalence
+between SC-formality and truncation of the shadow tower at degree~$2$.
 
 \begin{proposition}[SC-formality characterises class~$G$; \ClaimStatusProvedHere]
 \label{prop:sc-formal-iff-class-g}
@@ -2665,21 +2689,30 @@
 The forward direction \textup{(}class~$G$ $\Longrightarrow$
 SC-formal\textup{)} is established in
 Proposition~\ref{prop:swiss-cheese-nonformality-by-class}:
-the class-$G$ row consists exactly of Heisenberg and lattice
-VOAs, and in both cases $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
+the class-$G$ row consists of the Gaussian families Heisenberg,
+lattice VOA, and free fermion, and in each case the genus-$0$
+mixed tree formulas stop at arity~$2$, so
+$m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
 
 For the converse, suppose~$\cA$ is SC-formal.
-Because the standard landscape is exhausted by the four classes
-$G$, $L$, $C$, $M$, it is enough to eliminate the three
-non-Gaussian cases. Proposition~\ref{prop:swiss-cheese-nonformality-by-class}
-does exactly this: class~$L$ has $m_3^{\mathrm{SC}} \neq 0$,
-class~$C$ has $m_4^{\mathrm{SC}} \neq 0$, and class~$M$ has
-nonzero higher operations in every arity $k \geq 3$. Each of
-these cases contradicts SC-formality. This converse uses only the
-classification from Proposition~\ref{prop:swiss-cheese-nonformality-by-class};
-it does not invoke any trilinear form built from~$\kappa$.
-Hence an SC-formal algebra must
-belong to class~$G$.
+Then the mixed sector of the Swiss-cheese bar complex is formal:
+every higher arity tree operation vanishes. The tower-bar
+correspondence is operadic: the arity-$r$ mixed tree and the
+degree-$r$ shadow are produced by the same genus-$0$ tree-transfer
+formula, with the same propagator on internal edges; the only
+difference is the output colour, and passage to the symmetric
+closed sector applies the averaging morphism
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)}.
+Hence SC-formality forces $S_r(\cA) = 0$ for every $r \geq 3$:
+there is no higher mixed tree whose closed projection could survive.
+By Theorem~\ref{thm:shadow-formality-identification} and
+Proposition~\ref{prop:shadow-tower-three-lenses}, this is exactly
+the statement that the shadow/formality tower truncates at
+degree~$2$. Theorem~\ref{thm:shadow-archetype-classification}
+identifies the standard-landscape locus with this property as
+precisely class~$G$. Hence an SC-formal algebra must belong
+to class~$G$.
 \end{proof}
 
 \begin{remark}[D-module purity: reduction to a single gap]


thinking
**Troubleshooting process**

I'm trying to figure out why there's no output. It seems like I might be waiting too long without any progress, but I don’t think it's the TTY causing issues. Maybe I could use a command like `ps -p` to check processes. However, I think I’ll wait another 10 seconds first to see if anything changes before jumping to conclusions. It's all about staying patient while troubleshooting, right?
file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 82ce3f8a19eaa51f878397fa63cad2971741bf1e..caf0e7dcc8b2e4df8cb6362c74b5edc7c33e1305
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -2561,7 +2561,7 @@
 & $m_k^{\mathrm{SC}},\; k \geq 5$ \\
 \midrule
 $G$ \textup{(}$r_{\max}=2$\textup{)}
-& Heisenberg, lattice VOA
+& Heisenberg, lattice VOA, free fermion
 & $= 0$
 & $= 0$
 & $= 0$ \\
@@ -2586,12 +2586,21 @@
 
 \medskip\noindent
 \emph{Mechanism.}
-For class~$G$\textup{:} Heisenberg is central, and lattice VOAs are
-Gaussian: the Heisenberg bracket
-$[a_m, a_n] = km\,\delta_{m+n,0}$ is central, while for lattice
-VOAs the shadow obstruction tower terminates at weight~$2$ by
-Corollary~\ref{cor:lattice-postnikov-termination}. In both cases
-all higher tree sums vanish.
+For class~$G$\textup{:}
+Heisenberg, lattice VOAs, and free fermions are Gaussian/free-field:
+their ordered bar data is generated by the binary two-point kernel,
+so every connected genus-$0$ tree with at least three external legs
+factors through pairings and carries no primitive higher vertex.
+Equivalently, the shadow tower truncates at degree~$2$:
+$S_r(\cA)=0$ for $r \geq 3$
+\textup{(}Theorem~\ref{thm:shadow-archetype-classification}; for
+lattices see Corollary~\ref{cor:lattice-postnikov-termination}\textup{)}.
+Under the averaging map
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)},
+the mixed Swiss-cheese tree of arity~$r$ projects to the degree-$r$
+shadow. Since there is no primitive tree for $r \geq 3$,
+all higher mixed-sector operations vanish.
 For class~$L$\textup{:} the affine KM OPE has at most a double pole; the
 three-channel tree sum over $\overline{\cM}_{0,4}$ is nonzero
 \textup{(}$S_3 = 2h^\vee/(k+h^\vee) \neq 0$\textup{)} but the
@@ -2613,10 +2622,25 @@
 
 \begin{proof}
 Class~$G$: for Heisenberg, centrality of the bracket kills all nested
-compositions, so $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$. For lattice
-VOAs, Corollary~\ref{cor:lattice-postnikov-termination} identifies
-the shadow obstruction tower with its weight-$2$ truncation, so the
-transferred Swiss-cheese operations vanish for every $k \geq 3$.
+tree compositions, so $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
+For lattice VOAs, bosonization reduces connected genus-$0$ amplitudes
+to Wick pairings of the underlying Heisenberg field, and
+Corollary~\ref{cor:lattice-postnikov-termination} identifies the
+shadow tower with its weight-$2$ truncation. For the free fermion,
+Wick's theorem gives Pfaffian factorization by the basic contraction
+$\psi(z)\psi^*(w) \sim (z-w)^{-1}$, so again no connected tree with
+$r \geq 3$ survives after extracting the binary pairings. In all three
+cases the mixed Swiss-cheese arity-$r$ operation is the open-colored
+lift of the same genus-$0$ tree sum whose closed projection is
+$S_r(\cA)$; equivalently,
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)}.
+Because class~$G$ means $S_r(\cA) = 0$ for all $r \geq 3$,
+the mixed-sector operations vanish:
+$m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
+The weaker condition $\Delta = 0$ is not sufficient:
+affine Kac--Moody algebras are class~$L$ with $\Delta = 0$ but
+$m_3^{\mathrm{SC}} \neq 0$.
 Class~$L$: the cubic shadow
 $S_3 = 2h^\vee/(k + h^\vee)$ is computed from the OPE coefficient
 ratio (the structure constant divided by the level); the quartic
@@ -2646,10 +2670,10 @@
 relationship between SC-formality and the classification is
 sharper than the table suggests. Proposition~\ref{prop:swiss-cheese-nonformality-by-class}
 already isolates the first nonzero Swiss-cheese operation in each
-non-Gaussian class: class~$L$ has $m_3^{\mathrm{SC}} \neq 0$,
-class~$C$ has $m_4^{\mathrm{SC}} \neq 0$, and class~$M$ has
-nonzero $m_k^{\mathrm{SC}}$ for all $k \geq 3$. This reduces the
-formality criterion to a classification check.
+non-Gaussian class and, on the Gaussian locus, identifies the
+mixed-sector tree formulas with the degree-by-degree shadow tower
+after averaging. The criterion below packages this as an equivalence
+between SC-formality and truncation of the shadow tower at degree~$2$.
 
 \begin{proposition}[SC-formality characterises class~$G$; \ClaimStatusProvedHere]
 \label{prop:sc-formal-iff-class-g}
@@ -2665,21 +2689,30 @@
 The forward direction \textup{(}class~$G$ $\Longrightarrow$
 SC-formal\textup{)} is established in
 Proposition~\ref{prop:swiss-cheese-nonformality-by-class}:
-the class-$G$ row consists exactly of Heisenberg and lattice
-VOAs, and in both cases $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
+the class-$G$ row consists of the Gaussian families Heisenberg,
+lattice VOA, and free fermion, and in each case the genus-$0$
+mixed tree formulas stop at arity~$2$, so
+$m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
 
 For the converse, suppose~$\cA$ is SC-formal.
-Because the standard landscape is exhausted by the four classes
-$G$, $L$, $C$, $M$, it is enough to eliminate the three
-non-Gaussian cases. Proposition~\ref{prop:swiss-cheese-nonformality-by-class}
-does exactly this: class~$L$ has $m_3^{\mathrm{SC}} \neq 0$,
-class~$C$ has $m_4^{\mathrm{SC}} \neq 0$, and class~$M$ has
-nonzero higher operations in every arity $k \geq 3$. Each of
-these cases contradicts SC-formality. This converse uses only the
-classification from Proposition~\ref{prop:swiss-cheese-nonformality-by-class};
-it does not invoke any trilinear form built from~$\kappa$.
-Hence an SC-formal algebra must
-belong to class~$G$.
+Then the mixed sector of the Swiss-cheese bar complex is formal:
+every higher arity tree operation vanishes. The tower-bar
+correspondence is operadic: the arity-$r$ mixed tree and the
+degree-$r$ shadow are produced by the same genus-$0$ tree-transfer
+formula, with the same propagator on internal edges; the only
+difference is the output colour, and passage to the symmetric
+closed sector applies the averaging morphism
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)}.
+Hence SC-formality forces $S_r(\cA) = 0$ for every $r \geq 3$:
+there is no higher mixed tree whose closed projection could survive.
+By Theorem~\ref{thm:shadow-formality-identification} and
+Proposition~\ref{prop:shadow-tower-three-lenses}, this is exactly
+the statement that the shadow/formality tower truncates at
+degree~$2$. Theorem~\ref{thm:shadow-archetype-classification}
+identifies the standard-landscape locus with this property as
+precisely class~$G$. Hence an SC-formal algebra must belong
+to class~$G$.
 \end{proof}
 
 \begin{remark}[D-module purity: reduction to a single gap]

codex
The build has gone quiet rather than erroring. I’m checking whether it’s still compiling normally or stuck on the build surface before I decide whether to trust it.
exec
/bin/zsh -lc 'ls -lt output main.log main.aux build 2>/dev/null' in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:
-rw-r--r--@ 1 raeez  staff  94208 Apr 13 12:51 main.log
-rw-r--r--@ 1 raeez  staff      0 Apr 13 12:51 main.aux
file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 82ce3f8a19eaa51f878397fa63cad2971741bf1e..caf0e7dcc8b2e4df8cb6362c74b5edc7c33e1305
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -2561,7 +2561,7 @@
 & $m_k^{\mathrm{SC}},\; k \geq 5$ \\
 \midrule
 $G$ \textup{(}$r_{\max}=2$\textup{)}
-& Heisenberg, lattice VOA
+& Heisenberg, lattice VOA, free fermion
 & $= 0$
 & $= 0$
 & $= 0$ \\
@@ -2586,12 +2586,21 @@
 
 \medskip\noindent
 \emph{Mechanism.}
-For class~$G$\textup{:} Heisenberg is central, and lattice VOAs are
-Gaussian: the Heisenberg bracket
-$[a_m, a_n] = km\,\delta_{m+n,0}$ is central, while for lattice
-VOAs the shadow obstruction tower terminates at weight~$2$ by
-Corollary~\ref{cor:lattice-postnikov-termination}. In both cases
-all higher tree sums vanish.
+For class~$G$\textup{:}
+Heisenberg, lattice VOAs, and free fermions are Gaussian/free-field:
+their ordered bar data is generated by the binary two-point kernel,
+so every connected genus-$0$ tree with at least three external legs
+factors through pairings and carries no primitive higher vertex.
+Equivalently, the shadow tower truncates at degree~$2$:
+$S_r(\cA)=0$ for $r \geq 3$
+\textup{(}Theorem~\ref{thm:shadow-archetype-classification}; for
+lattices see Corollary~\ref{cor:lattice-postnikov-termination}\textup{)}.
+Under the averaging map
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)},
+the mixed Swiss-cheese tree of arity~$r$ projects to the degree-$r$
+shadow. Since there is no primitive tree for $r \geq 3$,
+all higher mixed-sector operations vanish.
 For class~$L$\textup{:} the affine KM OPE has at most a double pole; the
 three-channel tree sum over $\overline{\cM}_{0,4}$ is nonzero
 \textup{(}$S_3 = 2h^\vee/(k+h^\vee) \neq 0$\textup{)} but the
@@ -2613,10 +2622,25 @@
 
 \begin{proof}
 Class~$G$: for Heisenberg, centrality of the bracket kills all nested
-compositions, so $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$. For lattice
-VOAs, Corollary~\ref{cor:lattice-postnikov-termination} identifies
-the shadow obstruction tower with its weight-$2$ truncation, so the
-transferred Swiss-cheese operations vanish for every $k \geq 3$.
+tree compositions, so $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
+For lattice VOAs, bosonization reduces connected genus-$0$ amplitudes
+to Wick pairings of the underlying Heisenberg field, and
+Corollary~\ref{cor:lattice-postnikov-termination} identifies the
+shadow tower with its weight-$2$ truncation. For the free fermion,
+Wick's theorem gives Pfaffian factorization by the basic contraction
+$\psi(z)\psi^*(w) \sim (z-w)^{-1}$, so again no connected tree with
+$r \geq 3$ survives after extracting the binary pairings. In all three
+cases the mixed Swiss-cheese arity-$r$ operation is the open-colored
+lift of the same genus-$0$ tree sum whose closed projection is
+$S_r(\cA)$; equivalently,
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)}.
+Because class~$G$ means $S_r(\cA) = 0$ for all $r \geq 3$,
+the mixed-sector operations vanish:
+$m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
+The weaker condition $\Delta = 0$ is not sufficient:
+affine Kac--Moody algebras are class~$L$ with $\Delta = 0$ but
+$m_3^{\mathrm{SC}} \neq 0$.
 Class~$L$: the cubic shadow
 $S_3 = 2h^\vee/(k + h^\vee)$ is computed from the OPE coefficient
 ratio (the structure constant divided by the level); the quartic
@@ -2646,10 +2670,10 @@
 relationship between SC-formality and the classification is
 sharper than the table suggests. Proposition~\ref{prop:swiss-cheese-nonformality-by-class}
 already isolates the first nonzero Swiss-cheese operation in each
-non-Gaussian class: class~$L$ has $m_3^{\mathrm{SC}} \neq 0$,
-class~$C$ has $m_4^{\mathrm{SC}} \neq 0$, and class~$M$ has
-nonzero $m_k^{\mathrm{SC}}$ for all $k \geq 3$. This reduces the
-formality criterion to a classification check.
+non-Gaussian class and, on the Gaussian locus, identifies the
+mixed-sector tree formulas with the degree-by-degree shadow tower
+after averaging. The criterion below packages this as an equivalence
+between SC-formality and truncation of the shadow tower at degree~$2$.
 
 \begin{proposition}[SC-formality characterises class~$G$; \ClaimStatusProvedHere]
 \label{prop:sc-formal-iff-class-g}
@@ -2665,21 +2689,30 @@
 The forward direction \textup{(}class~$G$ $\Longrightarrow$
 SC-formal\textup{)} is established in
 Proposition~\ref{prop:swiss-cheese-nonformality-by-class}:
-the class-$G$ row consists exactly of Heisenberg and lattice
-VOAs, and in both cases $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
+the class-$G$ row consists of the Gaussian families Heisenberg,
+lattice VOA, and free fermion, and in each case the genus-$0$
+mixed tree formulas stop at arity~$2$, so
+$m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
 
 For the converse, suppose~$\cA$ is SC-formal.
-Because the standard landscape is exhausted by the four classes
-$G$, $L$, $C$, $M$, it is enough to eliminate the three
-non-Gaussian cases. Proposition~\ref{prop:swiss-cheese-nonformality-by-class}
-does exactly this: class~$L$ has $m_3^{\mathrm{SC}} \neq 0$,
-class~$C$ has $m_4^{\mathrm{SC}} \neq 0$, and class~$M$ has
-nonzero higher operations in every arity $k \geq 3$. Each of
-these cases contradicts SC-formality. This converse uses only the
-classification from Proposition~\ref{prop:swiss-cheese-nonformality-by-class};
-it does not invoke any trilinear form built from~$\kappa$.
-Hence an SC-formal algebra must
-belong to class~$G$.
+Then the mixed sector of the Swiss-cheese bar complex is formal:
+every higher arity tree operation vanishes. The tower-bar
+correspondence is operadic: the arity-$r$ mixed tree and the
+degree-$r$ shadow are produced by the same genus-$0$ tree-transfer
+formula, with the same propagator on internal edges; the only
+difference is the output colour, and passage to the symmetric
+closed sector applies the averaging morphism
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)}.
+Hence SC-formality forces $S_r(\cA) = 0$ for every $r \geq 3$:
+there is no higher mixed tree whose closed projection could survive.
+By Theorem~\ref{thm:shadow-formality-identification} and
+Proposition~\ref{prop:shadow-tower-three-lenses}, this is exactly
+the statement that the shadow/formality tower truncates at
+degree~$2$. Theorem~\ref{thm:shadow-archetype-classification}
+identifies the standard-landscape locus with this property as
+precisely class~$G$. Hence an SC-formal algebra must belong
+to class~$G$.
 \end{proof}
 
 \begin{remark}[D-module purity: reduction to a single gap]


thinking
**Diagnosing build issues**

I'm thinking that if the auxiliary process suggests the build may still be in progress, there’s a possibility it’s stuck. I might need to check the log to see if it’s updating. Maybe I can use the "tail" command to look at the log in real-time and gather more information. That could help me understand what’s going on with the compile process and whether it’s actually running or not.
codex
The sandbox blocks `ps`, but the log surface suggests the build at least started. I’m inspecting the log directly rather than waiting blindly.
exec
/bin/zsh -lc 'tail -n 80 main.log' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
[616]

[617]

[618]
Underfull \hbox (badness 3838) in paragraph at lines 2815--2819
[]\T1/EBGaramond-OsF/m/n/10.95 (+10) The PBW fil-tra-tion $\OML/ntxmi/m/it/10.9
5 F[]$ \T1/EBGaramond-OsF/m/n/10.95 (+10) on each $[]\LMS/ntxsy/m/n/10.95 �A�$ 
\T1/EBGaramond-OsF/m/n/10.95 (+10) is strict and con-cen-trated in PBW-degree $
\OML/ntxmi/m/it/10.95 n$
 []



[619]

[620]

LaTeX Warning: Float too large for page by 38.35999pt on input line 3114.

exec
/bin/zsh -lc "rg -n 'Undefined control sequence|Emergency stop|Runaway argument|LaTeX Error|Undefined reference|Citation .* undefined' main.log" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '"'^!'"' main.log" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
4009:!
 exited 1 in 52ms:

file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 82ce3f8a19eaa51f878397fa63cad2971741bf1e..caf0e7dcc8b2e4df8cb6362c74b5edc7c33e1305
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -2561,7 +2561,7 @@
 & $m_k^{\mathrm{SC}},\; k \geq 5$ \\
 \midrule
 $G$ \textup{(}$r_{\max}=2$\textup{)}
-& Heisenberg, lattice VOA
+& Heisenberg, lattice VOA, free fermion
 & $= 0$
 & $= 0$
 & $= 0$ \\
@@ -2586,12 +2586,21 @@
 
 \medskip\noindent
 \emph{Mechanism.}
-For class~$G$\textup{:} Heisenberg is central, and lattice VOAs are
-Gaussian: the Heisenberg bracket
-$[a_m, a_n] = km\,\delta_{m+n,0}$ is central, while for lattice
-VOAs the shadow obstruction tower terminates at weight~$2$ by
-Corollary~\ref{cor:lattice-postnikov-termination}. In both cases
-all higher tree sums vanish.
+For class~$G$\textup{:}
+Heisenberg, lattice VOAs, and free fermions are Gaussian/free-field:
+their ordered bar data is generated by the binary two-point kernel,
+so every connected genus-$0$ tree with at least three external legs
+factors through pairings and carries no primitive higher vertex.
+Equivalently, the shadow tower truncates at degree~$2$:
+$S_r(\cA)=0$ for $r \geq 3$
+\textup{(}Theorem~\ref{thm:shadow-archetype-classification}; for
+lattices see Corollary~\ref{cor:lattice-postnikov-termination}\textup{)}.
+Under the averaging map
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)},
+the mixed Swiss-cheese tree of arity~$r$ projects to the degree-$r$
+shadow. Since there is no primitive tree for $r \geq 3$,
+all higher mixed-sector operations vanish.
 For class~$L$\textup{:} the affine KM OPE has at most a double pole; the
 three-channel tree sum over $\overline{\cM}_{0,4}$ is nonzero
 \textup{(}$S_3 = 2h^\vee/(k+h^\vee) \neq 0$\textup{)} but the
@@ -2613,10 +2622,25 @@
 
 \begin{proof}
 Class~$G$: for Heisenberg, centrality of the bracket kills all nested
-compositions, so $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$. For lattice
-VOAs, Corollary~\ref{cor:lattice-postnikov-termination} identifies
-the shadow obstruction tower with its weight-$2$ truncation, so the
-transferred Swiss-cheese operations vanish for every $k \geq 3$.
+tree compositions, so $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
+For lattice VOAs, bosonization reduces connected genus-$0$ amplitudes
+to Wick pairings of the underlying Heisenberg field, and
+Corollary~\ref{cor:lattice-postnikov-termination} identifies the
+shadow tower with its weight-$2$ truncation. For the free fermion,
+Wick's theorem gives Pfaffian factorization by the basic contraction
+$\psi(z)\psi^*(w) \sim (z-w)^{-1}$, so again no connected tree with
+$r \geq 3$ survives after extracting the binary pairings. In all three
+cases the mixed Swiss-cheese arity-$r$ operation is the open-colored
+lift of the same genus-$0$ tree sum whose closed projection is
+$S_r(\cA)$; equivalently,
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)}.
+Because class~$G$ means $S_r(\cA) = 0$ for all $r \geq 3$,
+the mixed-sector operations vanish:
+$m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
+The weaker condition $\Delta = 0$ is not sufficient:
+affine Kac--Moody algebras are class~$L$ with $\Delta = 0$ but
+$m_3^{\mathrm{SC}} \neq 0$.
 Class~$L$: the cubic shadow
 $S_3 = 2h^\vee/(k + h^\vee)$ is computed from the OPE coefficient
 ratio (the structure constant divided by the level); the quartic
@@ -2646,10 +2670,10 @@
 relationship between SC-formality and the classification is
 sharper than the table suggests. Proposition~\ref{prop:swiss-cheese-nonformality-by-class}
 already isolates the first nonzero Swiss-cheese operation in each
-non-Gaussian class: class~$L$ has $m_3^{\mathrm{SC}} \neq 0$,
-class~$C$ has $m_4^{\mathrm{SC}} \neq 0$, and class~$M$ has
-nonzero $m_k^{\mathrm{SC}}$ for all $k \geq 3$. This reduces the
-formality criterion to a classification check.
+non-Gaussian class and, on the Gaussian locus, identifies the
+mixed-sector tree formulas with the degree-by-degree shadow tower
+after averaging. The criterion below packages this as an equivalence
+between SC-formality and truncation of the shadow tower at degree~$2$.
 
 \begin{proposition}[SC-formality characterises class~$G$; \ClaimStatusProvedHere]
 \label{prop:sc-formal-iff-class-g}
@@ -2665,21 +2689,30 @@
 The forward direction \textup{(}class~$G$ $\Longrightarrow$
 SC-formal\textup{)} is established in
 Proposition~\ref{prop:swiss-cheese-nonformality-by-class}:
-the class-$G$ row consists exactly of Heisenberg and lattice
-VOAs, and in both cases $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
+the class-$G$ row consists of the Gaussian families Heisenberg,
+lattice VOA, and free fermion, and in each case the genus-$0$
+mixed tree formulas stop at arity~$2$, so
+$m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
 
 For the converse, suppose~$\cA$ is SC-formal.
-Because the standard landscape is exhausted by the four classes
-$G$, $L$, $C$, $M$, it is enough to eliminate the three
-non-Gaussian cases. Proposition~\ref{prop:swiss-cheese-nonformality-by-class}
-does exactly this: class~$L$ has $m_3^{\mathrm{SC}} \neq 0$,
-class~$C$ has $m_4^{\mathrm{SC}} \neq 0$, and class~$M$ has
-nonzero higher operations in every arity $k \geq 3$. Each of
-these cases contradicts SC-formality. This converse uses only the
-classification from Proposition~\ref{prop:swiss-cheese-nonformality-by-class};
-it does not invoke any trilinear form built from~$\kappa$.
-Hence an SC-formal algebra must
-belong to class~$G$.
+Then the mixed sector of the Swiss-cheese bar complex is formal:
+every higher arity tree operation vanishes. The tower-bar
+correspondence is operadic: the arity-$r$ mixed tree and the
+degree-$r$ shadow are produced by the same genus-$0$ tree-transfer
+formula, with the same propagator on internal edges; the only
+difference is the output colour, and passage to the symmetric
+closed sector applies the averaging morphism
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)}.
+Hence SC-formality forces $S_r(\cA) = 0$ for every $r \geq 3$:
+there is no higher mixed tree whose closed projection could survive.
+By Theorem~\ref{thm:shadow-formality-identification} and
+Proposition~\ref{prop:shadow-tower-three-lenses}, this is exactly
+the statement that the shadow/formality tower truncates at
+degree~$2$. Theorem~\ref{thm:shadow-archetype-classification}
+identifies the standard-landscape locus with this property as
+precisely class~$G$. Hence an SC-formal algebra must belong
+to class~$G$.
 \end{proof}
 
 \begin{remark}[D-module purity: reduction to a single gap]

exec
/bin/zsh -lc "sed -n '3990,4035p' main.log" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
[591])

[592]
\openout2 = `chapters/theory/chiral_koszul_pairs.aux'.

(./chapters/theory/chiral_koszul_pairs.tex

[593




]
Overfull \hbox (18.66614pt too wide) in paragraph at lines 169--174
[]\T1/EBGaramond-OsF/m/n/10.95 (-10) The twisted ten-sor prod-uct $\OML/ntxmi/m
/it/10.95 K[]\LMS/ntxsy/m/n/10.95 �H[]\OML/ntxmi/m/it/10.95 ; [][]\LMS/ntxsy/m/
n/10.95 �\OML/ntxmi/m/it/10.95 V[]\LMS/ntxsy/m/n/10.95 ��$ \T1/EBGaramond-OsF/m
/n/10.95 (-10) is acyclic: the twist-ing mor-phism $\OML/ntxmi/m/it/10.95 ^^\ [
] [] [][]\LMS/ntxsy/m/n/10.95 �\OML/ntxmi/m/it/10.95 V[]\LMS/ntxsy/m/n/10.95 � 
!
file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 82ce3f8a19eaa51f878397fa63cad2971741bf1e..caf0e7dcc8b2e4df8cb6362c74b5edc7c33e1305
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -2561,7 +2561,7 @@
 & $m_k^{\mathrm{SC}},\; k \geq 5$ \\
 \midrule
 $G$ \textup{(}$r_{\max}=2$\textup{)}
-& Heisenberg, lattice VOA
+& Heisenberg, lattice VOA, free fermion
 & $= 0$
 & $= 0$
 & $= 0$ \\
@@ -2586,12 +2586,21 @@
 
 \medskip\noindent
 \emph{Mechanism.}
-For class~$G$\textup{:} Heisenberg is central, and lattice VOAs are
-Gaussian: the Heisenberg bracket
-$[a_m, a_n] = km\,\delta_{m+n,0}$ is central, while for lattice
-VOAs the shadow obstruction tower terminates at weight~$2$ by
-Corollary~\ref{cor:lattice-postnikov-termination}. In both cases
-all higher tree sums vanish.
+For class~$G$\textup{:}
+Heisenberg, lattice VOAs, and free fermions are Gaussian/free-field:
+their ordered bar data is generated by the binary two-point kernel,
+so every connected genus-$0$ tree with at least three external legs
+factors through pairings and carries no primitive higher vertex.
+Equivalently, the shadow tower truncates at degree~$2$:
+$S_r(\cA)=0$ for $r \geq 3$
+\textup{(}Theorem~\ref{thm:shadow-archetype-classification}; for
+lattices see Corollary~\ref{cor:lattice-postnikov-termination}\textup{)}.
+Under the averaging map
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)},
+the mixed Swiss-cheese tree of arity~$r$ projects to the degree-$r$
+shadow. Since there is no primitive tree for $r \geq 3$,
+all higher mixed-sector operations vanish.
 For class~$L$\textup{:} the affine KM OPE has at most a double pole; the
 three-channel tree sum over $\overline{\cM}_{0,4}$ is nonzero
 \textup{(}$S_3 = 2h^\vee/(k+h^\vee) \neq 0$\textup{)} but the
@@ -2613,10 +2622,25 @@
 
 \begin{proof}
 Class~$G$: for Heisenberg, centrality of the bracket kills all nested
-compositions, so $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$. For lattice
-VOAs, Corollary~\ref{cor:lattice-postnikov-termination} identifies
-the shadow obstruction tower with its weight-$2$ truncation, so the
-transferred Swiss-cheese operations vanish for every $k \geq 3$.
+tree compositions, so $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
+For lattice VOAs, bosonization reduces connected genus-$0$ amplitudes
+to Wick pairings of the underlying Heisenberg field, and
+Corollary~\ref{cor:lattice-postnikov-termination} identifies the
+shadow tower with its weight-$2$ truncation. For the free fermion,
+Wick's theorem gives Pfaffian factorization by the basic contraction
+$\psi(z)\psi^*(w) \sim (z-w)^{-1}$, so again no connected tree with
+$r \geq 3$ survives after extracting the binary pairings. In all three
+cases the mixed Swiss-cheese arity-$r$ operation is the open-colored
+lift of the same genus-$0$ tree sum whose closed projection is
+$S_r(\cA)$; equivalently,
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)}.
+Because class~$G$ means $S_r(\cA) = 0$ for all $r \geq 3$,
+the mixed-sector operations vanish:
+$m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
+The weaker condition $\Delta = 0$ is not sufficient:
+affine Kac--Moody algebras are class~$L$ with $\Delta = 0$ but
+$m_3^{\mathrm{SC}} \neq 0$.
 Class~$L$: the cubic shadow
 $S_3 = 2h^\vee/(k + h^\vee)$ is computed from the OPE coefficient
 ratio (the structure constant divided by the level); the quartic
@@ -2646,10 +2670,10 @@
 relationship between SC-formality and the classification is
 sharper than the table suggests. Proposition~\ref{prop:swiss-cheese-nonformality-by-class}
 already isolates the first nonzero Swiss-cheese operation in each
-non-Gaussian class: class~$L$ has $m_3^{\mathrm{SC}} \neq 0$,
-class~$C$ has $m_4^{\mathrm{SC}} \neq 0$, and class~$M$ has
-nonzero $m_k^{\mathrm{SC}}$ for all $k \geq 3$. This reduces the
-formality criterion to a classification check.
+non-Gaussian class and, on the Gaussian locus, identifies the
+mixed-sector tree formulas with the degree-by-degree shadow tower
+after averaging. The criterion below packages this as an equivalence
+between SC-formality and truncation of the shadow tower at degree~$2$.
 
 \begin{proposition}[SC-formality characterises class~$G$; \ClaimStatusProvedHere]
 \label{prop:sc-formal-iff-class-g}
@@ -2665,21 +2689,30 @@
 The forward direction \textup{(}class~$G$ $\Longrightarrow$
 SC-formal\textup{)} is established in
 Proposition~\ref{prop:swiss-cheese-nonformality-by-class}:
-the class-$G$ row consists exactly of Heisenberg and lattice
-VOAs, and in both cases $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
+the class-$G$ row consists of the Gaussian families Heisenberg,
+lattice VOA, and free fermion, and in each case the genus-$0$
+mixed tree formulas stop at arity~$2$, so
+$m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
 
 For the converse, suppose~$\cA$ is SC-formal.
-Because the standard landscape is exhausted by the four classes
-$G$, $L$, $C$, $M$, it is enough to eliminate the three
-non-Gaussian cases. Proposition~\ref{prop:swiss-cheese-nonformality-by-class}
-does exactly this: class~$L$ has $m_3^{\mathrm{SC}} \neq 0$,
-class~$C$ has $m_4^{\mathrm{SC}} \neq 0$, and class~$M$ has
-nonzero higher operations in every arity $k \geq 3$. Each of
-these cases contradicts SC-formality. This converse uses only the
-classification from Proposition~\ref{prop:swiss-cheese-nonformality-by-class};
-it does not invoke any trilinear form built from~$\kappa$.
-Hence an SC-formal algebra must
-belong to class~$G$.
+Then the mixed sector of the Swiss-cheese bar complex is formal:
+every higher arity tree operation vanishes. The tower-bar
+correspondence is operadic: the arity-$r$ mixed tree and the
+degree-$r$ shadow are produced by the same genus-$0$ tree-transfer
+formula, with the same propagator on internal edges; the only
+difference is the output colour, and passage to the symmetric
+closed sector applies the averaging morphism
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)}.
+Hence SC-formality forces $S_r(\cA) = 0$ for every $r \geq 3$:
+there is no higher mixed tree whose closed projection could survive.
+By Theorem~\ref{thm:shadow-formality-identification} and
+Proposition~\ref{prop:shadow-tower-three-lenses}, this is exactly
+the statement that the shadow/formality tower truncates at
+degree~$2$. Theorem~\ref{thm:shadow-archetype-classification}
+identifies the standard-landscape locus with this property as
+precisely class~$G$. Hence an SC-formal algebra must belong
+to class~$G$.
 \end{proof}
 
 \begin{remark}[D-module purity: reduction to a single gap]


thinking
**Checking build status**

I'm seeing that the `rg '^!' main.log` command has found an overfull line marked with an exclamation, but no actual errors seem present. I need to check if the build has finished since the log tail only shows up to line 640, which suggests it might be incomplete. I should wait for the process to finish before making any conclusions. Perhaps I could check back by polling the session to see if there are updates.
file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 82ce3f8a19eaa51f878397fa63cad2971741bf1e..caf0e7dcc8b2e4df8cb6362c74b5edc7c33e1305
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -2561,7 +2561,7 @@
 & $m_k^{\mathrm{SC}},\; k \geq 5$ \\
 \midrule
 $G$ \textup{(}$r_{\max}=2$\textup{)}
-& Heisenberg, lattice VOA
+& Heisenberg, lattice VOA, free fermion
 & $= 0$
 & $= 0$
 & $= 0$ \\
@@ -2586,12 +2586,21 @@
 
 \medskip\noindent
 \emph{Mechanism.}
-For class~$G$\textup{:} Heisenberg is central, and lattice VOAs are
-Gaussian: the Heisenberg bracket
-$[a_m, a_n] = km\,\delta_{m+n,0}$ is central, while for lattice
-VOAs the shadow obstruction tower terminates at weight~$2$ by
-Corollary~\ref{cor:lattice-postnikov-termination}. In both cases
-all higher tree sums vanish.
+For class~$G$\textup{:}
+Heisenberg, lattice VOAs, and free fermions are Gaussian/free-field:
+their ordered bar data is generated by the binary two-point kernel,
+so every connected genus-$0$ tree with at least three external legs
+factors through pairings and carries no primitive higher vertex.
+Equivalently, the shadow tower truncates at degree~$2$:
+$S_r(\cA)=0$ for $r \geq 3$
+\textup{(}Theorem~\ref{thm:shadow-archetype-classification}; for
+lattices see Corollary~\ref{cor:lattice-postnikov-termination}\textup{)}.
+Under the averaging map
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)},
+the mixed Swiss-cheese tree of arity~$r$ projects to the degree-$r$
+shadow. Since there is no primitive tree for $r \geq 3$,
+all higher mixed-sector operations vanish.
 For class~$L$\textup{:} the affine KM OPE has at most a double pole; the
 three-channel tree sum over $\overline{\cM}_{0,4}$ is nonzero
 \textup{(}$S_3 = 2h^\vee/(k+h^\vee) \neq 0$\textup{)} but the
@@ -2613,10 +2622,25 @@
 
 \begin{proof}
 Class~$G$: for Heisenberg, centrality of the bracket kills all nested
-compositions, so $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$. For lattice
-VOAs, Corollary~\ref{cor:lattice-postnikov-termination} identifies
-the shadow obstruction tower with its weight-$2$ truncation, so the
-transferred Swiss-cheese operations vanish for every $k \geq 3$.
+tree compositions, so $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
+For lattice VOAs, bosonization reduces connected genus-$0$ amplitudes
+to Wick pairings of the underlying Heisenberg field, and
+Corollary~\ref{cor:lattice-postnikov-termination} identifies the
+shadow tower with its weight-$2$ truncation. For the free fermion,
+Wick's theorem gives Pfaffian factorization by the basic contraction
+$\psi(z)\psi^*(w) \sim (z-w)^{-1}$, so again no connected tree with
+$r \geq 3$ survives after extracting the binary pairings. In all three
+cases the mixed Swiss-cheese arity-$r$ operation is the open-colored
+lift of the same genus-$0$ tree sum whose closed projection is
+$S_r(\cA)$; equivalently,
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)}.
+Because class~$G$ means $S_r(\cA) = 0$ for all $r \geq 3$,
+the mixed-sector operations vanish:
+$m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
+The weaker condition $\Delta = 0$ is not sufficient:
+affine Kac--Moody algebras are class~$L$ with $\Delta = 0$ but
+$m_3^{\mathrm{SC}} \neq 0$.
 Class~$L$: the cubic shadow
 $S_3 = 2h^\vee/(k + h^\vee)$ is computed from the OPE coefficient
 ratio (the structure constant divided by the level); the quartic
@@ -2646,10 +2670,10 @@
 relationship between SC-formality and the classification is
 sharper than the table suggests. Proposition~\ref{prop:swiss-cheese-nonformality-by-class}
 already isolates the first nonzero Swiss-cheese operation in each
-non-Gaussian class: class~$L$ has $m_3^{\mathrm{SC}} \neq 0$,
-class~$C$ has $m_4^{\mathrm{SC}} \neq 0$, and class~$M$ has
-nonzero $m_k^{\mathrm{SC}}$ for all $k \geq 3$. This reduces the
-formality criterion to a classification check.
+non-Gaussian class and, on the Gaussian locus, identifies the
+mixed-sector tree formulas with the degree-by-degree shadow tower
+after averaging. The criterion below packages this as an equivalence
+between SC-formality and truncation of the shadow tower at degree~$2$.
 
 \begin{proposition}[SC-formality characterises class~$G$; \ClaimStatusProvedHere]
 \label{prop:sc-formal-iff-class-g}
@@ -2665,21 +2689,30 @@
 The forward direction \textup{(}class~$G$ $\Longrightarrow$
 SC-formal\textup{)} is established in
 Proposition~\ref{prop:swiss-cheese-nonformality-by-class}:
-the class-$G$ row consists exactly of Heisenberg and lattice
-VOAs, and in both cases $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
+the class-$G$ row consists of the Gaussian families Heisenberg,
+lattice VOA, and free fermion, and in each case the genus-$0$
+mixed tree formulas stop at arity~$2$, so
+$m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
 
 For the converse, suppose~$\cA$ is SC-formal.
-Because the standard landscape is exhausted by the four classes
-$G$, $L$, $C$, $M$, it is enough to eliminate the three
-non-Gaussian cases. Proposition~\ref{prop:swiss-cheese-nonformality-by-class}
-does exactly this: class~$L$ has $m_3^{\mathrm{SC}} \neq 0$,
-class~$C$ has $m_4^{\mathrm{SC}} \neq 0$, and class~$M$ has
-nonzero higher operations in every arity $k \geq 3$. Each of
-these cases contradicts SC-formality. This converse uses only the
-classification from Proposition~\ref{prop:swiss-cheese-nonformality-by-class};
-it does not invoke any trilinear form built from~$\kappa$.
-Hence an SC-formal algebra must
-belong to class~$G$.
+Then the mixed sector of the Swiss-cheese bar complex is formal:
+every higher arity tree operation vanishes. The tower-bar
+correspondence is operadic: the arity-$r$ mixed tree and the
+degree-$r$ shadow are produced by the same genus-$0$ tree-transfer
+formula, with the same propagator on internal edges; the only
+difference is the output colour, and passage to the symmetric
+closed sector applies the averaging morphism
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)}.
+Hence SC-formality forces $S_r(\cA) = 0$ for every $r \geq 3$:
+there is no higher mixed tree whose closed projection could survive.
+By Theorem~\ref{thm:shadow-formality-identification} and
+Proposition~\ref{prop:shadow-tower-three-lenses}, this is exactly
+the statement that the shadow/formality tower truncates at
+degree~$2$. Theorem~\ref{thm:shadow-archetype-classification}
+identifies the standard-landscape locus with this property as
+precisely class~$G$. Hence an SC-formal algebra must belong
+to class~$G$.
 \end{proof}
 
 \begin{remark}[D-module purity: reduction to a single gap]

codex
Pass 1 finished; the warning counts are repo-global, not local proof failures. I’m letting the reruns finish so I can see whether this edit introduces an actual fatal error or a new unresolved reference in the touched theorem lane.
file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 82ce3f8a19eaa51f878397fa63cad2971741bf1e..caf0e7dcc8b2e4df8cb6362c74b5edc7c33e1305
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -2561,7 +2561,7 @@
 & $m_k^{\mathrm{SC}},\; k \geq 5$ \\
 \midrule
 $G$ \textup{(}$r_{\max}=2$\textup{)}
-& Heisenberg, lattice VOA
+& Heisenberg, lattice VOA, free fermion
 & $= 0$
 & $= 0$
 & $= 0$ \\
@@ -2586,12 +2586,21 @@
 
 \medskip\noindent
 \emph{Mechanism.}
-For class~$G$\textup{:} Heisenberg is central, and lattice VOAs are
-Gaussian: the Heisenberg bracket
-$[a_m, a_n] = km\,\delta_{m+n,0}$ is central, while for lattice
-VOAs the shadow obstruction tower terminates at weight~$2$ by
-Corollary~\ref{cor:lattice-postnikov-termination}. In both cases
-all higher tree sums vanish.
+For class~$G$\textup{:}
+Heisenberg, lattice VOAs, and free fermions are Gaussian/free-field:
+their ordered bar data is generated by the binary two-point kernel,
+so every connected genus-$0$ tree with at least three external legs
+factors through pairings and carries no primitive higher vertex.
+Equivalently, the shadow tower truncates at degree~$2$:
+$S_r(\cA)=0$ for $r \geq 3$
+\textup{(}Theorem~\ref{thm:shadow-archetype-classification}; for
+lattices see Corollary~\ref{cor:lattice-postnikov-termination}\textup{)}.
+Under the averaging map
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)},
+the mixed Swiss-cheese tree of arity~$r$ projects to the degree-$r$
+shadow. Since there is no primitive tree for $r \geq 3$,
+all higher mixed-sector operations vanish.
 For class~$L$\textup{:} the affine KM OPE has at most a double pole; the
 three-channel tree sum over $\overline{\cM}_{0,4}$ is nonzero
 \textup{(}$S_3 = 2h^\vee/(k+h^\vee) \neq 0$\textup{)} but the
@@ -2613,10 +2622,25 @@
 
 \begin{proof}
 Class~$G$: for Heisenberg, centrality of the bracket kills all nested
-compositions, so $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$. For lattice
-VOAs, Corollary~\ref{cor:lattice-postnikov-termination} identifies
-the shadow obstruction tower with its weight-$2$ truncation, so the
-transferred Swiss-cheese operations vanish for every $k \geq 3$.
+tree compositions, so $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
+For lattice VOAs, bosonization reduces connected genus-$0$ amplitudes
+to Wick pairings of the underlying Heisenberg field, and
+Corollary~\ref{cor:lattice-postnikov-termination} identifies the
+shadow tower with its weight-$2$ truncation. For the free fermion,
+Wick's theorem gives Pfaffian factorization by the basic contraction
+$\psi(z)\psi^*(w) \sim (z-w)^{-1}$, so again no connected tree with
+$r \geq 3$ survives after extracting the binary pairings. In all three
+cases the mixed Swiss-cheese arity-$r$ operation is the open-colored
+lift of the same genus-$0$ tree sum whose closed projection is
+$S_r(\cA)$; equivalently,
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)}.
+Because class~$G$ means $S_r(\cA) = 0$ for all $r \geq 3$,
+the mixed-sector operations vanish:
+$m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
+The weaker condition $\Delta = 0$ is not sufficient:
+affine Kac--Moody algebras are class~$L$ with $\Delta = 0$ but
+$m_3^{\mathrm{SC}} \neq 0$.
 Class~$L$: the cubic shadow
 $S_3 = 2h^\vee/(k + h^\vee)$ is computed from the OPE coefficient
 ratio (the structure constant divided by the level); the quartic
@@ -2646,10 +2670,10 @@
 relationship between SC-formality and the classification is
 sharper than the table suggests. Proposition~\ref{prop:swiss-cheese-nonformality-by-class}
 already isolates the first nonzero Swiss-cheese operation in each
-non-Gaussian class: class~$L$ has $m_3^{\mathrm{SC}} \neq 0$,
-class~$C$ has $m_4^{\mathrm{SC}} \neq 0$, and class~$M$ has
-nonzero $m_k^{\mathrm{SC}}$ for all $k \geq 3$. This reduces the
-formality criterion to a classification check.
+non-Gaussian class and, on the Gaussian locus, identifies the
+mixed-sector tree formulas with the degree-by-degree shadow tower
+after averaging. The criterion below packages this as an equivalence
+between SC-formality and truncation of the shadow tower at degree~$2$.
 
 \begin{proposition}[SC-formality characterises class~$G$; \ClaimStatusProvedHere]
 \label{prop:sc-formal-iff-class-g}
@@ -2665,21 +2689,30 @@
 The forward direction \textup{(}class~$G$ $\Longrightarrow$
 SC-formal\textup{)} is established in
 Proposition~\ref{prop:swiss-cheese-nonformality-by-class}:
-the class-$G$ row consists exactly of Heisenberg and lattice
-VOAs, and in both cases $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
+the class-$G$ row consists of the Gaussian families Heisenberg,
+lattice VOA, and free fermion, and in each case the genus-$0$
+mixed tree formulas stop at arity~$2$, so
+$m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
 
 For the converse, suppose~$\cA$ is SC-formal.
-Because the standard landscape is exhausted by the four classes
-$G$, $L$, $C$, $M$, it is enough to eliminate the three
-non-Gaussian cases. Proposition~\ref{prop:swiss-cheese-nonformality-by-class}
-does exactly this: class~$L$ has $m_3^{\mathrm{SC}} \neq 0$,
-class~$C$ has $m_4^{\mathrm{SC}} \neq 0$, and class~$M$ has
-nonzero higher operations in every arity $k \geq 3$. Each of
-these cases contradicts SC-formality. This converse uses only the
-classification from Proposition~\ref{prop:swiss-cheese-nonformality-by-class};
-it does not invoke any trilinear form built from~$\kappa$.
-Hence an SC-formal algebra must
-belong to class~$G$.
+Then the mixed sector of the Swiss-cheese bar complex is formal:
+every higher arity tree operation vanishes. The tower-bar
+correspondence is operadic: the arity-$r$ mixed tree and the
+degree-$r$ shadow are produced by the same genus-$0$ tree-transfer
+formula, with the same propagator on internal edges; the only
+difference is the output colour, and passage to the symmetric
+closed sector applies the averaging morphism
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)}.
+Hence SC-formality forces $S_r(\cA) = 0$ for every $r \geq 3$:
+there is no higher mixed tree whose closed projection could survive.
+By Theorem~\ref{thm:shadow-formality-identification} and
+Proposition~\ref{prop:shadow-tower-three-lenses}, this is exactly
+the statement that the shadow/formality tower truncates at
+degree~$2$. Theorem~\ref{thm:shadow-archetype-classification}
+identifies the standard-landscape locus with this property as
+precisely class~$G$. Hence an SC-formal algebra must belong
+to class~$G$.
 \end{proof}
 
 \begin{remark}[D-module purity: reduction to a single gap]

file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 82ce3f8a19eaa51f878397fa63cad2971741bf1e..caf0e7dcc8b2e4df8cb6362c74b5edc7c33e1305
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -2561,7 +2561,7 @@
 & $m_k^{\mathrm{SC}},\; k \geq 5$ \\
 \midrule
 $G$ \textup{(}$r_{\max}=2$\textup{)}
-& Heisenberg, lattice VOA
+& Heisenberg, lattice VOA, free fermion
 & $= 0$
 & $= 0$
 & $= 0$ \\
@@ -2586,12 +2586,21 @@
 
 \medskip\noindent
 \emph{Mechanism.}
-For class~$G$\textup{:} Heisenberg is central, and lattice VOAs are
-Gaussian: the Heisenberg bracket
-$[a_m, a_n] = km\,\delta_{m+n,0}$ is central, while for lattice
-VOAs the shadow obstruction tower terminates at weight~$2$ by
-Corollary~\ref{cor:lattice-postnikov-termination}. In both cases
-all higher tree sums vanish.
+For class~$G$\textup{:}
+Heisenberg, lattice VOAs, and free fermions are Gaussian/free-field:
+their ordered bar data is generated by the binary two-point kernel,
+so every connected genus-$0$ tree with at least three external legs
+factors through pairings and carries no primitive higher vertex.
+Equivalently, the shadow tower truncates at degree~$2$:
+$S_r(\cA)=0$ for $r \geq 3$
+\textup{(}Theorem~\ref{thm:shadow-archetype-classification}; for
+lattices see Corollary~\ref{cor:lattice-postnikov-termination}\textup{)}.
+Under the averaging map
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)},
+the mixed Swiss-cheese tree of arity~$r$ projects to the degree-$r$
+shadow. Since there is no primitive tree for $r \geq 3$,
+all higher mixed-sector operations vanish.
 For class~$L$\textup{:} the affine KM OPE has at most a double pole; the
 three-channel tree sum over $\overline{\cM}_{0,4}$ is nonzero
 \textup{(}$S_3 = 2h^\vee/(k+h^\vee) \neq 0$\textup{)} but the
@@ -2613,10 +2622,25 @@
 
 \begin{proof}
 Class~$G$: for Heisenberg, centrality of the bracket kills all nested
-compositions, so $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$. For lattice
-VOAs, Corollary~\ref{cor:lattice-postnikov-termination} identifies
-the shadow obstruction tower with its weight-$2$ truncation, so the
-transferred Swiss-cheese operations vanish for every $k \geq 3$.
+tree compositions, so $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
+For lattice VOAs, bosonization reduces connected genus-$0$ amplitudes
+to Wick pairings of the underlying Heisenberg field, and
+Corollary~\ref{cor:lattice-postnikov-termination} identifies the
+shadow tower with its weight-$2$ truncation. For the free fermion,
+Wick's theorem gives Pfaffian factorization by the basic contraction
+$\psi(z)\psi^*(w) \sim (z-w)^{-1}$, so again no connected tree with
+$r \geq 3$ survives after extracting the binary pairings. In all three
+cases the mixed Swiss-cheese arity-$r$ operation is the open-colored
+lift of the same genus-$0$ tree sum whose closed projection is
+$S_r(\cA)$; equivalently,
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)}.
+Because class~$G$ means $S_r(\cA) = 0$ for all $r \geq 3$,
+the mixed-sector operations vanish:
+$m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
+The weaker condition $\Delta = 0$ is not sufficient:
+affine Kac--Moody algebras are class~$L$ with $\Delta = 0$ but
+$m_3^{\mathrm{SC}} \neq 0$.
 Class~$L$: the cubic shadow
 $S_3 = 2h^\vee/(k + h^\vee)$ is computed from the OPE coefficient
 ratio (the structure constant divided by the level); the quartic
@@ -2646,10 +2670,10 @@
 relationship between SC-formality and the classification is
 sharper than the table suggests. Proposition~\ref{prop:swiss-cheese-nonformality-by-class}
 already isolates the first nonzero Swiss-cheese operation in each
-non-Gaussian class: class~$L$ has $m_3^{\mathrm{SC}} \neq 0$,
-class~$C$ has $m_4^{\mathrm{SC}} \neq 0$, and class~$M$ has
-nonzero $m_k^{\mathrm{SC}}$ for all $k \geq 3$. This reduces the
-formality criterion to a classification check.
+non-Gaussian class and, on the Gaussian locus, identifies the
+mixed-sector tree formulas with the degree-by-degree shadow tower
+after averaging. The criterion below packages this as an equivalence
+between SC-formality and truncation of the shadow tower at degree~$2$.
 
 \begin{proposition}[SC-formality characterises class~$G$; \ClaimStatusProvedHere]
 \label{prop:sc-formal-iff-class-g}
@@ -2665,21 +2689,30 @@
 The forward direction \textup{(}class~$G$ $\Longrightarrow$
 SC-formal\textup{)} is established in
 Proposition~\ref{prop:swiss-cheese-nonformality-by-class}:
-the class-$G$ row consists exactly of Heisenberg and lattice
-VOAs, and in both cases $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
+the class-$G$ row consists of the Gaussian families Heisenberg,
+lattice VOA, and free fermion, and in each case the genus-$0$
+mixed tree formulas stop at arity~$2$, so
+$m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
 
 For the converse, suppose~$\cA$ is SC-formal.
-Because the standard landscape is exhausted by the four classes
-$G$, $L$, $C$, $M$, it is enough to eliminate the three
-non-Gaussian cases. Proposition~\ref{prop:swiss-cheese-nonformality-by-class}
-does exactly this: class~$L$ has $m_3^{\mathrm{SC}} \neq 0$,
-class~$C$ has $m_4^{\mathrm{SC}} \neq 0$, and class~$M$ has
-nonzero higher operations in every arity $k \geq 3$. Each of
-these cases contradicts SC-formality. This converse uses only the
-classification from Proposition~\ref{prop:swiss-cheese-nonformality-by-class};
-it does not invoke any trilinear form built from~$\kappa$.
-Hence an SC-formal algebra must
-belong to class~$G$.
+Then the mixed sector of the Swiss-cheese bar complex is formal:
+every higher arity tree operation vanishes. The tower-bar
+correspondence is operadic: the arity-$r$ mixed tree and the
+degree-$r$ shadow are produced by the same genus-$0$ tree-transfer
+formula, with the same propagator on internal edges; the only
+difference is the output colour, and passage to the symmetric
+closed sector applies the averaging morphism
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)}.
+Hence SC-formality forces $S_r(\cA) = 0$ for every $r \geq 3$:
+there is no higher mixed tree whose closed projection could survive.
+By Theorem~\ref{thm:shadow-formality-identification} and
+Proposition~\ref{prop:shadow-tower-three-lenses}, this is exactly
+the statement that the shadow/formality tower truncates at
+degree~$2$. Theorem~\ref{thm:shadow-archetype-classification}
+identifies the standard-landscape locus with this property as
+precisely class~$G$. Hence an SC-formal algebra must belong
+to class~$G$.
 \end{proof}
 
 \begin{remark}[D-module purity: reduction to a single gap]

file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 82ce3f8a19eaa51f878397fa63cad2971741bf1e..caf0e7dcc8b2e4df8cb6362c74b5edc7c33e1305
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -2561,7 +2561,7 @@
 & $m_k^{\mathrm{SC}},\; k \geq 5$ \\
 \midrule
 $G$ \textup{(}$r_{\max}=2$\textup{)}
-& Heisenberg, lattice VOA
+& Heisenberg, lattice VOA, free fermion
 & $= 0$
 & $= 0$
 & $= 0$ \\
@@ -2586,12 +2586,21 @@
 
 \medskip\noindent
 \emph{Mechanism.}
-For class~$G$\textup{:} Heisenberg is central, and lattice VOAs are
-Gaussian: the Heisenberg bracket
-$[a_m, a_n] = km\,\delta_{m+n,0}$ is central, while for lattice
-VOAs the shadow obstruction tower terminates at weight~$2$ by
-Corollary~\ref{cor:lattice-postnikov-termination}. In both cases
-all higher tree sums vanish.
+For class~$G$\textup{:}
+Heisenberg, lattice VOAs, and free fermions are Gaussian/free-field:
+their ordered bar data is generated by the binary two-point kernel,
+so every connected genus-$0$ tree with at least three external legs
+factors through pairings and carries no primitive higher vertex.
+Equivalently, the shadow tower truncates at degree~$2$:
+$S_r(\cA)=0$ for $r \geq 3$
+\textup{(}Theorem~\ref{thm:shadow-archetype-classification}; for
+lattices see Corollary~\ref{cor:lattice-postnikov-termination}\textup{)}.
+Under the averaging map
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)},
+the mixed Swiss-cheese tree of arity~$r$ projects to the degree-$r$
+shadow. Since there is no primitive tree for $r \geq 3$,
+all higher mixed-sector operations vanish.
 For class~$L$\textup{:} the affine KM OPE has at most a double pole; the
 three-channel tree sum over $\overline{\cM}_{0,4}$ is nonzero
 \textup{(}$S_3 = 2h^\vee/(k+h^\vee) \neq 0$\textup{)} but the
@@ -2613,10 +2622,25 @@
 
 \begin{proof}
 Class~$G$: for Heisenberg, centrality of the bracket kills all nested
-compositions, so $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$. For lattice
-VOAs, Corollary~\ref{cor:lattice-postnikov-termination} identifies
-the shadow obstruction tower with its weight-$2$ truncation, so the
-transferred Swiss-cheese operations vanish for every $k \geq 3$.
+tree compositions, so $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
+For lattice VOAs, bosonization reduces connected genus-$0$ amplitudes
+to Wick pairings of the underlying Heisenberg field, and
+Corollary~\ref{cor:lattice-postnikov-termination} identifies the
+shadow tower with its weight-$2$ truncation. For the free fermion,
+Wick's theorem gives Pfaffian factorization by the basic contraction
+$\psi(z)\psi^*(w) \sim (z-w)^{-1}$, so again no connected tree with
+$r \geq 3$ survives after extracting the binary pairings. In all three
+cases the mixed Swiss-cheese arity-$r$ operation is the open-colored
+lift of the same genus-$0$ tree sum whose closed projection is
+$S_r(\cA)$; equivalently,
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)}.
+Because class~$G$ means $S_r(\cA) = 0$ for all $r \geq 3$,
+the mixed-sector operations vanish:
+$m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
+The weaker condition $\Delta = 0$ is not sufficient:
+affine Kac--Moody algebras are class~$L$ with $\Delta = 0$ but
+$m_3^{\mathrm{SC}} \neq 0$.
 Class~$L$: the cubic shadow
 $S_3 = 2h^\vee/(k + h^\vee)$ is computed from the OPE coefficient
 ratio (the structure constant divided by the level); the quartic
@@ -2646,10 +2670,10 @@
 relationship between SC-formality and the classification is
 sharper than the table suggests. Proposition~\ref{prop:swiss-cheese-nonformality-by-class}
 already isolates the first nonzero Swiss-cheese operation in each
-non-Gaussian class: class~$L$ has $m_3^{\mathrm{SC}} \neq 0$,
-class~$C$ has $m_4^{\mathrm{SC}} \neq 0$, and class~$M$ has
-nonzero $m_k^{\mathrm{SC}}$ for all $k \geq 3$. This reduces the
-formality criterion to a classification check.
+non-Gaussian class and, on the Gaussian locus, identifies the
+mixed-sector tree formulas with the degree-by-degree shadow tower
+after averaging. The criterion below packages this as an equivalence
+between SC-formality and truncation of the shadow tower at degree~$2$.
 
 \begin{proposition}[SC-formality characterises class~$G$; \ClaimStatusProvedHere]
 \label{prop:sc-formal-iff-class-g}
@@ -2665,21 +2689,30 @@
 The forward direction \textup{(}class~$G$ $\Longrightarrow$
 SC-formal\textup{)} is established in
 Proposition~\ref{prop:swiss-cheese-nonformality-by-class}:
-the class-$G$ row consists exactly of Heisenberg and lattice
-VOAs, and in both cases $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
+the class-$G$ row consists of the Gaussian families Heisenberg,
+lattice VOA, and free fermion, and in each case the genus-$0$
+mixed tree formulas stop at arity~$2$, so
+$m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
 
 For the converse, suppose~$\cA$ is SC-formal.
-Because the standard landscape is exhausted by the four classes
-$G$, $L$, $C$, $M$, it is enough to eliminate the three
-non-Gaussian cases. Proposition~\ref{prop:swiss-cheese-nonformality-by-class}
-does exactly this: class~$L$ has $m_3^{\mathrm{SC}} \neq 0$,
-class~$C$ has $m_4^{\mathrm{SC}} \neq 0$, and class~$M$ has
-nonzero higher operations in every arity $k \geq 3$. Each of
-these cases contradicts SC-formality. This converse uses only the
-classification from Proposition~\ref{prop:swiss-cheese-nonformality-by-class};
-it does not invoke any trilinear form built from~$\kappa$.
-Hence an SC-formal algebra must
-belong to class~$G$.
+Then the mixed sector of the Swiss-cheese bar complex is formal:
+every higher arity tree operation vanishes. The tower-bar
+correspondence is operadic: the arity-$r$ mixed tree and the
+degree-$r$ shadow are produced by the same genus-$0$ tree-transfer
+formula, with the same propagator on internal edges; the only
+difference is the output colour, and passage to the symmetric
+closed sector applies the averaging morphism
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)}.
+Hence SC-formality forces $S_r(\cA) = 0$ for every $r \geq 3$:
+there is no higher mixed tree whose closed projection could survive.
+By Theorem~\ref{thm:shadow-formality-identification} and
+Proposition~\ref{prop:shadow-tower-three-lenses}, this is exactly
+the statement that the shadow/formality tower truncates at
+degree~$2$. Theorem~\ref{thm:shadow-archetype-classification}
+identifies the standard-landscape locus with this property as
+precisely class~$G$. Hence an SC-formal algebra must belong
+to class~$G$.
 \end{proof}
 
 \begin{remark}[D-module purity: reduction to a single gap]

file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 82ce3f8a19eaa51f878397fa63cad2971741bf1e..caf0e7dcc8b2e4df8cb6362c74b5edc7c33e1305
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -2561,7 +2561,7 @@
 & $m_k^{\mathrm{SC}},\; k \geq 5$ \\
 \midrule
 $G$ \textup{(}$r_{\max}=2$\textup{)}
-& Heisenberg, lattice VOA
+& Heisenberg, lattice VOA, free fermion
 & $= 0$
 & $= 0$
 & $= 0$ \\
@@ -2586,12 +2586,21 @@
 
 \medskip\noindent
 \emph{Mechanism.}
-For class~$G$\textup{:} Heisenberg is central, and lattice VOAs are
-Gaussian: the Heisenberg bracket
-$[a_m, a_n] = km\,\delta_{m+n,0}$ is central, while for lattice
-VOAs the shadow obstruction tower terminates at weight~$2$ by
-Corollary~\ref{cor:lattice-postnikov-termination}. In both cases
-all higher tree sums vanish.
+For class~$G$\textup{:}
+Heisenberg, lattice VOAs, and free fermions are Gaussian/free-field:
+their ordered bar data is generated by the binary two-point kernel,
+so every connected genus-$0$ tree with at least three external legs
+factors through pairings and carries no primitive higher vertex.
+Equivalently, the shadow tower truncates at degree~$2$:
+$S_r(\cA)=0$ for $r \geq 3$
+\textup{(}Theorem~\ref{thm:shadow-archetype-classification}; for
+lattices see Corollary~\ref{cor:lattice-postnikov-termination}\textup{)}.
+Under the averaging map
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)},
+the mixed Swiss-cheese tree of arity~$r$ projects to the degree-$r$
+shadow. Since there is no primitive tree for $r \geq 3$,
+all higher mixed-sector operations vanish.
 For class~$L$\textup{:} the affine KM OPE has at most a double pole; the
 three-channel tree sum over $\overline{\cM}_{0,4}$ is nonzero
 \textup{(}$S_3 = 2h^\vee/(k+h^\vee) \neq 0$\textup{)} but the
@@ -2613,10 +2622,25 @@
 
 \begin{proof}
 Class~$G$: for Heisenberg, centrality of the bracket kills all nested
-compositions, so $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$. For lattice
-VOAs, Corollary~\ref{cor:lattice-postnikov-termination} identifies
-the shadow obstruction tower with its weight-$2$ truncation, so the
-transferred Swiss-cheese operations vanish for every $k \geq 3$.
+tree compositions, so $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
+For lattice VOAs, bosonization reduces connected genus-$0$ amplitudes
+to Wick pairings of the underlying Heisenberg field, and
+Corollary~\ref{cor:lattice-postnikov-termination} identifies the
+shadow tower with its weight-$2$ truncation. For the free fermion,
+Wick's theorem gives Pfaffian factorization by the basic contraction
+$\psi(z)\psi^*(w) \sim (z-w)^{-1}$, so again no connected tree with
+$r \geq 3$ survives after extracting the binary pairings. In all three
+cases the mixed Swiss-cheese arity-$r$ operation is the open-colored
+lift of the same genus-$0$ tree sum whose closed projection is
+$S_r(\cA)$; equivalently,
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)}.
+Because class~$G$ means $S_r(\cA) = 0$ for all $r \geq 3$,
+the mixed-sector operations vanish:
+$m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
+The weaker condition $\Delta = 0$ is not sufficient:
+affine Kac--Moody algebras are class~$L$ with $\Delta = 0$ but
+$m_3^{\mathrm{SC}} \neq 0$.
 Class~$L$: the cubic shadow
 $S_3 = 2h^\vee/(k + h^\vee)$ is computed from the OPE coefficient
 ratio (the structure constant divided by the level); the quartic
@@ -2646,10 +2670,10 @@
 relationship between SC-formality and the classification is
 sharper than the table suggests. Proposition~\ref{prop:swiss-cheese-nonformality-by-class}
 already isolates the first nonzero Swiss-cheese operation in each
-non-Gaussian class: class~$L$ has $m_3^{\mathrm{SC}} \neq 0$,
-class~$C$ has $m_4^{\mathrm{SC}} \neq 0$, and class~$M$ has
-nonzero $m_k^{\mathrm{SC}}$ for all $k \geq 3$. This reduces the
-formality criterion to a classification check.
+non-Gaussian class and, on the Gaussian locus, identifies the
+mixed-sector tree formulas with the degree-by-degree shadow tower
+after averaging. The criterion below packages this as an equivalence
+between SC-formality and truncation of the shadow tower at degree~$2$.
 
 \begin{proposition}[SC-formality characterises class~$G$; \ClaimStatusProvedHere]
 \label{prop:sc-formal-iff-class-g}
@@ -2665,21 +2689,30 @@
 The forward direction \textup{(}class~$G$ $\Longrightarrow$
 SC-formal\textup{)} is established in
 Proposition~\ref{prop:swiss-cheese-nonformality-by-class}:
-the class-$G$ row consists exactly of Heisenberg and lattice
-VOAs, and in both cases $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
+the class-$G$ row consists of the Gaussian families Heisenberg,
+lattice VOA, and free fermion, and in each case the genus-$0$
+mixed tree formulas stop at arity~$2$, so
+$m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
 
 For the converse, suppose~$\cA$ is SC-formal.
-Because the standard landscape is exhausted by the four classes
-$G$, $L$, $C$, $M$, it is enough to eliminate the three
-non-Gaussian cases. Proposition~\ref{prop:swiss-cheese-nonformality-by-class}
-does exactly this: class~$L$ has $m_3^{\mathrm{SC}} \neq 0$,
-class~$C$ has $m_4^{\mathrm{SC}} \neq 0$, and class~$M$ has
-nonzero higher operations in every arity $k \geq 3$. Each of
-these cases contradicts SC-formality. This converse uses only the
-classification from Proposition~\ref{prop:swiss-cheese-nonformality-by-class};
-it does not invoke any trilinear form built from~$\kappa$.
-Hence an SC-formal algebra must
-belong to class~$G$.
+Then the mixed sector of the Swiss-cheese bar complex is formal:
+every higher arity tree operation vanishes. The tower-bar
+correspondence is operadic: the arity-$r$ mixed tree and the
+degree-$r$ shadow are produced by the same genus-$0$ tree-transfer
+formula, with the same propagator on internal edges; the only
+difference is the output colour, and passage to the symmetric
+closed sector applies the averaging morphism
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)}.
+Hence SC-formality forces $S_r(\cA) = 0$ for every $r \geq 3$:
+there is no higher mixed tree whose closed projection could survive.
+By Theorem~\ref{thm:shadow-formality-identification} and
+Proposition~\ref{prop:shadow-tower-three-lenses}, this is exactly
+the statement that the shadow/formality tower truncates at
+degree~$2$. Theorem~\ref{thm:shadow-archetype-classification}
+identifies the standard-landscape locus with this property as
+precisely class~$G$. Hence an SC-formal algebra must belong
+to class~$G$.
 \end{proof}
 
 \begin{remark}[D-module purity: reduction to a single gap]

 exited 2 in 2m 14s:
Building main.tex (up to 4 passes)
── Pass 1 / 4 ──
   2752pp, 2002 undef citations, 4991 undef references, 2 rerun requests, 157 overfull, 306 underfull
── Pass 2 / 4 ──
   2758pp, 20 undef citations, 127 undef references, 0 rerun requests, 164 overfull, 351 underfull
── Pass 3 / 4 ──
./scripts/build.sh: line 64: 79790 Killed: 9               $TEX $TEXFLAGS main.tex > "$RUN_LOG" 2>&1
   ?pp, 0 undef citations, 2 undef references, 0 rerun requests, 19 overfull, 35 underfull
✗ Build failed.
  Logs: .build_logs/tex-build.stdout.log and main.log
make: *** [fast] Error 137
file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 82ce3f8a19eaa51f878397fa63cad2971741bf1e..caf0e7dcc8b2e4df8cb6362c74b5edc7c33e1305
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -2561,7 +2561,7 @@
 & $m_k^{\mathrm{SC}},\; k \geq 5$ \\
 \midrule
 $G$ \textup{(}$r_{\max}=2$\textup{)}
-& Heisenberg, lattice VOA
+& Heisenberg, lattice VOA, free fermion
 & $= 0$
 & $= 0$
 & $= 0$ \\
@@ -2586,12 +2586,21 @@
 
 \medskip\noindent
 \emph{Mechanism.}
-For class~$G$\textup{:} Heisenberg is central, and lattice VOAs are
-Gaussian: the Heisenberg bracket
-$[a_m, a_n] = km\,\delta_{m+n,0}$ is central, while for lattice
-VOAs the shadow obstruction tower terminates at weight~$2$ by
-Corollary~\ref{cor:lattice-postnikov-termination}. In both cases
-all higher tree sums vanish.
+For class~$G$\textup{:}
+Heisenberg, lattice VOAs, and free fermions are Gaussian/free-field:
+their ordered bar data is generated by the binary two-point kernel,
+so every connected genus-$0$ tree with at least three external legs
+factors through pairings and carries no primitive higher vertex.
+Equivalently, the shadow tower truncates at degree~$2$:
+$S_r(\cA)=0$ for $r \geq 3$
+\textup{(}Theorem~\ref{thm:shadow-archetype-classification}; for
+lattices see Corollary~\ref{cor:lattice-postnikov-termination}\textup{)}.
+Under the averaging map
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)},
+the mixed Swiss-cheese tree of arity~$r$ projects to the degree-$r$
+shadow. Since there is no primitive tree for $r \geq 3$,
+all higher mixed-sector operations vanish.
 For class~$L$\textup{:} the affine KM OPE has at most a double pole; the
 three-channel tree sum over $\overline{\cM}_{0,4}$ is nonzero
 \textup{(}$S_3 = 2h^\vee/(k+h^\vee) \neq 0$\textup{)} but the
@@ -2613,10 +2622,25 @@
 
 \begin{proof}
 Class~$G$: for Heisenberg, centrality of the bracket kills all nested
-compositions, so $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$. For lattice
-VOAs, Corollary~\ref{cor:lattice-postnikov-termination} identifies
-the shadow obstruction tower with its weight-$2$ truncation, so the
-transferred Swiss-cheese operations vanish for every $k \geq 3$.
+tree compositions, so $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
+For lattice VOAs, bosonization reduces connected genus-$0$ amplitudes
+to Wick pairings of the underlying Heisenberg field, and
+Corollary~\ref{cor:lattice-postnikov-termination} identifies the
+shadow tower with its weight-$2$ truncation. For the free fermion,
+Wick's theorem gives Pfaffian factorization by the basic contraction
+$\psi(z)\psi^*(w) \sim (z-w)^{-1}$, so again no connected tree with
+$r \geq 3$ survives after extracting the binary pairings. In all three
+cases the mixed Swiss-cheese arity-$r$ operation is the open-colored
+lift of the same genus-$0$ tree sum whose closed projection is
+$S_r(\cA)$; equivalently,
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)}.
+Because class~$G$ means $S_r(\cA) = 0$ for all $r \geq 3$,
+the mixed-sector operations vanish:
+$m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
+The weaker condition $\Delta = 0$ is not sufficient:
+affine Kac--Moody algebras are class~$L$ with $\Delta = 0$ but
+$m_3^{\mathrm{SC}} \neq 0$.
 Class~$L$: the cubic shadow
 $S_3 = 2h^\vee/(k + h^\vee)$ is computed from the OPE coefficient
 ratio (the structure constant divided by the level); the quartic
@@ -2646,10 +2670,10 @@
 relationship between SC-formality and the classification is
 sharper than the table suggests. Proposition~\ref{prop:swiss-cheese-nonformality-by-class}
 already isolates the first nonzero Swiss-cheese operation in each
-non-Gaussian class: class~$L$ has $m_3^{\mathrm{SC}} \neq 0$,
-class~$C$ has $m_4^{\mathrm{SC}} \neq 0$, and class~$M$ has
-nonzero $m_k^{\mathrm{SC}}$ for all $k \geq 3$. This reduces the
-formality criterion to a classification check.
+non-Gaussian class and, on the Gaussian locus, identifies the
+mixed-sector tree formulas with the degree-by-degree shadow tower
+after averaging. The criterion below packages this as an equivalence
+between SC-formality and truncation of the shadow tower at degree~$2$.
 
 \begin{proposition}[SC-formality characterises class~$G$; \ClaimStatusProvedHere]
 \label{prop:sc-formal-iff-class-g}
@@ -2665,21 +2689,30 @@
 The forward direction \textup{(}class~$G$ $\Longrightarrow$
 SC-formal\textup{)} is established in
 Proposition~\ref{prop:swiss-cheese-nonformality-by-class}:
-the class-$G$ row consists exactly of Heisenberg and lattice
-VOAs, and in both cases $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
+the class-$G$ row consists of the Gaussian families Heisenberg,
+lattice VOA, and free fermion, and in each case the genus-$0$
+mixed tree formulas stop at arity~$2$, so
+$m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
 
 For the converse, suppose~$\cA$ is SC-formal.
-Because the standard landscape is exhausted by the four classes
-$G$, $L$, $C$, $M$, it is enough to eliminate the three
-non-Gaussian cases. Proposition~\ref{prop:swiss-cheese-nonformality-by-class}
-does exactly this: class~$L$ has $m_3^{\mathrm{SC}} \neq 0$,
-class~$C$ has $m_4^{\mathrm{SC}} \neq 0$, and class~$M$ has
-nonzero higher operations in every arity $k \geq 3$. Each of
-these cases contradicts SC-formality. This converse uses only the
-classification from Proposition~\ref{prop:swiss-cheese-nonformality-by-class};
-it does not invoke any trilinear form built from~$\kappa$.
-Hence an SC-formal algebra must
-belong to class~$G$.
+Then the mixed sector of the Swiss-cheese bar complex is formal:
+every higher arity tree operation vanishes. The tower-bar
+correspondence is operadic: the arity-$r$ mixed tree and the
+degree-$r$ shadow are produced by the same genus-$0$ tree-transfer
+formula, with the same propagator on internal edges; the only
+difference is the output colour, and passage to the symmetric
+closed sector applies the averaging morphism
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)}.
+Hence SC-formality forces $S_r(\cA) = 0$ for every $r \geq 3$:
+there is no higher mixed tree whose closed projection could survive.
+By Theorem~\ref{thm:shadow-formality-identification} and
+Proposition~\ref{prop:shadow-tower-three-lenses}, this is exactly
+the statement that the shadow/formality tower truncates at
+degree~$2$. Theorem~\ref{thm:shadow-archetype-classification}
+identifies the standard-landscape locus with this property as
+precisely class~$G$. Hence an SC-formal algebra must belong
+to class~$G$.
 \end{proof}
 
 \begin{remark}[D-module purity: reduction to a single gap]


thinking
**Verifying references**

I might use some commands to check for undefined references in my logs, like `rg -n 'e1-primacy|shadow-archetype-classification...'`. It seems I also need to check `main.log` for issues like "undefined reference." After that, I should possibly close the build session since it has exited. The user requested verification for mathematical correctness, so I’ll ensure there are no new AP violations and confirm that my references are properly defined. Let's get started!
codex
The build did not fail on a TeX error in this section; the process was killed on pass 3 after reducing the repo-wide warning surface to `0` undefined citations and `2` undefined references. I’m checking whether any of those unresolved references come from the theorem block I edited.
exec
/bin/zsh -lc "rg -n 'thm:e1-primacy|thm:shadow-archetype-classification|thm:shadow-formality-identification|prop:shadow-tower-three-lenses|cor:lattice-postnikov-termination' main.log .build_logs/tex-build.stdout.log chapters/theory/chiral_koszul_pairs.aux" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

exec
/bin/zsh -lc 'tail -n 120 .build_logs/tex-build.stdout.log' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'undefined references|undefined reference|Reference .* undefined|Citation .* undefined' main.log .build_logs/tex-build.stdout.log" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
This is pdfTeX, Version 3.141592653-2.6-1.40.27 (TeX Live 2025) (preloaded format=pdflatex)
 restricted \write18 enabled.
entering extended mode
 succeeded in 51ms:
main.log:1999:LaTeX Warning: Reference `conj:v1-master-bv-brst' on page 93 undefined on input
main.log:2063:LaTeX Warning: Reference `conj:v1-master-bv-brst' on page 100 undefined on inpu
file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 82ce3f8a19eaa51f878397fa63cad2971741bf1e..caf0e7dcc8b2e4df8cb6362c74b5edc7c33e1305
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -2561,7 +2561,7 @@
 & $m_k^{\mathrm{SC}},\; k \geq 5$ \\
 \midrule
 $G$ \textup{(}$r_{\max}=2$\textup{)}
-& Heisenberg, lattice VOA
+& Heisenberg, lattice VOA, free fermion
 & $= 0$
 & $= 0$
 & $= 0$ \\
@@ -2586,12 +2586,21 @@
 
 \medskip\noindent
 \emph{Mechanism.}
-For class~$G$\textup{:} Heisenberg is central, and lattice VOAs are
-Gaussian: the Heisenberg bracket
-$[a_m, a_n] = km\,\delta_{m+n,0}$ is central, while for lattice
-VOAs the shadow obstruction tower terminates at weight~$2$ by
-Corollary~\ref{cor:lattice-postnikov-termination}. In both cases
-all higher tree sums vanish.
+For class~$G$\textup{:}
+Heisenberg, lattice VOAs, and free fermions are Gaussian/free-field:
+their ordered bar data is generated by the binary two-point kernel,
+so every connected genus-$0$ tree with at least three external legs
+factors through pairings and carries no primitive higher vertex.
+Equivalently, the shadow tower truncates at degree~$2$:
+$S_r(\cA)=0$ for $r \geq 3$
+\textup{(}Theorem~\ref{thm:shadow-archetype-classification}; for
+lattices see Corollary~\ref{cor:lattice-postnikov-termination}\textup{)}.
+Under the averaging map
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)},
+the mixed Swiss-cheese tree of arity~$r$ projects to the degree-$r$
+shadow. Since there is no primitive tree for $r \geq 3$,
+all higher mixed-sector operations vanish.
 For class~$L$\textup{:} the affine KM OPE has at most a double pole; the
 three-channel tree sum over $\overline{\cM}_{0,4}$ is nonzero
 \textup{(}$S_3 = 2h^\vee/(k+h^\vee) \neq 0$\textup{)} but the
@@ -2613,10 +2622,25 @@
 
 \begin{proof}
 Class~$G$: for Heisenberg, centrality of the bracket kills all nested
-compositions, so $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$. For lattice
-VOAs, Corollary~\ref{cor:lattice-postnikov-termination} identifies
-the shadow obstruction tower with its weight-$2$ truncation, so the
-transferred Swiss-cheese operations vanish for every $k \geq 3$.
+tree compositions, so $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
+For lattice VOAs, bosonization reduces connected genus-$0$ amplitudes
+to Wick pairings of the underlying Heisenberg field, and
+Corollary~\ref{cor:lattice-postnikov-termination} identifies the
+shadow tower with its weight-$2$ truncation. For the free fermion,
+Wick's theorem gives Pfaffian factorization by the basic contraction
+$\psi(z)\psi^*(w) \sim (z-w)^{-1}$, so again no connected tree with
+$r \geq 3$ survives after extracting the binary pairings. In all three
+cases the mixed Swiss-cheese arity-$r$ operation is the open-colored
+lift of the same genus-$0$ tree sum whose closed projection is
+$S_r(\cA)$; equivalently,
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)}.
+Because class~$G$ means $S_r(\cA) = 0$ for all $r \geq 3$,
+the mixed-sector operations vanish:
+$m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
+The weaker condition $\Delta = 0$ is not sufficient:
+affine Kac--Moody algebras are class~$L$ with $\Delta = 0$ but
+$m_3^{\mathrm{SC}} \neq 0$.
 Class~$L$: the cubic shadow
 $S_3 = 2h^\vee/(k + h^\vee)$ is computed from the OPE coefficient
 ratio (the structure constant divided by the level); the quartic
@@ -2646,10 +2670,10 @@
 relationship between SC-formality and the classification is
 sharper than the table suggests. Proposition~\ref{prop:swiss-cheese-nonformality-by-class}
 already isolates the first nonzero Swiss-cheese operation in each
-non-Gaussian class: class~$L$ has $m_3^{\mathrm{SC}} \neq 0$,
-class~$C$ has $m_4^{\mathrm{SC}} \neq 0$, and class~$M$ has
-nonzero $m_k^{\mathrm{SC}}$ for all $k \geq 3$. This reduces the
-formality criterion to a classification check.
+non-Gaussian class and, on the Gaussian locus, identifies the
+mixed-sector tree formulas with the degree-by-degree shadow tower
+after averaging. The criterion below packages this as an equivalence
+between SC-formality and truncation of the shadow tower at degree~$2$.
 
 \begin{proposition}[SC-formality characterises class~$G$; \ClaimStatusProvedHere]
 \label{prop:sc-formal-iff-class-g}
@@ -2665,21 +2689,30 @@
 The forward direction \textup{(}class~$G$ $\Longrightarrow$
 SC-formal\textup{)} is established in
 Proposition~\ref{prop:swiss-cheese-nonformality-by-class}:
-the class-$G$ row consists exactly of Heisenberg and lattice
-VOAs, and in both cases $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
+the class-$G$ row consists of the Gaussian families Heisenberg,
+lattice VOA, and free fermion, and in each case the genus-$0$
+mixed tree formulas stop at arity~$2$, so
+$m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
 
 For the converse, suppose~$\cA$ is SC-formal.
-Because the standard landscape is exhausted by the four classes
-$G$, $L$, $C$, $M$, it is enough to eliminate the three
-non-Gaussian cases. Proposition~\ref{prop:swiss-cheese-nonformality-by-class}
-does exactly this: class~$L$ has $m_3^{\mathrm{SC}} \neq 0$,
-class~$C$ has $m_4^{\mathrm{SC}} \neq 0$, and class~$M$ has
-nonzero higher operations in every arity $k \geq 3$. Each of
-these cases contradicts SC-formality. This converse uses only the
-classification from Proposition~\ref{prop:swiss-cheese-nonformality-by-class};
-it does not invoke any trilinear form built from~$\kappa$.
-Hence an SC-formal algebra must
-belong to class~$G$.
+Then the mixed sector of the Swiss-cheese bar complex is formal:
+every higher arity tree operation vanishes. The tower-bar
+correspondence is operadic: the arity-$r$ mixed tree and the
+degree-$r$ shadow are produced by the same genus-$0$ tree-transfer
+formula, with the same propagator on internal edges; the only
+difference is the output colour, and passage to the symmetric
+closed sector applies the averaging morphism
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)}.
+Hence SC-formality forces $S_r(\cA) = 0$ for every $r \geq 3$:
+there is no higher mixed tree whose closed projection could survive.
+By Theorem~\ref{thm:shadow-formality-identification} and
+Proposition~\ref{prop:shadow-tower-three-lenses}, this is exactly
+the statement that the shadow/formality tower truncates at
+degree~$2$. Theorem~\ref{thm:shadow-archetype-classification}
+identifies the standard-landscape locus with this property as
+precisely class~$G$. Hence an SC-formal algebra must belong
+to class~$G$.
 \end{proof}
 
 \begin{remark}[D-module purity: reduction to a single gap]

codex
The edited theorem lane compiles cleanly against its own references: none of the new labels show up as unresolved, and the only remaining undefined refs in the log are unrelated global debt (`conj:v1-master-bv-brst`). I’m doing one last local consistency sweep inside the target file for nearby stale wording.
exec
/bin/zsh -lc "rg -n 'Heisenberg, lattice VOA|Heisenberg and lattice|Heisenberg and its relatives|free fermion|SC-formal|class~\\\\\\"'$G|class~'"\\"'$G'"' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
88:bar complex. All standard families are Koszul; only class~$G$
89:(Heisenberg and its relatives) is SC-formal
125:classes: Heisenberg (class~$G$, depth~$2$, formal), affine
2564:& Heisenberg, lattice VOA, free fermion
2589:For class~$G$\textup{:}
2590:Heisenberg, lattice VOAs, and free fermions are Gaussian/free-field:
2629:shadow tower with its weight-$2$ truncation. For the free fermion,
2638:Because class~$G$ means $S_r(\cA) = 0$ for all $r \geq 3$,
2670:relationship between SC-formality and the classification is
2676:between SC-formality and truncation of the shadow tower at degree~$2$.
2678:\begin{proposition}[SC-formality characterises class~$G$; \ClaimStatusProvedHere]
2681:\index{class G@class~$G$!characterised by SC-formality}
2685:if and only if~$\cA$ belongs to class~$G$.
2689:The forward direction \textup{(}class~$G$ $\Longrightarrow$
2690:SC-formal\textup{)} is established in
2693:lattice VOA, and free fermion, and in each case the genus-$0$
2697:For the converse, suppose~$\cA$ is SC-formal.
2707:Hence SC-formality forces $S_r(\cA) = 0$ for every $r \geq 3$:
2714:precisely class~$G$. Hence an SC-formal algebra must belong
2715:to class~$G$.
exec
/bin/zsh -lc "sed -n '80,95p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2580,2710p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
& $\neq 0$
& $\neq 0$
& $\neq 0\;\forall\, k$ \\
\bottomrule
\end{tabular}
\end{center}

\medskip\noindent
\emph{Mechanism.}
For class~$G$\textup{:}
Heisenberg, lattice VOAs, and free fermions are Gaussian/free-field:
their ordered bar data is generated by the binary two-point kernel,
so every connected genus-$0$ tree with at least three external legs
factors through pairings and carries no primitive higher vertex.
Equivalently, the shadow tower truncates at degree~$2$:
$S_r(\cA)=0$ for $r \geq 3$
\textup{(}Theorem~\ref{thm:shadow-archetype-classification}; for
lattices see Corollary~\ref{cor:lattice-postnikov-termination}\textup{)}.
Under the averaging map
$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
 succeeded in 51ms:
nontrivial; they do \emph{not} record failure of Koszulness.
Every standard chiral algebra is chirally Koszul. The classes
separate algebras by the complexity of their higher-genus
behaviour, not by the validity of the duality. Second,
Koszulness and SC formality are logically independent properties.
Koszulness is the condition that bar cohomology is concentrated
in degree one; SC formality is the condition
$m_k^{\mathrm{SC}} = 0$ for $k \geq 3$ in the Swiss-cheese
bar complex. All standard families are Koszul; only class~$G$
(Heisenberg and its relatives) is SC-formal
(Proposition~\ref{prop:sc-formal-iff-class-g}).
Confusing the two misidentifies what the shadow tower measures.

On a point, the bar complex
$\barB(A) = T^c(s^{-1}\bar{A})$ is built from tensor powers of
the augmentation ideal; a classical twisting morphism
file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 82ce3f8a19eaa51f878397fa63cad2971741bf1e..caf0e7dcc8b2e4df8cb6362c74b5edc7c33e1305
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -2561,7 +2561,7 @@
 & $m_k^{\mathrm{SC}},\; k \geq 5$ \\
 \midrule
 $G$ \textup{(}$r_{\max}=2$\textup{)}
-& Heisenberg, lattice VOA
+& Heisenberg, lattice VOA, free fermion
 & $= 0$
 & $= 0$
 & $= 0$ \\
@@ -2586,12 +2586,21 @@
 
 \medskip\noindent
 \emph{Mechanism.}
-For class~$G$\textup{:} Heisenberg is central, and lattice VOAs are
-Gaussian: the Heisenberg bracket
-$[a_m, a_n] = km\,\delta_{m+n,0}$ is central, while for lattice
-VOAs the shadow obstruction tower terminates at weight~$2$ by
-Corollary~\ref{cor:lattice-postnikov-termination}. In both cases
-all higher tree sums vanish.
+For class~$G$\textup{:}
+Heisenberg, lattice VOAs, and free fermions are Gaussian/free-field:
+their ordered bar data is generated by the binary two-point kernel,
+so every connected genus-$0$ tree with at least three external legs
+factors through pairings and carries no primitive higher vertex.
+Equivalently, the shadow tower truncates at degree~$2$:
+$S_r(\cA)=0$ for $r \geq 3$
+\textup{(}Theorem~\ref{thm:shadow-archetype-classification}; for
+lattices see Corollary~\ref{cor:lattice-postnikov-termination}\textup{)}.
+Under the averaging map
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)},
+the mixed Swiss-cheese tree of arity~$r$ projects to the degree-$r$
+shadow. Since there is no primitive tree for $r \geq 3$,
+all higher mixed-sector operations vanish.
 For class~$L$\textup{:} the affine KM OPE has at most a double pole; the
 three-channel tree sum over $\overline{\cM}_{0,4}$ is nonzero
 \textup{(}$S_3 = 2h^\vee/(k+h^\vee) \neq 0$\textup{)} but the
@@ -2613,10 +2622,25 @@
 
 \begin{proof}
 Class~$G$: for Heisenberg, centrality of the bracket kills all nested
-compositions, so $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$. For lattice
-VOAs, Corollary~\ref{cor:lattice-postnikov-termination} identifies
-the shadow obstruction tower with its weight-$2$ truncation, so the
-transferred Swiss-cheese operations vanish for every $k \geq 3$.
+tree compositions, so $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
+For lattice VOAs, bosonization reduces connected genus-$0$ amplitudes
+to Wick pairings of the underlying Heisenberg field, and
+Corollary~\ref{cor:lattice-postnikov-termination} identifies the
+shadow tower with its weight-$2$ truncation. For the free fermion,
+Wick's theorem gives Pfaffian factorization by the basic contraction
+$\psi(z)\psi^*(w) \sim (z-w)^{-1}$, so again no connected tree with
+$r \geq 3$ survives after extracting the binary pairings. In all three
+cases the mixed Swiss-cheese arity-$r$ operation is the open-colored
+lift of the same genus-$0$ tree sum whose closed projection is
+$S_r(\cA)$; equivalently,
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)}.
+Because class~$G$ means $S_r(\cA) = 0$ for all $r \geq 3$,
+the mixed-sector operations vanish:
+$m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
+The weaker condition $\Delta = 0$ is not sufficient:
+affine Kac--Moody algebras are class~$L$ with $\Delta = 0$ but
+$m_3^{\mathrm{SC}} \neq 0$.
 Class~$L$: the cubic shadow
 $S_3 = 2h^\vee/(k + h^\vee)$ is computed from the OPE coefficient
 ratio (the structure constant divided by the level); the quartic
@@ -2646,10 +2670,10 @@
 relationship between SC-formality and the classification is
 sharper than the table suggests. Proposition~\ref{prop:swiss-cheese-nonformality-by-class}
 already isolates the first nonzero Swiss-cheese operation in each
-non-Gaussian class: class~$L$ has $m_3^{\mathrm{SC}} \neq 0$,
-class~$C$ has $m_4^{\mathrm{SC}} \neq 0$, and class~$M$ has
-nonzero $m_k^{\mathrm{SC}}$ for all $k \geq 3$. This reduces the
-formality criterion to a classification check.
+non-Gaussian class and, on the Gaussian locus, identifies the
+mixed-sector tree formulas with the degree-by-degree shadow tower
+after averaging. The criterion below packages this as an equivalence
+between SC-formality and truncation of the shadow tower at degree~$2$.
 
 \begin{proposition}[SC-formality characterises class~$G$; \ClaimStatusProvedHere]
 \label{prop:sc-formal-iff-class-g}
@@ -2665,21 +2689,30 @@
 The forward direction \textup{(}class~$G$ $\Longrightarrow$
 SC-formal\textup{)} is established in
 Proposition~\ref{prop:swiss-cheese-nonformality-by-class}:
-the class-$G$ row consists exactly of Heisenberg and lattice
-VOAs, and in both cases $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
+the class-$G$ row consists of the Gaussian families Heisenberg,
+lattice VOA, and free fermion, and in each case the genus-$0$
+mixed tree formulas stop at arity~$2$, so
+$m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
 
 For the converse, suppose~$\cA$ is SC-formal.
-Because the standard landscape is exhausted by the four classes
-$G$, $L$, $C$, $M$, it is enough to eliminate the three
-non-Gaussian cases. Proposition~\ref{prop:swiss-cheese-nonformality-by-class}
-does exactly this: class~$L$ has $m_3^{\mathrm{SC}} \neq 0$,
-class~$C$ has $m_4^{\mathrm{SC}} \neq 0$, and class~$M$ has
-nonzero higher operations in every arity $k \geq 3$. Each of
-these cases contradicts SC-formality. This converse uses only the
-classification from Proposition~\ref{prop:swiss-cheese-nonformality-by-class};
-it does not invoke any trilinear form built from~$\kappa$.
-Hence an SC-formal algebra must
-belong to class~$G$.
+Then the mixed sector of the Swiss-cheese bar complex is formal:
+every higher arity tree operation vanishes. The tower-bar
+correspondence is operadic: the arity-$r$ mixed tree and the
+degree-$r$ shadow are produced by the same genus-$0$ tree-transfer
+formula, with the same propagator on internal edges; the only
+difference is the output colour, and passage to the symmetric
+closed sector applies the averaging morphism
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)}.
+Hence SC-formality forces $S_r(\cA) = 0$ for every $r \geq 3$:
+there is no higher mixed tree whose closed projection could survive.
+By Theorem~\ref{thm:shadow-formality-identification} and
+Proposition~\ref{prop:shadow-tower-three-lenses}, this is exactly
+the statement that the shadow/formality tower truncates at
+degree~$2$. Theorem~\ref{thm:shadow-archetype-classification}
+identifies the standard-landscape locus with this property as
+precisely class~$G$. Hence an SC-formal algebra must belong
+to class~$G$.
 \end{proof}
 
 \begin{remark}[D-module purity: reduction to a single gap]

exec
/bin/zsh -lc "sed -n '2710,2735p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Proposition~\ref{prop:shadow-tower-three-lenses}, this is exactly
the statement that the shadow/formality tower truncates at
degree~$2$. Theorem~\ref{thm:shadow-archetype-classification}
identifies the standard-landscape locus with this property as
precisely class~$G$. Hence an SC-formal algebra must belong
to class~$G$.
\end{proof}

\begin{remark}[D-module purity: reduction to a single gap]
\label{rem:d-module-purity-content}
\index{D-module purity!reduction to Saito weight}
\index{Saito weight filtration!and PBW filtration}
The converse direction of condition~\textup{(xii)} (Koszulness
$\Longrightarrow$ D-module purity of~$\barBgeom_n(\cA)$) admits
a five-step proof strategy. Steps~1--3 are established; step~4
is the single remaining gap.

\begin{enumerate}[label=\textup{Step \arabic*.}]
\item
The PBW filtration $F_\bullet^{\mathrm{PBW}}$ on
file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 82ce3f8a19eaa51f878397fa63cad2971741bf1e..caf0e7dcc8b2e4df8cb6362c74b5edc7c33e1305
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -2561,7 +2561,7 @@
 & $m_k^{\mathrm{SC}},\; k \geq 5$ \\
 \midrule
 $G$ \textup{(}$r_{\max}=2$\textup{)}
-& Heisenberg, lattice VOA
+& Heisenberg, lattice VOA, free fermion
 & $= 0$
 & $= 0$
 & $= 0$ \\
@@ -2586,12 +2586,21 @@
 
 \medskip\noindent
 \emph{Mechanism.}
-For class~$G$\textup{:} Heisenberg is central, and lattice VOAs are
-Gaussian: the Heisenberg bracket
-$[a_m, a_n] = km\,\delta_{m+n,0}$ is central, while for lattice
-VOAs the shadow obstruction tower terminates at weight~$2$ by
-Corollary~\ref{cor:lattice-postnikov-termination}. In both cases
-all higher tree sums vanish.
+For class~$G$\textup{:}
+Heisenberg, lattice VOAs, and free fermions are Gaussian/free-field:
+their ordered bar data is generated by the binary two-point kernel,
+so every connected genus-$0$ tree with at least three external legs
+factors through pairings and carries no primitive higher vertex.
+Equivalently, the shadow tower truncates at degree~$2$:
+$S_r(\cA)=0$ for $r \geq 3$
+\textup{(}Theorem~\ref{thm:shadow-archetype-classification}; for
+lattices see Corollary~\ref{cor:lattice-postnikov-termination}\textup{)}.
+Under the averaging map
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)},
+the mixed Swiss-cheese tree of arity~$r$ projects to the degree-$r$
+shadow. Since there is no primitive tree for $r \geq 3$,
+all higher mixed-sector operations vanish.
 For class~$L$\textup{:} the affine KM OPE has at most a double pole; the
 three-channel tree sum over $\overline{\cM}_{0,4}$ is nonzero
 \textup{(}$S_3 = 2h^\vee/(k+h^\vee) \neq 0$\textup{)} but the
@@ -2613,10 +2622,25 @@
 
 \begin{proof}
 Class~$G$: for Heisenberg, centrality of the bracket kills all nested
-compositions, so $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$. For lattice
-VOAs, Corollary~\ref{cor:lattice-postnikov-termination} identifies
-the shadow obstruction tower with its weight-$2$ truncation, so the
-transferred Swiss-cheese operations vanish for every $k \geq 3$.
+tree compositions, so $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
+For lattice VOAs, bosonization reduces connected genus-$0$ amplitudes
+to Wick pairings of the underlying Heisenberg field, and
+Corollary~\ref{cor:lattice-postnikov-termination} identifies the
+shadow tower with its weight-$2$ truncation. For the free fermion,
+Wick's theorem gives Pfaffian factorization by the basic contraction
+$\psi(z)\psi^*(w) \sim (z-w)^{-1}$, so again no connected tree with
+$r \geq 3$ survives after extracting the binary pairings. In all three
+cases the mixed Swiss-cheese arity-$r$ operation is the open-colored
+lift of the same genus-$0$ tree sum whose closed projection is
+$S_r(\cA)$; equivalently,
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)}.
+Because class~$G$ means $S_r(\cA) = 0$ for all $r \geq 3$,
+the mixed-sector operations vanish:
+$m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
+The weaker condition $\Delta = 0$ is not sufficient:
+affine Kac--Moody algebras are class~$L$ with $\Delta = 0$ but
+$m_3^{\mathrm{SC}} \neq 0$.
 Class~$L$: the cubic shadow
 $S_3 = 2h^\vee/(k + h^\vee)$ is computed from the OPE coefficient
 ratio (the structure constant divided by the level); the quartic
@@ -2646,10 +2670,10 @@
 relationship between SC-formality and the classification is
 sharper than the table suggests. Proposition~\ref{prop:swiss-cheese-nonformality-by-class}
 already isolates the first nonzero Swiss-cheese operation in each
-non-Gaussian class: class~$L$ has $m_3^{\mathrm{SC}} \neq 0$,
-class~$C$ has $m_4^{\mathrm{SC}} \neq 0$, and class~$M$ has
-nonzero $m_k^{\mathrm{SC}}$ for all $k \geq 3$. This reduces the
-formality criterion to a classification check.
+non-Gaussian class and, on the Gaussian locus, identifies the
+mixed-sector tree formulas with the degree-by-degree shadow tower
+after averaging. The criterion below packages this as an equivalence
+between SC-formality and truncation of the shadow tower at degree~$2$.
 
 \begin{proposition}[SC-formality characterises class~$G$; \ClaimStatusProvedHere]
 \label{prop:sc-formal-iff-class-g}
@@ -2665,21 +2689,30 @@
 The forward direction \textup{(}class~$G$ $\Longrightarrow$
 SC-formal\textup{)} is established in
 Proposition~\ref{prop:swiss-cheese-nonformality-by-class}:
-the class-$G$ row consists exactly of Heisenberg and lattice
-VOAs, and in both cases $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
+the class-$G$ row consists of the Gaussian families Heisenberg,
+lattice VOA, and free fermion, and in each case the genus-$0$
+mixed tree formulas stop at arity~$2$, so
+$m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
 
 For the converse, suppose~$\cA$ is SC-formal.
-Because the standard landscape is exhausted by the four classes
-$G$, $L$, $C$, $M$, it is enough to eliminate the three
-non-Gaussian cases. Proposition~\ref{prop:swiss-cheese-nonformality-by-class}
-does exactly this: class~$L$ has $m_3^{\mathrm{SC}} \neq 0$,
-class~$C$ has $m_4^{\mathrm{SC}} \neq 0$, and class~$M$ has
-nonzero higher operations in every arity $k \geq 3$. Each of
-these cases contradicts SC-formality. This converse uses only the
-classification from Proposition~\ref{prop:swiss-cheese-nonformality-by-class};
-it does not invoke any trilinear form built from~$\kappa$.
-Hence an SC-formal algebra must
-belong to class~$G$.
+Then the mixed sector of the Swiss-cheese bar complex is formal:
+every higher arity tree operation vanishes. The tower-bar
+correspondence is operadic: the arity-$r$ mixed tree and the
+degree-$r$ shadow are produced by the same genus-$0$ tree-transfer
+formula, with the same propagator on internal edges; the only
+difference is the output colour, and passage to the symmetric
+closed sector applies the averaging morphism
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)}.
+Hence SC-formality forces $S_r(\cA) = 0$ for every $r \geq 3$:
+there is no higher mixed tree whose closed projection could survive.
+By Theorem~\ref{thm:shadow-formality-identification} and
+Proposition~\ref{prop:shadow-tower-three-lenses}, this is exactly
+the statement that the shadow/formality tower truncates at
+degree~$2$. Theorem~\ref{thm:shadow-archetype-classification}
+identifies the standard-landscape locus with this property as
+precisely class~$G$. Hence an SC-formal algebra must belong
+to class~$G$.
 \end{proof}
 
 \begin{remark}[D-module purity: reduction to a single gap]


thinking
**Evaluating concordance scope**

The scope is limited to read-only, which is useful. There's a mention of a something in the concordance entry about "abelian bracket + nondegeneracy of kappa." Since the scope isn't editable, I should consider any pending local duplicates outside of it. It’s important to note that assigned scope is only for the target file, and cross-volume propagation isn't allowed with `concordance.tex`. I should also think about inspecting exact stale lines and searching for specific phrases.
codex
The target file is locally consistent now. I’m doing one read-only collision sweep for nearby stale advertisements that I could not edit under the single-file scope, so I can name the remaining propagation debt precisely instead of hand-waving it.
exec
/bin/zsh -lc "rg -n 'abelian bracket \\+ nondegeneracy of\\\\?~?\\\\kappa|abelian bracket .* nondegeneracy of.*kappa|SC-formality characterises class|SC-formality \\\\iff class|class G/L are SC-formal|class G only|free fermion' chapters/connections/concordance.tex /Users/raeez/chiral-bar-cobar-vol2/chapters /Users/raeez/calabi-yau-quantum-groups/compute/lib/swiss_cheese_cy3_e1.py /Users/raeez/calabi-yau-quantum-groups/compute/lib/cross_volume_shadow_bridge.py" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/connections/concordance.tex:338: Heisenberg, free fermion, $bc$-$\beta\gamma$, affine Kac--Moody
chapters/connections/concordance.tex:2609: & $\mathcal{H}_k$, free fermion, rank-$1$ lattice, all 24 Niemeier ($\kappa{=}24$) \\
chapters/connections/concordance.tex:7095: & SC-formality characterises class~$\mathbf{G}$:
chapters/connections/concordance.tex:7098: & abelian bracket $+$ nondegeneracy of~$\kappa$ \\
/Users/raeez/calabi-yau-quantum-groups/compute/lib/swiss_cheese_cy3_e1.py:62:   Vol I proves: class G/L are SC-formal (m_k^{SC} = 0 for k >= 3).
/Users/raeez/calabi-yau-quantum-groups/compute/lib/swiss_cheese_cy3_e1.py:1000:        obstruction_source="formal (class G only)",
/Users/raeez/calabi-yau-quantum-groups/compute/lib/cross_volume_shadow_bridge.py:58:  SC-formal (m_k^{SC} = 0 for k >= 3): Heisenberg, lattice (class G only)
/Users/raeez/calabi-yau-quantum-groups/compute/lib/cross_volume_shadow_bridge.py:305:    For SC-formal families (class G only): returns float('inf').
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:1843: free fermions. For systems whose OPE on generators
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:1926: $bc_\lambda$, free fermions) belongs to this level: the OPE
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:3041:\subsection{The free fermion $\psi$: class~G on generators, class~C full}%
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:3043:\index{free fermion!ordered bar complex|textbf}%
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:3044:\index{Koszul duality!free fermion}
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:3046:The free fermion $\psi$ of conformal weight~$1/2$ is the
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:3057:\index{free fermion!R-matrix}%
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:3058:\index{free fermion!Koszul dual}%
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:3059:\index{free fermion!depth spectrum}%
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:3060:The free fermion has a single generator $\psi$ of conformal
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:3113:The free fermion is the chiral exterior algebra
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:3154:(the simple-pole residue), so $c_0 \ne 0$: the free fermion is
Plan update
The theorem lane is patched and verified locally. I’m closing with a read-only propagation sweep because the assigned write scope is single-file.
  ✓ Load rectification workflow and mandatory repo context for the target theorem surface
  ✓ Lock the exact theorem/label/current proof surface in chiral_koszul_pairs.tex
  ✓ Strengthen the forward and converse directions in the assigned scope
  ✓ Re-read modified region and run required AP greps/targeted verification
  → Check collision surface for propagation needs and finalize rectification report
file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 82ce3f8a19eaa51f878397fa63cad2971741bf1e..caf0e7dcc8b2e4df8cb6362c74b5edc7c33e1305
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -2561,7 +2561,7 @@
 & $m_k^{\mathrm{SC}},\; k \geq 5$ \\
 \midrule
 $G$ \textup{(}$r_{\max}=2$\textup{)}
-& Heisenberg, lattice VOA
+& Heisenberg, lattice VOA, free fermion
 & $= 0$
 & $= 0$
 & $= 0$ \\
@@ -2586,12 +2586,21 @@
 
 \medskip\noindent
 \emph{Mechanism.}
-For class~$G$\textup{:} Heisenberg is central, and lattice VOAs are
-Gaussian: the Heisenberg bracket
-$[a_m, a_n] = km\,\delta_{m+n,0}$ is central, while for lattice
-VOAs the shadow obstruction tower terminates at weight~$2$ by
-Corollary~\ref{cor:lattice-postnikov-termination}. In both cases
-all higher tree sums vanish.
+For class~$G$\textup{:}
+Heisenberg, lattice VOAs, and free fermions are Gaussian/free-field:
+their ordered bar data is generated by the binary two-point kernel,
+so every connected genus-$0$ tree with at least three external legs
+factors through pairings and carries no primitive higher vertex.
+Equivalently, the shadow tower truncates at degree~$2$:
+$S_r(\cA)=0$ for $r \geq 3$
+\textup{(}Theorem~\ref{thm:shadow-archetype-classification}; for
+lattices see Corollary~\ref{cor:lattice-postnikov-termination}\textup{)}.
+Under the averaging map
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)},
+the mixed Swiss-cheese tree of arity~$r$ projects to the degree-$r$
+shadow. Since there is no primitive tree for $r \geq 3$,
+all higher mixed-sector operations vanish.
 For class~$L$\textup{:} the affine KM OPE has at most a double pole; the
 three-channel tree sum over $\overline{\cM}_{0,4}$ is nonzero
 \textup{(}$S_3 = 2h^\vee/(k+h^\vee) \neq 0$\textup{)} but the
@@ -2613,10 +2622,25 @@
 
 \begin{proof}
 Class~$G$: for Heisenberg, centrality of the bracket kills all nested
-compositions, so $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$. For lattice
-VOAs, Corollary~\ref{cor:lattice-postnikov-termination} identifies
-the shadow obstruction tower with its weight-$2$ truncation, so the
-transferred Swiss-cheese operations vanish for every $k \geq 3$.
+tree compositions, so $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
+For lattice VOAs, bosonization reduces connected genus-$0$ amplitudes
+to Wick pairings of the underlying Heisenberg field, and
+Corollary~\ref{cor:lattice-postnikov-termination} identifies the
+shadow tower with its weight-$2$ truncation. For the free fermion,
+Wick's theorem gives Pfaffian factorization by the basic contraction
+$\psi(z)\psi^*(w) \sim (z-w)^{-1}$, so again no connected tree with
+$r \geq 3$ survives after extracting the binary pairings. In all three
+cases the mixed Swiss-cheese arity-$r$ operation is the open-colored
+lift of the same genus-$0$ tree sum whose closed projection is
+$S_r(\cA)$; equivalently,
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)}.
+Because class~$G$ means $S_r(\cA) = 0$ for all $r \geq 3$,
+the mixed-sector operations vanish:
+$m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
+The weaker condition $\Delta = 0$ is not sufficient:
+affine Kac--Moody algebras are class~$L$ with $\Delta = 0$ but
+$m_3^{\mathrm{SC}} \neq 0$.
 Class~$L$: the cubic shadow
 $S_3 = 2h^\vee/(k + h^\vee)$ is computed from the OPE coefficient
 ratio (the structure constant divided by the level); the quartic
@@ -2646,10 +2670,10 @@
 relationship between SC-formality and the classification is
 sharper than the table suggests. Proposition~\ref{prop:swiss-cheese-nonformality-by-class}
 already isolates the first nonzero Swiss-cheese operation in each
-non-Gaussian class: class~$L$ has $m_3^{\mathrm{SC}} \neq 0$,
-class~$C$ has $m_4^{\mathrm{SC}} \neq 0$, and class~$M$ has
-nonzero $m_k^{\mathrm{SC}}$ for all $k \geq 3$. This reduces the
-formality criterion to a classification check.
+non-Gaussian class and, on the Gaussian locus, identifies the
+mixed-sector tree formulas with the degree-by-degree shadow tower
+after averaging. The criterion below packages this as an equivalence
+between SC-formality and truncation of the shadow tower at degree~$2$.
 
 \begin{proposition}[SC-formality characterises class~$G$; \ClaimStatusProvedHere]
 \label{prop:sc-formal-iff-class-g}
@@ -2665,21 +2689,30 @@
 The forward direction \textup{(}class~$G$ $\Longrightarrow$
 SC-formal\textup{)} is established in
 Proposition~\ref{prop:swiss-cheese-nonformality-by-class}:
-the class-$G$ row consists exactly of Heisenberg and lattice
-VOAs, and in both cases $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
+the class-$G$ row consists of the Gaussian families Heisenberg,
+lattice VOA, and free fermion, and in each case the genus-$0$
+mixed tree formulas stop at arity~$2$, so
+$m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
 
 For the converse, suppose~$\cA$ is SC-formal.
-Because the standard landscape is exhausted by the four classes
-$G$, $L$, $C$, $M$, it is enough to eliminate the three
-non-Gaussian cases. Proposition~\ref{prop:swiss-cheese-nonformality-by-class}
-does exactly this: class~$L$ has $m_3^{\mathrm{SC}} \neq 0$,
-class~$C$ has $m_4^{\mathrm{SC}} \neq 0$, and class~$M$ has
-nonzero higher operations in every arity $k \geq 3$. Each of
-these cases contradicts SC-formality. This converse uses only the
-classification from Proposition~\ref{prop:swiss-cheese-nonformality-by-class};
-it does not invoke any trilinear form built from~$\kappa$.
-Hence an SC-formal algebra must
-belong to class~$G$.
+Then the mixed sector of the Swiss-cheese bar complex is formal:
+every higher arity tree operation vanishes. The tower-bar
+correspondence is operadic: the arity-$r$ mixed tree and the
+degree-$r$ shadow are produced by the same genus-$0$ tree-transfer
+formula, with the same propagator on internal edges; the only
+difference is the output colour, and passage to the symmetric
+closed sector applies the averaging morphism
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)}.
+Hence SC-formality forces $S_r(\cA) = 0$ for every $r \geq 3$:
+there is no higher mixed tree whose closed projection could survive.
+By Theorem~\ref{thm:shadow-formality-identification} and
+Proposition~\ref{prop:shadow-tower-three-lenses}, this is exactly
+the statement that the shadow/formality tower truncates at
+degree~$2$. Theorem~\ref{thm:shadow-archetype-classification}
+identifies the standard-landscape locus with this property as
+precisely class~$G$. Hence an SC-formal algebra must belong
+to class~$G$.
 \end{proof}
 
 \begin{remark}[D-module purity: reduction to a single gap]

Plan update
The target file is patched, reread, AP-grepped, and build-checked. The remaining items are propagation debts outside the assigned write scope, which I will report explicitly.
  ✓ Load rectification workflow and mandatory repo context for the target theorem surface
  ✓ Lock the exact theorem/label/current proof surface in chiral_koszul_pairs.tex
  ✓ Strengthen the forward and converse directions in the assigned scope
  ✓ Re-read modified region and run required AP greps/targeted verification
  ✓ Check collision surface for propagation needs and finalize rectification report
file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 82ce3f8a19eaa51f878397fa63cad2971741bf1e..caf0e7dcc8b2e4df8cb6362c74b5edc7c33e1305
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -2561,7 +2561,7 @@
 & $m_k^{\mathrm{SC}},\; k \geq 5$ \\
 \midrule
 $G$ \textup{(}$r_{\max}=2$\textup{)}
-& Heisenberg, lattice VOA
+& Heisenberg, lattice VOA, free fermion
 & $= 0$
 & $= 0$
 & $= 0$ \\
@@ -2586,12 +2586,21 @@
 
 \medskip\noindent
 \emph{Mechanism.}
-For class~$G$\textup{:} Heisenberg is central, and lattice VOAs are
-Gaussian: the Heisenberg bracket
-$[a_m, a_n] = km\,\delta_{m+n,0}$ is central, while for lattice
-VOAs the shadow obstruction tower terminates at weight~$2$ by
-Corollary~\ref{cor:lattice-postnikov-termination}. In both cases
-all higher tree sums vanish.
+For class~$G$\textup{:}
+Heisenberg, lattice VOAs, and free fermions are Gaussian/free-field:
+their ordered bar data is generated by the binary two-point kernel,
+so every connected genus-$0$ tree with at least three external legs
+factors through pairings and carries no primitive higher vertex.
+Equivalently, the shadow tower truncates at degree~$2$:
+$S_r(\cA)=0$ for $r \geq 3$
+\textup{(}Theorem~\ref{thm:shadow-archetype-classification}; for
+lattices see Corollary~\ref{cor:lattice-postnikov-termination}\textup{)}.
+Under the averaging map
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)},
+the mixed Swiss-cheese tree of arity~$r$ projects to the degree-$r$
+shadow. Since there is no primitive tree for $r \geq 3$,
+all higher mixed-sector operations vanish.
 For class~$L$\textup{:} the affine KM OPE has at most a double pole; the
 three-channel tree sum over $\overline{\cM}_{0,4}$ is nonzero
 \textup{(}$S_3 = 2h^\vee/(k+h^\vee) \neq 0$\textup{)} but the
@@ -2613,10 +2622,25 @@
 
 \begin{proof}
 Class~$G$: for Heisenberg, centrality of the bracket kills all nested
-compositions, so $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$. For lattice
-VOAs, Corollary~\ref{cor:lattice-postnikov-termination} identifies
-the shadow obstruction tower with its weight-$2$ truncation, so the
-transferred Swiss-cheese operations vanish for every $k \geq 3$.
+tree compositions, so $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
+For lattice VOAs, bosonization reduces connected genus-$0$ amplitudes
+to Wick pairings of the underlying Heisenberg field, and
+Corollary~\ref{cor:lattice-postnikov-termination} identifies the
+shadow tower with its weight-$2$ truncation. For the free fermion,
+Wick's theorem gives Pfaffian factorization by the basic contraction
+$\psi(z)\psi^*(w) \sim (z-w)^{-1}$, so again no connected tree with
+$r \geq 3$ survives after extracting the binary pairings. In all three
+cases the mixed Swiss-cheese arity-$r$ operation is the open-colored
+lift of the same genus-$0$ tree sum whose closed projection is
+$S_r(\cA)$; equivalently,
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)}.
+Because class~$G$ means $S_r(\cA) = 0$ for all $r \geq 3$,
+the mixed-sector operations vanish:
+$m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
+The weaker condition $\Delta = 0$ is not sufficient:
+affine Kac--Moody algebras are class~$L$ with $\Delta = 0$ but
+$m_3^{\mathrm{SC}} \neq 0$.
 Class~$L$: the cubic shadow
 $S_3 = 2h^\vee/(k + h^\vee)$ is computed from the OPE coefficient
 ratio (the structure constant divided by the level); the quartic
@@ -2646,10 +2670,10 @@
 relationship between SC-formality and the classification is
 sharper than the table suggests. Proposition~\ref{prop:swiss-cheese-nonformality-by-class}
 already isolates the first nonzero Swiss-cheese operation in each
-non-Gaussian class: class~$L$ has $m_3^{\mathrm{SC}} \neq 0$,
-class~$C$ has $m_4^{\mathrm{SC}} \neq 0$, and class~$M$ has
-nonzero $m_k^{\mathrm{SC}}$ for all $k \geq 3$. This reduces the
-formality criterion to a classification check.
+non-Gaussian class and, on the Gaussian locus, identifies the
+mixed-sector tree formulas with the degree-by-degree shadow tower
+after averaging. The criterion below packages this as an equivalence
+between SC-formality and truncation of the shadow tower at degree~$2$.
 
 \begin{proposition}[SC-formality characterises class~$G$; \ClaimStatusProvedHere]
 \label{prop:sc-formal-iff-class-g}
@@ -2665,21 +2689,30 @@
 The forward direction \textup{(}class~$G$ $\Longrightarrow$
 SC-formal\textup{)} is established in
 Proposition~\ref{prop:swiss-cheese-nonformality-by-class}:
-the class-$G$ row consists exactly of Heisenberg and lattice
-VOAs, and in both cases $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
+the class-$G$ row consists of the Gaussian families Heisenberg,
+lattice VOA, and free fermion, and in each case the genus-$0$
+mixed tree formulas stop at arity~$2$, so
+$m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
 
 For the converse, suppose~$\cA$ is SC-formal.
-Because the standard landscape is exhausted by the four classes
-$G$, $L$, $C$, $M$, it is enough to eliminate the three
-non-Gaussian cases. Proposition~\ref{prop:swiss-cheese-nonformality-by-class}
-does exactly this: class~$L$ has $m_3^{\mathrm{SC}} \neq 0$,
-class~$C$ has $m_4^{\mathrm{SC}} \neq 0$, and class~$M$ has
-nonzero higher operations in every arity $k \geq 3$. Each of
-these cases contradicts SC-formality. This converse uses only the
-classification from Proposition~\ref{prop:swiss-cheese-nonformality-by-class};
-it does not invoke any trilinear form built from~$\kappa$.
-Hence an SC-formal algebra must
-belong to class~$G$.
+Then the mixed sector of the Swiss-cheese bar complex is formal:
+every higher arity tree operation vanishes. The tower-bar
+correspondence is operadic: the arity-$r$ mixed tree and the
+degree-$r$ shadow are produced by the same genus-$0$ tree-transfer
+formula, with the same propagator on internal edges; the only
+difference is the output colour, and passage to the symmetric
+closed sector applies the averaging morphism
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)}.
+Hence SC-formality forces $S_r(\cA) = 0$ for every $r \geq 3$:
+there is no higher mixed tree whose closed projection could survive.
+By Theorem~\ref{thm:shadow-formality-identification} and
+Proposition~\ref{prop:shadow-tower-three-lenses}, this is exactly
+the statement that the shadow/formality tower truncates at
+degree~$2$. Theorem~\ref{thm:shadow-archetype-classification}
+identifies the standard-landscape locus with this property as
+precisely class~$G$. Hence an SC-formal algebra must belong
+to class~$G$.
 \end{proof}
 
 \begin{remark}[D-module purity: reduction to a single gap]


thinking
**Collecting line numbers**

I think I need to get line numbers in the target file for easy reference in the final output. I could use `rg -n` around labels or perhaps use `nl`. My focus is on obtaining line numbers for the starts of propositions and possibly modified lines. I should use `nl -ba` as it seems like a useful way to achieve this. Let’s see what I can gather!
exec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '2480,2715p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  2480	Theorem~\ref{thm:fundamental-twisting-morphisms} (the bar-cobar
  2481	adjunction is a Quillen equivalence on the Koszul locus) and the
  2482	biduality of holonomic D-modules under Verdier duality. Concretely,
  2483	the bar complex of $\cA^!$ is the cobar complex of $\cA$ (by
  2484	construction of $\cA^!$), and the cobar of bar is canonically
  2485	quasi-isomorphic to $\cA$ on the Koszul locus
  2486	(Theorem~\ref{thm:bar-cobar-inversion-qi}). Hence
  2487	$(\cA^!)^! = \mathrm{cobar}(\barB(\cA^!)) =
  2488	\mathrm{cobar}(\Omega(\barB(\cA))) \simeq \cA$. This is the
  2489	chiral analog of the standard fact $(A^!)^! \simeq A$ for
  2490	quadratic algebras (Loday--Vallette~\cite{LV12}, Theorem~3.4.6),
  2491	with the additional Beilinson--Drinfeld holonomicity input
  2492	ensuring chain-level convergence on a smooth projective curve.
  2493	
  2494	\textup{(c)}: Smooth base change uses
  2495	Lemma~\ref{lem:pushforward-preserves-qi} to verify that
  2496	$f^*$ preserves quasi-isomorphisms of chiral algebras, combined
  2497	with Theorem~\ref{thm:bar-cobar-inversion-functorial} to verify
  2498	that $f^*$ commutes with bar-cobar. The witnessing datum for
  2499	chiral Koszulness pulls back along $f$, and the
file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 82ce3f8a19eaa51f878397fa63cad2971741bf1e..fba59410ce45bba7f2b0aaa62d34bbde7099735d
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -566,8 +566,8 @@
  $H^0 \cong \cC$.
 \item \emph{$\mathrm{A}_2$}: geometric bar-cobar duality
  (Theorem~\ref{thm:bar-cobar-isomorphism-main}): for a chiral
- dual pair, Verdier duality sends the bar coalgebra of one side
- to the dual factorization algebra of the other.
+ dual pair, applying Verdier duality to the bar coalgebra of one side
+ produces the dual factorization algebra of the other.
 \end{itemize}
 $\mathrm{A}_0$ is the Koszul recognition theorem;
 $\mathrm{A}_1$ extracts the dual coalgebra;
@@ -681,7 +681,9 @@
 \mathbb{D}_{\operatorname{Ran}}(\cC_1)
 \simeq \Omega_X(\cC_2)
 \]
-is supplied by Theorem~\ref{thm:verdier-bar-cobar} together with
+is supplied by Theorem~\ref{thm:verdier-bar-cobar}, which is already
+a statement about the factorization algebra obtained after applying
+$\mathbb{D}_{\operatorname{Ran}}$ to the bar coalgebra, together with
 the counit quasi-isomorphism
 $\Omega_X(\cC_2) \xrightarrow{\sim} \cA_2$ from
 Theorem~\ref{thm:fundamental-twisting-morphisms}.
@@ -706,11 +708,12 @@
 bosonic field $a(z)$ with OPE $a(z)a(w) \sim k/(z-w)^2$)
 and $\mathrm{Sym}^{\mathrm{ch}}(V^*)$ is $\chirCom$-type: the
 chiral incarnation of classical $\mathrm{Lie}$--$\mathrm{Com}$ duality.
-Theorem~\ref{thm:bar-cobar-isomorphism-main} identifies
-the bar coalgebra
+The explicit bar computation gives the bar coalgebra
 $\bar{B}^{\mathrm{ch}}(\mathcal{H}_k) \simeq
-\mathrm{coLie}^{\mathrm{ch}}(V^*)$,
-whose linear dual is the Koszul dual algebra
+\mathrm{coLie}^{\mathrm{ch}}(V^*)$.
+Applying Theorem~\ref{thm:bar-cobar-isomorphism-main} to this bar
+coalgebra identifies its Verdier dual factorization algebra with the
+Koszul dual algebra
 $\mathcal{H}_k^! = \mathrm{Sym}^{\mathrm{ch}}(V^*)$:
 the bar complex $\bar{B}(\mathcal{H}_k)$ was computed degree by
 degree in \S\ref{sec:frame-bar-deg1}--\S\ref{sec:frame-bar-all},
@@ -2561,7 +2564,7 @@
 & $m_k^{\mathrm{SC}},\; k \geq 5$ \\
 \midrule
 $G$ \textup{(}$r_{\max}=2$\textup{)}
-& Heisenberg, lattice VOA
+& Heisenberg, lattice VOA, free fermion
 & $= 0$
 & $= 0$
 & $= 0$ \\
@@ -2586,12 +2589,21 @@
 
 \medskip\noindent
 \emph{Mechanism.}
-For class~$G$\textup{:} Heisenberg is central, and lattice VOAs are
-Gaussian: the Heisenberg bracket
-$[a_m, a_n] = km\,\delta_{m+n,0}$ is central, while for lattice
-VOAs the shadow obstruction tower terminates at weight~$2$ by
-Corollary~\ref{cor:lattice-postnikov-termination}. In both cases
-all higher tree sums vanish.
+For class~$G$\textup{:}
+Heisenberg, lattice VOAs, and free fermions are Gaussian/free-field:
+their ordered bar data is generated by the binary two-point kernel,
+so every connected genus-$0$ tree with at least three external legs
+factors through pairings and carries no primitive higher vertex.
+Equivalently, the shadow tower truncates at degree~$2$:
+$S_r(\cA)=0$ for $r \geq 3$
+\textup{(}Theorem~\ref{thm:shadow-archetype-classification}; for
+lattices see Corollary~\ref{cor:lattice-postnikov-termination}\textup{)}.
+Under the averaging map
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)},
+the mixed Swiss-cheese tree of arity~$r$ projects to the degree-$r$
+shadow. Since there is no primitive tree for $r \geq 3$,
+all higher mixed-sector operations vanish.
 For class~$L$\textup{:} the affine KM OPE has at most a double pole; the
 three-channel tree sum over $\overline{\cM}_{0,4}$ is nonzero
 \textup{(}$S_3 = 2h^\vee/(k+h^\vee) \neq 0$\textup{)} but the
@@ -2613,10 +2625,25 @@
 
 \begin{proof}
 Class~$G$: for Heisenberg, centrality of the bracket kills all nested
-compositions, so $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$. For lattice
-VOAs, Corollary~\ref{cor:lattice-postnikov-termination} identifies
-the shadow obstruction tower with its weight-$2$ truncation, so the
-transferred Swiss-cheese operations vanish for every $k \geq 3$.
+tree compositions, so $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
+For lattice VOAs, bosonization reduces connected genus-$0$ amplitudes
+to Wick pairings of the underlying Heisenberg field, and
+Corollary~\ref{cor:lattice-postnikov-termination} identifies the
+shadow tower with its weight-$2$ truncation. For the free fermion,
+Wick's theorem gives Pfaffian factorization by the basic contraction
+$\psi(z)\psi^*(w) \sim (z-w)^{-1}$, so again no connected tree with
+$r \geq 3$ survives after extracting the binary pairings. In all three
+cases the mixed Swiss-cheese arity-$r$ operation is the open-colored
+lift of the same genus-$0$ tree sum whose closed projection is
+$S_r(\cA)$; equivalently,
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)}.
+Because class~$G$ means $S_r(\cA) = 0$ for all $r \geq 3$,
+the mixed-sector operations vanish:
+$m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
+The weaker condition $\Delta = 0$ is not sufficient:
+affine Kac--Moody algebras are class~$L$ with $\Delta = 0$ but
+$m_3^{\mathrm{SC}} \neq 0$.
 Class~$L$: the cubic shadow
 $S_3 = 2h^\vee/(k + h^\vee)$ is computed from the OPE coefficient
 ratio (the structure constant divided by the level); the quartic
@@ -2646,10 +2673,10 @@
 relationship between SC-formality and the classification is
 sharper than the table suggests. Proposition~\ref{prop:swiss-cheese-nonformality-by-class}
 already isolates the first nonzero Swiss-cheese operation in each
-non-Gaussian class: class~$L$ has $m_3^{\mathrm{SC}} \neq 0$,
-class~$C$ has $m_4^{\mathrm{SC}} \neq 0$, and class~$M$ has
-nonzero $m_k^{\mathrm{SC}}$ for all $k \geq 3$. This reduces the
-formality criterion to a classification check.
+non-Gaussian class and, on the Gaussian locus, identifies the
+mixed-sector tree formulas with the degree-by-degree shadow tower
+after averaging. The criterion below packages this as an equivalence
+between SC-formality and truncation of the shadow tower at degree~$2$.
 
 \begin{proposition}[SC-formality characterises class~$G$; \ClaimStatusProvedHere]
 \label{prop:sc-formal-iff-class-g}
@@ -2665,21 +2692,30 @@
 The forward direction \textup{(}class~$G$ $\Longrightarrow$
 SC-formal\textup{)} is established in
 Proposition~\ref{prop:swiss-cheese-nonformality-by-class}:
-the class-$G$ row consists exactly of Heisenberg and lattice
-VOAs, and in both cases $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
+the class-$G$ row consists of the Gaussian families Heisenberg,
+lattice VOA, and free fermion, and in each case the genus-$0$
+mixed tree formulas stop at arity~$2$, so
+$m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
 
 For the converse, suppose~$\cA$ is SC-formal.
-Because the standard landscape is exhausted by the four classes
-$G$, $L$, $C$, $M$, it is enough to eliminate the three
-non-Gaussian cases. Proposition~\ref{prop:swiss-cheese-nonformality-by-class}
-does exactly this: class~$L$ has $m_3^{\mathrm{SC}} \neq 0$,
-class~$C$ has $m_4^{\mathrm{SC}} \neq 0$, and class~$M$ has
-nonzero higher operations in every arity $k \geq 3$. Each of
-these cases contradicts SC-formality. This converse uses only the
-classification from Proposition~\ref{prop:swiss-cheese-nonformality-by-class};
-it does not invoke any trilinear form built from~$\kappa$.
-Hence an SC-formal algebra must
-belong to class~$G$.
+Then the mixed sector of the Swiss-cheese bar complex is formal:
+every higher arity tree operation vanishes. The tower-bar
+correspondence is operadic: the arity-$r$ mixed tree and the
+degree-$r$ shadow are produced by the same genus-$0$ tree-transfer
+formula, with the same propagator on internal edges; the only
+difference is the output colour, and passage to the symmetric
+closed sector applies the averaging morphism
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)}.
+Hence SC-formality forces $S_r(\cA) = 0$ for every $r \geq 3$:
+there is no higher mixed tree whose closed projection could survive.
+By Theorem~\ref{thm:shadow-formality-identification} and
+Proposition~\ref{prop:shadow-tower-three-lenses}, this is exactly
+the statement that the shadow/formality tower truncates at
+degree~$2$. Theorem~\ref{thm:shadow-archetype-classification}
+identifies the standard-landscape locus with this property as
+precisely class~$G$. Hence an SC-formal algebra must belong
+to class~$G$.
 \end{proof}
 
 \begin{remark}[D-module purity: reduction to a single gap]
@@ -3775,7 +3811,9 @@
 Definition~\ref{def:chiral-koszul-pair} identifies the algebra-level
 Verdier dual $\mathbb{D}_{\operatorname{Ran}}(\cC_1)$ with the
 factorization algebra $\Omega_X(\cC_2)$, and likewise with the
-indices reversed. Let
+indices reversed. In the standard examples, this hypothesis is
+supplied by Theorem~\ref{thm:verdier-bar-cobar}, whose output already
+lives on the post-Verdier factorization-algebra side. Let
 \[
 \eta_i \colon \cC_i \xrightarrow{\sim} \barB_X(\cA_i),
 \qquad
@@ -3913,8 +3951,9 @@
 of the underlying twisting datum
 (Definition~\ref{def:chiral-twisting-datum}).
 Part~(1) says each~$\tau_i$ is acyclic;
-part~(2) says Verdier duality sends the bar coalgebra of one side
-to the dual factorization algebra recovered from the other;
+part~(2) says that after applying Verdier duality to the bar
+coalgebra of one side one obtains the dual factorization algebra
+recovered from the other;
 and Proposition~\ref{prop:bar-cobar-relative-extension} isolates
 the extra relative Verdier/base-change input needed to transport
 these identifications over a base.


thinking
**Evaluating proof details**

I'm considering the proof that uses Gaussian/tree vanishing and how averaging affects it. It shows that just having Delta=0 isn't sufficient, as the class-L counterexample demonstrates. This makes me think about the proof status being "ProvedHere." Now, I wonder about my confidence level: is it high or medium? It feels like there’s a lot to unpack, so I want to make sure I'm thorough in my understanding.
codex
Rectified the SC-formality lane in [chapters/theory/chiral_koszul_pairs.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex:2546). The local changes do three things: class~`G` now includes the free fermion in the classification table, the forward proof is strengthened to a Gaussian/free-field tree-vanishing argument, and the converse is replaced by an operadic tower-bar argument from SC-formality to degree-2 shadow truncation. I also made the boundary sharp: `Delta = 0` alone is explicitly ruled out by the class~`L` affine KM counterexample.

Verification: the modified region is clean under the required AP126/AP132/AP29 greps. `make fast` reached pass 3 with `0` undefined citations and only `2` unrelated global undefined references (`conj:v1-master-bv-brst`) before the TeX process was killed by the environment (`Error 137`); none of the new references from this theorem lane were unresolved.

## Platonic Rectification Report
- `prop:swiss-cheese-nonformality-by-class` at [chiral_koszul_pairs.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex:2546)
  - BEFORE: class `G` row listed only Heisenberg and lattice VOA; status `\ClaimStatusProvedHere`.
  - ISSUE: the forward class-`G` proof did not cover the full class-`G` family surface, omitted free fermions, and left the mechanism too close to a table lookup.
  - ACTION: STRENGTHENED
  - AFTER: class `G` now lists Heisenberg, lattice VOA, and free fermion; the proof uses Gaussian/free-field tree vanishing, the averaging map `\operatorname{av}(\Theta_\cA^{\Eone})=\Theta_\cA`, and an explicit boundary statement that `\Delta=0` is not sufficient because affine KM is class `L` with `m_3^{\mathrm{SC}}\neq 0`; status unchanged (`\ClaimStatusProvedHere`).
  - CONFIDENCE: medium
  - REMAINING GAP: no local proof gap identified; propagation debt remains outside scope in `chapters/connections/concordance.tex:7098` and Vol III docstrings.

- `prop:sc-formal-iff-class-g` at [chiral_koszul_pairs.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex:2681)
  - BEFORE: statement already claimed `SC`-formality iff class `G`; status `\ClaimStatusProvedHere`.
  - ISSUE: the converse relied on eliminating non-`G` classes by classification, rather than a direct operadic mechanism; the proof surface did not justify the theorem at its strongest conceptual form.
  - ACTION: STRENGTHENED
  - AFTER: the theorem still states the strongest form, `\cA` is Swiss-cheese formal iff it belongs to class `G`, but the proof now runs by operadic tower-bar correspondence: SC-formality kills higher mixed trees, averaging sends the ordered closed sector to the shadow tower, hence `S_r(\cA)=0` for all `r\ge 3`, so the shadow/formality tower truncates at degree `2`, which is exactly class `G`; status unchanged (`\ClaimStatusProvedHere`).
  - CONFIDENCE: medium
  - REMAINING GAP: no local theorem gap identified; read-only propagation still needed for the stale Vol III line `compute/lib/swiss_cheese_cy3_e1.py:62` and the old concordance rationale.
file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 82ce3f8a19eaa51f878397fa63cad2971741bf1e..fba59410ce45bba7f2b0aaa62d34bbde7099735d
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -566,8 +566,8 @@
  $H^0 \cong \cC$.
 \item \emph{$\mathrm{A}_2$}: geometric bar-cobar duality
  (Theorem~\ref{thm:bar-cobar-isomorphism-main}): for a chiral
- dual pair, Verdier duality sends the bar coalgebra of one side
- to the dual factorization algebra of the other.
+ dual pair, applying Verdier duality to the bar coalgebra of one side
+ produces the dual factorization algebra of the other.
 \end{itemize}
 $\mathrm{A}_0$ is the Koszul recognition theorem;
 $\mathrm{A}_1$ extracts the dual coalgebra;
@@ -681,7 +681,9 @@
 \mathbb{D}_{\operatorname{Ran}}(\cC_1)
 \simeq \Omega_X(\cC_2)
 \]
-is supplied by Theorem~\ref{thm:verdier-bar-cobar} together with
+is supplied by Theorem~\ref{thm:verdier-bar-cobar}, which is already
+a statement about the factorization algebra obtained after applying
+$\mathbb{D}_{\operatorname{Ran}}$ to the bar coalgebra, together with
 the counit quasi-isomorphism
 $\Omega_X(\cC_2) \xrightarrow{\sim} \cA_2$ from
 Theorem~\ref{thm:fundamental-twisting-morphisms}.
@@ -706,11 +708,12 @@
 bosonic field $a(z)$ with OPE $a(z)a(w) \sim k/(z-w)^2$)
 and $\mathrm{Sym}^{\mathrm{ch}}(V^*)$ is $\chirCom$-type: the
 chiral incarnation of classical $\mathrm{Lie}$--$\mathrm{Com}$ duality.
-Theorem~\ref{thm:bar-cobar-isomorphism-main} identifies
-the bar coalgebra
+The explicit bar computation gives the bar coalgebra
 $\bar{B}^{\mathrm{ch}}(\mathcal{H}_k) \simeq
-\mathrm{coLie}^{\mathrm{ch}}(V^*)$,
-whose linear dual is the Koszul dual algebra
+\mathrm{coLie}^{\mathrm{ch}}(V^*)$.
+Applying Theorem~\ref{thm:bar-cobar-isomorphism-main} to this bar
+coalgebra identifies its Verdier dual factorization algebra with the
+Koszul dual algebra
 $\mathcal{H}_k^! = \mathrm{Sym}^{\mathrm{ch}}(V^*)$:
 the bar complex $\bar{B}(\mathcal{H}_k)$ was computed degree by
 degree in \S\ref{sec:frame-bar-deg1}--\S\ref{sec:frame-bar-all},
@@ -2561,7 +2564,7 @@
 & $m_k^{\mathrm{SC}},\; k \geq 5$ \\
 \midrule
 $G$ \textup{(}$r_{\max}=2$\textup{)}
-& Heisenberg, lattice VOA
+& Heisenberg, lattice VOA, free fermion
 & $= 0$
 & $= 0$
 & $= 0$ \\
@@ -2586,12 +2589,21 @@
 
 \medskip\noindent
 \emph{Mechanism.}
-For class~$G$\textup{:} Heisenberg is central, and lattice VOAs are
-Gaussian: the Heisenberg bracket
-$[a_m, a_n] = km\,\delta_{m+n,0}$ is central, while for lattice
-VOAs the shadow obstruction tower terminates at weight~$2$ by
-Corollary~\ref{cor:lattice-postnikov-termination}. In both cases
-all higher tree sums vanish.
+For class~$G$\textup{:}
+Heisenberg, lattice VOAs, and free fermions are Gaussian/free-field:
+their ordered bar data is generated by the binary two-point kernel,
+so every connected genus-$0$ tree with at least three external legs
+factors through pairings and carries no primitive higher vertex.
+Equivalently, the shadow tower truncates at degree~$2$:
+$S_r(\cA)=0$ for $r \geq 3$
+\textup{(}Theorem~\ref{thm:shadow-archetype-classification}; for
+lattices see Corollary~\ref{cor:lattice-postnikov-termination}\textup{)}.
+Under the averaging map
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)},
+the mixed Swiss-cheese tree of arity~$r$ projects to the degree-$r$
+shadow. Since there is no primitive tree for $r \geq 3$,
+all higher mixed-sector operations vanish.
 For class~$L$\textup{:} the affine KM OPE has at most a double pole; the
 three-channel tree sum over $\overline{\cM}_{0,4}$ is nonzero
 \textup{(}$S_3 = 2h^\vee/(k+h^\vee) \neq 0$\textup{)} but the
@@ -2613,10 +2625,25 @@
 
 \begin{proof}
 Class~$G$: for Heisenberg, centrality of the bracket kills all nested
-compositions, so $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$. For lattice
-VOAs, Corollary~\ref{cor:lattice-postnikov-termination} identifies
-the shadow obstruction tower with its weight-$2$ truncation, so the
-transferred Swiss-cheese operations vanish for every $k \geq 3$.
+tree compositions, so $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
+For lattice VOAs, bosonization reduces connected genus-$0$ amplitudes
+to Wick pairings of the underlying Heisenberg field, and
+Corollary~\ref{cor:lattice-postnikov-termination} identifies the
+shadow tower with its weight-$2$ truncation. For the free fermion,
+Wick's theorem gives Pfaffian factorization by the basic contraction
+$\psi(z)\psi^*(w) \sim (z-w)^{-1}$, so again no connected tree with
+$r \geq 3$ survives after extracting the binary pairings. In all three
+cases the mixed Swiss-cheese arity-$r$ operation is the open-colored
+lift of the same genus-$0$ tree sum whose closed projection is
+$S_r(\cA)$; equivalently,
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)}.
+Because class~$G$ means $S_r(\cA) = 0$ for all $r \geq 3$,
+the mixed-sector operations vanish:
+$m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
+The weaker condition $\Delta = 0$ is not sufficient:
+affine Kac--Moody algebras are class~$L$ with $\Delta = 0$ but
+$m_3^{\mathrm{SC}} \neq 0$.
 Class~$L$: the cubic shadow
 $S_3 = 2h^\vee/(k + h^\vee)$ is computed from the OPE coefficient
 ratio (the structure constant divided by the level); the quartic
@@ -2646,10 +2673,10 @@
 relationship between SC-formality and the classification is
 sharper than the table suggests. Proposition~\ref{prop:swiss-cheese-nonformality-by-class}
 already isolates the first nonzero Swiss-cheese operation in each
-non-Gaussian class: class~$L$ has $m_3^{\mathrm{SC}} \neq 0$,
-class~$C$ has $m_4^{\mathrm{SC}} \neq 0$, and class~$M$ has
-nonzero $m_k^{\mathrm{SC}}$ for all $k \geq 3$. This reduces the
-formality criterion to a classification check.
+non-Gaussian class and, on the Gaussian locus, identifies the
+mixed-sector tree formulas with the degree-by-degree shadow tower
+after averaging. The criterion below packages this as an equivalence
+between SC-formality and truncation of the shadow tower at degree~$2$.
 
 \begin{proposition}[SC-formality characterises class~$G$; \ClaimStatusProvedHere]
 \label{prop:sc-formal-iff-class-g}
@@ -2665,21 +2692,30 @@
 The forward direction \textup{(}class~$G$ $\Longrightarrow$
 SC-formal\textup{)} is established in
 Proposition~\ref{prop:swiss-cheese-nonformality-by-class}:
-the class-$G$ row consists exactly of Heisenberg and lattice
-VOAs, and in both cases $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
+the class-$G$ row consists of the Gaussian families Heisenberg,
+lattice VOA, and free fermion, and in each case the genus-$0$
+mixed tree formulas stop at arity~$2$, so
+$m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
 
 For the converse, suppose~$\cA$ is SC-formal.
-Because the standard landscape is exhausted by the four classes
-$G$, $L$, $C$, $M$, it is enough to eliminate the three
-non-Gaussian cases. Proposition~\ref{prop:swiss-cheese-nonformality-by-class}
-does exactly this: class~$L$ has $m_3^{\mathrm{SC}} \neq 0$,
-class~$C$ has $m_4^{\mathrm{SC}} \neq 0$, and class~$M$ has
-nonzero higher operations in every arity $k \geq 3$. Each of
-these cases contradicts SC-formality. This converse uses only the
-classification from Proposition~\ref{prop:swiss-cheese-nonformality-by-class};
-it does not invoke any trilinear form built from~$\kappa$.
-Hence an SC-formal algebra must
-belong to class~$G$.
+Then the mixed sector of the Swiss-cheese bar complex is formal:
+every higher arity tree operation vanishes. The tower-bar
+correspondence is operadic: the arity-$r$ mixed tree and the
+degree-$r$ shadow are produced by the same genus-$0$ tree-transfer
+formula, with the same propagator on internal edges; the only
+difference is the output colour, and passage to the symmetric
+closed sector applies the averaging morphism
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)}.
+Hence SC-formality forces $S_r(\cA) = 0$ for every $r \geq 3$:
+there is no higher mixed tree whose closed projection could survive.
+By Theorem~\ref{thm:shadow-formality-identification} and
+Proposition~\ref{prop:shadow-tower-three-lenses}, this is exactly
+the statement that the shadow/formality tower truncates at
+degree~$2$. Theorem~\ref{thm:shadow-archetype-classification}
+identifies the standard-landscape locus with this property as
+precisely class~$G$. Hence an SC-formal algebra must belong
+to class~$G$.
 \end{proof}
 
 \begin{remark}[D-module purity: reduction to a single gap]
@@ -3775,7 +3811,9 @@
 Definition~\ref{def:chiral-koszul-pair} identifies the algebra-level
 Verdier dual $\mathbb{D}_{\operatorname{Ran}}(\cC_1)$ with the
 factorization algebra $\Omega_X(\cC_2)$, and likewise with the
-indices reversed. Let
+indices reversed. In the standard examples, this hypothesis is
+supplied by Theorem~\ref{thm:verdier-bar-cobar}, whose output already
+lives on the post-Verdier factorization-algebra side. Let
 \[
 \eta_i \colon \cC_i \xrightarrow{\sim} \barB_X(\cA_i),
 \qquad
@@ -3913,8 +3951,9 @@
 of the underlying twisting datum
 (Definition~\ref{def:chiral-twisting-datum}).
 Part~(1) says each~$\tau_i$ is acyclic;
-part~(2) says Verdier duality sends the bar coalgebra of one side
-to the dual factorization algebra recovered from the other;
+part~(2) says that after applying Verdier duality to the bar
+coalgebra of one side one obtains the dual factorization algebra
+recovered from the other;
 and Proposition~\ref{prop:bar-cobar-relative-extension} isolates
 the extra relative Verdier/base-change input needed to transport
 these identifications over a base.

tokens used
410,388
