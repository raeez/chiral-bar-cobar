# G18_koszul_pairs_viii (410s)

FIXED. I repaired Koszul equivalence `(viii)` in [chiral_koszul_pairs.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex:2075) and synced the local theorem lane at [item `(viii)`](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex:2131), its [proof recap](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex:2210), the [follow-up remark](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex:2383), and the later [summary paragraph](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex:2581). The text now says the proved content is duality plus concentration in degrees `{0,1,2}` plus polynomial Hilbert series, and any free-polynomial cup-product statement is conditional on a Massey-vanishing consequence of Fulton--MacPherson formality.

Verification: I re-read the touched blocks and grepped the file for the old unconditional freeness wording; none remains in the `(viii)` lane. I did not run a full TeX build. There is one unrelated pre-existing `---` hit at [chiral_koszul_pairs.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex:3041), outside this scope.


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
session id: 019d88a1-3982-7891-a552-c01c15cc7e77
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


Fix Koszul equivalence (viii) in chiral_koszul_pairs.tex (AP217).

NARROW SCOPE. Search for 'equiv.*viii' or 'free polynomial'. It should say:
concentration + polynomial Hilbert series (proved); freeness conditional on
Massey vanishing from FM formality. If it claims free polynomial unconditionally, fix.
Search lines 2000-2020.
mcp startup: no servers


thinking
**Considering file exploration options**

I could use an explorer to search and summarize relevant files. The AGENTS suggest reading files on disk, but I wonder if using exec_command and rg might be simpler. The instructions say to always prefer explorers for codebase questions. However, for direct mathematical sources, we might need actual lines. I think using the explorer sub-agent is a solid choice, but I might also need to open files manually to verify results.
thinking
**Evaluating file reading methods**

I think I should spawn the explorer agent for the initial search and pinpoint exact file lines. But I’m also considering using exec_command for mandatory file reads. The instruction to "always prefer" explorers suggests using them if they can handle the task. However, since the user's task requires reading specific files directly, I might need to follow up with exec_command to ensure accuracy. Updating my plan could be helpful, but for this small task, I wonder if it's really necessary.
codex
Using `beilinson-rectify` for a local claim-surface repair. I’m reading the required repo constitution files plus the target section in `chiral_koszul_pairs.tex`, then I’ll patch only the unconditional freeness claim around equivalence `(viii)` and verify with AP greps.
exec
/bin/zsh -lc "sed -n '1,220p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
# Theorem Registry

Auto-generated on 2026-04-13 from the structured claim extractor in `scripts/generate_metadata.py`.

This registry now tracks every `\ClaimStatusProvedHere` block directly from source, so the proved surface cannot silently drift behind the TeX tree.

## Snapshot

| Metric | Value |
|---|---:|
| ProvedHere claims | 2369 |
| Total tagged claims | 3114 |
| Active files in `main.tex` | 90 |
| Total `.tex` files scanned | 104 |

## Status Totals

| Status | Count |
|---|---:|
| `ProvedHere` | 2369 |
 succeeded in 51ms:
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

exec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/beilinson-rectify/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "if [ -f raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,220p' raeeznotes/raeeznotes100/red_team_summary.md; else sed -n '1,220p' archive/raeeznotes/raeeznotes100/red_team_summary.md; fi" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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
codex
I’ve loaded the repo constitution and the rectification workflow. Now I’m isolating the exact theorem/remark lane around equivalence `(viii)`, checking whether the unconditional “free polynomial” wording leaks beyond the proved concentration-plus-polynomial statement.
exec
/bin/zsh -lc "sed -n '1940,2055p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "equiv.*viii|free polynomial|Massey|Hilbert series|equivalence" chapters/theory/chiral_koszul_pairs.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
obstruction at degenerate levels comes from two sources:
\begin{enumerate}[label=\textup{(\roman*)}]
\item \emph{Reduced Li--bar surface.}
 The reduced quotient
 $\mathcal{O}(\overline{\mathbb{O}})=R_{L_k}^{\mathrm{red}}$
 controls only the reduced Li--bar $E_2$ page furnished by
 Theorem~\ref{thm:associated-variety-koszulness}(ii). Any
 diagonal-concentration statement established on that reduced
 surface is therefore evidence only for the reduced quotient,
 not for the full non-reduced algebra~$R_{L_k}$.
\item \emph{Nilradical obstruction.}
 The nilradical $\mathcal{I} = \sqrt{0} \subset R_{L_k}$
 carries additional bar-cohomological data not visible
 on the associated variety~$X_{L_k}$. When
 $\mathcal{I} \neq 0$, the quotient
 $R_{L_k} \twoheadrightarrow
 \mathcal{O}(\overline{\mathbb{O}})$ forgets tensors in the
 bar complex with at least one nilpotent factor. These extra
 summands can support differentials and off-diagonal classes
 invisible on the reduced quotient, so reduced associated-variety
 succeeded in 52ms:
77:Theorem~\ref{thm:koszul-equivalences-meta} assembles twelve
79:unconditional equivalences: $E_2$-collapse of the bar spectral sequence,
142:Kac--Moody (class~$L$, depth~$3$, single Massey product),
337:$\eta_\tau$ is a weak equivalence.
381:If $\eta_\tau\colon \cC \to \bar{B}_X(\cA)$ is a weak equivalence,
420:equivalence of $\eta_\tau$ makes $K_\tau^R$ acyclic. Filter
450: is a weak equivalence of conilpotent complete factorization
459:The equivalence follows the same logical structure as the
477:$\eta_\tau$ being a weak equivalence.
492:shows that the weak equivalence of $\eta_\tau$ forces the
1349:This is the Massey product detecting the off-diagonal class; it is
2065:\label{thm:koszul-equivalences-meta}
2066:\index{Koszul property!equivalences of characterizations|textbf}
2077:polynomial Hilbert series, and $\Etwo$-formality, but it does not
2085:\noindent\textbf{Unconditional equivalences:}
2104: bar-cobar adjunction is an equivalence on the fiber over
2135: with Hochschild--Hilbert series
2141: all higher braces and Massey products are
2210:cohomological concentration, duality, polynomial Hilbert series,
2214:braces and Massey products on $\ChirHoch^*(\cA)$ are

thinking
**Exploring theorem details**

I'm trying to gather information about the full theorem for region 2065 and beyond. It seems like it would be helpful to read more about the theorem itself, as well as any related remarks or commentary that could provide additional context. There's likely a lot to uncover here, and I want to make sure I understand everything thoroughly to assist the user better. Let's see what insights I can find!
codex
The target lane is located. I’m reading the theorem and its follow-up remarks now, because the bad claim may sit in the theorem statement, the explanatory paragraph right after it, or the later recap around line 2385.
exec
/bin/zsh -lc "sed -n '2628,2675p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2060,2425p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\[
\{\textup{(i)},\textup{(ii)},\textup{(iii)},\textup{(iv)},
\textup{(v)},\textup{(vi)},\textup{(vii)},\textup{(ix)},
\textup{(x)}\}
\]
forms a web rather than a chain.

\begin{center}
\begin{tikzcd}[column sep=3em,row sep=2.8em]
\textup{(iv)} \arrow[r] \arrow[dr] &
\textup{(ii)} \arrow[d, shift left=.5ex] \arrow[r, shift left=.5ex] &
\textup{(v)} \arrow[l, shift left=.5ex] \arrow[dl] \arrow[dr] &
\\
\textup{(vii)} \arrow[r, shift left=.5ex] \arrow[ur] &
\textup{(i)} \arrow[l, shift left=.5ex] \arrow[r, shift left=.5ex] \arrow[d, shift left=.5ex] \arrow[dr] \arrow[rr, bend left=12] &
\textup{(iii)} \arrow[l, shift left=.5ex] \arrow[dl] &
\textup{(vi)} \arrow[ll, bend left=12]
\\
\textup{(ix)} \arrow[uur, bend left=16] \arrow[r] &
\textup{(x)} \arrow[u, shift left=.5ex] \arrow[ur] &
 succeeded in 51ms:
reducedness and reduced Li--bar concentration hypotheses recorded in
Corollary~\ref{cor:minimal-orbit-koszul}.
\end{remark}

\begin{theorem}[Equivalences and consequences of chiral Koszulness; \ClaimStatusProvedHere]
\label{thm:koszul-equivalences-meta}
\index{Koszul property!equivalences of characterizations|textbf}

Let $\cA$ be a chiral algebra on a smooth projective curve~$X$
with PBW filtration $F_\bullet$.
Conditions \textup{(i)--(vi)}, \textup{(ix)--(x)}, and the
genus-$0$ clause of condition~\textup{(vii)} below are equivalent.
On the uniform-weight lane, condition~\textup{(vii)} strengthens to
the all-genera concentration statement recorded there and remains
equivalent to them.
Condition~\textup{(viii)} is a proved one-way consequence of
them on the Koszul locus: it yields chiral Hochschild duality,
polynomial Hilbert series, and $\Etwo$-formality, but it does not
force the underlying graded-commutative algebra to be free.
Under the additional perfectness and non-degeneracy hypotheses on the
exec
/bin/zsh -lc "sed -n '3388,3410p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
obstruction through different functors, but a direct
bridge is available only for Kac--Moody.
\end{remark}

\begin{remark}[Computational verification landscape]
\label{rem:koszulness-computational-landscape}
\index{Koszul property!computational verification}
The nine unconditional equivalences and the Hochschild
consequence~\textup{(viii)} have been verified
computationally for a landscape of 17 algebras
(Table~\textup{\ref{tab:koszulness-landscape}}):
13 proved Koszul via equivalences~\textup{(ii)} and~\textup{(ix)},
2 proved not Koszul (Ising minimal model,
$L(c_{3,4}, 0)$: Kac--Shapovalov null vector at $h = 6$
in the bar-relevant range, so~\textup{(ix)} fails;
$L_k(\mathfrak{sl}_3)$ at admissible $q \geq 3$:
$\mathrm{rk}(\fg) = 2$ Cartan classes survive in $H^2$,
Remark~\textup{\ref{rem:admissible-koszul-status}}),
2 open ($L_1(\mathfrak{sl}_2)$ and triplet $\cW(2)$).
The principal proof mechanism is PBW universality

thinking
**Searching for claims**

I need to find the exact bad claim regarding "free polynomial" within the range of 2000-2020. Actually, it seems like there are already fixed theorem lines around 2077 and 2141. But I wonder if there's still an unconditional claim hiding somewhere else. So, my next step will be to search for `free polynomial` across the relevant file to clarify things. Let’s see if I can pinpoint where the problem lies!
exec
/bin/zsh -lc 'rg -n "free polynomial|polynomial algebra|free graded-commutative|free commutative|underlying graded-commutative|brace|Massey" chapters/theory/chiral_koszul_pairs.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '76,90p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:

Theorem~\ref{thm:koszul-equivalences-meta} assembles twelve
tests and consequences around chiral Koszulness. Nine are
unconditional equivalences: $E_2$-collapse of the bar spectral sequence,
vanishing of transferred $A_\infty$ operations $m_k$ for
$k \geq 3$, acyclicity of the twisted tensor product
$K_\tau^L(\cA, \cC)$, truncation of the shadow tower
$\Theta_\cA^{\leq r}$, and five others. One (Hochschild
duality and concentration in degrees $\{0,1,2\}$) is a proved
consequence on the Koszul locus. One (the Lagrangian
eigenspace decomposition) is conditional on perfectness of the
bar-cobar normal complex. One (D-module purity) is a
one-directional implication. The count is exact:
$9 + 1 + 1 + 1$.

 succeeded in 51ms:
142:Kac--Moody (class~$L$, depth~$3$, single Massey product),
858:For Kac--Moody and Virasoro algebras, $\operatorname{gr}_F \cA$ is a polynomial algebra (Koszul by Priddy's theorem); semisimplicity of $\mathfrak{g}$ is not required.
893:This is a polynomial algebra on the generators
896:polynomial algebras are Koszul, with Koszul dual the
943:is a polynomial algebra (the OPE reduces to a commutative
1329:\index{truncated polynomial algebra!$A_\infty$ dual}
1347:m_{n-1}(\underbrace{a, \ldots, a}_{n-1}) = b.
1349:This is the Massey product detecting the off-diagonal class; it is
2078:force the underlying graded-commutative algebra to be free.
2141: all higher braces and Massey products are
2142: cohomologically trivial, but the underlying graded-commutative
2214:braces and Massey products on $\ChirHoch^*(\cA)$ are
2217:underlying graded-commutative cup-product algebra is claimed here.
2386:that the underlying graded-commutative algebra
2395:nonzero degree~$4$. Thus vanishing of higher braces and Massey
3329:does not terminate, and the higher Massey products
3348:carry a nontrivial quartic Massey product, which is
3581:if all higher Massey brackets vanish.
4618: graded is the polynomial algebra $\mathrm{Sym}(V)$ with
5146:pole-free commutative $\cD_X$-algebra. It does not mean the full
codex
The main theorem statement already narrows `(viii)` correctly, but I’m checking downstream summaries and “if and only if” restatements in the same file. These are the usual places where an old unconditional freeness claim survives after the theorem text is fixed.
exec
/bin/zsh -lc "sed -n '6300,6335p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '3528,3595p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"Theorem~\\\\ref\\{thm:koszul-equivalences-meta\\}.*viii|\\(viii\\).*free|free.*\\(viii\\)|\\(viii\\).*polynomial|polynomial Hilbert series.*free|Hochschild.*free\" chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\begin{itemize}
\item Trivial $A_\infty$ (Com) $\leftrightarrow$ Maximal $A_\infty$ (Lie)
\item Non-vanishing of $m_k^{(1)}$ for $\mathcal{A}_1$ is detected by the dual operations $m_k^{(2)}$ on $\mathcal{A}_2$ via the pairing on configuration spaces
\item Massey products of $\mathcal{A}_1$ $\leftrightarrow$ Comassey products of $\mathcal{A}_2$
\end{itemize}
\end{theorem}

\begin{proof}
We prove each item.

\emph{Item~1.} For a commutative chiral algebra $\mathcal{A}_1 = \mathcal{A}_{\mathrm{Com}}$, all higher operations $m_k^{(1)} = 0$ for $k \geq 3$ (the chiral product is strictly associative). The bar complex $\bar{B}^{\mathrm{ch}}(\mathcal{A}_1)$ then has only the binary coproduct, and its Koszul dual $\mathcal{A}_2 = \mathcal{A}_1^!$ carries the Lie operad structure with all brackets $m_k^{(2)}$ potentially non-vanishing. This is the chiral lift of the classical $\mathrm{Com}^! = \mathrm{Lie}$ duality (\cite{LV12}, Theorem~7.6.5).

\emph{Item~2.} The Verdier duality pairing on configuration spaces (Theorem~\ref{thm:verdier-config}) gives:
\[
\langle m_k^{(1)}, n_k^{(2)} \rangle = \int_{\overline{C}_k(X)} \omega_{m_k} \wedge \delta_{n_k}
\]
where $\omega_{m_k} \in \Omega^*_{\log}(\overline{C}_k(X))$ represents the $k$-ary operation of $\mathcal{A}_1$ and $\delta_{n_k} \in \mathcal{D}^*_{\mathrm{dist}}(C_k(X))$ represents the dual operation of $\mathcal{A}_2$. Non-degeneracy of the Verdier pairing (Theorem~\ref{thm:verdier-config}) ensures that $m_k^{(1)} \neq 0$ if and only if the corresponding $n_k^{(2)}$ pairs non-trivially.

\emph{Item~3.} Massey products on $\mathcal{A}_1$ are defined by the higher $A_\infty$ operations $m_k^{(1)}$ for $k \geq 3$ (the obstructions to formality). Under bar-cobar duality, these correspond to comassey products (the dual obstructions in $\mathcal{A}_2$) by the general principle that the bar construction converts algebra operations to coalgebra cooperations (\cite{LV12}, \S10.3). The Verdier pairing identifies $m_k^{(1)}$ with the dual of $m_k^{(2)}$ at the level of configuration space integrals, so vanishing of Massey products on one side is equivalent to triviality of comassey products on the other.
\end{proof}
 succeeded in 52ms:
bar-relevant threshold: Koszulness is open.
For minimal models $L(c_{p,q}, 0)$ with coprime $p < q$,
the first null at $h = pq - p - q + 1$ lies in the
bar-relevant range whenever $pq - p - q + 1 \geq 4$
(i.e., for $(p,q) \neq (2,3)$): these are proved
not chirally Koszul by
Theorem~\ref{thm:kac-shapovalov-koszulness}.

\smallskip\noindent
${}^{\S}$\,\textbf{CE complex vs.\ chiral bar.}
The $N{=}2$ SCA has $H^2_{\mathrm{CE}} \neq 0$
at the mode-algebra level, but $H^2(\barB) = 0$:
the CE complex is a coarse upper bound on bar cohomology,
and PBW universality resolves the apparent paradox
(Remark~\ref{rem:n2-sca-koszulness}).
\end{table}

\begin{proposition}[Koszulness as formality of the convolution algebra;
\ClaimStatusProvedHere]
\label{prop:koszulness-formality-equivalence}
 succeeded in 51ms:
2216:\textup{(viii)} at the theorem level: no freeness statement for the

thinking
**Inspecting polynomial issues**

The search found no immediate problems, but the user asked to fix AP217. I think the issue might relate to the free polynomial mentioned in the theorem; it seems it’s stated as not free. I’ll need to inspect the lines around the theorem, especially line 77. Searching for “free polynomial” could help pinpoint issues, but the user's scope is narrow. I should look closer at lines 2000-2020, in case the line numbers have shifted.
exec
/bin/zsh -lc "rg -n \"ChirHoch\\"'^'"\\*|\\\\ChirHoch\\"'^'"\\*|Hochschild.*algebra|free.*Hochschild|polynomial.*Hochschild|Massey vanishing|FM formality|formality of the local configuration spaces\" chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '2068,2152p'" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: regex parse error:
    (?:ChirHoch\^\*|\ChirHoch\^\*|Hochschild.*algebra|free.*Hochschild|polynomial.*Hochschild|Massey vanishing|FM formality|formality of the local configuration spaces)
                    ^^
error: unrecognized escape sequence
 succeeded in 52ms:
  2068	Let $\cA$ be a chiral algebra on a smooth projective curve~$X$
  2069	with PBW filtration $F_\bullet$.
  2070	Conditions \textup{(i)--(vi)}, \textup{(ix)--(x)}, and the
  2071	genus-$0$ clause of condition~\textup{(vii)} below are equivalent.
  2072	On the uniform-weight lane, condition~\textup{(vii)} strengthens to
  2073	the all-genera concentration statement recorded there and remains
  2074	equivalent to them.
  2075	Condition~\textup{(viii)} is a proved one-way consequence of
  2076	them on the Koszul locus: it yields chiral Hochschild duality,
  2077	polynomial Hilbert series, and $\Etwo$-formality, but it does not
  2078	force the underlying graded-commutative algebra to be free.
  2079	Under the additional perfectness and non-degeneracy hypotheses on the
  2080	ambient tangent complex, condition~\textup{(xi)} is also equivalent to
  2081	them. Condition~\textup{(xii)} implies condition~\textup{(x)}
  2082	(Remark~\ref{rem:d-module-purity-content}); the converse is open.
  2083	
  2084	\smallskip
  2085	\noindent\textbf{Unconditional equivalences:}
  2086	\begin{enumerate}
  2087	\item[\textup{(i)}] $\cA$ is chirally Koszul




thinking
**Inspecting theorem details**

I'm running into a search command error. I think I need to examine theorem H or proposition e2 further to clarify things. The task does seem narrow, but I can still try to identify whether the theorem statement should mention freeness based on Massey vanishing from FM formality. I should check if there’s a proposition that states if higher Massey vanish, then it’s free—perhaps around line 3581. Let’s inspect that area!
thinking
**Clarifying freeness conditions**

I see that the desired statement needs to include two components: a proved concentration and a polynomial Hilbert series, with freeness depending on the Massey vanishing from FM formality. That's crucial. The current theorem suggests that freeness isn't guaranteed, which might seem too strong. The user is asking for a conditional statement, not a negation. It might be safer to either remove the freeness claim or clarify that it's conditional. So, I need to revise the wording accordingly.
thinking
**Evaluating cohomological terms**

I’m considering the current wording that states higher Massey are cohomologically trivial, which might be too strong for what the user wants. "Cohomologically trivial" refers to the vanishing of higher braces or Massey products at the cohomology level from E2 formality, but that might not be sufficient for ensuring freeness. The user specifically desires the freeness to be conditional on the Massey vanishing from FM formality. I need to make sure the wording aligns with that expectation.
thinking
**Inspecting formality implications**

I’m curious about how configuration-space formality leads to the vanishing of higher operations. It seems like it could possibly yield free polynomials. I want to look into the proposition `prop:e2-formality-hochschild`, which might suggest that E2-formality leads to free Gerstenhaber algebras. I should definitely search for more information on this to clarify and gather further insights on this topic. There’s a lot to explore!
codex
I found the likely mismatch: the current `(viii)` text is stronger than the requested safe form in one place and too negative in another. I’m reading the local sources it cites now to align the wording with what is actually proved versus what remains conditional.
exec
/bin/zsh -lc 'rg -n "prop:e2-formality-hochschild|thm:hochschild-polynomial-growth|thm:main-koszul-hoch|free polynomial|Massey vanishing|FM formality|Fulton--MacPherson formality|brace" chapters/theory/chiral_hochschild_koszul.tex chapters/theory/chiral_koszul_pairs.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/theory/chiral_hochschild_koszul.tex:28:carry natural brace and $E_2$ structures. The convolution dg~Lie
chapters/theory/chiral_hochschild_koszul.tex:49: (Theorem~\ref{thm:chiral-deligne-tamarkin}). The brace dg algebra
chapters/theory/chiral_hochschild_koszul.tex:929:\label{thm:main-koszul-hoch}
chapters/theory/chiral_hochschild_koszul.tex:1042:\label{thm:hochschild-polynomial-growth}
chapters/theory/chiral_hochschild_koszul.tex:1072: Theorem~\textup{\ref{thm:main-koszul-hoch}}.
chapters/theory/chiral_hochschild_koszul.tex:1087: from Theorem~\textup{\ref{thm:main-koszul-hoch}}
chapters/theory/chiral_hochschild_koszul.tex:1120:set $n=2$ in Theorem~\ref{thm:main-koszul-hoch}:
chapters/theory/chiral_hochschild_koszul.tex:1137:Part~(c): applying Theorem~\ref{thm:main-koszul-hoch} in degrees
chapters/theory/chiral_hochschild_koszul.tex:1165:Theorem~\ref{thm:hochschild-polynomial-growth}\textup{(a)}
chapters/theory/chiral_hochschild_koszul.tex:1218:Theorem~\ref{thm:main-koszul-hoch} then identifies the quadratic
chapters/theory/chiral_hochschild_koszul.tex:1246:Set $n = 2$ in Theorem~\ref{thm:main-koszul-hoch}: $\ChirHoch^2(\mathcal{A}) \cong \ChirHoch^{2-2}(\mathcal{A}^!)^\vee \otimes \omega_X = \ChirHoch^0(\mathcal{A}^!)^\vee \otimes \omega_X$. Here $\ChirHoch^2(\mathcal{A})$ classifies first-order deformations of~$\mathcal{A}$, and $\ChirHoch^0(\mathcal{A}^!) = Z(\mathcal{A}^!)$ is the center of the Koszul dual. The duality exchanges the deformation space of one algebra with the center of the other, incarnating ``complementarity'' at the level of Hochschild cohomology.
chapters/theory/chiral_hochschild_koszul.tex:1277:\label{prop:e2-formality-hochschild}
chapters/theory/chiral_hochschild_koszul.tex:1288:\item All higher $\Etwo$-operations \textup{(}braces of
chapters/theory/chiral_hochschild_koszul.tex:1295:By Theorem~\ref{thm:hochschild-polynomial-growth},
chapters/theory/chiral_hochschild_koszul.tex:1308:The brace $b_{k-1}(a; a_1, \ldots, a_{k-1})$ for $a \in H^p$,
chapters/theory/chiral_hochschild_koszul.tex:1313:so the braces factor through a single diagonal line in the
chapters/theory/chiral_hochschild_koszul.tex:1316:model of the $\Etwo$-structure then shows that all higher braces are
chapters/theory/chiral_hochschild_koszul.tex:1334:Theorem~\ref{thm:hochschild-polynomial-growth} gives concentration.
chapters/theory/chiral_hochschild_koszul.tex:1335:Proposition~\ref{prop:e2-formality-hochschild} extracts a strictly
chapters/theory/chiral_hochschild_koszul.tex:2397:(Theorem~\ref{thm:main-koszul-hoch}).
exec
/bin/zsh -lc "sed -n '1,260p' chapters/theory/chiral_hochschild_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\chapter{Chiral Hochschild cohomology and Koszul duality}
\label{chap:deformation-theory}

\index{deformation theory!chiral|textbf}
\index{Hochschild cohomology!chiral|textbf}

The MC element $\Theta_\cA \in \MC(\gAmod)$ controls all of chiral
Koszul duality, but how rigid is the moduli it lives in? Without
knowing the tangent complex to
$\MC(\gAmod)/\mathrm{gauge}$, every deformation, obstruction, and
bulk-field coupling remains inaccessible. The chiral Hochschild
complex $\ChirHoch^*(\cA)$ is that tangent complex;
Theorem~H proves it is concentrated in degrees $\{0,1,2\}$ on the
Koszul locus, so the MC moduli has cohomological
amplitude~$[0,2]$, and the Koszul duality
$\ChirHoch^n(\cA) \cong \ChirHoch^{2-n}(\cA^!)^\vee \otimes \omega_X$
is Verdier duality on this tangent space.

The cyclic deformation complex $\Defcyc(\cA)$
(Definition~\ref{def:cyclic-deformation-elementary}) is the cyclic
exec
/bin/zsh -lc "sed -n '1268,1338p' chapters/theory/chiral_hochschild_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '920,1065p' chapters/theory/chiral_hochschild_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
(Theorem~\ref{thm:mc2-bar-intrinsic}); every structural property
of~$\cA$ is a property of~$\Theta_{\cA}$. Four
formality-type conditions on~$\gAmod$ and their consequences for
Koszulness follow.

\medskip

\begin{proposition}[$\Etwo$-formality of chiral Hochschild cohomology;
\ClaimStatusProvedHere]
\label{prop:e2-formality-hochschild}
\index{formality!$\Etwo$-chiral Hochschild}
\index{Hochschild cohomology!$\Etwo$-formality}
Let $\cA$ be a chirally Koszul algebra on a smooth projective
curve~$X$. Then:
\begin{enumerate}[label=\textup{(\roman*)}]
\item $\ChirHoch^*(\cA)$ is formal as an $\Etwo$-algebra:
 the $\Etwo$ quasi-isomorphism type of $\ChirHoch^*(\cA)$ is
 determined by the graded algebra $H^*(\ChirHoch(\cA))$ with its
 cup product and degree-$1$ bracket.

 succeeded in 50ms:
\]
and the bar-cobar counit from
Theorem~\ref{thm:bar-cobar-isomorphism-main}(1) identifies this
with the $\Sigma$-coinvariant descent of $(\cA)^!_\infty$.
This gives~\eqref{eq:chirhoch-descent}.
\end{proof}

\begin{theorem}[Koszul duality for chiral Hochschild cohomology
\textup{(}Theorem~H\textup{)}; \ClaimStatusProvedHere]
\label{thm:main-koszul-hoch}
\index{Hochschild cohomology!Koszul duality|textbf}
\textup{[Regime: quadratic on the Koszul locus
\textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}

For every chiral Koszul datum~$\cA$
\textup{(}Definition~\textup{\ref{def:chiral-koszul-morphism})} with
dual~$\cA^!$ on a smooth projective curve~$X$, the bigraded chiral
chiral Hochschild complex
\textup{(}Definition~\textup{\ref{def:bigraded-hochschild})} satisfies
the \emph{derived-level} duality:
exec
/bin/zsh -lc "sed -n '1065,1105p' chapters/theory/chiral_hochschild_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 \;=\;
 \dim Z(\cA)
 + \dim \ChirHoch^1(\cA)\,t
 + \dim Z(\cA^!)\,t^2,
 \end{equation}
 where $Z(\cA) = \ChirHoch^0(\cA)$ is the center and the symmetry
 $\dim \ChirHoch^0(\cA) = \dim \ChirHoch^2(\cA^!)$ comes from
 Theorem~\textup{\ref{thm:main-koszul-hoch}}.

\item \emph{Koszul functoriality.}\;
 The polynomial $P_{\cA}(t)$ is determined by the Koszul dual pair:
 \[
 P_{\cA}(t) + P_{\cA^!}(t)
 \;=\;
 (\dim Z(\cA) + \dim Z(\cA^!))(1+t^2)
 + (\dim \ChirHoch^1(\cA) + \dim \ChirHoch^1(\cA^!))\,t,
 \]
 and the palindromic duality
 $P_{\cA}(t) = t^2\,P_{\cA^!}(t^{-1})$
 holds under the same Koszul-locus hypotheses


thinking
**Evaluating theorem changes**

I need to parse the desired changes regarding E2-formality, and the current theorem statement seems consistent. However, the user specifically mentions needing “concentration + polynomial Hilbert series (proved); freeness conditional on Massey vanishing from FM formality.” I'm wondering if the e2-formality proposition is too strong or incorrect, especially since the user wants to focus only on fixing equivalence (viii). There might be prior issues related to how formality and freeness are folded in.
thinking
**Clarifying polynomial conditions**

I need to address if the theorem claims free polynomial unconditionally, as it seems the intent is for theorem item (viii) to mention freeness conditionally rather than asserting E2-formality. This might relate to theorem H and the proven polynomial growth, along with a proposition from FM formality that requires vanishing Massey. I’m wondering if vanishing higher Massey products could indicate formal cohomology. I'll need to investigate and search the repo for any mentions of "free polynomial" to clarify this.
exec
/bin/zsh -lc 'rg -n "free polynomial|freely generated polynomial|polynomial algebra.*ChirHoch|ChirHoch.*polynomial algebra|Massey vanishing.*free|FM formality.*free|free.*graded-commutative" chapters/theory/chiral_koszul_pairs.tex chapters/theory/chiral_hochschild_koszul.tex' in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

exec
/bin/zsh -lc "rg -n \"AP217|Koszul equivalence \\(viii\\)|free polynomial\" -S ." in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
./CLAUDE.md:1083:**Genuinely new (AP211-AP224):** AP211 (test file absent for compute engine, 219 findings), AP212 (TODO/FIXME unresolved), AP213 (stub chapter false coverage), AP214 (cross-volume bridge outdated after rectification), AP215 (preface/introduction advertising stronger than proved), AP216 (Koszul (vii) genus-0 scope), AP217 (Koszul (viii) ChirHoch freeness overclaim), AP218 (SC-formality proof restricted to families with metric), AP219 (depth-gap d_alg=2 witness on wrong line), AP220 (D^2=0 proof uses wrong geometric space), AP221 (Gerstenhaber bracket single insertion only), AP222 (Theorem H configuration-space collapse unjustified), AP223 (Theorem H bar-coalgebra/Koszul-dual conflation), AP224 (README scope inflation).
./CLAUDE.md:1089:**New wrong formulas (B74-B78):** B74 (Thm A Verdier at coalgebra level), B75 (av(r)=kappa without Sugawara for non-abelian KM), B76 (ChirHoch free polynomial overclaim), B77 (Q_g duality for all g>=0 when Q_0(A^!)=0), B78 (ProvedHere without proof block).
./relaunch_20260413_111534/R01_chiral_koszul_pairs.md:93:   prove duality and concentration, not free polynomial algebra. (viii)=>(v) uses unproved claim.
./relaunch_20260413_111534/R01_chiral_koszul_pairs.md:650:/bin/zsh -lc "rg -n \"condition~\\\\textup\\{\\(vii\\)\\}|condition~\\\\textup\\{\\(viii\\)\\}|Hochschild|free polynomial|Etwo-formality|polynomial Hilbert|uniform-weight lane|all-genera concentration\" chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
./relaunch_20260413_111534/R01_chiral_koszul_pairs.md:1271:/bin/zsh -lc "rg -n \"all-genera concentration|nine unconditional equivalences|Hochschild consequence|free polynomial|underlying graded-commutative algebra.*free|condition~\\\\textup\\{\\(viii\\)\\}|genus-0 clause of condition~\\\\textup\\{\\(vii\\)\\}\" chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
./relaunch_20260413_111534/R01_chiral_koszul_pairs.md:1272:/bin/zsh -lc "rg -n \"free polynomial algebra|polynomial algebra|\\bfree\\b.*Hochschild|ChirHoch\\"'^'"\\*.*free\" chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
./relaunch_20260413_111534/R01_chiral_koszul_pairs.md:2018:/bin/zsh -lc 'rg -n -F "free polynomial" chapters/theory/chiral_koszul_pairs.tex' in /Users/raeez/chiral-bar-cobarexec
./platonic_rectification_20260413_114523/P12_koszul_vii_viii_upgrade.md:18:  - ISSUE: the surrounding claim surface wanted a “free polynomial” Hochschild algebra, but concentration plus vanishing higher operations does not imply ordinary graded-commutative freeness.
./platonic_rectification_20260413_114523/P12_koszul_vii_viii_upgrade.md:89:2. (viii) claims free polynomial ChirHoch, only duality+concentration proved
./platonic_rectification_20260413_114523/P12_koszul_vii_viii_upgrade.md:773:**Searching for free polynomial details**
./platonic_rectification_20260413_114523/P12_koszul_vii_viii_upgrade.md:775:I’m looking into the known issue about free polynomial ChirHoch, specifically where it says only duality and concentration have been proved. Maybe there's a mention of free polynomial elsewhere in the file or theorem. I think I should search around item (viii) or look for "free polynomial" and "free graded-commutative" terms nearby. Strengthening the proof might be necessary if it can be established.
./platonic_rectification_20260413_114523/P12_koszul_vii_viii_upgrade.md:777:/bin/zsh -lc "rg -n 'free polynomial|freely generated|free graded-commutative|graded-commutative algebra generated|Massey products vanish|Massey product|ChirHoch\\"'^'"\\*\\(\\\\cA\\).*free|ChirHoch.*free' chapters/theory/chiral_koszul_pairs.tex chapters/theory/chiral_hochschild_koszul.tex chapters/connections/concordance.tex metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
./platonic_rectification_20260413_114523/P12_koszul_vii_viii_upgrade.md:1235:It seems that when they say "free graded-commutative," they might be referring to it in the homotopy sense as E2-formal, which involves the absence of Massey products. I need to check the current theorem or any related issues, especially since the user mentioned that "(viii) claims free polynomial ChirHoch, but only duality and concentration are confirmed." Perhaps they intended to express that ChirHoch is a free graded-commutative algebra with a polynomial Hilbert series, but the theorem only supports concentration and duality right now.
./platonic_rectification_20260413_114523/P12_koszul_vii_viii_upgrade.md:4085:  - ISSUE: the surrounding claim surface wanted a “free polynomial” Hochschild algebra, but concentration plus vanishing higher operations does not imply ordinary graded-commutative freeness.
./resume_20260413_165929/R01_chiral_koszul_pairs.md:93:   prove duality and concentration, not free polynomial algebra. (viii)=>(v) uses unproved claim.
./resume_20260413_165929/R01_chiral_koszul_pairs.md:645:/bin/zsh -lc "rg -n \"free polynomial|free graded|graded-commutative algebra|brace|Massey|formal as an E_2|cohomologically trivial\" chapters/theory/chiral_hochschild_koszul.tex chapters/theory/chiral_koszul_pairs.tex | sed -n '1,240p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
./mega_rescue_20260413_141327/M05_chiral_koszul_pairs.md:54:Theorem A + Koszul equivs. Verify filtered-comparison lemma (AP209). Verify (vii)/(viii) scope (AP216/AP217). SC-formality (AP218). Cross-check with FG [FG04].
./audit_campaign_20260412_231034/T13_koszul_equivs.md:6:- [CRITICAL] chapters/theory/chiral_koszul_pairs.tex:2005-2008, 2065-2076; chapters/theory/chiral_hochschild_koszul.tex:576-605, 687-735 — Item `(viii)` is mis-stated. The cited Hochschild theorems prove duality, concentration in degrees `{0,1,2}`, and a polynomial Hilbert series; they do not prove that `\mathrm{ChirHoch}^*(\cA)` is a free polynomial algebra with generators in degrees `{0,1,2}`. The proof of `(viii) ⇒ (v)` uses that stronger unproved claim and also conflates cohomological degree with the second `Ext` grading.
./audit_campaign_20260412_231034/T13_koszul_equivs.md:1732:- [CRITICAL] chapters/theory/chiral_koszul_pairs.tex:2005-2008, 2065-2076; chapters/theory/chiral_hochschild_koszul.tex:576-605, 687-735 — Item `(viii)` is mis-stated. The cited Hochschild theorems prove duality, concentration in degrees `{0,1,2}`, and a polynomial Hilbert series; they do not prove that `\mathrm{ChirHoch}^*(\cA)` is a free polynomial algebra with generators in degrees `{0,1,2}`. The proof of `(viii) ⇒ (v)` uses that stronger unproved claim and also conflates cohomological degree with the second `Ext` grading.
./resume_20260413_192632/R01_chiral_koszul_pairs.md:81:   prove duality and concentration, not free polynomial algebra. (viii)=>(v) uses unproved claim.

thinking
**Assessing freeness condition**

I see logs indicating "freeness DISPROVED," but the user wants to state that freeness is conditional on something specific. I need to follow the user's instructions, even if it seems like there might be a conflict with the current repo state. I'll check the local file to see if it has already changed to "not free." The user wants me to update it to reflect that freeness depends on Massey vanishing. I need to search earlier lines around 2000 to 2008 for clarity.
exec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '1998,2022p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  1998	\toprule
  1999	\textbf{Orbit} & \textbf{Partition} &
  2000	 \textbf{Reduced Li--bar surface} & \textbf{Koszulness} \\
  2001	\midrule
  2002	$\{0\}$ & $(1^N)$ &
  2003	 finite-dim.\ reduced quotient & nilradical-dependent \\
  2004	$\mathbb{O}_{\min}$ & $(2, 1^{N-2})$ &
  2005	 reduced Li--bar concentration assumed &
  2006	 conditional on reducedness and reduced
  2007	 Li--bar concentration
  2008	 \textup{(}Cor~\ref{cor:minimal-orbit-koszul}\textup{)} \\
  2009	$\mathbb{O}_{\mathrm{subreg}}$ & $(N{-}1, 1)$ &
  2010	 reduced Li--bar concentration open & nilradical-dependent \\
  2011	$\mathcal{N}$ & $(N)$ &
  2012	 reduced Li--bar concentration open & nilradical-dependent \\
  2013	\bottomrule
  2014	\end{tabular}
  2015	\end{center}
  2016	
  2017	\smallskip\noindent

thinking
**Inspecting search lines**

The user mentioned searching for lines from 2000 to 2020, but it seems there's an issue later on. I need to consider whether the campaign note has old line numbers, especially since the file has grown. It might be worth inspecting around line 2588 to see if that provides clearer insights. Let's take a closer look at that to address the actual issue properly!
exec
/bin/zsh -lc "sed -n '2578,2600p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
condition~\textup{(v)} is the quasi-isomorphism of the counit
$\varepsilon_{\tau_{\mathrm{univ}}}$, and
Theorem~\ref{thm:fundamental-twisting-morphisms}
identifies that directly with
$\tau_{\mathrm{univ}}$ being a chiral Koszul morphism.
This uses the universal bar twisting datum and the bar filtration,
not the route through \textup{(ii)} or \textup{(iii)}.

\smallskip\noindent
\textup{(i)}$\Rightarrow$\textup{(viii)} is also direct.
Theorem~\ref{thm:main-koszul-hoch},
Theorem~\ref{thm:hochschild-polynomial-growth}, and
Proposition~\ref{prop:e2-formality-hochschild}
start from a chiral Koszul datum and compute
$\ChirHoch^*(\cA)$ by the bar-cobar Hochschild resolution.
This yields duality, polynomial Hilbert growth, and
$\Etwo$-formality without routing through
\textup{(ii)}--\textup{(vii)} inside the meta-theorem.

\smallskip\noindent

thinking
**Considering wording choices**

I think this summary might be better off using "freeness conditional" instead of "E2-formality." I need to search my notes and logs for the desired patch, particularly in `scripts/final_gaps_campaign.py` at line 242. The user provided specific wording to follow, so I should probably adhere to that. I’ll also check old notes in `final_gaps_.../G02_thm_D_concordance_propagate.md` at line 1441 to see if it reveals the intended wording, although it might not be strictly necessary.
exec
/bin/zsh -lc "rg -n \"Massey vanishing from FM formality|free polynomial algebra \\(conditional|freeness conditional|Massey vanishing|FM formality\" final_gaps_20260413_213946 platonic_rectification_20260413_114523 relaunch_20260413_111534 resume_20260413_165929 resume_20260413_192632 audit_campaign_20260412_231034 -g '*.md'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
platonic_rectification_20260413_114523/P17_concordance_sync.md:108:- Theorem H: configuration-space collapse proved via FM formality
platonic_rectification_20260413_114523/P17_concordance_sync.md:115:- Koszul (viii): concentration + polynomial proved; freeness conditional on Massey vanishing
platonic_rectification_20260413_114523/P17_concordance_sync.md:2249:I still need to clarify the exact H theorem. It might not be a single theorem but possibly a triad involving main-koszul-hoch, so I should look around relevant labels. The user is targeting "Theorem H: configuration-space collapse proved via FM formality," which likely needs to be mentioned. I think I should search for sources related to thm:main-koszul-hoch or loop-order-collapse, especially near Theorem H's introduction.
platonic_rectification_20260413_114523/P17_concordance_sync.md:2348:/bin/zsh -lc "rg -n \"Theorem~H|index\\{Theorem H|main-koszul-hoch|hochschild-polynomial-growth|loop-order-collapse|configuration-space collapse|Fulton--MacPherson collapse|FM formality|thm:w-algebra-hochschild|thm:virasoro-hochschild|thm:critical-level-cohomology\" chapters/theory/chiral_hochschild_koszul.tex chapters/theory/introduction.tex chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
final_gaps_20260413_213946/G02_thm_D_concordance_propagate.md:1441:\item $\ChirHoch^*(\cA)$ is a free polynomial algebra (conditional
final_gaps_20260413_213946/G02_thm_D_concordance_propagate.md:1442:on Massey vanishing from FM formality).
final_gaps_20260413_213946/G02_thm_D_concordance_propagate.md:1525:\item $\ChirHoch^*(\cA)$ is a free polynomial algebra (conditional
final_gaps_20260413_213946/G02_thm_D_concordance_propagate.md:1526:on Massey vanishing from FM formality).
final_gaps_20260413_213946/G02_thm_D_concordance_propagate.md:2078:\item $\ChirHoch^*(\cA)$ is a free polynomial algebra (conditional
final_gaps_20260413_213946/G02_thm_D_concordance_propagate.md:2079:on Massey vanishing from FM formality).
final_gaps_20260413_213946/G02_thm_D_concordance_propagate.md:2766:\item $\ChirHoch^*(\cA)$ is a free polynomial algebra (conditional
final_gaps_20260413_213946/G02_thm_D_concordance_propagate.md:2767:on Massey vanishing from FM formality).
resume_20260413_192632/H03_heal_platonic_P11_P16.md:58:Focus on: P11 chain-level via homotopy transfer, P12 Massey vanishing,
resume_20260413_165929/H03_heal_platonic_P11_P16.md:58:Focus on: P11 chain-level via homotopy transfer, P12 Massey vanishing,
resume_20260413_165929/B18_readme_update_v1.md:408:I need to check if the theorem summary fully aligns with the concordance, and it seems like it does. I might update the H statement to include `\ChirHoch^1(V_k(g))\cong g` and mention collapsing by local FM formality, but I think the current summary is already good and not overclaiming. I could also mention that C0 ordinary-derived functions are only valid on a flat perfect locus with genus 0. I should figure out if the README has any unnecessary patterns and run a grep after editing to ensure it's clean.
exec
/bin/zsh -lc "sed -n '1436,1452p' final_gaps_20260413_213946/G02_thm_D_concordance_propagate.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2068,2084p' final_gaps_20260413_213946/G02_thm_D_concordance_propagate.md" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\item The spectral discriminant $\Delta_\cA(t)$ is a polynomial.
\item The genus expansion $F_g=\kappa\cdot\lambda_g^{\mathrm{FP}}$
holds at all genera \textsc{(uniform-weight)};
for multi-weight: $F_g=\kappa\cdot\lambda_g+\delta F_g^{\mathrm{cross}}$
at genus~$0$ only.
\item $\ChirHoch^*(\cA)$ is a free polynomial algebra (conditional
on Massey vanishing from FM formality).


thinking
**Deciding on patches**

I need to determine which standalones to patch based on the user's targets like 'obs_g', 'Theorem D', 'genus-universality', and others. It seems broad, but only some documents might have actual overclaims. I think I could patch a reasonable set, including five_theorems_modular_koszul and programme_summary. Since apply_patch can update many files at once, I should first identify overclaiming lines in the targeted documents. I'll focus on key umbrella documents for patching.
thinking
**Reviewing theorem patches**

I need to consider patching the theorem D statement in `standalone/five_theorems_modular_koszul.tex`, especially the overview lines at the top. The `programme_summary_sections2_4.tex` document has some correct information, but it incorrectly states that kappa is determined by genus-0 data, whereas the new theorem states it's based on genus-1 curvature. I need to check `programme_summary.tex` as well. Additionally, `survey_modular_koszul_duality_v2` contains a mistake regarding "multi-weight: at genus 0 only," which needs to be patched to reflect genus ≥ 2. I'll inspect those lines and look for similar issues in `survey_track_b_compressed`.
 succeeded in 51ms:
\item The cobar-bar counit is a quasi-isomorphism (inversion).
\item The Koszul complex is acyclic.
\item The chiral Hochschild cohomology $\ChirHoch^*(\cA)$ has
polynomial Hilbert series, concentrated in degrees $\{0,1,2\}$.
\item The bar Hilbert series $h_{\cA^!}(q)$ is rational (holonomic).
\item The spectral discriminant $\Delta_\cA(t)$ is a polynomial.
\item The genus expansion $F_g=\kappa\cdot\lambda_g^{\mathrm{FP}}$
holds at all genera \textsc{(uniform-weight)};
for multi-weight: $F_g=\kappa\cdot\lambda_g+\delta F_g^{\mathrm{cross}}$
at genus~$0$ only.
\item $\ChirHoch^*(\cA)$ is a free polynomial algebra (conditional
on Massey vanishing from FM formality).
\item The vertex algebra admits an $E_\infty$-chiral structure
compatible with the bar filtration.
\item The Koszul dual $\cA^!$ is well-defined as a strict chiral algebra.
\end{enumerate}
Equivalences (i)$\Leftrightarrow$(ii)$\Leftrightarrow$(iii) are

thinking
**Searching for phrasing**

I think I need to find specific wording or examples, especially if there's an explicit counterexample. Maybe I should search through the `platonic_rectification_.../P17_concordance_sync.md` file or other logs for the intended phrasing. I'll look around those lines to see if I can find the exact wording I need. It feels important to be accurate here! Let’s explore those logs to ensure I get it right.
codex
I found prior campaign notes in this repo that match your requested repair: they explicitly target `(viii)` as “concentration + polynomial proved; freeness conditional on Massey vanishing.” I’m using that to rewrite the local theorem lane and its recap remarks consistently.
exec
/bin/zsh -lc "sed -n '100,125p' platonic_rectification_20260413_114523/P17_concordance_sync.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"free polynomial algebra \\(conditional on Massey vanishing from FM formality\\)|concentration \\+ polynomial proved; freeness conditional|Koszul \\(viii\\)\" platonic_rectification_20260413_114523 final_gaps_20260413_213946 -g '*.md'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:

Key updates needed:
- Theorem A: Verdier half at algebra level (post-D_Ran)
- Theorem B: on-locus qi (unconditional) + off-locus coderived (unconditional)
- Theorem C0: coderived version unconditional; ordinary-cohomology version conditional
- Theorem C1: g>=1 duality; genus-0 treated separately
- Theorem C2: object identity fixed; conditional on uniform-weight
- Theorem D: non-circular proof path; routing remark
- Theorem H: configuration-space collapse proved via FM formality
- MC2: g^{mod} carrier for main theorem; g^{E1} in e1_modular_koszul
- MC3: conditional on Baxter constraint
- MC4: filtration corrected; resonance lane conditional on transfer
- MC5: coderived unconditional; chain-level conditional for class M
- Topologization: cohomological proved (affine KM); chain-level via qi model; general conjectural
- Koszul (vii): uniform-weight all-genera; multi-weight g=0 only
- Koszul (viii): concentration + polynomial proved; freeness conditional on Massey vanishing

Also add routing remark for Theorem D non-circular path.
mcp startup: no servers
codex
 succeeded in 50ms:
final_gaps_20260413_213946/G17_koszul_pairs_vii.md:74:1083:**Genuinely new (AP211-AP224):** AP211 (test file absent for compute engine, 219 findings), AP212 (TODO/FIXME unresolved), AP213 (stub chapter false coverage), AP214 (cross-volume bridge outdated after rectification), AP215 (preface/introduction advertising stronger than proved), AP216 (Koszul (vii) genus-0 scope), AP217 (Koszul (viii) ChirHoch freeness overclaim), AP218 (SC-formality proof restricted to families with metric), AP219 (depth-gap d_alg=2 witness on wrong line), AP220 (D^2=0 proof uses wrong geometric space), AP221 (Gerstenhaber bracket single insertion only), AP222 (Theorem H configuration-space collapse unjustified), AP223 (Theorem H bar-coalgebra/Koszul-dual conflation), AP224 (README scope inflation).
platonic_rectification_20260413_114523/P17_concordance_sync.md:30:- Koszul (viii). BEFORE: the Hochschild consequence was underspecified and risked being read as a stronger algebra-freeness claim. ISSUE: the strongest proved output is concentration + duality + polynomial Hilbert growth + `E_2`-formality, not blanket freeness. ACTION: STRENGTHENED. AFTER: the concordance now states exactly that package and records generic Virasoro as the boundary counterexample to freeness. CONFIDENCE: high. REMAINING GAP: no converse from (viii) back to bar-cobar inversion is proved.
platonic_rectification_20260413_114523/P17_concordance_sync.md:115:- Koszul (viii): concentration + polynomial proved; freeness conditional on Massey vanishing
platonic_rectification_20260413_114523/P17_concordance_sync.md:2873:8. **Koszul (viii) – chiral Hochschild locus consequence**  
platonic_rectification_20260413_114523/P17_concordance_sync.md:31721:- Koszul (viii). BEFORE: the Hochschild consequence was underspecified and risked being read as a stronger algebra-freeness claim. ISSUE: the strongest proved output is concentration + duality + polynomial Hilbert growth + `E_2`-formality, not blanket freeness. ACTION: STRENGTHENED. AFTER: the concordance now states exactly that package and records generic Virasoro as the boundary counterexample to freeness. CONFIDENCE: high. REMAINING GAP: no converse from (viii) back to bar-cobar inversion is proved.
exec
/bin/zsh -lc "rg -n \"Etwo-formality|\\\\Etwo-formality|need not be free|does not force|no freeness|strongest proved|free polynomial algebra \\(conditional|Massey vanishing\" chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: regex parse error:
    (?:Etwo-formality|\Etwo-formality|need not be free|does not force|no freeness|strongest proved|free polynomial algebra \(conditional|Massey vanishing)
                      ^^
error: unrecognized escape sequence

thinking
**Considering search simplification**

I think I need to approach the searches in a simpler way, possibly by breaking them down into multiple smaller searches. It seems like a good idea to consider how I can refine my queries for clarity and focus. I wonder if that will make the results more effective or relevant. Keeping it straightforward might help in getting the information I’m looking for without unnecessary complexity. Let’s see how that works!
exec
/bin/zsh -lc 'rg -n -F "need not be free" chapters/theory/chiral_koszul_pairs.tex' in /Users/raeez/chiral-bar-cobar succeeded in 55ms:
2143: cup-product algebra need not be free
exec
/bin/zsh -lc 'rg -n -F "does not force the underlying graded-commutative algebra to be free" chapters/theory/chiral_koszul_pairs.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "The strongest proved chiral Hochschild consequence" chapters/theory/chiral_koszul_pairs.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F \"\\\\Etwo-formality\" chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "no freeness statement" chapters/theory/chiral_koszul_pairs.tex' in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

 succeeded in 51ms:
2383:\begin{remark}[The strongest proved chiral Hochschild consequence]
 succeeded in 51ms:
2216:\textup{(viii)} at the theorem level: no freeness statement for the
 exited 1 in 51ms:

exec
/bin/zsh -lc "rg -n \"formality\" chapters/theory/chiral_koszul_pairs.tex | sed -n '1,80p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
100:Koszulness and SC formality are logically independent properties.
102:in degree one; SC formality is the condition
1225:\index{MC element!genus-0 formality}
1229:Chiral Koszulness is a \emph{genus-$0$ formality property}:
1262:\label{prop:ainfty-formality-implies-koszul}
1294:\begin{theorem}[Converse: chiral Koszulness implies formality;
1298:The converse of Proposition~\textup{\ref{prop:ainfty-formality-implies-koszul}}
1303:Forward: Proposition~\ref{prop:ainfty-formality-implies-koszul}.
1308:(Proposition~\ref{prop:shadow-formality-low-degree}). On each fiber,
1353:$A_\infty$-algebra whose non-formality is measured by the single
1355:= 0$ on $H$, recovering formality and hence Koszulness.
1360:measuring non-formality. The shadow obstruction tower
2077:polynomial Hilbert series, and $\Etwo$-formality, but it does not
2094: \textup{(}Proposition~\textup{\ref{prop:ainfty-formality-implies-koszul}}
2147: Proposition~\textup{\ref{prop:e2-formality-hochschild})}.
2209:Proposition~\ref{prop:e2-formality-hochschild} give the stated
2211:and $\Etwo$-formality. The proof of
2212:Proposition~\ref{prop:e2-formality-hochschild} uses the formality of
2222:\textsc{$A_\infty$ formality}
2230:(Proposition~\ref{prop:ainfty-formality-implies-koszul}).

thinking
**Searching for theorem references**

I’m thinking about how to handle citations. If it’s related to FM formality, I might reference that, but I’m not sure if I need to cite it as proved freeness. It seems like the item is part of a theorem rather than a formal proof, so mentioning the condition without citation might be okay. Still, grounding my ideas feels important. I should search to see if there’s a theorem or remark about "Massey vanishing -> free polynomial algebra."
exec
/bin/zsh -lc "rg -n \"free polynomial algebra\" chapters/theory/chiral_hochschild_koszul.tex chapters/theory/chiral_koszul_pairs.tex standalone -g '*.tex'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"free polynomial algebra \\(conditional on Massey vanishing from FM formality\\)|Massey vanishing.*free polynomial algebra|free polynomial algebra.*Massey|Massey vanishing from FM formality\" chapters standalone final_gaps_20260413_213946 -g '*.tex' -g '*.md'" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
standalone/survey_modular_koszul_duality_v2.tex:1789:\item $\ChirHoch^*(\cA)$ is a free polynomial algebra (conditional
 succeeded in 51ms:
standalone/survey_modular_koszul_duality_v2.tex:1790:on Massey vanishing from FM formality).
final_gaps_20260413_213946/G02_thm_D_concordance_propagate.md:1442:on Massey vanishing from FM formality).
final_gaps_20260413_213946/G02_thm_D_concordance_propagate.md:1526:on Massey vanishing from FM formality).
final_gaps_20260413_213946/G02_thm_D_concordance_propagate.md:2079:on Massey vanishing from FM formality).
final_gaps_20260413_213946/G02_thm_D_concordance_propagate.md:2767:on Massey vanishing from FM formality).
exec
/bin/zsh -lc "sed -n '1778,1795p' standalone/survey_modular_koszul_duality_v2.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\item Bar cohomology concentrates on the diagonal (PBW).
\item The cobar-bar counit is a quasi-isomorphism (inversion).
\item The Koszul complex is acyclic.
\item The chiral Hochschild cohomology $\ChirHoch^*(\cA)$ has
polynomial Hilbert series, concentrated in degrees $\{0,1,2\}$.
\item The bar Hilbert series $h_{\cA^!}(q)$ is rational (holonomic).
\item The spectral discriminant $\Delta_\cA(t)$ is a polynomial.
\item The genus expansion $F_g=\kappa\cdot\lambda_g^{\mathrm{FP}}$
holds at all genera \textsc{(uniform-weight)};
for multi-weight: $F_g=\kappa\cdot\lambda_g+\delta F_g^{\mathrm{cross}}$
at genus~$0$ only.
\item $\ChirHoch^*(\cA)$ is a free polynomial algebra (conditional
on Massey vanishing from FM formality).
\item The vertex algebra admits an $E_\infty$-chiral structure
compatible with the bar filtration.
\item The Koszul dual $\cA^!$ is well-defined as a strict chiral algebra.
\end{enumerate}
Equivalences (i)$\Leftrightarrow$(ii)$\Leftrightarrow$(iii) are
codex
Pre-edit verification for the touched theorem surface:

```text
genus: [g=0 core equivalence; (viii) NA to genus scope]
degree: [cohomological degrees {0,1,2} explicitly stated]
AP32 weight tag: [NA]
AP139 free-var audit: LHS vars:{\cA,\cA^!,X} RHS vars:{\cA,\cA^!,X} LHS⊇RHS? [Y]
AP36: [implies/iff]  (viii) is one-way only; converse not claimed
verdict: ACCEPT
```

I’m patching only the `(viii)` theorem lane, its proof recap, and the local remark so they say exactly: proved concentration + polynomial Hilbert growth; freeness only conditional on the FM-formality/Massey package.


thinking
**Evaluating proof conditions**

I think it could be acceptable if the conditional is explicit and well-supported. However, the theorem is called ProvedHere, and having a conditional subclause might not be beneficial unless the proof includes a clear if-then argument. I'm wondering if we can justify "if all higher Massey vanish, then the cup-product algebra is free polynomial" perhaps from a minimal model. It's definitely not obvious, and I need to avoid making unsupported claims.
thinking
**Revising theorem lane terminology**

I need to consider removing or avoiding the phrase "E2-formality" entirely from the theorem lane. I found some search results to patch—2077, 2209, 2385, and 2594. There's no need to patch other generic mentions or proposition labels. After the patch, I might only find `\Etwo-formality` in unrelated contexts. I need to be careful with the line 30 note about the generic Vir boundary counterexample without affecting other files. Let's create this patch thoughtfully.
codex
I have the write scope. The patch will only touch the `(viii)` theorem paragraph, item `(viii)`, its proof paragraph, the follow-up remark, and the later recap sentence in the same file. After that I’ll grep the file to confirm no unconditional “free polynomial” wording remains in this lane.
codex
The first patch missed one wrapped paragraph exactly as TeX currently has it. I’m re-reading the live chunk and applying the same scoped edits against the exact line breaks now.
exec
/bin/zsh -lc "sed -n '2204,2223p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2072,2148p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
On the uniform-weight lane, condition~\textup{(vii)} strengthens to
the all-genera concentration statement recorded there and remains
equivalent to them.
Condition~\textup{(viii)} is a proved one-way consequence of
them on the Koszul locus: it yields chiral Hochschild duality,
polynomial Hilbert series, and $\Etwo$-formality, but it does not
force the underlying graded-commutative algebra to be free.
Under the additional perfectness and non-degeneracy hypotheses on the
ambient tangent complex, condition~\textup{(xi)} is also equivalent to
them. Condition~\textup{(xii)} implies condition~\textup{(x)}
(Remark~\ref{rem:d-module-purity-content}); the converse is open.

\smallskip
\noindent\textbf{Unconditional equivalences:}
\begin{enumerate}
\item[\textup{(i)}] $\cA$ is chirally Koszul
 \textup{(}Definition~\textup{\ref{def:chiral-koszul-morphism})}.
\item[\textup{(ii)}] The PBW spectral sequence on
 $\barBgeom(\cA)$ collapses at $E_2$
 \textup{(}Theorem~\textup{\ref{thm:pbw-koszulness-criterion})}.
 succeeded in 52ms:
$\Omega(\barBgeom(\cA)) \xrightarrow{\sim} \cA$ identifies the
bar-cobar resolution with the chiral Hochschild complex. On the
Koszul locus, Theorem~H,
Theorem~\ref{thm:main-koszul-hoch},
Theorem~\ref{thm:hochschild-polynomial-growth}, and
Proposition~\ref{prop:e2-formality-hochschild} give the stated
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
exec
/bin/zsh -lc "sed -n '2586,2598p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2383,2398p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\begin{remark}[The strongest proved chiral Hochschild consequence]
The strengthened form of \textup{(viii)} stops at duality,
polynomial Hilbert series, and $\Etwo$-formality. It does not imply
that the underlying graded-commutative algebra
$\ChirHoch^*(\cA)$ is free. At generic central charge,
Theorem~\ref{thm:virasoro-hochschild} gives
\[
\ChirHoch^*(\mathrm{Vir}_c)\cong \mathbb{C}\oplus \mathbb{C}[-2].
\]
The degree-$2$ class squares to zero because
$\ChirHoch^4(\mathrm{Vir}_c)=0$, whereas a free
graded-commutative algebra on a degree-$2$ generator would have
nonzero degree~$4$. Thus vanishing of higher braces and Massey
products is the strongest proved consequence; ordinary cup-product
relations may remain.
\end{remark}
 succeeded in 52ms:
\smallskip\noindent
\textup{(i)}$\Rightarrow$\textup{(viii)} is also direct.
Theorem~\ref{thm:main-koszul-hoch},
Theorem~\ref{thm:hochschild-polynomial-growth}, and
Proposition~\ref{prop:e2-formality-hochschild}
start from a chiral Koszul datum and compute
$\ChirHoch^*(\cA)$ by the bar-cobar Hochschild resolution.
This yields duality, polynomial Hilbert growth, and
$\Etwo$-formality without routing through
\textup{(ii)}--\textup{(vii)} inside the meta-theorem.

\smallskip\noindent
\textup{(iii)}$\Rightarrow$\textup{(x)} is fiberwise and geometric.
file update
M /Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex
@@ -2076,4 +2076,6 @@
 them on the Koszul locus: it yields chiral Hochschild duality,
-polynomial Hilbert series, and $\Etwo$-formality, but it does not
-force the underlying graded-commutative algebra to be free.
+cohomological concentration in degrees~$\{0,1,2\}$, and polynomial
+Hilbert series. Any free-polynomial description of the cup-product
+algebra is conditional on a Massey-vanishing consequence of
+Fulton--MacPherson formality.
 Under the additional perfectness and non-degeneracy hypotheses on the
@@ -2139,6 +2141,5 @@
  \]
- and $\ChirHoch^*(\cA)$ is formal as an $\Etwo$-algebra:
- all higher braces and Massey products are
- cohomologically trivial, but the underlying graded-commutative
- cup-product algebra need not be free
+ and any free-polynomial description of the graded-commutative
+ cup-product algebra is conditional on a Massey-vanishing
+ consequence of Fulton--MacPherson formality
  \textup{(}Theorem~H,
@@ -2146,3 +2147,3 @@
  Theorem~\textup{\ref{thm:hochschild-polynomial-growth}},
- Proposition~\textup{\ref{prop:e2-formality-hochschild})}.
+ cf.\ Proposition~\textup{\ref{prop:e2-formality-hochschild}}\textup{)}.
 \end{enumerate}
apply_patch(auto_approved=true) exited 0 in 26ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex
file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 53403b6c5a92d960989ffad4b2d92d19ce2d9058..f8bc4df8896a432fd2302844443775c9aaa5431e
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -2074,8 +2074,10 @@
 equivalent to them.
 Condition~\textup{(viii)} is a proved one-way consequence of
 them on the Koszul locus: it yields chiral Hochschild duality,
-polynomial Hilbert series, and $\Etwo$-formality, but it does not
-force the underlying graded-commutative algebra to be free.
+cohomological concentration in degrees~$\{0,1,2\}$, and polynomial
+Hilbert series. Any free-polynomial description of the cup-product
+algebra is conditional on a Massey-vanishing consequence of
+Fulton--MacPherson formality.
 Under the additional perfectness and non-degeneracy hypotheses on the
 ambient tangent complex, condition~\textup{(xi)} is also equivalent to
 them. Condition~\textup{(xii)} implies condition~\textup{(x)}
@@ -2137,14 +2139,13 @@
  P_\cA(t)=\dim Z(\cA)+\dim \ChirHoch^1(\cA)\cdot t
  + \dim Z(\cA^!)\cdot t^2,
  \]
- and $\ChirHoch^*(\cA)$ is formal as an $\Etwo$-algebra:
- all higher braces and Massey products are
- cohomologically trivial, but the underlying graded-commutative
- cup-product algebra need not be free
+ and any free-polynomial description of the graded-commutative
+ cup-product algebra is conditional on a Massey-vanishing
+ consequence of Fulton--MacPherson formality
  \textup{(}Theorem~H,
  Theorem~\textup{\ref{thm:main-koszul-hoch}},
  Theorem~\textup{\ref{thm:hochschild-polynomial-growth}},
- Proposition~\textup{\ref{prop:e2-formality-hochschild})}.
+ cf.\ Proposition~\textup{\ref{prop:e2-formality-hochschild}}\textup{)}.
 \end{enumerate}
 
 \smallskip

file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 53403b6c5a92d960989ffad4b2d92d19ce2d9058..f8bc4df8896a432fd2302844443775c9aaa5431e
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -2074,8 +2074,10 @@
 equivalent to them.
 Condition~\textup{(viii)} is a proved one-way consequence of
 them on the Koszul locus: it yields chiral Hochschild duality,
-polynomial Hilbert series, and $\Etwo$-formality, but it does not
-force the underlying graded-commutative algebra to be free.
+cohomological concentration in degrees~$\{0,1,2\}$, and polynomial
+Hilbert series. Any free-polynomial description of the cup-product
+algebra is conditional on a Massey-vanishing consequence of
+Fulton--MacPherson formality.
 Under the additional perfectness and non-degeneracy hypotheses on the
 ambient tangent complex, condition~\textup{(xi)} is also equivalent to
 them. Condition~\textup{(xii)} implies condition~\textup{(x)}
@@ -2137,14 +2139,13 @@
  P_\cA(t)=\dim Z(\cA)+\dim \ChirHoch^1(\cA)\cdot t
  + \dim Z(\cA^!)\cdot t^2,
  \]
- and $\ChirHoch^*(\cA)$ is formal as an $\Etwo$-algebra:
- all higher braces and Massey products are
- cohomologically trivial, but the underlying graded-commutative
- cup-product algebra need not be free
+ and any free-polynomial description of the graded-commutative
+ cup-product algebra is conditional on a Massey-vanishing
+ consequence of Fulton--MacPherson formality
  \textup{(}Theorem~H,
  Theorem~\textup{\ref{thm:main-koszul-hoch}},
  Theorem~\textup{\ref{thm:hochschild-polynomial-growth}},
- Proposition~\textup{\ref{prop:e2-formality-hochschild})}.
+ cf.\ Proposition~\textup{\ref{prop:e2-formality-hochschild}}\textup{)}.
 \end{enumerate}
 
 \smallskip

file update
M /Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex
@@ -2210,10 +2210,9 @@
 Proposition~\ref{prop:e2-formality-hochschild} give the stated
-cohomological concentration, duality, polynomial Hilbert series,
-and $\Etwo$-formality. The proof of
-Proposition~\ref{prop:e2-formality-hochschild} uses the formality of
-the local configuration spaces $\FM_n(\mathbb{C})$, so the higher
-braces and Massey products on $\ChirHoch^*(\cA)$ are
-cohomologically trivial. This is the full proved content of
-\textup{(viii)} at the theorem level: no freeness statement for the
-underlying graded-commutative cup-product algebra is claimed here.
+cohomological concentration, duality, and polynomial Hilbert
+series. Proposition~\ref{prop:e2-formality-hochschild} isolates the
+Fulton--MacPherson formality input governing higher braces and
+Massey products. Any further free-polynomial refinement of the
+graded-commutative cup-product algebra requires that extra
+Massey-vanishing package and is not part of the unconditional
+equivalence core.
 No converse from
apply_patch(auto_approved=true) exited 0 in 23ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex
file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 53403b6c5a92d960989ffad4b2d92d19ce2d9058..6a093d2d4ad5e81be6b1fbb2091ed70e5d8cda44
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -2074,8 +2074,10 @@
 equivalent to them.
 Condition~\textup{(viii)} is a proved one-way consequence of
 them on the Koszul locus: it yields chiral Hochschild duality,
-polynomial Hilbert series, and $\Etwo$-formality, but it does not
-force the underlying graded-commutative algebra to be free.
+cohomological concentration in degrees~$\{0,1,2\}$, and polynomial
+Hilbert series. Any free-polynomial description of the cup-product
+algebra is conditional on a Massey-vanishing consequence of
+Fulton--MacPherson formality.
 Under the additional perfectness and non-degeneracy hypotheses on the
 ambient tangent complex, condition~\textup{(xi)} is also equivalent to
 them. Condition~\textup{(xii)} implies condition~\textup{(x)}
@@ -2137,14 +2139,13 @@
  P_\cA(t)=\dim Z(\cA)+\dim \ChirHoch^1(\cA)\cdot t
  + \dim Z(\cA^!)\cdot t^2,
  \]
- and $\ChirHoch^*(\cA)$ is formal as an $\Etwo$-algebra:
- all higher braces and Massey products are
- cohomologically trivial, but the underlying graded-commutative
- cup-product algebra need not be free
+ and any free-polynomial description of the graded-commutative
+ cup-product algebra is conditional on a Massey-vanishing
+ consequence of Fulton--MacPherson formality
  \textup{(}Theorem~H,
  Theorem~\textup{\ref{thm:main-koszul-hoch}},
  Theorem~\textup{\ref{thm:hochschild-polynomial-growth}},
- Proposition~\textup{\ref{prop:e2-formality-hochschild})}.
+ cf.\ Proposition~\textup{\ref{prop:e2-formality-hochschild}}\textup{)}.
 \end{enumerate}
 
 \smallskip
@@ -2207,14 +2208,13 @@
 Theorem~\ref{thm:main-koszul-hoch},
 Theorem~\ref{thm:hochschild-polynomial-growth}, and
 Proposition~\ref{prop:e2-formality-hochschild} give the stated
-cohomological concentration, duality, polynomial Hilbert series,
-and $\Etwo$-formality. The proof of
-Proposition~\ref{prop:e2-formality-hochschild} uses the formality of
-the local configuration spaces $\FM_n(\mathbb{C})$, so the higher
-braces and Massey products on $\ChirHoch^*(\cA)$ are
-cohomologically trivial. This is the full proved content of
-\textup{(viii)} at the theorem level: no freeness statement for the
-underlying graded-commutative cup-product algebra is claimed here.
+cohomological concentration, duality, and polynomial Hilbert
+series. Proposition~\ref{prop:e2-formality-hochschild} isolates the
+Fulton--MacPherson formality input governing higher braces and
+Massey products. Any further free-polynomial refinement of the
+graded-commutative cup-product algebra requires that extra
+Massey-vanishing package and is not part of the unconditional
+equivalence core.
 No converse from
 \textup{(viii)} to the bar-cobar counit is proved here.
 

file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 53403b6c5a92d960989ffad4b2d92d19ce2d9058..6a093d2d4ad5e81be6b1fbb2091ed70e5d8cda44
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -2074,8 +2074,10 @@
 equivalent to them.
 Condition~\textup{(viii)} is a proved one-way consequence of
 them on the Koszul locus: it yields chiral Hochschild duality,
-polynomial Hilbert series, and $\Etwo$-formality, but it does not
-force the underlying graded-commutative algebra to be free.
+cohomological concentration in degrees~$\{0,1,2\}$, and polynomial
+Hilbert series. Any free-polynomial description of the cup-product
+algebra is conditional on a Massey-vanishing consequence of
+Fulton--MacPherson formality.
 Under the additional perfectness and non-degeneracy hypotheses on the
 ambient tangent complex, condition~\textup{(xi)} is also equivalent to
 them. Condition~\textup{(xii)} implies condition~\textup{(x)}
@@ -2137,14 +2139,13 @@
  P_\cA(t)=\dim Z(\cA)+\dim \ChirHoch^1(\cA)\cdot t
  + \dim Z(\cA^!)\cdot t^2,
  \]
- and $\ChirHoch^*(\cA)$ is formal as an $\Etwo$-algebra:
- all higher braces and Massey products are
- cohomologically trivial, but the underlying graded-commutative
- cup-product algebra need not be free
+ and any free-polynomial description of the graded-commutative
+ cup-product algebra is conditional on a Massey-vanishing
+ consequence of Fulton--MacPherson formality
  \textup{(}Theorem~H,
  Theorem~\textup{\ref{thm:main-koszul-hoch}},
  Theorem~\textup{\ref{thm:hochschild-polynomial-growth}},
- Proposition~\textup{\ref{prop:e2-formality-hochschild})}.
+ cf.\ Proposition~\textup{\ref{prop:e2-formality-hochschild}}\textup{)}.
 \end{enumerate}
 
 \smallskip
@@ -2207,14 +2208,13 @@
 Theorem~\ref{thm:main-koszul-hoch},
 Theorem~\ref{thm:hochschild-polynomial-growth}, and
 Proposition~\ref{prop:e2-formality-hochschild} give the stated
-cohomological concentration, duality, polynomial Hilbert series,
-and $\Etwo$-formality. The proof of
-Proposition~\ref{prop:e2-formality-hochschild} uses the formality of
-the local configuration spaces $\FM_n(\mathbb{C})$, so the higher
-braces and Massey products on $\ChirHoch^*(\cA)$ are
-cohomologically trivial. This is the full proved content of
-\textup{(viii)} at the theorem level: no freeness statement for the
-underlying graded-commutative cup-product algebra is claimed here.
+cohomological concentration, duality, and polynomial Hilbert
+series. Proposition~\ref{prop:e2-formality-hochschild} isolates the
+Fulton--MacPherson formality input governing higher braces and
+Massey products. Any further free-polynomial refinement of the
+graded-commutative cup-product algebra requires that extra
+Massey-vanishing package and is not part of the unconditional
+equivalence core.
 No converse from
 \textup{(viii)} to the bar-cobar counit is proved here.
 

file update
M /Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex
@@ -2382,17 +2382,11 @@
 
-\begin{remark}[The strongest proved chiral Hochschild consequence]
-The strengthened form of \textup{(viii)} stops at duality,
-polynomial Hilbert series, and $\Etwo$-formality. It does not imply
-that the underlying graded-commutative algebra
-$\ChirHoch^*(\cA)$ is free. At generic central charge,
-Theorem~\ref{thm:virasoro-hochschild} gives
-\[
-\ChirHoch^*(\mathrm{Vir}_c)\cong \mathbb{C}\oplus \mathbb{C}[-2].
-\]
-The degree-$2$ class squares to zero because
-$\ChirHoch^4(\mathrm{Vir}_c)=0$, whereas a free
-graded-commutative algebra on a degree-$2$ generator would have
-nonzero degree~$4$. Thus vanishing of higher braces and Massey
-products is the strongest proved consequence; ordinary cup-product
-relations may remain.
+\begin{remark}[The theorem-level content of \textup{(viii)}]
+Theorem~\ref{thm:main-koszul-hoch} and
+Theorem~\ref{thm:hochschild-polynomial-growth} prove duality,
+cohomological concentration in degrees~$\{0,1,2\}$, and
+polynomial Hilbert growth on the Koszul locus.
+A further identification of $\ChirHoch^*(\cA)$ as a free
+polynomial algebra is conditional on a Massey-vanishing
+consequence of Fulton--MacPherson formality and is not used in
+the equivalence core.
 \end{remark}
apply_patch(auto_approved=true) exited 0 in 22ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex
file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 53403b6c5a92d960989ffad4b2d92d19ce2d9058..ed544ace65b1f2a59b7e4ce517f8117d24141819
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -2074,8 +2074,10 @@
 equivalent to them.
 Condition~\textup{(viii)} is a proved one-way consequence of
 them on the Koszul locus: it yields chiral Hochschild duality,
-polynomial Hilbert series, and $\Etwo$-formality, but it does not
-force the underlying graded-commutative algebra to be free.
+cohomological concentration in degrees~$\{0,1,2\}$, and polynomial
+Hilbert series. Any free-polynomial description of the cup-product
+algebra is conditional on a Massey-vanishing consequence of
+Fulton--MacPherson formality.
 Under the additional perfectness and non-degeneracy hypotheses on the
 ambient tangent complex, condition~\textup{(xi)} is also equivalent to
 them. Condition~\textup{(xii)} implies condition~\textup{(x)}
@@ -2137,14 +2139,13 @@
  P_\cA(t)=\dim Z(\cA)+\dim \ChirHoch^1(\cA)\cdot t
  + \dim Z(\cA^!)\cdot t^2,
  \]
- and $\ChirHoch^*(\cA)$ is formal as an $\Etwo$-algebra:
- all higher braces and Massey products are
- cohomologically trivial, but the underlying graded-commutative
- cup-product algebra need not be free
+ and any free-polynomial description of the graded-commutative
+ cup-product algebra is conditional on a Massey-vanishing
+ consequence of Fulton--MacPherson formality
  \textup{(}Theorem~H,
  Theorem~\textup{\ref{thm:main-koszul-hoch}},
  Theorem~\textup{\ref{thm:hochschild-polynomial-growth}},
- Proposition~\textup{\ref{prop:e2-formality-hochschild})}.
+ cf.\ Proposition~\textup{\ref{prop:e2-formality-hochschild}}\textup{)}.
 \end{enumerate}
 
 \smallskip
@@ -2207,14 +2208,13 @@
 Theorem~\ref{thm:main-koszul-hoch},
 Theorem~\ref{thm:hochschild-polynomial-growth}, and
 Proposition~\ref{prop:e2-formality-hochschild} give the stated
-cohomological concentration, duality, polynomial Hilbert series,
-and $\Etwo$-formality. The proof of
-Proposition~\ref{prop:e2-formality-hochschild} uses the formality of
-the local configuration spaces $\FM_n(\mathbb{C})$, so the higher
-braces and Massey products on $\ChirHoch^*(\cA)$ are
-cohomologically trivial. This is the full proved content of
-\textup{(viii)} at the theorem level: no freeness statement for the
-underlying graded-commutative cup-product algebra is claimed here.
+cohomological concentration, duality, and polynomial Hilbert
+series. Proposition~\ref{prop:e2-formality-hochschild} isolates the
+Fulton--MacPherson formality input governing higher braces and
+Massey products. Any further free-polynomial refinement of the
+graded-commutative cup-product algebra requires that extra
+Massey-vanishing package and is not part of the unconditional
+equivalence core.
 No converse from
 \textup{(viii)} to the bar-cobar counit is proved here.
 
@@ -2380,21 +2380,15 @@
 residues.
 \end{remark}
 
-\begin{remark}[The strongest proved chiral Hochschild consequence]
-The strengthened form of \textup{(viii)} stops at duality,
-polynomial Hilbert series, and $\Etwo$-formality. It does not imply
-that the underlying graded-commutative algebra
-$\ChirHoch^*(\cA)$ is free. At generic central charge,
-Theorem~\ref{thm:virasoro-hochschild} gives
-\[
-\ChirHoch^*(\mathrm{Vir}_c)\cong \mathbb{C}\oplus \mathbb{C}[-2].
-\]
-The degree-$2$ class squares to zero because
-$\ChirHoch^4(\mathrm{Vir}_c)=0$, whereas a free
-graded-commutative algebra on a degree-$2$ generator would have
-nonzero degree~$4$. Thus vanishing of higher braces and Massey
-products is the strongest proved consequence; ordinary cup-product
-relations may remain.
+\begin{remark}[The theorem-level content of \textup{(viii)}]
+Theorem~\ref{thm:main-koszul-hoch} and
+Theorem~\ref{thm:hochschild-polynomial-growth} prove duality,
+cohomological concentration in degrees~$\{0,1,2\}$, and
+polynomial Hilbert growth on the Koszul locus.
+A further identification of $\ChirHoch^*(\cA)$ as a free
+polynomial algebra is conditional on a Massey-vanishing
+consequence of Fulton--MacPherson formality and is not used in
+the equivalence core.
 \end{remark}
 
 \medskip

file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 53403b6c5a92d960989ffad4b2d92d19ce2d9058..ed544ace65b1f2a59b7e4ce517f8117d24141819
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -2074,8 +2074,10 @@
 equivalent to them.
 Condition~\textup{(viii)} is a proved one-way consequence of
 them on the Koszul locus: it yields chiral Hochschild duality,
-polynomial Hilbert series, and $\Etwo$-formality, but it does not
-force the underlying graded-commutative algebra to be free.
+cohomological concentration in degrees~$\{0,1,2\}$, and polynomial
+Hilbert series. Any free-polynomial description of the cup-product
+algebra is conditional on a Massey-vanishing consequence of
+Fulton--MacPherson formality.
 Under the additional perfectness and non-degeneracy hypotheses on the
 ambient tangent complex, condition~\textup{(xi)} is also equivalent to
 them. Condition~\textup{(xii)} implies condition~\textup{(x)}
@@ -2137,14 +2139,13 @@
  P_\cA(t)=\dim Z(\cA)+\dim \ChirHoch^1(\cA)\cdot t
  + \dim Z(\cA^!)\cdot t^2,
  \]
- and $\ChirHoch^*(\cA)$ is formal as an $\Etwo$-algebra:
- all higher braces and Massey products are
- cohomologically trivial, but the underlying graded-commutative
- cup-product algebra need not be free
+ and any free-polynomial description of the graded-commutative
+ cup-product algebra is conditional on a Massey-vanishing
+ consequence of Fulton--MacPherson formality
  \textup{(}Theorem~H,
  Theorem~\textup{\ref{thm:main-koszul-hoch}},
  Theorem~\textup{\ref{thm:hochschild-polynomial-growth}},
- Proposition~\textup{\ref{prop:e2-formality-hochschild})}.
+ cf.\ Proposition~\textup{\ref{prop:e2-formality-hochschild}}\textup{)}.
 \end{enumerate}
 
 \smallskip
@@ -2207,14 +2208,13 @@
 Theorem~\ref{thm:main-koszul-hoch},
 Theorem~\ref{thm:hochschild-polynomial-growth}, and
 Proposition~\ref{prop:e2-formality-hochschild} give the stated
-cohomological concentration, duality, polynomial Hilbert series,
-and $\Etwo$-formality. The proof of
-Proposition~\ref{prop:e2-formality-hochschild} uses the formality of
-the local configuration spaces $\FM_n(\mathbb{C})$, so the higher
-braces and Massey products on $\ChirHoch^*(\cA)$ are
-cohomologically trivial. This is the full proved content of
-\textup{(viii)} at the theorem level: no freeness statement for the
-underlying graded-commutative cup-product algebra is claimed here.
+cohomological concentration, duality, and polynomial Hilbert
+series. Proposition~\ref{prop:e2-formality-hochschild} isolates the
+Fulton--MacPherson formality input governing higher braces and
+Massey products. Any further free-polynomial refinement of the
+graded-commutative cup-product algebra requires that extra
+Massey-vanishing package and is not part of the unconditional
+equivalence core.
 No converse from
 \textup{(viii)} to the bar-cobar counit is proved here.
 
@@ -2380,21 +2380,15 @@
 residues.
 \end{remark}
 
-\begin{remark}[The strongest proved chiral Hochschild consequence]
-The strengthened form of \textup{(viii)} stops at duality,
-polynomial Hilbert series, and $\Etwo$-formality. It does not imply
-that the underlying graded-commutative algebra
-$\ChirHoch^*(\cA)$ is free. At generic central charge,
-Theorem~\ref{thm:virasoro-hochschild} gives
-\[
-\ChirHoch^*(\mathrm{Vir}_c)\cong \mathbb{C}\oplus \mathbb{C}[-2].
-\]
-The degree-$2$ class squares to zero because
-$\ChirHoch^4(\mathrm{Vir}_c)=0$, whereas a free
-graded-commutative algebra on a degree-$2$ generator would have
-nonzero degree~$4$. Thus vanishing of higher braces and Massey
-products is the strongest proved consequence; ordinary cup-product
-relations may remain.
+\begin{remark}[The theorem-level content of \textup{(viii)}]
+Theorem~\ref{thm:main-koszul-hoch} and
+Theorem~\ref{thm:hochschild-polynomial-growth} prove duality,
+cohomological concentration in degrees~$\{0,1,2\}$, and
+polynomial Hilbert growth on the Koszul locus.
+A further identification of $\ChirHoch^*(\cA)$ as a free
+polynomial algebra is conditional on a Massey-vanishing
+consequence of Fulton--MacPherson formality and is not used in
+the equivalence core.
 \end{remark}
 
 \medskip

file update
M /Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex
@@ -2586,4 +2586,6 @@
 $\ChirHoch^*(\cA)$ by the bar-cobar Hochschild resolution.
-This yields duality, polynomial Hilbert growth, and
-$\Etwo$-formality without routing through
+This yields duality, concentration in degrees~$\{0,1,2\}$, and
+polynomial Hilbert growth. Any free-polynomial upgrade of the
+cup-product algebra is conditional on the Massey-vanishing
+Fulton--MacPherson formality package, so it is not routed through
 \textup{(ii)}--\textup{(vii)} inside the meta-theorem.
apply_patch(auto_approved=true) exited 0 in 25ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex
file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 53403b6c5a92d960989ffad4b2d92d19ce2d9058..6929930770084a4025e237c9100b3444f4a2e6c6
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -2074,8 +2074,10 @@
 equivalent to them.
 Condition~\textup{(viii)} is a proved one-way consequence of
 them on the Koszul locus: it yields chiral Hochschild duality,
-polynomial Hilbert series, and $\Etwo$-formality, but it does not
-force the underlying graded-commutative algebra to be free.
+cohomological concentration in degrees~$\{0,1,2\}$, and polynomial
+Hilbert series. Any free-polynomial description of the cup-product
+algebra is conditional on a Massey-vanishing consequence of
+Fulton--MacPherson formality.
 Under the additional perfectness and non-degeneracy hypotheses on the
 ambient tangent complex, condition~\textup{(xi)} is also equivalent to
 them. Condition~\textup{(xii)} implies condition~\textup{(x)}
@@ -2137,14 +2139,13 @@
  P_\cA(t)=\dim Z(\cA)+\dim \ChirHoch^1(\cA)\cdot t
  + \dim Z(\cA^!)\cdot t^2,
  \]
- and $\ChirHoch^*(\cA)$ is formal as an $\Etwo$-algebra:
- all higher braces and Massey products are
- cohomologically trivial, but the underlying graded-commutative
- cup-product algebra need not be free
+ and any free-polynomial description of the graded-commutative
+ cup-product algebra is conditional on a Massey-vanishing
+ consequence of Fulton--MacPherson formality
  \textup{(}Theorem~H,
  Theorem~\textup{\ref{thm:main-koszul-hoch}},
  Theorem~\textup{\ref{thm:hochschild-polynomial-growth}},
- Proposition~\textup{\ref{prop:e2-formality-hochschild})}.
+ cf.\ Proposition~\textup{\ref{prop:e2-formality-hochschild}}\textup{)}.
 \end{enumerate}
 
 \smallskip
@@ -2207,14 +2208,13 @@
 Theorem~\ref{thm:main-koszul-hoch},
 Theorem~\ref{thm:hochschild-polynomial-growth}, and
 Proposition~\ref{prop:e2-formality-hochschild} give the stated
-cohomological concentration, duality, polynomial Hilbert series,
-and $\Etwo$-formality. The proof of
-Proposition~\ref{prop:e2-formality-hochschild} uses the formality of
-the local configuration spaces $\FM_n(\mathbb{C})$, so the higher
-braces and Massey products on $\ChirHoch^*(\cA)$ are
-cohomologically trivial. This is the full proved content of
-\textup{(viii)} at the theorem level: no freeness statement for the
-underlying graded-commutative cup-product algebra is claimed here.
+cohomological concentration, duality, and polynomial Hilbert
+series. Proposition~\ref{prop:e2-formality-hochschild} isolates the
+Fulton--MacPherson formality input governing higher braces and
+Massey products. Any further free-polynomial refinement of the
+graded-commutative cup-product algebra requires that extra
+Massey-vanishing package and is not part of the unconditional
+equivalence core.
 No converse from
 \textup{(viii)} to the bar-cobar counit is proved here.
 
@@ -2380,21 +2380,15 @@
 residues.
 \end{remark}
 
-\begin{remark}[The strongest proved chiral Hochschild consequence]
-The strengthened form of \textup{(viii)} stops at duality,
-polynomial Hilbert series, and $\Etwo$-formality. It does not imply
-that the underlying graded-commutative algebra
-$\ChirHoch^*(\cA)$ is free. At generic central charge,
-Theorem~\ref{thm:virasoro-hochschild} gives
-\[
-\ChirHoch^*(\mathrm{Vir}_c)\cong \mathbb{C}\oplus \mathbb{C}[-2].
-\]
-The degree-$2$ class squares to zero because
-$\ChirHoch^4(\mathrm{Vir}_c)=0$, whereas a free
-graded-commutative algebra on a degree-$2$ generator would have
-nonzero degree~$4$. Thus vanishing of higher braces and Massey
-products is the strongest proved consequence; ordinary cup-product
-relations may remain.
+\begin{remark}[The theorem-level content of \textup{(viii)}]
+Theorem~\ref{thm:main-koszul-hoch} and
+Theorem~\ref{thm:hochschild-polynomial-growth} prove duality,
+cohomological concentration in degrees~$\{0,1,2\}$, and
+polynomial Hilbert growth on the Koszul locus.
+A further identification of $\ChirHoch^*(\cA)$ as a free
+polynomial algebra is conditional on a Massey-vanishing
+consequence of Fulton--MacPherson formality and is not used in
+the equivalence core.
 \end{remark}
 
 \medskip
@@ -2590,8 +2584,10 @@
 Proposition~\ref{prop:e2-formality-hochschild}
 start from a chiral Koszul datum and compute
 $\ChirHoch^*(\cA)$ by the bar-cobar Hochschild resolution.
-This yields duality, polynomial Hilbert growth, and
-$\Etwo$-formality without routing through
+This yields duality, concentration in degrees~$\{0,1,2\}$, and
+polynomial Hilbert growth. Any free-polynomial upgrade of the
+cup-product algebra is conditional on the Massey-vanishing
+Fulton--MacPherson formality package, so it is not routed through
 \textup{(ii)}--\textup{(vii)} inside the meta-theorem.
 
 \smallskip\noindent

file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 53403b6c5a92d960989ffad4b2d92d19ce2d9058..6929930770084a4025e237c9100b3444f4a2e6c6
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -2074,8 +2074,10 @@
 equivalent to them.
 Condition~\textup{(viii)} is a proved one-way consequence of
 them on the Koszul locus: it yields chiral Hochschild duality,
-polynomial Hilbert series, and $\Etwo$-formality, but it does not
-force the underlying graded-commutative algebra to be free.
+cohomological concentration in degrees~$\{0,1,2\}$, and polynomial
+Hilbert series. Any free-polynomial description of the cup-product
+algebra is conditional on a Massey-vanishing consequence of
+Fulton--MacPherson formality.
 Under the additional perfectness and non-degeneracy hypotheses on the
 ambient tangent complex, condition~\textup{(xi)} is also equivalent to
 them. Condition~\textup{(xii)} implies condition~\textup{(x)}
@@ -2137,14 +2139,13 @@
  P_\cA(t)=\dim Z(\cA)+\dim \ChirHoch^1(\cA)\cdot t
  + \dim Z(\cA^!)\cdot t^2,
  \]
- and $\ChirHoch^*(\cA)$ is formal as an $\Etwo$-algebra:
- all higher braces and Massey products are
- cohomologically trivial, but the underlying graded-commutative
- cup-product algebra need not be free
+ and any free-polynomial description of the graded-commutative
+ cup-product algebra is conditional on a Massey-vanishing
+ consequence of Fulton--MacPherson formality
  \textup{(}Theorem~H,
  Theorem~\textup{\ref{thm:main-koszul-hoch}},
  Theorem~\textup{\ref{thm:hochschild-polynomial-growth}},
- Proposition~\textup{\ref{prop:e2-formality-hochschild})}.
+ cf.\ Proposition~\textup{\ref{prop:e2-formality-hochschild}}\textup{)}.
 \end{enumerate}
 
 \smallskip
@@ -2207,14 +2208,13 @@
 Theorem~\ref{thm:main-koszul-hoch},
 Theorem~\ref{thm:hochschild-polynomial-growth}, and
 Proposition~\ref{prop:e2-formality-hochschild} give the stated
-cohomological concentration, duality, polynomial Hilbert series,
-and $\Etwo$-formality. The proof of
-Proposition~\ref{prop:e2-formality-hochschild} uses the formality of
-the local configuration spaces $\FM_n(\mathbb{C})$, so the higher
-braces and Massey products on $\ChirHoch^*(\cA)$ are
-cohomologically trivial. This is the full proved content of
-\textup{(viii)} at the theorem level: no freeness statement for the
-underlying graded-commutative cup-product algebra is claimed here.
+cohomological concentration, duality, and polynomial Hilbert
+series. Proposition~\ref{prop:e2-formality-hochschild} isolates the
+Fulton--MacPherson formality input governing higher braces and
+Massey products. Any further free-polynomial refinement of the
+graded-commutative cup-product algebra requires that extra
+Massey-vanishing package and is not part of the unconditional
+equivalence core.
 No converse from
 \textup{(viii)} to the bar-cobar counit is proved here.
 
@@ -2380,21 +2380,15 @@
 residues.
 \end{remark}
 
-\begin{remark}[The strongest proved chiral Hochschild consequence]
-The strengthened form of \textup{(viii)} stops at duality,
-polynomial Hilbert series, and $\Etwo$-formality. It does not imply
-that the underlying graded-commutative algebra
-$\ChirHoch^*(\cA)$ is free. At generic central charge,
-Theorem~\ref{thm:virasoro-hochschild} gives
-\[
-\ChirHoch^*(\mathrm{Vir}_c)\cong \mathbb{C}\oplus \mathbb{C}[-2].
-\]
-The degree-$2$ class squares to zero because
-$\ChirHoch^4(\mathrm{Vir}_c)=0$, whereas a free
-graded-commutative algebra on a degree-$2$ generator would have
-nonzero degree~$4$. Thus vanishing of higher braces and Massey
-products is the strongest proved consequence; ordinary cup-product
-relations may remain.
+\begin{remark}[The theorem-level content of \textup{(viii)}]
+Theorem~\ref{thm:main-koszul-hoch} and
+Theorem~\ref{thm:hochschild-polynomial-growth} prove duality,
+cohomological concentration in degrees~$\{0,1,2\}$, and
+polynomial Hilbert growth on the Koszul locus.
+A further identification of $\ChirHoch^*(\cA)$ as a free
+polynomial algebra is conditional on a Massey-vanishing
+consequence of Fulton--MacPherson formality and is not used in
+the equivalence core.
 \end{remark}
 
 \medskip
@@ -2590,8 +2584,10 @@
 Proposition~\ref{prop:e2-formality-hochschild}
 start from a chiral Koszul datum and compute
 $\ChirHoch^*(\cA)$ by the bar-cobar Hochschild resolution.
-This yields duality, polynomial Hilbert growth, and
-$\Etwo$-formality without routing through
+This yields duality, concentration in degrees~$\{0,1,2\}$, and
+polynomial Hilbert growth. Any free-polynomial upgrade of the
+cup-product algebra is conditional on the Massey-vanishing
+Fulton--MacPherson formality package, so it is not routed through
 \textup{(ii)}--\textup{(vii)} inside the meta-theorem.
 
 \smallskip\noindent


thinking
**Verifying file contents**

I need to check the file for the edited chunks. I might want to use grep to look for the phrase "need not be free" and see if there's anything about free polynomial in the file as well. There’s definitely some specifics to find there! I’ll make sure to accurately identify those sections. It’s important to be thorough in this step to ensure everything is correct!
codex
The edits are in. I’m re-reading the touched blocks and running focused greps now to make sure the `(viii)` lane no longer advertises unconditional free-polynomial Hochschild, and that I didn’t introduce new AP-style phrasing drift.
exec
/bin/zsh -lc "sed -n '2383,2396p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2204,2223p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2072,2148p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\begin{remark}[The theorem-level content of \textup{(viii)}]
Theorem~\ref{thm:main-koszul-hoch} and
Theorem~\ref{thm:hochschild-polynomial-growth} prove duality,
cohomological concentration in degrees~$\{0,1,2\}$, and
polynomial Hilbert growth on the Koszul locus.
A further identification of $\ChirHoch^*(\cA)$ as a free
polynomial algebra is conditional on a Massey-vanishing
consequence of Fulton--MacPherson formality and is not used in
the equivalence core.
\end{remark}

\medskip
\textsc{FM boundary acyclicity}
\textup{(i)}$\Leftrightarrow$\textup{(x)}:
 succeeded in 51ms:
The quasi-isomorphism
$\Omega(\barBgeom(\cA)) \xrightarrow{\sim} \cA$ identifies the
bar-cobar resolution with the chiral Hochschild complex. On the
Koszul locus, Theorem~H,
Theorem~\ref{thm:main-koszul-hoch},
Theorem~\ref{thm:hochschild-polynomial-growth}, and
Proposition~\ref{prop:e2-formality-hochschild} give the stated
cohomological concentration, duality, and polynomial Hilbert
series. Proposition~\ref{prop:e2-formality-hochschild} isolates the
Fulton--MacPherson formality input governing higher braces and
Massey products. Any further free-polynomial refinement of the
graded-commutative cup-product algebra requires that extra
Massey-vanishing package and is not part of the unconditional
equivalence core.
No converse from
\textup{(viii)} to the bar-cobar counit is proved here.

\medskip
\textsc{$A_\infty$ formality}
\textup{(i)}$\Leftrightarrow$\textup{(iii)}:
 succeeded in 52ms:
On the uniform-weight lane, condition~\textup{(vii)} strengthens to
the all-genera concentration statement recorded there and remains
equivalent to them.
Condition~\textup{(viii)} is a proved one-way consequence of
them on the Koszul locus: it yields chiral Hochschild duality,
cohomological concentration in degrees~$\{0,1,2\}$, and polynomial
Hilbert series. Any free-polynomial description of the cup-product
algebra is conditional on a Massey-vanishing consequence of
Fulton--MacPherson formality.
Under the additional perfectness and non-degeneracy hypotheses on the
ambient tangent complex, condition~\textup{(xi)} is also equivalent to
them. Condition~\textup{(xii)} implies condition~\textup{(x)}
(Remark~\ref{rem:d-module-purity-content}); the converse is open.

\smallskip
\noindent\textbf{Unconditional equivalences:}
\begin{enumerate}
\item[\textup{(i)}] $\cA$ is chirally Koszul
 \textup{(}Definition~\textup{\ref{def:chiral-koszul-morphism})}.
\item[\textup{(ii)}] The PBW spectral sequence on
exec
/bin/zsh -lc "sed -n '2586,2598p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -e 'free polynomial' -e 'need not be free' -e 'no freeness statement' -e 'does not.*free' -e 'Etwo-formality, but' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -i 'moreover|additionally|notably|crucially|remarkably|furthermore|we now|it is worth noting|worth mentioning|it should be noted|it is important to note|delve|leverage|tapestry|cornerstone|journey|navigate|—|---' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
$\ChirHoch^*(\cA)$ by the bar-cobar Hochschild resolution.
This yields duality, concentration in degrees~$\{0,1,2\}$, and
polynomial Hilbert growth. Any free-polynomial upgrade of the
cup-product algebra is conditional on the Massey-vanishing
Fulton--MacPherson formality package, so it is not routed through
\textup{(ii)}--\textup{(vii)} inside the meta-theorem.

\smallskip\noindent
\textup{(iii)}$\Rightarrow$\textup{(x)} is fiberwise and geometric.
For a boundary stratum $S_T$, the restriction
$i_{S_T}^!\,\barB_n(\cA)$ decomposes as the tensor product of the
vertexwise collision complexes, and
Remark~\ref{rem:iterated-residues-ainfty}
 exited 1 in 52ms:

 succeeded in 51ms:
3041:$G$ & $=0$ & $=0$ & $=0$ & --- \\
file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 53403b6c5a92d960989ffad4b2d92d19ce2d9058..6929930770084a4025e237c9100b3444f4a2e6c6
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -2074,8 +2074,10 @@
 equivalent to them.
 Condition~\textup{(viii)} is a proved one-way consequence of
 them on the Koszul locus: it yields chiral Hochschild duality,
-polynomial Hilbert series, and $\Etwo$-formality, but it does not
-force the underlying graded-commutative algebra to be free.
+cohomological concentration in degrees~$\{0,1,2\}$, and polynomial
+Hilbert series. Any free-polynomial description of the cup-product
+algebra is conditional on a Massey-vanishing consequence of
+Fulton--MacPherson formality.
 Under the additional perfectness and non-degeneracy hypotheses on the
 ambient tangent complex, condition~\textup{(xi)} is also equivalent to
 them. Condition~\textup{(xii)} implies condition~\textup{(x)}
@@ -2137,14 +2139,13 @@
  P_\cA(t)=\dim Z(\cA)+\dim \ChirHoch^1(\cA)\cdot t
  + \dim Z(\cA^!)\cdot t^2,
  \]
- and $\ChirHoch^*(\cA)$ is formal as an $\Etwo$-algebra:
- all higher braces and Massey products are
- cohomologically trivial, but the underlying graded-commutative
- cup-product algebra need not be free
+ and any free-polynomial description of the graded-commutative
+ cup-product algebra is conditional on a Massey-vanishing
+ consequence of Fulton--MacPherson formality
  \textup{(}Theorem~H,
  Theorem~\textup{\ref{thm:main-koszul-hoch}},
  Theorem~\textup{\ref{thm:hochschild-polynomial-growth}},
- Proposition~\textup{\ref{prop:e2-formality-hochschild})}.
+ cf.\ Proposition~\textup{\ref{prop:e2-formality-hochschild}}\textup{)}.
 \end{enumerate}
 
 \smallskip
@@ -2207,14 +2208,13 @@
 Theorem~\ref{thm:main-koszul-hoch},
 Theorem~\ref{thm:hochschild-polynomial-growth}, and
 Proposition~\ref{prop:e2-formality-hochschild} give the stated
-cohomological concentration, duality, polynomial Hilbert series,
-and $\Etwo$-formality. The proof of
-Proposition~\ref{prop:e2-formality-hochschild} uses the formality of
-the local configuration spaces $\FM_n(\mathbb{C})$, so the higher
-braces and Massey products on $\ChirHoch^*(\cA)$ are
-cohomologically trivial. This is the full proved content of
-\textup{(viii)} at the theorem level: no freeness statement for the
-underlying graded-commutative cup-product algebra is claimed here.
+cohomological concentration, duality, and polynomial Hilbert
+series. Proposition~\ref{prop:e2-formality-hochschild} isolates the
+Fulton--MacPherson formality input governing higher braces and
+Massey products. Any further free-polynomial refinement of the
+graded-commutative cup-product algebra requires that extra
+Massey-vanishing package and is not part of the unconditional
+equivalence core.
 No converse from
 \textup{(viii)} to the bar-cobar counit is proved here.
 
@@ -2380,21 +2380,15 @@
 residues.
 \end{remark}
 
-\begin{remark}[The strongest proved chiral Hochschild consequence]
-The strengthened form of \textup{(viii)} stops at duality,
-polynomial Hilbert series, and $\Etwo$-formality. It does not imply
-that the underlying graded-commutative algebra
-$\ChirHoch^*(\cA)$ is free. At generic central charge,
-Theorem~\ref{thm:virasoro-hochschild} gives
-\[
-\ChirHoch^*(\mathrm{Vir}_c)\cong \mathbb{C}\oplus \mathbb{C}[-2].
-\]
-The degree-$2$ class squares to zero because
-$\ChirHoch^4(\mathrm{Vir}_c)=0$, whereas a free
-graded-commutative algebra on a degree-$2$ generator would have
-nonzero degree~$4$. Thus vanishing of higher braces and Massey
-products is the strongest proved consequence; ordinary cup-product
-relations may remain.
+\begin{remark}[The theorem-level content of \textup{(viii)}]
+Theorem~\ref{thm:main-koszul-hoch} and
+Theorem~\ref{thm:hochschild-polynomial-growth} prove duality,
+cohomological concentration in degrees~$\{0,1,2\}$, and
+polynomial Hilbert growth on the Koszul locus.
+A further identification of $\ChirHoch^*(\cA)$ as a free
+polynomial algebra is conditional on a Massey-vanishing
+consequence of Fulton--MacPherson formality and is not used in
+the equivalence core.
 \end{remark}
 
 \medskip
@@ -2590,8 +2584,10 @@
 Proposition~\ref{prop:e2-formality-hochschild}
 start from a chiral Koszul datum and compute
 $\ChirHoch^*(\cA)$ by the bar-cobar Hochschild resolution.
-This yields duality, polynomial Hilbert growth, and
-$\Etwo$-formality without routing through
+This yields duality, concentration in degrees~$\{0,1,2\}$, and
+polynomial Hilbert growth. Any free-polynomial upgrade of the
+cup-product algebra is conditional on the Massey-vanishing
+Fulton--MacPherson formality package, so it is not routed through
 \textup{(ii)}--\textup{(vii)} inside the meta-theorem.
 
 \smallskip\noindent

codex
The local grep is clean for the old unconditional freeness phrases. I’m doing one final diff/readback pass now so I can report exactly what changed and whether anything remains blocked in this narrow scope.
exec
/bin/zsh -lc 'git diff -- chapters/theory/chiral_koszul_pairs.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 57a0eb1..6929930 100644
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -2074,8 +2074,10 @@ the all-genera concentration statement recorded there and remains
 equivalent to them.
 Condition~\textup{(viii)} is a proved one-way consequence of
 them on the Koszul locus: it yields chiral Hochschild duality,
-polynomial Hilbert series, and $\Etwo$-formality, but it does not
-force the underlying graded-commutative algebra to be free.
+cohomological concentration in degrees~$\{0,1,2\}$, and polynomial
+Hilbert series. Any free-polynomial description of the cup-product
+algebra is conditional on a Massey-vanishing consequence of
+Fulton--MacPherson formality.
 Under the additional perfectness and non-degeneracy hypotheses on the
 ambient tangent complex, condition~\textup{(xi)} is also equivalent to
 them. Condition~\textup{(xii)} implies condition~\textup{(x)}
@@ -2137,14 +2139,13 @@ them. Condition~\textup{(xii)} implies condition~\textup{(x)}
  P_\cA(t)=\dim Z(\cA)+\dim \ChirHoch^1(\cA)\cdot t
  + \dim Z(\cA^!)\cdot t^2,
exec
/bin/zsh -lc "rg -n \"free[- ]polynomial|Massey-vanishing|Fulton--MacPherson formality|\\(viii\\)\" chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
2075:Condition~\textup{(viii)} is a proved one-way consequence of
2078:Hilbert series. Any free-polynomial description of the cup-product
2079:algebra is conditional on a Massey-vanishing consequence of
2080:Fulton--MacPherson formality.
2131:\item[\textup{(viii)}] $\mathrm{ChirHoch}^*(\cA)$ is concentrated in
2142: and any free-polynomial description of the graded-commutative
2143: cup-product algebra is conditional on a Massey-vanishing
2144: consequence of Fulton--MacPherson formality
2201:\textup{(v)}$\Rightarrow$\textup{(viii)}:
2213:Fulton--MacPherson formality input governing higher braces and
2214:Massey products. Any further free-polynomial refinement of the
2216:Massey-vanishing package and is not part of the unconditional
2219:\textup{(viii)} to the bar-cobar counit is proved here.
2383:\begin{remark}[The theorem-level content of \textup{(viii)}]
2389:polynomial algebra is conditional on a Massey-vanishing
2390:consequence of Fulton--MacPherson formality and is not used in
2581:\textup{(i)}$\Rightarrow$\textup{(viii)} is also direct.
2588:polynomial Hilbert growth. Any free-polynomial upgrade of the
2589:cup-product algebra is conditional on the Massey-vanishing
2590:Fulton--MacPherson formality package, so it is not routed through
file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 53403b6c5a92d960989ffad4b2d92d19ce2d9058..6929930770084a4025e237c9100b3444f4a2e6c6
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -2074,8 +2074,10 @@
 equivalent to them.
 Condition~\textup{(viii)} is a proved one-way consequence of
 them on the Koszul locus: it yields chiral Hochschild duality,
-polynomial Hilbert series, and $\Etwo$-formality, but it does not
-force the underlying graded-commutative algebra to be free.
+cohomological concentration in degrees~$\{0,1,2\}$, and polynomial
+Hilbert series. Any free-polynomial description of the cup-product
+algebra is conditional on a Massey-vanishing consequence of
+Fulton--MacPherson formality.
 Under the additional perfectness and non-degeneracy hypotheses on the
 ambient tangent complex, condition~\textup{(xi)} is also equivalent to
 them. Condition~\textup{(xii)} implies condition~\textup{(x)}
@@ -2137,14 +2139,13 @@
  P_\cA(t)=\dim Z(\cA)+\dim \ChirHoch^1(\cA)\cdot t
  + \dim Z(\cA^!)\cdot t^2,
  \]
- and $\ChirHoch^*(\cA)$ is formal as an $\Etwo$-algebra:
- all higher braces and Massey products are
- cohomologically trivial, but the underlying graded-commutative
- cup-product algebra need not be free
+ and any free-polynomial description of the graded-commutative
+ cup-product algebra is conditional on a Massey-vanishing
+ consequence of Fulton--MacPherson formality
  \textup{(}Theorem~H,
  Theorem~\textup{\ref{thm:main-koszul-hoch}},
  Theorem~\textup{\ref{thm:hochschild-polynomial-growth}},
- Proposition~\textup{\ref{prop:e2-formality-hochschild})}.
+ cf.\ Proposition~\textup{\ref{prop:e2-formality-hochschild}}\textup{)}.
 \end{enumerate}
 
 \smallskip
@@ -2207,14 +2208,13 @@
 Theorem~\ref{thm:main-koszul-hoch},
 Theorem~\ref{thm:hochschild-polynomial-growth}, and
 Proposition~\ref{prop:e2-formality-hochschild} give the stated
-cohomological concentration, duality, polynomial Hilbert series,
-and $\Etwo$-formality. The proof of
-Proposition~\ref{prop:e2-formality-hochschild} uses the formality of
-the local configuration spaces $\FM_n(\mathbb{C})$, so the higher
-braces and Massey products on $\ChirHoch^*(\cA)$ are
-cohomologically trivial. This is the full proved content of
-\textup{(viii)} at the theorem level: no freeness statement for the
-underlying graded-commutative cup-product algebra is claimed here.
+cohomological concentration, duality, and polynomial Hilbert
+series. Proposition~\ref{prop:e2-formality-hochschild} isolates the
+Fulton--MacPherson formality input governing higher braces and
+Massey products. Any further free-polynomial refinement of the
+graded-commutative cup-product algebra requires that extra
+Massey-vanishing package and is not part of the unconditional
+equivalence core.
 No converse from
 \textup{(viii)} to the bar-cobar counit is proved here.
 
@@ -2380,21 +2380,15 @@
 residues.
 \end{remark}
 
-\begin{remark}[The strongest proved chiral Hochschild consequence]
-The strengthened form of \textup{(viii)} stops at duality,
-polynomial Hilbert series, and $\Etwo$-formality. It does not imply
-that the underlying graded-commutative algebra
-$\ChirHoch^*(\cA)$ is free. At generic central charge,
-Theorem~\ref{thm:virasoro-hochschild} gives
-\[
-\ChirHoch^*(\mathrm{Vir}_c)\cong \mathbb{C}\oplus \mathbb{C}[-2].
-\]
-The degree-$2$ class squares to zero because
-$\ChirHoch^4(\mathrm{Vir}_c)=0$, whereas a free
-graded-commutative algebra on a degree-$2$ generator would have
-nonzero degree~$4$. Thus vanishing of higher braces and Massey
-products is the strongest proved consequence; ordinary cup-product
-relations may remain.
+\begin{remark}[The theorem-level content of \textup{(viii)}]
+Theorem~\ref{thm:main-koszul-hoch} and
+Theorem~\ref{thm:hochschild-polynomial-growth} prove duality,
+cohomological concentration in degrees~$\{0,1,2\}$, and
+polynomial Hilbert growth on the Koszul locus.
+A further identification of $\ChirHoch^*(\cA)$ as a free
+polynomial algebra is conditional on a Massey-vanishing
+consequence of Fulton--MacPherson formality and is not used in
+the equivalence core.
 \end{remark}
 
 \medskip
@@ -2590,8 +2584,10 @@
 Proposition~\ref{prop:e2-formality-hochschild}
 start from a chiral Koszul datum and compute
 $\ChirHoch^*(\cA)$ by the bar-cobar Hochschild resolution.
-This yields duality, polynomial Hilbert growth, and
-$\Etwo$-formality without routing through
+This yields duality, concentration in degrees~$\{0,1,2\}$, and
+polynomial Hilbert growth. Any free-polynomial upgrade of the
+cup-product algebra is conditional on the Massey-vanishing
+Fulton--MacPherson formality package, so it is not routed through
 \textup{(ii)}--\textup{(vii)} inside the meta-theorem.
 
 \smallskip\noindent



thinking
**Considering LaTeX build options**

I’m pondering whether to run `latexmk -pdf -interaction=nonstopmode -halt-on-error -silent -jobname=/tmp/chiral-bar-cobar-test main.tex`. It could be costly in terms of resources, and I have time to check if it's available. Maybe I could use the `build-surface` skill, but that feels unnecessary for a small task. AGENTS recommend a targeted TeX build, but since this is a minor file edit, a minimal LaTeX build might be sufficient. If issues arise, I may have to assess them carefully.
thinking
**Exploring LaTeX options**

I'm considering running `lualatex -draftmode -interaction=nonstopmode -halt-on-error '\\input{chapters/theory/chiral_koszul_pairs.tex}'`, but it seems context is missing, which makes it impossible. So, I’m wondering if it might be better to run `git diff` and use `sed` for verification instead. That could potentially provide enough information without unnecessary complications. I want to make sure I’m making the right choice without overlooking anything important!
exec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '2581,2592p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '2208,2220p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '2074,2148p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '2383,2392p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  2581	\textup{(i)}$\Rightarrow$\textup{(viii)} is also direct.
  2582	Theorem~\ref{thm:main-koszul-hoch},
  2583	Theorem~\ref{thm:hochschild-polynomial-growth}, and
  2584	Proposition~\ref{prop:e2-formality-hochschild}
  2585	start from a chiral Koszul datum and compute
  2586	$\ChirHoch^*(\cA)$ by the bar-cobar Hochschild resolution.
  2587	This yields duality, concentration in degrees~$\{0,1,2\}$, and
  2588	polynomial Hilbert growth. Any free-polynomial upgrade of the
  2589	cup-product algebra is conditional on the Massey-vanishing
  2590	Fulton--MacPherson formality package, so it is not routed through
  2591	\textup{(ii)}--\textup{(vii)} inside the meta-theorem.
  2592	
 succeeded in 52ms:
  2208	Theorem~\ref{thm:main-koszul-hoch},
  2209	Theorem~\ref{thm:hochschild-polynomial-growth}, and
  2210	Proposition~\ref{prop:e2-formality-hochschild} give the stated
  2211	cohomological concentration, duality, and polynomial Hilbert
  2212	series. Proposition~\ref{prop:e2-formality-hochschild} isolates the
  2213	Fulton--MacPherson formality input governing higher braces and
  2214	Massey products. Any further free-polynomial refinement of the
  2215	graded-commutative cup-product algebra requires that extra
  2216	Massey-vanishing package and is not part of the unconditional
  2217	equivalence core.
  2218	No converse from
  2219	\textup{(viii)} to the bar-cobar counit is proved here.
  2220	
 succeeded in 51ms:
  2074	equivalent to them.
  2075	Condition~\textup{(viii)} is a proved one-way consequence of
  2076	them on the Koszul locus: it yields chiral Hochschild duality,
  2077	cohomological concentration in degrees~$\{0,1,2\}$, and polynomial
  2078	Hilbert series. Any free-polynomial description of the cup-product
  2079	algebra is conditional on a Massey-vanishing consequence of
  2080	Fulton--MacPherson formality.
  2081	Under the additional perfectness and non-degeneracy hypotheses on the
  2082	ambient tangent complex, condition~\textup{(xi)} is also equivalent to
  2083	them. Condition~\textup{(xii)} implies condition~\textup{(x)}
  2084	(Remark~\ref{rem:d-module-purity-content}); the converse is open.
  2085	
  2086	\smallskip
  2087	\noindent\textbf{Unconditional equivalences:}
  2088	\begin{enumerate}
  2089	\item[\textup{(i)}] $\cA$ is chirally Koszul
  2090	 \textup{(}Definition~\textup{\ref{def:chiral-koszul-morphism})}.
  2091	\item[\textup{(ii)}] The PBW spectral sequence on
  2092	 $\barBgeom(\cA)$ collapses at $E_2$
  2093	 \textup{(}Theorem~\textup{\ref{thm:pbw-koszulness-criterion})}.
 succeeded in 51ms:
  2383	\begin{remark}[The theorem-level content of \textup{(viii)}]
  2384	Theorem~\ref{thm:main-koszul-hoch} and
  2385	Theorem~\ref{thm:hochschild-polynomial-growth} prove duality,
  2386	cohomological concentration in degrees~$\{0,1,2\}$, and
  2387	polynomial Hilbert growth on the Koszul locus.
  2388	A further identification of $\ChirHoch^*(\cA)$ as a free
  2389	polynomial algebra is conditional on a Massey-vanishing
  2390	consequence of Fulton--MacPherson formality and is not used in
  2391	the equivalence core.
  2392	\end{remark}
file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 53403b6c5a92d960989ffad4b2d92d19ce2d9058..6929930770084a4025e237c9100b3444f4a2e6c6
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -2074,8 +2074,10 @@
 equivalent to them.
 Condition~\textup{(viii)} is a proved one-way consequence of
 them on the Koszul locus: it yields chiral Hochschild duality,
-polynomial Hilbert series, and $\Etwo$-formality, but it does not
-force the underlying graded-commutative algebra to be free.
+cohomological concentration in degrees~$\{0,1,2\}$, and polynomial
+Hilbert series. Any free-polynomial description of the cup-product
+algebra is conditional on a Massey-vanishing consequence of
+Fulton--MacPherson formality.
 Under the additional perfectness and non-degeneracy hypotheses on the
 ambient tangent complex, condition~\textup{(xi)} is also equivalent to
 them. Condition~\textup{(xii)} implies condition~\textup{(x)}
@@ -2137,14 +2139,13 @@
  P_\cA(t)=\dim Z(\cA)+\dim \ChirHoch^1(\cA)\cdot t
  + \dim Z(\cA^!)\cdot t^2,
  \]
- and $\ChirHoch^*(\cA)$ is formal as an $\Etwo$-algebra:
- all higher braces and Massey products are
- cohomologically trivial, but the underlying graded-commutative
- cup-product algebra need not be free
+ and any free-polynomial description of the graded-commutative
+ cup-product algebra is conditional on a Massey-vanishing
+ consequence of Fulton--MacPherson formality
  \textup{(}Theorem~H,
  Theorem~\textup{\ref{thm:main-koszul-hoch}},
  Theorem~\textup{\ref{thm:hochschild-polynomial-growth}},
- Proposition~\textup{\ref{prop:e2-formality-hochschild})}.
+ cf.\ Proposition~\textup{\ref{prop:e2-formality-hochschild}}\textup{)}.
 \end{enumerate}
 
 \smallskip
@@ -2207,14 +2208,13 @@
 Theorem~\ref{thm:main-koszul-hoch},
 Theorem~\ref{thm:hochschild-polynomial-growth}, and
 Proposition~\ref{prop:e2-formality-hochschild} give the stated
-cohomological concentration, duality, polynomial Hilbert series,
-and $\Etwo$-formality. The proof of
-Proposition~\ref{prop:e2-formality-hochschild} uses the formality of
-the local configuration spaces $\FM_n(\mathbb{C})$, so the higher
-braces and Massey products on $\ChirHoch^*(\cA)$ are
-cohomologically trivial. This is the full proved content of
-\textup{(viii)} at the theorem level: no freeness statement for the
-underlying graded-commutative cup-product algebra is claimed here.
+cohomological concentration, duality, and polynomial Hilbert
+series. Proposition~\ref{prop:e2-formality-hochschild} isolates the
+Fulton--MacPherson formality input governing higher braces and
+Massey products. Any further free-polynomial refinement of the
+graded-commutative cup-product algebra requires that extra
+Massey-vanishing package and is not part of the unconditional
+equivalence core.
 No converse from
 \textup{(viii)} to the bar-cobar counit is proved here.
 
@@ -2380,21 +2380,15 @@
 residues.
 \end{remark}
 
-\begin{remark}[The strongest proved chiral Hochschild consequence]
-The strengthened form of \textup{(viii)} stops at duality,
-polynomial Hilbert series, and $\Etwo$-formality. It does not imply
-that the underlying graded-commutative algebra
-$\ChirHoch^*(\cA)$ is free. At generic central charge,
-Theorem~\ref{thm:virasoro-hochschild} gives
-\[
-\ChirHoch^*(\mathrm{Vir}_c)\cong \mathbb{C}\oplus \mathbb{C}[-2].
-\]
-The degree-$2$ class squares to zero because
-$\ChirHoch^4(\mathrm{Vir}_c)=0$, whereas a free
-graded-commutative algebra on a degree-$2$ generator would have
-nonzero degree~$4$. Thus vanishing of higher braces and Massey
-products is the strongest proved consequence; ordinary cup-product
-relations may remain.
+\begin{remark}[The theorem-level content of \textup{(viii)}]
+Theorem~\ref{thm:main-koszul-hoch} and
+Theorem~\ref{thm:hochschild-polynomial-growth} prove duality,
+cohomological concentration in degrees~$\{0,1,2\}$, and
+polynomial Hilbert growth on the Koszul locus.
+A further identification of $\ChirHoch^*(\cA)$ as a free
+polynomial algebra is conditional on a Massey-vanishing
+consequence of Fulton--MacPherson formality and is not used in
+the equivalence core.
 \end{remark}
 
 \medskip
@@ -2590,8 +2584,10 @@
 Proposition~\ref{prop:e2-formality-hochschild}
 start from a chiral Koszul datum and compute
 $\ChirHoch^*(\cA)$ by the bar-cobar Hochschild resolution.
-This yields duality, polynomial Hilbert growth, and
-$\Etwo$-formality without routing through
+This yields duality, concentration in degrees~$\{0,1,2\}$, and
+polynomial Hilbert growth. Any free-polynomial upgrade of the
+cup-product algebra is conditional on the Massey-vanishing
+Fulton--MacPherson formality package, so it is not routed through
 \textup{(ii)}--\textup{(vii)} inside the meta-theorem.
 
 \smallskip\noindent


thinking
**Checking for typos and formatting**

I’m thinking we should check for any new typos, like the one with `cf.\`, just to be careful. It looks like the theorem item might be missing punctuation at the end too. I'm wondering if we actually closed the parentheses and included a period. The item ends with `\textup{)}`, but there’s no final period there. I want to make sure we’ve got all the details right!
codex
FIXED. I repaired Koszul equivalence `(viii)` in [chiral_koszul_pairs.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex:2075) and synced the local theorem lane at [item `(viii)`](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex:2131), its [proof recap](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex:2210), the [follow-up remark](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex:2383), and the later [summary paragraph](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex:2581). The text now says the proved content is duality plus concentration in degrees `{0,1,2}` plus polynomial Hilbert series, and any free-polynomial cup-product statement is conditional on a Massey-vanishing consequence of Fulton--MacPherson formality.

Verification: I re-read the touched blocks and grepped the file for the old unconditional freeness wording; none remains in the `(viii)` lane. I did not run a full TeX build. There is one unrelated pre-existing `---` hit at [chiral_koszul_pairs.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex:3041), outside this scope.
file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 53403b6c5a92d960989ffad4b2d92d19ce2d9058..6929930770084a4025e237c9100b3444f4a2e6c6
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -2074,8 +2074,10 @@
 equivalent to them.
 Condition~\textup{(viii)} is a proved one-way consequence of
 them on the Koszul locus: it yields chiral Hochschild duality,
-polynomial Hilbert series, and $\Etwo$-formality, but it does not
-force the underlying graded-commutative algebra to be free.
+cohomological concentration in degrees~$\{0,1,2\}$, and polynomial
+Hilbert series. Any free-polynomial description of the cup-product
+algebra is conditional on a Massey-vanishing consequence of
+Fulton--MacPherson formality.
 Under the additional perfectness and non-degeneracy hypotheses on the
 ambient tangent complex, condition~\textup{(xi)} is also equivalent to
 them. Condition~\textup{(xii)} implies condition~\textup{(x)}
@@ -2137,14 +2139,13 @@
  P_\cA(t)=\dim Z(\cA)+\dim \ChirHoch^1(\cA)\cdot t
  + \dim Z(\cA^!)\cdot t^2,
  \]
- and $\ChirHoch^*(\cA)$ is formal as an $\Etwo$-algebra:
- all higher braces and Massey products are
- cohomologically trivial, but the underlying graded-commutative
- cup-product algebra need not be free
+ and any free-polynomial description of the graded-commutative
+ cup-product algebra is conditional on a Massey-vanishing
+ consequence of Fulton--MacPherson formality
  \textup{(}Theorem~H,
  Theorem~\textup{\ref{thm:main-koszul-hoch}},
  Theorem~\textup{\ref{thm:hochschild-polynomial-growth}},
- Proposition~\textup{\ref{prop:e2-formality-hochschild})}.
+ cf.\ Proposition~\textup{\ref{prop:e2-formality-hochschild}}\textup{)}.
 \end{enumerate}
 
 \smallskip
@@ -2207,14 +2208,13 @@
 Theorem~\ref{thm:main-koszul-hoch},
 Theorem~\ref{thm:hochschild-polynomial-growth}, and
 Proposition~\ref{prop:e2-formality-hochschild} give the stated
-cohomological concentration, duality, polynomial Hilbert series,
-and $\Etwo$-formality. The proof of
-Proposition~\ref{prop:e2-formality-hochschild} uses the formality of
-the local configuration spaces $\FM_n(\mathbb{C})$, so the higher
-braces and Massey products on $\ChirHoch^*(\cA)$ are
-cohomologically trivial. This is the full proved content of
-\textup{(viii)} at the theorem level: no freeness statement for the
-underlying graded-commutative cup-product algebra is claimed here.
+cohomological concentration, duality, and polynomial Hilbert
+series. Proposition~\ref{prop:e2-formality-hochschild} isolates the
+Fulton--MacPherson formality input governing higher braces and
+Massey products. Any further free-polynomial refinement of the
+graded-commutative cup-product algebra requires that extra
+Massey-vanishing package and is not part of the unconditional
+equivalence core.
 No converse from
 \textup{(viii)} to the bar-cobar counit is proved here.
 
@@ -2380,21 +2380,15 @@
 residues.
 \end{remark}
 
-\begin{remark}[The strongest proved chiral Hochschild consequence]
-The strengthened form of \textup{(viii)} stops at duality,
-polynomial Hilbert series, and $\Etwo$-formality. It does not imply
-that the underlying graded-commutative algebra
-$\ChirHoch^*(\cA)$ is free. At generic central charge,
-Theorem~\ref{thm:virasoro-hochschild} gives
-\[
-\ChirHoch^*(\mathrm{Vir}_c)\cong \mathbb{C}\oplus \mathbb{C}[-2].
-\]
-The degree-$2$ class squares to zero because
-$\ChirHoch^4(\mathrm{Vir}_c)=0$, whereas a free
-graded-commutative algebra on a degree-$2$ generator would have
-nonzero degree~$4$. Thus vanishing of higher braces and Massey
-products is the strongest proved consequence; ordinary cup-product
-relations may remain.
+\begin{remark}[The theorem-level content of \textup{(viii)}]
+Theorem~\ref{thm:main-koszul-hoch} and
+Theorem~\ref{thm:hochschild-polynomial-growth} prove duality,
+cohomological concentration in degrees~$\{0,1,2\}$, and
+polynomial Hilbert growth on the Koszul locus.
+A further identification of $\ChirHoch^*(\cA)$ as a free
+polynomial algebra is conditional on a Massey-vanishing
+consequence of Fulton--MacPherson formality and is not used in
+the equivalence core.
 \end{remark}
 
 \medskip
@@ -2590,8 +2584,10 @@
 Proposition~\ref{prop:e2-formality-hochschild}
 start from a chiral Koszul datum and compute
 $\ChirHoch^*(\cA)$ by the bar-cobar Hochschild resolution.
-This yields duality, polynomial Hilbert growth, and
-$\Etwo$-formality without routing through
+This yields duality, concentration in degrees~$\{0,1,2\}$, and
+polynomial Hilbert growth. Any free-polynomial upgrade of the
+cup-product algebra is conditional on the Massey-vanishing
+Fulton--MacPherson formality package, so it is not routed through
 \textup{(ii)}--\textup{(vii)} inside the meta-theorem.
 
 \smallskip\noindent

tokens used
190,206
