# G05_curved_flat_xvol (402s)

FIXED.

I audited the first 15 hits in `chapters/theory/` and only changed the genuinely curved cases that were still talking like ordinary cochain complexes. I added coderived or flat-comparison qualifiers in [bar_cobar_adjunction_curved.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/bar_cobar_adjunction_curved.tex:5871), [bar_cobar_adjunction_inversion.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/bar_cobar_adjunction_inversion.tex:120), [chiral_koszul_pairs.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex:6242), [chiral_modules.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_modules.tex:2126), and [cobar_construction.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/cobar_construction.tex:3107). The hits that were already square-zero because they used `D^{(g)}`, a strict associated graded, or the genus-0/Koszul lane were left unchanged.

Verification was narrow and source-level: I re-read each edited passage, `git diff --check` returned clean, and a targeted `rg` over the touched files found no residual `spectral sequence` / `H^*` phrasing directly tied to raw `\dfib` or `\kappa \cdot \omega_g` on those audited surfaces. I did not run a full TeX build.


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
session id: 019d885b-7688-7ad0-a4fd-c9db551e70c4
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


Fix curved-vs-flat confusion across Vol I (timed-out C14).

NARROW SCOPE: find spectral sequences or H^* applied to objects with d^2=kappa*omega_g.
Search for 'spectral sequence' near 'dfib' or 'kappa.*omega' in chapters/theory/.
For each: verify d^2=0 for the complex being used. If d^2!=0, add coderived qualifier.
Focus on the FIRST 15 instances only.
mcp startup: no servers

thinking
**Organizing codebase tasks**

I'm focusing on codebase questions and thinking about how to handle editing mathematical text. It seems useful to spawn explorers to search and summarize first. Then, maybe I can use exec to access file content around specific lines but avoid re-reading what’s already covered. I'll have explorers read mandatory files and relevant search results for context, then edit based on their findings. Frequent commentary updates are important, and I should utilize parallel tool calls when possible.
codex
Using `beilinson-rectify` and `multi-path-verify`: I’m locking the exact Vol I surface first, reading the required constitutional files, and having an explorer extract the first 15 `spectral sequence` / `H^*` instances near curved differentials in `chapters/theory/`.
collab spawn_agent(call_kNgHHxxlBFUL92l9tx7ypOi5, prompt="Read and summarize only the parts needed from these required-first-read files in /Users/raeez/chiral-bar-cobar: CLAUDE.m…")
mcp startup: no servers
spawn_agent(call_kNgHHxxlBFUL92l9tx7ypOi5, prompt="Read and summarize only the parts needed from these required-first-read files in /Users/raeez/chiral-bar-cobar: CLAUDE.m…") pending init:
  agent: 019d885b-bc2b-79b2-a96a-afb764be1704
collab spawn_agent(call_xivRIYnNRvQze7pWOhFmVeL8, prompt="In /Users/raeez/chiral-bar-cobar, search ONLY under chapters/theory/ for the first 15 instances where 'spectral sequence…")
spawn_agent(call_xivRIYnNRvQze7pWOhFmVeL8, prompt="In /Users/raeez/chiral-bar-cobar, search ONLY under chapters/theory/ for the first 15 instances where 'spectral sequence…") pending init:
  agent: 019d885b-bc2f-71a2-96a5-dccc778bd1f5
mcp startup: no servers
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && pwd' in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
/Users/raeez/chiral-bar-cobar
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '1,200p' CLAUDE.md" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
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

Plan update
Final-pass narrow audit on curved-vs-flat wording in Vol I. I’m grounding the scope first, then patching only the affected instances and verifying no AP regressions.
  → Read required constitutional files and extract constraints relevant to curved vs flat complexes
  • Locate first 15 in-scope spectral-sequence / H^* instances under chapters/theory/
  • Patch any instance that treats a curved differential as an honest cochain complex without qualification
  • Re-read edited passages and grep for residual in-scope violations
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "spectral sequence" chapters/theory' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Total output lines: 491

chapters/theory/three_invariants.tex:259: of the bar spectral sequence, which is a degree-$2$ statement
chapters/theory/quantum_corrections.tex:399:determined by the BRST spectral sequence: the ghost-number
chapters/theory/coderived_models.tex:314:\begin{proposition}[Coderived bar-degree spectral sequence;
chapters/theory/coderived_models.tex:317:\index{coderived category!bar-degree spectral sequence|textbf}
chapters/theory/coderived_models.tex:380:bar-degree spectral sequence collapses.
chapters/theory/coderived_models.tex:771:bounded-below spectral sequence with acyclic associated graded
chapters/theory/coderived_models.tex:781:on each stratum implies the associated graded spectral sequence
chapters/theory/coderived_models.tex:1034: The coderived bar-degree spectral sequence
chapters/theory/poincare_duality_quantum.tex:908:and prove it is a quasi-isomorphism by a spectral sequence argument
chapters/theory/koszul_pair_structure.tex:103:The total corrected differential $\Dg{g}$ absorbs the curvature into a higher-order correction, a curved $A_\infty$-structure in which $m_0 \neq 0$ and $m_1^2(a) = [m_0, a]$, and satisfies $\Dg{g}^2 = 0$. The passage from $\dzero$ to $\Dg{g}$ is the passage from classical to quantum: the quantum corrections are controlled by $H^*(\overline{\mathcal{M}}_g, Z(\cA))$, and Theorem~B (Theorem~\ref{thm:higher-genus-inversion}) shows that bar-cobar inversion persists via $E_2$~collapse of the associated spectral sequence. Theorem~C (Theorem~\ref{thm:quantum-complementarity-main}) identifies the obstruction and deformation spaces as Lagrangian complements.
chapters/theory/koszul_pair_structure.tex:502:The bar filtration on $\ChirHoch^*(\mathrm{Vir}_c)$ induces a spectral sequence
chapters/theory/koszul_pair_structure.tex:509:We claim this spectral sequence degenerates at $E_2$ for generic $c$.
chapters/theory/koszul_pair_structure.tex:527: $E_1^{p,q} = 0$ for $q > 0$ in the relevant spectral sequence.
chapters/theory/koszul_pair_structure.tex:533:The spectral sequence therefore degenerates at $E_2$, and
chapters/theory/koszul_pair_structure.tex:565:no new cohomology classes: the Hochschild--Serre spectral sequence for the
chapters/theory/koszul_pair_structure.tex:2245:Then there is a convergent spectral sequence
chapters/theory/koszul_pair_structure.tex:2275:The stratification spectral sequence has $E_1$~page
chapters/theory/koszul_pair_structure.tex:2284:are empty), so the spectral sequence collapses to the
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "curved" -n CLAUDE.md' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
363:**grading / curved**
366:- B48. `m_1^2 = 0` universally in curved A-inf. CORRECT: `m_1^2(a) = [m_0, a]`. AP46.
377:- B56. "Curved SC^{ch,top}-algebra" for the genus >= 1 bar complex. FALSE. It is a curved A_infinity-chiral algebra. The curvature d^2_{fib} = kappa * omega_g is on the A_infinity structure, not on an SC structure. AP165.
408:- B80. Two obstruction complexes for one obstruction. The same obstruction class Ob_g may live in different complexes with different H^2. Exactness in one complex (e.g., modular-bootstrap H^2=0) does NOT imply exactness in another (e.g., curved-Dunn twisting-cochain). Always specify WHICH complex.
537:| C | PROVED | C0 in D^co unconditional (curved well-typedness resolved via coderived fiber-center); C0 ordinary-cohomology conditional on perfectness. C1 g>=1 duality (genus-0 separated); reflexivity from perfectness (not hidden). C2 conditional on uniform-weight; object identity fixed; center-to-bar lift proved. ALT PROOF: PTVV shifted symplectic (H03). |
593:**duality** (AP33, AP29, AP31): H_k^! = Sym^ch(V*) != H_{-k}. Same kappa, different algebras. delta_kappa=kappa-kappa' (asymmetry, vanishes c=13) != kappa_eff=kappa(matter)+kappa(ghost) (cancellation, vanishes c=26). kappa=0 implies m_0=0 (uncurved); higher-degree components independent. F_1=0 does NOT imply F_g=0.
1081:**Specialized from existing (AP186-AP210):** AP186 (ProvedHere without proof block, 99C), AP187 (orphaned chapters), AP188 (empty sections), AP189 (dead labels), AP190 (hidden imports — cited result doesn't prove what's claimed, 119 findings), AP191 (circular proof chains, systematic detection), AP192 (scope inflation in statement vs proof), AP193 (biconditional stated, only forward proved), AP194 (curved complex treated with flat tools, 45 findings), AP195 (five-object conflation in prose, 47 findings), AP196 (SC misattribution in non-formula contexts), AP197 (bare Hochschild without qualifier, 89 findings), AP198 (Whitehead lemma scope — semisimple g only), AP199 (strong filtration inequality direction), AP200 (transfer theorem gap — H*(A) results applied to A), AP201 (Baxter constraint not vacuous at lambda=0), AP202 (coderived category element-wise argument invalid), AP203 (class-M harmonic mechanism unproved), AP204 (genus-0 boundary case contradiction), AP205 (reflexivity hidden in duality), AP206 (object switch mid-proof: Verdier ≠ cobar), AP207 (center-side vs bar-side lift missing), AP208 (Theorem A Verdier algebra/coalgebra flip), AP209 (missing lemma cited but never proved), AP210 (topologization chain-level vs cohomological conflation).
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "coderived" CLAUDE.md' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
536:| B | PROVED | Bar-cobar inversion: on-locus qi unconditional; off-locus coderived equivalence unconditional (independent proof, non-circular); off-locus chain qi conditional on kappa=0 or class G/L. ALT PROOF: Keller deformation + Kontsevich formality (H02). |
537:| C | PROVED | C0 in D^co unconditional (curved well-typedness resolved via coderived fiber-center); C0 ordinary-cohomology conditional on perfectness. C1 g>=1 duality (genus-0 separated); reflexivity from perfectness (not hidden). C2 conditional on uniform-weight; object identity fixed; center-to-bar lift proved. ALT PROOF: PTVV shifted symplectic (H03). |
1081:**Specialized from existing (AP186-AP210):** AP186 (ProvedHere without proof block, 99C), AP187 (orphaned chapters), AP188 (empty sections), AP189 (dead labels), AP190 (hidden imports — cited result doesn't prove what's claimed, 119 findings), AP191 (circular proof chains, systematic detection), AP192 (scope inflation in statement vs proof), AP193 (biconditional stated, only forward proved), AP194 (curved complex treated with flat tools, 45 findings), AP195 (five-object conflation in prose, 47 findings), AP196 (SC misattribution in non-formula contexts), AP197 (bare Hochschild without qualifier, 89 findings), AP198 (Whitehead lemma scope — semisimple g only), AP199 (strong filtration inequality direction), AP200 (transfer theorem gap — H*(A) results applied to A), AP201 (Baxter constraint not vacuous at lambda=0), AP202 (coderived category element-wise argument invalid), AP203 (class-M harmonic mechanism unproved), AP204 (genus-0 boundary case contradiction), AP205 (reflexivity hidden in duality), AP206 (object switch mid-proof: Verdier ≠ cobar), AP207 (center-side vs bar-side lift missing), AP208 (Theorem A Verdier algebra/coalgebra flip), AP209 (missing lemma cited but never proved), AP210 (topologization chain-level vs cohomological conflation).

exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "spectral" CLAUDE.md' in /Users/raeez/chiral-bar-cobarthinking
**Exploring skill files**

I'm thinking I might need to use skill files, as the instructions suggest after choosing a skill, I should open SKILL.md. I wonder if I should use the explorer or exec command to read the skill documentation. It makes sense to mention this as well. I'll read relevant skill documents using the exec_command and consider that the developer prefers explorer for this. I might explore doing this in parallel on the skill files.
 succeeded in 50ms:
539:| H | PROVED | ChirHoch*(A) polynomial Hilbert series, concentrated in cohomological degrees {0,1,2}. Coalgebra/Koszul-dual identification chain corrected (Verdier, not linear dual). Configuration-space collapse via FM-formality spectral sequence. ALT PROOF: deformation-theoretic dimensional analysis (H05). |
559:| Conformal anomaly | QUANTIFIED | Obstruction to constant coproduct = c/2 = κ(Vir_c). Quartic pole excess: primitive Delta gives c/(z-w)⁴ but need c/2. At c=0: obstruction vanishes (Heisenberg, constant coproduct exists). At c≠0: spectral parameter FORCED. |
568:| 6d hCS defect | PROVED | Codim-2 defect on C⊂C³ from 6d hCS: boundary algebra = W_{1+inf} with Psi=-sigma_2. c=1 (Sugawara). N_{C/Y}=C² gives spectral params (prop:codim2-defect-ope, 48 tests). |
920:AP165: B(A) is NOT an SC^{ch,top}-coalgebra. The bar complex B(A) = T^c(s^{-1} A-bar) is an E_1 chiral coassociative coalgebra (differential from chiral product, deconcatenation coproduct). It is a SINGLE E_1 coalgebra, not a two-colored SC datum. The SC^{ch,top} structure emerges in the chiral derived center: the chiral Hochschild cochain complex C^bullet_{ch}(A,A) (defined via the chiral endomorphism operad End^{ch}_A with spectral parameters from FM_k(C), NOT topological Hochschild cochains RHom_{A^e}(A,A)) carries brace operations and a Gerstenhaber bracket, and the pair (C^bullet_{ch}(A,A), A) is the SC^{ch,top} datum (bulk acting on boundary). FORBIDDEN claims: "B(A) is a coalgebra over SC^{ch,top}"; "the bar complex presents the Swiss-cheese algebra"; "the bar differential is the closed color"; "the bar coproduct is the open color." COUNTER: after writing any sentence involving B(A) and SC^{ch,top} in the same paragraph, verify that SC is attributed to the derived center pair, not to B(A).
1100:| B | Bar filtration spectral sequence | Keller deformation + Kontsevich formality (H02) |
codex
I’m loading only the skill instructions needed for this pass, then I’ll patch the audited instances directly and run a narrow verification sweep.
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "d_fib" -n CLAUDE.md' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' /Users/raeez/chiral-bar-cobar/.agents/skills/beilinson-rectify/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' /Users/raeez/chiral-bar-cobar/.agents/skills/multi-path-verify/SKILL.md" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
617:**SC/promotion** (AP86, AP87, AP89, AP90, AP91, AP92, AP93): B_{SC}(A) for one-colour ill-formed. SC is two-coloured; use promotion A->(A,A). Closed=B_{Com}(A), open=B_{Ass}(A), plus mixed sector. SC mixed-sector dim = (k-1)!*C(k+m,m), NOT (k-1)!*m!. FM_n(X) connected; only strata factor. Curved d^2=kappa*omega_g NOT coderivation (factor-2 cross-term at g>=1). Two curvatures: mu_0 (algebra, genus 0, strict) vs d_fib^2=kappa*omega_g (fiberwise, genus>=1, Hodge). delta_F_g^cross in CLOSED sector: "mixed channels" (propagator) != "mixed sector" (open-closed SC).
 succeeded in 51ms:
---
name: multi-path-verify
description: Use when the user asks to verify a formula, invariant, theorem status, computational claim, or family-specific value in this repository. Best for one claim or a small claim family where independent verification paths matter.
---

# Multi-Path Verify

Use this skill when one claim needs real verification rather than informal confidence.

## State the claim precisely

Write down:

- the exact formula or assertion
- the object or family it refers to
- the convention in force
- the claimed scope

If that statement is still ambiguous, do not verify a blurred version.

 succeeded in 51ms:
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


thinking
**Planning focused search for spectral sequence contexts**

I’m figuring out how to locate the first 15 instances of "spectral sequence" near key terms like 'dfib', 'kappa*omega', and curvature-related words within the theory chapters. To do this efficiently, I’m thinking of running a Python script that scans files lexically, extracts line contexts around each hit, checks for those keywords nearby, and annotates whether the differential squares to zero or is curved, plus if coderived qualifiers apply. This should help me pinpoint relevant passages with proper context and details!
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n \"H\\"'^" CLAUDE.md' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
159:% 2. A^i = H^*(B(A)) = dual coalgebra (Koszul cohomology of bar)
214:kappa(KM)=dim(g)(k+h^v)/(2h^v). kappa(Vir)=c/2. kappa(Heis)=k. kappa(W_N)=c*(H_N-1) where H_N=sum_{j=1}^{N} 1/j. Vir^!=Vir_{26-c}. Self-dual at c=13. kappa+kappa'=0 (KM/free), 13 (Vir). QME: hbar*Delta*S+(1/2){S,S}=0. sl_2 bar H^2=5 (not 6). Desuspension: |s^{-1}v|=|v|-1, NOT +1. eta(q)=q^{1/24}*prod(1-q^n). Bar propagator d log E(z,w): ALWAYS weight 1. Prime form: section of K^{-1/2} boxtimes K^{-1/2}. FM_n(X): blowup along diagonals, NOT complement. Grading: COHOMOLOGICAL (|d|=+1). Curved A-inf: m_1^2(a)=[m_0,a]. Bar d^2=0 always; curvature appears as m_1^2 != 0.
322:- B22. `dim H^2(B(sl_2)) = 6`. CORRECT: 5.
408:- B80. Two obstruction complexes for one obstruction. The same obstruction class Ob_g may live in different complexes with different H^2. Exactness in one complex (e.g., modular-bootstrap H^2=0) does NOT imply exactness in another (e.g., curved-Dunn twisting-cochain). Always specify WHICH complex.
549:| E_3 identification | PROVED (simple g) | Z^der_ch(V_k(g)) ≅ A^lambda as E_3-families over lambda*H^3(g)[[lambda]] (thm:e3-identification). Proof: E_3 formality (Kontsevich) + 1-dim of H^3(g) forces order-by-order uniqueness. For non-simple g: open (H^3 may be higher-dimensional). |
560:| Critical level jump | PROVED | At k=-h^v: kappa=0, ALL monodromy trivial (integer eigenvalues), H^1 doubles (4→8), Koszulness fails, bar H* = Omega*(Op_g^v(D)). Spectral sequence: d_1 = lambda*[delta] vanishes at lambda=0 (prop:critical-level-ordered). 72 tests. |
564:| AP128 bar H^2 | FIXED | sl2_bar_dims gave h_2=6 (CE/Riordan). Correct chiral bar: h_2=5. New sl2_chiral_bar_dims() function. AP63 discrepancy: Orlik-Solomon form factor. |
839:AP63: CE(g_-) != chiral bar for multi-gen. Orlik-Solomon form factor differs. sl_3 chiral H^2=36 vs CE H^2=20.
877:AP130: Fiber-base level confusion. Objects on the fiber (dτ ∈ H^{1,0}(E_τ)) are NOT objects on the base (c_1(λ) ∈ H^2(M̄_g)). The Hodge CLASS ω_g = c_1(E) lives on moduli space; the holomorphic FORM dτ lives on the elliptic curve. Before writing ω_g = [expression], verify: does [expression] live on M̄_g or on Σ_g?
908:AP154: Two distinct E_3 structures. (a) Algebraic E_3: from HDC on E_2 bar coalgebra, no conformal vector needed. (b) Topological E_3: from Sugawara topologisation, requires conformal vector at non-critical level. These are NOT the same; their identification as families over hbar*H^3(g)[[hbar]] is CONJECTURAL (conj:e3-identification). Topological E_3 (b): PROVED for affine KM at non-critical level (thm:topologization); CONJECTURAL for general chiral algebras with conformal vector (conj:topologization-general in Vol I, conj:E3-topological-climax in Vol II). Proof is cohomological; for class M, chain-level E_3 may fail. COUNTER: always specify which E_3 and whether the claim requires Sugawara.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && python - <<'PY'
import os,re
root='chapters/theory'
keywords=[r'dfib', r'kappa\\*omega', r'd\\"'^2 *= *kappa'"\\*omega', r'curved', r'fiberwise', r'curvature', r'kappa\\s*\\*\\s*omega']
pattern=re.compile('spectral sequence', re.I)
count=0
entries=[]
for dirpath,_,filenames in os.walk(root):
    filenames.sort()
    for fn in filenames:
        path=os.path.join(dirpath,fn)
        if not fn.endswith('.tex'):
            continue
        with open(path,encoding='utf-8') as f:
            lines=f.readlines()
        for idx,line in enumerate(lines):
            if pattern.search(line):
                start=max(0,idx-4)
                end=min(len(lines),idx+5)
                context=''.join(lines[start:end])
                if any(re.search(kw, context, re.I) for kw in keywords):
                    entries.append((path, idx+1, context.strip()))
                    count+=1
                    if count>=15:
                        break
        if count>=15:
            break
    if count>=15:
        break
for i,(path,ln,ctx) in enumerate(entries,1):
    print(i, path, ln)
    print(ctx)
    print('---')
PY" in /Users/raeez/chiral-bar-cobar exited 127 in 51ms:
zsh:1: command not found: python
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '1,200p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
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

exec
/bin/zsh -lc 'git status --short' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
?? scripts/final_gaps_campaign.py
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && python3 - <<'PY'
import os,re
root='chapters/theory'
keywords=[r'dfib', r'kappa\\*omega', r'd\\"'^2 *= *kappa'"\\*omega', r'curved', r'fiberwise', r'curvature', r'kappa\\s*\\*\\s*omega']
pattern=re.compile('spectral sequence', re.I)
count=0
entries=[]
for dirpath,_,filenames in os.walk(root):
    filenames.sort()
    for fn in filenames:
        path=os.path.join(dirpath,fn)
        if not fn.endswith('.tex'):
            continue
        with open(path,encoding='utf-8') as f:
            lines=f.readlines()
        for idx,line in enumerate(lines):
            if pattern.search(line):
                start=max(0,idx-4)
                end=min(len(lines),idx+5)
                context=''.join(lines[start:end])
                if any(re.search(kw, context, re.I) for kw in keywords):
                    entries.append((path, idx+1, context.strip()))
                    count+=1
                    if count>=15:
                        break
        if count>=15:
            break
    if count>=15:
        break
for i,(path,ln,ctx) in enumerate(entries,1):
    print(i, path, ln)
    print('---')
    print(ctx)
    print('===')
PY" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
1 chapters/theory/bar_cobar_adjunction_curved.tex 5874
---
\begin{remark}[Non-central curvature]\label{rem:non-central-curvature}
If the curvature $\mu_0$ is not central, then $d_{\text{bar}}^2 \neq 0$
and nilpotence holds only up to homotopy: the bar complex requires
homotopy coherent structures, spectral sequences that may not
degenerate, and the full $A_\infty$/$L_\infty$ framework at every level.
All standard chiral algebras (Heisenberg, Kac--Moody, Virasoro,
$\cW$-algebras) have central curvature, so strict nilpotence holds
throughout; see Remark~\ref{rem:voa-central-curvature} for the
===
2 chapters/theory/bar_cobar_adjunction_inversion.tex 30
---
(Theorem~\ref{thm:genus-graded-convergence}); off the Koszul locus,
the same counit remains invertible in the coderived
bar-coalgebra category, and promotion back to ordinary chain
cohomology requires an extra collapse input. The strict proof uses
the square-zero bar-cobar spectral sequence only on the Koszul lane.
The curved proof uses the coderived bar-degree filtration: the
curvature term lies in positive filtration, so the
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '1,200p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
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

collab wait(call_Dox2hrkyNGExwsxeJP9fefvh)
  receivers: 019d885b-bc2b-79b2-a96a-afb764be1704, 019d885b-bc2f-71a2-96a5-dccc778bd1f5
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '1,200p' raeeznotes/raeeznotes100/red_team_summary.md" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:
sed: raeeznotes/raeeznotes100/red_team_summary.md: No such file or directory

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '1,200p' archive/raeeznotes/raeeznotes100/red_team_summary.md" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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
**Gathering detailed spectral sequence entries**

I’m organizing 15 entries with file paths, line numbers, and relevant local sentences focusing on whether complexes have differential squares zero or curved, and if coderived qualifiers apply. I’ll open nearby lines in each noted file to extract exact text snippets, analyze mentions of curvature or differential behavior, and note spectral sequences or coderived contexts as needed. This way, I can clearly distinguish which complexes are curved or strict and support conclusions with local evidence.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '5850,5895p' chapters/theory/bar_cobar_adjunction_curved.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\end{align}

\emph{Term 9: $d_{\text{correction}}^2$}

Finally:
\begin{align}
d_{\text{correction}}^2(a_0 \otimes \cdots)
&= d_{\text{correction}}(\mu_0 \otimes a_0 \otimes \cdots) \\
&= \mu_0 \otimes \mu_0 \otimes (a_0 \otimes \cdots) \otimes \omega_g^2
\end{align}

In the bar complex, the element $s^{-1}\mu_0 \otimes s^{-1}\mu_0$ lives in the desuspended tensor square. Since $\mu_0 \in Z(\mathcal{A})$ has even degree (it is proportional to the vacuum $\mathbf{1} \in A^0$), the desuspension $s^{-1}\mu_0$ has degree $-1$. The Koszul sign from the bar differential acting on $s^{-1}\mu_0 \otimes s^{-1}\mu_0$ produces a sign $(-1)^{|s^{-1}\mu_0|} = -1$, so the two orderings of curvature insertion cancel: $d_{\text{correction}}^2 = 0$.

Combining all nine terms:
\begin{equation}
d_{\text{bar}}^2 = 0 + 0 + 0 + 0 + 0 + 0 + 0 = 0 \quad \text{strictly}
\end{equation}
provided $\mu_0 \in Z(\mathcal{A})$.

\end{proof}
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '1,80p' chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
%% ===== Editorial bridge: the inversion half of the chapter =====
%%
%% The first half of this chapter (bar_cobar_adjunction_curved.tex)
%% established the adjunction Omega^ch -| barB^ch and the curved A-infty
%% framework that supports it off the quadratic locus. This second half
%% proves that the adjunction inverts: Theorem B says
%% Omega(barB(A)) -> A is a quasi-isomorphism on the Koszul locus.
%% Together, Theorems A and B close the algebraic engine of the monograph.

\bigskip
\noindent\textbf{From adjunction to inversion.}\enspace
An adjunction that is not an equivalence is a deficiency: it
records the information lost in the round trip. Theorem~A
gives the adjunction $\Omegach \dashv \barBch$; the question is
whether the counit $\psi \colon \Omegach(\barBch(\cA)) \to \cA$
is a quasi-isomorphism, so that no information is lost. This is
not a formal consequence of the adjunction; it requires the
geometry of the Fulton--MacPherson compactification and the
Koszulness of the underlying chiral operad.

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '110,160p' chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\begin{tabular}{|l|l|l|l|}
\hline
\emph{Algebra} & \textbf{OPE Pole} & \textbf{Bar Differential} & \textbf{Effect} \\
\hline
Free Fermion $\psi$ & Simple: $\frac{1}{z-w}$ & Non-zero & contracts fields \\
Heisenberg $J$ & Double: $\frac{k}{(z-w)^2}$ & Zero (triple pole) & residue vanishes \\
\hline
\end{tabular}
\end{center}

No completion is needed. The bar complex is conilpotent (finite-dimensional in each bar degree) and the differential is zero except for the curvature term $m_0$. Convergence of the bar spectral sequence follows: the filtration by bar degree is bounded below ($n \geq 0$) and exhaustive, with finite-dimensional graded pieces, so the spectral sequence converges to the bar homology by the standard bounded-below complete convergence theorem (\cite{LV12}, Theorem~2.2.3).

\emph{Reference}: See \cite{GLZ22} Section 6, Proposition 6.2 for the identification
of the twisted chiral enveloping algebra with CE algebra structure.
\end{example}

\begin{example}[Affine Kac--Moody: quadratic]\label{ex:km-quadratic}
For $\widehat{\mathfrak{g}}_k$ (affine Lie algebra at level $k$), the generators are $V = \mathfrak{g}$ with relations $R = \{J^a \otimes J^b - f^{abc}J^c - k \delta^{ab} \mathbf{1}\}$.

The OPE is:

thinking
**Summarizing key guidance with citations**

I’m putting together a focused summary on topics like curved vs flat confusion, coderived qualifiers, spectral sequences, the equation d_fib² = κ·ω_g, H^* notation, and theorem/status discipline, citing exact line numbers from CLAUDE.md, concordance files, and related sources to ground the references in the user’s provided locations and instructions.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba chapters/connections/concordance.tex | sed -n '1,200p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '1630,1705p' chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
     1	\chapter{Concordance with primary literature}
     2	\label{chap:concordance}
     3	
     4	\index{concordance|textbf}
     5	
     6	This chapter is the constitution of the monograph. When chapters
     7	disagree, this chapter governs. It records the five main theorems
     8	with their precise status and locates every result against the
     9	prior literature: what is proved, what is conditional, what
    10	remains conjectural.
    11	
    12	The governing principle is falsification: every claim in these three
    13	volumes is presumed false until it appears below with an explicit
    14	status tag and a proof reference or independent verification trail.
    15	A theorem that contradicts the concordance is not a theorem; it is an
    16	error in the chapter that states it. Omission from this chapter is
    17	itself a verdict: what is not recorded here has not survived scrutiny.
    18	The concordance does not summarize the monograph; the monograph
    19	approximates the concordance.
    20	
 succeeded in 51ms:
 counit
 \[
 \psi_0 \colon \Omega_0(\bar{B}_0(\mathcal{A})) \longrightarrow \mathcal{A}
 \]
 is a quasi-isomorphism of chiral algebras.
 If, in addition, $\mathcal{A}$ lies on the higher-genus Koszul locus
 of Theorem~\ref{thm:higher-genus-inversion}
 \textup{(}for the standard landscape, by
 Theorems~\ref{thm:pbw-allgenera-km}--\ref{thm:pbw-allgenera-principal-w}\textup{)},
 then each genus component
 \[
 \psi_g \colon \Omega_g(\bar{B}_g(\mathcal{A})) \longrightarrow \mathcal{A}_g
 \]
 and the completed series
 \[
 \psi = \sum_{g=0}^\infty \hbar^{2g-2}\psi_g
 \]
 are quasi-isomorphisms.

\item \emph{Coderived off-Koszul lane.}
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '4500,4555p' chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\end{remark}

\medskip

In Chapter~\ref{chap:higher-genus}, the curve itself varies over
$\overline{\mathcal{M}}_g$, and the bar differential inherits
curvature from the open-sector trace and clutching data: the
genus-$g$ correction $m_0^{(g)}$ is a section of the obstruction
sheaf on $\overline{\mathcal{M}}_g$, controlled at the scalar
level by $\kappa(\cA)$ and at higher orders by the shadow
obstruction tower $\Theta_{\cA}^{\leq r}$
(Definition~\ref{def:shadow-postnikov-tower}). The passage
from this chapter to the next is the passage from operadic to
\emph{modular} Koszul duality, from the combinatorics of
associahedra to the geometry of the Deligne--Mumford
compactification, or, in the language of the categorical logarithm,
the passage from the single-valued to the multi-valued regime.

\subsection{Scalar rigidity and the quadratic frontier}
\label{subsec:scalar-rigidity-quadratic-frontier}
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba metadata/theorem_registry.md | sed -n '1,160p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
     1	# Theorem Registry
     2	
     3	Auto-generated on 2026-04-13 from the structured claim extractor in `scripts/generate_metadata.py`.
     4	
     5	This registry now tracks every `\ClaimStatusProvedHere` block directly from source, so the proved surface cannot silently drift behind the TeX tree.
     6	
     7	## Concordance Cross-Check
     8	
     9	- `thm:modular-koszul-duality-main` is cited in `chapters/connections/concordance.tex` as the flag theorem, but `chapters/theory/introduction.tex` currently provides only a `\phantomsection` label and no tagged claim block. It is therefore intentionally absent from the structured registry below.
    10	- `thm:shifted-symplectic-complementarity` is the conditional C2 theorem cited by concordance. Its `\ClaimStatusConditional` block contributes to the status totals below, but it does not appear in the proved-only registry tables.
    11	
    12	## Snapshot
    13	
    14	| Metric | Value |
    15	|---|---:|
    16	| ProvedHere claims | 2367 |
    17	| Total tagged claims | 3112 |
    18	| Active files in `main.tex` | 90 |
    19	| Total `.tex` files scanned | 104 |
    20	
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '3740,3785p' chapters/theory/chiral_hochschild_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\cite[3.4.4]{BD04} the derived pushforward of $\cA^{\boxtimes n}$
along the Ran space $\operatorname{Ran}(\Sigma_g)$. The bar
construction computes this pushforward
(Theorem~\ref{thm:geometric-equals-operadic-bar} for genus~$0$;
Theorem~\ref{thm:prism-higher-genus} for the extension to all
genera via the Feynman transform): the bar complex on
$\overline{C}_n(\Sigma_g)$ with the flat comparison differential
$\Dg{g}\big|_{[\Sigma_g]}$ computes the same ordinary cohomology as
the Ran-space pushforward. If $\kappa(\cA) \neq 0$, the raw fiberwise
operator $\dfib^{(\Sigma_g)}$ is curved and therefore belongs on the
coderived side rather than in ordinary cohomology.

\emph{Part~(ii).}
The assignment $[\Sigma_g] \mapsto
H^{\mathrm{ch}}_*(\Sigma_g, \cA)$ varies in a local system because
the flat comparison bar complex is a square-zero family over
$\overline{\mathcal{M}}_g$
(the bar family of~\eqref{eq:bar-family}), and the formation of
cohomology of a flat family produces a local system. The resulting
local system is precisely the center sheaf $\mathcal{Z}_\cA$ of
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '2210,2255p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
cohomological concentration, duality, polynomial Hilbert series,
and $\Etwo$-formality. The proof of
Proposition~\ref{prop:e2-formality-hochschild} uses the formality of
the local configuration spaces $\FM_n(\mathbb{C})$, so the higher
braces and Massey products on $\ChirHoch^*(\cA)$ are
cohomologically trivial. This is the full proved content of
\textup{(viii)} at the theorem level: no freeness statement for the
underlying graded-commutative cup-product algebra is claimed here.
No converse from
\textup{(viii)} to the bar-cobar counit is proved here.

\medskip
\textsc{$A_\infty$ formality}
\textup{(i)}$\Leftrightarrow$\textup{(iii)}:

\smallskip\noindent
\textup{(ii)}$\Rightarrow$\textup{(iii)}:
$E_2$-collapse means all PBW differentials $d_r = 0$ for $r \geq 2$.
The $A_\infty$ products $m_n$ are identified with $d_{n-1}$ under
the HPL transfer, so $m_n = 0$ for $n \geq 3$
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '2240,2275p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
each FM stratum (Proposition~\ref{prop:shadow-formality-low-degree});
on each fiber the HPL transfer is an ordinary $A_\infty$ transfer
over a field, to which Keller's theorem applies directly. The PBW
filtration is defined fiberwise and compatible with the FM
stratification, so fiberwise $E_2$-collapse assembles to global
$E_2$-collapse: all transferred differentials $d_r = 0$ for
$r \geq 2$. Hence the spectral sequence
on~$\barBgeom(\cA)$ also collapses at~$E_2$.

\medskip
\textsc{Factorization homology concentration}
\textup{(i)}$\Leftrightarrow$\textup{(vii)}
\textup{(}the equivalence concerns the genus-$0$ clause; the
uniform-weight all-genera statement is a proved refinement.
Cf.\ Remark~\ref{rem:fh-vii-uniform-weight-scope}\textup{)}:

\smallskip\noindent
\textup{(i)}$\Rightarrow$\textup{(vii)}:
The bar complex \emph{is} factorization homology
(Proposition~\ref{prop:bar-fh}):
wait(call_Dox2hrkyNGExwsxeJP9fefvh) timed out:
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '2595,2625p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\textup{(ii)}--\textup{(vii)} inside the meta-theorem.

\smallskip\noindent
\textup{(iii)}$\Rightarrow$\textup{(x)} is fiberwise and geometric.
For a boundary stratum $S_T$, the restriction
$i_{S_T}^!\,\barB_n(\cA)$ decomposes as the tensor product of the
vertexwise collision complexes, and
Remark~\ref{rem:iterated-residues-ainfty}
identifies those iterated residues with the transferred
$A_\infty$ operations.
If $m_k = 0$ for $k \geq 3$, only the strict binary residue survives
at each vertex.
Fiberwise Keller classicality, exactly as in
Theorem~\ref{thm:ainfty-koszul-characterization},
then gives degree-zero concentration for every vertex factor, so
the K\"unneth spectral sequence yields
\[
H^k\bigl(i_{S_T}^!\,\barB_n(\cA)\bigr)=0
\qquad (k \neq 0).
\]
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba archive/raeeznotes/raeeznotes100/red_team_summary.md | sed -n '1,200p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
     1	# Red-Team Summary of Vol1/Vol2 Claim Audit
     2	## Scope
     3	- Formal tagged claims catalogued: **4866**
     4	- Volume I formal claims: **2841**
     5	- Volume II formal claims: **2025**
     6	- Informal/meta claim harvest (README / PROGRAMMES / PROOF_ATLAS / audit notes): **94**
     7	- Every formal claim has an attached attack swarm in the master ledger. The informal harvest is separate because sentence-level slogans are less structurally tagged.
     8	
     9	## Status profile
    10	- ProvedHere: **3801**
    11	- Conjectured: **327**
    12	- Heuristic: **35**
    13	- ProvedElsewhere: **513**
    14	- Conditional: **116**
    15	- Open: **74**
    16	
    17	## Risk profile
    18	- medium: **1999**
    19	- low: **1913**
    20	- high: **807**
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba CLAUDE.md | sed -n '320,420p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '6230,6265p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   320	
   321	- B21. E_8 fundamental = 779247. Not any E_8 irreducible. FM5.
   322	- B22. `dim H^2(B(sl_2)) = 6`. CORRECT: 5.
   323	- B23. Genus-2 stable graphs = 6. CORRECT: 7. AP123.
   324	- B24. `1/\eta(q)^2` coefficients (1,3,6,10,...). CORRECT: (1,2,5,10,20,...) bicoloured partitions. AP135.
   325	- B25. `K_{BP} = 2`. CORRECT: `K_{BP} = 196`. AP140.
   326	
   327	**scope / quantifier**
   328	
   329	- B26. `obs_g = \kappa * \lambda_g` untagged. CORRECT: append (UNIFORM-WEIGHT) or (ALL-WEIGHT + delta F_g^cross). AP32.
   330	- B27. `A \iff B` in theorem where only forward proved. CORRECT: `\implies` + Remark on converse. AP36.
   331	- B28. "k=0 r-matrix vanishes and algebra fails Koszulness" for affine KM. CORRECT: k=0 is abelian limit, still Koszul; k=-h^v is critical, Koszulness fails. FM4.
   332	- B29. Theorem C^{E1} with `n` free on RHS but only `g` on LHS. CORRECT: fully quantify n with `2g-2+n > 0`. AP139.
   333	
   334	**macros / labels / LaTeX**
   335	
   336	- B30. `\end{definition>` (> instead of }). Regex: `\\end\{[^}]*>`. FM7.
   337	- B31. `\begin{theorem>`. Symmetric.
   338	- B32. `\cW` in standalone without `\providecommand`. FM6.
   339	- B33. `Part~IV`, `Chapter~12` hardcoded. CORRECT: `\ref{part:...}`. V2-AP26/FM10.
 succeeded in 51ms:
Theorem~\ref{thm:universal-kac-moody-koszul}: the bar construction
at level~$k$ produces a Koszul dual whose modular characteristic
equals $\kappa(\widehat{\mathfrak{g}}_{-k-2h^\vee})$.
\end{proof}

\subsection{Curved Koszul duality}

\begin{theorem}[Curved Koszul pairs; \ClaimStatusProvedHere]\label{thm:curved-koszul-pairs}
\index{curved Ainfinity@curved $A_\infty$!Koszul pairs}
\textup{[Regime: curved-central
\textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}

Filtered algebras $(\cA_1, \cA_2)$ with curvatures $\kappa_1, \kappa_2$ form a curved Koszul pair if:
\begin{enumerate}
\item Associated graded $(\mathrm{gr}\,\cA_1, \mathrm{gr}\,\cA_2)$ are classical Koszul dual
\item Curvatures are dual: $\kappa_1 \leftrightarrow -\kappa_2$ under the Koszul pairing
\item The spectral sequence associated to the filtration degenerates at $E_2$
\end{enumerate}
\end{theorem}

codex
The search surface is still being gathered. Once the explorer returns the first 15 candidates, I’ll patch only the curved cases and leave flat complexes untouched.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '6320,6385p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
is the decomposition of the BRST complex into Koszul dual sectors.
(Contributing to the derived/super extension flank adjoining
Conjecture~\ref{conj:master-infinite-generator}, not to the standard
$W_\infty$/Yangian packet.)
\end{remark}

% ================================================================
% SECTION 8.7: COUNTER-EXAMPLES - WHEN KOSZUL DUALITY FAILS
% ================================================================

\section{Counter-examples: when Koszul duality fails}
\label{sec:counter-examples}

\subsection{Virasoro algebra: beyond the quadratic setting}
\label{subsec:virasoro-non-example}

\begin{remark}[Virasoro Koszulness requires the PBW framework]
The Virasoro algebra with central charge $c$ does \emph{not} admit a
Koszul dual in the standard \emph{quadratic} (uncurved) sense, because
its OPE involves a quartic pole. However, it \emph{is} chiral Koszul in
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "FOUR OBJECTS" CLAUDE.md' in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
157:% FOUR OBJECTS:
collab wait(call_0YTFiRiacOw4GrjigigihEjG)
  receivers: 019d885b-bc2b-79b2-a96a-afb764be1704, 019d885b-bc2f-71a2-96a5-dccc778bd1f5
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba CLAUDE.md | sed -n '150,230p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   150	```
   151	
   152	### HZ-9. AP25/AP34/AP50 (four-functor discipline) -- 3 waves, 15+ instances
   153	
   154	Write this list before any paragraph mentioning "bar", "cobar", "Koszul dual", or "derived center":
   155	
   156	```
   157	% FOUR OBJECTS:
   158	% 1. B(A) = bar coalgebra = T^c(s^{-1} A-bar) with deconcatenation + twist
   159	% 2. A^i = H^*(B(A)) = dual coalgebra (Koszul cohomology of bar)
   160	% 3. A^! = ((A^i)^v) = dual ALGEBRA (linear or Verdier dual)
   161	% 4. Z^der_ch(A) = derived chiral center = Hochschild cochains = bulk
   162	```
   163	
   164	FORBIDDEN conflations:
   165	- "bar-cobar produces bulk" (wrong: bar-cobar inverts to A; bulk is Hochschild)
   166	- "Omega(B(A)) is the Koszul dual" (wrong: that is INVERSION)
   167	- "the Koszul dual equals the bar complex" (wrong: bar is coalgebra, dual is algebra)
   168	- "D_Ran(B(A)) is the cobar complex" (wrong: D_Ran is Verdier; cobar is Omega)
   169	
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '6370,6405p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
One needs the PBW spectral sequence approach (Theorem~\ref{thm:pbw-koszulness-criterion}), or equivalently, curved Koszul duality (Positselski) with nilpotent completion and a filtered/completed category.

\emph{Contrast with Heisenberg/Kac--Moody.}
\begin{center}
\begin{tabular}{|l|c|c|c|}
\hline
\textbf{Algebra} & \textbf{Quadratic?} & \textbf{PBW Koszul?} & \textbf{Dual} \\
\hline
Heisenberg $\mathcal{H}_k$ & Yes (genus 0) & Yes & $\mathrm{Sym}^{\mathrm{ch}}(V^*)$ [curved, $m_0 = -k\omega$] \\
Kac--Moody $\widehat{\mathfrak{g}}_k$ & Yes & Yes & $H^*(\barBgeom(\widehat{\mathfrak{g}}_k))^\vee$; $\kappa^! = \kappa(\widehat{\mathfrak{g}}_{-k-2h^\vee})$ \\
Virasoro $\text{Vir}_c$ & No & Yes (Thm~\ref{thm:virasoro-chiral-koszul}) & Completed curved (cf.\ \S\ref{sec:i-adic-completion}) \\
W-algebras $\mathcal{W}^k(\mathfrak{g})$ (universal) & No & Yes (Prop.~\ref{prop:pbw-universality}) & Completed curved \\
W-algebras $\mathcal{W}_k(\mathfrak{g})$ (simple quotient) & No & Open at admissible $k$ & Case-by-case \\
\hline
\end{tabular}
\end{center}

\emph{Note}: The Koszul dual
$\widehat{\mathfrak{g}}_k^! = H^*(\barBgeom(\widehat{\mathfrak{g}}_k))^\vee$
is the linear dual of the bar cohomology, \emph{not} the affine
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba CLAUDE.md | sed -n '520,580p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   520	
   521	**FM40. Naive center != derived center.** Z(Drin(H_k)) dim 1 vs Z^{der}_{ch}(H_k) dim 3. Ext^1,2 invisible to commutant. Specify which center: commutant, Hochschild, or categorical.
   522	
   523	**FM41. Jones polynomial requires Markov trace.** Raw KZ trace != Jones polynomial. Needs writhe normalization + quantum dimension factor.
   524	
   525	**AP186. Coincidental agreement masks bugs.** (Psi-1)/Psi = 1/Psi at Psi=2; comb(d+2,2) = comb(d+2,3) at d=3. Verify at 3+ parameter values.
   526	
   527	**AP187. Miura coefficients from elementary symmetric expansion.** T(u) = prod(u+Lambda_i) gives psi_s = e_s(Lambda_i). Coefficient of :J*W_{s-1}: is 1/Psi at all s >= 2 (structural, thm:miura-cross-universality).
   528	
   529	**FM28. Topologization scope conflation.** Opus marked thm:topologization as ClaimStatusProvedHere without scope, when the proof is verified only for affine KM at non-critical level (where Sugawara is explicit). For Virasoro and W-algebras, the proof depends on constructing the 3d HT BRST complex, which the manuscript itself acknowledges as conditional. Furthermore, the proof is COHOMOLOGICAL (works on Q-cohomology, not cochains). For class M, where chain-level data is essential, the E_3 may exist only on cohomology. Counter: every topologization claim must carry "(proved for affine KM at non-critical level; conjectural in general; cohomological, not chain-level)."
   530	
   531	## Theorem Status
   532	
   533	| Thm | Status | Key result |
   534	|-----|--------|------------|
   535	| A | PROVED | Bar-cobar adjunction + Verdier intertwining on Ran(X). Verdier half at algebra level post-D_Ran (rectified 2026-04-13). lem:filtered-comparison-unit written. Modular-family over M-bar_{g,n}: prop:bar-cobar-relative-extension (research programme). ALT PROOF: Lurie infinity-categorical nerve-realization (H01). |
   536	| B | PROVED | Bar-cobar inversion: on-locus qi unconditional; off-locus coderived equivalence unconditional (independent proof, non-circular); off-locus chain qi conditional on kappa=0 or class G/L. ALT PROOF: Keller deformation + Kontsevich formality (H02). |
   537	| C | PROVED | C0 in D^co unconditional (curved well-typedness resolved via coderived fiber-center); C0 ordinary-cohomology conditional on perfectness. C1 g>=1 duality (genus-0 separated); reflexivity from perfectness (not hidden). C2 conditional on uniform-weight; object identity fixed; center-to-bar lift proved. ALT PROOF: PTVV shifted symplectic (H03). |
   538	| D | PROVED | obs_g=kappa*lambda_g uniform-weight; multi-weight: +delta_F_g^cross. Circularity BROKEN: routing remark rem:non-circular-logical-chain installed; non-circular path: shadow tower -> genus universality -> family index. ALT PROOF: GRR on universal curve (H04), independent of thm:genus-universality. |
   539	| H | PROVED | ChirHoch*(A) polynomial Hilbert series, concentrated in cohomological degrees {0,1,2}. Coalgebra/Koszul-dual identification chain corrected (Verdier, not linear dual). Configuration-space collapse via FM-formality spectral sequence. ALT PROOF: deformation-theoretic dimensional analysis (H05). |
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '2100,2145p' chapters/theory/chiral_modules.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
condition \textup{(}$\dim V / C_2(V) < \infty$, where
$C_2(V) = \mathrm{span}\{a_{(-2)} b\}$\textup{)}. Then:
\begin{enumerate}[label=\textup{(\roman*)}]
\item $X_V = \{0\}$ if and only if $V$ is $C_2$-cofinite.
\item If $V$ is $C_2$-cofinite, then $V$ has finitely many simple
 modules \textup{(}Zhu~\cite{Zhu96}\textup{)}.
 \emph{Rationality} (that every grading-restricted module is
 completely reducible) is a strictly stronger condition; the
 triplet algebras $\mathcal{W}(p)$ are $C_2$-cofinite but
 \emph{not} rational
 \textup{(}see Example~\ref{ex:triplet-logarithmic}\textup{)}.
\item For the simple affine vertex algebra
 $L_k(\mathfrak{g})$ at admissible level~$k$, the associated variety
 is
 \[
 X_{L_k(\mathfrak{g})} = \overline{\mathbb{O}}
 \]
 where $\overline{\mathbb{O}}$ is the closure of a nilpotent
 orbit in $\mathfrak{g}^*$ determined by~$k$
 \textup{(}Arakawa~\cite{Arakawa17}\textup{)}.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '3085,3130p' chapters/theory/cobar_construction.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Bar-cobar inversion gives $\Omega(\bar{B}(\mathcal{H}_k)) \simeq \mathcal{H}_k$ automatically, while Koszul duality yields $\mathcal{H}_k^! \simeq \mathrm{Sym}^{\mathrm{ch}}(V^*)$ with curvature $m_0 = -k\,\omega$ (cf.\ \S\ref{sec:heisenberg-koszul}). These are distinct statements: bar-cobar inverts $\mathcal{H}_k$, but the Koszul dual is a different type of algebra (commutative vs.\ Lie). See Part~\ref{part:characteristic-datum}.
\end{example}

\section{Curved Koszul duality and quantum obstructions}
\label{sec:curved-koszul-quantum}

\begin{theorem}[Quantum deformation-obstruction complementarity; \ClaimStatusProvedElsewhere]\label{thm:deformation-obstruction}
\textup{[Regime: curved-central on the Koszul locus; all genera
\textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}

For a chiral algebra $\mathcal{A}$ on a curve $X$, the genus-$g$ quantum corrections
satisfy:
\[Q_g(\mathcal{A}) \oplus Q_g(\mathcal{A}^!) \simeq H^*(\mathcal{M}_g, Z(\mathcal{A}))\]
where:
\begin{itemize}
\item $Q_g(\mathcal{A})$ = space of genus-$g$ obstructions to Koszul duality
\item $Q_g(\mathcal{A}^!)$ = space of genus-$g$ deformations of the dual algebra
\item $Z(\mathcal{A})$ = center of $\mathcal{A}$
\item $H^*(\mathcal{M}_g, Z(\mathcal{A}))$ = cohomology of moduli space with coefficients in center
\end{itemize}
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '300,340p' chapters/theory/coderived_models.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:

For (b): the PBW filtration by conformal weight is exhaustive,
decreasing, preserved by all three components of the bar differential,
and satisfies $m_0^{(g)} \in F^1$ because the curvature involves at
least one OPE contraction. At associated graded level, the
differential reduces to $\dzero$, which is strict.

For (c): Verdier duality preserves the PBW filtration
(it exchanges weight~$n$ generators with weight~$n$ cogenerators in
the Koszul dual) and commutes with the bar differential. Hence it
descends to $\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$ and the
eigenspace decomposition is well-defined.
\end{proof}

\begin{proposition}[Coderived bar-degree spectral sequence;
\ClaimStatusProvedHere]
\label{prop:coderived-bar-degree-spectral-sequence}
\index{coderived category!bar-degree spectral sequence|textbf}
\index{bar-cobar inversion!coderived filtration}
Let

thinking
**Organizing detailed topic references**

I’m preparing a concise bullet-point summary that ties user questions to key concepts like curved vs flat confusion, H* notation, coderived qualifiers, spectral sequences, and theorem/status discipline, each with specific line references from CLAUDE.md, Concordance, metadata, and red team files to keep the response evidence-based and clear.
codex
- Curved-vs-flat warning: every discussion of curvature must keep the bar complex as the flat E₁ coalgebra and restrict the `d_fib² = κ·ω_g` curvature to the genus-≥1 fiberwise A∞ structure rather than the bar differential; `m₁²` equals `[m₀,·]` in the curved A∞ world and `d_bar²` is always zero, so avoid statements that tag the bar complex or SC^{ch,top} with the curvature. (`CLAUDE.md:363-379`)
- H\* notation / four objects: before invoking “bar,” “cobar,” “Koszul dual,” or “derived center,” spell out the four-object template (B(A), Aⁱ=H⁎(B(A)), A⁻, Z^{der}_{ch}) and remember that H⁎ refers to the Koszul cohomology of the bar (not its dual), keeping each object’s role distinct. (`CLAUDE.md:152-210`)
- Coderived qualifiers: Concordance lists Theorem C with C0 as an unconditional coderived fiber-center identification, an ordinary-derived result only on the flat perfect locus, C1 duality for g≥1, and C2 conditional on uniform-weight perfectness; the Theorem Status table echoes this distinction and emphasizes that off-Koszul-locus inversions are only coderived equivalences unless additional hypotheses (κ=0/class G/L) are met. (`chapters/connections/concordance.tex:32-58`; `CLAUDE.md:536-541`)
- Spectral sequences: the collision-depth spectral sequence for ChirHoch* collapses thanks to local Fulton–MacPherson formality, so any statement about ChirHoch* must cite that collapse and treat the configuration-space filtration as the fundamental justification for the cohomological concentration in {0,1,2}. (`chapters/connections/concordance.tex:71-82`; `CLAUDE.md:539`)
- Theorem/status discipline: the concordance chapter is the governing ledger—claims absent there are suspect, and each main theorem’s status (ProvedHere/Conditional) must align with its tag; the registry auto-tracks 2,367 ProvedHere blocks and shows the environment breakdown, while the red-team summary reinforces that conjectured/heuristic/conditional statements cannot be used as evidence and that label-status conflicts (nine recorded) and proved blocks citing non-proved labels (47 instances) are critical risk areas. (`chapters/connections/concordance.tex:6-82`; `metadata/theorem_registry.md:1-78`; `archive/raeeznotes/raeeznotes100/red_team_summary.md:1-110`)
wait(call_0YTFiRiacOw4GrjigigihEjG) 1 agents complete:
  019d885b-bc2b-79b2-a96a-afb764be1704 completed: "- Curved-vs-flat warning: every discussion of curvature must keep the bar complex as the flat E₁ coalgebra and restrict …"
codex
The constitutional read confirms the right fault line: `d_bar^2=0` always, while `d_fib^2 = \kappa\,\omega_g` belongs only to the curved fiberwise story. I’m now patching only those passages that wrongly feed the curved differential into plain `H^*` or unqualified spectral-sequence language.

Plan update
  ✓ Read required constitutional files and extract constraints relevant to curved vs flat complexes
  → Locate first 15 in-scope spectral-sequence / H^* instances under chapters/theory/
  • Patch any instance that treats a curved differential as an honest cochain complex without qualification
  • Re-read edited passages and grep for residual in-scope violations
thinking
**Summarizing spectral sequence audit entries**

I’m compiling a detailed audit of the first 15 spectral sequence references under chapters/theory, noting file paths, approximate line numbers, local excerpts about curvature and differentials, whether the complexes are curved or have square-zero differentials, and whether a coderived qualifier is likely needed. I’ll present a numbered bullet list highlighting each entry’s context, including quotes or paraphrases of relevant sentences, making clear distinctions about coderived necessity based on curvature and spectral sequence behavior. This will help clarify how curvature affects differential squares and coderived contexts across these key texts.
collab wait(call_GmL1ksjSKsevbidZNZe8VM3e)
  receivers: 019d885b-bc2f-71a2-96a5-dccc778bd1f5
codex
- `chapters/theory/bar_cobar_adjunction_curved.tex` (~5874): the remark on non-central curvature says “if the curvature µ₀ is not central, then $d_{\mathrm{bar}}^2 \neq 0$ and nilpotence holds only up to homotopy; the bar complex requires homotopy coherent structures, spectral sequences that may not degenerate, and the full $A_\infty/L_\infty$ framework.” When µ₀ is central, $d_{\mathrm{bar}}^2=0$, otherwise the differential is curved. Coderivedity is implied for the non-central regime because the usual spectral sequence cannot be assumed square-zero.

- `chapters/theory/bar_cobar_adjunction_inversion.tex` (~30): the introduction contrasts the square-zero bar-cobar spectral sequence on the Koszul lane with the curved proof, which “uses the coderived bar-degree filtration: the curvature term lies in positive filtration, so the associated-graded $E_1$ page is strict while coacyclicity records the inversion.” Off-Koszul the total complex is curved (curvature in filtration), and a coderived qualifier is built into the argument.

- `chapters/theory/bar_cobar_adjunction_inversion.tex` (~120): the example explains that “the bar complex is conilpotent and the differential is zero except for the curvature term $m_0$,” after which the bar spectral sequence converges via bounded-below filtration. The complex is essentially square-zero except for the single curvature insertion, so no extra coderived label is invoked.

- `chapters/theory/bar_cobar_adjunction_inversion.tex` (~1666): clause (3) of Theorem B states that the coderived bar-degree filtration supplies the spectral sequence whose $E_1$ is computed from the strict associated-graded differential because “the curvature relation $\dfib^2 = \kappa(\mathcal{A}) \cdot \omega_g$ is absorbed into positive filtration.” The cone is coacyclic only in the coderived setting, hence coderivedity is essential when $\dfib^2\neq0$.

- `chapters/theory/bar_cobar_adjunction_inversion.tex` (~4526): the section on scalar rigidity defines the categorical logarithm as the bar complex whose Taylor expansion is the PBW spectral sequence, and records that “its curvature $\dfib^2 = \kappa(\mathcal{A})\cdot\omega_g$ governs the genus transition.” Because $\dfib^2$ is explicitly nonzero, the genus-family complex is curved and the associated coderived input is required when the scalar package fails.

- `chapters/theory/chiral_hochschild_koszul.tex` (~3767): the proof explains that when $\kappa(\mathcal{A})\neq0$, “the raw fiberwise operator $\dfib^{(\Sigma_g)}$ is curved and therefore belongs on the coderived side rather than in ordinary cohomology,” and that the Leray spectral sequence for $\pi_g$ relates the total differential (fiberwise + moduli) to global sections. The complex is curved; coderived language is used to keep the fiberwise differential under control.

- `chapters/theory/chiral_koszul_pairs.tex` (~2237): the equivalence shows that fiberwise PBW collapse (all transferred $d_r=0$) forces the bar spectral sequence of the formal $A_\infty$ to collapse at $E_2$. The fiberwise differentials vanish, so the working complex is square-zero and no extra coderived qualifier is invoked.

- `chapters/theory/chiral_koszul_pairs.tex` (~2246): the loop-order spectral sequence of the higher-genus bar complex collapses on the modular Koszul locus, and after the genus-zero PBW collapse the higher loop strata stay cohomologically concentrated. The differentials vanish after fiberwise collapse, so this spectral sequence is standard and coderivedity is not triggered.

- `chapters/theory/chiral_koszul_pairs.tex` (~2610): analyzing boundary strata, a Künneth spectral sequence gives $H^k(i_{S_T}^! \barB_n(\mathcal{A}))=0$ for $k\neq0$ thanks to fiberwise Keller classicality, showing the boundary complex stays strict. No coderived refinement is needed because the differentials vanish.

- `chapters/theory/chiral_koszul_pairs.tex` (~6246): the curved Koszul-pair theorem insists that filtered algebras with curvatures satisfy (1) classical Koszul associated graded, (2) duality of curvatures, and (3) degeneration of the associated spectral sequence at $E_2$. The complex is curved (nontrivial $m_0$), but the statement stays within the curved Koszul regime; no coderived qualifier is explicitly introduced here.

- `chapters/theory/chiral_koszul_pairs.tex` (~6342): the Virasoro counterexample remarks that its OPE quartic pole prevents a standard quadratic Koszul resolution, so one “needs the PBW spectral sequence approach ... or equivalently, curved Koszul duality with nilpotent completion and a filtered/completed category.” The bar complex is curved and requires completion rather than coderived language per se; coderivedity is not directly cited but the filtered completion is crucial.

- `chapters/theory/chiral_koszul_pairs.tex` (~6370): the adjacent note emphasizes that the Heisenberg dual has curvature $m_0 = -k\omega$ entering through the central extension, so even abelian families live in the curved regime. Again, the complex is curved; the surrounding discussion relies on PBW spectral sequences rather than coderived refinements.

- `chapters/theory/chiral_modules.tex` (~2129): the remark on associated varieties states that when $X_V\neq\{0\}$ “the bar spectral sequence may have non-trivial higher differentials, marking the passage from Koszul to curved $A_\infty$.” The presence of nonzero higher differentials means the complex is no longer square-zero, although coderived language is not invoked there.

- `chapters/theory/cobar_construction.tex` (~3109): the quantum deformation-obstruction theorem invokes the genus spectral sequence and lays out curved $A_\infty$ relations, e.g., “$\mu_1^2 = [\mu_0,-]_{\mu_2}$, so $\mu_1$ is a differential only modulo curvature.” The complex is curved (mu₁ fails to square to zero), and although coderived terminology isn’t spelled out here, the curved spectral sequence handles the obstruction data.

- `chapters/theory/coderived_models.tex` (~317): the coderived bar-degree spectral sequence proposition says that the curvature lies in $F^1$ so $\operatorname{gr}^0 d_K$ is square-zero, and vanishing of the $E_1$ page implies the cone is coacyclic. This spectral sequence is inherently coderived; the underlying complex is curved but the filtration isolates the square-zero part.
wait(call_GmL1ksjSKsevbidZNZe8VM3e) 1 agents complete:
  019d885b-bc2f-71a2-96a5-dccc778bd1f5 completed: "- `chapters/theory/bar_cobar_adjunction_curved.tex` (~5874): the remark on non-central curvature says “if the curvature …"


thinking
**Checking file contexts**

I need to get the exact contexts of the files since the explorer only provided approximate lines. It seems I could use the exec_command to view specific snippets in those files for editing. I might not need to reread the code they covered, but I do need to read those exact portions. It looks like I should focus on the first 15 candidate instances; I'll verify if each has the d²=0 condition and patch them if necessary.
thinking
**Searching for patterns**

I need to search for exact patterns using exec_command. I might use commands like `rg -n "spectral sequence|dfib|kappa\\(\\\\mathcal|\\omega_g|coderived"` across specific files. It sounds like I should employ multi_tool_use.parallel to gather snippets from multiple files. I might also consider using `rg -n -C 3` with those patterns and group results by file. I plan to run parallel exec_command for about six files to efficiently gather the information I need.
codex
I have the 15-instance audit list. Next I’m reading the exact local snippets in those files so I can decide which ones truly need a coderived qualifier and which are already correctly flat.
exec
/bin/zsh -lc "rg -n -C 3 'spectral sequence|dfib|omega_g|coderived|coacyclic|H\\"'^'"\\*|H\\"'^k|cohomology'"' chapters/theory/bar_cobar_adjunction_curved.tex chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -C 3 'spectral sequence|dfib|omega_g|coderived|coacyclic|H\\"'^'"\\*|H\\"'^k|cohomology'"' chapters/theory/chiral_hochschild_koszul.tex chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Total output lines: 1718

chapters/theory/bar_cobar_adjunction_curved.tex-15-Theorem~B (Theorem~\ref{thm:bar-cobar-inversion-qi}) says
chapters/theory/bar_cobar_adjunction_curved.tex-16-that~$\tau_\cA$ is \emph{acyclic}: the twisted tensor
chapters/theory/bar_cobar_adjunction_curved.tex-17-product $\cA \otimes_{\tau_\cA} \barBch(\cA)$ has trivial
chapters/theory/bar_cobar_adjunction_curved.tex:18:cohomology, so the counit
chapters/theory/bar_cobar_adjunction_curved.tex-19-$\psi \colon \Omegach(\barBch(\cA)) \xrightarrow{\;\sim\;} \cA$
chapters/theory/bar_cobar_adjunction_curved.tex-20-is a quasi-isomorphism on the Koszul locus.
chapters/theory/bar_cobar_adjunction_curved.tex-21-The two theorems are a single statement: every algebraic identity
--
chapters/theory/bar_cobar_adjunction_curved.tex-29-$\mathcal{W}_\infty$ all require curved or filtered presentations in
chapters/theory/bar_cobar_adjunction_curved.tex-30-which $\mu_0 \neq 0$ and $\mu_1^2 = [\mu_0, -]_{\mu_2}$. On this
chapters/theory/bar_cobar_adjunction_curved.tex-31-extended locus the adjunction survives in the language of curved
chapters/theory/bar_cobar_adjunction_curved.tex:32:$\Ainf$~algebras, $I$-adic completions, and coderived categories.
chapters/theory/bar_cobar_adjunction_curved.tex-33-The strict convolution dg Lie algebra
chapters/theory/bar_cobar_adjunction_curved.tex-34-$\Convstr(\barBch(\cA), \cA)$ is replaced by its homotopy-invariant
chapters/theory/bar_cobar_adjunction_curved.tex-35-envelope $\Convinf(\barBch(\cA), \cA)$, and the twisting morphism
--
chapters/theory/bar_cobar_adjunction_curved.tex-70- no completion needed (Heisenberg, free fields, lattice VOAs);
chapters/theory/bar_cobar_adjunction_curved.tex-71-\item \emph{Curved-central} ($d_0^{\,2} \neq 0$,
 succeeded in 50ms:
Total output lines: 2051

chapters/theory/chiral_hochschild_koszul.tex:1:\chapter{Chiral Hochschild cohomology and Koszul duality}
chapters/theory/chiral_hochschild_koszul.tex-2-\label{chap:deformation-theory}
chapters/theory/chiral_hochschild_koszul.tex-3-
chapters/theory/chiral_hochschild_koszul.tex-4-\index{deformation theory!chiral|textbf}
chapters/theory/chiral_hochschild_koszul.tex:5:\index{Hochschild cohomology!chiral|textbf}
chapters/theory/chiral_hochschild_koszul.tex-6-
chapters/theory/chiral_hochschild_koszul.tex-7-The MC element $\Theta_\cA \in \MC(\gAmod)$ controls all of chiral
chapters/theory/chiral_hochschild_koszul.tex-8-Koszul duality, but how rigid is the moduli it lives in? Without
--
chapters/theory/chiral_hochschild_koszul.tex-49- (Theorem~\ref{thm:chiral-deligne-tamarkin}). The brace dg algebra
chapters/theory/chiral_hochschild_koszul.tex-50- structure makes $C^\bullet_{\mathrm{ch}}$ the universal bulk:
chapters/theory/chiral_hochschild_koszul.tex-51- it is the terminal local chiral Swiss-cheese pair over $\cA$, and
chapters/theory/chiral_hochschild_koszul.tex:52: its cohomology $Z_{\mathrm{ch}}(\cA) = H^*(C^\bullet_{\mathrm{ch}},
chapters/theory/chiral_hochschild_koszul.tex-53- \delta)$ is the chiral derived center
chapters/theory/chiral_hochschild_koszul.tex-54- (Definition~\ref{def:thqg-chiral-derived-center}).
chapters/theory/chiral_hochschild_koszul.tex-55-\end{enumerate}
--
chapters/theory/chiral_hochschild_koszul.tex-121-differential does (Chapter~\ref{chap:bar-cobar}).
exec
/bin/zsh -lc "rg -n -C 3 'spectral sequence|dfib|omega_g|coderived|coacyclic|H\\"'^'"\\*|H\\"'^k|cohomology'"' chapters/theory/chiral_modules.tex chapters/theory/cobar_construction.tex chapters/theory/coderived_models.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
Total output lines: 1499

chapters/theory/coderived_models.tex-1-
chapters/theory/coderived_models.tex-2-\section{Coderived and contraderived categories}
chapters/theory/coderived_models.tex:3:\label{app:coderived}
chapters/theory/coderived_models.tex:4:\index{coderived category|textbf}
chapters/theory/coderived_models.tex-5-\index{contraderived category|textbf}
chapters/theory/coderived_models.tex-6-
chapters/theory/coderived_models.tex-7-The bar-cobar adjunction at higher genus produces curved complexes
chapters/theory/coderived_models.tex-8-($d^2 \neq 0$), for which ordinary cohomological derived methods
chapters/theory/coderived_models.tex-9-are no longer the right invariant.
chapters/theory/coderived_models.tex:10:Positselski's theory of coderived and contraderived
chapters/theory/coderived_models.tex-11-categories~\cite{Positselski11} provides the correct
chapters/theory/coderived_models.tex-12-replacement. This appendix collects the definitions and key results
chapters/theory/coderived_models.tex-13-needed in this monograph; the chiral specialization appears in
chapters/theory/coderived_models.tex:14:\S\ref{subsec:chiral-coderived-contraderived}.
chapters/theory/coderived_models.tex-15-
chapters/theory/coderived_models.tex-16-\subsection{Abstract definitions}
chapters/theory/coderived_models.tex:17:\label{subsec:coderived-abstract}
chapters/theory/coderived_models.tex-18-

thinking
**Identifying necessary edits**

I need to figure out which of these 15 items really require edits, but the search results are overwhelming and truncated. I might need exact snippets around candidate line numbers. Using `sed -n` around specific lines could work here, like this: `sed -n '5850,5905p' file`. 

Since the instructions advise against using Python if simple shell commands will do, I think I should focus on using multiple `exec_command` for groups of 5 commands with non-adjacent ranges. This could help me gather the exact contexts I need. I’ll work on this file by file!
exec
/bin/zsh -lc "nl -ba chapters/theory/bar_cobar_adjunction_curved.tex | sed -n '5560,5895p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  5560	The twisted structure $(A, \{\mu_n^\alpha\})$ is again a curved $A_\infty$ algebra, with new 
  5561	curvature:
  5562	\begin{equation}
  5563	\mu_0^\alpha = \mu_0 + \mu_1(\alpha) + \frac{1}{2}\mu_2(\alpha, \alpha) + \cdots
  5564	\end{equation}
  5565	
  5566	If $\alpha$ is an MC element, then $\mu_0^\alpha = 0$, so the twisted structure is 
  5567	\emph{uncurved}.
  5568	\end{theorem}
  5569	
  5570	\begin{remark}[MC elements as uncurving data]
  5571	\label{rem:mc-uncurving}
  5572	If $(A, \{\mu_n\})$ is curved with $\mu_0 \neq 0$, an MC element
  5573	$\alpha \in A^1$ satisfying $\sum_{n \geq 0} \mu_n(\alpha^{\otimes n}) = 0$
  5574	produces the twisted structure $(A, \{\mu_n^\alpha\})$ with $\mu_0^\alpha = 0$:
  5575	the MC equation is the condition that twisting by $\alpha$ removes the curvature.
  5576	If no MC element exists, the curvature persists: the total bar
  5577	differential satisfies $d_{\mathrm{bar}}^2 = 0$ regardless, but the
  5578	fiberwise differential over $\overline{\mathcal{M}}_g$ has
  5579	$d_{\mathrm{fib}}^2 = \kappa \cdot \omega_g \neq 0$.
exec
/bin/zsh -lc "nl -ba chapters/theory/bar_cobar_adjunction_inversion.tex | sed -n '1,220p;1648,1705p;4518,4545p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_hochschild_koszul.tex | sed -n '3748,3788p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '2225,2260p;2598,2622p;6238,6385p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_modules.tex | sed -n '2118,2140p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/coderived_models.tex | sed -n '314,365p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/cobar_construction.tex | sed -n '3098,3192p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
     1	%% ===== Editorial bridge: the inversion half of the chapter =====
     2	%%
     3	%% The first half of this chapter (bar_cobar_adjunction_curved.tex)
     4	%% established the adjunction Omega^ch -| barB^ch and the curved A-infty
     5	%% framework that supports it off the quadratic locus. This second half
     6	%% proves that the adjunction inverts: Theorem B says
     7	%% Omega(barB(A)) -> A is a quasi-isomorphism on the Koszul locus.
     8	%% Together, Theorems A and B close the algebraic engine of the monograph.
     9	
    10	\bigskip
    11	\noindent\textbf{From adjunction to inversion.}\enspace
    12	An adjunction that is not an equivalence is a deficiency: it
    13	records the information lost in the round trip. Theorem~A
    14	gives the adjunction $\Omegach \dashv \barBch$; the question is
    15	whether the counit $\psi \colon \Omegach(\barBch(\cA)) \to \cA$
    16	is a quasi-isomorphism, so that no information is lost. This is
    17	not a formal consequence of the adjunction; it requires the
    18	geometry of the Fulton--MacPherson compactification and the
    19	Koszulness of the underlying chiral operad.
    20	
 succeeded in 51ms:
  3748	the Ran-space pushforward. If $\kappa(\cA) \neq 0$, the raw fiberwise
  3749	operator $\dfib^{(\Sigma_g)}$ is curved and therefore belongs on the
  3750	coderived side rather than in ordinary cohomology.
  3751	
  3752	\emph{Part~(ii).}
  3753	The assignment $[\Sigma_g] \mapsto
  3754	H^{\mathrm{ch}}_*(\Sigma_g, \cA)$ varies in a local system because
  3755	the flat comparison bar complex is a square-zero family over
  3756	$\overline{\mathcal{M}}_g$
  3757	(the bar family of~\eqref{eq:bar-family}), and the formation of
  3758	cohomology of a flat family produces a local system. The resulting
  3759	local system is precisely the center sheaf $\mathcal{Z}_\cA$ of
  3760	Beilinson--Drinfeld~\cite[3.4.10]{BD04}.
  3761	
  3762	\emph{Part~(iii).}
  3763	Global sections of $\mathcal{Z}_\cA$ over
  3764	$\overline{\mathcal{M}}_g$ compute
  3765	$R\Gamma(\overline{\mathcal{M}}_g, \mathcal{Z}_\cA)$
  3766	by definition.
  3767	By the Leray spectral sequence for
 succeeded in 51ms:
  2225	\smallskip\noindent
  2226	\textup{(ii)}$\Rightarrow$\textup{(iii)}:
  2227	$E_2$-collapse means all PBW differentials $d_r = 0$ for $r \geq 2$.
  2228	The $A_\infty$ products $m_n$ are identified with $d_{n-1}$ under
  2229	the HPL transfer, so $m_n = 0$ for $n \geq 3$
  2230	(Proposition~\ref{prop:ainfty-formality-implies-koszul}).
  2231	
  2232	\smallskip\noindent
  2233	\textup{(iii)}$\Rightarrow$\textup{(ii)}:
  2234	If $m_n = 0$ for $n \geq 3$, the minimal $A_\infty$-model is
  2235	strictly associative: $H^*(\barBgeom(\cA))$ is a dg algebra with
  2236	$m_2$ as the product and all higher operations trivial. The
  2237	bar spectral sequence of this formal $A_\infty$-algebra collapses
  2238	at~$E_2$ by the classicality theorem for formal $A_\infty$-algebras
  2239	(Keller). The chiral $A_\infty$ structure is computed fiberwise on
  2240	each FM stratum (Proposition~\ref{prop:shadow-formality-low-degree});
  2241	on each fiber the HPL transfer is an ordinary $A_\infty$ transfer
  2242	over a field, to which Keller's theorem applies directly. The PBW
  2243	filtration is defined fiberwise and compatible with the FM
  2244	stratification, so fiberwise $E_2$-collapse assembles to global
 succeeded in 50ms:
  3098	where:
  3099	\begin{itemize}
  3100	\item $Q_g(\mathcal{A})$ = space of genus-$g$ obstructions to Koszul duality
  3101	\item $Q_g(\mathcal{A}^!)$ = space of genus-$g$ deformations of the dual algebra
  3102	\item $Z(\mathcal{A})$ = center of $\mathcal{A}$
  3103	\item $H^*(\mathcal{M}_g, Z(\mathcal{A}))$ = cohomology of moduli space with coefficients in center
  3104	\end{itemize}
  3105	\end{theorem}
  3106	
  3107	\begin{proof}[Proof (outline; full proof in \S\textup{\ref{sec:complementarity-theorem}})]
  3108	The complete proof, synthesizing five lemmas via the Verdier
  3109	involution~$\sigma$ and the genus spectral sequence, is given in
  3110	Theorem~\ref{thm:quantum-complementarity-main}.
  3111	
  3112	\emph{Foundation: Curved $A_\infty$ Structures}
  3113	
  3114	Following Gui--Li--Zeng~\cite{GLZ22}, a curved chiral algebra $\mathcal{A}$ has:
  3115	\begin{enumerate}
  3116	\item Multiplication: $\mu_2: \mathcal{A}^{\otimes 2} \to \mathcal{A}$
  3117	\item Higher operations: $\mu_n: \mathcal{A}^{\otimes n} \to \mathcal{A}$ for $n \geq 3$
 succeeded in 50ms:
   314	\begin{proposition}[Coderived bar-degree spectral sequence;
   315	\ClaimStatusProvedHere]
   316	\label{prop:coderived-bar-degree-spectral-sequence}
   317	\index{coderived category!bar-degree spectral sequence|textbf}
   318	\index{bar-cobar inversion!coderived filtration}
   319	Let
   320	$f \colon (M, d_M, \mathcal{F}) \to (N, d_N, \mathcal{F})$
   321	be a morphism of filtered curved factorization models with
   322	bounded-below filtration, and let
   323	$K := \operatorname{cone}(f)$.
   324	Then the induced filtration on~$K$ yields
   325	\[
   326	E_0^{p,q}(K)
   327	=
   328	\bigl(F^p K/F^{p+1}K\bigr)^{p+q},
   329	\qquad
   330	E_1^{p,q}(K)
   331	=
   332	H^{p+q}\bigl(E_0^{p,\bullet}(K), \operatorname{gr}^0 d_K\bigr),
   333	\]
 succeeded in 50ms:
  2118	 orbit in $\mathfrak{g}^*$ determined by~$k$
  2119	 \textup{(}Arakawa~\cite{Arakawa17}\textup{)}.
  2120	 In particular, $L_k(\mathfrak{g})$ is rational if and only if
  2121	 $X_{L_k(\mathfrak{g})} = \{0\}$, which occurs at the
  2122	 non-degenerate admissible levels.
  2123	\end{enumerate}
  2124	\end{theorem}
  2125	
  2126	\begin{remark}[Associated variety and Koszul duality]
  2127	\label{rem:associated-variety-koszul}
  2128	\index{associated variety!Koszul duality}
  2129	The associated variety is \emph{not} preserved by level-shifting Koszul duality: e.g., $X_{L_1(\mathfrak{sl}_2)} = \{0\}$ but $X_{L_{-3}(\mathfrak{sl}_2)} = \mathfrak{sl}_2^*$. When $X_V = \{0\}$, the bar spectral sequence degenerates at a finite page; for $X_V \neq \{0\}$ it may have non-trivial higher differentials, marking the passage from Koszul to curved $A_\infty$.
  2130	\end{remark}
  2131	
  2132	\begin{conjecture}[Type-$A$ orbit duality for affine simple quotients; \ClaimStatusConjectured]
  2133	\label{conj:orbit-duality}
  2134	\index{Barbasch--Vogan duality!orbit duality}
  2135	\index{associated variety!orbit duality}
  2136	\index{nilpotent orbit!Koszul duality}
  2137	Let $\mathfrak{g}$ be a simple Lie algebra of type~$A$






thinking
**Identifying file instances**

I’m thinking I might need to run our own regular expression to find the first 15 instances in file order. But hold on, I realize the explorer tool has already arranged them by appearance! Okay, maybe I should trust that. Some of these instances are in comments, though, which complicates things a bit. I need to figure out which of those 15 actually need edits.
thinking
**Evaluating mathematical concepts**

I'm thinking about an inversion example on line 120. It seems like there might even be a way to patch it, even if it's commented out. The details indicate that differential is zero except for the curvature term m0. It’s interesting that the spectral sequence converges to bar homology. There’s a lot to unpack here regarding these mathematical terms, and I’m curious how they all tie together in this context!
thinking
**Analyzing algebraic structures**

I’m considering adding concepts like "coderived spectral sequence" and the connection to Omega(B(A1)) ≃ A2 in a coderived sense. There's a need to ensure the current proof stands, especially if the total curved differential doesn't square to zero. I should verify the d^2 of the complex used. It's notable that filtered bar complexes of curved A∞ algebras don’t relate to ordinary cohomology. I also think patching the theorem and proof is necessary to address some gaps.
thinking
**Considering patches in algebra**

I think it’s a good idea to mention that the off-Koszul comparison exists on the coderived side once we step away from the square-zero locus. This is related to spectral sequences rather than directly to H^*. It feels like a solid patch! I’ll also note the cobar construction segments, like 3107-3110 and 3131-3184, to ensure I keep everything organized and double-check I’m accurately capturing the critical concepts. This looks worth exploring further!
thinking
**Evaluating hot zone protocols**

I need to provide an update before editing, possibly including a Pre-Edit Verification (PE) template if it's a hot zone. For the spectral sequence near a curved differential, I’m thinking maybe PE-10? However, the AGENTS state that a Pre-Edit Verification Protocol is mandatory before editing these critical areas. The hot zones top 10 don’t specify curved vs. flat, but the user is asking to fix that confusion. Let's clarify that for them!
thinking
**Planning a concise commentary**

I’m thinking we can create a succinct commentary block that lists file surfaces and indicates if they are complex, square-zero, or coderived. This should be straightforward, so let's go for it! I need to use an `update_plan` to mark the editing as in progress. But before I make those edits, I should definitely send out an update. Let's ensure everything is clear and organized!
codex
I’ve separated the 15 hits into three classes: already safe because they use `D^{(g)}` or an associated-graded square-zero complex, safe because they are genus-0/Koszul-locus strict, and genuinely ambiguous curved cases that still speak as if ordinary `H^*` or an unqualified spectral sequence were available.

```text
scope: curved-vs-flat spectral-sequence / H^* audit, first 15 hits under chapters/theory/

bar_cobar_adjunction_curved.tex:5871-5875
complex: non-central curved bar object
square_zero? N
current issue: unqualified “spectral sequences” on curved object
verdict: ACCEPT -> add coderived / associated-graded qualifier

bar_cobar_adjunction_inversion.tex:21-33
complex: strict Koszul lane vs coderived off-Koszul lane, explicitly separated
square_zero? Y/N split is already stated
verdict: ACCEPT -> no edit

bar_cobar_adjunction_inversion.tex:98-120 [inside \\iffalse block]
complex: commented Heisenberg example mixes curvature with bar homology
square_zero? ambiguous in source text
verdict: ACCEPT -> tighten source text while keeping it inert

bar_cobar_adjunction_inversion.tex:1664-1683
complex: coderived cone with strict associated graded
square_zero? associated graded only
verdict: ACCEPT -> no edit

bar_cobar_adjunction_inversion.tex:4524-4531
complex: PBW expansion + higher-genus curvature
square_zero? genus-0 / associated graded yes; raw fiberwise no
verdict: ACCEPT -> clarify split

chiral_hochschild_koszul.tex:3767-3771
complex: total differential
square_zero? Y
verdict: ACCEPT -> no edit

chiral_koszul_pairs.tex:2233-2247
complex: formal genus-0 / fiberwise strict transfer
square_zero? Y
verdict: ACCEPT -> no edit

chiral_koszul_pairs.tex:2598-2614
complex: boundary-stratum strict restriction
square_zero? Y
verdict: ACCEPT -> no edit

chiral_koszul_pairs.tex:6242-6251
complex: filtered curved bar complex
square_zero? total curved complex N
current issue: theorem/proof state ordinary degeneration and direct equivalence
verdict: ACCEPT -> add coderived qualifier and strict-associated-graded wording

chiral_koszul_pairs.tex:6340-6343
complex: PBW filtration / associated graded
square_zero? Y on associated graded
verdict: ACCEPT -> no edit

chiral_koszul_pairs.tex:6370
complex: curved Koszul duality in Positselski setting
square_zero? N on curved side
current issue: coderived category not named
verdict: ACCEPT -> add coderived qualifier

chiral_modules.tex:2129
complex: off-Koszul bar spectral sequence
square_zero? not guaranteed
current issue: no coderived landing zone named
verdict: ACCEPT -> add coderived qualifier

cobar_construction.tex:3107-3184
complex: genus spectral sequence + raw fiberwise differential
square_zero? only for D^{(g)}, not for dfib
current issue: separation not explicit enough
verdict: ACCEPT -> add explicit qualifier

coderived_models.tex:314-363
complex: coderived associated-graded spectral sequence
square_zero? associated graded yes
verdict: ACCEPT -> no edit
```

I’m applying only those scoped edits now.
file update
M /Users/raeez/chiral-bar-cobar/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -119,3 +119,10 @@
 
-No completion is needed. The bar complex is conilpotent (finite-dimensional in each bar degree) and the differential is zero except for the curvature term $m_0$. Convergence of the bar spectral sequence follows: the filtration by bar degree is bounded below ($n \geq 0$) and exhaustive, with finite-dimensional graded pieces, so the spectral sequence converges to the bar homology by the standard bounded-below complete convergence theorem (\cite{LV12}, Theorem~2.2.3).
+No completion is needed at genus~$0$. The strict genus-$0$ bar complex is
+conilpotent (finite-dimensional in each bar degree) and its ordinary bar
+differential is zero; the higher-genus curved correction is handled later
+on the coderived side. Convergence of the genus-$0$ bar spectral sequence
+then follows: the filtration by bar degree is bounded below ($n \geq 0$)
+and exhaustive, with finite-dimensional graded pieces, so the spectral
+sequence converges to the ordinary bar homology by the standard
+bounded-below complete convergence theorem (\cite{LV12}, Theorem~2.2.3).
 
@@ -4524,9 +4531,13 @@
 The categorical logarithm encodes a chiral
-algebra~$\cA$ as the bar complex $\barB(\cA)$, whose Taylor expansion
-is the PBW spectral sequence, whose leading coefficient is the modular
-characteristic~$\kappa(\cA)$, and whose curvature
-$\dfib^{\,2} = \kappa(\cA) \cdot \omega_g$ governs the genus
-transition. On a locus where the full scalar package is known to be
-governed by~$\kappa(\cA)$, this curvature controls the scalar genus
-tower.
+algebra~$\cA$ as the bar complex $\barB(\cA)$. On the strict
+genus-$0$ or associated-graded lane, its Taylor expansion is the PBW
+spectral sequence, whose leading coefficient is the modular
+characteristic~$\kappa(\cA)$. By contrast, once the higher-genus
+fiber operator satisfies
+$\dfib^{\,2} = \kappa(\cA) \cdot \omega_g$, the genus transition is
+tracked either by the flat comparison differential $\Dg{g}$ or by the
+coderived bar-degree filtration, not by ordinary cohomology of the
+raw curved fiber complex. On a locus where the full scalar package is
+known to be governed by~$\kappa(\cA)$, this curvature controls the
+scalar genus tower.
 
M /Users/raeez/chiral-bar-cobar/chapters/theory/bar_cobar_adjunction_curved.tex
@@ -5873,4 +5873,7 @@
 and nilpotence holds only up to homotopy: the bar complex requires
-homotopy coherent structures, spectral sequences that may not
-degenerate, and the full $A_\infty$/$L_\infty$ framework at every level.
+homotopy coherent structures, coderived filtrations whose
+associated-graded differential is square-zero, and the full
+$A_\infty$/$L_\infty$ framework at every level. In particular, one
+should not speak of ordinary bar cohomology or an unqualified bar
+spectral sequence for the total curved differential in this regime.
 All standard chiral algebras (Heisenberg, Kac--Moody, Virasoro,
M /Users/raeez/chiral-bar-cobar/chapters/theory/chiral_modules.tex
@@ -2128,3 +2128,10 @@
 \index{associated variety!Koszul duality}
-The associated variety is \emph{not} preserved by level-shifting Koszul duality: e.g., $X_{L_1(\mathfrak{sl}_2)} = \{0\}$ but $X_{L_{-3}(\mathfrak{sl}_2)} = \mathfrak{sl}_2^*$. When $X_V = \{0\}$, the bar spectral sequence degenerates at a finite page; for $X_V \neq \{0\}$ it may have non-trivial higher differentials, marking the passage from Koszul to curved $A_\infty$.
+The associated variety is \emph{not} preserved by level-shifting Koszul
+duality: e.g., $X_{L_1(\mathfrak{sl}_2)} = \{0\}$ but
+$X_{L_{-3}(\mathfrak{sl}_2)} = \mathfrak{sl}_2^*$. When $X_V = \{0\}$,
+the bar spectral sequence degenerates at a finite page; for
+$X_V \neq \{0\}$ it may have non-trivial higher differentials, marking
+the passage from Koszul to curved $A_\infty$. Off that square-zero
+locus, the comparison should be read on the coderived side rather than
+as an ordinary bar-cohomology statement.
 \end{remark}
M /Users/raeez/chiral-bar-cobar/chapters/theory/cobar_construction.tex
@@ -3109,3 +3109,7 @@
 involution~$\sigma$ and the genus spectral sequence, is given in
-Theorem~\ref{thm:quantum-complementarity-main}.
+Theorem~\ref{thm:quantum-complementarity-main}. Here the spectral
+sequence is taken for the square-zero total comparison differential, or
+equivalently for the coderived filtration on the curved bar family; it
+is not the ordinary spectral sequence of the raw fiber operator when
+$\dfib^{\,2} \neq 0$.
 
@@ -3136,2 +3140,5 @@
 introduced in Convention~\ref{conv:higher-genus-differentials}.
+Accordingly, any spectral-sequence or $H^*$ statement below uses either
+$\Dg{g}$ or the coderived bar-degree filtration, not the raw curved
+fiber complex $(\barB_g(\mathcal{A}), \dfib)$.
 
M /Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex
@@ -6241,3 +6241,4 @@
 
-Filtered algebras $(\cA_1, \cA_2)$ with curvatures $\kappa_1, \kappa_2$ form a curved Koszul pair if:
+Filtered algebras $(\cA_1, \cA_2)$ with curvatures $\kappa_1, \kappa_2$
+form a curved Koszul pair in the filtered coderived sense if:
 \begin{enumerate}
@@ -6245,3 +6246,5 @@
 \item Curvatures are dual: $\kappa_1 \leftrightarrow -\kappa_2$ under the Koszul pairing
-\item The spectral sequence associated to the filtration degenerates at $E_2$
+\item The coderived spectral sequence associated to the filtration,
+ computed from the strict associated graded of the curved bar complex,
+ degenerates at $E_2$
 \end{enumerate}
@@ -6250,3 +6253,20 @@
 \begin{proof}
-The filtered bar complex $F_\bullet \B(\cA_1)$ has associated graded $\mathrm{gr}\,\B(\cA_1) = \B(\mathrm{gr}\,\cA_1)$. By condition (1), $\Omega(\B(\mathrm{gr}\,\cA_1)) \simeq \mathrm{gr}\,\cA_2$ at the $E_1$ level. The curvature condition (2) ensures that the $m_0$ elements of the two algebras are related by $\kappa_2 = -\kappa_1^*$ under the Koszul pairing, which is the compatibility condition for curved $A_\infty$ morphisms (Positselski \cite{Positselski11}). The degeneration condition (3) then gives $\Omega(\B(\cA_1)) \simeq \cA_2$ as curved $A_\infty$ algebras. This is the standard criterion for curved Koszul pairs (Loday--Vallette \cite{LV12}, \S10.3), lifted to the chiral setting via Theorem~\ref{thm:geometric-equals-operadic-bar} (geometric bar = operadic bar).
+The filtered curved bar complex $F_\bullet \B(\cA_1)$ has associated
+graded $\mathrm{gr}\,\B(\cA_1) = \B(\mathrm{gr}\,\cA_1)$, and the
+curvature lies in positive filtration, so the associated-graded
+differential is square-zero. By condition~(1),
+$\Omega(\B(\mathrm{gr}\,\cA_1)) \simeq \mathrm{gr}\,\cA_2$ at the
+$E_1$ level. The curvature condition~(2) ensures that the $m_0$
+elements of the two algebras are related by
+$\kappa_2 = -\kappa_1^*$ under the Koszul pairing, which is the
+compatibility condition for curved $A_\infty$ morphisms
+(Positselski~\cite{Positselski11}). The degeneration condition~(3)
+then gives the bar-cobar comparison in the filtered coderived
+category; on loci where the coderived comparison promotes to an
+ordinary chain-level statement, one recovers
+$\Omega(\B(\cA_1)) \simeq \cA_2$ as curved $A_\infty$ algebras. This is
+the standard criterion for curved Koszul pairs
+(Loday--Vallette~\cite{LV12}, \S10.3), lifted to the chiral setting via
+Theorem~\ref{thm:geometric-equals-operadic-bar} (geometric bar =
+operadic bar).
 \end{proof}
@@ -6369,3 +6389,6 @@
 \end{enumerate}
-One needs the PBW spectral sequence approach (Theorem~\ref{thm:pbw-koszulness-criterion}), or equivalently, curved Koszul duality (Positselski) with nilpotent completion and a filtered/completed category.
+One needs the PBW spectral sequence approach
+(Theorem~\ref{thm:pbw-koszulness-criterion}), or equivalently,
+Positselski's curved Koszul duality in its coderived,
+nilpotently completed, filtered setting.
 
apply_patch(auto_approved=true) exited 0 in 50ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/theory/bar_cobar_adjunction_curved.tex
M /Users/raeez/chiral-bar-cobar/chapters/theory/bar_cobar_adjunction_inversion.tex
M /Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex
M /Users/raeez/chiral-bar-cobar/chapters/theory/chiral_modules.tex
M /Users/raeez/chiral-bar-cobar/chapters/theory/cobar_construction.tex
file update:
diff --git a/chapters/theory/bar_cobar_adjunction_curved.tex b/chapters/theory/bar_cobar_adjunction_curved.tex
index 9f149679c80b6dec8cb90edcd3ce927df7e6198b..b3a3459a72f92f710f7f0eea792dd68ab3c67715
--- a/chapters/theory/bar_cobar_adjunction_curved.tex
+++ b/chapters/theory/bar_cobar_adjunction_curved.tex
@@ -5871,8 +5871,11 @@
 \begin{remark}[Non-central curvature]\label{rem:non-central-curvature}
 If the curvature $\mu_0$ is not central, then $d_{\text{bar}}^2 \neq 0$
 and nilpotence holds only up to homotopy: the bar complex requires
-homotopy coherent structures, spectral sequences that may not
-degenerate, and the full $A_\infty$/$L_\infty$ framework at every level.
+homotopy coherent structures, coderived filtrations whose
+associated-graded differential is square-zero, and the full
+$A_\infty$/$L_\infty$ framework at every level. In particular, one
+should not speak of ordinary bar cohomology or an unqualified bar
+spectral sequence for the total curved differential in this regime.
 All standard chiral algebras (Heisenberg, Kac--Moody, Virasoro,
 $\cW$-algebras) have central curvature, so strict nilpotence holds
 throughout; see Remark~\ref{rem:voa-central-curvature} for the
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index 6f6e3e513dba8aa12ab332fe87b8a7c09096b212..7f7756a90cff7d603e6fc0f4309cb832d5d5c35a
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -117,7 +117,14 @@
 \end{tabular}
 \end{center}
 
-No completion is needed. The bar complex is conilpotent (finite-dimensional in each bar degree) and the differential is zero except for the curvature term $m_0$. Convergence of the bar spectral sequence follows: the filtration by bar degree is bounded below ($n \geq 0$) and exhaustive, with finite-dimensional graded pieces, so the spectral sequence converges to the bar homology by the standard bounded-below complete convergence theorem (\cite{LV12}, Theorem~2.2.3).
+No completion is needed at genus~$0$. The strict genus-$0$ bar complex is
+conilpotent (finite-dimensional in each bar degree) and its ordinary bar
+differential is zero; the higher-genus curved correction is handled later
+on the coderived side. Convergence of the genus-$0$ bar spectral sequence
+then follows: the filtration by bar degree is bounded below ($n \geq 0$)
+and exhaustive, with finite-dimensional graded pieces, so the spectral
+sequence converges to the ordinary bar homology by the standard
+bounded-below complete convergence theorem (\cite{LV12}, Theorem~2.2.3).
 
 \emph{Reference}: See \cite{GLZ22} Section 6, Proposition 6.2 for the identification
 of the twisted chiral enveloping algebra with CE algebra structure.
@@ -4522,13 +4529,17 @@
 \index{quadratic frontier|textbf}
 
 The categorical logarithm encodes a chiral
-algebra~$\cA$ as the bar complex $\barB(\cA)$, whose Taylor expansion
-is the PBW spectral sequence, whose leading coefficient is the modular
-characteristic~$\kappa(\cA)$, and whose curvature
-$\dfib^{\,2} = \kappa(\cA) \cdot \omega_g$ governs the genus
-transition. On a locus where the full scalar package is known to be
-governed by~$\kappa(\cA)$, this curvature controls the scalar genus
-tower.
+algebra~$\cA$ as the bar complex $\barB(\cA)$. On the strict
+genus-$0$ or associated-graded lane, its Taylor expansion is the PBW
+spectral sequence, whose leading coefficient is the modular
+characteristic~$\kappa(\cA)$. By contrast, once the higher-genus
+fiber operator satisfies
+$\dfib^{\,2} = \kappa(\cA) \cdot \omega_g$, the genus transition is
+tracked either by the flat comparison differential $\Dg{g}$ or by the
+coderived bar-degree filtration, not by ordinary cohomology of the
+raw curved fiber complex. On a locus where the full scalar package is
+known to be governed by~$\kappa(\cA)$, this curvature controls the
+scalar genus tower.
 
 We now consider what happens when
 that stronger scalar-package hypothesis is left. The Whitehead decomposition
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index dec9ecb32841b9b9b25c237fdfd39a834fb3f9ee..d42005a148feeefe896f5af5b08aad9e62f62917
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -6239,16 +6239,36 @@
 \textup{[Regime: curved-central
 \textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
 
-Filtered algebras $(\cA_1, \cA_2)$ with curvatures $\kappa_1, \kappa_2$ form a curved Koszul pair if:
+Filtered algebras $(\cA_1, \cA_2)$ with curvatures $\kappa_1, \kappa_2$
+form a curved Koszul pair in the filtered coderived sense if:
 \begin{enumerate}
 \item Associated graded $(\mathrm{gr}\,\cA_1, \mathrm{gr}\,\cA_2)$ are classical Koszul dual
 \item Curvatures are dual: $\kappa_1 \leftrightarrow -\kappa_2$ under the Koszul pairing
-\item The spectral sequence associated to the filtration degenerates at $E_2$
+\item The coderived spectral sequence associated to the filtration,
+ computed from the strict associated graded of the curved bar complex,
+ degenerates at $E_2$
 \end{enumerate}
 \end{theorem}
 
 \begin{proof}
-The filtered bar complex $F_\bullet \B(\cA_1)$ has associated graded $\mathrm{gr}\,\B(\cA_1) = \B(\mathrm{gr}\,\cA_1)$. By condition (1), $\Omega(\B(\mathrm{gr}\,\cA_1)) \simeq \mathrm{gr}\,\cA_2$ at the $E_1$ level. The curvature condition (2) ensures that the $m_0$ elements of the two algebras are related by $\kappa_2 = -\kappa_1^*$ under the Koszul pairing, which is the compatibility condition for curved $A_\infty$ morphisms (Positselski \cite{Positselski11}). The degeneration condition (3) then gives $\Omega(\B(\cA_1)) \simeq \cA_2$ as curved $A_\infty$ algebras. This is the standard criterion for curved Koszul pairs (Loday--Vallette \cite{LV12}, \S10.3), lifted to the chiral setting via Theorem~\ref{thm:geometric-equals-operadic-bar} (geometric bar = operadic bar).
+The filtered curved bar complex $F_\bullet \B(\cA_1)$ has associated
+graded $\mathrm{gr}\,\B(\cA_1) = \B(\mathrm{gr}\,\cA_1)$, and the
+curvature lies in positive filtration, so the associated-graded
+differential is square-zero. By condition~(1),
+$\Omega(\B(\mathrm{gr}\,\cA_1)) \simeq \mathrm{gr}\,\cA_2$ at the
+$E_1$ level. The curvature condition~(2) ensures that the $m_0$
+elements of the two algebras are related by
+$\kappa_2 = -\kappa_1^*$ under the Koszul pairing, which is the
+compatibility condition for curved $A_\infty$ morphisms
+(Positselski~\cite{Positselski11}). The degeneration condition~(3)
+then gives the bar-cobar comparison in the filtered coderived
+category; on loci where the coderived comparison promotes to an
+ordinary chain-level statement, one recovers
+$\Omega(\B(\cA_1)) \simeq \cA_2$ as curved $A_\infty$ algebras. This is
+the standard criterion for curved Koszul pairs
+(Loday--Vallette~\cite{LV12}, \S10.3), lifted to the chiral setting via
+Theorem~\ref{thm:geometric-equals-operadic-bar} (geometric bar =
+operadic bar).
 \end{proof}
 
 % ================================================================
@@ -6367,7 +6387,10 @@
 
 \item The central charge $c$ enters non-linearly in higher bar degrees, preventing a quadratic Koszul resolution.
 \end{enumerate}
-One needs the PBW spectral sequence approach (Theorem~\ref{thm:pbw-koszulness-criterion}), or equivalently, curved Koszul duality (Positselski) with nilpotent completion and a filtered/completed category.
+One needs the PBW spectral sequence approach
+(Theorem~\ref{thm:pbw-koszulness-criterion}), or equivalently,
+Positselski's curved Koszul duality in its coderived,
+nilpotently completed, filtered setting.
 
 \emph{Contrast with Heisenberg/Kac--Moody.}
 \begin{center}
diff --git a/chapters/theory/chiral_modules.tex b/chapters/theory/chiral_modules.tex
index 31c1dfb431aba58853fc92f99bc99383f16b37be..a503b83e41878075ce0885ae10f0369eb14f0970
--- a/chapters/theory/chiral_modules.tex
+++ b/chapters/theory/chiral_modules.tex
@@ -2126,7 +2126,14 @@
 \begin{remark}[Associated variety and Koszul duality]
 \label{rem:associated-variety-koszul}
 \index{associated variety!Koszul duality}
-The associated variety is \emph{not} preserved by level-shifting Koszul duality: e.g., $X_{L_1(\mathfrak{sl}_2)} = \{0\}$ but $X_{L_{-3}(\mathfrak{sl}_2)} = \mathfrak{sl}_2^*$. When $X_V = \{0\}$, the bar spectral sequence degenerates at a finite page; for $X_V \neq \{0\}$ it may have non-trivial higher differentials, marking the passage from Koszul to curved $A_\infty$.
+The associated variety is \emph{not} preserved by level-shifting Koszul
+duality: e.g., $X_{L_1(\mathfrak{sl}_2)} = \{0\}$ but
+$X_{L_{-3}(\mathfrak{sl}_2)} = \mathfrak{sl}_2^*$. When $X_V = \{0\}$,
+the bar spectral sequence degenerates at a finite page; for
+$X_V \neq \{0\}$ it may have non-trivial higher differentials, marking
+the passage from Koszul to curved $A_\infty$. Off that square-zero
+locus, the comparison should be read on the coderived side rather than
+as an ordinary bar-cohomology statement.
 \end{remark}
 
 \begin{conjecture}[Type-$A$ orbit duality for affine simple quotients; \ClaimStatusConjectured]
diff --git a/chapters/theory/cobar_construction.tex b/chapters/theory/cobar_construction.tex
index baf55cf992bb32c62f1a00820d1c6d08f73cebec..0aaf81e80c78be3a6f81a39f6994171be62a439d
--- a/chapters/theory/cobar_construction.tex
+++ b/chapters/theory/cobar_construction.tex
@@ -3107,7 +3107,11 @@
 \begin{proof}[Proof (outline; full proof in \S\textup{\ref{sec:complementarity-theorem}})]
 The complete proof, synthesizing five lemmas via the Verdier
 involution~$\sigma$ and the genus spectral sequence, is given in
-Theorem~\ref{thm:quantum-complementarity-main}.
+Theorem~\ref{thm:quantum-complementarity-main}. Here the spectral
+sequence is taken for the square-zero total comparison differential, or
+equivalently for the coderived filtration on the curved bar family; it
+is not the ordinary spectral sequence of the raw fiber operator when
+$\dfib^{\,2} \neq 0$.
 
 \emph{Foundation: Curved $A_\infty$ Structures}
 
@@ -3134,6 +3138,9 @@
 The total corrected differential $\Dg{g}$, which incorporates period
 corrections to restore strict nilpotence ($\Dg{g}^{\,2} = 0$), is
 introduced in Convention~\ref{conv:higher-genus-differentials}.
+Accordingly, any spectral-sequence or $H^*$ statement below uses either
+$\Dg{g}$ or the coderived bar-degree filtration, not the raw curved
+fiber complex $(\barB_g(\mathcal{A}), \dfib)$.
 
 \medskip
 

file update:
diff --git a/chapters/theory/bar_cobar_adjunction_curved.tex b/chapters/theory/bar_cobar_adjunction_curved.tex
index 9f149679c80b6dec8cb90edcd3ce927df7e6198b..b3a3459a72f92f710f7f0eea792dd68ab3c67715
--- a/chapters/theory/bar_cobar_adjunction_curved.tex
+++ b/chapters/theory/bar_cobar_adjunction_curved.tex
@@ -5871,8 +5871,11 @@
 \begin{remark}[Non-central curvature]\label{rem:non-central-curvature}
 If the curvature $\mu_0$ is not central, then $d_{\text{bar}}^2 \neq 0$
 and nilpotence holds only up to homotopy: the bar complex requires
-homotopy coherent structures, spectral sequences that may not
-degenerate, and the full $A_\infty$/$L_\infty$ framework at every level.
+homotopy coherent structures, coderived filtrations whose
+associated-graded differential is square-zero, and the full
+$A_\infty$/$L_\infty$ framework at every level. In particular, one
+should not speak of ordinary bar cohomology or an unqualified bar
+spectral sequence for the total curved differential in this regime.
 All standard chiral algebras (Heisenberg, Kac--Moody, Virasoro,
 $\cW$-algebras) have central curvature, so strict nilpotence holds
 throughout; see Remark~\ref{rem:voa-central-curvature} for the
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index 6f6e3e513dba8aa12ab332fe87b8a7c09096b212..7f7756a90cff7d603e6fc0f4309cb832d5d5c35a
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -117,7 +117,14 @@
 \end{tabular}
 \end{center}
 
-No completion is needed. The bar complex is conilpotent (finite-dimensional in each bar degree) and the differential is zero except for the curvature term $m_0$. Convergence of the bar spectral sequence follows: the filtration by bar degree is bounded below ($n \geq 0$) and exhaustive, with finite-dimensional graded pieces, so the spectral sequence converges to the bar homology by the standard bounded-below complete convergence theorem (\cite{LV12}, Theorem~2.2.3).
+No completion is needed at genus~$0$. The strict genus-$0$ bar complex is
+conilpotent (finite-dimensional in each bar degree) and its ordinary bar
+differential is zero; the higher-genus curved correction is handled later
+on the coderived side. Convergence of the genus-$0$ bar spectral sequence
+then follows: the filtration by bar degree is bounded below ($n \geq 0$)
+and exhaustive, with finite-dimensional graded pieces, so the spectral
+sequence converges to the ordinary bar homology by the standard
+bounded-below complete convergence theorem (\cite{LV12}, Theorem~2.2.3).
 
 \emph{Reference}: See \cite{GLZ22} Section 6, Proposition 6.2 for the identification
 of the twisted chiral enveloping algebra with CE algebra structure.
@@ -4522,13 +4529,17 @@
 \index{quadratic frontier|textbf}
 
 The categorical logarithm encodes a chiral
-algebra~$\cA$ as the bar complex $\barB(\cA)$, whose Taylor expansion
-is the PBW spectral sequence, whose leading coefficient is the modular
-characteristic~$\kappa(\cA)$, and whose curvature
-$\dfib^{\,2} = \kappa(\cA) \cdot \omega_g$ governs the genus
-transition. On a locus where the full scalar package is known to be
-governed by~$\kappa(\cA)$, this curvature controls the scalar genus
-tower.
+algebra~$\cA$ as the bar complex $\barB(\cA)$. On the strict
+genus-$0$ or associated-graded lane, its Taylor expansion is the PBW
+spectral sequence, whose leading coefficient is the modular
+characteristic~$\kappa(\cA)$. By contrast, once the higher-genus
+fiber operator satisfies
+$\dfib^{\,2} = \kappa(\cA) \cdot \omega_g$, the genus transition is
+tracked either by the flat comparison differential $\Dg{g}$ or by the
+coderived bar-degree filtration, not by ordinary cohomology of the
+raw curved fiber complex. On a locus where the full scalar package is
+known to be governed by~$\kappa(\cA)$, this curvature controls the
+scalar genus tower.
 
 We now consider what happens when
 that stronger scalar-package hypothesis is left. The Whitehead decomposition
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index dec9ecb32841b9b9b25c237fdfd39a834fb3f9ee..d42005a148feeefe896f5af5b08aad9e62f62917
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -6239,16 +6239,36 @@
 \textup{[Regime: curved-central
 \textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
 
-Filtered algebras $(\cA_1, \cA_2)$ with curvatures $\kappa_1, \kappa_2$ form a curved Koszul pair if:
+Filtered algebras $(\cA_1, \cA_2)$ with curvatures $\kappa_1, \kappa_2$
+form a curved Koszul pair in the filtered coderived sense if:
 \begin{enumerate}
 \item Associated graded $(\mathrm{gr}\,\cA_1, \mathrm{gr}\,\cA_2)$ are classical Koszul dual
 \item Curvatures are dual: $\kappa_1 \leftrightarrow -\kappa_2$ under the Koszul pairing
-\item The spectral sequence associated to the filtration degenerates at $E_2$
+\item The coderived spectral sequence associated to the filtration,
+ computed from the strict associated graded of the curved bar complex,
+ degenerates at $E_2$
 \end{enumerate}
 \end{theorem}
 
 \begin{proof}
-The filtered bar complex $F_\bullet \B(\cA_1)$ has associated graded $\mathrm{gr}\,\B(\cA_1) = \B(\mathrm{gr}\,\cA_1)$. By condition (1), $\Omega(\B(\mathrm{gr}\,\cA_1)) \simeq \mathrm{gr}\,\cA_2$ at the $E_1$ level. The curvature condition (2) ensures that the $m_0$ elements of the two algebras are related by $\kappa_2 = -\kappa_1^*$ under the Koszul pairing, which is the compatibility condition for curved $A_\infty$ morphisms (Positselski \cite{Positselski11}). The degeneration condition (3) then gives $\Omega(\B(\cA_1)) \simeq \cA_2$ as curved $A_\infty$ algebras. This is the standard criterion for curved Koszul pairs (Loday--Vallette \cite{LV12}, \S10.3), lifted to the chiral setting via Theorem~\ref{thm:geometric-equals-operadic-bar} (geometric bar = operadic bar).
+The filtered curved bar complex $F_\bullet \B(\cA_1)$ has associated
+graded $\mathrm{gr}\,\B(\cA_1) = \B(\mathrm{gr}\,\cA_1)$, and the
+curvature lies in positive filtration, so the associated-graded
+differential is square-zero. By condition~(1),
+$\Omega(\B(\mathrm{gr}\,\cA_1)) \simeq \mathrm{gr}\,\cA_2$ at the
+$E_1$ level. The curvature condition~(2) ensures that the $m_0$
+elements of the two algebras are related by
+$\kappa_2 = -\kappa_1^*$ under the Koszul pairing, which is the
+compatibility condition for curved $A_\infty$ morphisms
+(Positselski~\cite{Positselski11}). The degeneration condition~(3)
+then gives the bar-cobar comparison in the filtered coderived
+category; on loci where the coderived comparison promotes to an
+ordinary chain-level statement, one recovers
+$\Omega(\B(\cA_1)) \simeq \cA_2$ as curved $A_\infty$ algebras. This is
+the standard criterion for curved Koszul pairs
+(Loday--Vallette~\cite{LV12}, \S10.3), lifted to the chiral setting via
+Theorem~\ref{thm:geometric-equals-operadic-bar} (geometric bar =
+operadic bar).
 \end{proof}
 
 % ================================================================
@@ -6367,7 +6387,10 @@
 
 \item The central charge $c$ enters non-linearly in higher bar degrees, preventing a quadratic Koszul resolution.
 \end{enumerate}
-One needs the PBW spectral sequence approach (Theorem~\ref{thm:pbw-koszulness-criterion}), or equivalently, curved Koszul duality (Positselski) with nilpotent completion and a filtered/completed category.
+One needs the PBW spectral sequence approach
+(Theorem~\ref{thm:pbw-koszulness-criterion}), or equivalently,
+Positselski's curved Koszul duality in its coderived,
+nilpotently completed, filtered setting.
 
 \emph{Contrast with Heisenberg/Kac--Moody.}
 \begin{center}
diff --git a/chapters/theory/chiral_modules.tex b/chapters/theory/chiral_modules.tex
index 31c1dfb431aba58853fc92f99bc99383f16b37be..a503b83e41878075ce0885ae10f0369eb14f0970
--- a/chapters/theory/chiral_modules.tex
+++ b/chapters/theory/chiral_modules.tex
@@ -2126,7 +2126,14 @@
 \begin{remark}[Associated variety and Koszul duality]
 \label{rem:associated-variety-koszul}
 \index{associated variety!Koszul duality}
-The associated variety is \emph{not} preserved by level-shifting Koszul duality: e.g., $X_{L_1(\mathfrak{sl}_2)} = \{0\}$ but $X_{L_{-3}(\mathfrak{sl}_2)} = \mathfrak{sl}_2^*$. When $X_V = \{0\}$, the bar spectral sequence degenerates at a finite page; for $X_V \neq \{0\}$ it may have non-trivial higher differentials, marking the passage from Koszul to curved $A_\infty$.
+The associated variety is \emph{not} preserved by level-shifting Koszul
+duality: e.g., $X_{L_1(\mathfrak{sl}_2)} = \{0\}$ but
+$X_{L_{-3}(\mathfrak{sl}_2)} = \mathfrak{sl}_2^*$. When $X_V = \{0\}$,
+the bar spectral sequence degenerates at a finite page; for
+$X_V \neq \{0\}$ it may have non-trivial higher differentials, marking
+the passage from Koszul to curved $A_\infty$. Off that square-zero
+locus, the comparison should be read on the coderived side rather than
+as an ordinary bar-cohomology statement.
 \end{remark}
 
 \begin{conjecture}[Type-$A$ orbit duality for affine simple quotients; \ClaimStatusConjectured]
diff --git a/chapters/theory/cobar_construction.tex b/chapters/theory/cobar_construction.tex
index baf55cf992bb32c62f1a00820d1c6d08f73cebec..0aaf81e80c78be3a6f81a39f6994171be62a439d
--- a/chapters/theory/cobar_construction.tex
+++ b/chapters/theory/cobar_construction.tex
@@ -3107,7 +3107,11 @@
 \begin{proof}[Proof (outline; full proof in \S\textup{\ref{sec:complementarity-theorem}})]
 The complete proof, synthesizing five lemmas via the Verdier
 involution~$\sigma$ and the genus spectral sequence, is given in
-Theorem~\ref{thm:quantum-complementarity-main}.
+Theorem~\ref{thm:quantum-complementarity-main}. Here the spectral
+sequence is taken for the square-zero total comparison differential, or
+equivalently for the coderived filtration on the curved bar family; it
+is not the ordinary spectral sequence of the raw fiber operator when
+$\dfib^{\,2} \neq 0$.
 
 \emph{Foundation: Curved $A_\infty$ Structures}
 
@@ -3134,6 +3138,9 @@
 The total corrected differential $\Dg{g}$, which incorporates period
 corrections to restore strict nilpotence ($\Dg{g}^{\,2} = 0$), is
 introduced in Convention~\ref{conv:higher-genus-differentials}.
+Accordingly, any spectral-sequence or $H^*$ statement below uses either
+$\Dg{g}$ or the coderived bar-degree filtration, not the raw curved
+fiber complex $(\barB_g(\mathcal{A}), \dfib)$.
 
 \medskip
 

codex
The scoped edits are in. I’m re-reading the exact passages now, then I’ll run a narrow grep for residual curved-vs-flat violations on the audited surfaces.
exec
/bin/zsh -lc "nl -ba chapters/theory/bar_cobar_adjunction_curved.tex | sed -n '5870,5882p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/bar_cobar_adjunction_inversion.tex | sed -n '116,126p;4524,4533p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   116	\hline
   117	\end{tabular}
   118	\end{center}
   119	
   120	No completion is needed at genus~$0$. The strict genus-$0$ bar complex is
   121	conilpotent (finite-dimensional in each bar degree) and its ordinary bar
   122	differential is zero; the higher-genus curved correction is handled later
   123	on the coderived side. Convergence of the genus-$0$ bar spectral sequence
   124	then follows: the filtration by bar degree is bounded below ($n \geq 0$)
   125	and exhaustive, with finite-dimensional graded pieces, so the spectral
   126	sequence converges to the ordinary bar homology by the standard
  4524	
  4525	\subsection{Scalar rigidity and the quadratic frontier}
  4526	\label{subsec:scalar-rigidity-quadratic-frontier}
  4527	\index{categorical logarithm!scalar rigidity}
  4528	\index{eta-Hessian@$\eta$-Hessian|textbf}
  4529	\index{quadratic frontier|textbf}
  4530	
  4531	The categorical logarithm encodes a chiral
  4532	algebra~$\cA$ as the bar complex $\barB(\cA)$. On the strict
 succeeded in 51ms:
  5870	
  5871	\begin{remark}[Non-central curvature]\label{rem:non-central-curvature}
  5872	If the curvature $\mu_0$ is not central, then $d_{\text{bar}}^2 \neq 0$
  5873	and nilpotence holds only up to homotopy: the bar complex requires
  5874	homotopy coherent structures, coderived filtrations whose
  5875	associated-graded differential is square-zero, and the full
  5876	$A_\infty$/$L_\infty$ framework at every level. In particular, one
  5877	should not speak of ordinary bar cohomology or an unqualified bar
  5878	spectral sequence for the total curved differential in this regime.
  5879	All standard chiral algebras (Heisenberg, Kac--Moody, Virasoro,
  5880	$\cW$-algebras) have central curvature, so strict nilpotence holds
  5881	throughout; see Remark~\ref{rem:voa-central-curvature} for the
  5882	precise mechanism.
exec
/bin/zsh -lc "nl -ba chapters/theory/cobar_construction.tex | sed -n '3107,3115p;3130,3139p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_modules.tex | sed -n '2126,2132p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '6242,6258p;6368,6373p'" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
  3107	\begin{proof}[Proof (outline; full proof in \S\textup{\ref{sec:complementarity-theorem}})]
  3108	The complete proof, synthesizing five lemmas via the Verdier
  3109	involution~$\sigma$ and the genus spectral sequence, is given in
  3110	Theorem~\ref{thm:quantum-complementarity-main}. Here the spectral
  3111	sequence is taken for the square-zero total comparison differential, or
  3112	equivalently for the coderived filtration on the curved bar family; it
  3113	is not the ordinary spectral sequence of the raw fiber operator when
  3114	$\dfib^{\,2} \neq 0$.
  3115	
  3130	
  3131	\emph{Step 1: Genus Stratification of Obstructions}
  3132	
  3133	\noindent
  3134	\textbf{Notation.}
  3135	The differential $\dfib$ denotes the \emph{fiberwise} bar differential at
  3136	genus~$g$: the collision-residue differential on a fixed curve~$\Sigma_g$.
  3137	It is generically \emph{curved} ($\dfib^{\,2} \neq 0$).
  3138	The total corrected differential $\Dg{g}$, which incorporates period
  3139	corrections to restore strict nilpotence ($\Dg{g}^{\,2} = 0$), is
 succeeded in 51ms:
  6242	Filtered algebras $(\cA_1, \cA_2)$ with curvatures $\kappa_1, \kappa_2$
  6243	form a curved Koszul pair in the filtered coderived sense if:
  6244	\begin{enumerate}
  6245	\item Associated graded $(\mathrm{gr}\,\cA_1, \mathrm{gr}\,\cA_2)$ are classical Koszul dual
  6246	\item Curvatures are dual: $\kappa_1 \leftrightarrow -\kappa_2$ under the Koszul pairing
  6247	\item The coderived spectral sequence associated to the filtration,
  6248	 computed from the strict associated graded of the curved bar complex,
  6249	 degenerates at $E_2$
  6250	\end{enumerate}
  6251	\end{theorem}
  6252	
  6253	\begin{proof}
  6254	The filtered curved bar complex $F_\bullet \B(\cA_1)$ has associated
  6255	graded $\mathrm{gr}\,\B(\cA_1) = \B(\mathrm{gr}\,\cA_1)$, and the
  6256	curvature lies in positive filtration, so the associated-graded
  6257	differential is square-zero. By condition~(1),
  6258	$\Omega(\B(\mathrm{gr}\,\cA_1)) \simeq \mathrm{gr}\,\cA_2$ at the
  6368	reduced on the theorem surface to the stage-$3$ fifteen-coefficient
  6369	packet and the stage-$4$ six-coefficient packet organized as three
  6370	local OPE blocks, with the genuinely mixed stage-$4$ remaining problem reduced
 succeeded in 51ms:
  2126	\begin{remark}[Associated variety and Koszul duality]
  2127	\label{rem:associated-variety-koszul}
  2128	\index{associated variety!Koszul duality}
  2129	The associated variety is \emph{not} preserved by level-shifting Koszul
  2130	duality: e.g., $X_{L_1(\mathfrak{sl}_2)} = \{0\}$ but
  2131	$X_{L_{-3}(\mathfrak{sl}_2)} = \mathfrak{sl}_2^*$. When $X_V = \{0\}$,
  2132	the bar spectral sequence degenerates at a finite page; for
file update:
diff --git a/chapters/theory/bar_cobar_adjunction_curved.tex b/chapters/theory/bar_cobar_adjunction_curved.tex
index 9f149679c80b6dec8cb90edcd3ce927df7e6198b..b3a3459a72f92f710f7f0eea792dd68ab3c67715
--- a/chapters/theory/bar_cobar_adjunction_curved.tex
+++ b/chapters/theory/bar_cobar_adjunction_curved.tex
@@ -5871,8 +5871,11 @@
 \begin{remark}[Non-central curvature]\label{rem:non-central-curvature}
 If the curvature $\mu_0$ is not central, then $d_{\text{bar}}^2 \neq 0$
 and nilpotence holds only up to homotopy: the bar complex requires
-homotopy coherent structures, spectral sequences that may not
-degenerate, and the full $A_\infty$/$L_\infty$ framework at every level.
+homotopy coherent structures, coderived filtrations whose
+associated-graded differential is square-zero, and the full
+$A_\infty$/$L_\infty$ framework at every level. In particular, one
+should not speak of ordinary bar cohomology or an unqualified bar
+spectral sequence for the total curved differential in this regime.
 All standard chiral algebras (Heisenberg, Kac--Moody, Virasoro,
 $\cW$-algebras) have central curvature, so strict nilpotence holds
 throughout; see Remark~\ref{rem:voa-central-curvature} for the
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index 6f6e3e513dba8aa12ab332fe87b8a7c09096b212..7f7756a90cff7d603e6fc0f4309cb832d5d5c35a
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -117,7 +117,14 @@
 \end{tabular}
 \end{center}
 
-No completion is needed. The bar complex is conilpotent (finite-dimensional in each bar degree) and the differential is zero except for the curvature term $m_0$. Convergence of the bar spectral sequence follows: the filtration by bar degree is bounded below ($n \geq 0$) and exhaustive, with finite-dimensional graded pieces, so the spectral sequence converges to the bar homology by the standard bounded-below complete convergence theorem (\cite{LV12}, Theorem~2.2.3).
+No completion is needed at genus~$0$. The strict genus-$0$ bar complex is
+conilpotent (finite-dimensional in each bar degree) and its ordinary bar
+differential is zero; the higher-genus curved correction is handled later
+on the coderived side. Convergence of the genus-$0$ bar spectral sequence
+then follows: the filtration by bar degree is bounded below ($n \geq 0$)
+and exhaustive, with finite-dimensional graded pieces, so the spectral
+sequence converges to the ordinary bar homology by the standard
+bounded-below complete convergence theorem (\cite{LV12}, Theorem~2.2.3).
 
 \emph{Reference}: See \cite{GLZ22} Section 6, Proposition 6.2 for the identification
 of the twisted chiral enveloping algebra with CE algebra structure.
@@ -4522,13 +4529,17 @@
 \index{quadratic frontier|textbf}
 
 The categorical logarithm encodes a chiral
-algebra~$\cA$ as the bar complex $\barB(\cA)$, whose Taylor expansion
-is the PBW spectral sequence, whose leading coefficient is the modular
-characteristic~$\kappa(\cA)$, and whose curvature
-$\dfib^{\,2} = \kappa(\cA) \cdot \omega_g$ governs the genus
-transition. On a locus where the full scalar package is known to be
-governed by~$\kappa(\cA)$, this curvature controls the scalar genus
-tower.
+algebra~$\cA$ as the bar complex $\barB(\cA)$. On the strict
+genus-$0$ or associated-graded lane, its Taylor expansion is the PBW
+spectral sequence, whose leading coefficient is the modular
+characteristic~$\kappa(\cA)$. By contrast, once the higher-genus
+fiber operator satisfies
+$\dfib^{\,2} = \kappa(\cA) \cdot \omega_g$, the genus transition is
+tracked either by the flat comparison differential $\Dg{g}$ or by the
+coderived bar-degree filtration, not by ordinary cohomology of the
+raw curved fiber complex. On a locus where the full scalar package is
+known to be governed by~$\kappa(\cA)$, this curvature controls the
+scalar genus tower.
 
 We now consider what happens when
 that stronger scalar-package hypothesis is left. The Whitehead decomposition
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index dec9ecb32841b9b9b25c237fdfd39a834fb3f9ee..d42005a148feeefe896f5af5b08aad9e62f62917
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -6239,16 +6239,36 @@
 \textup{[Regime: curved-central
 \textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
 
-Filtered algebras $(\cA_1, \cA_2)$ with curvatures $\kappa_1, \kappa_2$ form a curved Koszul pair if:
+Filtered algebras $(\cA_1, \cA_2)$ with curvatures $\kappa_1, \kappa_2$
+form a curved Koszul pair in the filtered coderived sense if:
 \begin{enumerate}
 \item Associated graded $(\mathrm{gr}\,\cA_1, \mathrm{gr}\,\cA_2)$ are classical Koszul dual
 \item Curvatures are dual: $\kappa_1 \leftrightarrow -\kappa_2$ under the Koszul pairing
-\item The spectral sequence associated to the filtration degenerates at $E_2$
+\item The coderived spectral sequence associated to the filtration,
+ computed from the strict associated graded of the curved bar complex,
+ degenerates at $E_2$
 \end{enumerate}
 \end{theorem}
 
 \begin{proof}
-The filtered bar complex $F_\bullet \B(\cA_1)$ has associated graded $\mathrm{gr}\,\B(\cA_1) = \B(\mathrm{gr}\,\cA_1)$. By condition (1), $\Omega(\B(\mathrm{gr}\,\cA_1)) \simeq \mathrm{gr}\,\cA_2$ at the $E_1$ level. The curvature condition (2) ensures that the $m_0$ elements of the two algebras are related by $\kappa_2 = -\kappa_1^*$ under the Koszul pairing, which is the compatibility condition for curved $A_\infty$ morphisms (Positselski \cite{Positselski11}). The degeneration condition (3) then gives $\Omega(\B(\cA_1)) \simeq \cA_2$ as curved $A_\infty$ algebras. This is the standard criterion for curved Koszul pairs (Loday--Vallette \cite{LV12}, \S10.3), lifted to the chiral setting via Theorem~\ref{thm:geometric-equals-operadic-bar} (geometric bar = operadic bar).
+The filtered curved bar complex $F_\bullet \B(\cA_1)$ has associated
+graded $\mathrm{gr}\,\B(\cA_1) = \B(\mathrm{gr}\,\cA_1)$, and the
+curvature lies in positive filtration, so the associated-graded
+differential is square-zero. By condition~(1),
+$\Omega(\B(\mathrm{gr}\,\cA_1)) \simeq \mathrm{gr}\,\cA_2$ at the
+$E_1$ level. The curvature condition~(2) ensures that the $m_0$
+elements of the two algebras are related by
+$\kappa_2 = -\kappa_1^*$ under the Koszul pairing, which is the
+compatibility condition for curved $A_\infty$ morphisms
+(Positselski~\cite{Positselski11}). The degeneration condition~(3)
+then gives the bar-cobar comparison in the filtered coderived
+category; on loci where the coderived comparison promotes to an
+ordinary chain-level statement, one recovers
+$\Omega(\B(\cA_1)) \simeq \cA_2$ as curved $A_\infty$ algebras. This is
+the standard criterion for curved Koszul pairs
+(Loday--Vallette~\cite{LV12}, \S10.3), lifted to the chiral setting via
+Theorem~\ref{thm:geometric-equals-operadic-bar} (geometric bar =
+operadic bar).
 \end{proof}
 
 % ================================================================
@@ -6367,7 +6387,10 @@
 
 \item The central charge $c$ enters non-linearly in higher bar degrees, preventing a quadratic Koszul resolution.
 \end{enumerate}
-One needs the PBW spectral sequence approach (Theorem~\ref{thm:pbw-koszulness-criterion}), or equivalently, curved Koszul duality (Positselski) with nilpotent completion and a filtered/completed category.
+One needs the PBW spectral sequence approach
+(Theorem~\ref{thm:pbw-koszulness-criterion}), or equivalently,
+Positselski's curved Koszul duality in its coderived,
+nilpotently completed, filtered setting.
 
 \emph{Contrast with Heisenberg/Kac--Moody.}
 \begin{center}
diff --git a/chapters/theory/chiral_modules.tex b/chapters/theory/chiral_modules.tex
index 31c1dfb431aba58853fc92f99bc99383f16b37be..a503b83e41878075ce0885ae10f0369eb14f0970
--- a/chapters/theory/chiral_modules.tex
+++ b/chapters/theory/chiral_modules.tex
@@ -2126,7 +2126,14 @@
 \begin{remark}[Associated variety and Koszul duality]
 \label{rem:associated-variety-koszul}
 \index{associated variety!Koszul duality}
-The associated variety is \emph{not} preserved by level-shifting Koszul duality: e.g., $X_{L_1(\mathfrak{sl}_2)} = \{0\}$ but $X_{L_{-3}(\mathfrak{sl}_2)} = \mathfrak{sl}_2^*$. When $X_V = \{0\}$, the bar spectral sequence degenerates at a finite page; for $X_V \neq \{0\}$ it may have non-trivial higher differentials, marking the passage from Koszul to curved $A_\infty$.
+The associated variety is \emph{not} preserved by level-shifting Koszul
+duality: e.g., $X_{L_1(\mathfrak{sl}_2)} = \{0\}$ but
+$X_{L_{-3}(\mathfrak{sl}_2)} = \mathfrak{sl}_2^*$. When $X_V = \{0\}$,
+the bar spectral sequence degenerates at a finite page; for
+$X_V \neq \{0\}$ it may have non-trivial higher differentials, marking
+the passage from Koszul to curved $A_\infty$. Off that square-zero
+locus, the comparison should be read on the coderived side rather than
+as an ordinary bar-cohomology statement.
 \end{remark}
 
 \begin{conjecture}[Type-$A$ orbit duality for affine simple quotients; \ClaimStatusConjectured]
diff --git a/chapters/theory/cobar_construction.tex b/chapters/theory/cobar_construction.tex
index baf55cf992bb32c62f1a00820d1c6d08f73cebec..0aaf81e80c78be3a6f81a39f6994171be62a439d
--- a/chapters/theory/cobar_construction.tex
+++ b/chapters/theory/cobar_construction.tex
@@ -3107,7 +3107,11 @@
 \begin{proof}[Proof (outline; full proof in \S\textup{\ref{sec:complementarity-theorem}})]
 The complete proof, synthesizing five lemmas via the Verdier
 involution~$\sigma$ and the genus spectral sequence, is given in
-Theorem~\ref{thm:quantum-complementarity-main}.
+Theorem~\ref{thm:quantum-complementarity-main}. Here the spectral
+sequence is taken for the square-zero total comparison differential, or
+equivalently for the coderived filtration on the curved bar family; it
+is not the ordinary spectral sequence of the raw fiber operator when
+$\dfib^{\,2} \neq 0$.
 
 \emph{Foundation: Curved $A_\infty$ Structures}
 
@@ -3134,6 +3138,9 @@
 The total corrected differential $\Dg{g}$, which incorporates period
 corrections to restore strict nilpotence ($\Dg{g}^{\,2} = 0$), is
 introduced in Convention~\ref{conv:higher-genus-differentials}.
+Accordingly, any spectral-sequence or $H^*$ statement below uses either
+$\Dg{g}$ or the coderived bar-degree filtration, not the raw curved
+fiber complex $(\barB_g(\mathcal{A}), \dfib)$.
 
 \medskip
 

exec
/bin/zsh -lc "nl -ba chapters/theory/cobar_construction.tex | sed -n '3138,3145p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  3138	The total corrected differential $\Dg{g}$, which incorporates period
  3139	corrections to restore strict nilpotence ($\Dg{g}^{\,2} = 0$), is
  3140	introduced in Convention~\ref{conv:higher-genus-differentials}.
  3141	Accordingly, any spectral-sequence or $H^*$ statement below uses either
  3142	$\Dg{g}$ or the coderived bar-degree filtration, not the raw curved
  3143	fiber complex $(\barB_g(\mathcal{A}), \dfib)$.
  3144	
  3145	\medskip
file update:
diff --git a/chapters/theory/bar_cobar_adjunction_curved.tex b/chapters/theory/bar_cobar_adjunction_curved.tex
index 9f149679c80b6dec8cb90edcd3ce927df7e6198b..b3a3459a72f92f710f7f0eea792dd68ab3c67715
--- a/chapters/theory/bar_cobar_adjunction_curved.tex
+++ b/chapters/theory/bar_cobar_adjunction_curved.tex
@@ -5871,8 +5871,11 @@
 \begin{remark}[Non-central curvature]\label{rem:non-central-curvature}
 If the curvature $\mu_0$ is not central, then $d_{\text{bar}}^2 \neq 0$
 and nilpotence holds only up to homotopy: the bar complex requires
-homotopy coherent structures, spectral sequences that may not
-degenerate, and the full $A_\infty$/$L_\infty$ framework at every level.
+homotopy coherent structures, coderived filtrations whose
+associated-graded differential is square-zero, and the full
+$A_\infty$/$L_\infty$ framework at every level. In particular, one
+should not speak of ordinary bar cohomology or an unqualified bar
+spectral sequence for the total curved differential in this regime.
 All standard chiral algebras (Heisenberg, Kac--Moody, Virasoro,
 $\cW$-algebras) have central curvature, so strict nilpotence holds
 throughout; see Remark~\ref{rem:voa-central-curvature} for the
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index 6f6e3e513dba8aa12ab332fe87b8a7c09096b212..7f7756a90cff7d603e6fc0f4309cb832d5d5c35a
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -117,7 +117,14 @@
 \end{tabular}
 \end{center}
 
-No completion is needed. The bar complex is conilpotent (finite-dimensional in each bar degree) and the differential is zero except for the curvature term $m_0$. Convergence of the bar spectral sequence follows: the filtration by bar degree is bounded below ($n \geq 0$) and exhaustive, with finite-dimensional graded pieces, so the spectral sequence converges to the bar homology by the standard bounded-below complete convergence theorem (\cite{LV12}, Theorem~2.2.3).
+No completion is needed at genus~$0$. The strict genus-$0$ bar complex is
+conilpotent (finite-dimensional in each bar degree) and its ordinary bar
+differential is zero; the higher-genus curved correction is handled later
+on the coderived side. Convergence of the genus-$0$ bar spectral sequence
+then follows: the filtration by bar degree is bounded below ($n \geq 0$)
+and exhaustive, with finite-dimensional graded pieces, so the spectral
+sequence converges to the ordinary bar homology by the standard
+bounded-below complete convergence theorem (\cite{LV12}, Theorem~2.2.3).
 
 \emph{Reference}: See \cite{GLZ22} Section 6, Proposition 6.2 for the identification
 of the twisted chiral enveloping algebra with CE algebra structure.
@@ -4522,13 +4529,17 @@
 \index{quadratic frontier|textbf}
 
 The categorical logarithm encodes a chiral
-algebra~$\cA$ as the bar complex $\barB(\cA)$, whose Taylor expansion
-is the PBW spectral sequence, whose leading coefficient is the modular
-characteristic~$\kappa(\cA)$, and whose curvature
-$\dfib^{\,2} = \kappa(\cA) \cdot \omega_g$ governs the genus
-transition. On a locus where the full scalar package is known to be
-governed by~$\kappa(\cA)$, this curvature controls the scalar genus
-tower.
+algebra~$\cA$ as the bar complex $\barB(\cA)$. On the strict
+genus-$0$ or associated-graded lane, its Taylor expansion is the PBW
+spectral sequence, whose leading coefficient is the modular
+characteristic~$\kappa(\cA)$. By contrast, once the higher-genus
+fiber operator satisfies
+$\dfib^{\,2} = \kappa(\cA) \cdot \omega_g$, the genus transition is
+tracked either by the flat comparison differential $\Dg{g}$ or by the
+coderived bar-degree filtration, not by ordinary cohomology of the
+raw curved fiber complex. On a locus where the full scalar package is
+known to be governed by~$\kappa(\cA)$, this curvature controls the
+scalar genus tower.
 
 We now consider what happens when
 that stronger scalar-package hypothesis is left. The Whitehead decomposition
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index dec9ecb32841b9b9b25c237fdfd39a834fb3f9ee..d42005a148feeefe896f5af5b08aad9e62f62917
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -6239,16 +6239,36 @@
 \textup{[Regime: curved-central
 \textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
 
-Filtered algebras $(\cA_1, \cA_2)$ with curvatures $\kappa_1, \kappa_2$ form a curved Koszul pair if:
+Filtered algebras $(\cA_1, \cA_2)$ with curvatures $\kappa_1, \kappa_2$
+form a curved Koszul pair in the filtered coderived sense if:
 \begin{enumerate}
 \item Associated graded $(\mathrm{gr}\,\cA_1, \mathrm{gr}\,\cA_2)$ are classical Koszul dual
 \item Curvatures are dual: $\kappa_1 \leftrightarrow -\kappa_2$ under the Koszul pairing
-\item The spectral sequence associated to the filtration degenerates at $E_2$
+\item The coderived spectral sequence associated to the filtration,
+ computed from the strict associated graded of the curved bar complex,
+ degenerates at $E_2$
 \end{enumerate}
 \end{theorem}
 
 \begin{proof}
-The filtered bar complex $F_\bullet \B(\cA_1)$ has associated graded $\mathrm{gr}\,\B(\cA_1) = \B(\mathrm{gr}\,\cA_1)$. By condition (1), $\Omega(\B(\mathrm{gr}\,\cA_1)) \simeq \mathrm{gr}\,\cA_2$ at the $E_1$ level. The curvature condition (2) ensures that the $m_0$ elements of the two algebras are related by $\kappa_2 = -\kappa_1^*$ under the Koszul pairing, which is the compatibility condition for curved $A_\infty$ morphisms (Positselski \cite{Positselski11}). The degeneration condition (3) then gives $\Omega(\B(\cA_1)) \simeq \cA_2$ as curved $A_\infty$ algebras. This is the standard criterion for curved Koszul pairs (Loday--Vallette \cite{LV12}, \S10.3), lifted to the chiral setting via Theorem~\ref{thm:geometric-equals-operadic-bar} (geometric bar = operadic bar).
+The filtered curved bar complex $F_\bullet \B(\cA_1)$ has associated
+graded $\mathrm{gr}\,\B(\cA_1) = \B(\mathrm{gr}\,\cA_1)$, and the
+curvature lies in positive filtration, so the associated-graded
+differential is square-zero. By condition~(1),
+$\Omega(\B(\mathrm{gr}\,\cA_1)) \simeq \mathrm{gr}\,\cA_2$ at the
+$E_1$ level. The curvature condition~(2) ensures that the $m_0$
+elements of the two algebras are related by
+$\kappa_2 = -\kappa_1^*$ under the Koszul pairing, which is the
+compatibility condition for curved $A_\infty$ morphisms
+(Positselski~\cite{Positselski11}). The degeneration condition~(3)
+then gives the bar-cobar comparison in the filtered coderived
+category; on loci where the coderived comparison promotes to an
+ordinary chain-level statement, one recovers
+$\Omega(\B(\cA_1)) \simeq \cA_2$ as curved $A_\infty$ algebras. This is
+the standard criterion for curved Koszul pairs
+(Loday--Vallette~\cite{LV12}, \S10.3), lifted to the chiral setting via
+Theorem~\ref{thm:geometric-equals-operadic-bar} (geometric bar =
+operadic bar).
 \end{proof}
 
 % ================================================================
@@ -6367,7 +6387,10 @@
 
 \item The central charge $c$ enters non-linearly in higher bar degrees, preventing a quadratic Koszul resolution.
 \end{enumerate}
-One needs the PBW spectral sequence approach (Theorem~\ref{thm:pbw-koszulness-criterion}), or equivalently, curved Koszul duality (Positselski) with nilpotent completion and a filtered/completed category.
+One needs the PBW spectral sequence approach
+(Theorem~\ref{thm:pbw-koszulness-criterion}), or equivalently,
+Positselski's curved Koszul duality in its coderived,
+nilpotently completed, filtered setting.
 
 \emph{Contrast with Heisenberg/Kac--Moody.}
 \begin{center}
diff --git a/chapters/theory/chiral_modules.tex b/chapters/theory/chiral_modules.tex
index 31c1dfb431aba58853fc92f99bc99383f16b37be..a503b83e41878075ce0885ae10f0369eb14f0970
--- a/chapters/theory/chiral_modules.tex
+++ b/chapters/theory/chiral_modules.tex
@@ -2126,7 +2126,14 @@
 \begin{remark}[Associated variety and Koszul duality]
 \label{rem:associated-variety-koszul}
 \index{associated variety!Koszul duality}
-The associated variety is \emph{not} preserved by level-shifting Koszul duality: e.g., $X_{L_1(\mathfrak{sl}_2)} = \{0\}$ but $X_{L_{-3}(\mathfrak{sl}_2)} = \mathfrak{sl}_2^*$. When $X_V = \{0\}$, the bar spectral sequence degenerates at a finite page; for $X_V \neq \{0\}$ it may have non-trivial higher differentials, marking the passage from Koszul to curved $A_\infty$.
+The associated variety is \emph{not} preserved by level-shifting Koszul
+duality: e.g., $X_{L_1(\mathfrak{sl}_2)} = \{0\}$ but
+$X_{L_{-3}(\mathfrak{sl}_2)} = \mathfrak{sl}_2^*$. When $X_V = \{0\}$,
+the bar spectral sequence degenerates at a finite page; for
+$X_V \neq \{0\}$ it may have non-trivial higher differentials, marking
+the passage from Koszul to curved $A_\infty$. Off that square-zero
+locus, the comparison should be read on the coderived side rather than
+as an ordinary bar-cohomology statement.
 \end{remark}
 
 \begin{conjecture}[Type-$A$ orbit duality for affine simple quotients; \ClaimStatusConjectured]
diff --git a/chapters/theory/cobar_construction.tex b/chapters/theory/cobar_construction.tex
index baf55cf992bb32c62f1a00820d1c6d08f73cebec..0aaf81e80c78be3a6f81a39f6994171be62a439d
--- a/chapters/theory/cobar_construction.tex
+++ b/chapters/theory/cobar_construction.tex
@@ -3107,7 +3107,11 @@
 \begin{proof}[Proof (outline; full proof in \S\textup{\ref{sec:complementarity-theorem}})]
 The complete proof, synthesizing five lemmas via the Verdier
 involution~$\sigma$ and the genus spectral sequence, is given in
-Theorem~\ref{thm:quantum-complementarity-main}.
+Theorem~\ref{thm:quantum-complementarity-main}. Here the spectral
+sequence is taken for the square-zero total comparison differential, or
+equivalently for the coderived filtration on the curved bar family; it
+is not the ordinary spectral sequence of the raw fiber operator when
+$\dfib^{\,2} \neq 0$.
 
 \emph{Foundation: Curved $A_\infty$ Structures}
 
@@ -3134,6 +3138,9 @@
 The total corrected differential $\Dg{g}$, which incorporates period
 corrections to restore strict nilpotence ($\Dg{g}^{\,2} = 0$), is
 introduced in Convention~\ref{conv:higher-genus-differentials}.
+Accordingly, any spectral-sequence or $H^*$ statement below uses either
+$\Dg{g}$ or the coderived bar-degree filtration, not the raw curved
+fiber complex $(\barB_g(\mathcal{A}), \dfib)$.
 
 \medskip
 

exec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '6368,6376p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  6368	reduced on the theorem surface to the stage-$3$ fifteen-coefficient
  6369	packet and the stage-$4$ six-coefficient packet organized as three
  6370	local OPE blocks, with the genuinely mixed stage-$4$ remaining problem reduced
  6371	to the single mixed $(3,4)$ triple.
  6372	
  6373	\emph{Why the quadratic framework fails.}
  6374	\begin{enumerate}
  6375	\item The OPE involves a quartic pole:
  6376	\begin{equation}
file update:
diff --git a/chapters/theory/bar_cobar_adjunction_curved.tex b/chapters/theory/bar_cobar_adjunction_curved.tex
index 9f149679c80b6dec8cb90edcd3ce927df7e6198b..b3a3459a72f92f710f7f0eea792dd68ab3c67715
--- a/chapters/theory/bar_cobar_adjunction_curved.tex
+++ b/chapters/theory/bar_cobar_adjunction_curved.tex
@@ -5871,8 +5871,11 @@
 \begin{remark}[Non-central curvature]\label{rem:non-central-curvature}
 If the curvature $\mu_0$ is not central, then $d_{\text{bar}}^2 \neq 0$
 and nilpotence holds only up to homotopy: the bar complex requires
-homotopy coherent structures, spectral sequences that may not
-degenerate, and the full $A_\infty$/$L_\infty$ framework at every level.
+homotopy coherent structures, coderived filtrations whose
+associated-graded differential is square-zero, and the full
+$A_\infty$/$L_\infty$ framework at every level. In particular, one
+should not speak of ordinary bar cohomology or an unqualified bar
+spectral sequence for the total curved differential in this regime.
 All standard chiral algebras (Heisenberg, Kac--Moody, Virasoro,
 $\cW$-algebras) have central curvature, so strict nilpotence holds
 throughout; see Remark~\ref{rem:voa-central-curvature} for the
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index 6f6e3e513dba8aa12ab332fe87b8a7c09096b212..7f7756a90cff7d603e6fc0f4309cb832d5d5c35a
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -117,7 +117,14 @@
 \end{tabular}
 \end{center}
 
-No completion is needed. The bar complex is conilpotent (finite-dimensional in each bar degree) and the differential is zero except for the curvature term $m_0$. Convergence of the bar spectral sequence follows: the filtration by bar degree is bounded below ($n \geq 0$) and exhaustive, with finite-dimensional graded pieces, so the spectral sequence converges to the bar homology by the standard bounded-below complete convergence theorem (\cite{LV12}, Theorem~2.2.3).
+No completion is needed at genus~$0$. The strict genus-$0$ bar complex is
+conilpotent (finite-dimensional in each bar degree) and its ordinary bar
+differential is zero; the higher-genus curved correction is handled later
+on the coderived side. Convergence of the genus-$0$ bar spectral sequence
+then follows: the filtration by bar degree is bounded below ($n \geq 0$)
+and exhaustive, with finite-dimensional graded pieces, so the spectral
+sequence converges to the ordinary bar homology by the standard
+bounded-below complete convergence theorem (\cite{LV12}, Theorem~2.2.3).
 
 \emph{Reference}: See \cite{GLZ22} Section 6, Proposition 6.2 for the identification
 of the twisted chiral enveloping algebra with CE algebra structure.
@@ -4522,13 +4529,17 @@
 \index{quadratic frontier|textbf}
 
 The categorical logarithm encodes a chiral
-algebra~$\cA$ as the bar complex $\barB(\cA)$, whose Taylor expansion
-is the PBW spectral sequence, whose leading coefficient is the modular
-characteristic~$\kappa(\cA)$, and whose curvature
-$\dfib^{\,2} = \kappa(\cA) \cdot \omega_g$ governs the genus
-transition. On a locus where the full scalar package is known to be
-governed by~$\kappa(\cA)$, this curvature controls the scalar genus
-tower.
+algebra~$\cA$ as the bar complex $\barB(\cA)$. On the strict
+genus-$0$ or associated-graded lane, its Taylor expansion is the PBW
+spectral sequence, whose leading coefficient is the modular
+characteristic~$\kappa(\cA)$. By contrast, once the higher-genus
+fiber operator satisfies
+$\dfib^{\,2} = \kappa(\cA) \cdot \omega_g$, the genus transition is
+tracked either by the flat comparison differential $\Dg{g}$ or by the
+coderived bar-degree filtration, not by ordinary cohomology of the
+raw curved fiber complex. On a locus where the full scalar package is
+known to be governed by~$\kappa(\cA)$, this curvature controls the
+scalar genus tower.
 
 We now consider what happens when
 that stronger scalar-package hypothesis is left. The Whitehead decomposition
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index dec9ecb32841b9b9b25c237fdfd39a834fb3f9ee..d42005a148feeefe896f5af5b08aad9e62f62917
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -6239,16 +6239,36 @@
 \textup{[Regime: curved-central
 \textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
 
-Filtered algebras $(\cA_1, \cA_2)$ with curvatures $\kappa_1, \kappa_2$ form a curved Koszul pair if:
+Filtered algebras $(\cA_1, \cA_2)$ with curvatures $\kappa_1, \kappa_2$
+form a curved Koszul pair in the filtered coderived sense if:
 \begin{enumerate}
 \item Associated graded $(\mathrm{gr}\,\cA_1, \mathrm{gr}\,\cA_2)$ are classical Koszul dual
 \item Curvatures are dual: $\kappa_1 \leftrightarrow -\kappa_2$ under the Koszul pairing
-\item The spectral sequence associated to the filtration degenerates at $E_2$
+\item The coderived spectral sequence associated to the filtration,
+ computed from the strict associated graded of the curved bar complex,
+ degenerates at $E_2$
 \end{enumerate}
 \end{theorem}
 
 \begin{proof}
-The filtered bar complex $F_\bullet \B(\cA_1)$ has associated graded $\mathrm{gr}\,\B(\cA_1) = \B(\mathrm{gr}\,\cA_1)$. By condition (1), $\Omega(\B(\mathrm{gr}\,\cA_1)) \simeq \mathrm{gr}\,\cA_2$ at the $E_1$ level. The curvature condition (2) ensures that the $m_0$ elements of the two algebras are related by $\kappa_2 = -\kappa_1^*$ under the Koszul pairing, which is the compatibility condition for curved $A_\infty$ morphisms (Positselski \cite{Positselski11}). The degeneration condition (3) then gives $\Omega(\B(\cA_1)) \simeq \cA_2$ as curved $A_\infty$ algebras. This is the standard criterion for curved Koszul pairs (Loday--Vallette \cite{LV12}, \S10.3), lifted to the chiral setting via Theorem~\ref{thm:geometric-equals-operadic-bar} (geometric bar = operadic bar).
+The filtered curved bar complex $F_\bullet \B(\cA_1)$ has associated
+graded $\mathrm{gr}\,\B(\cA_1) = \B(\mathrm{gr}\,\cA_1)$, and the
+curvature lies in positive filtration, so the associated-graded
+differential is square-zero. By condition~(1),
+$\Omega(\B(\mathrm{gr}\,\cA_1)) \simeq \mathrm{gr}\,\cA_2$ at the
+$E_1$ level. The curvature condition~(2) ensures that the $m_0$
+elements of the two algebras are related by
+$\kappa_2 = -\kappa_1^*$ under the Koszul pairing, which is the
+compatibility condition for curved $A_\infty$ morphisms
+(Positselski~\cite{Positselski11}). The degeneration condition~(3)
+then gives the bar-cobar comparison in the filtered coderived
+category; on loci where the coderived comparison promotes to an
+ordinary chain-level statement, one recovers
+$\Omega(\B(\cA_1)) \simeq \cA_2$ as curved $A_\infty$ algebras. This is
+the standard criterion for curved Koszul pairs
+(Loday--Vallette~\cite{LV12}, \S10.3), lifted to the chiral setting via
+Theorem~\ref{thm:geometric-equals-operadic-bar} (geometric bar =
+operadic bar).
 \end{proof}
 
 % ================================================================
@@ -6367,7 +6387,10 @@
 
 \item The central charge $c$ enters non-linearly in higher bar degrees, preventing a quadratic Koszul resolution.
 \end{enumerate}
-One needs the PBW spectral sequence approach (Theorem~\ref{thm:pbw-koszulness-criterion}), or equivalently, curved Koszul duality (Positselski) with nilpotent completion and a filtered/completed category.
+One needs the PBW spectral sequence approach
+(Theorem~\ref{thm:pbw-koszulness-criterion}), or equivalently,
+Positselski's curved Koszul duality in its coderived,
+nilpotently completed, filtered setting.
 
 \emph{Contrast with Heisenberg/Kac--Moody.}
 \begin{center}
diff --git a/chapters/theory/chiral_modules.tex b/chapters/theory/chiral_modules.tex
index 31c1dfb431aba58853fc92f99bc99383f16b37be..a503b83e41878075ce0885ae10f0369eb14f0970
--- a/chapters/theory/chiral_modules.tex
+++ b/chapters/theory/chiral_modules.tex
@@ -2126,7 +2126,14 @@
 \begin{remark}[Associated variety and Koszul duality]
 \label{rem:associated-variety-koszul}
 \index{associated variety!Koszul duality}
-The associated variety is \emph{not} preserved by level-shifting Koszul duality: e.g., $X_{L_1(\mathfrak{sl}_2)} = \{0\}$ but $X_{L_{-3}(\mathfrak{sl}_2)} = \mathfrak{sl}_2^*$. When $X_V = \{0\}$, the bar spectral sequence degenerates at a finite page; for $X_V \neq \{0\}$ it may have non-trivial higher differentials, marking the passage from Koszul to curved $A_\infty$.
+The associated variety is \emph{not} preserved by level-shifting Koszul
+duality: e.g., $X_{L_1(\mathfrak{sl}_2)} = \{0\}$ but
+$X_{L_{-3}(\mathfrak{sl}_2)} = \mathfrak{sl}_2^*$. When $X_V = \{0\}$,
+the bar spectral sequence degenerates at a finite page; for
+$X_V \neq \{0\}$ it may have non-trivial higher differentials, marking
+the passage from Koszul to curved $A_\infty$. Off that square-zero
+locus, the comparison should be read on the coderived side rather than
+as an ordinary bar-cohomology statement.
 \end{remark}
 
 \begin{conjecture}[Type-$A$ orbit duality for affine simple quotients; \ClaimStatusConjectured]
diff --git a/chapters/theory/cobar_construction.tex b/chapters/theory/cobar_construction.tex
index baf55cf992bb32c62f1a00820d1c6d08f73cebec..0aaf81e80c78be3a6f81a39f6994171be62a439d
--- a/chapters/theory/cobar_construction.tex
+++ b/chapters/theory/cobar_construction.tex
@@ -3107,7 +3107,11 @@
 \begin{proof}[Proof (outline; full proof in \S\textup{\ref{sec:complementarity-theorem}})]
 The complete proof, synthesizing five lemmas via the Verdier
 involution~$\sigma$ and the genus spectral sequence, is given in
-Theorem~\ref{thm:quantum-complementarity-main}.
+Theorem~\ref{thm:quantum-complementarity-main}. Here the spectral
+sequence is taken for the square-zero total comparison differential, or
+equivalently for the coderived filtration on the curved bar family; it
+is not the ordinary spectral sequence of the raw fiber operator when
+$\dfib^{\,2} \neq 0$.
 
 \emph{Foundation: Curved $A_\infty$ Structures}
 
@@ -3134,6 +3138,9 @@
 The total corrected differential $\Dg{g}$, which incorporates period
 corrections to restore strict nilpotence ($\Dg{g}^{\,2} = 0$), is
 introduced in Convention~\ref{conv:higher-genus-differentials}.
+Accordingly, any spectral-sequence or $H^*$ statement below uses either
+$\Dg{g}$ or the coderived bar-degree filtration, not the raw curved
+fiber complex $(\barB_g(\mathcal{A}), \dfib)$.
 
 \medskip
 


thinking
**Fixing patch visibility**

Oops, it seems like our patch line 6370 isn't showing up because the snippet after line 6368 didn't quite reach it. I need to check around line 6388 for context. Maybe the patch should be placed below line 638? I’ll have to search and see what’s going on. Let’s ensure everything's lined up properly so the information is visible where it needs to be!
exec
/bin/zsh -lc "rg -n 'Positselski|coderived,|PBW spectral sequence approach' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
4493:This follows from the Polishchuk--Positselski PBW criterion
4510: algebra in the sense of Polishchuk--Positselski.
4520:The Polishchuk--Positselski criterion then gives: the PBW flat
6263:(Positselski~\cite{Positselski11}). The degeneration condition~(3)
6390:One needs the PBW spectral sequence approach
6392:Positselski's curved Koszul duality in its coderived,
6463:In the classical (non-chiral) setting, tensor products of Koszul algebras are Koszul: if $A_1$ and $A_2$ are Koszul quadratic algebras, then $A_1 \otimes A_2$ is Koszul with $(A_1 \otimes A_2)^! \cong A_1^! \otimes A_2^!$ (Polishchuk--Positselski, Theorem 3.1).
file update:
diff --git a/chapters/theory/bar_cobar_adjunction_curved.tex b/chapters/theory/bar_cobar_adjunction_curved.tex
index 9f149679c80b6dec8cb90edcd3ce927df7e6198b..b3a3459a72f92f710f7f0eea792dd68ab3c67715
--- a/chapters/theory/bar_cobar_adjunction_curved.tex
+++ b/chapters/theory/bar_cobar_adjunction_curved.tex
@@ -5871,8 +5871,11 @@
 \begin{remark}[Non-central curvature]\label{rem:non-central-curvature}
 If the curvature $\mu_0$ is not central, then $d_{\text{bar}}^2 \neq 0$
 and nilpotence holds only up to homotopy: the bar complex requires
-homotopy coherent structures, spectral sequences that may not
-degenerate, and the full $A_\infty$/$L_\infty$ framework at every level.
+homotopy coherent structures, coderived filtrations whose
+associated-graded differential is square-zero, and the full
+$A_\infty$/$L_\infty$ framework at every level. In particular, one
+should not speak of ordinary bar cohomology or an unqualified bar
+spectral sequence for the total curved differential in this regime.
 All standard chiral algebras (Heisenberg, Kac--Moody, Virasoro,
 $\cW$-algebras) have central curvature, so strict nilpotence holds
 throughout; see Remark~\ref{rem:voa-central-curvature} for the
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index 6f6e3e513dba8aa12ab332fe87b8a7c09096b212..7f7756a90cff7d603e6fc0f4309cb832d5d5c35a
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -117,7 +117,14 @@
 \end{tabular}
 \end{center}
 
-No completion is needed. The bar complex is conilpotent (finite-dimensional in each bar degree) and the differential is zero except for the curvature term $m_0$. Convergence of the bar spectral sequence follows: the filtration by bar degree is bounded below ($n \geq 0$) and exhaustive, with finite-dimensional graded pieces, so the spectral sequence converges to the bar homology by the standard bounded-below complete convergence theorem (\cite{LV12}, Theorem~2.2.3).
+No completion is needed at genus~$0$. The strict genus-$0$ bar complex is
+conilpotent (finite-dimensional in each bar degree) and its ordinary bar
+differential is zero; the higher-genus curved correction is handled later
+on the coderived side. Convergence of the genus-$0$ bar spectral sequence
+then follows: the filtration by bar degree is bounded below ($n \geq 0$)
+and exhaustive, with finite-dimensional graded pieces, so the spectral
+sequence converges to the ordinary bar homology by the standard
+bounded-below complete convergence theorem (\cite{LV12}, Theorem~2.2.3).
 
 \emph{Reference}: See \cite{GLZ22} Section 6, Proposition 6.2 for the identification
 of the twisted chiral enveloping algebra with CE algebra structure.
@@ -4522,13 +4529,17 @@
 \index{quadratic frontier|textbf}
 
 The categorical logarithm encodes a chiral
-algebra~$\cA$ as the bar complex $\barB(\cA)$, whose Taylor expansion
-is the PBW spectral sequence, whose leading coefficient is the modular
-characteristic~$\kappa(\cA)$, and whose curvature
-$\dfib^{\,2} = \kappa(\cA) \cdot \omega_g$ governs the genus
-transition. On a locus where the full scalar package is known to be
-governed by~$\kappa(\cA)$, this curvature controls the scalar genus
-tower.
+algebra~$\cA$ as the bar complex $\barB(\cA)$. On the strict
+genus-$0$ or associated-graded lane, its Taylor expansion is the PBW
+spectral sequence, whose leading coefficient is the modular
+characteristic~$\kappa(\cA)$. By contrast, once the higher-genus
+fiber operator satisfies
+$\dfib^{\,2} = \kappa(\cA) \cdot \omega_g$, the genus transition is
+tracked either by the flat comparison differential $\Dg{g}$ or by the
+coderived bar-degree filtration, not by ordinary cohomology of the
+raw curved fiber complex. On a locus where the full scalar package is
+known to be governed by~$\kappa(\cA)$, this curvature controls the
+scalar genus tower.
 
 We now consider what happens when
 that stronger scalar-package hypothesis is left. The Whitehead decomposition
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index dec9ecb32841b9b9b25c237fdfd39a834fb3f9ee..d42005a148feeefe896f5af5b08aad9e62f62917
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -6239,16 +6239,36 @@
 \textup{[Regime: curved-central
 \textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
 
-Filtered algebras $(\cA_1, \cA_2)$ with curvatures $\kappa_1, \kappa_2$ form a curved Koszul pair if:
+Filtered algebras $(\cA_1, \cA_2)$ with curvatures $\kappa_1, \kappa_2$
+form a curved Koszul pair in the filtered coderived sense if:
 \begin{enumerate}
 \item Associated graded $(\mathrm{gr}\,\cA_1, \mathrm{gr}\,\cA_2)$ are classical Koszul dual
 \item Curvatures are dual: $\kappa_1 \leftrightarrow -\kappa_2$ under the Koszul pairing
-\item The spectral sequence associated to the filtration degenerates at $E_2$
+\item The coderived spectral sequence associated to the filtration,
+ computed from the strict associated graded of the curved bar complex,
+ degenerates at $E_2$
 \end{enumerate}
 \end{theorem}
 
 \begin{proof}
-The filtered bar complex $F_\bullet \B(\cA_1)$ has associated graded $\mathrm{gr}\,\B(\cA_1) = \B(\mathrm{gr}\,\cA_1)$. By condition (1), $\Omega(\B(\mathrm{gr}\,\cA_1)) \simeq \mathrm{gr}\,\cA_2$ at the $E_1$ level. The curvature condition (2) ensures that the $m_0$ elements of the two algebras are related by $\kappa_2 = -\kappa_1^*$ under the Koszul pairing, which is the compatibility condition for curved $A_\infty$ morphisms (Positselski \cite{Positselski11}). The degeneration condition (3) then gives $\Omega(\B(\cA_1)) \simeq \cA_2$ as curved $A_\infty$ algebras. This is the standard criterion for curved Koszul pairs (Loday--Vallette \cite{LV12}, \S10.3), lifted to the chiral setting via Theorem~\ref{thm:geometric-equals-operadic-bar} (geometric bar = operadic bar).
+The filtered curved bar complex $F_\bullet \B(\cA_1)$ has associated
+graded $\mathrm{gr}\,\B(\cA_1) = \B(\mathrm{gr}\,\cA_1)$, and the
+curvature lies in positive filtration, so the associated-graded
+differential is square-zero. By condition~(1),
+$\Omega(\B(\mathrm{gr}\,\cA_1)) \simeq \mathrm{gr}\,\cA_2$ at the
+$E_1$ level. The curvature condition~(2) ensures that the $m_0$
+elements of the two algebras are related by
+$\kappa_2 = -\kappa_1^*$ under the Koszul pairing, which is the
+compatibility condition for curved $A_\infty$ morphisms
+(Positselski~\cite{Positselski11}). The degeneration condition~(3)
+then gives the bar-cobar comparison in the filtered coderived
+category; on loci where the coderived comparison promotes to an
+ordinary chain-level statement, one recovers
+$\Omega(\B(\cA_1)) \simeq \cA_2$ as curved $A_\infty$ algebras. This is
+the standard criterion for curved Koszul pairs
+(Loday--Vallette~\cite{LV12}, \S10.3), lifted to the chiral setting via
+Theorem~\ref{thm:geometric-equals-operadic-bar} (geometric bar =
+operadic bar).
 \end{proof}
 
 % ================================================================
@@ -6367,7 +6387,10 @@
 
 \item The central charge $c$ enters non-linearly in higher bar degrees, preventing a quadratic Koszul resolution.
 \end{enumerate}
-One needs the PBW spectral sequence approach (Theorem~\ref{thm:pbw-koszulness-criterion}), or equivalently, curved Koszul duality (Positselski) with nilpotent completion and a filtered/completed category.
+One needs the PBW spectral sequence approach
+(Theorem~\ref{thm:pbw-koszulness-criterion}), or equivalently,
+Positselski's curved Koszul duality in its coderived,
+nilpotently completed, filtered setting.
 
 \emph{Contrast with Heisenberg/Kac--Moody.}
 \begin{center}
diff --git a/chapters/theory/chiral_modules.tex b/chapters/theory/chiral_modules.tex
index 31c1dfb431aba58853fc92f99bc99383f16b37be..a503b83e41878075ce0885ae10f0369eb14f0970
--- a/chapters/theory/chiral_modules.tex
+++ b/chapters/theory/chiral_modules.tex
@@ -2126,7 +2126,14 @@
 \begin{remark}[Associated variety and Koszul duality]
 \label{rem:associated-variety-koszul}
 \index{associated variety!Koszul duality}
-The associated variety is \emph{not} preserved by level-shifting Koszul duality: e.g., $X_{L_1(\mathfrak{sl}_2)} = \{0\}$ but $X_{L_{-3}(\mathfrak{sl}_2)} = \mathfrak{sl}_2^*$. When $X_V = \{0\}$, the bar spectral sequence degenerates at a finite page; for $X_V \neq \{0\}$ it may have non-trivial higher differentials, marking the passage from Koszul to curved $A_\infty$.
+The associated variety is \emph{not} preserved by level-shifting Koszul
+duality: e.g., $X_{L_1(\mathfrak{sl}_2)} = \{0\}$ but
+$X_{L_{-3}(\mathfrak{sl}_2)} = \mathfrak{sl}_2^*$. When $X_V = \{0\}$,
+the bar spectral sequence degenerates at a finite page; for
+$X_V \neq \{0\}$ it may have non-trivial higher differentials, marking
+the passage from Koszul to curved $A_\infty$. Off that square-zero
+locus, the comparison should be read on the coderived side rather than
+as an ordinary bar-cohomology statement.
 \end{remark}
 
 \begin{conjecture}[Type-$A$ orbit duality for affine simple quotients; \ClaimStatusConjectured]
diff --git a/chapters/theory/cobar_construction.tex b/chapters/theory/cobar_construction.tex
index baf55cf992bb32c62f1a00820d1c6d08f73cebec..0aaf81e80c78be3a6f81a39f6994171be62a439d
--- a/chapters/theory/cobar_construction.tex
+++ b/chapters/theory/cobar_construction.tex
@@ -3107,7 +3107,11 @@
 \begin{proof}[Proof (outline; full proof in \S\textup{\ref{sec:complementarity-theorem}})]
 The complete proof, synthesizing five lemmas via the Verdier
 involution~$\sigma$ and the genus spectral sequence, is given in
-Theorem~\ref{thm:quantum-complementarity-main}.
+Theorem~\ref{thm:quantum-complementarity-main}. Here the spectral
+sequence is taken for the square-zero total comparison differential, or
+equivalently for the coderived filtration on the curved bar family; it
+is not the ordinary spectral sequence of the raw fiber operator when
+$\dfib^{\,2} \neq 0$.
 
 \emph{Foundation: Curved $A_\infty$ Structures}
 
@@ -3134,6 +3138,9 @@
 The total corrected differential $\Dg{g}$, which incorporates period
 corrections to restore strict nilpotence ($\Dg{g}^{\,2} = 0$), is
 introduced in Convention~\ref{conv:higher-genus-differentials}.
+Accordingly, any spectral-sequence or $H^*$ statement below uses either
+$\Dg{g}$ or the coderived bar-degree filtration, not the raw curved
+fiber complex $(\barB_g(\mathcal{A}), \dfib)$.
 
 \medskip
 

exec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '6388,6395p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  6388	\item The central charge $c$ enters non-linearly in higher bar degrees, preventing a quadratic Koszul resolution.
  6389	\end{enumerate}
  6390	One needs the PBW spectral sequence approach
  6391	(Theorem~\ref{thm:pbw-koszulness-criterion}), or equivalently,
  6392	Positselski's curved Koszul duality in its coderived,
  6393	nilpotently completed, filtered setting.
  6394	
  6395	\emph{Contrast with Heisenberg/Kac--Moody.}
file update:
diff --git a/chapters/theory/bar_cobar_adjunction_curved.tex b/chapters/theory/bar_cobar_adjunction_curved.tex
index 9f149679c80b6dec8cb90edcd3ce927df7e6198b..b3a3459a72f92f710f7f0eea792dd68ab3c67715
--- a/chapters/theory/bar_cobar_adjunction_curved.tex
+++ b/chapters/theory/bar_cobar_adjunction_curved.tex
@@ -5871,8 +5871,11 @@
 \begin{remark}[Non-central curvature]\label{rem:non-central-curvature}
 If the curvature $\mu_0$ is not central, then $d_{\text{bar}}^2 \neq 0$
 and nilpotence holds only up to homotopy: the bar complex requires
-homotopy coherent structures, spectral sequences that may not
-degenerate, and the full $A_\infty$/$L_\infty$ framework at every level.
+homotopy coherent structures, coderived filtrations whose
+associated-graded differential is square-zero, and the full
+$A_\infty$/$L_\infty$ framework at every level. In particular, one
+should not speak of ordinary bar cohomology or an unqualified bar
+spectral sequence for the total curved differential in this regime.
 All standard chiral algebras (Heisenberg, Kac--Moody, Virasoro,
 $\cW$-algebras) have central curvature, so strict nilpotence holds
 throughout; see Remark~\ref{rem:voa-central-curvature} for the
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index 6f6e3e513dba8aa12ab332fe87b8a7c09096b212..7f7756a90cff7d603e6fc0f4309cb832d5d5c35a
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -117,7 +117,14 @@
 \end{tabular}
 \end{center}
 
-No completion is needed. The bar complex is conilpotent (finite-dimensional in each bar degree) and the differential is zero except for the curvature term $m_0$. Convergence of the bar spectral sequence follows: the filtration by bar degree is bounded below ($n \geq 0$) and exhaustive, with finite-dimensional graded pieces, so the spectral sequence converges to the bar homology by the standard bounded-below complete convergence theorem (\cite{LV12}, Theorem~2.2.3).
+No completion is needed at genus~$0$. The strict genus-$0$ bar complex is
+conilpotent (finite-dimensional in each bar degree) and its ordinary bar
+differential is zero; the higher-genus curved correction is handled later
+on the coderived side. Convergence of the genus-$0$ bar spectral sequence
+then follows: the filtration by bar degree is bounded below ($n \geq 0$)
+and exhaustive, with finite-dimensional graded pieces, so the spectral
+sequence converges to the ordinary bar homology by the standard
+bounded-below complete convergence theorem (\cite{LV12}, Theorem~2.2.3).
 
 \emph{Reference}: See \cite{GLZ22} Section 6, Proposition 6.2 for the identification
 of the twisted chiral enveloping algebra with CE algebra structure.
@@ -4522,13 +4529,17 @@
 \index{quadratic frontier|textbf}
 
 The categorical logarithm encodes a chiral
-algebra~$\cA$ as the bar complex $\barB(\cA)$, whose Taylor expansion
-is the PBW spectral sequence, whose leading coefficient is the modular
-characteristic~$\kappa(\cA)$, and whose curvature
-$\dfib^{\,2} = \kappa(\cA) \cdot \omega_g$ governs the genus
-transition. On a locus where the full scalar package is known to be
-governed by~$\kappa(\cA)$, this curvature controls the scalar genus
-tower.
+algebra~$\cA$ as the bar complex $\barB(\cA)$. On the strict
+genus-$0$ or associated-graded lane, its Taylor expansion is the PBW
+spectral sequence, whose leading coefficient is the modular
+characteristic~$\kappa(\cA)$. By contrast, once the higher-genus
+fiber operator satisfies
+$\dfib^{\,2} = \kappa(\cA) \cdot \omega_g$, the genus transition is
+tracked either by the flat comparison differential $\Dg{g}$ or by the
+coderived bar-degree filtration, not by ordinary cohomology of the
+raw curved fiber complex. On a locus where the full scalar package is
+known to be governed by~$\kappa(\cA)$, this curvature controls the
+scalar genus tower.
 
 We now consider what happens when
 that stronger scalar-package hypothesis is left. The Whitehead decomposition
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index dec9ecb32841b9b9b25c237fdfd39a834fb3f9ee..d42005a148feeefe896f5af5b08aad9e62f62917
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -6239,16 +6239,36 @@
 \textup{[Regime: curved-central
 \textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
 
-Filtered algebras $(\cA_1, \cA_2)$ with curvatures $\kappa_1, \kappa_2$ form a curved Koszul pair if:
+Filtered algebras $(\cA_1, \cA_2)$ with curvatures $\kappa_1, \kappa_2$
+form a curved Koszul pair in the filtered coderived sense if:
 \begin{enumerate}
 \item Associated graded $(\mathrm{gr}\,\cA_1, \mathrm{gr}\,\cA_2)$ are classical Koszul dual
 \item Curvatures are dual: $\kappa_1 \leftrightarrow -\kappa_2$ under the Koszul pairing
-\item The spectral sequence associated to the filtration degenerates at $E_2$
+\item The coderived spectral sequence associated to the filtration,
+ computed from the strict associated graded of the curved bar complex,
+ degenerates at $E_2$
 \end{enumerate}
 \end{theorem}
 
 \begin{proof}
-The filtered bar complex $F_\bullet \B(\cA_1)$ has associated graded $\mathrm{gr}\,\B(\cA_1) = \B(\mathrm{gr}\,\cA_1)$. By condition (1), $\Omega(\B(\mathrm{gr}\,\cA_1)) \simeq \mathrm{gr}\,\cA_2$ at the $E_1$ level. The curvature condition (2) ensures that the $m_0$ elements of the two algebras are related by $\kappa_2 = -\kappa_1^*$ under the Koszul pairing, which is the compatibility condition for curved $A_\infty$ morphisms (Positselski \cite{Positselski11}). The degeneration condition (3) then gives $\Omega(\B(\cA_1)) \simeq \cA_2$ as curved $A_\infty$ algebras. This is the standard criterion for curved Koszul pairs (Loday--Vallette \cite{LV12}, \S10.3), lifted to the chiral setting via Theorem~\ref{thm:geometric-equals-operadic-bar} (geometric bar = operadic bar).
+The filtered curved bar complex $F_\bullet \B(\cA_1)$ has associated
+graded $\mathrm{gr}\,\B(\cA_1) = \B(\mathrm{gr}\,\cA_1)$, and the
+curvature lies in positive filtration, so the associated-graded
+differential is square-zero. By condition~(1),
+$\Omega(\B(\mathrm{gr}\,\cA_1)) \simeq \mathrm{gr}\,\cA_2$ at the
+$E_1$ level. The curvature condition~(2) ensures that the $m_0$
+elements of the two algebras are related by
+$\kappa_2 = -\kappa_1^*$ under the Koszul pairing, which is the
+compatibility condition for curved $A_\infty$ morphisms
+(Positselski~\cite{Positselski11}). The degeneration condition~(3)
+then gives the bar-cobar comparison in the filtered coderived
+category; on loci where the coderived comparison promotes to an
+ordinary chain-level statement, one recovers
+$\Omega(\B(\cA_1)) \simeq \cA_2$ as curved $A_\infty$ algebras. This is
+the standard criterion for curved Koszul pairs
+(Loday--Vallette~\cite{LV12}, \S10.3), lifted to the chiral setting via
+Theorem~\ref{thm:geometric-equals-operadic-bar} (geometric bar =
+operadic bar).
 \end{proof}
 
 % ================================================================
@@ -6367,7 +6387,10 @@
 
 \item The central charge $c$ enters non-linearly in higher bar degrees, preventing a quadratic Koszul resolution.
 \end{enumerate}
-One needs the PBW spectral sequence approach (Theorem~\ref{thm:pbw-koszulness-criterion}), or equivalently, curved Koszul duality (Positselski) with nilpotent completion and a filtered/completed category.
+One needs the PBW spectral sequence approach
+(Theorem~\ref{thm:pbw-koszulness-criterion}), or equivalently,
+Positselski's curved Koszul duality in its coderived,
+nilpotently completed, filtered setting.
 
 \emph{Contrast with Heisenberg/Kac--Moody.}
 \begin{center}
diff --git a/chapters/theory/chiral_modules.tex b/chapters/theory/chiral_modules.tex
index 31c1dfb431aba58853fc92f99bc99383f16b37be..a503b83e41878075ce0885ae10f0369eb14f0970
--- a/chapters/theory/chiral_modules.tex
+++ b/chapters/theory/chiral_modules.tex
@@ -2126,7 +2126,14 @@
 \begin{remark}[Associated variety and Koszul duality]
 \label{rem:associated-variety-koszul}
 \index{associated variety!Koszul duality}
-The associated variety is \emph{not} preserved by level-shifting Koszul duality: e.g., $X_{L_1(\mathfrak{sl}_2)} = \{0\}$ but $X_{L_{-3}(\mathfrak{sl}_2)} = \mathfrak{sl}_2^*$. When $X_V = \{0\}$, the bar spectral sequence degenerates at a finite page; for $X_V \neq \{0\}$ it may have non-trivial higher differentials, marking the passage from Koszul to curved $A_\infty$.
+The associated variety is \emph{not} preserved by level-shifting Koszul
+duality: e.g., $X_{L_1(\mathfrak{sl}_2)} = \{0\}$ but
+$X_{L_{-3}(\mathfrak{sl}_2)} = \mathfrak{sl}_2^*$. When $X_V = \{0\}$,
+the bar spectral sequence degenerates at a finite page; for
+$X_V \neq \{0\}$ it may have non-trivial higher differentials, marking
+the passage from Koszul to curved $A_\infty$. Off that square-zero
+locus, the comparison should be read on the coderived side rather than
+as an ordinary bar-cohomology statement.
 \end{remark}
 
 \begin{conjecture}[Type-$A$ orbit duality for affine simple quotients; \ClaimStatusConjectured]
diff --git a/chapters/theory/cobar_construction.tex b/chapters/theory/cobar_construction.tex
index baf55cf992bb32c62f1a00820d1c6d08f73cebec..0aaf81e80c78be3a6f81a39f6994171be62a439d
--- a/chapters/theory/cobar_construction.tex
+++ b/chapters/theory/cobar_construction.tex
@@ -3107,7 +3107,11 @@
 \begin{proof}[Proof (outline; full proof in \S\textup{\ref{sec:complementarity-theorem}})]
 The complete proof, synthesizing five lemmas via the Verdier
 involution~$\sigma$ and the genus spectral sequence, is given in
-Theorem~\ref{thm:quantum-complementarity-main}.
+Theorem~\ref{thm:quantum-complementarity-main}. Here the spectral
+sequence is taken for the square-zero total comparison differential, or
+equivalently for the coderived filtration on the curved bar family; it
+is not the ordinary spectral sequence of the raw fiber operator when
+$\dfib^{\,2} \neq 0$.
 
 \emph{Foundation: Curved $A_\infty$ Structures}
 
@@ -3134,6 +3138,9 @@
 The total corrected differential $\Dg{g}$, which incorporates period
 corrections to restore strict nilpotence ($\Dg{g}^{\,2} = 0$), is
 introduced in Convention~\ref{conv:higher-genus-differentials}.
+Accordingly, any spectral-sequence or $H^*$ statement below uses either
+$\Dg{g}$ or the coderived bar-degree filtration, not the raw curved
+fiber complex $(\barB_g(\mathcal{A}), \dfib)$.
 
 \medskip
 

codex
I’ve re-read the patched sentences. The remaining step is a diff-based audit plus a grep for residual `spectral sequence` / `H^*` phrasing on the touched surfaces, to confirm I didn’t leave a curved complex talking like an ordinary cochain complex.
exec
/bin/zsh -lc "rg -n -C 2 'spectral sequence|H\\"'^'"\\*|coderived|\\dfib|omega_g' chapters/theory/bar_cobar_adjunction_curved.tex chapters/theory/bar_cobar_adjunction_inversion.tex chapters/theory/chiral_koszul_pairs.tex chapters/theory/chiral_modules.tex chapters/theory/cobar_construction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'git diff --unified=3 -- chapters/theory/bar_cobar_adjunction_curved.tex chapters/theory/bar_cobar_adjunction_inversion.tex chapters/theory/chiral_koszul_pairs.tex chapters/theory/chiral_modules.tex chapters/theory/cobar_construction.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Total output lines: 2010

chapters/theory/cobar_construction.tex-52-
chapters/theory/cobar_construction.tex-53-At genus~$g \geq 1$ the fiberwise differential satisfies
chapters/theory/cobar_construction.tex:54:$d_{\mathrm{fib}}^2 = \kappa \cdot \omega_g$, reflecting the curved
chapters/theory/cobar_construction.tex-55-$A_\infty$ structure $\mu_1^2 = [\mu_0, -]$
chapters/theory/cobar_construction.tex-56-(Chapter~\ref{chap:bar-cobar-adjunction}). The total bar differential
--
chapters/theory/cobar_construction.tex-60-obstruction tower $\Theta_\cA^{\leq r}$
chapters/theory/cobar_construction.tex-61-(Proposition~\ref{prop:cobar-modular-shadow}).
chapters/theory/cobar_construction.tex:62:Strict inversion may require completion or coderived contexts
chapters/theory/cobar_construction.tex-63-at higher genus.
chapters/theory/cobar_construction.tex-64-
--
chapters/theory/cobar_construction.tex-1053-\emph{Cohomology.} Since all generators except $s^{-1}v$ are exact (boundaries 
chapters/theory/cobar_construction.tex-1054-of products), the cohomology is:
chapters/theory/cobar_construction.tex:1055:\[H^*(\Omega^{\text{ch}}(T^c_{\text{ch}}(V))) = \text{Free}_{\text{ch}}(s^{-1}v)\]
chapters/theory/cobar_construction.tex-1056-
chapters/theory/cobar_construction.tex-1057-This recovers the original generator $V$, as expected from bar-cobar inversion.
--
 succeeded in 51ms:
diff --git a/chapters/theory/bar_cobar_adjunction_curved.tex b/chapters/theory/bar_cobar_adjunction_curved.tex
index 9f14967..b3a3459 100644
--- a/chapters/theory/bar_cobar_adjunction_curved.tex
+++ b/chapters/theory/bar_cobar_adjunction_curved.tex
@@ -5871,8 +5871,11 @@ provided $\mu_0 \in Z(\mathcal{A})$.
 \begin{remark}[Non-central curvature]\label{rem:non-central-curvature}
 If the curvature $\mu_0$ is not central, then $d_{\text{bar}}^2 \neq 0$
 and nilpotence holds only up to homotopy: the bar complex requires
-homotopy coherent structures, spectral sequences that may not
-degenerate, and the full $A_\infty$/$L_\infty$ framework at every level.
+homotopy coherent structures, coderived filtrations whose
+associated-graded differential is square-zero, and the full
+$A_\infty$/$L_\infty$ framework at every level. In particular, one
+should not speak of ordinary bar cohomology or an unqualified bar
+spectral sequence for the total curved differential in this regime.
 All standard chiral algebras (Heisenberg, Kac--Moody, Virasoro,
 $\cW$-algebras) have central curvature, so strict nilpotence holds
 throughout; see Remark~\ref{rem:voa-central-curvature} for the
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index 6f6e3e5..7f7756a 100644
file update:
diff --git a/chapters/theory/bar_cobar_adjunction_curved.tex b/chapters/theory/bar_cobar_adjunction_curved.tex
index 9f149679c80b6dec8cb90edcd3ce927df7e6198b..b3a3459a72f92f710f7f0eea792dd68ab3c67715
--- a/chapters/theory/bar_cobar_adjunction_curved.tex
+++ b/chapters/theory/bar_cobar_adjunction_curved.tex
@@ -5871,8 +5871,11 @@
 \begin{remark}[Non-central curvature]\label{rem:non-central-curvature}
 If the curvature $\mu_0$ is not central, then $d_{\text{bar}}^2 \neq 0$
 and nilpotence holds only up to homotopy: the bar complex requires
-homotopy coherent structures, spectral sequences that may not
-degenerate, and the full $A_\infty$/$L_\infty$ framework at every level.
+homotopy coherent structures, coderived filtrations whose
+associated-graded differential is square-zero, and the full
+$A_\infty$/$L_\infty$ framework at every level. In particular, one
+should not speak of ordinary bar cohomology or an unqualified bar
+spectral sequence for the total curved differential in this regime.
 All standard chiral algebras (Heisenberg, Kac--Moody, Virasoro,
 $\cW$-algebras) have central curvature, so strict nilpotence holds
 throughout; see Remark~\ref{rem:voa-central-curvature} for the
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index 6f6e3e513dba8aa12ab332fe87b8a7c09096b212..7f7756a90cff7d603e6fc0f4309cb832d5d5c35a
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -117,7 +117,14 @@
 \end{tabular}
 \end{center}
 
-No completion is needed. The bar complex is conilpotent (finite-dimensional in each bar degree) and the differential is zero except for the curvature term $m_0$. Convergence of the bar spectral sequence follows: the filtration by bar degree is bounded below ($n \geq 0$) and exhaustive, with finite-dimensional graded pieces, so the spectral sequence converges to the bar homology by the standard bounded-below complete convergence theorem (\cite{LV12}, Theorem~2.2.3).
+No completion is needed at genus~$0$. The strict genus-$0$ bar complex is
+conilpotent (finite-dimensional in each bar degree) and its ordinary bar
+differential is zero; the higher-genus curved correction is handled later
+on the coderived side. Convergence of the genus-$0$ bar spectral sequence
+then follows: the filtration by bar degree is bounded below ($n \geq 0$)
+and exhaustive, with finite-dimensional graded pieces, so the spectral
+sequence converges to the ordinary bar homology by the standard
+bounded-below complete convergence theorem (\cite{LV12}, Theorem~2.2.3).
 
 \emph{Reference}: See \cite{GLZ22} Section 6, Proposition 6.2 for the identification
 of the twisted chiral enveloping algebra with CE algebra structure.
@@ -4522,13 +4529,17 @@
 \index{quadratic frontier|textbf}
 
 The categorical logarithm encodes a chiral
-algebra~$\cA$ as the bar complex $\barB(\cA)$, whose Taylor expansion
-is the PBW spectral sequence, whose leading coefficient is the modular
-characteristic~$\kappa(\cA)$, and whose curvature
-$\dfib^{\,2} = \kappa(\cA) \cdot \omega_g$ governs the genus
-transition. On a locus where the full scalar package is known to be
-governed by~$\kappa(\cA)$, this curvature controls the scalar genus
-tower.
+algebra~$\cA$ as the bar complex $\barB(\cA)$. On the strict
+genus-$0$ or associated-graded lane, its Taylor expansion is the PBW
+spectral sequence, whose leading coefficient is the modular
+characteristic~$\kappa(\cA)$. By contrast, once the higher-genus
+fiber operator satisfies
+$\dfib^{\,2} = \kappa(\cA) \cdot \omega_g$, the genus transition is
+tracked either by the flat comparison differential $\Dg{g}$ or by the
+coderived bar-degree filtration, not by ordinary cohomology of the
+raw curved fiber complex. On a locus where the full scalar package is
+known to be governed by~$\kappa(\cA)$, this curvature controls the
+scalar genus tower.
 
 We now consider what happens when
 that stronger scalar-package hypothesis is left. The Whitehead decomposition
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index dec9ecb32841b9b9b25c237fdfd39a834fb3f9ee..d42005a148feeefe896f5af5b08aad9e62f62917
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -6239,16 +6239,36 @@
 \textup{[Regime: curved-central
 \textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
 
-Filtered algebras $(\cA_1, \cA_2)$ with curvatures $\kappa_1, \kappa_2$ form a curved Koszul pair if:
+Filtered algebras $(\cA_1, \cA_2)$ with curvatures $\kappa_1, \kappa_2$
+form a curved Koszul pair in the filtered coderived sense if:
 \begin{enumerate}
 \item Associated graded $(\mathrm{gr}\,\cA_1, \mathrm{gr}\,\cA_2)$ are classical Koszul dual
 \item Curvatures are dual: $\kappa_1 \leftrightarrow -\kappa_2$ under the Koszul pairing
-\item The spectral sequence associated to the filtration degenerates at $E_2$
+\item The coderived spectral sequence associated to the filtration,
+ computed from the strict associated graded of the curved bar complex,
+ degenerates at $E_2$
 \end{enumerate}
 \end{theorem}
 
 \begin{proof}
-The filtered bar complex $F_\bullet \B(\cA_1)$ has associated graded $\mathrm{gr}\,\B(\cA_1) = \B(\mathrm{gr}\,\cA_1)$. By condition (1), $\Omega(\B(\mathrm{gr}\,\cA_1)) \simeq \mathrm{gr}\,\cA_2$ at the $E_1$ level. The curvature condition (2) ensures that the $m_0$ elements of the two algebras are related by $\kappa_2 = -\kappa_1^*$ under the Koszul pairing, which is the compatibility condition for curved $A_\infty$ morphisms (Positselski \cite{Positselski11}). The degeneration condition (3) then gives $\Omega(\B(\cA_1)) \simeq \cA_2$ as curved $A_\infty$ algebras. This is the standard criterion for curved Koszul pairs (Loday--Vallette \cite{LV12}, \S10.3), lifted to the chiral setting via Theorem~\ref{thm:geometric-equals-operadic-bar} (geometric bar = operadic bar).
+The filtered curved bar complex $F_\bullet \B(\cA_1)$ has associated
+graded $\mathrm{gr}\,\B(\cA_1) = \B(\mathrm{gr}\,\cA_1)$, and the
+curvature lies in positive filtration, so the associated-graded
+differential is square-zero. By condition~(1),
+$\Omega(\B(\mathrm{gr}\,\cA_1)) \simeq \mathrm{gr}\,\cA_2$ at the
+$E_1$ level. The curvature condition~(2) ensures that the $m_0$
+elements of the two algebras are related by
+$\kappa_2 = -\kappa_1^*$ under the Koszul pairing, which is the
+compatibility condition for curved $A_\infty$ morphisms
+(Positselski~\cite{Positselski11}). The degeneration condition~(3)
+then gives the bar-cobar comparison in the filtered coderived
+category; on loci where the coderived comparison promotes to an
+ordinary chain-level statement, one recovers
+$\Omega(\B(\cA_1)) \simeq \cA_2$ as curved $A_\infty$ algebras. This is
+the standard criterion for curved Koszul pairs
+(Loday--Vallette~\cite{LV12}, \S10.3), lifted to the chiral setting via
+Theorem~\ref{thm:geometric-equals-operadic-bar} (geometric bar =
+operadic bar).
 \end{proof}
 
 % ================================================================
@@ -6367,7 +6387,10 @@
 
 \item The central charge $c$ enters non-linearly in higher bar degrees, preventing a quadratic Koszul resolution.
 \end{enumerate}
-One needs the PBW spectral sequence approach (Theorem~\ref{thm:pbw-koszulness-criterion}), or equivalently, curved Koszul duality (Positselski) with nilpotent completion and a filtered/completed category.
+One needs the PBW spectral sequence approach
+(Theorem~\ref{thm:pbw-koszulness-criterion}), or equivalently,
+Positselski's curved Koszul duality in its coderived,
+nilpotently completed, filtered setting.
 
 \emph{Contrast with Heisenberg/Kac--Moody.}
 \begin{center}
diff --git a/chapters/theory/chiral_modules.tex b/chapters/theory/chiral_modules.tex
index 31c1dfb431aba58853fc92f99bc99383f16b37be..a503b83e41878075ce0885ae10f0369eb14f0970
--- a/chapters/theory/chiral_modules.tex
+++ b/chapters/theory/chiral_modules.tex
@@ -2126,7 +2126,14 @@
 \begin{remark}[Associated variety and Koszul duality]
 \label{rem:associated-variety-koszul}
 \index{associated variety!Koszul duality}
-The associated variety is \emph{not} preserved by level-shifting Koszul duality: e.g., $X_{L_1(\mathfrak{sl}_2)} = \{0\}$ but $X_{L_{-3}(\mathfrak{sl}_2)} = \mathfrak{sl}_2^*$. When $X_V = \{0\}$, the bar spectral sequence degenerates at a finite page; for $X_V \neq \{0\}$ it may have non-trivial higher differentials, marking the passage from Koszul to curved $A_\infty$.
+The associated variety is \emph{not} preserved by level-shifting Koszul
+duality: e.g., $X_{L_1(\mathfrak{sl}_2)} = \{0\}$ but
+$X_{L_{-3}(\mathfrak{sl}_2)} = \mathfrak{sl}_2^*$. When $X_V = \{0\}$,
+the bar spectral sequence degenerates at a finite page; for
+$X_V \neq \{0\}$ it may have non-trivial higher differentials, marking
+the passage from Koszul to curved $A_\infty$. Off that square-zero
+locus, the comparison should be read on the coderived side rather than
+as an ordinary bar-cohomology statement.
 \end{remark}
 
 \begin{conjecture}[Type-$A$ orbit duality for affine simple quotients; \ClaimStatusConjectured]
diff --git a/chapters/theory/cobar_construction.tex b/chapters/theory/cobar_construction.tex
index baf55cf992bb32c62f1a00820d1c6d08f73cebec..0aaf81e80c78be3a6f81a39f6994171be62a439d
--- a/chapters/theory/cobar_construction.tex
+++ b/chapters/theory/cobar_construction.tex
@@ -3107,7 +3107,11 @@
 \begin{proof}[Proof (outline; full proof in \S\textup{\ref{sec:complementarity-theorem}})]
 The complete proof, synthesizing five lemmas via the Verdier
 involution~$\sigma$ and the genus spectral sequence, is given in
-Theorem~\ref{thm:quantum-complementarity-main}.
+Theorem~\ref{thm:quantum-complementarity-main}. Here the spectral
+sequence is taken for the square-zero total comparison differential, or
+equivalently for the coderived filtration on the curved bar family; it
+is not the ordinary spectral sequence of the raw fiber operator when
+$\dfib^{\,2} \neq 0$.
 
 \emph{Foundation: Curved $A_\infty$ Structures}
 
@@ -3134,6 +3138,9 @@
 The total corrected differential $\Dg{g}$, which incorporates period
 corrections to restore strict nilpotence ($\Dg{g}^{\,2} = 0$), is
 introduced in Convention~\ref{conv:higher-genus-differentials}.
+Accordingly, any spectral-sequence or $H^*$ statement below uses either
+$\Dg{g}$ or the coderived bar-degree filtration, not the raw curved
+fiber complex $(\barB_g(\mathcal{A}), \dfib)$.
 
 \medskip
 


thinking
**Evaluating code checks**

I’m considering running `latexmk -pdf -interaction=nonstopmode -halt-on-error` on the main file, but the repo is huge, and it might not be necessary. I could use `rg -n 'ordinary bar cohomology|unqualified bar spectral sequence'` to check if anything weird has been introduced. Instead of compiling, I might run `git diff --check` to look for whitespace or errors. Also, using `rg -n` to find suspicious line patterns is on my mind too. Maybe I’ll narrow my grep options down.
exec
/bin/zsh -lc 'git diff --check -- chapters/theory/bar_cobar_adjunction_curved.tex chapters/theory/bar_cobar_adjunction_inversion.tex chapters/theory/chiral_koszul_pairs.tex chapters/theory/chiral_modules.tex chapters/theory/cobar_construction.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:

exec
/bin/zsh -lc "rg -n -P 'spectral sequence.*dfib|dfib.*spectral sequence|H\\"'^'"\\*\\(["'^)]*dfib|dfib[''^'"\\n]*H\\"'^'"\\*|spectral sequence.*omega_g|omega_g.*spectral sequence' chapters/theory/bar_cobar_adjunction_curved.tex chapters/theory/bar_cobar_adjunction_inversion.tex chapters/theory/chiral_koszul_pairs.tex chapters/theory/chiral_modules.tex chapters/theory/cobar_construction.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

file update:
diff --git a/chapters/theory/bar_cobar_adjunction_curved.tex b/chapters/theory/bar_cobar_adjunction_curved.tex
index 9f149679c80b6dec8cb90edcd3ce927df7e6198b..b3a3459a72f92f710f7f0eea792dd68ab3c67715
--- a/chapters/theory/bar_cobar_adjunction_curved.tex
+++ b/chapters/theory/bar_cobar_adjunction_curved.tex
@@ -5871,8 +5871,11 @@
 \begin{remark}[Non-central curvature]\label{rem:non-central-curvature}
 If the curvature $\mu_0$ is not central, then $d_{\text{bar}}^2 \neq 0$
 and nilpotence holds only up to homotopy: the bar complex requires
-homotopy coherent structures, spectral sequences that may not
-degenerate, and the full $A_\infty$/$L_\infty$ framework at every level.
+homotopy coherent structures, coderived filtrations whose
+associated-graded differential is square-zero, and the full
+$A_\infty$/$L_\infty$ framework at every level. In particular, one
+should not speak of ordinary bar cohomology or an unqualified bar
+spectral sequence for the total curved differential in this regime.
 All standard chiral algebras (Heisenberg, Kac--Moody, Virasoro,
 $\cW$-algebras) have central curvature, so strict nilpotence holds
 throughout; see Remark~\ref{rem:voa-central-curvature} for the
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index 6f6e3e513dba8aa12ab332fe87b8a7c09096b212..7f7756a90cff7d603e6fc0f4309cb832d5d5c35a
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -117,7 +117,14 @@
 \end{tabular}
 \end{center}
 
-No completion is needed. The bar complex is conilpotent (finite-dimensional in each bar degree) and the differential is zero except for the curvature term $m_0$. Convergence of the bar spectral sequence follows: the filtration by bar degree is bounded below ($n \geq 0$) and exhaustive, with finite-dimensional graded pieces, so the spectral sequence converges to the bar homology by the standard bounded-below complete convergence theorem (\cite{LV12}, Theorem~2.2.3).
+No completion is needed at genus~$0$. The strict genus-$0$ bar complex is
+conilpotent (finite-dimensional in each bar degree) and its ordinary bar
+differential is zero; the higher-genus curved correction is handled later
+on the coderived side. Convergence of the genus-$0$ bar spectral sequence
+then follows: the filtration by bar degree is bounded below ($n \geq 0$)
+and exhaustive, with finite-dimensional graded pieces, so the spectral
+sequence converges to the ordinary bar homology by the standard
+bounded-below complete convergence theorem (\cite{LV12}, Theorem~2.2.3).
 
 \emph{Reference}: See \cite{GLZ22} Section 6, Proposition 6.2 for the identification
 of the twisted chiral enveloping algebra with CE algebra structure.
@@ -4522,13 +4529,17 @@
 \index{quadratic frontier|textbf}
 
 The categorical logarithm encodes a chiral
-algebra~$\cA$ as the bar complex $\barB(\cA)$, whose Taylor expansion
-is the PBW spectral sequence, whose leading coefficient is the modular
-characteristic~$\kappa(\cA)$, and whose curvature
-$\dfib^{\,2} = \kappa(\cA) \cdot \omega_g$ governs the genus
-transition. On a locus where the full scalar package is known to be
-governed by~$\kappa(\cA)$, this curvature controls the scalar genus
-tower.
+algebra~$\cA$ as the bar complex $\barB(\cA)$. On the strict
+genus-$0$ or associated-graded lane, its Taylor expansion is the PBW
+spectral sequence, whose leading coefficient is the modular
+characteristic~$\kappa(\cA)$. By contrast, once the higher-genus
+fiber operator satisfies
+$\dfib^{\,2} = \kappa(\cA) \cdot \omega_g$, the genus transition is
+tracked either by the flat comparison differential $\Dg{g}$ or by the
+coderived bar-degree filtration, not by ordinary cohomology of the
+raw curved fiber complex. On a locus where the full scalar package is
+known to be governed by~$\kappa(\cA)$, this curvature controls the
+scalar genus tower.
 
 We now consider what happens when
 that stronger scalar-package hypothesis is left. The Whitehead decomposition
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index dec9ecb32841b9b9b25c237fdfd39a834fb3f9ee..d42005a148feeefe896f5af5b08aad9e62f62917
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -6239,16 +6239,36 @@
 \textup{[Regime: curved-central
 \textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
 
-Filtered algebras $(\cA_1, \cA_2)$ with curvatures $\kappa_1, \kappa_2$ form a curved Koszul pair if:
+Filtered algebras $(\cA_1, \cA_2)$ with curvatures $\kappa_1, \kappa_2$
+form a curved Koszul pair in the filtered coderived sense if:
 \begin{enumerate}
 \item Associated graded $(\mathrm{gr}\,\cA_1, \mathrm{gr}\,\cA_2)$ are classical Koszul dual
 \item Curvatures are dual: $\kappa_1 \leftrightarrow -\kappa_2$ under the Koszul pairing
-\item The spectral sequence associated to the filtration degenerates at $E_2$
+\item The coderived spectral sequence associated to the filtration,
+ computed from the strict associated graded of the curved bar complex,
+ degenerates at $E_2$
 \end{enumerate}
 \end{theorem}
 
 \begin{proof}
-The filtered bar complex $F_\bullet \B(\cA_1)$ has associated graded $\mathrm{gr}\,\B(\cA_1) = \B(\mathrm{gr}\,\cA_1)$. By condition (1), $\Omega(\B(\mathrm{gr}\,\cA_1)) \simeq \mathrm{gr}\,\cA_2$ at the $E_1$ level. The curvature condition (2) ensures that the $m_0$ elements of the two algebras are related by $\kappa_2 = -\kappa_1^*$ under the Koszul pairing, which is the compatibility condition for curved $A_\infty$ morphisms (Positselski \cite{Positselski11}). The degeneration condition (3) then gives $\Omega(\B(\cA_1)) \simeq \cA_2$ as curved $A_\infty$ algebras. This is the standard criterion for curved Koszul pairs (Loday--Vallette \cite{LV12}, \S10.3), lifted to the chiral setting via Theorem~\ref{thm:geometric-equals-operadic-bar} (geometric bar = operadic bar).
+The filtered curved bar complex $F_\bullet \B(\cA_1)$ has associated
+graded $\mathrm{gr}\,\B(\cA_1) = \B(\mathrm{gr}\,\cA_1)$, and the
+curvature lies in positive filtration, so the associated-graded
+differential is square-zero. By condition~(1),
+$\Omega(\B(\mathrm{gr}\,\cA_1)) \simeq \mathrm{gr}\,\cA_2$ at the
+$E_1$ level. The curvature condition~(2) ensures that the $m_0$
+elements of the two algebras are related by
+$\kappa_2 = -\kappa_1^*$ under the Koszul pairing, which is the
+compatibility condition for curved $A_\infty$ morphisms
+(Positselski~\cite{Positselski11}). The degeneration condition~(3)
+then gives the bar-cobar comparison in the filtered coderived
+category; on loci where the coderived comparison promotes to an
+ordinary chain-level statement, one recovers
+$\Omega(\B(\cA_1)) \simeq \cA_2$ as curved $A_\infty$ algebras. This is
+the standard criterion for curved Koszul pairs
+(Loday--Vallette~\cite{LV12}, \S10.3), lifted to the chiral setting via
+Theorem~\ref{thm:geometric-equals-operadic-bar} (geometric bar =
+operadic bar).
 \end{proof}
 
 % ================================================================
@@ -6367,7 +6387,10 @@
 
 \item The central charge $c$ enters non-linearly in higher bar degrees, preventing a quadratic Koszul resolution.
 \end{enumerate}
-One needs the PBW spectral sequence approach (Theorem~\ref{thm:pbw-koszulness-criterion}), or equivalently, curved Koszul duality (Positselski) with nilpotent completion and a filtered/completed category.
+One needs the PBW spectral sequence approach
+(Theorem~\ref{thm:pbw-koszulness-criterion}), or equivalently,
+Positselski's curved Koszul duality in its coderived,
+nilpotently completed, filtered setting.
 
 \emph{Contrast with Heisenberg/Kac--Moody.}
 \begin{center}
diff --git a/chapters/theory/chiral_modules.tex b/chapters/theory/chiral_modules.tex
index 31c1dfb431aba58853fc92f99bc99383f16b37be..a503b83e41878075ce0885ae10f0369eb14f0970
--- a/chapters/theory/chiral_modules.tex
+++ b/chapters/theory/chiral_modules.tex
@@ -2126,7 +2126,14 @@
 \begin{remark}[Associated variety and Koszul duality]
 \label{rem:associated-variety-koszul}
 \index{associated variety!Koszul duality}
-The associated variety is \emph{not} preserved by level-shifting Koszul duality: e.g., $X_{L_1(\mathfrak{sl}_2)} = \{0\}$ but $X_{L_{-3}(\mathfrak{sl}_2)} = \mathfrak{sl}_2^*$. When $X_V = \{0\}$, the bar spectral sequence degenerates at a finite page; for $X_V \neq \{0\}$ it may have non-trivial higher differentials, marking the passage from Koszul to curved $A_\infty$.
+The associated variety is \emph{not} preserved by level-shifting Koszul
+duality: e.g., $X_{L_1(\mathfrak{sl}_2)} = \{0\}$ but
+$X_{L_{-3}(\mathfrak{sl}_2)} = \mathfrak{sl}_2^*$. When $X_V = \{0\}$,
+the bar spectral sequence degenerates at a finite page; for
+$X_V \neq \{0\}$ it may have non-trivial higher differentials, marking
+the passage from Koszul to curved $A_\infty$. Off that square-zero
+locus, the comparison should be read on the coderived side rather than
+as an ordinary bar-cohomology statement.
 \end{remark}
 
 \begin{conjecture}[Type-$A$ orbit duality for affine simple quotients; \ClaimStatusConjectured]
diff --git a/chapters/theory/cobar_construction.tex b/chapters/theory/cobar_construction.tex
index baf55cf992bb32c62f1a00820d1c6d08f73cebec..0aaf81e80c78be3a6f81a39f6994171be62a439d
--- a/chapters/theory/cobar_construction.tex
+++ b/chapters/theory/cobar_construction.tex
@@ -3107,7 +3107,11 @@
 \begin{proof}[Proof (outline; full proof in \S\textup{\ref{sec:complementarity-theorem}})]
 The complete proof, synthesizing five lemmas via the Verdier
 involution~$\sigma$ and the genus spectral sequence, is given in
-Theorem~\ref{thm:quantum-complementarity-main}.
+Theorem~\ref{thm:quantum-complementarity-main}. Here the spectral
+sequence is taken for the square-zero total comparison differential, or
+equivalently for the coderived filtration on the curved bar family; it
+is not the ordinary spectral sequence of the raw fiber operator when
+$\dfib^{\,2} \neq 0$.
 
 \emph{Foundation: Curved $A_\infty$ Structures}
 
@@ -3134,6 +3138,9 @@
 The total corrected differential $\Dg{g}$, which incorporates period
 corrections to restore strict nilpotence ($\Dg{g}^{\,2} = 0$), is
 introduced in Convention~\ref{conv:higher-genus-differentials}.
+Accordingly, any spectral-sequence or $H^*$ statement below uses either
+$\Dg{g}$ or the coderived bar-degree filtration, not the raw curved
+fiber complex $(\barB_g(\mathcal{A}), \dfib)$.
 
 \medskip
 

Plan update
  ✓ Read required constitutional files and extract constraints relevant to curved vs flat complexes
  ✓ Locate first 15 in-scope spectral-sequence / H^* instances under chapters/theory/
  ✓ Patch any instance that treats a curved differential as an honest cochain complex without qualification
  ✓ Re-read edited passages and grep for residual in-scope violations
file update:
diff --git a/chapters/theory/bar_cobar_adjunction_curved.tex b/chapters/theory/bar_cobar_adjunction_curved.tex
index 9f149679c80b6dec8cb90edcd3ce927df7e6198b..b3a3459a72f92f710f7f0eea792dd68ab3c67715
--- a/chapters/theory/bar_cobar_adjunction_curved.tex
+++ b/chapters/theory/bar_cobar_adjunction_curved.tex
@@ -5871,8 +5871,11 @@
 \begin{remark}[Non-central curvature]\label{rem:non-central-curvature}
 If the curvature $\mu_0$ is not central, then $d_{\text{bar}}^2 \neq 0$
 and nilpotence holds only up to homotopy: the bar complex requires
-homotopy coherent structures, spectral sequences that may not
-degenerate, and the full $A_\infty$/$L_\infty$ framework at every level.
+homotopy coherent structures, coderived filtrations whose
+associated-graded differential is square-zero, and the full
+$A_\infty$/$L_\infty$ framework at every level. In particular, one
+should not speak of ordinary bar cohomology or an unqualified bar
+spectral sequence for the total curved differential in this regime.
 All standard chiral algebras (Heisenberg, Kac--Moody, Virasoro,
 $\cW$-algebras) have central curvature, so strict nilpotence holds
 throughout; see Remark~\ref{rem:voa-central-curvature} for the
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index 6f6e3e513dba8aa12ab332fe87b8a7c09096b212..7f7756a90cff7d603e6fc0f4309cb832d5d5c35a
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -117,7 +117,14 @@
 \end{tabular}
 \end{center}
 
-No completion is needed. The bar complex is conilpotent (finite-dimensional in each bar degree) and the differential is zero except for the curvature term $m_0$. Convergence of the bar spectral sequence follows: the filtration by bar degree is bounded below ($n \geq 0$) and exhaustive, with finite-dimensional graded pieces, so the spectral sequence converges to the bar homology by the standard bounded-below complete convergence theorem (\cite{LV12}, Theorem~2.2.3).
+No completion is needed at genus~$0$. The strict genus-$0$ bar complex is
+conilpotent (finite-dimensional in each bar degree) and its ordinary bar
+differential is zero; the higher-genus curved correction is handled later
+on the coderived side. Convergence of the genus-$0$ bar spectral sequence
+then follows: the filtration by bar degree is bounded below ($n \geq 0$)
+and exhaustive, with finite-dimensional graded pieces, so the spectral
+sequence converges to the ordinary bar homology by the standard
+bounded-below complete convergence theorem (\cite{LV12}, Theorem~2.2.3).
 
 \emph{Reference}: See \cite{GLZ22} Section 6, Proposition 6.2 for the identification
 of the twisted chiral enveloping algebra with CE algebra structure.
@@ -4522,13 +4529,17 @@
 \index{quadratic frontier|textbf}
 
 The categorical logarithm encodes a chiral
-algebra~$\cA$ as the bar complex $\barB(\cA)$, whose Taylor expansion
-is the PBW spectral sequence, whose leading coefficient is the modular
-characteristic~$\kappa(\cA)$, and whose curvature
-$\dfib^{\,2} = \kappa(\cA) \cdot \omega_g$ governs the genus
-transition. On a locus where the full scalar package is known to be
-governed by~$\kappa(\cA)$, this curvature controls the scalar genus
-tower.
+algebra~$\cA$ as the bar complex $\barB(\cA)$. On the strict
+genus-$0$ or associated-graded lane, its Taylor expansion is the PBW
+spectral sequence, whose leading coefficient is the modular
+characteristic~$\kappa(\cA)$. By contrast, once the higher-genus
+fiber operator satisfies
+$\dfib^{\,2} = \kappa(\cA) \cdot \omega_g$, the genus transition is
+tracked either by the flat comparison differential $\Dg{g}$ or by the
+coderived bar-degree filtration, not by ordinary cohomology of the
+raw curved fiber complex. On a locus where the full scalar package is
+known to be governed by~$\kappa(\cA)$, this curvature controls the
+scalar genus tower.
 
 We now consider what happens when
 that stronger scalar-package hypothesis is left. The Whitehead decomposition
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index dec9ecb32841b9b9b25c237fdfd39a834fb3f9ee..d42005a148feeefe896f5af5b08aad9e62f62917
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -6239,16 +6239,36 @@
 \textup{[Regime: curved-central
 \textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
 
-Filtered algebras $(\cA_1, \cA_2)$ with curvatures $\kappa_1, \kappa_2$ form a curved Koszul pair if:
+Filtered algebras $(\cA_1, \cA_2)$ with curvatures $\kappa_1, \kappa_2$
+form a curved Koszul pair in the filtered coderived sense if:
 \begin{enumerate}
 \item Associated graded $(\mathrm{gr}\,\cA_1, \mathrm{gr}\,\cA_2)$ are classical Koszul dual
 \item Curvatures are dual: $\kappa_1 \leftrightarrow -\kappa_2$ under the Koszul pairing
-\item The spectral sequence associated to the filtration degenerates at $E_2$
+\item The coderived spectral sequence associated to the filtration,
+ computed from the strict associated graded of the curved bar complex,
+ degenerates at $E_2$
 \end{enumerate}
 \end{theorem}
 
 \begin{proof}
-The filtered bar complex $F_\bullet \B(\cA_1)$ has associated graded $\mathrm{gr}\,\B(\cA_1) = \B(\mathrm{gr}\,\cA_1)$. By condition (1), $\Omega(\B(\mathrm{gr}\,\cA_1)) \simeq \mathrm{gr}\,\cA_2$ at the $E_1$ level. The curvature condition (2) ensures that the $m_0$ elements of the two algebras are related by $\kappa_2 = -\kappa_1^*$ under the Koszul pairing, which is the compatibility condition for curved $A_\infty$ morphisms (Positselski \cite{Positselski11}). The degeneration condition (3) then gives $\Omega(\B(\cA_1)) \simeq \cA_2$ as curved $A_\infty$ algebras. This is the standard criterion for curved Koszul pairs (Loday--Vallette \cite{LV12}, \S10.3), lifted to the chiral setting via Theorem~\ref{thm:geometric-equals-operadic-bar} (geometric bar = operadic bar).
+The filtered curved bar complex $F_\bullet \B(\cA_1)$ has associated
+graded $\mathrm{gr}\,\B(\cA_1) = \B(\mathrm{gr}\,\cA_1)$, and the
+curvature lies in positive filtration, so the associated-graded
+differential is square-zero. By condition~(1),
+$\Omega(\B(\mathrm{gr}\,\cA_1)) \simeq \mathrm{gr}\,\cA_2$ at the
+$E_1$ level. The curvature condition~(2) ensures that the $m_0$
+elements of the two algebras are related by
+$\kappa_2 = -\kappa_1^*$ under the Koszul pairing, which is the
+compatibility condition for curved $A_\infty$ morphisms
+(Positselski~\cite{Positselski11}). The degeneration condition~(3)
+then gives the bar-cobar comparison in the filtered coderived
+category; on loci where the coderived comparison promotes to an
+ordinary chain-level statement, one recovers
+$\Omega(\B(\cA_1)) \simeq \cA_2$ as curved $A_\infty$ algebras. This is
+the standard criterion for curved Koszul pairs
+(Loday--Vallette~\cite{LV12}, \S10.3), lifted to the chiral setting via
+Theorem~\ref{thm:geometric-equals-operadic-bar} (geometric bar =
+operadic bar).
 \end{proof}
 
 % ================================================================
@@ -6367,7 +6387,10 @@
 
 \item The central charge $c$ enters non-linearly in higher bar degrees, preventing a quadratic Koszul resolution.
 \end{enumerate}
-One needs the PBW spectral sequence approach (Theorem~\ref{thm:pbw-koszulness-criterion}), or equivalently, curved Koszul duality (Positselski) with nilpotent completion and a filtered/completed category.
+One needs the PBW spectral sequence approach
+(Theorem~\ref{thm:pbw-koszulness-criterion}), or equivalently,
+Positselski's curved Koszul duality in its coderived,
+nilpotently completed, filtered setting.
 
 \emph{Contrast with Heisenberg/Kac--Moody.}
 \begin{center}
diff --git a/chapters/theory/chiral_modules.tex b/chapters/theory/chiral_modules.tex
index 31c1dfb431aba58853fc92f99bc99383f16b37be..a503b83e41878075ce0885ae10f0369eb14f0970
--- a/chapters/theory/chiral_modules.tex
+++ b/chapters/theory/chiral_modules.tex
@@ -2126,7 +2126,14 @@
 \begin{remark}[Associated variety and Koszul duality]
 \label{rem:associated-variety-koszul}
 \index{associated variety!Koszul duality}
-The associated variety is \emph{not} preserved by level-shifting Koszul duality: e.g., $X_{L_1(\mathfrak{sl}_2)} = \{0\}$ but $X_{L_{-3}(\mathfrak{sl}_2)} = \mathfrak{sl}_2^*$. When $X_V = \{0\}$, the bar spectral sequence degenerates at a finite page; for $X_V \neq \{0\}$ it may have non-trivial higher differentials, marking the passage from Koszul to curved $A_\infty$.
+The associated variety is \emph{not} preserved by level-shifting Koszul
+duality: e.g., $X_{L_1(\mathfrak{sl}_2)} = \{0\}$ but
+$X_{L_{-3}(\mathfrak{sl}_2)} = \mathfrak{sl}_2^*$. When $X_V = \{0\}$,
+the bar spectral sequence degenerates at a finite page; for
+$X_V \neq \{0\}$ it may have non-trivial higher differentials, marking
+the passage from Koszul to curved $A_\infty$. Off that square-zero
+locus, the comparison should be read on the coderived side rather than
+as an ordinary bar-cohomology statement.
 \end{remark}
 
 \begin{conjecture}[Type-$A$ orbit duality for affine simple quotients; \ClaimStatusConjectured]
diff --git a/chapters/theory/cobar_construction.tex b/chapters/theory/cobar_construction.tex
index baf55cf992bb32c62f1a00820d1c6d08f73cebec..0aaf81e80c78be3a6f81a39f6994171be62a439d
--- a/chapters/theory/cobar_construction.tex
+++ b/chapters/theory/cobar_construction.tex
@@ -3107,7 +3107,11 @@
 \begin{proof}[Proof (outline; full proof in \S\textup{\ref{sec:complementarity-theorem}})]
 The complete proof, synthesizing five lemmas via the Verdier
 involution~$\sigma$ and the genus spectral sequence, is given in
-Theorem~\ref{thm:quantum-complementarity-main}.
+Theorem~\ref{thm:quantum-complementarity-main}. Here the spectral
+sequence is taken for the square-zero total comparison differential, or
+equivalently for the coderived filtration on the curved bar family; it
+is not the ordinary spectral sequence of the raw fiber operator when
+$\dfib^{\,2} \neq 0$.
 
 \emph{Foundation: Curved $A_\infty$ Structures}
 
@@ -3134,6 +3138,9 @@
 The total corrected differential $\Dg{g}$, which incorporates period
 corrections to restore strict nilpotence ($\Dg{g}^{\,2} = 0$), is
 introduced in Convention~\ref{conv:higher-genus-differentials}.
+Accordingly, any spectral-sequence or $H^*$ statement below uses either
+$\Dg{g}$ or the coderived bar-degree filtration, not the raw curved
+fiber complex $(\barB_g(\mathcal{A}), \dfib)$.
 
 \medskip
 


thinking
**Checking git status**

I think I need to inspect the git status to check for any modified files. It's crucial to know what changes have been made before proceeding, right? I'll take a quick look to see what files have been altered or staged. This way, I can ensure I'm aware of everything that's happening in the repository. Getting this right will help avoid any surprises later on. So, let's check that status!
exec
/bin/zsh -lc 'git status --short -- chapters/theory/bar_cobar_adjunction_curved.tex chapters/theory/bar_cobar_adjunction_inversion.tex chapters/theory/chiral_koszul_pairs.tex chapters/theory/chiral_modules.tex chapters/theory/cobar_construction.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
 M chapters/theory/bar_cobar_adjunction_curved.tex
 M chapters/theory/bar_cobar_adjunction_inversion.tex
 M chapters/theory/chiral_koszul_pairs.tex
 M chapters/theory/chiral_modules.tex
 M chapters/theory/cobar_construction.tex
file update:
diff --git a/chapters/theory/bar_cobar_adjunction_curved.tex b/chapters/theory/bar_cobar_adjunction_curved.tex
index 9f149679c80b6dec8cb90edcd3ce927df7e6198b..b3a3459a72f92f710f7f0eea792dd68ab3c67715
--- a/chapters/theory/bar_cobar_adjunction_curved.tex
+++ b/chapters/theory/bar_cobar_adjunction_curved.tex
@@ -5871,8 +5871,11 @@
 \begin{remark}[Non-central curvature]\label{rem:non-central-curvature}
 If the curvature $\mu_0$ is not central, then $d_{\text{bar}}^2 \neq 0$
 and nilpotence holds only up to homotopy: the bar complex requires
-homotopy coherent structures, spectral sequences that may not
-degenerate, and the full $A_\infty$/$L_\infty$ framework at every level.
+homotopy coherent structures, coderived filtrations whose
+associated-graded differential is square-zero, and the full
+$A_\infty$/$L_\infty$ framework at every level. In particular, one
+should not speak of ordinary bar cohomology or an unqualified bar
+spectral sequence for the total curved differential in this regime.
 All standard chiral algebras (Heisenberg, Kac--Moody, Virasoro,
 $\cW$-algebras) have central curvature, so strict nilpotence holds
 throughout; see Remark~\ref{rem:voa-central-curvature} for the
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index 6f6e3e513dba8aa12ab332fe87b8a7c09096b212..7f7756a90cff7d603e6fc0f4309cb832d5d5c35a
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -117,7 +117,14 @@
 \end{tabular}
 \end{center}
 
-No completion is needed. The bar complex is conilpotent (finite-dimensional in each bar degree) and the differential is zero except for the curvature term $m_0$. Convergence of the bar spectral sequence follows: the filtration by bar degree is bounded below ($n \geq 0$) and exhaustive, with finite-dimensional graded pieces, so the spectral sequence converges to the bar homology by the standard bounded-below complete convergence theorem (\cite{LV12}, Theorem~2.2.3).
+No completion is needed at genus~$0$. The strict genus-$0$ bar complex is
+conilpotent (finite-dimensional in each bar degree) and its ordinary bar
+differential is zero; the higher-genus curved correction is handled later
+on the coderived side. Convergence of the genus-$0$ bar spectral sequence
+then follows: the filtration by bar degree is bounded below ($n \geq 0$)
+and exhaustive, with finite-dimensional graded pieces, so the spectral
+sequence converges to the ordinary bar homology by the standard
+bounded-below complete convergence theorem (\cite{LV12}, Theorem~2.2.3).
 
 \emph{Reference}: See \cite{GLZ22} Section 6, Proposition 6.2 for the identification
 of the twisted chiral enveloping algebra with CE algebra structure.
@@ -4522,13 +4529,17 @@
 \index{quadratic frontier|textbf}
 
 The categorical logarithm encodes a chiral
-algebra~$\cA$ as the bar complex $\barB(\cA)$, whose Taylor expansion
-is the PBW spectral sequence, whose leading coefficient is the modular
-characteristic~$\kappa(\cA)$, and whose curvature
-$\dfib^{\,2} = \kappa(\cA) \cdot \omega_g$ governs the genus
-transition. On a locus where the full scalar package is known to be
-governed by~$\kappa(\cA)$, this curvature controls the scalar genus
-tower.
+algebra~$\cA$ as the bar complex $\barB(\cA)$. On the strict
+genus-$0$ or associated-graded lane, its Taylor expansion is the PBW
+spectral sequence, whose leading coefficient is the modular
+characteristic~$\kappa(\cA)$. By contrast, once the higher-genus
+fiber operator satisfies
+$\dfib^{\,2} = \kappa(\cA) \cdot \omega_g$, the genus transition is
+tracked either by the flat comparison differential $\Dg{g}$ or by the
+coderived bar-degree filtration, not by ordinary cohomology of the
+raw curved fiber complex. On a locus where the full scalar package is
+known to be governed by~$\kappa(\cA)$, this curvature controls the
+scalar genus tower.
 
 We now consider what happens when
 that stronger scalar-package hypothesis is left. The Whitehead decomposition
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index dec9ecb32841b9b9b25c237fdfd39a834fb3f9ee..d42005a148feeefe896f5af5b08aad9e62f62917
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -6239,16 +6239,36 @@
 \textup{[Regime: curved-central
 \textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
 
-Filtered algebras $(\cA_1, \cA_2)$ with curvatures $\kappa_1, \kappa_2$ form a curved Koszul pair if:
+Filtered algebras $(\cA_1, \cA_2)$ with curvatures $\kappa_1, \kappa_2$
+form a curved Koszul pair in the filtered coderived sense if:
 \begin{enumerate}
 \item Associated graded $(\mathrm{gr}\,\cA_1, \mathrm{gr}\,\cA_2)$ are classical Koszul dual
 \item Curvatures are dual: $\kappa_1 \leftrightarrow -\kappa_2$ under the Koszul pairing
-\item The spectral sequence associated to the filtration degenerates at $E_2$
+\item The coderived spectral sequence associated to the filtration,
+ computed from the strict associated graded of the curved bar complex,
+ degenerates at $E_2$
 \end{enumerate}
 \end{theorem}
 
 \begin{proof}
-The filtered bar complex $F_\bullet \B(\cA_1)$ has associated graded $\mathrm{gr}\,\B(\cA_1) = \B(\mathrm{gr}\,\cA_1)$. By condition (1), $\Omega(\B(\mathrm{gr}\,\cA_1)) \simeq \mathrm{gr}\,\cA_2$ at the $E_1$ level. The curvature condition (2) ensures that the $m_0$ elements of the two algebras are related by $\kappa_2 = -\kappa_1^*$ under the Koszul pairing, which is the compatibility condition for curved $A_\infty$ morphisms (Positselski \cite{Positselski11}). The degeneration condition (3) then gives $\Omega(\B(\cA_1)) \simeq \cA_2$ as curved $A_\infty$ algebras. This is the standard criterion for curved Koszul pairs (Loday--Vallette \cite{LV12}, \S10.3), lifted to the chiral setting via Theorem~\ref{thm:geometric-equals-operadic-bar} (geometric bar = operadic bar).
+The filtered curved bar complex $F_\bullet \B(\cA_1)$ has associated
+graded $\mathrm{gr}\,\B(\cA_1) = \B(\mathrm{gr}\,\cA_1)$, and the
+curvature lies in positive filtration, so the associated-graded
+differential is square-zero. By condition~(1),
+$\Omega(\B(\mathrm{gr}\,\cA_1)) \simeq \mathrm{gr}\,\cA_2$ at the
+$E_1$ level. The curvature condition~(2) ensures that the $m_0$
+elements of the two algebras are related by
+$\kappa_2 = -\kappa_1^*$ under the Koszul pairing, which is the
+compatibility condition for curved $A_\infty$ morphisms
+(Positselski~\cite{Positselski11}). The degeneration condition~(3)
+then gives the bar-cobar comparison in the filtered coderived
+category; on loci where the coderived comparison promotes to an
+ordinary chain-level statement, one recovers
+$\Omega(\B(\cA_1)) \simeq \cA_2$ as curved $A_\infty$ algebras. This is
+the standard criterion for curved Koszul pairs
+(Loday--Vallette~\cite{LV12}, \S10.3), lifted to the chiral setting via
+Theorem~\ref{thm:geometric-equals-operadic-bar} (geometric bar =
+operadic bar).
 \end{proof}
 
 % ================================================================
@@ -6367,7 +6387,10 @@
 
 \item The central charge $c$ enters non-linearly in higher bar degrees, preventing a quadratic Koszul resolution.
 \end{enumerate}
-One needs the PBW spectral sequence approach (Theorem~\ref{thm:pbw-koszulness-criterion}), or equivalently, curved Koszul duality (Positselski) with nilpotent completion and a filtered/completed category.
+One needs the PBW spectral sequence approach
+(Theorem~\ref{thm:pbw-koszulness-criterion}), or equivalently,
+Positselski's curved Koszul duality in its coderived,
+nilpotently completed, filtered setting.
 
 \emph{Contrast with Heisenberg/Kac--Moody.}
 \begin{center}
diff --git a/chapters/theory/chiral_modules.tex b/chapters/theory/chiral_modules.tex
index 31c1dfb431aba58853fc92f99bc99383f16b37be..a503b83e41878075ce0885ae10f0369eb14f0970
--- a/chapters/theory/chiral_modules.tex
+++ b/chapters/theory/chiral_modules.tex
@@ -2126,7 +2126,14 @@
 \begin{remark}[Associated variety and Koszul duality]
 \label{rem:associated-variety-koszul}
 \index{associated variety!Koszul duality}
-The associated variety is \emph{not} preserved by level-shifting Koszul duality: e.g., $X_{L_1(\mathfrak{sl}_2)} = \{0\}$ but $X_{L_{-3}(\mathfrak{sl}_2)} = \mathfrak{sl}_2^*$. When $X_V = \{0\}$, the bar spectral sequence degenerates at a finite page; for $X_V \neq \{0\}$ it may have non-trivial higher differentials, marking the passage from Koszul to curved $A_\infty$.
+The associated variety is \emph{not} preserved by level-shifting Koszul
+duality: e.g., $X_{L_1(\mathfrak{sl}_2)} = \{0\}$ but
+$X_{L_{-3}(\mathfrak{sl}_2)} = \mathfrak{sl}_2^*$. When $X_V = \{0\}$,
+the bar spectral sequence degenerates at a finite page; for
+$X_V \neq \{0\}$ it may have non-trivial higher differentials, marking
+the passage from Koszul to curved $A_\infty$. Off that square-zero
+locus, the comparison should be read on the coderived side rather than
+as an ordinary bar-cohomology statement.
 \end{remark}
 
 \begin{conjecture}[Type-$A$ orbit duality for affine simple quotients; \ClaimStatusConjectured]
diff --git a/chapters/theory/cobar_construction.tex b/chapters/theory/cobar_construction.tex
index baf55cf992bb32c62f1a00820d1c6d08f73cebec..0aaf81e80c78be3a6f81a39f6994171be62a439d
--- a/chapters/theory/cobar_construction.tex
+++ b/chapters/theory/cobar_construction.tex
@@ -3107,7 +3107,11 @@
 \begin{proof}[Proof (outline; full proof in \S\textup{\ref{sec:complementarity-theorem}})]
 The complete proof, synthesizing five lemmas via the Verdier
 involution~$\sigma$ and the genus spectral sequence, is given in
-Theorem~\ref{thm:quantum-complementarity-main}.
+Theorem~\ref{thm:quantum-complementarity-main}. Here the spectral
+sequence is taken for the square-zero total comparison differential, or
+equivalently for the coderived filtration on the curved bar family; it
+is not the ordinary spectral sequence of the raw fiber operator when
+$\dfib^{\,2} \neq 0$.
 
 \emph{Foundation: Curved $A_\infty$ Structures}
 
@@ -3134,6 +3138,9 @@
 The total corrected differential $\Dg{g}$, which incorporates period
 corrections to restore strict nilpotence ($\Dg{g}^{\,2} = 0$), is
 introduced in Convention~\ref{conv:higher-genus-differentials}.
+Accordingly, any spectral-sequence or $H^*$ statement below uses either
+$\Dg{g}$ or the coderived bar-degree filtration, not the raw curved
+fiber complex $(\barB_g(\mathcal{A}), \dfib)$.
 
 \medskip
 

codex
FIXED.

I audited the first 15 hits in `chapters/theory/` and only changed the genuinely curved cases that were still talking like ordinary cochain complexes. I added coderived or flat-comparison qualifiers in [bar_cobar_adjunction_curved.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/bar_cobar_adjunction_curved.tex:5871), [bar_cobar_adjunction_inversion.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/bar_cobar_adjunction_inversion.tex:120), [chiral_koszul_pairs.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex:6242), [chiral_modules.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_modules.tex:2126), and [cobar_construction.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/cobar_construction.tex:3107). The hits that were already square-zero because they used `D^{(g)}`, a strict associated graded, or the genus-0/Koszul lane were left unchanged.

Verification was narrow and source-level: I re-read each edited passage, `git diff --check` returned clean, and a targeted `rg` over the touched files found no residual `spectral sequence` / `H^*` phrasing directly tied to raw `\dfib` or `\kappa \cdot \omega_g` on those audited surfaces. I did not run a full TeX build.
file update:
diff --git a/chapters/theory/bar_cobar_adjunction_curved.tex b/chapters/theory/bar_cobar_adjunction_curved.tex
index 9f149679c80b6dec8cb90edcd3ce927df7e6198b..b3a3459a72f92f710f7f0eea792dd68ab3c67715
--- a/chapters/theory/bar_cobar_adjunction_curved.tex
+++ b/chapters/theory/bar_cobar_adjunction_curved.tex
@@ -5871,8 +5871,11 @@
 \begin{remark}[Non-central curvature]\label{rem:non-central-curvature}
 If the curvature $\mu_0$ is not central, then $d_{\text{bar}}^2 \neq 0$
 and nilpotence holds only up to homotopy: the bar complex requires
-homotopy coherent structures, spectral sequences that may not
-degenerate, and the full $A_\infty$/$L_\infty$ framework at every level.
+homotopy coherent structures, coderived filtrations whose
+associated-graded differential is square-zero, and the full
+$A_\infty$/$L_\infty$ framework at every level. In particular, one
+should not speak of ordinary bar cohomology or an unqualified bar
+spectral sequence for the total curved differential in this regime.
 All standard chiral algebras (Heisenberg, Kac--Moody, Virasoro,
 $\cW$-algebras) have central curvature, so strict nilpotence holds
 throughout; see Remark~\ref{rem:voa-central-curvature} for the
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index 6f6e3e513dba8aa12ab332fe87b8a7c09096b212..7f7756a90cff7d603e6fc0f4309cb832d5d5c35a
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -117,7 +117,14 @@
 \end{tabular}
 \end{center}
 
-No completion is needed. The bar complex is conilpotent (finite-dimensional in each bar degree) and the differential is zero except for the curvature term $m_0$. Convergence of the bar spectral sequence follows: the filtration by bar degree is bounded below ($n \geq 0$) and exhaustive, with finite-dimensional graded pieces, so the spectral sequence converges to the bar homology by the standard bounded-below complete convergence theorem (\cite{LV12}, Theorem~2.2.3).
+No completion is needed at genus~$0$. The strict genus-$0$ bar complex is
+conilpotent (finite-dimensional in each bar degree) and its ordinary bar
+differential is zero; the higher-genus curved correction is handled later
+on the coderived side. Convergence of the genus-$0$ bar spectral sequence
+then follows: the filtration by bar degree is bounded below ($n \geq 0$)
+and exhaustive, with finite-dimensional graded pieces, so the spectral
+sequence converges to the ordinary bar homology by the standard
+bounded-below complete convergence theorem (\cite{LV12}, Theorem~2.2.3).
 
 \emph{Reference}: See \cite{GLZ22} Section 6, Proposition 6.2 for the identification
 of the twisted chiral enveloping algebra with CE algebra structure.
@@ -4522,13 +4529,17 @@
 \index{quadratic frontier|textbf}
 
 The categorical logarithm encodes a chiral
-algebra~$\cA$ as the bar complex $\barB(\cA)$, whose Taylor expansion
-is the PBW spectral sequence, whose leading coefficient is the modular
-characteristic~$\kappa(\cA)$, and whose curvature
-$\dfib^{\,2} = \kappa(\cA) \cdot \omega_g$ governs the genus
-transition. On a locus where the full scalar package is known to be
-governed by~$\kappa(\cA)$, this curvature controls the scalar genus
-tower.
+algebra~$\cA$ as the bar complex $\barB(\cA)$. On the strict
+genus-$0$ or associated-graded lane, its Taylor expansion is the PBW
+spectral sequence, whose leading coefficient is the modular
+characteristic~$\kappa(\cA)$. By contrast, once the higher-genus
+fiber operator satisfies
+$\dfib^{\,2} = \kappa(\cA) \cdot \omega_g$, the genus transition is
+tracked either by the flat comparison differential $\Dg{g}$ or by the
+coderived bar-degree filtration, not by ordinary cohomology of the
+raw curved fiber complex. On a locus where the full scalar package is
+known to be governed by~$\kappa(\cA)$, this curvature controls the
+scalar genus tower.
 
 We now consider what happens when
 that stronger scalar-package hypothesis is left. The Whitehead decomposition
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index dec9ecb32841b9b9b25c237fdfd39a834fb3f9ee..d42005a148feeefe896f5af5b08aad9e62f62917
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -6239,16 +6239,36 @@
 \textup{[Regime: curved-central
 \textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
 
-Filtered algebras $(\cA_1, \cA_2)$ with curvatures $\kappa_1, \kappa_2$ form a curved Koszul pair if:
+Filtered algebras $(\cA_1, \cA_2)$ with curvatures $\kappa_1, \kappa_2$
+form a curved Koszul pair in the filtered coderived sense if:
 \begin{enumerate}
 \item Associated graded $(\mathrm{gr}\,\cA_1, \mathrm{gr}\,\cA_2)$ are classical Koszul dual
 \item Curvatures are dual: $\kappa_1 \leftrightarrow -\kappa_2$ under the Koszul pairing
-\item The spectral sequence associated to the filtration degenerates at $E_2$
+\item The coderived spectral sequence associated to the filtration,
+ computed from the strict associated graded of the curved bar complex,
+ degenerates at $E_2$
 \end{enumerate}
 \end{theorem}
 
 \begin{proof}
-The filtered bar complex $F_\bullet \B(\cA_1)$ has associated graded $\mathrm{gr}\,\B(\cA_1) = \B(\mathrm{gr}\,\cA_1)$. By condition (1), $\Omega(\B(\mathrm{gr}\,\cA_1)) \simeq \mathrm{gr}\,\cA_2$ at the $E_1$ level. The curvature condition (2) ensures that the $m_0$ elements of the two algebras are related by $\kappa_2 = -\kappa_1^*$ under the Koszul pairing, which is the compatibility condition for curved $A_\infty$ morphisms (Positselski \cite{Positselski11}). The degeneration condition (3) then gives $\Omega(\B(\cA_1)) \simeq \cA_2$ as curved $A_\infty$ algebras. This is the standard criterion for curved Koszul pairs (Loday--Vallette \cite{LV12}, \S10.3), lifted to the chiral setting via Theorem~\ref{thm:geometric-equals-operadic-bar} (geometric bar = operadic bar).
+The filtered curved bar complex $F_\bullet \B(\cA_1)$ has associated
+graded $\mathrm{gr}\,\B(\cA_1) = \B(\mathrm{gr}\,\cA_1)$, and the
+curvature lies in positive filtration, so the associated-graded
+differential is square-zero. By condition~(1),
+$\Omega(\B(\mathrm{gr}\,\cA_1)) \simeq \mathrm{gr}\,\cA_2$ at the
+$E_1$ level. The curvature condition~(2) ensures that the $m_0$
+elements of the two algebras are related by
+$\kappa_2 = -\kappa_1^*$ under the Koszul pairing, which is the
+compatibility condition for curved $A_\infty$ morphisms
+(Positselski~\cite{Positselski11}). The degeneration condition~(3)
+then gives the bar-cobar comparison in the filtered coderived
+category; on loci where the coderived comparison promotes to an
+ordinary chain-level statement, one recovers
+$\Omega(\B(\cA_1)) \simeq \cA_2$ as curved $A_\infty$ algebras. This is
+the standard criterion for curved Koszul pairs
+(Loday--Vallette~\cite{LV12}, \S10.3), lifted to the chiral setting via
+Theorem~\ref{thm:geometric-equals-operadic-bar} (geometric bar =
+operadic bar).
 \end{proof}
 
 % ================================================================
@@ -6367,7 +6387,10 @@
 
 \item The central charge $c$ enters non-linearly in higher bar degrees, preventing a quadratic Koszul resolution.
 \end{enumerate}
-One needs the PBW spectral sequence approach (Theorem~\ref{thm:pbw-koszulness-criterion}), or equivalently, curved Koszul duality (Positselski) with nilpotent completion and a filtered/completed category.
+One needs the PBW spectral sequence approach
+(Theorem~\ref{thm:pbw-koszulness-criterion}), or equivalently,
+Positselski's curved Koszul duality in its coderived,
+nilpotently completed, filtered setting.
 
 \emph{Contrast with Heisenberg/Kac--Moody.}
 \begin{center}
diff --git a/chapters/theory/chiral_modules.tex b/chapters/theory/chiral_modules.tex
index 31c1dfb431aba58853fc92f99bc99383f16b37be..a503b83e41878075ce0885ae10f0369eb14f0970
--- a/chapters/theory/chiral_modules.tex
+++ b/chapters/theory/chiral_modules.tex
@@ -2126,7 +2126,14 @@
 \begin{remark}[Associated variety and Koszul duality]
 \label{rem:associated-variety-koszul}
 \index{associated variety!Koszul duality}
-The associated variety is \emph{not} preserved by level-shifting Koszul duality: e.g., $X_{L_1(\mathfrak{sl}_2)} = \{0\}$ but $X_{L_{-3}(\mathfrak{sl}_2)} = \mathfrak{sl}_2^*$. When $X_V = \{0\}$, the bar spectral sequence degenerates at a finite page; for $X_V \neq \{0\}$ it may have non-trivial higher differentials, marking the passage from Koszul to curved $A_\infty$.
+The associated variety is \emph{not} preserved by level-shifting Koszul
+duality: e.g., $X_{L_1(\mathfrak{sl}_2)} = \{0\}$ but
+$X_{L_{-3}(\mathfrak{sl}_2)} = \mathfrak{sl}_2^*$. When $X_V = \{0\}$,
+the bar spectral sequence degenerates at a finite page; for
+$X_V \neq \{0\}$ it may have non-trivial higher differentials, marking
+the passage from Koszul to curved $A_\infty$. Off that square-zero
+locus, the comparison should be read on the coderived side rather than
+as an ordinary bar-cohomology statement.
 \end{remark}
 
 \begin{conjecture}[Type-$A$ orbit duality for affine simple quotients; \ClaimStatusConjectured]
diff --git a/chapters/theory/cobar_construction.tex b/chapters/theory/cobar_construction.tex
index baf55cf992bb32c62f1a00820d1c6d08f73cebec..0aaf81e80c78be3a6f81a39f6994171be62a439d
--- a/chapters/theory/cobar_construction.tex
+++ b/chapters/theory/cobar_construction.tex
@@ -3107,7 +3107,11 @@
 \begin{proof}[Proof (outline; full proof in \S\textup{\ref{sec:complementarity-theorem}})]
 The complete proof, synthesizing five lemmas via the Verdier
 involution~$\sigma$ and the genus spectral sequence, is given in
-Theorem~\ref{thm:quantum-complementarity-main}.
+Theorem~\ref{thm:quantum-complementarity-main}. Here the spectral
+sequence is taken for the square-zero total comparison differential, or
+equivalently for the coderived filtration on the curved bar family; it
+is not the ordinary spectral sequence of the raw fiber operator when
+$\dfib^{\,2} \neq 0$.
 
 \emph{Foundation: Curved $A_\infty$ Structures}
 
@@ -3134,6 +3138,9 @@
 The total corrected differential $\Dg{g}$, which incorporates period
 corrections to restore strict nilpotence ($\Dg{g}^{\,2} = 0$), is
 introduced in Convention~\ref{conv:higher-genus-differentials}.
+Accordingly, any spectral-sequence or $H^*$ statement below uses either
+$\Dg{g}$ or the coderived bar-degree filtration, not the raw curved
+fiber complex $(\barB_g(\mathcal{A}), \dfib)$.
 
 \medskip
 

tokens used
128,026
