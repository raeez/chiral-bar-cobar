# T04_thm_C1 (460s, gpt-5.4)

- [CRITICAL] [thqg_symplectic_polarization.tex:476](/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_symplectic_polarization.tex:476), [thqg_symplectic_polarization.tex:694](/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_symplectic_polarization.tex:694) — The theorem claims for every `g >= 0` that `Q_g(\cA) \cong Q_g(\cA^!)^\vee`, but the same file later proves `Q_0(\cA)=Z(\cA)` and `Q_0(\cA^!)=0`. No hypothesis forces `Z(\cA)=0`, so the genus-`0` boundary case contradicts the theorem as stated. The same contradiction propagates to [higher_genus_complementarity.tex:455](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:455) and [higher_genus_complementarity.tex:1701](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:1701).

- [CRITICAL] [thqg_symplectic_polarization.tex:197](/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_symplectic_polarization.tex:197), [thqg_symplectic_polarization.tex:220](/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_symplectic_polarization.tex:220), [thqg_symplectic_polarization.tex:163](/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_symplectic_polarization.tex:163) — The cochain involution `\sigma` is not actually constructed at the claimed unconditional level. The displayed definition uses an `ev` map `\mathbf C_g(\cA)^{\vee\vee} -> \mathbf C_g(\cA)` with no reflexivity/perfectness hypothesis or local justification, and this `\vee\vee` construction does not reappear elsewhere in the audited surfaces. Even the ambient-complex input quietly imports finite-dimensional fiber-cohomology from the perfectness criterion. That is a hidden assumption exactly where the theorem claims “no perfectness.”

- [CRITICAL] [thqg_symplectic_polarization.tex:592](/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_symplectic_polarization.tex:592), [higher_genus_complementarity.tex:1514](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:1514), [higher_genus_complementarity.tex:843](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:843) — Stage 3 does not follow from its citations. The proof identifies `+1/-1` eigencochains with `j_*/j_!` bar sectors and with `Q_g`, but `lem:eigenspace-decomposition-complete` is only a cohomology-level statement about `H^*(...)^\pm = Q_g`, and `lem:quantum-from-ss` only defines `Q_g` as `gr^g H^*(\bar B)` while explicitly deferring the eigenspace identification to that later lemma. So the core step proving “which summand is `\cA` and which is `\cA^!`” is unsupported.

- [HIGH] [thqg_symplectic_polarization.tex:621](/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_symplectic_polarization.tex:621), [thqg_symplectic_polarization.tex:388](/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_symplectic_polarization.tex:388) — The duality part of the proof is conditional as written. Stage 4 invokes `lem:thqg-III-nondegeneracy`, but that lemma assumes the relative bar family is perfect. The note at lines 633-640 says an unconditional proof could instead come from `cor:quantum-dual-complete`, but that alternative argument is not actually supplied.

- [HIGH] [concordance.tex:4954](/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:4954), [higher_genus_complementarity.tex:72](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:72), [higher_genus_complementarity.tex:455](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:455), [higher_genus_complementarity.tex:1783](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:1783) — The claim surface drifts on the central question “why Lagrangian, and is it unconditional?” The concordance and chapter introduction treat C1 as the direct-sum/eigenspace decomposition and C2 as the conditional Lagrangian upgrade via the Verdier pairing. But the main theory theorem and the later proposition promote Lagrangianity and perfect pairing to unconditional statements. The pairing in play is the Verdier pairing, but the manuscript does not maintain a consistent status boundary for its nondegeneracy or for the Lagrangian conclusion.

- [MEDIUM] [thqg_symplectic_polarization.tex:419](/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_symplectic_polarization.tex:419), [thqg_symplectic_polarization.tex:444](/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_symplectic_polarization.tex:444), [thqg_symplectic_polarization.tex:719](/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_symplectic_polarization.tex:719) — The genus-`1` scope is not fixed consistently. The theorem and ambient complex are stated over `\overline{\mathcal M}_g`, the degree-shift proof uses `\dim_\C \overline{\mathcal M}_g = 3g-3`, but the same file then switches to `\overline{\mathcal M}_{1,1}` for the actual genus-`1` computations. That leaves the genus-`1` boundary case formally ambiguous.

## Summary
Instances checked: 13 | Violations found: 6 | Verdict: FAIL

The eigenspace decomposition itself is supposed to be the `\pm1` splitting of the Verdier involution. The alleged Lagrangian property comes from the Verdier pairing. On the audited source, Stage 1-2 are only formal once a genuine cochain involution exists; Stage 3 is unsupported; Stage 4 is conditional; and the all-genera statement already breaks at `g=0`.


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
session id: 019d8388-33a9-7cb1-ab81-a042bc9e97dc
--------
user
<task>
You are an ADVERSARIAL mathematical auditor for a 4,500-page research mathematics manuscript on operadic Koszul duality in the chiral realm (3 volumes). Your mission is FALSIFICATION — assume everything is WRONG until independently verified from first principles. DO NOT modify any files. Only READ and REPORT.
</task>

<grounding_rules>
Ground every claim in file contents or tool outputs you actually read. If a point is inference, label it clearly. Never present guesses as facts.
</grounding_rules>

<completeness_contract>
Resolve the audit fully. Do not stop at the first finding. Check for second-order failures, edge cases, and downstream propagation.
</completeness_contract>

<verification_loop>
Before finalizing, re-verify each finding against the actual file contents. Remove false positives. Keep only genuine discrepancies.
</verification_loop>

<structured_output_contract>
Return findings ordered by severity:
- [CRITICAL] file:line — description
- [HIGH] file:line — description
- [MEDIUM] file:line — description
- [LOW] file:line — description

End with:
## Summary
Instances checked: N | Violations found: N | Verdict: PASS/FAIL
</structured_output_contract>

<default_follow_through_policy>
Keep going until you have enough evidence. Do not stop to ask questions.
</default_follow_through_policy>


MISSION: FALSIFY the proof of Theorem C1: Lagrangian eigenspace decomposition (unconditional). Check: (a) what is the eigenspace decomposition? (b) why is it Lagrangian? (c) what pairing? (d) is it really unconditional?

Search the chapters/ directory for the theorem. Read the full statement AND proof.
For EACH step of the proof:
1. Does this step follow logically from previous steps?
2. Are all cited lemmas/propositions actually proved?
3. Is the scope correct (genus, level, type, family)?
4. Are there hidden assumptions?
5. Could a counterexample exist at boundary values?

Look for: circular reasoning, scope inflation, missing hypotheses, conflation of distinct objects, convention errors, status inflation.
mcp startup: no servers

thinking
**Updating commentary plan**

I’m considering reading the theorem_registry and the concordance to check the status of theorem C1. The red team summary might also be relevant, but since the user specifically asked to search chapters, I should focus on that. I realize I need to provide an update plan since this could require substantial work. It seems like a good idea to start my commentary with an acknowledgment and clarification of my first steps, possibly including a skill announcement too.
codex
Using `deep-beilinson-audit` because this is an adversarial proof audit. I’m locating Theorem C1, its full proof, and every cited dependency before I test the logic and scope.
Plan update
  → Locate Theorem C1 statement, proof, and status surfaces in chapters/ plus concordance/registry
  • Read cited lemmas/propositions and verify whether each proof step is supported
  • Check scope, hidden assumptions, boundary cases, and downstream propagation across volumes
  • Re-verify findings against source lines and produce severity-ordered audit report

thinking
**Considering skill file access**

I think I might need to open the skill file, specifically "deep-beilinson-audit SKILL," and maybe "claim-surface-sync" for theorem status. The primary focus seems to be the audit skill. I'll use `exec_command` to read the file since no modifications should be made. It might be faster to read AGENTS in parallel. I plan to use a multi-tool parallel approach for efficiency, especially to look into theorem C1 and related chapters.
codex
I’m reading the audit workflow and locating every live surface where `Theorem C1` appears so the proof check is tied to the exact claim and status boundary.
exec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/deep-beilinson-audit/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "Theorem C1|thm:.*C1|C1[: ]|Lagrangian eigenspace decomposition|eigenspace decomposition" chapters metadata CLAUDE.md' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
---
name: deep-beilinson-audit
description: Use when the user asks to audit, falsify, red-team, pressure-test, or verify a theorem, chapter, proof, compute module, or frontier claim in this repository. Not for straightforward local edits that do not require an adversarial audit.
---

# Deep Beilinson Audit

Run this skill when correctness matters more than speed and the task is to challenge a claim, not merely improve its presentation.

## Load first

- `CLAUDE.md`
- `chapters/connections/concordance.tex`
- `metadata/theorem_registry.md`
- `archive/raeeznotes/raeeznotes100/red_team_summary.md`
- the target files
- the directly cited dependencies

For status-heavy work, also load the relevant metadata files.

 succeeded in 51ms:
CLAUDE.md:488:| C | PROVED | Complementarity; C0 (fiber-center identification) unconditional, C1 (Lagrangian eigenspace) unconditional, C2 (scalar BV pairing) conditional on uniform-weight |
CLAUDE.md:545:**shadow/Hochschild** (AP94, AP95, AP96, AP97, AP98, AP100, AP102): ChirHoch*(Vir_c) concentrated in degrees {0,1,2}. NEVER C[Theta]. ChirHoch != Gelfand-Fuchs (GF infinite-dim, ChirHoch bounded). Shadow algebra has graded Lie bracket, NOT ring. av: g^{E_1}->g^mod is LOSSY; av(r(z))=kappa. kappa Eulerian weight parity-dependent. Theorem C: C0 fiber-center; C1 Lagrangian eigenspace decomposition unconditional; C2 shifted symplectic/BV upgrade conditional. Scalar kappa+kappa'=K follows from C1 + Theorem D, not from C2. Theorems must specify which bar: B^ord, B^Sigma, or B^Lie.
chapters/examples/w_algebras_deep.tex:1052:Theorem~\ref{thm:master-pbw} (MC1 for principal $\mathcal{W}$-algebras).
chapters/examples/w_algebras_deep.tex:1226:Theorem~\ref{thm:master-pbw} (MC1 for principal
metadata/dependency_graph.dot:940:  thm_thqg_III_eigenspace_decomposition [label="thm:thqg-III-eigenspace-decomposition\ntheorem [Pr]\nHolographic eigenspace decomposition (C1...", style=filled, fillcolor="#c8e6c9"];
metadata/dependency_graph.dot:2085:  thm_uniform_pbw_bridge [label="thm:uniform-pbw-bridge\ntheorem [Pr]\nUniform PBW bridge from MC1 to MC4", style=filled, fillcolor="#c8e6c9"];
metadata/theorem_registry.md:149:| `thm:uniform-pbw-bridge` | `theorem` | 1919 | Uniform PBW bridge from MC1 to MC4 |
metadata/theorem_registry.md:3065:| `thm:thqg-III-eigenspace-decomposition` | `theorem` | 474 | Holographic eigenspace decomposition (C1) |
chapters/connections/outlook.tex:259:MC1 through MC4 are proved. MC5 is partially proved: the analytic
chapters/frame/preface_sections10_13_draft.tex:368:MC1 through MC4 are proved; MC5 is partially proved. The analytic HS-sewing package is proved at all genera; the genus-$0$ algebraic BRST/bar comparison is proved; BV=bar in the coderived category is proved for all four shadow classes (including class~M). The genuswise chain-level BV/BRST/bar identification remains conjectural (class~M chain-level false), and the tree-level amplitude pairing is conditional.
chapters/connections/editorial_constitution.tex:141:MC1 & PBW concentration
chapters/connections/editorial_constitution.tex:157:resolved load-bearing layers (the MC1 entry theorem and the MC2
chapters/connections/editorial_constitution.tex:176:bridge from MC1 (Theorem~\ref{thm:uniform-pbw-bridge}).
chapters/connections/editorial_constitution.tex:206:\emph{This resolves MC1 for the standard finite-type interacting
chapters/connections/editorial_constitution.tex:213:of MC1 for the named families rests on the family theorems above;
chapters/connections/editorial_constitution.tex:367:bridge (Theorem~\ref{thm:uniform-pbw-bridge}) connects MC1 to MC4.
chapters/connections/editorial_constitution.tex:481:it resolves MC1 for the standard finite-type interacting families.
chapters/connections/editorial_constitution.tex:774:bridge (Theorem~\ref{thm:uniform-pbw-bridge}) connects MC1 to MC4.
chapters/connections/editorial_constitution.tex:798:MC1 & \textbf{Proved} (Thm~\ref{thm:master-pbw})
chapters/connections/arithmetic_shadows.tex:9382:preserves the Hecke eigenspace decomposition at every
codex
I’ve located the claimed `C1` surface in `thqg_symplectic_polarization.tex`. Next I’m reading the theorem, its proof, the construction it cites, and the concordance/registry status entries to see whether the “unconditional” tag is actually supported.
exec
/bin/zsh -lc "sed -n '3048,3084p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '450,620p' chapters/connections/thqg_symplectic_polarization.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '620,760p' chapters/connections/thqg_symplectic_polarization.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "thqg-III-eigenspace-decomposition|C1|Lagrangian eigenspace|Verdier involution" chapters/connections/concordance.tex archive/raeeznotes/raeeznotes100/red_team_summary.md CLAUDE.md' in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
\]
The duality $Q_g(\cA) \cong Q_g(\cA^!)^{\vee}$ follows from
the Verdier pairing. For $v \in Q_g(\cA)$ and
$w \in Q_g(\cA^!)$, the pairing $\langle v, w \rangle_g$
is nondegenerate: if $\langle v, w \rangle_g = 0$ for all
$w \in Q_g(\cA^!)$, then $v$ lies in the radical of the
restricted pairing. Since
$\langle Q_g(\cA), Q_g(\cA) \rangle_g = 0$
(isotropy from anti-symmetry of $\sigma$),
$v$ lies in the radical of the full pairing on
$\mathcal{H}_g(\cA)$, which is zero by nondegeneracy
(Lemma~\ref{lem:thqg-III-nondegeneracy}).

\emph{Note on unconditionality.}
Stages 1--3 use only $\sigma^2 = \id$ and the
identification of $\sigma$-eigenspaces with $j_*/j_!$
extensions. No perfectness or nondegeneracy hypothesis is
needed. The duality statement in Stage~4 uses
nondegeneracy but can also be obtained unconditionally from
spectral sequence duality
 succeeded in 51ms:
is $\overline{\mathcal{M}}_{1,1}$, where the pairing has
degree~$0$. This is the reason genus~$1$ complementarity
has the simplest form:
$Q_1(\cA) \oplus Q_1(\cA^!) \cong H^*(\overline{\mathcal{M}}_{1,1},
\mathcal{Z}(\cA))$ with a classical (unshifted) pairing.
\end{remark}

% ======================================================================
%
% 2. THE UNCONDITIONAL EIGENSPACE DECOMPOSITION (C1)
%
% ======================================================================

\subsection{The unconditional eigenspace decomposition}
\label{subsec:thqg-III-eigenspace-decomposition}
\index{eigenspace decomposition!holographic|textbf}
\index{complementarity!C1 decomposition}

The eigenspace decomposition~(C1) holds unconditionally on the
Koszul locus, requiring no perfectness or nondegeneracy hypotheses.
 succeeded in 51ms:
| `comp:thqg-VI-virasoro-quintic-soft` | `computation` | 1684 | Quintic soft factor for Virasoro |
| `prop:thqg-VI-inductive-nontermination` | `proposition` | 1719 | Inductive non-termination for class $\mathbf{M}$ |
| `prop:thqg-VI-polynomial-growth` | `proposition` | 1800 | Polynomial growth of soft factors |
| `cor:thqg-VI-soft-convergence` | `corollary` | 1849 | Convergence of the soft expansion |
| `prop:thqg-VI-celestial-structure` | `proposition` | 1916 | Structure of the celestial soft algebra |
| `thm:thqg-VI-soft-ope` | `theorem` | 1996 | Soft graviton OPE |
| `prop:thqg-VI-asymptotic-symmetry` | `proposition` | 2067 | Asymptotic symmetry algebra from the shadow obstruction tower |

#### `chapters/connections/thqg_symplectic_polarization.tex` (16)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:thqg-III-ambient-properties` | `proposition` | 126 | Properties of the holographic ambient complex |
| `prop:thqg-III-involutivity` | `proposition` | 237 | Involutivity and anti-symmetry |
| `prop:thqg-III-mc-compatibility` | `proposition` | 297 | Compatibility with the modular MC element |
| `lem:thqg-III-nondegeneracy` | `lemma` | 388 | Nondegeneracy of the holographic pairing |
| `prop:thqg-III-degree-shift` | `proposition` | 421 | Degree shift at each genus |
| `thm:thqg-III-eigenspace-decomposition` | `theorem` | 474 | Holographic eigenspace decomposition (C1) |
| `cor:thqg-III-complementarity-exchange` | `corollary` | 655 | Complementarity exchange principle |
| `cor:thqg-III-dimension-parity` | `corollary` | 678 | Dimension parity |
 succeeded in 52ms:
CLAUDE.md:219:Canonical source for every formula. Never write from memory; cite this census or landscape_census.tex. Each entry has (canonical form, two sanity checks, wrong variants). Source: true_formula_census_draft_wave12.md (C1-C31 full entries).
CLAUDE.md:221:**C1. Heisenberg kappa.** `kappa(H_k) = k`. Checks: k=0 -> 0; k=1 -> 1 (matches c_Heis(1)=1). Wrong: k/2 (Vir pattern-match), k*dim/(2h^v) (KM paste).
CLAUDE.md:237:**C9. Affine KM classical r-matrix.** Two equivalent conventions coexist: (i) trace-form `r(z) = k*Omega/z` where Omega is the inverse Killing form Casimir (d-log absorption of OPE double pole; level prefix k MANDATORY, AP126); (ii) KZ normalization `r(z) = Omega/((k+h^v)*z)` (collision-residue dualization; Sugawara denominator). Bridge identity: `k*Omega_tr = Omega/(k+h^v)` at generic k. Checks (trace-form): k=0 -> r=0 (abelian limit, double pole vanishes); k=-h^v -> critical level. Checks (KZ): k=0 -> Omega/(h^v*z) != 0 (Lie bracket persists for non-abelian g); k=-h^v -> diverges (Sugawara singularity). Averaging: av(k*Omega/z) = k*dim(g)/(2h^v) = kappa_dp (double-pole channel); full kappa = av(r) + dim(g)/2 (Sugawara shift from simple-pole self-contraction, see C13). Wrong: Omega/z (bare, AP126 -- MOST VIOLATED); k*Omega/z^2 (double pole).
CLAUDE.md:239:**C10. Heisenberg classical r-matrix.** `r^Heis(z) = k/z`. Checks: k=0 -> 0; av(k/z)=k=kappa. Wrong: k/z^2 (OPE pole confusion); 1/z (level stripped).
CLAUDE.md:241:**C11. Virasoro classical r-matrix.** `r^Vir(z) = (c/2)/z^3 + 2T/z`. Cubic + simple, NOT quartic. Check: OPE has quartic pole; d-log absorbs one (AP19). Wrong: (c/2)/z^4 (forgets absorption); c/z^3 (drops 1/2 and 2T/z).
CLAUDE.md:243:**C12. r-matrix/OPE pole absorption.** `pole_r = pole_OPE - 1` via d-log absorption. Heis OPE ~ 1/z^2 -> r ~ 1/z; Vir OPE ~ 1/z^4 -> r ~ 1/z^3.
CLAUDE.md:245:**C13. Averaging map identity.** `av(r(z)) = kappa(A)` at degree 2 for abelian algebras (Heisenberg, free fields): direct. For NON-ABELIAN KM (trace-form convention r=k*Omega/z): `av(r(z)) = k*dim(g)/(2h^v) = kappa_dp` (double-pole channel only). The full kappa includes the Sugawara shift: `kappa(V_k(g)) = av(r(z)) + dim(g)/2 = dim(g)*(k+h^v)/(2h^v)`. The dim(g)/2 term is kappa_sp, the simple-pole self-contraction through the adjoint Casimir eigenvalue 2h^v (proved at kac_moody.tex:1430-1474, introduction.tex:1182, higher_genus_modular_koszul.tex:3060). Wrong: `av(r)=k` for KM (bare level, forgets trace); `av(r)=kappa` for non-abelian KM without Sugawara shift (FM11).
CLAUDE.md:247:**C14. Bar complex uses augmentation ideal.** `B(A) = T^c(s^{-1} A-bar)`, `A-bar = ker(epsilon)`. NOT `T^c(s^{-1} A)` (AP132). NOT `T^c(s A-bar)` (AP22). NOT `T(s^{-1} A-bar)` (tensor ALGEBRA loses deconcatenation).
CLAUDE.md:249:**C15. Desuspension grading.** `|s^{-1} v| = |v| - 1`. Mnemonic: bar = down = desuspension = s^{-1}. Wrong: `+1` (suspension direction).
CLAUDE.md:251:**C16. E_8 fundamental dimensions.** `{248, 3875, 30380, 147250, 2450240, 6696000, 146325270, 6899079264}`. Adjoint = omega_1 = 248. Sum = 7056003287. Wrong: 779247 (not any E_8 irreducible, Wave 10-8 error); 3875 as adjoint (confusing omega_2 with omega_1). Source: `compute/lib/bc_exceptional_categorical_zeta_engine.py::FUNDAMENTAL_DIMS['E8']`.
CLAUDE.md:253:**C17. W_N conformal weight range.** Generators at `s in {2, 3, ..., N}`. N-1 generators, highest weight N. Checks: W_2 -> {2} = Vir; W_3 -> {2,3}. Wrong: `{2,...,N+1}` (extra phantom field); `{1,...,N}` (includes weight-1 field).
CLAUDE.md:255:**C18. Koszul complementarity per family.** `K(A) = kappa(A)+kappa(A^!)`: 0 for KM/Heis/lattice/free; 13 for Vir; 250/3 for W_3; 196 for Bershadsky-Polyakov. NOT universal 0 (AP24).
CLAUDE.md:257:**C19. Harmonic number.** `H_N = sum_{j=1}^{N} 1/j`. H_1=1, H_2=3/2. `H_{N-1} != H_N - 1`: at N=2, H_1=1 but H_2-1=1/2 (AP136).
CLAUDE.md:488:| C | PROVED | Complementarity; C0 (fiber-center identification) unconditional, C1 (Lagrangian eigenspace) unconditional, C2 (scalar BV pairing) conditional on uniform-weight |
CLAUDE.md:491:| MC1-4 | PROVED | PBW, MC element, thick gen (all types), completion tower; MC3 layer 3 (shifted prefundamental generation) unconditional in type A, conditional outside type A |
CLAUDE.md:545:**shadow/Hochschild** (AP94, AP95, AP96, AP97, AP98, AP100, AP102): ChirHoch*(Vir_c) concentrated in degrees {0,1,2}. NEVER C[Theta]. ChirHoch != Gelfand-Fuchs (GF infinite-dim, ChirHoch bounded). Shadow algebra has graded Lie bracket, NOT ring. av: g^{E_1}->g^mod is LOSSY; av(r(z))=kappa. kappa Eulerian weight parity-dependent. Theorem C: C0 fiber-center; C1 Lagrangian eigenspace decomposition unconditional; C2 shifted symplectic/BV upgrade conditional. Scalar kappa+kappa'=K follows from C1 + Theorem D, not from C2. Theorems must specify which bar: B^ord, B^Sigma, or B^Lie.
CLAUDE.md:823:AP144: Convention coexistence without bridge. Different chapters independently develop conventions for the same object (r-matrix: trace-form k*Omega/z vs KZ Omega/((k+h^v)*z); kappa: several families). The conventions agree at generic parameter values but diverge at boundary values (k=0, k=-h^v). When multiple conventions coexist, a BRIDGE IDENTITY must be stated explicitly at every site, and boundary behavior must be checked in EACH convention separately. The r-matrix normalization issue (C9/C13/AP126 inconsistency, resolved April 2026) is the canonical example. After introducing ANY convention for a shared object, grep all three volumes for alternative conventions of the same object and install bridge identities.
chapters/connections/concordance.tex:192: The Verdier involution sends $\Theta_\cA$ to $\Theta_{\cA^!}$,
chapters/connections/concordance.tex:1838:\item \emph{MC1 and MC2}: Pillar~B realizes every algebra as an MC
chapters/connections/concordance.tex:1842: MC1 (PBW concentration) holds unconditionally for universal

thinking
**Searching for theorem details**

I need to read the precise context around theorem C and possibly its status lines. I plan to focus my search on the Construction of the Verdier involution and find specific references like Proposition 237 and Lemma 388. The theorem also cites several specific elements, and I need to locate all of them, some of which might be in different files. I'll look for theorem C in the higher_genus_complementarity.tex document and ensure I check for any cross-volume duplicates.
codex
I have the main proof. Now I’m tracing each cited dependency to see whether the proof imports actual proved statements or just narrative claims, and whether the “Lagrangian” language is earned by the displayed proof.
exec
/bin/zsh -lc "sed -n '1,460p' chapters/connections/thqg_symplectic_polarization.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "constr:thqg-III-verdier-involution|prop:thqg-III-involutivity|lem:eigenspace-decomposition-complete|lem:quantum-from-ss|cor:quantum-dual-complete|lem:thqg-III-nondegeneracy|thm:thqg-III-eigenspace-decomposition|Holographic eigenspace decomposition" chapters metadata' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '4920,4995p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "C1 .*unconditional|Lagrangian eigenspace|eigenspace decomposition.*unconditional|Complementarity; C0 .* C1 .* C2" archive/raeeznotes/raeeznotes100/red_team_summary.md chapters/connections/concordance.tex chapters/theory/higher_genus_complementarity.tex chapters/theory/chiral_koszul_pairs.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
% Section file for Chapter: Twisted Holography and Quantum Gravity
% Result (G3): Complementarity as Shifted-Symplectic Polarization

% Local macros (providecommand only; never \newcommand in chapter files)
\providecommand{\MC}{\mathrm{MC}}
\providecommand{\Defcyc}{\mathrm{Def}_{\mathrm{cyc}}}
\providecommand{\Definfmod}{\mathrm{Def}^{\mathrm{mod}}_\infty}
\providecommand{\Sh}{\mathrm{Sh}}
\providecommand{\gr}{\operatorname{gr}}
\providecommand{\id}{\mathrm{id}}
\providecommand{\Tr}{\operatorname{Tr}}
\providecommand{\Sym}{\operatorname{Sym}}
\providecommand{\Hom}{\operatorname{Hom}}
\providecommand{\End}{\operatorname{End}}
\providecommand{\Spec}{\operatorname{Spec}}
\providecommand{\Res}{\operatorname{Res}}
\providecommand{\rank}{\operatorname{rank}}
\providecommand{\ad}{\operatorname{ad}}
\providecommand{\Fred}{\operatorname{Fred}}
\providecommand{\Map}{\operatorname{Map}}
 succeeded in 50ms:
metadata/dependency_graph.dot:936:  prop_thqg_III_involutivity [label="prop:thqg-III-involutivity\nproposition [Pr]\nInvolutivity and anti-symmetry", style=filled, fillcolor="#c8e6c9"];
metadata/dependency_graph.dot:938:  lem_thqg_III_nondegeneracy [label="lem:thqg-III-nondegeneracy\nlemma [Pr]\nNondegeneracy of the holographic pairing", style=filled, fillcolor="#c8e6c9"];
metadata/dependency_graph.dot:940:  thm_thqg_III_eigenspace_decomposition [label="thm:thqg-III-eigenspace-decomposition\ntheorem [Pr]\nHolographic eigenspace decomposition (C1...", style=filled, fillcolor="#c8e6c9"];
metadata/dependency_graph.dot:2753:  lem_quantum_from_ss [label="lem:quantum-from-ss\nlemma [Pr]\nQuantum corrections as spectral sequence...", style=filled, fillcolor="#c8e6c9"];
metadata/dependency_graph.dot:2758:  cor_quantum_dual_complete [label="cor:quantum-dual-complete\ncorollary [Pr]\nQuantum corrections are dual", style=filled, fillcolor="#c8e6c9"];
metadata/dependency_graph.dot:2762:  lem_eigenspace_decomposition_complete [label="lem:eigenspace-decomposition-complete\nlemma [Pr]\nEigenspace decomposition", style=filled, fillcolor="#c8e6c9"];
metadata/theorem_registry.md:712:| `lem:quantum-from-ss` | `lemma` | 823 | Quantum corrections as spectral sequence limit |
metadata/theorem_registry.md:717:| `cor:quantum-dual-complete` | `corollary` | 1190 | Quantum corrections are dual |
metadata/theorem_registry.md:721:| `lem:eigenspace-decomposition-complete` | `lemma` | 1494 | Eigenspace decomposition |
metadata/theorem_registry.md:3061:| `prop:thqg-III-involutivity` | `proposition` | 237 | Involutivity and anti-symmetry |
metadata/theorem_registry.md:3063:| `lem:thqg-III-nondegeneracy` | `lemma` | 388 | Nondegeneracy of the holographic pairing |
metadata/theorem_registry.md:3065:| `thm:thqg-III-eigenspace-decomposition` | `theorem` | 474 | Holographic eigenspace decomposition (C1) |
metadata/label_index.json:3570:  "constr:thqg-III-verdier-involution": {
metadata/label_index.json:4574:  "cor:quantum-dual-complete": {
metadata/label_index.json:23630:  "lem:eigenspace-decomposition-complete": {
metadata/label_index.json:23826:  "lem:quantum-from-ss": {
metadata/label_index.json:23906:  "lem:thqg-III-nondegeneracy": {
metadata/label_index.json:27494:  "prop:thqg-III-involutivity": {
metadata/label_index.json:49730:  "thm:thqg-III-eigenspace-decomposition": {
metadata/claims.jsonl:904:{"label": "prop:thqg-III-involutivity", "env_type": "proposition", "status": "ProvedHere", "file": "chapters/connections/thqg_symplectic_polarization.tex", "line": 237, "title": "Involutivity and anti-symmetry", "labels_in_block": ["prop:thqg-III-involutivity", "eq:thqg-III-anti-symmetry"], "refs_in_block": ["constr:thqg-III-verdier-involution"]}
 succeeded in 50ms:
$\operatorname{Ran}(X)$. Theorem~\ref{thm:bar-cobar-isomorphism-main}
provides the adjunction; Theorem~\ref{thm:higher-genus-inversion}
provides inversion on the Koszul locus.
Appendix~\ref{app:coderived},
\S\ref{subsec:coderived-ran-formalism} develops the coderived
and contraderived categories on~$\operatorname{Ran}(X)$: curved
factorization coalgebras with CDG-factorization compatibility
(Definition~\ref{def:curved-fact-coalgebra}), coacyclic
factorization objects
(Definition~\ref{def:coacyclic-fact}), stratified conservative
restriction via the injective characterization
(Theorem~\ref{thm:stratified-conservative-restriction}),
and the factorization co-contra correspondence
(Theorem~\ref{thm:fact-co-contra-general}). The provisional
coderived category embeds fully faithfully
(Proposition~\ref{prop:provisional-embedding}).

\emph{Now complete.}
The formerly conjectural off-Koszul bar-cobar inversion on
$\operatorname{Ran}(X)$ is proved
 succeeded in 52ms:
chapters/theory/higher_genus_complementarity.tex:1783:\begin{proposition}[Verdier pairing and Lagrangian eigenspaces; \ClaimStatusProvedHere]
chapters/connections/concordance.tex:1842: MC1 (PBW concentration) holds unconditionally for universal

thinking
**Searching for theorem C details**

I need to find more concordance lines related to theorem C, particularly its status around 1981. It seems there might be some useful information out there that could clarify this. I’ll start by searching specifically for theorem C to gather relevant data. I’m curious about what I might discover and how it can help shed light on its historical context!
codex
The connection chapter’s `C1` proof is already leaning on several theory-chapter lemmas. I’m reading those exact proofs now, especially the earlier “Verdier pairing and Lagrangian eigenspaces” result, because that appears to be the real source of the Lagrangian claim.
exec
/bin/zsh -lc "sed -n '800,910p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
(Artin vanishing for proper DM stacks,
\cite[\S4.1]{Olsson16}).

\emph{(2) Constructibility of the fiber sheaves.}
The fiber cohomology sheaf
$\mathcal{H}^q_{\mathrm{fiber}}(\cA)$ on
$\overline{\mathcal{M}}_g$ is constructible with respect to
the stratification by topological type of stable curve.
On the smooth locus $\mathcal{M}_g$, it is a local system
by Lemma~\ref{lem:fiber-cohomology-center} (constancy of
the center $Z(\cA)$ under variation of complex structure).
On each boundary stratum $D_\Gamma$
(indexed by stable graphs~$\Gamma$), the monodromy
is quasi-unipotent: the Picard--Lefschetz formula gives
monodromy operators $T_e = \mathrm{id} + N_e$ where $N_e$
is nilpotent (one Jordan block per node
$e \in E(\Gamma)$). A local system with quasi-unipotent
monodromy along a normal crossing divisor is constructible
(\cite[\S8.1]{KS90}).

exec
/bin/zsh -lc "sed -n '1778,1868p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1490,1568p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1180,1238p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\emph{Differential $d_1$}: The differential $d_1: E_1^{p,q,g} \to E_1^{p+1,q,g}$ is 
induced by the moduli space differential. Under Verdier duality:
\begin{equation}
\mathbb{D} \circ d_1 = (-1)^{p+q} d_1^\vee \circ \mathbb{D}
\end{equation}
where $d_1^\vee$ is the dual differential.

This sign is precisely the Koszul sign convention (see Appendix~\ref{app:signs}, \S\ref{app:sign-conventions}). 
Thus the differential on $(E_1)_{\mathcal{A}}$ is dual to the differential on 
$(E_1)_{\mathcal{A}^!}$, up to the appropriate sign.

\emph{Higher pages}: By induction, if $(E_r)_{\mathcal{A}} \cong ((E_r)_{\mathcal{A}^!})^\vee$, 
then taking cohomology with respect to $d_r$ preserves this duality:
\begin{equation}
(E_{r+1})_{\mathcal{A}} = H(E_r, d_r)_{\mathcal{A}} \cong (H(E_r, d_r)_{\mathcal{A}^!})^\vee 
= ((E_{r+1})_{\mathcal{A}^!})^\vee
\end{equation}

\emph{$E_\infty$ page}: Taking the limit $r \to \infty$:
\begin{equation}
 succeeded in 52ms:
intersection $\mathcal{L} \times_{\mathcal{M}} \mathcal{L}^!$
carries the $(-1)$-shifted symplectic structure that governs the
Verdier pairing of Proposition~\ref{prop:lagrangian-eigenspaces}.
\end{remark}

\begin{proposition}[Verdier pairing and Lagrangian eigenspaces; \ClaimStatusProvedHere]
\label{prop:lagrangian-eigenspaces}
\index{Lagrangian!eigenspaces|textbf}
\index{Verdier duality!pairing on moduli}
Let $(\cA, \cA^!)$ be a chiral Koszul pair and let
$V = H^*(\overline{\mathcal{M}}_g, \mathcal{Z}(\cA))$.
\begin{enumerate}[label=\textup{(\roman*)}]
\item Verdier duality on the center local system $\mathcal{Z}(\cA)$
 induces a non-degenerate bilinear pairing
 \[
 \langle -, - \rangle_{\mathbb{D}} \colon V \otimes V \to \mathbb{C}
 \]
 of cohomological degree $-(3g-3)$ \textup{(}the shift coming from
 $\dim_{\mathbb{C}} \overline{\mathcal{M}}_g = 3g-3$\textup{)}.
\item The Verdier involution $\sigma$ is an \emph{anti-involution}
 succeeded in 52ms:
$\mathbb{D}$ then exchanges these subquotients, inducing the involution
$\sigma$ on the total space. Explicitly, $\sigma$ acts on the $E_2$ page by:
\begin{equation}
\sigma: E_2^{p,q}(\mathcal{A}) \to E_2^{p,d-q}(\mathcal{A}^!) \cong
E_2^{p,d-q}(\mathcal{A})
\end{equation}
(the last isomorphism via the Koszul identification). This descends to $E_\infty$:
Verdier duality is an exact functor on the derived category of constructible sheaves,
and the Leray spectral sequence is functorial with respect to exact functors.
Therefore $\sigma$, being induced by the composition of Verdier duality with the
Koszul identification, commutes with the spectral sequence differentials $d_r$
at each page (with sign absorbed by the Koszul sign convention, cf.\
Lemma~\ref{lem:ss-duality-complete}).

\emph{Eigenvalue identification.}
The key sign is: $j_*$ and $j_!$ differ by a shift of $2\dim(\partial)$ in the
dualizing complex, which introduces a factor of $(-1)^{\dim \partial}$ in the
eigenvalue identification.

\emph{Involutivity.} $\sigma^2 = \mathrm{id}$ follows from

thinking
**Locating proof details**

I need to find the complete proof for the lem:eigenspace beyond the truncated text at "However, the Verdier involution." I'll read further to gather more context. It seems like I should also revisit steps 7-10 related to the theorem and quantum complementarity. I’ll look for the statement and proof regarding Theorem C specifically, starting from around page 1420 onwards. Plus, I need to locate Step 7 of the main theorem.
exec
/bin/zsh -lc "sed -n '1568,1676p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"quantum-complementarity-main|Step 7:|Step 8: Verdier involution and eigenspace decomposition|Theorem~\\\\ref\\{thm:quantum-complementarity-main\\}|begin\\{theorem\\}\\[Koszul Complementarity at Higher Genus|Complementarity at Higher Genus\" chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1340,1468p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
However, the Verdier involution $\sigma$ on
$\mathcal{H}_g(\mathcal{A})$ identifies $Q_g(\mathcal{A}^!)$ not
through its own spectral sequence but through the $j_! \leftrightarrow j_*$
interchange. Concretely, $\sigma$ sends
$j_!$-extended classes to $j_*$-extended classes.
The eigenvalue is determined by the anti-commutativity
of~$\sigma$ with the Kodaira--Spencer action
\eqref{eq:verdier-ks-anticommute}: for $\beta$ arising from
$\bar{B}^{(g)}(\mathcal{A}^!)$,
\[
\sigma(\beta)
= \sigma\bigl(\text{$j_!$-extension}\bigr)
= \text{$j_*$-extension}
= -\beta
\]
where the sign $-1$ arises because the $j_! \to j_*$ natural
transformation, composed with the Koszul identification
$(\mathcal{A}^!)^! \simeq \mathcal{A}$, picks up the sign from
the anti-commutativity~\eqref{eq:verdier-ks-anticommute}.
Therefore elements from $\bar{B}^{(g)}(\mathcal{A}^!)$ have
 succeeded in 51ms:
39:(Theorem~\ref{thm:quantum-complementarity-main}).
67: \textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main})}.
435:$\mathrm{C}_1$ (Theorem~\ref{thm:quantum-complementarity-main})
456:\label{thm:quantum-complementarity-main}
867:anticipating Theorem~C (Theorem~\ref{thm:quantum-complementarity-main}),
1237:\emph{Step 7: Center action on moduli space cohomology.}
1420:\emph{Step 8: Verdier involution and eigenspace decomposition.}
1740:This completes the proof of Theorem~\ref{thm:quantum-complementarity-main}. \qedhere
1749:Theorem~\ref{thm:quantum-complementarity-main} via three steps.
1821:Theorem~\ref{thm:quantum-complementarity-main}, Step~7), so the
1837:Theorem~\ref{thm:quantum-complementarity-main}), the involution
1858:Theorem~\ref{thm:quantum-complementarity-main} is a Lagrangian
2048: (Theorem~\ref{thm:quantum-complementarity-main}), we have
2183:The conjecture asserts that quantum complementarity (Theorem~\ref{thm:quantum-complementarity-main}) reproduces established physics identifications (central charge duality, marginal-obstruction exchange, electric-magnetic splitting) when applied to specific CFT Koszul pairs.
2203:complementarity decomposition is functorial (property 3 of Theorem~\ref{thm:quantum-complementarity-main}), it commutes with the modular action.
2321:(Theorem~\ref{thm:quantum-complementarity-main}):
2390:(Theorem~\ref{thm:quantum-complementarity-main}) with
2428:The mathematical content is that Theorem~\ref{thm:quantum-complementarity-main}
2682:By Theorem~\ref{thm:quantum-complementarity-main},
2708:(Theorem~\ref{thm:quantum-complementarity-main}),
 succeeded in 51ms:
$\mathbb{D}(\mathcal{F})$ carries the contragredient action
$\rho^\vee = -\rho^t$, which reverses signs):
\begin{equation}\label{eq:verdier-lie-anticommute}
\mathbb{D} \circ \mathcal{L}_{\tilde{v}} = -\mathcal{L}_{\tilde{v}} \circ \mathbb{D}
\end{equation}

Concretely, $\mathbb{D}$ reverses the orientation of the fibers of the FM
compactification, and the Lie derivative reverses sign under orientation reversal.

\emph{Ingredient 2: Verdier duality intertwines center actions via the Koszul pairing.}
For $z \in Z(\mathcal{A})$, the action $\rho(z)$ on the bar complex
$\bar{B}^{(g)}(\mathcal{A})$ is a $\mathcal{D}$-module endomorphism (since $z$ is
central). The Koszul pairing $\mathcal{A} \otimes \mathcal{A}^! \to \omega_X$ restricts
to a perfect pairing on centers $Z(\mathcal{A}) \otimes Z(\mathcal{A}^!) \to \mathbb{C}$:
the module Koszul duality equivalence $\Phi$ of
Sublemma~\ref{lem:center-isomorphism} identifies
$Z(\mathcal{A}) = \mathrm{End}_{\mathrm{Mod}_{\mathcal{A}}}(\mathcal{A})$ with
$Z(\mathcal{A}^!) = \mathrm{End}_{\mathrm{Mod}_{\mathcal{A}^!}}(\mathcal{A}^!)$,
and $\Phi$ intertwines the Koszul pairing
(Corollary~\ref{cor:duality-bar-complexes-complete}) with the
exec
/bin/zsh -lc "sed -n '1468,1518p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '452,540p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\begin{proof}[Proof of Sublemma]
Since every $E_\infty$-chiral algebra is in particular an $E_1$-chiral algebra, and the Koszul property at the $E_\infty$ level implies Koszulity at the $E_1$ level (the forgetful functor is exact on bar complexes), we may apply the module Koszul duality equivalence
(Theorem~\ref{thm:e1-module-koszul-duality}), which gives:
\begin{equation}
\Phi: D^b(\mathrm{Mod}^{\Eone}_{\mathcal{A}}) \xrightarrow{\;\sim\;}
D^b(\mathrm{Mod}^{\Eone}_{\mathcal{A}^!})
\end{equation}
Under~$\Phi$, the unit module $\mathcal{A}$ (viewed as a module over itself)
maps to $\bar{B}^{\mathrm{ch}}(\mathcal{A}) = \mathcal{A}^!$ (viewed as a
module over~$\mathcal{A}^!$). Since equivalences of categories preserve
endomorphism algebras:
\begin{equation}
Z(\mathcal{A}) = \mathrm{End}_{D(\mathrm{Mod}_{\mathcal{A}})}(\mathcal{A})
\;\xrightarrow[\Phi]{\;\sim\;}\;
\mathrm{End}_{D(\mathrm{Mod}_{\mathcal{A}^!})}(\mathcal{A}^!)
= Z(\mathcal{A}^!)
\end{equation}
This isomorphism is canonical (determined by the bar-cobar equivalence) and
compatible with the Koszul pairing.
\end{proof}
exec
/bin/zsh -lc "sed -n '1728,1752p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
of~\S\ref{sec:frame-complementarity} generalizes to a Lagrangian
polarization:

\begin{theorem}[Quantum complementarity as Lagrangian polarization; \ClaimStatusProvedHere]
\label{thm:quantum-complementarity-main}
\label{thm:quantum-complementarity}
\index{deformation-obstruction complementarity|textbf}
\index{Lagrangian!complementarity|textbf}
\textup{[}Regime: curved-central
\textup{(}Convention~\textup{\ref{conv:regime-tags})].}

Let $(\mathcal{A}, \mathcal{A}^!)$ be a chiral Koszul pair on a smooth projective
curve $X$ over $\mathbb{C}$, with $\mathcal{A}$ a sheaf of chiral algebras in
the sense of Beilinson--Drinfeld \cite[Chapter 3]{BD04} and $\mathcal{A}^!$
its Koszul dual (Theorem~\ref{thm:chiral-koszul-duality}).
Write $\mathbf{C}_g(\cA)$, $\mathbf{Q}_g(\cA)$, $\mathbf{Q}_g(\cA^!)$
for the ambient complex and homotopy eigenspaces of
Definition~\textup{\ref{def:complementarity-complexes}}.

\smallskip\noindent
 succeeded in 51ms:
\item Direct sum: $Q_g(\mathcal{A}) \cap Q_g(\mathcal{A}^!) = 0$ as eigenspaces of
$\sigma$ (Step 9)
\item Exhaustion: $Q_g(\mathcal{A}) \oplus Q_g(\mathcal{A}^!) = H^*(\overline{
\mathcal{M}}_g, Z(\mathcal{A}))$ because $\sigma^2 = \mathrm{id}$ (Step 10)
\end{enumerate}

Therefore:
\begin{equation}
Q_g(\mathcal{A}) \oplus Q_g(\mathcal{A}^!) \cong H^*(\overline{\mathcal{M}}_g,
Z(\mathcal{A}))
\end{equation}

This completes the proof of Theorem~\ref{thm:quantum-complementarity-main}. \qedhere

\end{proof}

\begin{remark}[Proof architecture summary for Theorem~C]
\label{rem:h-level-proof-summary}
\index{Theorem C!proof architecture summary}
The distributed proof above establishes both the

thinking
**Gathering architecture details**

I think I need a bit more proof regarding the architecture summary. There might be relevant details or admissions included. I could start reading from around the year 1752 and see if there are any mentions of H-level. It seems important to understand the context better and ensure I’m capturing everything necessary. I want to make sure I’m thorough in my approach!
exec
/bin/zsh -lc "sed -n '1752,1796p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
$\mathbf{C}_g(\cA) = R\Gamma(\overline{\mathcal{M}}_g, \mathcal{Z}(\cA))$:
it is induced by the composition of Verdier duality~$\mathbb{D}$
(an exact functor on $D^b_{\mathrm{hol}}(\mathcal{D})$) with the
Koszul identification
$\mathcal{Z}(\cA) \cong \mathcal{Z}(\cA^!)$
(Theorem~\ref{thm:kodaira-spencer-chiral-complete}, Step~7).
Since~$\sigma$ is induced by exact functors, it commutes with
differentials at every page of the spectral sequence
(Lemma~\ref{lem:verdier-involution-moduli}).
\emph{Second}, Lemma~\ref{lem:involution-splitting}(a) gives
the cochain-level splitting: the projectors
$p^\pm = \tfrac{1}{2}(\mathrm{id} \pm \sigma)$ are cochain maps
whose images provide a quasi-isomorphic direct sum decomposition
$\mathbf{C}_g \simeq \operatorname{im}(p^+) \oplus \operatorname{im}(p^-)$.
\emph{Third}, model independence
(Proposition~\ref{prop:model-independence}) ensures the
decomposition depends only on the Koszul pair $(\cA, \cA^!)$,
not on auxiliary choices.
\end{remark}

exec
/bin/zsh -lc "rg -n \"lem:involution-splitting|Involution splitting|p\\"'^'"\\+|homotopy eigenspaces\" chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
195:Define the \emph{deformation-obstruction complexes} as homotopy eigenspaces:
217:(Lemma~\ref{lem:involution-splitting}) makes the passage automatic
221:\begin{lemma}[Involution splitting in characteristic~\texorpdfstring{$0$}{0}; \ClaimStatusProvedHere]
222:\label{lem:involution-splitting}
228:\item The homotopy eigenspaces
245:are cochain maps with $p^+ + p^- = \mathrm{id}$,
246:$(p^\pm)^2 = p^\pm$, and $p^+ \circ p^- = 0$.
247:Part~(a): the inclusion $\operatorname{im}(p^+) \oplus \operatorname{im}(p^-)
468:for the ambient complex and homotopy eigenspaces of
480: By Lemma~\textup{\ref{lem:involution-splitting}(a,c)},
503:\mathcal{Z}(\cA))$, Lemma~\textup{\ref{lem:involution-splitting}(b)}
560:$\operatorname{im}(p^+)$ with $p^+=\tfrac{1}{2}(\mathrm{id}+\sigma)$
562:The Lagrangian property is $\langle p^+x,p^+y\rangle=0$
563:(Lemma~\ref{lem:involution-splitting}(c)).
1761:\emph{Second}, Lemma~\ref{lem:involution-splitting}(a) gives
1765:$\mathbf{C}_g \simeq \operatorname{im}(p^+) \oplus \operatorname{im}(p^-)$.
5243:the involution-splitting (Lemma~\ref{lem:involution-splitting})
codex
I’ve hit the first structural issue: the connection chapter’s “self-contained” proof is importing a theory-chapter eigenspace lemma and a spectral-sequence lemma whose own statements already anticipate Theorem C. I’m checking whether that anticipation is harmless or actually circular.
exec
/bin/zsh -lc "sed -n '170,270p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '270,340p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '540,572p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
boundary conditions: the genus-$g$ obstruction space
$H^*(\overline{\mathcal{M}}_g, \mathcal{Z}(\cA))$ decomposes
into the deformation space of one boundary and the obstruction
space of the other. What~$\cA$ sees as anomaly at genus~$g$,
the transverse boundary~$\cA^!$ absorbs as deformation.
The Lagrangian upgrade~(C2) is the statement that the two
boundaries meet in a shifted-symplectic ambient space at
exactly half rank: transversality in the sense of
Pantev--To\"en--Vaqui\'e--Vezzosi~\cite{PTVV13}.
\end{remark}

\subsection{Statement of the theorem}

\begin{definition}[Deformation-obstruction complexes: H-level]
\label{def:complementarity-complexes}
\index{deformation-obstruction complexes|textbf}
Let $(\cA, \cA^!)$ be a chiral Koszul pair on~$X$.
The \emph{ambient complex} at genus~$g$ is
\[
\mathbf{C}_g(\cA) := R\Gamma(\overline{\mathcal{M}}_g, \mathcal{Z}(\cA)),
 succeeded in 51ms:
on the fixed curve~$\Sigma$ with the fiberwise curved
differential~$\dfib$
\textup{(}Convention~\textup{\ref{conv:higher-genus-differentials})}.
\end{definition}

\begin{lemma}[Perfectness criterion for the relative bar family;
\ClaimStatusProvedHere]
\label{lem:perfectness-criterion}
\index{perfectness criterion|textbf}
\index{bar complex!relative perfectness|textbf}
Let $(\cA, \cA^!)$ be a chiral Koszul pair on a smooth projective
curve~$X$, carrying a modular pre-Koszul datum
\textup{(}Definition~\textup{\ref{def:modular-koszul-chiral})}.
Suppose the following two conditions hold:
\begin{enumerate}[label=\textup{(\roman*)}]
\item \emph{PBW filterability.}
 The genus-$g$ bar complex $\bar{B}^{(g)}(\cA)$ admits an
 exhaustive multiplicative filtration~$F_\bullet$ such that the
 associated graded $\operatorname{gr}_F \bar{B}^{(g)}(\cA)$
 sees only the genus-$0$ collision differential~$\dzero$ and is
 succeeded in 51ms:
geometry, no external preprint), and the involution-splitting
lemma (linear algebra in characteristic~$0$).
In particular, Theorem~C does \emph{not} depend on the
ambient-level $D^2 = 0$
(Theorem~\textup{\ref{thm:ambient-d-squared-zero}},
which uses \textup{[}Mok25\textup{]}) or on the full
bar-intrinsic MC element $\Theta_\cA$
(Theorem~\textup{\ref{thm:mc2-bar-intrinsic}}).
The only curvature input is the scalar $\kappa(\cA)$,
which comes from the convolution-level
$D^2 = 0$ (unconditional).
\end{remark}

\begin{remark}[Elementary model presentation;
Convention~\ref{conv:proof-architecture}]
\label{rem:theorem-c-model}
\label{rem:complementarity-model}% backward-compatible label
\index{complementarity!model presentation}
\emph{Step~B} (M-level): The homotopy eigenspace
$\mathbf{Q}_g(\cA)=\operatorname{fib}(\sigma-\mathrm{id})$ is modeled by



thinking
**Clarifying theorem connections**

I need more context on theorem C1 in the specific chapter and how it connects to theorem C. I should check whether the claim of "no perfectness or nondegeneracy" aligns with constructions relying on perfectness. Also, I'll look into certain lemmas that may be hidden assumptions.

The user asked for a proof of theorem C1, so I should conduct a careful audit of assumptions and also confirm the exact statement of theorem C1 in the relevant chapter. It might determine whether it’s unconditional or conditional.
thinking
**Examining theorem dependencies**

I need to assess whether theorem C is unconditional, or if theorem C1 is merely a decomposition while C2 is conditional on pairing. The main aspect of theorem C involves Lagrangian H-level decomposition with anti-symmetric pairing, which raises questions about its unconditional status. I should also check if perfect duality or Lagrangian aspects relate to perfectness.

The non-degenerate pairing of homotopy summands is noted, but there’s potential circular reasoning if earlier propositions rely on theorem C itself. I need to read closely for any remarks about external dependencies linked to perfectness.
thinking
**Exploring nondegenerate pairing origins**

I’m questioning the source of nondegenerate pairing since Verdier duality suggests it induces anti-symmetric pairing of cohomological degree -(3g-3). The lemma in splitting also refers to a decomposition where each summand is Lagrangian. However, the actual proof seems deferred in the chapter. 

I need to check if it establishes nondegenerate pairing without relying on perfectness. Looking for Step 7 might help, along with any mention of quantum duality. I should search for an explicit proof of this pairing as well.
exec
/bin/zsh -lc "rg -n \"non-degenerate pairing|Lagrangian|pairing restricts|Verdier pairing|nondegenerate\" chapters/theory/higher_genus_complementarity.tex | sed -n '1,120p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
27:complex, which splits the moduli contribution into two Lagrangian
69:\item \emph{Shifted-symplectic Lagrangian upgrade
74: Verdier pairing $\langle -,- \rangle_{\mathbb{D}}$ on the ambient
80: $\mathbf{Q}_g(\cA^!)$ are Lagrangian subspaces: isotropic of half
90:nondegeneracy of the Verdier pairing is a hypothesis verified
95:Koszul locus; the H-level Lagrangian upgrade~(C2) is the
104:(a nondegenerate invariant bilinear form), then
115:framework for shifted Lagrangian morphisms that provides
148:and Lagrangian.
175:The Lagrangian upgrade~(C2) is the statement that the two
239: non-degenerate, they are Lagrangian.
436:gives the Verdier eigenspace decomposition and its Lagrangian
452:of~\S\ref{sec:frame-complementarity} generalizes to a Lagrangian
455:\begin{theorem}[Quantum complementarity as Lagrangian polarization; \ClaimStatusProvedHere]
459:\index{Lagrangian!complementarity|textbf}
475:\item \emph{Homotopy Lagrangian decomposition.}
485: with each summand Lagrangian for
490: non-degenerate pairing
513:are Lagrangians for the induced pairing on~$\mathcal{H}_g$, and
532:as Lagrangian complements.
exec
/bin/zsh -lc "sed -n '60,100p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 \;=\;
 Q_g(\cA) \;\oplus\; Q_g(\cA^!),
 \end{equation}
 where $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
 $Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$ are the eigenspaces of
 the Verdier involution~$\sigma$, and $Q_g(\cA) \cong
 Q_g(\cA^!)^\vee$
 \textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main})}.

\item \emph{Shifted-symplectic Lagrangian upgrade
 \textup{(}conditional on perfectness and nondegeneracy\textup{)}.}\;
 When the relative bar family
 $R\pi_{g*}\barB^{(g)}(\cA)$ is perfect
 \textup{(}Lemma~\textup{\ref{lem:perfectness-criterion})} and the
 Verdier pairing $\langle -,- \rangle_{\mathbb{D}}$ on the ambient
 complex $\mathbf{C}_g(\cA) = R\Gamma(\overline{\mathcal{M}}_g,
 \mathcal{Z}(\cA))$ is non-degenerate, the complex
 $\mathbf{C}_g(\cA)$ carries a $({-}(3g{-}3))$-shifted symplectic
 structure \textup{(}PTVV
 \cite{PTVV13}\textup{)}, and the summands $\mathbf{Q}_g(\cA)$ and
codex
I’ve confirmed at least one real dependency mismatch: the proof cites `lem:quantum-from-ss` for a `j_*`-extension identification that that lemma does not state. I’m pulling exact line numbers now and checking whether the same mismatch causes broader scope inflation around “Lagrangian” and “unconditional.”
exec
/bin/zsh -lc "nl -ba chapters/connections/thqg_symplectic_polarization.tex | sed -n '468,646p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '452,516p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '840,885p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '1512,1606p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   468	The eigenspace decomposition~(C1) holds unconditionally on the
   469	Koszul locus, requiring no perfectness or nondegeneracy hypotheses.
   470	We give a self-contained proof in the holographic setting.
   471	
   472	\begin{theorem}[Holographic eigenspace decomposition (C1);
   473	\ClaimStatusProvedHere]
   474	\label{thm:thqg-III-eigenspace-decomposition}
   475	\index{Lagrangian!eigenspace decomposition!holographic}
   476	Let $(\cA, \cA^!)$ be a chiral Koszul pair on a smooth projective
   477	curve $X$ over $\mathbb{C}$, and let $g \ge 0$.
   478	
   479	\smallskip\noindent
   480	\textbf{H-level.}\;
   481	The Verdier involution $\sigma$ of
   482	Construction~\textup{\ref{constr:thqg-III-verdier-involution}}
   483	splits the ambient complex:
   484	\begin{equation}\label{eq:thqg-III-C1-homotopy}
   485	\mathbf{C}_g(\cA)
   486	\;\simeq\;
   487	\mathbf{Q}_g(\cA) \;\oplus\; \mathbf{Q}_g(\cA^!),
 succeeded in 51ms:
   452	of~\S\ref{sec:frame-complementarity} generalizes to a Lagrangian
   453	polarization:
   454	
   455	\begin{theorem}[Quantum complementarity as Lagrangian polarization; \ClaimStatusProvedHere]
   456	\label{thm:quantum-complementarity-main}
   457	\label{thm:quantum-complementarity}
   458	\index{deformation-obstruction complementarity|textbf}
   459	\index{Lagrangian!complementarity|textbf}
   460	\textup{[}Regime: curved-central
   461	\textup{(}Convention~\textup{\ref{conv:regime-tags})].}
   462	
   463	Let $(\mathcal{A}, \mathcal{A}^!)$ be a chiral Koszul pair on a smooth projective
   464	curve $X$ over $\mathbb{C}$, with $\mathcal{A}$ a sheaf of chiral algebras in
   465	the sense of Beilinson--Drinfeld \cite[Chapter 3]{BD04} and $\mathcal{A}^!$
   466	its Koszul dual (Theorem~\ref{thm:chiral-koszul-duality}).
   467	Write $\mathbf{C}_g(\cA)$, $\mathbf{Q}_g(\cA)$, $\mathbf{Q}_g(\cA^!)$
   468	for the ambient complex and homotopy eigenspaces of
   469	Definition~\textup{\ref{def:complementarity-complexes}}.
   470	
   471	\smallskip\noindent
 succeeded in 52ms:
   840	
   841	\emph{Step 3: Quantum corrections are $E_\infty$ contributions.}
   842	
   843	\begin{lemma}[Quantum corrections as spectral sequence limit; \ClaimStatusProvedHere]
   844	\label{lem:quantum-from-ss}
   845	The genus-$g$ quantum correction space is:
   846	\begin{equation}
   847	Q_g(\mathcal{A}) = E_\infty^{*,*,g} = \bigoplus_{p+q=*} \text{gr}^g H^{p+q}(
   848	\bar{B}(\mathcal{A}))
   849	\end{equation}
   850	where $\text{gr}^g$ denotes the $g$-th graded piece of the genus filtration.
   851	\end{lemma}
   852	
   853	\begin{proof}[Proof of Lemma~\ref{lem:quantum-from-ss}]
   854	By definition of spectral sequences, $E_\infty$ is the associated graded of the 
   855	filtered cohomology:
   856	\begin{equation}
   857	E_\infty^{p,q,g} \cong \frac{F^g H^{p+q}(\bar{B}(\mathcal{A}))}{F^{g-1} H^{p+q}(
   858	\bar{B}(\mathcal{A}))}
   859	\end{equation}
 succeeded in 50ms:
  1512	\end{proof}
  1513	
  1514	\begin{lemma}[Eigenspace decomposition; \ClaimStatusProvedHere]
  1515	\label{lem:eigenspace-decomposition-complete}
  1516	The involution $\sigma$ decomposes moduli cohomology into $\pm 1$
  1517	eigenspaces:
  1518	\begin{equation}
  1519	H^*(\overline{\mathcal{M}}_g, Z(\mathcal{A})) =
  1520	H^*(\overline{\mathcal{M}}_g, Z(\mathcal{A}))^+ \oplus
  1521	H^*(\overline{\mathcal{M}}_g, Z(\mathcal{A}))^-
  1522	\end{equation}
  1523	where $H^*(\overline{\mathcal{M}}_g, Z(\mathcal{A}))^\pm = \ker(\sigma \mp
  1524	\mathrm{id})$. These eigenspaces are identified with the quantum corrections:
  1525	\begin{align}
  1526	Q_g(\mathcal{A}) &= H^*(\overline{\mathcal{M}}_g, Z(\mathcal{A}))^+\\
  1527	Q_g(\mathcal{A}^!) &= H^*(\overline{\mathcal{M}}_g, Z(\mathcal{A}))^-
  1528	\end{align}
  1529	\end{lemma}
  1530	
  1531	\begin{proof}[Proof of Lemma~\ref{lem:eigenspace-decomposition-complete}]
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '72,100p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '1783,1852p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/thqg_symplectic_polarization.tex | sed -n '220,242p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
    72	 $R\pi_{g*}\barB^{(g)}(\cA)$ is perfect
    73	 \textup{(}Lemma~\textup{\ref{lem:perfectness-criterion})} and the
    74	 Verdier pairing $\langle -,- \rangle_{\mathbb{D}}$ on the ambient
    75	 complex $\mathbf{C}_g(\cA) = R\Gamma(\overline{\mathcal{M}}_g,
    76	 \mathcal{Z}(\cA))$ is non-degenerate, the complex
    77	 $\mathbf{C}_g(\cA)$ carries a $({-}(3g{-}3))$-shifted symplectic
    78	 structure \textup{(}PTVV
    79	 \cite{PTVV13}\textup{)}, and the summands $\mathbf{Q}_g(\cA)$ and
    80	 $\mathbf{Q}_g(\cA^!)$ are Lagrangian subspaces: isotropic of half
    81	 rank, with $\mathbf{Q}_g(\cA) \simeq
    82	 \mathbf{Q}_g(\cA^!)^\vee[-(3g{-}3)]$.
    83	 This is the geometric home of the finite-order shadow
    84	 tower~$\Theta_{\cA}^{\leq r}$
    85	 \textup{(}Appendix~\textup{\ref{app:nonlinear-modular-shadows})}.
    86	\end{enumerate}
    87	The conditionality in~(C2) is substantive:
    88	perfectness requires PBW filterability and finite-dimensional
    89	fiber cohomology (Lemma~\ref{lem:perfectness-criterion}), and
    90	nondegeneracy of the Verdier pairing is a hypothesis verified
    91	family by family
 succeeded in 50ms:
   220	\mathbf{C}_g(\cA)^{\vee\vee}[{-(3g{-}3)}][{3g{-}3}]
   221	\arrow[r, "\mathrm{ev}"]
   222	&
   223	\mathbf{C}_g(\cA)
   224	\end{tikzcd}
   225	\end{equation}
   226	Here $\mathbb{D}$ is the Verdier duality map from
   227	Corollary~\ref{cor:duality-bar-complexes-complete},
   228	$\mathrm{KS}$ is the Koszul identification
   229	$\mathbf{C}_g(\cA) \xrightarrow{\sim} \mathbf{C}_g(\cA^!)$
   230	via Lemma~\ref{lem:center-isomorphism}, and $\mathrm{ev}$
   231	is the evaluation map. The shifts cancel, and the composition
   232	is well-defined as a cochain map of degree zero.
   233	\end{construction}
   234	
   235	\begin{proposition}[Involutivity and anti-symmetry;
   236	\ClaimStatusProvedHere]
   237	\label{prop:thqg-III-involutivity}
   238	\index{Verdier involution!involutivity}
   239	The endomorphism $\sigma$ of
 succeeded in 50ms:
  1783	\begin{proposition}[Verdier pairing and Lagrangian eigenspaces; \ClaimStatusProvedHere]
  1784	\label{prop:lagrangian-eigenspaces}
  1785	\index{Lagrangian!eigenspaces|textbf}
  1786	\index{Verdier duality!pairing on moduli}
  1787	Let $(\cA, \cA^!)$ be a chiral Koszul pair and let
  1788	$V = H^*(\overline{\mathcal{M}}_g, \mathcal{Z}(\cA))$.
  1789	\begin{enumerate}[label=\textup{(\roman*)}]
  1790	\item Verdier duality on the center local system $\mathcal{Z}(\cA)$
  1791	 induces a non-degenerate bilinear pairing
  1792	 \[
  1793	 \langle -, - \rangle_{\mathbb{D}} \colon V \otimes V \to \mathbb{C}
  1794	 \]
  1795	 of cohomological degree $-(3g-3)$ \textup{(}the shift coming from
  1796	 $\dim_{\mathbb{C}} \overline{\mathcal{M}}_g = 3g-3$\textup{)}.
  1797	\item The Verdier involution $\sigma$ is an \emph{anti-involution}
  1798	 for this pairing:
  1799	 $\langle \sigma(v), \sigma(w) \rangle_{\mathbb{D}} = -\langle v, w \rangle_{\mathbb{D}}$
  1800	 for all $v, w \in V$.
  1801	\item Consequently, the eigenspaces
  1802	 $V^+ = Q_g(\cA)$ and $V^- = Q_g(\cA^!)$
exec
/bin/zsh -lc "nl -ba chapters/connections/thqg_symplectic_polarization.tex | sed -n '388,418p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   388	\label{lem:thqg-III-nondegeneracy}
   389	\index{Verdier pairing!nondegeneracy}
   390	When the relative bar family is perfect
   391	\textup{(}Lemma~\textup{\ref{lem:perfectness-criterion})},
   392	the holographic Verdier pairing
   393	\eqref{eq:thqg-III-holographic-pairing-def} is nondegenerate.
   394	\end{lemma}
   395	
   396	\begin{proof}
   397	Perfectness of $R\pi_{g*}\barB^{(g)}(\cA)$ ensures that
   398	the Verdier duality map
   399	$\mathcal{Z}(\cA) \xrightarrow{\sim}
   400	\mathbb{D}\,\mathcal{Z}(\cA)[3g - 3]$
   401	is a quasi-isomorphism of perfect complexes on the smooth
   402	proper DM stack $\overline{\mathcal{M}}_g$. Applying $\RGamma$
   403	and Serre duality on the stack gives a perfect pairing on
   404	cohomology. On the cochain level, the cup-product pairing
   405	\[
   406	C^p(\overline{\mathcal{M}}_g, \mathcal{Z})
   407	\otimes

thinking
**Reviewing proof details**

I need to find the exact lines for the prop:thqg-III-involutivity proof part b because it might be problematic. I’ll focus on reading it alongside the numbers to make sure I’m not missing anything critical. It’s important to ensure that everything lines up correctly, so I want to pay close attention to this part. I'll dive deeper and see if I can clarify any potential issues!
exec
/bin/zsh -lc "nl -ba chapters/connections/thqg_symplectic_polarization.tex | sed -n '235,292p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   235	\begin{proposition}[Involutivity and anti-symmetry;
   236	\ClaimStatusProvedHere]
   237	\label{prop:thqg-III-involutivity}
   238	\index{Verdier involution!involutivity}
   239	The endomorphism $\sigma$ of
   240	Construction~\textup{\ref{constr:thqg-III-verdier-involution}}
   241	satisfies:
   242	\begin{enumerate}[label=\textup{(\alph*)}]
   243	\item $\sigma^2 = \id$ \textup{(}involutivity\textup{)}.
   244	\item The Verdier pairing
   245	 $\langle -, - \rangle_{\mathbb{D}} \colon
   246	 \mathbf{C}_g(\cA) \otimes \mathbf{C}_g(\cA) \to
   247	 \mathbb{C}[{-(3g{-}3)}]$
   248	 satisfies the anti-symmetry
   249	 \begin{equation}\label{eq:thqg-III-anti-symmetry}
   250	 \langle \sigma(v), \sigma(w) \rangle_{\mathbb{D}}
   251	 = -\langle v, w \rangle_{\mathbb{D}}
   252	 \end{equation}
   253	 for all $v, w \in \mathbf{C}_g(\cA)$.
   254	\end{enumerate}



thinking
**Evaluating propositions and theorems**

I'm noticing a potential circular dependency in the propositions I'm looking at. Proposition `prop:lagrangian-eigenspaces` is cited later in the theory chapter, while proposition 237 refers to proposition 1783. This feels backwards, and I suspect there's a mixing of dependencies. In the thqg chapter, proposition 237 cites theorem k-s and potentially `prop:lagrangian-eigenspaces`, which isn't organized properly by label. I'll need to check if this proof relies on certain theorems or lemmas, including whether it could be circular in its dependency on earlier propositions. An audit seems necessary.
thinking
**Assessing circular dependencies**

I've noticed that Stage 4 relies on isotropy derived from the anti-symmetry of sigma, specifically Prop 237(b). This is established in the thqg file by referring to `lagrangian-eigenspaces`, which itself cites Theorem C, particularly Step 7. I need to evaluate whether this circularity is problematic. Theorem C1 might not need anti-symmetry, but it does mention duality while lacking explicit reference to isotropy. I'll have to inspect the `lagrangian-eigenspaces` proposition more closely, as it appears to connect back to Theorem C, raising questions about its role as a corollary. An audit of Theorem C's proof will help clarify if it's truly circular.
thinking
**Analyzing proof dependencies**

I'm examining the proof that seems to rely on Prop 237(b) indirectly, particularly in Stage 4. It looks like Prop 237(b) may be circular since it references `lagrangian-eigenspaces` and Theorem C. This brings up potential concerns about the severity of any circularity, especially regarding the duality aspect, which might not be fully fleshed out in the decomposition. I think I need to clarify and evaluate the implications of these dependencies more thoroughly.
codex
I’ve found a second structural fault: the very construction of `σ` uses an arrow `C_g(A)^{\vee\vee} -> C_g(A)` labeled `ev` without any reflexivity/perfectness hypothesis. I’m checking whether the surrounding text justifies that map anywhere, because if not, the involution is not actually constructed at the claimed generality.
exec
/bin/zsh -lc "nl -ba chapters/connections/thqg_symplectic_polarization.tex | sed -n '190,233p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"\\"'^{'"\\\\vee\\\\vee}|double dual|evaluation map|reflexive|ev\\}\" chapters/connections/thqg_symplectic_polarization.tex chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "thm:verdier-duality-config-complete|cor:duality-bar-complexes-complete|lem:center-isomorphism|thm:kodaira-spencer-chiral-complete|lem:verdier-extension-exchange|lem:ss-duality-complete" chapters/theory/higher_genus_complementarity.tex metadata/theorem_registry.md' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   190	morphisms of chiral algebras (being a homotopy fiber of the
   191	bar complex, which is functorial by
   192	Theorem~\ref{thm:geometric-equals-operadic-bar}).
   193	Applying $\RGamma(\overline{\mathcal{M}}_g, -)$ preserves
   194	functoriality.
   195	\end{proof}
   196	
   197	\begin{construction}[Verdier involution on the ambient complex]
   198	\label{constr:thqg-III-verdier-involution}
   199	\index{Verdier involution!construction|textbf}
   200	The Verdier self-duality of
   201	Proposition~\ref{prop:thqg-III-ambient-properties}(ii) and
   202	the Koszul involutivity
   203	$(\cA^!)^! \simeq \cA$
   204	(Theorem~\ref{thm:chiral-koszul-duality}) combine to produce
   205	a cochain-level endomorphism
   206	\begin{equation}\label{eq:thqg-III-sigma-def}
   207	\sigma
   208	\colon
   209	\mathbf{C}_g(\cA) \longrightarrow \mathbf{C}_g(\cA)
 exited 2 in 51ms:
rg: regex parse error:
    (?:\^{\vee\vee}|double dual|evaluation map|reflexive|ev\})
          ^
error: repetition quantifier expects a valid decimal
 succeeded in 51ms:
chapters/theory/higher_genus_complementarity.tex:528:Step~II (from Theorem~\ref{thm:verdier-duality-config-complete})
chapters/theory/higher_genus_complementarity.tex:530:Step~III (from Theorem~\ref{thm:kodaira-spencer-chiral-complete})
chapters/theory/higher_genus_complementarity.tex:1044:\label{thm:verdier-duality-config-complete}
chapters/theory/higher_genus_complementarity.tex:1056:\begin{proof}[Proof of Theorem~\ref{thm:verdier-duality-config-complete}]
chapters/theory/higher_genus_complementarity.tex:1117:\label{cor:duality-bar-complexes-complete}
chapters/theory/higher_genus_complementarity.tex:1126:\begin{proof}[Proof of Corollary~\ref{cor:duality-bar-complexes-complete}]
chapters/theory/higher_genus_complementarity.tex:1144:Combining with the Verdier pairing on $\Omega^*_{\log}$ from Theorem~\ref{thm:verdier-duality-config-complete}, we obtain:
chapters/theory/higher_genus_complementarity.tex:1157:\label{lem:ss-duality-complete}
chapters/theory/higher_genus_complementarity.tex:1158:The Verdier duality of Theorem~\ref{thm:verdier-duality-config-complete} induces an isomorphism 
chapters/theory/higher_genus_complementarity.tex:1166:\begin{proof}[Proof of Lemma~\ref{lem:ss-duality-complete}]
chapters/theory/higher_genus_complementarity.tex:1173:By Corollary~\ref{cor:duality-bar-complexes-complete}, the pairing:
chapters/theory/higher_genus_complementarity.tex:1220:Immediate from Lemma~\ref{lem:ss-duality-complete} by taking the sum over all $(p,q)$ with 
chapters/theory/higher_genus_complementarity.tex:1240:\label{thm:kodaira-spencer-chiral-complete}
chapters/theory/higher_genus_complementarity.tex:1263:\begin{proof}[Proof of Theorem~\ref{thm:kodaira-spencer-chiral-complete}]
chapters/theory/higher_genus_complementarity.tex:1330:exchanges $j_*$ and $j_!$ extensions (Lemma~\ref{lem:verdier-extension-exchange}):
chapters/theory/higher_genus_complementarity.tex:1355:Sublemma~\ref{lem:center-isomorphism} identifies
chapters/theory/higher_genus_complementarity.tex:1359:(Corollary~\ref{cor:duality-bar-complexes-complete}) with the
chapters/theory/higher_genus_complementarity.tex:1441:By Corollary~\ref{cor:duality-bar-complexes-complete}, the Verdier-Koszul pairing
chapters/theory/higher_genus_complementarity.tex:1455:duality on compact smooth varieties, see Theorem~\ref{thm:verdier-duality-config-complete}).
chapters/theory/higher_genus_complementarity.tex:1463:\label{lem:center-isomorphism}
exec
/bin/zsh -lc "rg -n -F \"double dual\" chapters/connections/thqg_symplectic_polarization.tex chapters/theory/higher_genus_complementarity.tex && rg -n -F \"evaluation map\" chapters/connections/thqg_symplectic_polarization.tex chapters/theory/higher_genus_complementarity.tex && rg -n -F \"vee\\\\vee\" chapters/connections/thqg_symplectic_polarization.tex chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '1096,1165p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '1023,1095p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  1096	\overline{C}_n(X))$ (forms with logarithmic poles along $\partial \overline{C}_n(X)$), 
  1097	the duality becomes:
  1098	\begin{equation}
  1099	\Omega^k_{\log}(\overline{C}_n(X)) \times \Omega^{2n-k}_{\log}(\overline{C}_n(X)) 
  1100	\to \mathbb{C}
  1101	\end{equation}
  1102	given by:
  1103	\begin{equation}
  1104	\langle \eta, \xi \rangle = \text{Res}_{\partial \overline{C}_n(X)} (\eta \wedge \xi)
  1105	\end{equation}
  1106	where $\text{Res}$ denotes the Poincaré residue map.
  1107	
  1108	This pairing is also perfect, by the logarithmic Poincar\'e lemma
  1109	(Deligne~\cite{Deligne71}, Hodge~II, Proposition~3.1.8), which
  1110	identifies $H^*(\Omega^*_{\log}(\overline{C}_n(X) \setminus D))
  1111	\cong H^*(C_n(X))$; the perfectness then follows from
  1112	Poincar\'e--Lefschetz duality for the smooth quasi-projective
  1113	variety~$C_n(X)$.
  1114	\end{proof}
  1115	
 succeeded in 51ms:
  1023	\mathcal{H}^q_{\mathrm{fiber}}(\mathcal{A})
  1024	\big|_{\mathcal{M}_g^{\mathrm{smooth}}} = 0
  1025	\quad\text{for } q \neq 0,
  1026	\qquad
  1027	\mathcal{H}^0_{\mathrm{fiber}}
  1028	\cong Z(\mathcal{A}) \otimes \underline{\mathbb{C}}.
  1029	\end{equation}
  1030	\end{proof}
  1031	
  1032	This completes Step~I: the genus filtration, the associated spectral
  1033	sequence, and the identification of $Q_g(\mathcal{A})$ with $E_\infty$
  1034	are in place, and the fiber cohomology has been shown to lie in the center.
  1035	\end{proof}
  1036	
  1037	\subsection{Step II: Verdier duality on fibers}
  1038	
  1039	\begin{proof}[Step II: Steps 5-6]
  1040	
  1041	\emph{Step 5: Poincaré--Verdier duality on configuration spaces.}
  1042	

thinking
**Inspecting mathematical steps**

I need to look closely at theorem k-s, specifically step 7, between lines 1330 and 1415, to examine anti-commutativity as it's essential for stage 3. I think we've already discussed the end, but I want to verify if step 7 relies on theorem C. I should check for any circular reasoning. My plan is to inspect the section around lines 1240 to 1410 to make sure I have everything covered.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '1240,1418p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  1240	\label{thm:kodaira-spencer-chiral-complete}
  1241	\index{Kodaira--Spencer map|textbf}
  1242	\textup{[Regime: curved-central on the Koszul locus; all genera
  1243	\textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
  1244	
  1245	Let $(\mathcal{A}, \mathcal{A}^!)$ be a chiral Koszul pair and let $\pi: \mathcal{C}_g
  1246	\to \overline{\mathcal{M}}_g$ be the universal curve. There is a natural action:
  1247	\begin{equation}
  1248	\rho: Z(\mathcal{A}) \to \mathrm{End}\bigl(H^*(\overline{\mathcal{M}}_g, Z(\mathcal{A}))\bigr)
  1249	\end{equation}
  1250	constructed from the Gauss--Manin connection on the chiral homology sheaf.
  1251	
  1252	This action interacts with Verdier duality via anti-commutativity: let
  1253	$\mathbb{D}: H^*(\bar{B}^{(g)}(\mathcal{A})) \xrightarrow{\sim} H^*(\bar{B}^{(g)}(
  1254	\mathcal{A}^!))^\vee$ be the Verdier isomorphism of Corollary~\ref{cor:quantum-dual-complete}.
  1255	Then for every $z \in Z(\mathcal{A})$ and $v \in T_{[\Sigma_g]}\overline{\mathcal{M}}_g$:
  1256	\begin{equation}\label{eq:verdier-ks-anticommute}
  1257	\mathbb{D} \circ \nabla_{\kappa(v)}^z = -\nabla_{\kappa(v)}^z \circ \mathbb{D}
  1258	\end{equation}
  1259	where $\kappa(v)$ is the Kodaira--Spencer class associated to $v$ and $\nabla^z$
exec
/bin/zsh -lc "nl -ba chapters/connections/thqg_symplectic_polarization.tex | sed -n '418,460p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   418	
   419	\begin{proposition}[Degree shift at each genus;
   420	\ClaimStatusProvedHere]
   421	\label{prop:thqg-III-degree-shift}
   422	The holographic Verdier pairing has cohomological degree
   423	$-(3g - 3)$. In particular:
   424	\begin{enumerate}[label=\textup{(\alph*)}]
   425	\item At genus $0$: degree $+3$, pairing
   426	 $H^0 \otimes H^0 \to \mathbb{C}[3]$
   427	 \textup{(}trivially degenerate on one-dimensional $H^0$;
   428	 the complementarity is purely at the S-level\textup{)}.
   429	\item At genus $1$: degree $0$, pairing
   430	 $H^0 \otimes H^0 \to \mathbb{C}$
   431	 \textup{(}classical pairing\textup{)}.
   432	\item At genus $g \ge 2$: degree $-(3g - 3)$,
   433	 giving a genuine shifted-symplectic structure.
   434	\end{enumerate}
   435	\end{proposition}
   436	
   437	\begin{proof}

thinking
**Verifying theorem statement**

This seems like a crucial counterexample! I need to confirm my findings. The theorem statement from lines 476-510 specifies that g≥0. Then the proposition for genus-0 from lines 694 onwards states Q_0(A)=Z(A) and Q_0(A^!)=0. If there's a nonzero center, this contradicts the concept of duality. Should I consider a possible derived shift? Nope, that doesn't work. So, it looks like the theorem is false as stated. I ought to pinpoint the exact lines for the genus-0 property.
codex
A genuine boundary-value contradiction is showing up at `g=0`: the theorem states `Q_g(A) ≅ Q_g(A^!)^∨` for all `g ≥ 0`, but the same file later states `Q_0(A)=Z(A)` and `Q_0(A^!)=0`. I’m verifying the exact lines and whether any convention elsewhere rescues this, but on the face of the source that makes the theorem false as stated at genus zero.
exec
/bin/zsh -lc "nl -ba chapters/connections/thqg_symplectic_polarization.tex | sed -n '690,718p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '188,240p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"Q_1\\(|overline\\\\{\\\\mathcal\\\\{M\\\\}\\}_\\{1,1\\}|overline\\\\{\\\\mathcal\\\\{M\\\\}\\}_1\" chapters/connections/thqg_symplectic_polarization.tex chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"Q_0\\(|genus-0 complementarity|Q_0\\(\\\\cA\\)|Q_0\\(\\\\mathcal\\{A\\}\\)|Q_0\\(.*\\"'^!'"\\)\" chapters/theory/higher_genus_complementarity.tex chapters/connections/thqg_symplectic_polarization.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   690	\end{proof}
   691	
   692	\begin{proposition}[Genus-$0$ complementarity;
   693	\ClaimStatusProvedHere]
   694	\label{prop:thqg-III-genus-0}
   695	\index{complementarity!genus 0}
   696	At genus~$0$, $\overline{\mathcal{M}}_0 = \mathrm{pt}$ and
   697	$\mathcal{H}_0(\cA) = Z(\cA)$.
   698	The Verdier involution $\sigma$ acts as $+\id$ on $Z(\cA)$,
   699	giving:
   700	\[
   701	Q_0(\cA) = Z(\cA), \qquad Q_0(\cA^!) = 0.
   702	\]
   703	\end{proposition}
   704	
   705	\begin{proof}
   706	Since $\overline{\mathcal{M}}_0$ is a point, the center
   707	local system has a single stalk $Z(\cA)$. The bar complex
   708	at genus~$0$ is uncurved (the curvature
   709	$\dfib^{\,2} = \kappa(\cA) \cdot \omega_g$ vanishes
 succeeded in 51ms:
   188	\[
   189	\mathbf{C}_g(\cA) := R\Gamma(\overline{\mathcal{M}}_g, \mathcal{Z}(\cA)),
   190	\]
   191	where $\mathcal{Z}(\cA)$ is the center local system.
   192	The Verdier involution $\sigma$ acts on $\mathbf{C}_g(\cA)$ as a
   193	cochain-level endomorphism with $\sigma^2 = \mathrm{id}$
   194	(Theorem~\ref{thm:verdier-bar-cobar}).
   195	Define the \emph{deformation-obstruction complexes} as homotopy eigenspaces:
   196	\begin{equation}\label{eq:complementarity-fiber}
   197	\mathbf{Q}_g(\cA) := \operatorname{fib}(\sigma - \mathrm{id}\colon
   198	\mathbf{C}_g \to \mathbf{C}_g), \qquad
   199	\mathbf{Q}_g(\cA^!) := \operatorname{fib}(\sigma + \mathrm{id}\colon
   200	\mathbf{C}_g \to \mathbf{C}_g).
   201	\end{equation}
   202	The \emph{cohomological shadows} (S-level) are defined by:
   203	\begin{align}\label{eq:shadow-spaces}
   204	Q_g(\cA) &:= H^*(\mathbf{Q}_g(\cA))
   205	= \ker(\sigma - \mathrm{id} \mid H^*(\overline{\mathcal{M}}_g, \mathcal{Z}(\cA))),\\
   206	Q_g(\cA^!) &:= H^*(\mathbf{Q}_g(\cA^!))
   207	= \ker(\sigma + \mathrm{id} \mid H^*(\overline{\mathcal{M}}_g, \mathcal{Z}(\cA))).
 exited 2 in 52ms:
rg: regex parse error:
    (?:Q_1\(|overline\{\mathcal\{M\}\}_\{1,1\}|overline\{\mathcal\{M\}\}_1)
                       ^^
error: unrecognized escape sequence
 exited 2 in 51ms:
rg: regex parse error:
    (?:Q_0\(|genus-0 complementarity|Q_0\(\cA\)|Q_0\(\mathcal\{A\}\)|Q_0\(.*\^!\))
                                          ^^
error: unrecognized escape sequence
exec
/bin/zsh -lc 'rg -n -F "Q_0(" chapters/theory/higher_genus_complementarity.tex chapters/connections/thqg_symplectic_polarization.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F \"overline{\\mathcal{M}}_{1,1}\" chapters/theory/higher_genus_complementarity.tex chapters/connections/thqg_symplectic_polarization.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F \"overline{\\mathcal{M}}_1\" chapters/theory/higher_genus_complementarity.tex chapters/connections/thqg_symplectic_polarization.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
chapters/connections/thqg_symplectic_polarization.tex:701:Q_0(\cA) = Z(\cA), \qquad Q_0(\cA^!) = 0.
chapters/theory/higher_genus_complementarity.tex:1703:giving $Q_0(\mathcal{A}) = \mathbb{C}$, $Q_0(\mathcal{A}^!) = 0$. Dimension check:
chapters/theory/higher_genus_complementarity.tex:2285:At genus~$0$: $Q_0(\cA)=\mathbb{C}$, $Q_0(\cA^!)=0$ (tree-level,
 succeeded in 51ms:
chapters/connections/thqg_symplectic_polarization.tex:447:At genus~$1$, $\dim \overline{\mathcal{M}}_{1,1} = 1$
chapters/connections/thqg_symplectic_polarization.tex:450:is $\overline{\mathcal{M}}_{1,1}$, where the pairing has
chapters/connections/thqg_symplectic_polarization.tex:453:$Q_1(\cA) \oplus Q_1(\cA^!) \cong H^*(\overline{\mathcal{M}}_{1,1},
chapters/connections/thqg_symplectic_polarization.tex:722:$H^*(\overline{\mathcal{M}}_{1,1})
chapters/connections/thqg_symplectic_polarization.tex:740:$\overline{\mathcal{M}}_{1,1}$. The class $\kappa$ is the
chapters/connections/thqg_symplectic_polarization.tex:750:= \dim H^*(\overline{\mathcal{M}}_{1,1})$.
chapters/connections/thqg_symplectic_polarization.tex:1428:$\overline{\mathcal{M}}_{1,1} \cong \overline{\mathbb{H}/\mathrm{SL}_2(\mathbb{Z})}$
chapters/connections/thqg_symplectic_polarization.tex:1430:$H^*(\overline{\mathcal{M}}_{1,1})
chapters/connections/thqg_symplectic_polarization.tex:1444: = H^*(\overline{\mathcal{M}}_{1,1}, \mathcal{Z}(\cA))
chapters/connections/thqg_symplectic_polarization.tex:1477:$H^*(\overline{\mathcal{M}}_{1,1}) = \mathbb{Q} \oplus
chapters/connections/thqg_symplectic_polarization.tex:1480:over $\overline{\mathcal{M}}_{1,1}$ (the center is constant
chapters/connections/thqg_symplectic_polarization.tex:1495:= \int_{\overline{\mathcal{M}}_{1,1}} \kappa(\cA) \cdot
chapters/connections/thqg_symplectic_polarization.tex:1497:$\int_{\overline{\mathcal{M}}_{1,1}} \lambda_1 = 1/24$,
chapters/theory/higher_genus_complementarity.tex:155:$H^*(\overline{\mathcal{M}}_{1,1})=\mathbb{Q}\oplus\mathbb{Q}\lambda$,
chapters/theory/higher_genus_complementarity.tex:1411:$H^*(\overline{\mathcal{M}}_{1,1})$ is:
chapters/theory/higher_genus_complementarity.tex:1706:\emph{Genus $1$}: $\dim H^*(\overline{\mathcal{M}}_{1,1}) = 2$ ($H^0 \oplus H^2$).
chapters/theory/higher_genus_complementarity.tex:2354:At genus~1: $\dim H^*(\overline{\mathcal{M}}_{1,1}) = 2$,
chapters/theory/higher_genus_complementarity.tex:2445:\emph{Genus 1 moduli space}: The cohomology ring of $\overline{\mathcal{M}}_{1,1}$ is generated by $\lambda = c_1(\mathbb{E})$:
chapters/theory/higher_genus_complementarity.tex:2447:H^*(\overline{\mathcal{M}}_{1,1}) = \mathbb{Q}[\lambda] / (\lambda^2) = \mathbb{Q} 
chapters/theory/higher_genus_complementarity.tex:2476:where $\omega_1 \in H^2(\overline{\mathcal{M}}_{1,1})$ is the fundamental class (the $B$-cycle monodromy of the propagator, valued in $\mathbb{C} \cdot \kappa$).
 succeeded in 51ms:
chapters/theory/higher_genus_complementarity.tex:1889:\cong H^*(\overline{\mathcal{M}}_1, Z(\mathcal{H}_\kappa))$ that we
chapters/theory/higher_genus_complementarity.tex:2572:\dim Q_1(\widehat{\mathfrak{g}}_{-h^\vee}^!) = \dim H^*(\overline{\mathcal{M}}_1) - \dim Q_1(
chapters/connections/thqg_symplectic_polarization.tex:448:but $\dim \overline{\mathcal{M}}_1 = 0$ (a point for the
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '1688,1710p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  1688	Since $\sigma^2 = \mathrm{id}$ on the finite-dimensional vector space
  1689	$V = H^*(\overline{\mathcal{M}}_g, Z(\mathcal{A}))$, the minimal polynomial of
  1690	$\sigma$ divides $t^2 - 1 = (t-1)(t+1)$. Over $\mathbb{C}$, every vector decomposes
  1691	uniquely into $\pm 1$ eigenvectors via the projectors
  1692	$\pi^+ = \frac{1}{2}(\mathrm{id} + \sigma)$ and
  1693	$\pi^- = \frac{1}{2}(\mathrm{id} - \sigma)$. Therefore:
  1694	\begin{equation}
  1695	V = V^+ \oplus V^- = Q_g(\mathcal{A}) \oplus Q_g(\mathcal{A}^!)
  1696	\end{equation}
  1697	and in particular $\dim V^+ + \dim V^- = \dim V$.
  1698	
  1699	\emph{Verification at small genera.}
  1700	
  1701	\emph{Genus $0$}: $\overline{\mathcal{M}}_0 = \mathrm{pt}$, so
  1702	$\dim H^* = 1$. The involution $\sigma$ acts as $+1$ on $H^0$ (identity class),
  1703	giving $Q_0(\mathcal{A}) = \mathbb{C}$, $Q_0(\mathcal{A}^!) = 0$. Dimension check:
  1704	$1 + 0 = 1$.
  1705	
  1706	\emph{Genus $1$}: $\dim H^*(\overline{\mathcal{M}}_{1,1}) = 2$ ($H^0 \oplus H^2$).
  1707	For the Heisenberg algebra: $Q_1(\mathcal{H}_\kappa) = \mathbb{C} \cdot \kappa$
exec
/bin/zsh -lc "rg -n -F '\\vee\\vee' chapters/connections/thqg_symplectic_polarization.tex chapters/theory/higher_genus_complementarity.tex CLAUDE.md metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/connections/thqg_symplectic_polarization.tex:220:\mathbf{C}_g(\cA)^{\vee\vee}[{-(3g{-}3)}][{3g{-}3}]



thinking
**Analyzing proof structure**

I discovered that there isn't any additional support in the files. It seems that the search didn't find any further occurrences of `\vee\vee`. Now, regarding the proof being self-contained, Stage 3 of the theorem cites a lemma that claims it anticipates Theorem C and refers back to another lemma for identification. This might indicate a circularity within the proof. I need to look closer at how this lemma fits into the overall structure of the theorem and its proof.
thinking
**Evaluating theorem proof**

The user has requested the theorem proof, and it seems there's a contradiction in the connection chapter that claims the proof is self-contained while citing a lemma from the theory chapter. This lemma might have been independently proved elsewhere in the book, which could still support the theorem without creating circularity. I need to check if the lemma references Theorem C directly. As it's integrated into Theorem C's proof architecture, the claim of a self-contained proof in the connection chapter might not hold true.
thinking
**Identifying logical gaps**

In Stage 3, there's a mis-citation concerning the lemma quantum-from-ss. The claim about Q_g(A) being a subspace from j_*-extension is incorrect since quantum-from-ss only defines Q_g as `gr^g H*(bar B)` and points out that the eigenspace identification is proved by another lemma. This creates a genuine logical gap, which seems significant. I should gather the exact line references from both files to clarify this. Additionally, the theorem's duality part relies on a conditional non-degeneracy lemma, which contradicts its unconditional claim.
exec
/bin/zsh -lc "nl -ba chapters/connections/concordance.tex | sed -n '4938,4970p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  4938	The formerly conjectural off-Koszul bar-cobar inversion on
  4939	$\operatorname{Ran}(X)$ is proved
  4940	(Theorem~\ref{thm:off-koszul-ran-inversion}): the counit
  4941	$\Omega_X \barB_X(\cA) \to \cA$ is an isomorphism in
  4942	$D^{\mathrm{co}}(\mathrm{CoFact}(X))$ without Koszulness.
  4943	The proof follows the same three-step assembly as
  4944	Theorem~\ref{thm:fact-co-contra-general}: (i) on each stratum
  4945	$\operatorname{Ran}_n$, Positselski~\cite[Theorem~7.2]{Positselski11}
  4946	gives the coderived equivalence for the restricted CDG-coalgebra;
  4947	(ii)~factorization compatibility of the bar-cobar counit;
  4948	(iii)~conservative assembly via
  4949	Theorem~\ref{thm:stratified-conservative-restriction}.
  4950	This closes structural gap~H1 and completes Future~2.
  4951	
  4952	\subsection{The Lagrangian form of complementarity}
  4953	
  4954	Theorem~C (Theorem~\ref{thm:quantum-complementarity-main}) establishes
  4955	the direct-sum decomposition
  4956	$Q_g(\cA) \oplus Q_g(\cA^!)
  4957	= H^*(\overline{\mathcal{M}}_g, \mathcal{Z}(\cA))$


thinking
**Analyzing theorem proof**

I'm considering that the theorem proof didn't clarify where non-degeneracy originates. It might relate to Step II duality regarding bar complexes, but not the ambient complex. The user’s request concerns proving Theorem C1, linked to chapter connections; I might not need to cover everything. I've noted important things like cross-surface drift and the interplay between theorem C and non-degenerate pairings. I should clarify if theorem C depends on non-degeneracy and possibly explore connections to support cross-surface drift.
thinking
**Evaluating Stage 1 dependencies**

I need to consider if Stage 1 relies on Proposition thqg-III-involutivity(a), which involves the `ev` map. That might be okay, but there’s a concern: if sigma isn't well-defined, Stage 1 could fail. That would be critical since it's foundational. I want to ensure everything lines up correctly so that the progression makes sense. It's essential to confirm that all the dependencies are solid before moving forward.
codex
The dependence web is broader than I first thought: even the ambient-complex proposition feeding the construction of `σ` quietly imports the perfectness criterion. I’m checking exact lines so I can separate foundational failures from downstream proof gaps.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '240,340p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/thqg_symplectic_polarization.tex | sed -n '96,195p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
    96	\mathbf{C}_g(\cA)
    97	:= \RGamma(\overline{\mathcal{M}}_g, \mathcal{Z}(\cA)),
    98	\end{equation}
    99	where $\mathcal{Z}(\cA)$ is the center local system on the
   100	Deligne--Mumford--Knudsen compactification
   101	$\overline{\mathcal{M}}_g$. When $g \ge 2$ and the relative bar
   102	family is perfect
   103	(Lemma~\ref{lem:perfectness-criterion}), the fiber--center
   104	identification
   105	(Theorem~\ref{thm:fiber-center-identification}) gives
   106	\begin{equation}\label{eq:thqg-III-bar-center}
   107	\mathbf{C}_g(\cA)
   108	\simeq
   109	\RGamma(\overline{\mathcal{M}}_g,
   110	R^0\pi_{g*}\barB^{(g)}(\cA)).
   111	\end{equation}
   112	\end{definition}
   113	
   114	\begin{remark}[H/M/S layers]\label{rem:thqg-III-hms}
   115	Following Convention~\ref{conv:hms-levels}:
 succeeded in 51ms:
   240	\end{enumerate}
   241	\end{lemma}
   242	
   243	\begin{proof}
   244	The projectors $p^\pm := \tfrac{1}{2}(\mathrm{id} \pm \sigma)$
   245	are cochain maps with $p^+ + p^- = \mathrm{id}$,
   246	$(p^\pm)^2 = p^\pm$, and $p^+ \circ p^- = 0$.
   247	Part~(a): the inclusion $\operatorname{im}(p^+) \oplus \operatorname{im}(p^-)
   248	\hookrightarrow V$ is a quasi-isomorphism by direct-sum decomposition,
   249	and $\operatorname{im}(p^\pm) \simeq \operatorname{fib}(\sigma \mp \mathrm{id})$
   250	via the standard cone identification.
   251	Part~(b) follows by applying $H^*$ to~(a).
   252	Part~(c): for $x, y \in V^+$ we have $\sigma x = x$, $\sigma y = y$,
   253	so $\langle x, y \rangle = \langle \sigma x, \sigma y \rangle
   254	= -\langle x, y \rangle$, hence $\langle x, y \rangle = 0$.
   255	Maximality is immediate from the direct-sum decomposition.
   256	\end{proof}
   257	
   258	\begin{definition}[Relative bar fiber complex]\label{def:relative-bar-fiber}
   259	\index{bar complex!relative fiber|textbf}







thinking
**Verifying theorem consistency**

I need to verify the exact lines in my file that relate to theorem C and its concordance. I'm feeling good about using the line numbers already in place. There's a potential degree shift at genus 1 that seems inconsistent with the dimension formula. I really need to nail down the exact issue here. 

Looking at proposition line 422, it states that degree = -(3g-3), and for g=1, this results in 0. Let's analyze this carefully!
thinking
**Evaluating index entry clarity**

I'm noticing that the index entry at 475 seems a bit misleading. It’s labeled as [MEDIUM/HIGH], but I’m questioning whether that accurately reflects what’s going on. I wonder if this could confuse users looking for precise information. Maybe I should consider double-checking the context to understand why it has that label. It’s important for clarity, so sorting that out could help prevent misunderstandings later.
thinking
**Evaluating duality stages**

I'm considering the duality stage conditionals. For Stage 4, I see it uses the nondegeneracy lemma from lines 621-631. But this lemma is conditional on perfectness mentioned in lines 390-393. There’s a note indicating that an alternative unconditional corollary exists but isn't written down. So, I conclude that what’s written doesn't support an unconditional statement. This whole framework seems a bit tricky, and I want to ensure clarity in my understanding.
thinking
**Analyzing theories and propositions**

I'm noticing a potential issue with the order of the propositions and theorems in the chapters. The proposition about Lagrangian eigenspaces appears later in the same chapter as a main theorem, while a theorem in the connections chapter might treat it as established earlier. I really need to check the sequence of parts because citations might not focus on the chapter order. It seems the proof claims to be self-contained, but I'm questioning that. This seems less severe than other construction issues, though.
thinking
**Structuring findings and counts**

I need to make sure my final structured output includes findings ordered by severity, followed by a summary. I should count the instances I've checked, possibly by step or dependency. Maybe I need to clarify what “instances checked” means—like the files or proof steps I'm reviewing? The user requested, “Instances checked: N | Violations found: N,” so I should define N as the total of “statement/proof/dependency surfaces checked.” I might also want to count the relevant sources I’ve read, including the theorem, proofs, and dependencies.
thinking
**Considering final summary structure**

I’m thinking about how to summarize the evaluation for different stages. Stage 1 and 2 are okay with sigma, but Stage 3 is unsupported, and Stage 4 is conditional, which contradicts genus 0. For clarity, I could format it as a bullet list where each bullet starts with `[CRITICAL]`. Each line would include a corresponding file and line number along with a brief description. I can also note multiple references in one bullet separated by semicolons.
thinking
**Verifying findings**

I'm considering how the quality comes from the Verdier pairing, but it's not completely proven yet. This is a good response to the question! I think I should ensure I counted "Instances checked 13" correctly. Let’s double-check and confirm that I've actually examined 13 surfaces. That seems fine to me! Now, I’ll get ready to prepare the final output.
codex
- [CRITICAL] [thqg_symplectic_polarization.tex:476](/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_symplectic_polarization.tex:476), [thqg_symplectic_polarization.tex:694](/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_symplectic_polarization.tex:694) — The theorem claims for every `g >= 0` that `Q_g(\cA) \cong Q_g(\cA^!)^\vee`, but the same file later proves `Q_0(\cA)=Z(\cA)` and `Q_0(\cA^!)=0`. No hypothesis forces `Z(\cA)=0`, so the genus-`0` boundary case contradicts the theorem as stated. The same contradiction propagates to [higher_genus_complementarity.tex:455](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:455) and [higher_genus_complementarity.tex:1701](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:1701).

- [CRITICAL] [thqg_symplectic_polarization.tex:197](/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_symplectic_polarization.tex:197), [thqg_symplectic_polarization.tex:220](/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_symplectic_polarization.tex:220), [thqg_symplectic_polarization.tex:163](/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_symplectic_polarization.tex:163) — The cochain involution `\sigma` is not actually constructed at the claimed unconditional level. The displayed definition uses an `ev` map `\mathbf C_g(\cA)^{\vee\vee} -> \mathbf C_g(\cA)` with no reflexivity/perfectness hypothesis or local justification, and this `\vee\vee` construction does not reappear elsewhere in the audited surfaces. Even the ambient-complex input quietly imports finite-dimensional fiber-cohomology from the perfectness criterion. That is a hidden assumption exactly where the theorem claims “no perfectness.”

- [CRITICAL] [thqg_symplectic_polarization.tex:592](/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_symplectic_polarization.tex:592), [higher_genus_complementarity.tex:1514](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:1514), [higher_genus_complementarity.tex:843](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:843) — Stage 3 does not follow from its citations. The proof identifies `+1/-1` eigencochains with `j_*/j_!` bar sectors and with `Q_g`, but `lem:eigenspace-decomposition-complete` is only a cohomology-level statement about `H^*(...)^\pm = Q_g`, and `lem:quantum-from-ss` only defines `Q_g` as `gr^g H^*(\bar B)` while explicitly deferring the eigenspace identification to that later lemma. So the core step proving “which summand is `\cA` and which is `\cA^!`” is unsupported.

- [HIGH] [thqg_symplectic_polarization.tex:621](/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_symplectic_polarization.tex:621), [thqg_symplectic_polarization.tex:388](/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_symplectic_polarization.tex:388) — The duality part of the proof is conditional as written. Stage 4 invokes `lem:thqg-III-nondegeneracy`, but that lemma assumes the relative bar family is perfect. The note at lines 633-640 says an unconditional proof could instead come from `cor:quantum-dual-complete`, but that alternative argument is not actually supplied.

- [HIGH] [concordance.tex:4954](/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:4954), [higher_genus_complementarity.tex:72](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:72), [higher_genus_complementarity.tex:455](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:455), [higher_genus_complementarity.tex:1783](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:1783) — The claim surface drifts on the central question “why Lagrangian, and is it unconditional?” The concordance and chapter introduction treat C1 as the direct-sum/eigenspace decomposition and C2 as the conditional Lagrangian upgrade via the Verdier pairing. But the main theory theorem and the later proposition promote Lagrangianity and perfect pairing to unconditional statements. The pairing in play is the Verdier pairing, but the manuscript does not maintain a consistent status boundary for its nondegeneracy or for the Lagrangian conclusion.

- [MEDIUM] [thqg_symplectic_polarization.tex:419](/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_symplectic_polarization.tex:419), [thqg_symplectic_polarization.tex:444](/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_symplectic_polarization.tex:444), [thqg_symplectic_polarization.tex:719](/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_symplectic_polarization.tex:719) — The genus-`1` scope is not fixed consistently. The theorem and ambient complex are stated over `\overline{\mathcal M}_g`, the degree-shift proof uses `\dim_\C \overline{\mathcal M}_g = 3g-3`, but the same file then switches to `\overline{\mathcal M}_{1,1}` for the actual genus-`1` computations. That leaves the genus-`1` boundary case formally ambiguous.

## Summary
Instances checked: 13 | Violations found: 6 | Verdict: FAIL

The eigenspace decomposition itself is supposed to be the `\pm1` splitting of the Verdier involution. The alleged Lagrangian property comes from the Verdier pairing. On the audited source, Stage 1-2 are only formal once a genuine cochain involution exists; Stage 3 is unsupported; Stage 4 is conditional; and the all-genera statement already breaks at `g=0`.
tokens used
113,642
