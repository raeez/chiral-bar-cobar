# B08_fix_broken_refs_v3 (349s)

Updated [chapters/examples/k3_times_e.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3_times_e.tex).

- `FIXED` `ch:holographic-datum-master` at both broken sites by retargeting to `ch:cy-holographic-datum-master`.
- `FIXED` `sec:mo-r-matrix` by retargeting it to `sec:k3e-mo-rmatrix`.
- `FIXED` `thm:k3e-wall-crossing-mc` by retargeting it to the live MC-gauge theorem `thm:ks-mc-gauge`.
- `FIXED` `thm:obstruction-recursion` by retargeting it to the live Vol I stub label `thm:riccati-algebraicity`.
- `FIXED` `thm:denom-bar-euler` by retargeting it to the live Vol I stub label `thm:lattice-voa-bar`.
- `FIXED` `ex:k3-step1` by removing the dead note-only reference and inlining the sentence’s actual content.

Verification passed:
- Static label scan over `main.tex`, `chapters/`, and `appendices/`: `MISSING 0`.
- Grep for the stale labels in the modified file: no matches.
- `make fast`: converged after 2 passes with `0 undef references` and `0 undef citations`.

No blockers.


---
STDERR:
OpenAI Codex v0.104.0 (research preview)
--------
workdir: /Users/raeez/calabi-yau-quantum-groups
model: gpt-5.4
provider: openai
approval: never
sandbox: workspace-write [workdir, /tmp, $TMPDIR]
reasoning effort: xhigh
reasoning summaries: auto
session id: 019d87ba-1100-7ee0-a17a-65682456a49f
--------
user
<task>
You are a SURGICAL FIX agent. Read the audit findings, read the source, make the MINIMUM
truthful edit that resolves each finding. Do NOT rewrite sections that are correct.
For each edit: verify it doesn't break surrounding context.
</task>
<action_safety>
Only edit files explicitly assigned. Keep changes tightly scoped.
After editing, re-read to verify coherence. Check \ref and \label validity.
</action_safety>
<completeness_contract>
Address EVERY finding listed. For each: state FIXED (how) or BLOCKED (why).
</completeness_contract>
<verification_loop>
After all edits, grep for forbidden patterns in the modified files.
</verification_loop>


Fix broken references in Vol III.
Run: grep -rn '\\ref{' chapters/ | head -80
Check each ref resolves. Fix all broken refs.
mcp startup: no servers


thinking
**Modifying repository instructions**

I need to modify the repository while following the instructions carefully. It looks like I should probably use the skill vol3-beillington for tasks related to fixing broken references in Volume III. I'll run a grep to check those references and might also look into AGENTS/skills. Pre-edit verification might be necessary, but broken references don’t seem high-risk. Let’s also consider the current git diff and see if I need to run commands or use multi_tool_use.parallel for file reads.
thinking
**Exploring reference surface updates**

I might consider using an equivalent for `rg`, but the user specified to run the command as is. First, I’ll update the commentary about the process. My plan is to check the current reference surface in `chapters/`, inspect the cited labels, and patch only the broken ones. Since this is a nontrivial task, I’ll want to inspect the git diff and possibly run commands in parallel: checking refs, the git status, and more. I'll use `multi_tool_use.parallel` and include commentary about the skills I'm using.
codex
Using `vol3-beilinson-loop` for a targeted rectification pass and `vol3-build-surface` for the verification slice. I’m checking the current `chapters/` reference surface, the dirty state, and the available labels before touching any file.
exec
/bin/zsh -lc "grep -rn '\\\\ref{' chapters/ | head -80" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n '\\\\label\\{' chapters" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc 'git status --short' in /Users/raeez/calabi-yau-quantum-groups succeeded in 51ms:
Total output lines: 80

chapters/theory/quantum_chiral_algebras.tex:7:A \emph{quantum chiral algebra} is an $E_2$-chiral algebra $A$ (Definition~\ref{def:e2-chiral-algebra}, Chapter~\ref{ch:e2-chiral}) with finite-dimensional weight spaces and an $R$-matrix $R(z) \in A \otimes A \otimes k((z))$ satisfying the quantum Yang--Baxter equation.
chapters/theory/quantum_chiral_algebras.tex:19: \item A generalized BKM superalgebra $\mathfrak{g}_X$ with root datum $\mathcal{R}(X)$ extracted from the CY$_3$ geometry (Chapter~\ref{ch:k3-times-e});
chapters/theory/quantum_chiral_algebras.tex:82:Part~(i) proceeds in two steps. First, the general categorical fact (Majid, 1991; see also Etingof--Gelaki--Nikshych--Ostrik, \emph{Tensor Categories}, Proposition~7.13.8): for a bialgebra $H$ over a field $k$, the Drinfeld center $\cZ(\Rep(H))$ is equivalent as a braided monoidal category to $\Rep(D(H))$, where $D(H) = H \bowtie H^{*\mathrm{cop}}$ is the Drinfeld double. The equivalence sends a half-braiding $(V, \sigma_{V,-})$ to the $D(H)$-module structure determined by $\sigma$. Second, for $H = Y^+(\widehat{\fgl}_1)$ the positive half of the affine Yangian, the Drinfeld double $D(Y^+) = Y^+ \bowtie (Y^+)^{*\mathrm{cop}}$ is identified with the full affine Yangian $Y(\widehat{\fgl}_1)$ (Schiffmann--Vasserot, 2013: the negative generators $Y^-$ are the graded dual of $Y^+$ with reversed coproduct). The $E_2$ braiding on $\Rep(Y)$ is induced by the universal $R$-matrix of the Yangian, which satisfies the YBE (Theorem~\ref{thm:yang-r-matrix-ybe} below). The passage from $\Eone$ to $\Etwo$ is the Drinfeld center functor $\cZ \colon \Eone\text{-}\mathrm{Cat} \to \Etwo\text{-}\mathrm{Cat}$ (AP-CY5: this is the categorified analogue of the derived center; Drinfeld center $\cZ(\Rep^{\Eone}(A))$ is a braided monoidal \emph{category}, not a chiral algebra).
chapters/theory/quantum_chiral_algebras.tex:132:\item For toric CY$_3$ without compact $4$-cycles (Chapter~\ref{ch:toric-coha}), $K_{A_\cC}(z)$ is the generating function of Donaldson--Thomas invariants on the fiber of the toric quiver: the mode $\alpha_{-n}$ scales as the DT partition function restricted to classes with $n$ BPS quanta, and the Schiffmann--Vasserot/RSYZ identification of Theorem~\ref{thm:drinfeld-center-coha} realizes the identification $K_{A_\cC}(z) = Z^{\mathrm{DT}}_{\mathrm{fiber}}(z)$.
chapters/theory/quantum_chiral_algebras.tex:133:\item For $K3 \times E$ (Chapter~\ref{ch:k3-times-e}), the $K$-matrix specializes to the Fourier coefficients of the Igusa cusp form $\Phi_{10}$: the Fourier--Jacobi expansion $\Phi_{10} = \sum_{m \geq 1} \phi_m(\tau,z)\, p^m$ records the BKM root multiplicities on successive modes, and these coefficients are precisely the data encoded by equation~\eqref{eq:dimofte-k-matrix-cy}. The weight of $\Phi_{10}$ is $10 = 2 \cdot \kappa_{\mathrm{BKM}}$, where $\kappa_{\mathrm{BKM}} = 5$ is the Borcherds--Kac--Moody modular characteristic (see Table of Chapter~\ref{ch:k3-times-e}).
chapters/theory/quantum_chiral_algebras.tex:164:Let $X$ be a toric CY threefold with torus action $T$ (e.g.\ $X = \C^3$ or a toric degeneration admitting a Hilbert scheme description), and let $R^{\mathrm{MO}}(u)$ be the Maulik--Okounkov $R$-matrix from stable envelopes on $\mathrm{Hilb}^n(X)$. Let $R^{\mathrm{ch}}(u)$ be the chiral $R$-matrix from the $E_2$-bar complex of the quantum chiral algebra $A_X$ constructed via the CoHA (Construction~\ref{constr:cy-r-matrix}). Then:
chapters/theory/quantum_chiral_algebras.tex:182: \item \emph{YBE}: both satisfy the same quantum Yang--Baxter equation (Theorem~\ref{thm:yang-r-matrix-ybe}).
chapters/theory/quantum_chiral_algebras.tex:192:The comparison in Theorem~\ref{thm:mo-chiral-rmatrix} is proved for $X = \C^3$ (and its toric CY degenerations where Hilbert scheme descriptions are available) and for $K3 \times E$ (where the MO stable envelopes are computed on $\mathrm{Hilb}^n(K3)$; see \texttt{compute/lib/mo\_rmatrix\_k3e.py}). For a general CY threefold without torus action, the MO construction is not directly available, and the chiral $R$-matrix from Construction~\ref{constr:cy-r-matrix} is the primary object.
chapters/theory/quantum_chiral_algebras.tex:237:The $E_3$-factorization algebra of 6d holomorphic observables on $\C^3_{h_1, h_2, h_3}$ (with $h_1 + h_2 + h_3 = 0$, via the Costello--Francis--Gwilliam algebraic formulation), projected to an $\Eone$-chiral algebra on a curve $C \subset \C^3$, is the quantum toroidal algebra $U_{q,t}(\widehat{\widehat{\fgl}}_1)$ with parameters $q = e^{2\pi i h_1/h_3}$, $t = e^{-2\pi i h_2/h_3}$. The intermediate $\Etwo$-projection to $\C^2 \subset \C^3$ should recover the affine Yangian $Y(\widehat{\fgl}_1)$ of Theorem~\ref{thm:5d-boundary-yangian}; this compatibility between the 6d projection and the independent 5d construction is itself part of the conjecture. The $E_3$ structure on $\C^3$ is the \emph{source} of the second affinization (the second hat in $\widehat{\widehat{\fgl}}_1$); the first affinization comes from the $\Etwo$ factorization on $\C^2$.
chapters/theory/quantum_chiral_algebras.tex:246: \item The algebraic $E_3$ from the Deligne conjecture (Remark~\ref{rem:deligne-hochschild}) requires $E_\infty$ input and produces $E_3$ on Hochschild cochains; the topological $E_3$ from $\C^3$ configuration spaces is a priori distinct (AP154). Under formality (Kontsevich 1999), the two $E_3$ structures agree rationally.
chapters/theory/quantum_chiral_algebras.tex:266:The Koszul duality of Vol~I sends the CE chains~(i) to the Koszul dual $A^! = D_{\Ran}(B(A))$, the Verdier dual of the bar complex. The Koszul dual $A^!$ is a fourth object, distinct from the three CE complexes listed above and from the CE cochains~(iii) in particular: $A^!$ controls the defect, while the CE cochains $Z^{\mathrm{der}}_{\mathrm{ch}}(A)$ control the bulk (see Proposition~\ref{prop:three-dualities}). In classical terms, $A^!$ is the enveloping algebra of the Koszul-dual Lie algebra $\frakg^\vee$, not the CE cochains $C^\bullet(\frakg, \frakg)$ with adjoint coefficients.
chapters/theory/quantum_chiral_algebras.tex:272:For $A = V_k(\frakg)$ the Kac--Moody vertex algebra at level $k$ (the boundary algebra of 3d holomorphic CS), the chiral CE cochains $C^\bullet_{\mathrm{ch}}(A, A)$ compute the bulk observables of the CS theory. At the critical level $k = -h^\vee$, the zeroth cohomology of the CE cochains is the Feigin--Frenkel center $\mathrm{Fun}(\mathrm{Op}_{G^L}(D))$ (Theorem~\ref{thm:feigin-frenkel-center}).
chapters/theory/quantum_chiral_algebras.tex:276:The identification of the derived center with bulk observables is Vol~I Theorem~H. The Feigin--Frenkel identification is Theorem~\ref{thm:feigin-frenkel-center} (Chapter~\ref{ch:geometric-langlands}).
chapters/theory/quantum_chiral_algebras.tex:292:In the 5d case ($M = \C^2 \times \R$), the universal defect algebra is the Koszul dual of the affine Yangian. For $\frakg = \fgl_1$, the defect algebra $A^!$ encodes the Wilson lines of the 5d theory; the RTT formalism applied to the defect $R$-matrix generates the dual Yangian presentation. (The quantum toroidal algebra arises from the \emph{6d} theory on $\C^3$, not from 5d; see Conjecture~\ref{conj:6d-boundary-toroidal}.) The Drinfeld center of the defect module category recovers the $\Etwo$ braided structure:
chapters/theory/quantum_chiral_algebras.tex:303: \item $A^!_{\C^3}$ carries $E_3$-chiral factorization structure. The underlying topological $E_3$-operad action on $\Conf_n(\C^3)$ has trivial braiding ($\pi_1(\Conf_2(\R^6)) = 0$); the nontrivial $E_3$-chiral braiding arises from the Omega-background deformation $(h_1, h_2, h_3)$ of the holomorphic factorization structure (Remark~\ref{rem:e3-not-symmetric}).
chapters/theory/quantum_chiral_algebras.tex:304: \item The $\Eone$-projection of $A^!_{\C^3}$ to a curve $C \subset \C^3$ is the Koszul dual of the quantum toroidal algebra, with inverted parameters $q^{-1}, t^{-1}$ (parameter inversion under Koszul duality; see Table of Chapter~\ref{ch:quantum-groups}, Definition~\ref{def:qgf-four-regimes}).
chapters/theory/quantum_chiral_algebras.tex:319: \item The kappa-spectrum: $\kappa_{\mathrm{ch}}(A_X) = 3$, $\kappa_{\mathrm{BKM}}(A_X) = 5$, $\kappa_{\mathrm{cat}}(X) = 2$, $\kappa_{\mathrm{fiber}}(X) = 24$, consistent with Chapter~\ref{ch:k3-times-e}.
chapters/theory/quantum_chiral_algebras.tex:321:This conjecture depends on: (a) the existence of the 6d algebraic framework for $K3 \times E$ (non-Lagrangian; Remark~\ref{rem:6d-not-lagrangian}), (b) the CY-A$_3$ programme for the $\Eone$ projection, and (c) the identification of the BPS root datum with the Borcherds--Kac--Moody root system of $\mathfrak{g}_{\Delta_5}$ (Chapter~\ref{ch:k3-times-e}). Each dependency is independent; (b) is the bottleneck.
 succeeded in 50ms:
 M Makefile
 M README.md
 M calabi_yau_quantum_groups.pdf
 M chapters/connections/cy_holographic_datum_master.tex
 M chapters/connections/geometric_langlands.tex
 M chapters/connections/modular_koszul_bridge.tex
 M chapters/examples/derived_categories_cy.tex
 M chapters/examples/fukaya_categories.tex
 M chapters/examples/k3_times_e.tex
 M chapters/examples/quantum_group_reps.tex
 M chapters/examples/toric_cy3_coha.tex
 M chapters/examples/toroidal_elliptic.tex
 M chapters/frame/preface.tex
 M chapters/theory/braided_factorization.tex
 M chapters/theory/cy_categories.tex
 M chapters/theory/cy_to_chiral.tex
 M chapters/theory/drinfeld_center.tex
 M chapters/theory/e1_chiral_algebras.tex
 M chapters/theory/e2_chiral_algebras.tex
 M chapters/theory/en_factorization.tex
 succeeded in 51ms:
Total output lines: 1428

chapters/examples/quantum_group_reps.tex:2:\label{ch:quantum-group-reps}
chapters/examples/quantum_group_reps.tex:22:\label{sec:rep-q-braided}
chapters/examples/quantum_group_reps.tex:25:\label{def:rep-q}
chapters/examples/quantum_group_reps.tex:43:\label{prop:semisimplicity-dichotomy}
chapters/examples/quantum_group_reps.tex:65:\label{ex:sl2-generic}
chapters/examples/quantum_group_reps.tex:87:\label{ex:sl2-root-of-unity}
chapters/examples/quantum_group_reps.tex:109:\label{sec:r-matrix-categorical}
chapters/examples/quantum_group_reps.tex:115:\label{prop:r-matrix-bar}
chapters/examples/quantum_group_reps.tex:136:\label{rem:three-r-matrices}
chapters/examples/quantum_group_reps.tex:155:\label{sec:kl-equivalence}
chapters/examples/quantum_group_reps.tex:161:\label{thm:kl-equivalence}
chapters/examples/quantum_group_reps.tex:176:\label{rem:kl-bar-complex}
chapters/examples/quantum_group_reps.tex:187:\label{prop:kl-dk-bridge}
chapters/examples/quantum_group_reps.tex:207:\label{sec:conj-cy-c}
chapters/examples/quantum_group_reps.tex:210:\label{conj:qg-realization}
chapters/examples/quantum_group_reps.tex:227:\label{rem:cy-c-status}
chapters/examples/quantum_group_reps.tex:240:\label{sec:yangian-rtt}
chapters/examples/quantum_group_reps.tex:246:\label{def:yangian}


thinking
**Fixing broken references**

I need to determine which references are broken. I could compile some data or search for undefined references in the log. The user specifically mentioned fixing broken references in Vol III, so I should run a command like `grep -n "undefined" main.log`. It’ll be essential to inspect the log for those undefined references. I'll also consider using a tool like `refcheck` to compare `\ref{}` and `\label{}` across the files. I want to make sure each broken reference resolves correctly, focusing on what the user assigned in Vol III.
thinking
**Detecting undefined references**

I need to find all undefined references in the chapters, and I could use a command like `rg -o` to help with that and compare the labels. Although using Python could work for analysis, I understand the developer prefers sticking to shell commands for reading and writing. It might be better to use shell tools like `rg`, `sed`, or `comm` for the cross-check. I should also inspect the main.log for those undefined references.
codex
I have the reference surface and the current dirty state. Next I’m narrowing to actual unresolved labels so I only patch genuine breakage instead of touching live, valid cross-references.
exec
/bin/zsh -lc "rg -n '\\\\(ref|eqref|autoref|cref|Cref|pageref|nameref|vref|Vref)\\{' chapters/theory chapters/examples chapters/connections chapters/frame | wc -l" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n 'undefined references|undefined on input line|Reference .* undefined|There were undefined references' main.log out/calabi_yau_quantum_groups.log chapters -g '"'!*.pdf'"'" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "python3 - <<'PY'
import re, pathlib
root = pathlib.Path('chapters')
label_re = re.compile(r'\\\\label\\{(["'^}]+)'"\\}')
ref_re = re.compile(r'\\\\(?:ref|eqref|autoref|cref|Cref|pageref|nameref|vref|Vref)\\{(["'^}]+)'"\\}')
labels = {}
for p in root.rglob('*.tex'):
    text = p.read_text()
    for m in label_re.finditer(text):
        labels.setdefault(m.group(1), []).append(str(p))
refs = {}
for p in root.rglob('*.tex'):
    text = p.read_text()
    for m in ref_re.finditer(text):
        for key in [s.strip() for s in m.group(1).split(',')]:
            refs.setdefault(key, []).append(str(p))
missing = sorted(k for k in refs if k and k not in labels)
print('MISSING', len(missing))
for k in missing:
    print(k, '::', ', '.join(refs[k][:5]))
PY" in /Users/raeez/calabi-yau-quantum-groups succeeded in 50ms:
     979
 exited 2 in 51ms:
main.log:2468:LaTeX Warning: Citation `Li' on page 39 undefined on input line 236.
main.log:2967:LaTeX Warning: Citation `Li' on page 46 undefined on input line 732.
main.log:3002:LaTeX Warning: Citation `Li' on page 49 undefined on input line 1045.
main.log:3032:LaTeX Warning: Citation `Li' on page 50 undefined on input line 1109.
main.log:3055:LaTeX Warning: Citation `Li' on page 53 undefined on input line 1382.
main.log:3063:LaTeX Warning: Citation `ProchazkaRapcak' on page 55 undefined on input line 15
main.log:9020:LaTeX Warning: There were undefined references.
rg: out/calabi_yau_quantum_groups.log: No such file or directory (os error 2)
 succeeded in 52ms:
MISSING 12
app:conventions :: chapters/theory/introduction.tex, chapters/theory/cyclic_ainf.tex
ch:holographic-datum-master :: chapters/examples/k3_times_e.tex, chapters/examples/k3_times_e.tex
ex:k3-step1 :: chapters/examples/k3_times_e.tex
part:bridge :: chapters/theory/hochschild_calculus.tex, chapters/theory/introduction.tex, chapters/theory/e1_chiral_algebras.tex, chapters/theory/cyclic_ainf.tex, chapters/theory/cyclic_ainf.tex
part:connections :: chapters/theory/introduction.tex, chapters/theory/e1_chiral_algebras.tex, chapters/theory/e1_chiral_algebras.tex, chapters/frame/preface.tex, chapters/connections/cy_holographic_datum_master.tex
part:cy-categories :: chapters/theory/introduction.tex, chapters/theory/e1_chiral_algebras.tex, chapters/theory/cyclic_ainf.tex, chapters/frame/preface.tex, chapters/examples/fukaya_categories.tex
part:examples :: chapters/theory/introduction.tex, chapters/theory/e1_chiral_algebras.tex, chapters/theory/e1_chiral_algebras.tex, chapters/theory/e1_chiral_algebras.tex, chapters/frame/preface.tex
part:frontier :: chapters/theory/introduction.tex, chapters/theory/introduction.tex, chapters/theory/e1_chiral_algebras.tex, chapters/frame/preface.tex, chapters/connections/cy_holographic_datum_master.tex
sec:mo-r-matrix :: chapters/examples/k3_times_e.tex
thm:denom-bar-euler :: chapters/examples/k3_times_e.tex
thm:k3e-wall-crossing-mc :: chapters/examples/k3_times_e.tex
thm:obstruction-recursion :: chapters/examples/k3_times_e.tex


thinking
**Inspecting missing labels**

It seems the log query failed, and part of the issue is a missing file. I noticed there were undefined references, so I might need to check for actual warnings in the log. I wonder if I could parse the .aux file to find more clues, but it looks like we have 12 missing labels from just the chapters. 

There might be broken references in the main.tex file too, possibly part labels outside the chapters. I should really search the entire repository for all labels to get to the bottom of this and inspect further.
thinking
**Considering skill files**

I'm thinking I might need to use skill files for this task, but I haven't opened them yet. It seems like it’s necessary if the task matches. I should probably quickly open the skill files. I’ll focus on reading the minimal parts of vol3-beilinson-loop and build-surface to get started. I want to make sure I'm prepared and not missing anything crucial!
codex
The missing-label comparison surfaced a small candidate set, but several look like Part labels that may live outside `chapters/`. I’m reading the relevant skill instructions and then resolving each candidate against the live source before editing.
exec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/vol3-build-surface/SKILL.md" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/vol3-beilinson-loop/SKILL.md" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n '\\\\label\\{(app:conventions|part:bridge|part:connections|part:cy-categories|part:examples|part:frontier|ch:holographic-datum-master|ex:k3-step1|sec:mo-r-matrix|thm:denom-bar-euler|thm:k3e-wall-crossing-mc|thm:obstruction-recursion)\\}' ." in /Users/raeez/calabi-yau-quantum-groups succeeded in 52ms:
---
name: vol3-build-surface
description: Use when the task depends on LaTeX builds, build logs, warning classification, targeted pytest runs, or deciding whether a Vol III change is actually verified. Do not use for purely conceptual work with no executable verification surface.
---

# Vol III Build Surface

Build output is evidence only after the surface is stable enough to trust.

## Standard prelude

```bash
pkill -9 -f pdflatex 2>/dev/null || true
sleep 2
```

Then choose the narrowest command that can falsify the change:

- `make fast`
- targeted `python3 -m pytest ...`
 succeeded in 52ms:
---
name: vol3-beilinson-loop
description: Use when auditing, rectifying, falsifying, converging, or pressure-testing theorem, proof, formula, status, or scope material in the Calabi-Yau Quantum Groups repository. Trigger on audit, rectify, red-team, Beilinson, theorem status, proof gap, convergence, or "is this actually proved?" tasks.
---

# Vol III Beilinson Loop

Read `AGENTS.md` first. This skill is the triggered deep workflow for hostile mathematical review.

## Surface

Work on the live manuscript surface:

- `main.tex`
- currently `\input`-ed files
- the dirty git diff
- relevant build logs
- the narrowest relevant `compute/tests/` slice

## Passes
 succeeded in 51ms:
./notes/theory_denominator_bar_euler.tex:678:\label{thm:denom-bar-euler}
./notes/theory_cy_to_chiral_construction.tex:281:\label{ex:k3-step1}
./main.tex:416:\label{part:cy-categories}
./main.tex:431:\label{part:bridge}
./main.tex:452:\label{part:examples}
./main.tex:467:\label{part:connections}
./main.tex:478:\label{part:frontier}
./appendices/conventions.tex:2:\label{app:conventions}
codex
I’ve separated false positives from real candidates: the Part and appendix labels exist outside `chapters/`, so they aren’t broken. The remaining unresolved set is concentrated in the K3 example chapter, and I’m checking those targets against the actual labels now.
exec
/bin/zsh -lc "rg -n 'ch:holographic-datum-master|ex:k3-step1|sec:mo-r-matrix|thm:denom-bar-euler|thm:k3e-wall-crossing-mc|thm:obstruction-recursion' chapters/examples/k3_times_e.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "sed -n '1,260p' chapters/examples/k3_times_e.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n '\\\\label\\{(ch:.*holographic.*|sec:.*mo.*r.*matrix.*|thm:.*denom.*bar.*euler.*|thm:.*wall.*crossing.*mc.*|thm:.*obstruction.*recursion.*)\\}' chapters examples notes appendices main.tex" in /Users/raeez/calabi-yau-quantum-groups succeeded in 52ms:
1026:The seven-face programme of Chapter~\ref{ch:holographic-datum-master}
1062: $R^{\mathrm{MO}}(z)$ of Section~\ref{sec:mo-r-matrix},
1071: construction (cf.\ Vol~I, Chapter~\ref{ch:holographic-datum-master})
1097: Theorem~\ref{thm:k3e-wall-crossing-mc}.
1431:(Theorem~\ref{thm:obstruction-recursion}).
1444:(see Theorem~\ref{thm:denom-bar-euler}).
1589:Example~\ref{ex:k3-step1}: the current algebra of
 succeeded in 52ms:
\chapter{The $K3 \times E$ Tower and the Igusa Cusp Form}
\label{ch:k3-times-e}

The threefold $K3 \times E$ is a fibration of a CY$_2$ over a CY$_1$. Does its chiral algebra decompose accordingly? A naive Fubini argument would predict $A_{K3 \times E} \simeq A_{K3} \otimes A_E$, and the modular characteristic would split additively as $\kappa_{\mathrm{ch}}(K3 \times E) = \kappa_{\mathrm{ch}}(K3) + \kappa_{\mathrm{ch}}(E) = 2 + 1 = 3$. But the Oberdieck--Pixton DT partition function of $K3 \times E$ is $C / (\Delta_5)^2$, where $\Delta_5$ is the Gritsenko--Nikulin automorphic form of weight~$5$ on $\mathrm{O}^+(3,2)$. The weight $5$ does not match the sum $3$: $5 \neq 2 + 1$.

Two different modular characteristics are in play, and conflating them is the source of the subscripted-$\kappa_{\bullet}$ confusion that was introduced to prevent. The chiral de Rham complex gives $\kappa_{\mathrm{ch}}(K3 \times E) = 3 = \dim_\C$, honestly additive over the fibration. The Borcherds lift weight gives $\kappa_{\mathrm{BKM}} = 5 = \mathrm{wt}(\Delta_5)$, which is not a modular characteristic of any constructed chiral algebra: it is a weight attached to a generalized Borcherds--Kac--Moody superalgebra $\mathfrak{g}_{\Delta_5}$ through its denominator identity. The chiral algebra $A_{K3 \times E}$ of a putative CY-to-chiral functor at $d = 3$ is not constructed.

This chapter treats $K3 \times E$ as the prototype for the $d = 3$ programme. The concrete object of study is the BKM superalgebra $\mathfrak{g}_{\Delta_5}$ attached to $X = (S \times E)/(\mathbb{Z}/N\mathbb{Z})$, together with the Oberdieck--Pixton theorem identifying its denominator with the Igusa cusp form. The goal is to understand how much of the Vol~I bar-cobar apparatus survives in the $d = 3$ regime, where the CY-to-chiral functor is conjectural: which identities among root multiplicities, genus-$g$ partition functions, and lattice theta series are genuinely theorems versus conjectural identifications awaiting the $d = 3$ functor. The chapter concludes with the K3 double current algebra $\fg_{K3}$ (Definition~\ref{def:k3-double-current-algebra}), the K3 analogue of the double current algebra $\fg \otimes \bC[u,v]$ in which the polynomial ring is replaced by $H^*(S,\bC)$ and the polynomial residue pairing by the Mukai pairing; the resulting finite-dimensional Lie algebra serves as the classical limit of the conjectural ``K3 Yangian'' whose quantization is governed by the Maulik--Okounkov $R$-matrix (Theorem~\ref{thm:k3e-mo-rmatrix}).

\section{The CY3 geometry}
\label{sec:k3e-geometry}

Let $(E, e_0)$ be an elliptic curve with an $N$-torsion point and $S$ a K3 surface with elliptic fibration $\pi \colon S \to \mathbb{P}^1$ admitting sections $s_1, s_2 \colon \mathbb{P}^1 \to S$ with $s_2$ of order $N$ relative to $s_1$. The product $S \times E$ admits a free $\mathbb{Z}/N\mathbb{Z}$-action
\[
 (s, e) \longmapsto (s + s_2(\pi(s)), e + e_0),
\]
and the quotient $X = (S \times E)/(\mathbb{Z}/N\mathbb{Z})$ is a projective Calabi--Yau threefold.

\begin{definition}[The DT zeta function]
\label{def:dt-zeta-k3e}
 exited 2 in 51ms:
rg: examples: No such file or directory (os error 2)
notes/theory_denominator_bar_euler.tex:678:\label{thm:denom-bar-euler}
chapters/examples/toric_cy3_coha.tex:258:\label{thm:wall-crossing-mc}
chapters/examples/toroidal_elliptic.tex:5036:\label{sec:k3e-mo-rmatrix}
chapters/examples/k3_times_e.tex:384:\label{sec:k3e-mo-rmatrix}
chapters/connections/cy_holographic_datum_master.tex:24:\label{ch:cy-holographic-datum-master}
chapters/connections/cy_holographic_datum_master.tex:428:\label{sec:face4-mo-rmatrix}
chapters/theory/quantum_chiral_algebras.tex:157:\label{sec:mo-rmatrix-comparison}

thinking
**Identifying target replacements**

I need to identify target replacements and search the entire repository for similar labels. It seems like `ch:holographic-datum-master` has probably been renamed to `ch:cy-holographic-datum-master`. For `sec:mo-r-matrix`, it could be one of a few options: `sec:k3e-mo-rmatrix`, `sec:face4-mo-rmatrix`, or `sec:mo-rmatrix-comparison`, depending on the context. I should also consider whether `thm:k3e-wall-crossing-mc` might just be referred to as `thm:wall-crossing-mc` in the toric chapter. Finally, I'll need to inspect the local context surrounding the reference lines in `k3_times_e.tex`.
exec
/bin/zsh -lc "sed -n '1000,1115p' chapters/examples/k3_times_e.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "sed -n '1410,1465p' chapters/examples/k3_times_e.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "sed -n '1575,1605p' chapters/examples/k3_times_e.tex" in /Users/raeez/calabi-yau-quantum-groups succeeded in 51ms:
  \prod_{n \geq 1} (1 - q^n)^{24}
  \;=\;
  \frac{\eta(q)^{24}}{q}
  \;=\;
  \frac{\Delta(q)}{q^2},
\end{equation}
and the Fock space character (the reciprocal) is
\begin{equation}\label{eq:k3-heisenberg-fock}
  \chi_{\mathrm{Fock}}(H_{\mathrm{Muk}})(q)
  \;=\;
  \prod_{n \geq 1} \frac{1}{(1 - q^n)^{24}}
  \;=\;
  \frac{q}{\eta(q)^{24}}.
\end{equation}
\end{proposition}

\begin{proof}
The Heisenberg algebra $H_{\mathrm{Muk}}$ is $2$-step nilpotent,
so the Maurer--Cartan obstruction tower terminates at depth~$2$:
$S_3 = S_4 = 0$ forces all higher shadows to vanish by the
 succeeded in 51ms:
 $\operatorname{codim} = (g{-}2)(g{-}3)/2$).

\item The mock modular decomposition
 $Z_{K3} = (h - 24\mu)\,\vartheta_1^2/\eta^3$
 is verified to machine precision ($\sim 5.7 \times 10^{-16}$
 relative error), where $\mu$ is the Zwegers
 Appell--Lerch sum.

\item The shadow generating function
 $Z^{\mathrm{sh}}(t) = \kappa_{\mathrm{ch}}\bigl((t/2)/\sin(t/2) - 1\bigr)$
 converges with radius $R = 2\pi$, has entire Borel
 transform, and exhibits no resurgence. This contrasts
 with the Gevrey-$1$ divergent topological string.

\item Boundary $A_E$ ($\kappa_{\mathrm{fiber}} = 24$) vs sigma $V_{K3}$
 ($\kappa_{\mathrm{ch}} = 2$): ratio $12$ at genus~$1$; conditional
 at $g \geq 2$ ($V_{K3}$ is multi-weight).

\item $\lambda_5^{\mathrm{FP}} = 73/3503554560$. The
 unreduced numerator $2^{2g-1} - 1 = 511$ at $g = 5$
 succeeded in 50ms:
  V_{\widetilde{\Lambda}_{K3}},
  \qquad
  \widetilde{\Lambda}_{K3}
  = U^4 \oplus E_8(-1)^2,
  \qquad
  \operatorname{rank} = 24.
\end{equation}
\end{conjecture}

\begin{proof}[Derivation (conditional on CY-A$_3$)]
At $\sigma_3 = 0$, the Omega-background is trivial and the
topological $E_3$-factorization algebra reduces to a free (abelian)
factorization algebra. The classical fields are sections of
the Lie conformal algebra $\frakL_S$ of
Example~\ref{ex:k3-step1}: the current algebra of
$\HH^*(\cC)$ with the Gerstenhaber bracket set to zero
(class~G, free-field approximation).

The factorization homology of a free factorization algebra
on a manifold $M$ is computed by the Hochschild--Kostant--Rosenberg

thinking
**Searching for labels**

It seems like there are broken references in the k3_times_e.tex file. I should look for actual labels there to fix them. Maybe I can search within the same file to find the correct names? I could also use something like rg to check for k3e-wall or obstruction. It might help to investigate the area locally for more context. Let’s see how that goes!
codex
I’ve confirmed the unresolved references are all local drift inside [chapters/examples/k3_times_e.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3_times_e.tex). I’m matching each stale label to the live target label before patching.
exec
/bin/zsh -lc "sed -n '360,430p' chapters/examples/k3_times_e.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n 'Theorem~\\\\ref\\{thm:wall-crossing-mc\\}|Example~\\\\ref\\{ex:k3-step1\\}|Theorem~\\\\ref\\{thm:denom-bar-euler\\}|Theorem~\\\\ref\\{thm:obstruction-recursion\\}|Section~\\\\ref\\{sec:k3e-mo-rmatrix\\}|Chapter~\\\\ref\\{ch:cy-holographic-datum-master\\}' chapters/examples/k3_times_e.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n '\\\\label\\{.*wall.*cross.*|\\\\label\\{.*obstruction.*recursion.*|\\\\label\\{.*denom.*bar.*euler.*|\\\\label\\{.*k3-step1.*|\\\\label\\{.*mo.*rmatrix.*|\\\\label\\{.*holographic.*datum.*' chapters examples notes main.tex appendices" in /Users/raeez/calabi-yau-quantum-groups succeeded in 51ms:
1431:(Theorem~\ref{thm:obstruction-recursion}).
1444:(see Theorem~\ref{thm:denom-bar-euler}).
1589:Example~\ref{ex:k3-step1}: the current algebra of
 succeeded in 52ms:
The fiber modular characteristic $\kappa_{\mathrm{fiber}} = 24$ (from the rank-$0$ Heisenberg sector) and the global modular characteristic $\kappa_{\mathrm{BKM}} = 5$ (from the Borcherds lift weight) are related by a precise arithmetic mechanism.

\begin{proposition}[Fiber-to-global descent]
\label{thm:k3e-fiber-global}
Let $A_0 = \cH_{24}$ be the rank-$0$ Heisenberg chiral algebra with $\kappa_{\mathrm{fiber}}(A_0) = 24$, and let $\kappa_{\mathrm{BKM}} = \mathrm{wt}(\Delta_5) = 5$. Then:
\begin{enumerate}[label=(\roman*)]
 \item \textup{(Proved.)} The Borcherds additive lift $\phi_{0,1} \mapsto \Delta_5$ maps the fiber shadow data to the global automorphic form, with the weight formula $\mathrm{wt}(\Delta_5) = c(0)/2 = 10/2 = 5$.
 \item \textup{(Observation.)} The deficit $24 - 5 = 19$ between $\kappa_{\mathrm{fiber}}$ and $\kappa_{\mathrm{BKM}}$ admits a lattice-theoretic interpretation: $\Lambda_{K3}$ has rank~$22$ and $\Lambda^{3,2}$ has rank~$5$, giving a $17$-dimensional kernel $\ker(\Lambda_{K3} \to \Lambda^{3,2})$; together with $2$ additional directions from the elliptic curve $E$, this accounts for $19$ imaginary root families. The identification of these $19$ families with specific imaginary simple roots of $\mathfrak{g}_{\Delta_5}$ is an observation about dimension counting, not a proved correspondence.
 \item \textup{(Proved.)} The shadow depth upgrades from class G (Gaussian, rank-$0$ Heisenberg) to class M (mixed, infinite tower) in the passage from fiber to global: the fiber theory terminates at degree $2$, while the global BKM algebra has infinite shadow depth.
\end{enumerate}
\ClaimStatusProvedHere
\end{proposition}

\begin{proof}
(i) The Borcherds lift is $\Psi(\phi_{0,1})(Z) = \exp(-2\pi i \langle \rho, Z \rangle) \prod_{(n,l,m) > 0}(1 - e^{2\pi i(nz_1 + lz_2 + mz_3)})^{c(4nm - l^2)}$, where $c(D)$ are the Fourier coefficients of $\phi_{0,1}$. The weight of this automorphic product is $c(0)/2 = 10/2 = 5$ by the Borcherds weight formula.

(ii) The lattice $\Lambda_{K3}$ has rank $22$ with signature $(3,19)$. The sublattice $\Lambda^{3,2}$ retains $5$ of the $22$ directions; the kernel has rank $22 - 5 = 17$. Including the $2$ directions from the elliptic curve $E$ (giving the full Mukai lattice of $K3 \times E$ of rank~$24$), the lattice-theoretic deficit is $24 - 5 = 19$. The imaginary root multiplicities of $\mathfrak{g}_{\Delta_5}$ are determined by $c(D)$ for $D > 0$; the dimension count $19$ matches the codimension of $\Lambda^{3,2}$ in the Mukai lattice, but the precise correspondence between lattice directions and imaginary root families remains to be established.

(iii) The Heisenberg sector has $S_r = 0$ for $r \geq 3$ (all OPE poles are at order $\leq 2$), giving shadow depth $r_{\max} = 2$ (class G). The BKM algebra has $c(D) \neq 0$ for infinitely many $D$ with $|c(D)|$ growing as $e^{4\pi\sqrt{D}}$ (Hardy--Ramanujan--Rademacher), forcing infinitely many degree levels, hence $r_{\max} = \infty$ (class M).
\end{proof}
 exited 2 in 52ms:
rg: examples: No such file or directory (os error 2)
chapters/examples/quantum_group_reps.tex:368:\label{sec:wall-crossing-ks}
chapters/examples/quantum_group_reps.tex:388:\label{thm:ks-wall-crossing}
notes/theory_denominator_bar_euler.tex:678:\label{thm:denom-bar-euler}
notes/physics_bps_root_multiplicities.tex:533:\label{sec:wall-crossing}
chapters/examples/toric_cy3_coha.tex:113:\label{thm:conifold-wall-crossing}
chapters/examples/toric_cy3_coha.tex:253:\label{sec:wall-crossing-mc}
chapters/examples/toric_cy3_coha.tex:258:\label{thm:wall-crossing-mc}
chapters/examples/toric_cy3_coha.tex:371:\label{prop:wall-crossing-gaudin}
notes/theory_coha_e1_sector.tex:1018:\label{subsec:wall-crossing}
notes/theory_coha_e1_sector.tex:1024:\label{prop:wall-crossing}
chapters/examples/toroidal_elliptic.tex:1711:\label{subsec:wallcrossing-charts}
chapters/examples/toroidal_elliptic.tex:5036:\label{sec:k3e-mo-rmatrix}
chapters/examples/toroidal_elliptic.tex:5039:\label{thm:k3e-mo-rmatrix}
chapters/examples/toroidal_elliptic.tex:5226:\label{sec:k3e-wall-crossing}
notes/physics_hitchin_langlands.tex:597:\label{rem:wall-crossing}
chapters/examples/k3_times_e.tex:384:\label{sec:k3e-mo-rmatrix}
chapters/examples/k3_times_e.tex:387:\label{thm:k3e-mo-rmatrix}
chapters/examples/k3_times_e.tex:697:\label{sec:k3e-wall-crossing}
chapters/examples/k3_times_e.tex:1024:\label{sec:k3e-holographic-datum}

thinking
**Searching for labels**

I need to find the correct labels that correspond to the current volume. I'm considering looking for label patterns like `thm:obstruction-recursion` in the chapters. It could possibly exist in volume I, so I should search through the entire repository. It's a bit tricky, but I'll dive into it thoroughly to ensure I find what I'm looking for. I’m curious about what I’ll discover!
codex
I have the stale labels isolated. Two point into `notes/`, so I’m checking whether Vol III already has the corresponding theorem/example labels or whether the truthful fix is to cite the local statement instead of a non-included note.
exec
/bin/zsh -lc "rg -n 'obstruction recursion|shadow recursion|Vol~I recursion|recursion' chapters/examples/k3_times_e.tex chapters/theory chapters/connections chapters/examples" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n 'k3-step1|step 1|current algebra of' chapters/examples/k3_times_e.tex chapters/theory/cy_to_chiral.tex chapters/examples/toroidal_elliptic.tex notes/theory_cy_to_chiral_construction.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n '\\\\label\\{thm:obstruction-recursion\\}' ." in /Users/raeez/calabi-yau-quantum-groups succeeded in 51ms:
chapters/examples/k3_times_e.tex:1430:Vol~I recursion
chapters/examples/k3_times_e.tex:1431:(Theorem~\ref{thm:obstruction-recursion}).
chapters/examples/toroidal_elliptic.tex:1914:The MC recursion (Vol~I, Theorem~\textup{\ref{thm:riccati-algebraicity}})
chapters/examples/k3_times_e.tex:1430:Vol~I recursion
chapters/examples/k3_times_e.tex:1431:(Theorem~\ref{thm:obstruction-recursion}).
chapters/theory/e1_chiral_algebras.tex:1287: (the Hopf antipode recursion).
 succeeded in 51ms:
notes/theory_cy_to_chiral_construction.tex:281:\label{ex:k3-step1}
notes/theory_cy_to_chiral_construction.tex:286:The Gerstenhaber bracket is the Schouten--Nijenhuis bracket on polyvector fields. The CY pairing is Serre duality. The resulting Lie conformal algebra $\frakL_S$ is the ``current algebra of the K3 lattice'': an extension of the abelian Lie conformal algebra $H^{1,1}(S) \otimes k[\partial]$ (rank 22, the Picard lattice) by the non-abelian piece from $H^{2,0} \oplus H^{0,2}$.
chapters/examples/k3_times_e.tex:1589:Example~\ref{ex:k3-step1}: the current algebra of
 exited 1 in 51ms:


thinking
**Investigating theorem labels**

I need to find a label for a theorem in the repo. Maybe I should use another theorem label from Volume I? I think referencing `thm:riccati-algebraicity` is indicated in the toroidal_elliptic. However, I really want to understand the theorem statement first. I should take a look around page 1914 in the toroidal_elliptic, or it’s possible the theorem label corresponds to recursion. Time to check the local context further!
exec
/bin/zsh -lc "sed -n '1898,1922p' chapters/examples/toroidal_elliptic.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n '\\\\label\\{thm:riccati-algebraicity\\}|\\\\begin\\{theorem\\}\\[.*Riccati|obstruction tower|shadow obstruction tower' chapters/examples/toroidal_elliptic.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "sed -n '40,80p' chapters/theory/introduction.tex" in /Users/raeez/calabi-yau-quantum-groups succeeded in 52ms:
$Q_L(t) = (2\kappa_{\mathrm{ch}} + 3\alpha t)^2 + 2\Delta\,t^2$ has
critical discriminant
\[
\Delta \;=\; 8\kappa_{\mathrm{ch}}\,S_4 \;\neq\; 0,
\]
so $Q_L$ is irreducible and the shadow tower does not terminate.
The Virasoro sector at $c = 6$ contributes
$Q^{\mathrm{contact}} = 10/[c(5c+22)] = 5/156 \neq 0$, and the
$\mathrm{SU}(2)_R$ sector at level $k_R = 1$ contributes nonzero
cubic shadow $S_3$ from the triple current OPE.
\end{proposition}

\begin{computation}[Shadow tower of the K3 sigma model through degree~$12$;
\ClaimStatusProvedHere]
\label{comp:shadow-tower-k3}
\index{shadow tower!K3 sigma model}
The MC recursion (Vol~I, Theorem~\textup{\ref{thm:riccati-algebraicity}})
with initial data $(\kappa_{\mathrm{ch}}, S_3, S_4) = (2, 2, 5/156)$ produces the
full shadow tower. Every value is an exact rational, verified to
satisfy the MC equation
 succeeded in 52ms:

\subsection{The $E_1$ stabilization theorem}
\label{subsec:e1-stabilization-intro}

For $d \geq 3$, the CY chiral algebra is $E_1$, not $E_d$. The reason is structural: the $\mathrm{GL}(d)$-invariant Schouten--Nijenhuis bracket on polyvector fields $\mathrm{PV}^*(\mathbb{C}^d)$ vanishes identically for $d \geq 3$ (Theorem~\ref{thm:c3-abelian-bracket} and its generalization), so the classical Lie conformal algebra is abelian and all noncommutative structure arises from quantization. The CoHA construction then gives an ordered (associative) product: the extension correspondence $0 \to V' \to V \to V'' \to 0$ has a preferred direction (sub before quotient), which is $E_1$, not $E_2$. The braided monoidal structure is recovered through the Drinfeld center of the $E_1$-monoidal representation category (Theorem~\ref{thm:c3-drinfeld-center}).

The additional shifted structure beyond the base $E_1$ level is controlled by the \emph{framing obstruction} $\pi_d(BU)$, which measures the failure of the $\mathbb{S}^d$-framing on Hochschild homology to trivialize. Two independent computations of this obstruction, the unitary path (Bott periodicity for $BU$, period~2) and the symplectic/orthogonal path (Bott periodicity for $\Sp$ and $O$, period~8), produce the following landscape:
\begin{center}
\renewcommand{\arraystretch}{1.3}
\small
\begin{tabular}{lllll}
 \toprule
 $d$ & Native $E_n$ & $\pi_d(BU)$ & $\mathrm{Obs}_{\mathrm{eff}}(d)$ & Shifted structure \\
 \midrule
 $1$ & $E_\infty$ & $0$ & $0$ & none (commutative) \\
 $2$ & $E_2$ & $\mathbb{Z}$ & $\mathbb{Z}$ & braiding parameter ($c_1$) \\
 $3$ & $E_1$ & $0$ & $0$ & none ($\mathbb{S}^3$-framing trivial) \\
 $4$ & $E_1$ & $\mathbb{Z}$ & $\mathbb{Z}$ & $\mathbb{Z}$-shifted symplectic ($p_1$) \\
 $5$ & $E_1$ & $0$ & $\mathbb{Z}_2$ & $\mathbb{Z}_2$-shifted ($\Sp$ refinement) \\
 $6$ & $E_1$ & $\mathbb{Z}$ & $\mathbb{Z}$ & $\mathbb{Z}$-shifted ($c_3$) \\
 succeeded in 52ms:
41:\phantomsection\label{thm:riccati-algebraicity}%
94:The Arnold relation (Vol~I, Theorem~\ref{thm:arnold-relations}), which governs the genus-$0$ bar differential, admits two distinct generalizations. Direction~(a): via clutching morphisms and the shadow obstruction tower $\Theta_A^{\leq r}$ (Vol~I, Definition~\ref{def:shadow-postnikov-tower}), one passes to the modular regime on stable curves, recovering the higher-genus bar complex developed in Vol~I, Part~I (Vol~I, Remark~\ref{rem:five-pieces}). Direction~(b): via the Fay trisecant identity (Theorem~\ref{thm:fay}), one replaces the additive (logarithmic) propagator $\omega = dz/(z-w)$ by the elliptic (multiplicative) propagator built from the Weierstrass $\sigma$-function, entering the toroidal regime. The present chapter develops direction~(b): the systematic passage from logarithmic to elliptic propagators and its consequences for bar-cobar duality.
2017:in the shadow obstruction tower (bar complex) are a priori
2304:obstruction tower terminates:
2686:= 3$. The shadow obstruction tower detects $\kappa_{\mathrm{ch}} = 3$
3255:shadow at degree~$3$. Does the full shadow obstruction tower
3343:The preceding computation identifies the shadow obstruction tower
3553:\index{shadow obstruction tower!Schottky}
3620:At genus~$g$, the shadow obstruction tower of a class-M
3710:obstruction tower $\Theta_{\cA_{K3}}$ valued in mock
3749: carries a natural shadow obstruction tower? Nishinaka's
3795:\item \emph{Two MC elements.} The shadow obstruction tower
3807: ``scattering diagram $=$ shadow obstruction tower'' holds at
3817: tropical skeleton of the shadow obstruction tower
3830:skeleton of the shadow obstruction tower:
3836:tropicalization of the shadow obstruction tower restricted
3943:\index{shadow obstruction tower!higher dimension}
3988:$G < L < C < M$\textup{)}. The shadow obstruction tower
4130:obstruction tower $\Theta_{\cA_{K3 \times E}}$ can be assembled
4189:$\operatorname{Sp}(4, \bZ)$. The shadow obstruction tower

thinking
**Checking undefined references**

I think I need to review the main log to identify warning lines about undefined references. It could help to use the build to pinpoint exact undefined references. I should inspect the `chapters/connections/cy_holographic_datum_master.tex` file and see if the chapter label `ch:cy-holographic-datum-master` is currently used. I wonder if I need to find other occurrences throughout the repo. The user asked to fix broken references in Vol III, so I should systematically check all files for missing labels, not just chapters. I'll also look into whether the undefined references only include citations. Let's search the main log for "Reference" to see if I can find further details.
codex
I’m checking the actual LaTeX warning surface before editing. That catches anything my static label comparison might miss, especially references outside `chapters/` or references hidden behind macros.
exec
/bin/zsh -lc "rg -n 'Reference "'`[''^`]+` undefined'"' main.log" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n '\\\\ref\\{thm:k3-kappa\\}' chapters/examples/k3_times_e.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n '\\\\label\\{thm:k3-kappa\\}' chapters notes ." in /Users/raeez/calabi-yau-quantum-groups exited 1 in 52ms:

 succeeded in 52ms:
409:This is consistent with the enhanced supersymmetry: the $\mathcal{N} = (4,4)$ algebra has a free-field realization in which the braiding becomes symmetric (non-quantum). Note that the modular characteristic $\kappa_{\mathrm{ch}}(K3) = 2$ (Theorem~\ref{thm:k3-kappa}) is a global invariant of the chiral algebra, not a point-wise function on $\cM_{K3}$; the trivialization of the $R$-matrix at the Gepner point reflects the enhanced symmetry of the representation category, not a vanishing of $\kappa_{\mathrm{ch}}$.
511:Theorem~\ref{thm:k3-kappa}.
687: \item \textup{(Proved.)} At genus~$1$: the shadow free energy $F_1 = \kappa_{\mathrm{ch}} / 24 = 2/24 = 1/12$ (Theorem~\ref{thm:k3-kappa}) matches the genus-$1$ Gromov--Witten contribution $\sum_h N_{1,h}^{\mathrm{red}} \, Q^h$ via the KKV formula, after extracting the $\kappa_{\mathrm{ch}}$-dependent piece.
 succeeded in 52ms:
chapters/examples/toroidal_elliptic.tex:4966:\label{thm:k3-kappa}
chapters/examples/k3_times_e.tex:315:\label{thm:k3-kappa}
./chapters/examples/toroidal_elliptic.tex:4966:\label{thm:k3-kappa}
./chapters/examples/k3_times_e.tex:315:\label{thm:k3-kappa}
exec
/bin/zsh -lc "sed -n '1,80p' chapters/connections/cy_holographic_datum_master.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "sed -n '5200,5245p' chapters/examples/toroidal_elliptic.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n '\\\\label\\{.*denom.*bar.*euler.*\\}|bar Euler product|eta\\"'^'"\\{24\\}|Leech lattice VOA' chapters/examples/k3_times_e.tex chapters/examples/toroidal_elliptic.tex chapters/theory/e1_chiral_algebras.tex chapters/theory/quantum_chiral_algebras.tex" in /Users/raeez/calabi-yau-quantum-groups succeeded in 52ms:
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% CHAPTER: The seven faces of r_{CY}(z) for Calabi-Yau chiral algebras
% Vol III specialization of the Vol I / Vol II seven-face programme.
% Mirrors Vol I Part III seven-face master and Vol II Part III seven-face master.
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%% Cross-volume label stubs. These labels are defined in Volume I and
%% referenced from this chapter. The phantomsection stubs prevent
%% undefined-reference errors at compile time; the canonical statements
%% live in Vol I.
\phantomsection\label{thm:gz26-commuting-differentials}%
\phantomsection\label{thm:gaudin-yangian-identification}%
\phantomsection\label{thm:yangian-sklyanin-quantization}%
\phantomsection\label{thm:dnp-bar-cobar-identification}%
\phantomsection\label{thm:kz-classical-quantum-bridge}%
\phantomsection\label{thm:shadow-depth-operator-order}%
\phantomsection\label{thm:vol1-seven-face-master}%
\phantomsection\label{thm:vol2-seven-face-master}%
\phantomsection\label{def:p-max}%
\phantomsection\label{def:k-max}%
 succeeded in 52ms:
\ClaimStatusProvedElsewhere
The genus-$0$ BPS invariants $n_h^0$ of $K3$ satisfy
\[
 \sum_{h \geq 0} n_h^0 \, q^h = \prod_{k \geq 1} \frac{1}{(1 - q^k)^{24}} = \frac{q}{\eta(q)^{24}},
\]
giving $n_0^0 = 1$, $n_1^0 = 24$, $n_2^0 = 324$, $n_3^0 = 3200$, $n_4^0 = 25650$, $n_5^0 = 176256$. Equivalently, $n_h^0 = \chi(\mathrm{Hilb}^h(K3))$.
\ClaimStatusProvedElsewhere
\end{theorem}

This is proved by Beauville (1999) via deformation to the Hilbert scheme and by Bryan--Leung (2000) via symplectic techniques. The BPS integrality $n_h^g \in \Z$ for all genera is proved by Pandharipande--Thomas (2016).

\begin{proposition}[BPS / shadow tower comparison]
\label{prop:k3e-bps-shadow}
The Yau--Zaslow generating function and the shadow obstruction tower of $A_{K3,\mathrm{rel}}$ are related by:
\begin{enumerate}[label=(\roman*)]
 \item At genus~$0$: $n_h^0 = \chi(\mathrm{Hilb}^h(K3))$ counts rational curves, while $F_0 = 0$ (the genus-$0$ shadow obstruction vanishes by definition of the shadow tower, which starts at $g \geq 1$).
 \item At genus~$1$: the shadow free energy $F_1 = \kappa_{\mathrm{ch}} / 24 = 2/24 = 1/12$ (Theorem~\ref{thm:k3-kappa}) matches the genus-$1$ Gromov--Witten contribution $\sum_h N_{1,h}^{\mathrm{red}} \, Q^h$ via the KKV formula, after extracting the $\kappa_{\mathrm{ch}}$-dependent piece.
 \item At genus~$g \geq 2$: $F_g = \kappa_{\mathrm{ch}} \cdot \lambda_g^{\mathrm{FP}} = 2 \cdot \lambda_g^{\mathrm{FP}}$ (all-weight, with cross-channel correction $\delta F_g^{\mathrm{cross}}$) captures the tautological class contribution, while the full genus-$g$ GW invariant receives additional contributions from higher BPS states $n_h^g$ with $g \leq h$.
\end{enumerate}
\ClaimStatusProvedHere
 succeeded in 51ms:
chapters/examples/k3_times_e.tex:514:constructed as the $\Z/2$-orbifold of the Leech lattice VOA $V_\Lambda$.
chapters/examples/k3_times_e.tex:523:(iii) \emph{Lattice VOA.} The Leech lattice VOA $V_\Lambda$ has $c = 24$ and
chapters/examples/k3_times_e.tex:836:The two lifts are related by the identity $\phi_{0,1} = \phi_{10,1} / \eta^{24}$ (up to the factor from $\phi_{12,1} / \Delta_{12}$), connecting the ``enumerative input'' ($\phi_{0,1}$, root multiplicities) to the ``automorphic output'' ($\phi_{10,1}$, Fourier--Jacobi coefficient).
chapters/examples/k3_times_e.tex:1127:functor (Conjecture~CY-A$_3$) and the Vol~I bar Euler product
chapters/examples/k3_times_e.tex:1131:(AP-CY8: the Borcherds denominator is not the bar Euler product without the CY-to-chiral functor).
chapters/examples/k3_times_e.tex:1406:The energy-graded bar Euler product is
chapters/examples/k3_times_e.tex:1432:The exponent~$24$ in the bar Euler product equals
chapters/examples/k3_times_e.tex:1440:\begin{remark}[Rank coincidence with the Leech lattice VOA]
chapters/examples/k3_times_e.tex:1442:The bar Euler product~\eqref{eq:k3-heisenberg-bar-euler} agrees with
chapters/examples/k3_times_e.tex:1443:that of the Leech lattice VOA $V_{\Lambda_{24}}$ of rank~$24$
chapters/examples/k3_times_e.tex:1447:energy-graded bar Euler product of any rank-$r$ lattice VOA or
chapters/examples/k3_times_e.tex:1451:in the \emph{full root-lattice-graded} bar Euler product,
chapters/examples/k3_times_e.tex:1776:The key identity: the ratio $\phi_{0,1} = \phi_{10,1}/\eta^{24}$
chapters/examples/k3_times_e.tex:1781:$\eta^{24}$. The one-loop correction $\phi_{10,1}/\eta^{24}$
chapters/examples/k3_times_e.tex:1784:$1/\eta^{24}$ and the first Fourier--Jacobi coefficient of the
chapters/examples/k3_times_e.tex:1873: The character is $1/\eta^{24}$ and all root
chapters/examples/k3_times_e.tex:1879: $\phi_{10,1}/\eta^{24}$ matches the first Fourier--Jacobi
chapters/examples/toroidal_elliptic.tex:2682:In the factorization $\eta^{18} = \eta^{24} \cdot \eta^{-6}$:
chapters/examples/toroidal_elliptic.tex:2683:$\eta^{24} = \Delta$ is the Ramanujan discriminant
chapters/examples/toroidal_elliptic.tex:2820:Leech lattice VOA $V_\Lambda$ through order $q^1$:

thinking
**Searching for theorems**

I'm looking into the `thm:denom-bar-euler`, which seems to exist only in notes. I wonder if there's a theorem related to the Leech lattice VOA bar Euler product in current volumes. I should search through k3_times_e or toroidal_elliptic, and maybe I can label it as `prop:leech-free-field`. I need to inspect around 2800 and see if I can find relevant information about the Leech lattice. Let's dive into the search!
codex
Two of the broken labels only exist in notes, not on the live build surface. I’m looking for the live Vol III statements that carry the same mathematical content so the fix stays truthful instead of introducing placeholder labels.
exec
/bin/zsh -lc "rg -n 'Leech lattice VOA|V_\\\\Lambda|V_\\{\\\\Lambda|rank-24 lattice VOA|bar Euler product.*Leech|denominator.*Euler' chapters/examples/toroidal_elliptic.tex chapters/examples/k3_times_e.tex chapters/examples/quantum_group_reps.tex chapters/theory/e1_chiral_algebras.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "sed -n '2800,2855p' chapters/examples/toroidal_elliptic.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "sed -n '4940,4995p' chapters/examples/toroidal_elliptic.tex" in /Users/raeez/calabi-yau-quantum-groups succeeded in 52ms:
chapters/examples/k3_times_e.tex:495: Lattice VOA & $V_\Lambda$ (Leech) & $24$ & $24$ & $\operatorname{rank}(\Lambda) = 24$ \\
chapters/examples/k3_times_e.tex:514:constructed as the $\Z/2$-orbifold of the Leech lattice VOA $V_\Lambda$.
chapters/examples/k3_times_e.tex:523:(iii) \emph{Lattice VOA.} The Leech lattice VOA $V_\Lambda$ has $c = 24$ and
chapters/examples/k3_times_e.tex:524:$\kappa_{\mathrm{ch}}(V_\Lambda) = \operatorname{rank}(\Lambda) = 24$
chapters/examples/k3_times_e.tex:541: $\Z/2$-orbifold of $V_\Lambda$. The orbifolding halves $\kappa_{\mathrm{ch}}$
chapters/examples/k3_times_e.tex:549:The ratio $\kappa_{\mathrm{ch}}(V_\Lambda) / \kappa_{\mathrm{ch}}(V^\natural) /
chapters/examples/k3_times_e.tex:1131:(AP-CY8: the Borcherds denominator is not the bar Euler product without the CY-to-chiral functor).
chapters/examples/k3_times_e.tex:1440:\begin{remark}[Rank coincidence with the Leech lattice VOA]
chapters/examples/k3_times_e.tex:1443:that of the Leech lattice VOA $V_{\Lambda_{24}}$ of rank~$24$
chapters/examples/k3_times_e.tex:1565:  V_{\Lambda_{K3}},
chapters/examples/k3_times_e.tex:1568:rank $22$ and signature $(3,19)$, and $V_{\Lambda_{K3}}$ is the
chapters/examples/k3_times_e.tex:1829: algebra $V_{\Lambda_E}$, where $\Lambda_E = U$ is the
chapters/examples/toroidal_elliptic.tex:2299:$V_\Lambda$ with $\Lambda$ determined by the fiber cohomology
chapters/examples/toroidal_elliptic.tex:2301:theorem, $\kappa_{\mathrm{ch}}(V_\Lambda) = \mathrm{rank}(\Lambda)$ for any
chapters/examples/toroidal_elliptic.tex:2322:$\kappa_{\mathrm{ch}}(V_\Lambda) = \mathrm{rank}(\Lambda)$ for all lattice VAs
chapters/examples/toroidal_elliptic.tex:2820:Leech lattice VOA $V_\Lambda$ through order $q^1$:
chapters/examples/toroidal_elliptic.tex:2822:$V_\Lambda$ has $\dim (V_\Lambda)_1 = 0$ and
chapters/examples/toroidal_elliptic.tex:2823:$\dim (V_\Lambda)_2 = 196560$. The two diverge at
chapters/examples/toroidal_elliptic.tex:2827:The Leech lattice has $\kappa_{\mathrm{ch}}(V_\Lambda) = 24 = \kappa_{\mathrm{ch}}(A_E)$
chapters/examples/toroidal_elliptic.tex:3743: structure of the Leech lattice VOA beyond free fields.
 succeeded in 50ms:
therefore proved at $g = 1$ and conditional at $g \geq 2$.
\end{proposition}

\begin{proof}
$\kappa_{\mathrm{ch}}(A_E) = 24$ (rank of the free-boson lattice).
$\kappa_{\mathrm{ch}}(V_{K3}) = 2$ (Proposition~\ref{prop:kappa-k3}).
Their ratio is $24/2 = 12$. At genus~$1$,
$F_1(\cA) = \kappa_{\mathrm{ch}}(\cA)/24$ for both algebras, giving the
ratio $12$. At $g \geq 2$: $A_E$ is uniform-weight (class~G),
so $F_g(A_E) = 24 \cdot \lambda_g^{\mathrm{FP}}$ at all genera $V_{K3}$ has generators at weights $1, 3/2, 2$; the scalar
formula $F_g = 2 \cdot \lambda_g^{\mathrm{FP}}$ is proved at
$g = 1$ but receives multi-weight cross-channel corrections
$\delta F_g^{\mathrm{cross}}$ at $g \geq 2$ \textup{(all-weight; Vol~I)}.
\end{proof}

\begin{remark}[Leech connection]
\label{rem:leech-connection}
\index{Leech lattice!K3 connection}
The boundary partition function
$Z_1(A_E;\tau) = 1/\eta(\tau)^{48}$ at genus~$1$ matches the
 succeeded in 50ms:
\ClaimStatusProvedElsewhere
\end{theorem}

\begin{remark}[CY involution]
\label{rem:k3e-cy-involution}
The functional equation $g(z)g(-z) = 1$ is the Yangian-level manifestation of the CY$_3$ Serre duality $\Ext^i(E,F) \simeq \Ext^{3-i}(F,E)^*$. It forces $g_{2k} = P_k(g_1, g_3, \ldots, g_{2k-1})$ for explicit polynomials $P_k$, halving the number of independent generators.
\end{remark}

\noindent\textit{Verification}: 90 tests in \texttt{k3e\_coha\_structure.py} covering CoHA presentation, Fourier coefficient tables, row-sum vanishing through $n = 50$, rank-0 Heisenberg identification, and Yangian CY involution through order $z^{-12}$.

\section{The relative chiral algebra}
\label{sec:k3e-relative-chiral}

The abstract functor $\Phi \colon D^b(\Coh(X)) \to \text{ChirAlg}$ of Conjecture CY-A$_3$ can be bypassed for $K3 \times E$ by exploiting the elliptic fibration $\pi \colon S \to \bP^1$ directly.

\begin{construction}[Relative chiral algebra]
\label{constr:k3e-relative-chiral}
The elliptic fibration $\pi \colon S \to \bP^1$ determines a relative derived category $D^b(\Coh_\pi(S))$ with a natural chiral algebra structure via fiberwise Fourier--Mukai. Let $A_{K3,\mathrm{rel}}$ denote this chiral algebra. Its defining data:
\begin{enumerate}[label=(\roman*)]
 \item The fiber over a generic point $t \in \bP^1$ is a smooth elliptic curve $E_t$, contributing a rank-$1$ Heisenberg factor.

thinking
**Considering chapter updates**

I'm thinking about the target chapter in the current volume, which specializes in Vol I and II. There's a label that needs fixing. Perhaps I could use a local analogy, but it’s only a reference fix. I could consider rephrasing it to say "cf. the seven-face holographic datum chapter," but that does change the wording a bit. I might just update the label and adjust "Vol I" to "the Vol III seven-face specialization."
exec
/bin/zsh -lc "sed -n '5200,5260p' chapters/examples/toroidal_elliptic.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "sed -n '730,860p' chapters/examples/k3_times_e.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n '\\\\label\\{thm:.*wall.*cross.*mc.*\\}|\\\\begin\\{theorem\\}\\[.*wall-crossing|Kontsevich--Soibelman|gauge transformation' chapters/examples/k3_times_e.tex" in /Users/raeez/calabi-yau-quantum-groups succeeded in 51ms:
\ClaimStatusProvedElsewhere
The genus-$0$ BPS invariants $n_h^0$ of $K3$ satisfy
\[
 \sum_{h \geq 0} n_h^0 \, q^h = \prod_{k \geq 1} \frac{1}{(1 - q^k)^{24}} = \frac{q}{\eta(q)^{24}},
\]
giving $n_0^0 = 1$, $n_1^0 = 24$, $n_2^0 = 324$, $n_3^0 = 3200$, $n_4^0 = 25650$, $n_5^0 = 176256$. Equivalently, $n_h^0 = \chi(\mathrm{Hilb}^h(K3))$.
\ClaimStatusProvedElsewhere
\end{theorem}

This is proved by Beauville (1999) via deformation to the Hilbert scheme and by Bryan--Leung (2000) via symplectic techniques. The BPS integrality $n_h^g \in \Z$ for all genera is proved by Pandharipande--Thomas (2016).

\begin{proposition}[BPS / shadow tower comparison]
\label{prop:k3e-bps-shadow}
The Yau--Zaslow generating function and the shadow obstruction tower of $A_{K3,\mathrm{rel}}$ are related by:
\begin{enumerate}[label=(\roman*)]
 \item At genus~$0$: $n_h^0 = \chi(\mathrm{Hilb}^h(K3))$ counts rational curves, while $F_0 = 0$ (the genus-$0$ shadow obstruction vanishes by definition of the shadow tower, which starts at $g \geq 1$).
 \item At genus~$1$: the shadow free energy $F_1 = \kappa_{\mathrm{ch}} / 24 = 2/24 = 1/12$ (Theorem~\ref{thm:k3-kappa}) matches the genus-$1$ Gromov--Witten contribution $\sum_h N_{1,h}^{\mathrm{red}} \, Q^h$ via the KKV formula, after extracting the $\kappa_{\mathrm{ch}}$-dependent piece.
 \item At genus~$g \geq 2$: $F_g = \kappa_{\mathrm{ch}} \cdot \lambda_g^{\mathrm{FP}} = 2 \cdot \lambda_g^{\mathrm{FP}}$ (all-weight, with cross-channel correction $\delta F_g^{\mathrm{cross}}$) captures the tautological class contribution, while the full genus-$g$ GW invariant receives additional contributions from higher BPS states $n_h^g$ with $g \leq h$.
\end{enumerate}
\ClaimStatusProvedHere
 succeeded in 51ms:
\[
 \cW(v_1, v_2) = \{ \sigma \in \mathrm{Stab}^\dagger(K3) : \phi_\sigma(v_1) = \phi_\sigma(v_2) \},
\]
where $\phi_\sigma(w) = (1/\pi) \arg Z_\sigma(w)$ is the phase. In the large-volume slice $\{B + i\omega : \omega > 0\}$, each wall is a semicircle centered on the $B$-axis.
\end{definition}

\begin{proposition}[Wall-crossing and root system]
\label{prop:k3e-walls-roots}
Crossing a wall $\cW(v_1, v_2)$ corresponds to a reflection in the root system of~$\mathfrak{g}_{\Delta_5}$:
\begin{enumerate}[label=(\roman*)]
 \item For $v_1^2 = v_2^2 = -2$ (both real roots), the wall-crossing is a \emph{flop}: the moduli space $M_\sigma(v)$ undergoes a birational transformation.
 \item For $v_i^2 = 0$ (a lightlike decomposition), the wall-crossing corresponds to a null root of $\mathfrak{g}_{\Delta_5}$ with multiplicity $f(0) = 10$ (or $c_0(0) = 20$ in the K3 elliptic genus convention).
 \item For $v_i^2 < 0$ (imaginary root), the wall-crossing acquires BPS multiplicity $\mult(\alpha) = |f(D(\alpha))|$ from the $\phi_{0,1}$ Fourier coefficients (Remark~\ref{rem:k3e-convention-delta5-phi10}).
\end{enumerate}
The chamber structure in $\mathrm{Stab}^\dagger(K3)$ is dual to the Weyl chamber decomposition of the positive cone in the root lattice of~$\mathfrak{g}_{\Delta_5}$.
\ClaimStatusProvedElsewhere
\end{proposition}

\subsection{Kontsevich--Soibelman wall-crossing formula}
\label{subsec:k3e-ks-formula}
 succeeded in 51ms:
748:\subsection{Kontsevich--Soibelman wall-crossing formula}
751:\begin{theorem}[KS wall-crossing for $K3 \times E$]
862:The Kontsevich--Soibelman wall-crossing formula and the shadow obstruction tower of the chiral algebra $A_{K3 \times E}$ are both governed by Maurer--Cartan elements in convolution algebras. The connection between them passes through the formalism of scattering diagrams.
912:The naive Baker--Campbell--Hausdorff pair-commutator of KS automorphisms does \emph{not} reproduce the $\phi_{0,1}$ multiplicities at low degrees. The quantitative mismatch was verified computationally: at degree~$4$, the naive BCH gives root multiplicities differing from $c(D)$ by non-uniform ratios that measure higher BPS bound-state contributions. The full identification requires the motivic DT theory of Kontsevich--Soibelman, in which the integration map $\int \colon \cH_{\mathrm{mot}} \to \hat{\C}[\Gamma]$ preserves the MC structure but introduces motivic measure corrections beyond the naive product formula.
1095: the monodromy around each wall is the Kontsevich--Soibelman
1096: gauge transformation of

thinking
**Searching for theorems**

I’m realizing there’s no theorem specifically named "k3e-wall-crossing-mc." It likely should be referenced as `thm:k3e-ks-wc`. I need to confirm that the wording "gauge transformation" is accurate, since the theorem might actually state something about KS automorphism, which fits the context. It also makes me think that the note could have been referring to an MC gauge theorem found in another location. I should check for the "MC-gauge" label.
exec
/bin/zsh -lc "rg -n '\\\\label\\{thm:ks-mc-gauge\\}|MC gauge|Maurer--Cartan gauge|wall-crossing.*MC' chapters" in /Users/raeez/calabi-yau-quantum-groups succeeded in 52ms:
chapters/examples/toric_cy3_coha.tex:112:\begin{theorem}[Wall-crossing as MC gauge transformation]
chapters/examples/toric_cy3_coha.tex:252:\section{Wall-crossing as MC gauge equivalence}
chapters/examples/toric_cy3_coha.tex:255:The Kontsevich--Soibelman wall-crossing formula, viewed through the shadow obstruction tower, is a gauge equivalence between MC elements.
chapters/examples/toric_cy3_coha.tex:257:\begin{theorem}[Wall-crossing $=$ MC gauge]
chapters/examples/toric_cy3_coha.tex:528:  is equivalent to the MC gauge equivalence
chapters/examples/toric_cy3_coha.tex:880:The MC gauge equivalence
chapters/examples/toroidal_elliptic.tex:5484:The $K3 \times E$ example exhibits every structural feature of the programme in concrete form: the fiber-to-global shadow depth jump (G $\to$ M), the genus-$1$ to genus-$2$ escalation via Borcherds lift, the infinite BKM root system from finite elliptic genus data, the DT/PT identity from $\chi = 0$, and the wall-crossing / scattering diagram connection to the MC formalism. It is the unique example where all five routes to the quantum vertex chiral group (Section~\ref{sec:k3e-five-routes}) are simultaneously available, making it the Rosetta stone for the CY quantum group programme.
chapters/examples/k3_times_e.tex:956:The $K3 \times E$ example exhibits every structural feature of the programme in concrete form: the fiber-to-global shadow depth jump (G $\to$ M), the genus-$1$ to genus-$2$ escalation via Borcherds lift, the infinite BKM root system from finite elliptic genus data, the DT/PT identity from $\chi = 0$, and the wall-crossing / scattering diagram connection to the MC formalism. It is the unique example where all five routes to the quantum vertex chiral group (Section~\ref{sec:k3e-five-routes}) are simultaneously available, making it the Rosetta stone for the CY quantum group programme.
chapters/connections/cy_holographic_datum_master.tex:606:automorphism. In the present language, this is exactly an MC gauge
chapters/frame/preface.tex:260:Kontsevich--Soibelman wall-crossing formula is the MC gauge
chapters/frame/preface.tex:323:wall-crossing is conjecturally MC gauge equivalence. The quantum
chapters/frame/preface.tex:490:\noindent\textbf{Wall-crossing as Maurer--Cartan gauge
chapters/frame/preface.tex:500:$\sigma'$ is Maurer--Cartan gauge equivalence
chapters/frame/preface.tex:664:(I)~wall-crossing as MC gauge equivalence; (J)~the
chapters/theory/introduction.tex:479: with transition maps given by MC gauge equivalence across walls.
chapters/theory/cy_to_chiral.tex:1202:\begin{theorem}[KS wall-crossing $=$ homotopy colimit $=$ MC gauge equivalence]
chapters/theory/cy_to_chiral.tex:1203:\label{thm:ks-mc-gauge}
chapters/theory/cy_to_chiral.tex:1252: \item The gauge equivalence class of $\Theta$ is chamber-independent: wall-crossing automorphisms $K_\gamma = \exp(\mathrm{Li}_2(X^\gamma) \cdot \partial_\gamma)$ act as MC gauge transformations, and the pentagon identity is a cocycle condition.
exec
/bin/zsh -lc "sed -n '1188,1225p' chapters/theory/cy_to_chiral.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "sed -n '588,616p' chapters/connections/cy_holographic_datum_master.tex" in /Users/raeez/calabi-yau-quantum-groups succeeded in 52ms:

\begin{proposition}[Quiver mutation = $\Eone$ quasi-isomorphism]
\label{prop:mutation-e1-equivalence}
\ClaimStatusProvedHere{}
Let $(Q, W)$ be a quiver with CY$_3$ potential and let $k$ be a vertex of $Q$ with no loops. The Fomin--Zelevinsky mutation $\mu_k$ produces a new quiver with potential $(Q', W') = \mu_k(Q, W)$. Then the induced map on critical CoHAs
\[
 \mu_k^* \colon \CoHA(Q, W) \;\xrightarrow{\;\simeq_{E_1}\;}\; \CoHA(Q', W')
\]
is an $\Eone$ quasi-isomorphism of associative dg algebras. The proof has four steps: (a)~mutation is a derived equivalence $\Phi_k \colon D^b(\mathrm{Jac}(Q,W)) \xrightarrow{\sim} D^b(\mathrm{Jac}(Q',W'))$ (Keller--Yang); (b)~derived equivalences of CY$_3$ categories preserve the cyclic $\Ainf$-structure; (c)~the cyclic $\Ainf$-structure determines the $\Eone$-CoHA multiplication; (d)~therefore $\mu_k$ induces an $\Eone$-algebra quasi-isomorphism on critical cohomology. On the charge lattice $\Gamma = \Z^{Q_0}$, mutation acts by $\mu_k(e_i) = e_i$ for $i \neq k$ and $\mu_k(e_k) = -e_k + \sum_{i \to k} e_i$. BPS invariants transform as $\Omega(\gamma;\sigma_+) = \Omega(\mu_k(\gamma);\sigma_-)$. Mutation satisfies the involution $\mu_k^2 = \mathrm{id}$ and preserves the antisymmetry of the exchange matrix.

\noindent\textit{Verification}: 155 tests in \texttt{test\_mutation\_e1\_equivalence.py}, verifying 16 independent paths including: mutation involution, exchange matrix antisymmetry, derived equivalence functor, cyclic $\Ainf$-preservation, $\Eone$ product compatibility, BPS spectrum transformation, and explicit conifold/local-$\bP^2$/$\C^3/\Z_2{\times}\Z_2$ computations (\texttt{mutation\_e1\_equivalence.py}).
\end{proposition}


\begin{theorem}[KS wall-crossing $=$ homotopy colimit $=$ MC gauge equivalence]
\label{thm:ks-mc-gauge}
\ClaimStatusProvedHere{}
For a CY$_3$ category $\cC$ with charge lattice $\Gamma$ and central charge $Z$, the following three formulations of Donaldson--Thomas theory are equivalent:
\begin{enumerate}[label=\textup{(\Roman*)}]
 \item \textbf{KS wall-crossing.} The DT partition function $Z_{\DT}(\cC, \sigma)$ is computed by the phase-ordered product $\prod_{\arg Z(\gamma) \downarrow} E(X^\gamma)^{\Omega(\gamma)}$ (labeled-ordered by decreasing phase of the central charge $Z$) of quantum dilogarithm factors in the quantum torus, with transitions across walls governed by the Kontsevich--Soibelman pentagon identity.
 succeeded in 52ms:
Fix marked points $z_1, \ldots, z_n \in \C$ (the chiral curve, with $n$
copies of the Fock representation of $Y(\widehat{\fgl}_1)$). Define
\[
 H_i^{\C^3} \;:=\; \sum_{j \neq i} \frac{k\,\Omega_{ij}^{Y(\widehat{\fgl}_1)}}{z_i - z_j}
 \;\in\; Y(\widehat{\fgl}_1)^{\otimes n},
\]
where $\Omega_{ij}^{Y(\widehat{\fgl}_1)}$ is the $Y(\widehat{\fgl}_1)$
Casimir $\Res_{z=0} r_{CY}^{\C^3}(z)$, acting on the $i$-th and $j$-th
tensor factors. The operators $\{H_i^{\C^3}\}$ commute pairwise as a
direct consequence of the classical Yang--Baxter equation for
$r_{CY}^{\C^3}$ (cf.\ Vol~I,
Theorem~\ref{thm:gaudin-yangian-identification}).
\end{construction}

\begin{remark}[Wall-crossing as gauge equivalence]
\label{rem:c3-wall-crossing-mc-gauge}
Across walls in the Bridgeland stability manifold, the toric Yangian
$r$-matrix transforms by a Kontsevich--Soibelman wall-crossing
automorphism. In the present language, this is exactly an MC gauge
equivalence on $\Theta_{A_X}$ (Theorem~\ref{thm:wall-crossing-mc}):

thinking
**Evaluating theorems and labels**

I’m noticing that the text mentions Vol I and recursion, specifically regarding higher shadows vanishing. It seems like I should look into the `thm:riccati-algebraicity` in toroidal_elliptic, since it's referenced somewhere else for MC recursion. I might need to see if this theorem addresses termination from S3=S4=0. Also, I’ll look for live theorems that match this content, like `prop:k3-heisenberg-bar-euler`. I'll have to check around line 1400 and examine nearby labels.
exec
/bin/zsh -lc "sed -n '1370,1455p' chapters/examples/k3_times_e.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "sed -n '2288,2335p' chapters/examples/toroidal_elliptic.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n '\\\\label\\{.*heisenberg.*bar.*euler.*|\\\\label\\{.*lattice.*voa.*|\\\\label\\{.*rank.*lattice.*|\\\\label\\{.*kappa.*lattice.*' chapters/examples/k3_times_e.tex chapters/examples/toroidal_elliptic.tex" in /Users/raeez/calabi-yau-quantum-groups succeeded in 50ms:
\, \mathbf{c}$.
Since $\gl_1$ has a one-dimensional invariant form normalised to~$1$,
the bracket is purely central.
The Jacobi identity holds trivially: every triple bracket vanishes
because $[\mathbf{c}, {-}] = 0$.
\end{proof}

The Mukai pairing matrix, in the ordered basis
$(\alpha_0, \alpha_1, \ldots, \alpha_{22}, \alpha_{23})$, has
block structure
\begin{equation}\label{eq:mukai-block-matrix}
  M_{\mathrm{Muk}} \;=\;
  \begin{pmatrix}
    0 & 0_{1 \times 22} & -1 \\
    0_{22 \times 1} & Q_{22} & 0_{22 \times 1} \\
    -1 & 0_{1 \times 22} & 0
  \end{pmatrix},
\end{equation}
where $Q_{22}$ is the intersection form on $H^2(S, \bZ)$ of
signature~$(3, 19)$.
 succeeded in 50ms:
 \]
 where $\eta_{ab} = \int_S \omega_a \wedge \omega_b$ is the
 intersection form restricted to $H^{1,1}(S)$, of signature
 $(1,19)$.
 \item The remaining generators \textup{(}from $H^{2,0}$,
 $H^{0,2}$, $H^0(\cO_S)$, $H^2(\cO_S)$\textup{)} have at most
 double-pole OPE.
 \item No poles of order $\geq 3$ appear: the $6$-dimensional
 theory is free with at most quadratic action.
\end{enumerate}
In particular, $\cA_{\mathrm{free}}$ is a lattice vertex algebra
$V_\Lambda$ with $\Lambda$ determined by the fiber cohomology
surviving the closure constraint. By the Vol~I lattice curvature
theorem, $\kappa_{\mathrm{ch}}(V_\Lambda) = \mathrm{rank}(\Lambda)$ for any
lattice VA, shadow class~$\mathbf{G}$
\textup{(}Gaussian, $r_{\max} = 2$\textup{)}, and the shadow
obstruction tower terminates:
$\Theta_{\cA_{\mathrm{free}}} = \kappa_{\mathrm{ch}} \cdot \omega_g$ at all genera \end{proposition}

\begin{remark}[The $\kappa_{\mathrm{ch}}$-collapse: rank $\to$ $\dim_\bC$]
 succeeded in 51ms:
chapters/examples/k3_times_e.tex:1407:\begin{equation}\label{eq:k3-heisenberg-bar-euler}
chapters/examples/toroidal_elliptic.tex:37:\phantomsection\label{thm:lattice-voa-bar}%
chapters/examples/toroidal_elliptic.tex:2132:\label{rem:lattice-voa-k3}

thinking
**Investigating a theorem label**

I see that `toroidal_elliptic` has a phantom label `thm:lattice-voa-bar`, which might relate to the lattice VOA bar complex. I should inspect this label more closely. It appears to be just a phantom section stub. I also note that the remark referencing `thm:denom-bar-euler` might actually need to point to `thm:lattice-voa-bar` instead. I need to find the exact statement of the lattice VOA bar theorem from Volume I and search its uses in the repository.
exec
/bin/zsh -lc "sed -n '1,60p' chapters/examples/toroidal_elliptic.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n 'thm:lattice-voa-bar' chapters main.tex ." in /Users/raeez/calabi-yau-quantum-groups succeeded in 52ms:
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% CHAPTER: TOROIDAL AND ELLIPTIC ALGEBRAS
% Migrated from Vol I (Chapter 66) with K3 x E content merged from k3_times_e.tex.
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%% Cross-volume label stubs: these labels are defined in Vol I and
%% referenced in this chapter. The stubs prevent undefined-reference
%% errors; the actual content lives in Vol I.
\phantomsection\label{conj:master-infinite-generator}%
\phantomsection\label{constr:platonic-package}%
\phantomsection\label{conv:bar-coalgebra-identity}%
\phantomsection\label{conv:hms-levels}%
\phantomsection\label{conv:regime-tags}%
\phantomsection\label{cor:bar-is-dgcoalg}%
\phantomsection\label{cor:shadow-extraction}%
\phantomsection\label{def:chiral-ass-operad}%
\phantomsection\label{def:cyclically-admissible}%
\phantomsection\label{def:shadow-depth-classification}%
\phantomsection\label{def:shadow-postnikov-tower}%
\phantomsection\label{prop:independent-sum-factorization}%
 succeeded in 52ms:
chapters/examples/toroidal_elliptic.tex:37:\phantomsection\label{thm:lattice-voa-bar}%
chapters/examples/toroidal_elliptic.tex:3429: Vol~I, Theorem~\ref{thm:lattice-voa-bar}, applied to the
./chapters/examples/toroidal_elliptic.tex:37:\phantomsection\label{thm:lattice-voa-bar}%
./chapters/examples/toroidal_elliptic.tex:3429: Vol~I, Theorem~\ref{thm:lattice-voa-bar}, applied to the
exec
/bin/zsh -lc "rg -n 'lattice curvature theorem|lattice VA|lattice VOA bar' chapters/examples/toroidal_elliptic.tex chapters/examples/k3_times_e.tex chapters/theory/e1_chiral_algebras.tex" in /Users/raeez/calabi-yau-quantum-groups succeeded in 51ms:
chapters/examples/k3_times_e.tex:516:(Vol~III, Remark~\ref{rem:lattice-voa-k3} and the lattice VOA bar complex of
chapters/examples/toroidal_elliptic.tex:2302:lattice VA, shadow class~$\mathbf{G}$
chapters/examples/toroidal_elliptic.tex:2321:can produce $\kappa_{\mathrm{ch}} = 2$: the Vol~I lattice curvature theorem gives
chapters/examples/toroidal_elliptic.tex:2322:$\kappa_{\mathrm{ch}}(V_\Lambda) = \mathrm{rank}(\Lambda)$ for all lattice VAs
codex
I’ve got candidate replacements for the theorem-level drifts. The remaining question is the orphan `ex:k3-step1`, which only exists in a note, so I’m locating the live Vol III surface that states the same K3 current-algebra input.
exec
/bin/zsh -lc "rg -n 'current algebra of the K3 lattice|current algebra of|Gerstenhaber bracket set to zero|class~G, free-field approximation|free-field approximation|Lie conformal algebra.*K3' chapters/examples/k3_times_e.tex chapters/theory/cy_to_chiral.tex chapters/examples/toroidal_elliptic.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "sed -n '1510,1605p' chapters/examples/k3_times_e.tex" in /Users/raeez/calabi-yau-quantum-groups succeeded in 50ms:
chapters/examples/k3_times_e.tex:1589:Example~\ref{ex:k3-step1}: the current algebra of
chapters/examples/k3_times_e.tex:1590:$\HH^*(\cC)$ with the Gerstenhaber bracket set to zero
chapters/examples/k3_times_e.tex:1591:(class~G, free-field approximation).
exec
/bin/zsh -lc "rg -n '\\\\label\\{(rem:lattice-voa-k3|def:k3-double-current-algebra|thm:k3-kappa|constr:k3e-relative-chiral|prop:k3e-heisenberg-bar|prop:k3-heisenberg-bar|def:k3-current|ex:k3.*)\\}' chapters/examples/k3_times_e.tex chapters/examples/toroidal_elliptic.tex chapters/theory/cy_to_chiral.tex" in /Users/raeez/calabi-yau-quantum-groups succeeded in 51ms:

\begin{remark}[Obstruction to the equivariant construction]
\label{rem:k3-yangian-obstruction}
For the affine Yangian $Y(\widehat{\gl}_1)$ of $\bC^3$, the structure
function has degree~$3$, matching the three equivariant parameters
$h_1, h_2, h_3$ (with $h_1 + h_2 + h_3 = 0$) of the torus action.
A K3 surface has no torus action, so the Maulik--Okounkov construction
of $R$-matrices via equivariant geometry does not apply directly.
The K3 Yangian must instead arise from the \emph{full Mukai lattice
structure}, giving a degree-$24$ structure function---a K3 analogue of
the quantum toroidal algebra rather than the affine Yangian.
The construction of $Y(\fg_{K3})$ is conditional on the CY-to-chiral
functor at $d = 2$ (CY-A$_2$, which is proved) together with a
separate quantisation step that remains open.
\end{remark}


%% ========================================================================
%% Perturbative factorization homology of K3
%% ========================================================================
 succeeded in 52ms:
chapters/examples/k3_times_e.tex:305:\label{constr:k3e-relative-chiral}
chapters/examples/k3_times_e.tex:315:\label{thm:k3-kappa}
chapters/examples/k3_times_e.tex:1170:\label{def:k3-double-current-algebra}
chapters/examples/k3_times_e.tex:1398:\label{prop:k3-heisenberg-bar}
chapters/examples/toroidal_elliptic.tex:2132:\label{rem:lattice-voa-k3}
chapters/examples/toroidal_elliptic.tex:4956:\label{constr:k3e-relative-chiral}
chapters/examples/toroidal_elliptic.tex:4966:\label{thm:k3-kappa}


thinking
**Examining references and labels**

I might need to consider `\eqref` or `\cref` in main.tex or the appendices since we only checked the chapters before. The user is focused on fixing broken references in Volume III, so running grep -rn in the chapters makes sense. But to be thorough, I should probably do a static comparison of all .tex files, including chapters and appendices, to catch any issues. I’ll keep an eye out for undefined references while building, possibly using `make fast`.
thinking
**Reviewing build options**

After applying the patch, I should consider running a narrow falsifier, like `latexmk` or possibly `make fast`. I might need to look at the Makefile, but that may not be necessary since it seems like `make fast` could be sufficient for fixing references in just one file. Alternatively, I can run `python3 tools/refcheck`, but I wonder if sticking with `make fast` might be the simplest approach. I'll check the Makefile for available targets.
codex
I’m patching the single live file with broken labels, keeping the edits strictly local to the stale cross-references. Two of the fixes retarget note-only labels to live Vol III / Vol I stub labels, and one removes an orphan example reference by inlining the description already present in the sentence.
codex
The patch failed on the orphan example reference because the local line wrapping shifted. I’m re-reading the exact spans and applying the same small edits against the live context.
exec
/bin/zsh -lc "sed -n '1582,1596p' chapters/examples/k3_times_e.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "sed -n '1426,1450p' chapters/examples/k3_times_e.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "sed -n '1018,1102p' chapters/examples/k3_times_e.tex" in /Users/raeez/calabi-yau-quantum-groups succeeded in 52ms:
\end{conjecture}

\begin{proof}[Derivation (conditional on CY-A$_3$)]
At $\sigma_3 = 0$, the Omega-background is trivial and the
topological $E_3$-factorization algebra reduces to a free (abelian)
factorization algebra. The classical fields are sections of
the Lie conformal algebra $\frakL_S$ of
Example~\ref{ex:k3-step1}: the current algebra of
$\HH^*(\cC)$ with the Gerstenhaber bracket set to zero
(class~G, free-field approximation).

The factorization homology of a free factorization algebra
on a manifold $M$ is computed by the Hochschild--Kostant--Rosenberg
theorem applied fiberwise. For $M = K3$:
\begin{enumerate}[label=(\roman*)]
 succeeded in 51ms:
\begin{proof}
The Heisenberg algebra $H_{\mathrm{Muk}}$ is $2$-step nilpotent,
so the Maurer--Cartan obstruction tower terminates at depth~$2$:
$S_3 = S_4 = 0$ forces all higher shadows to vanish by the
Vol~I recursion
(Theorem~\ref{thm:obstruction-recursion}).
The exponent~$24$ in the bar Euler product equals
$\dim H_{\mathrm{Muk}}^{\mathrm{ab}} = \dim H^*(S, \bC) = 24$:
each energy level $n \geq 1$ contributes $24$ bosonic oscillators
to the Chevalley--Eilenberg complex, and the Euler characteristic
of each exterior algebra $\Lambda^{\bullet}(\bC^{24})$ gives
the factor $(1 - q^n)^{24}$.
\end{proof}

\begin{remark}[Rank coincidence with the Leech lattice VOA]
\label{rem:k3-heisenberg-leech}
The bar Euler product~\eqref{eq:k3-heisenberg-bar-euler} agrees with
that of the Leech lattice VOA $V_{\Lambda_{24}}$ of rank~$24$
(see Theorem~\ref{thm:denom-bar-euler}).
Both produce $\eta(q)^{24}/q = \Delta(q)/q^2$.
 succeeded in 51ms:
\item $\lambda_5^{\mathrm{FP}} = 73/3503554560$. The
 unreduced numerator $2^{2g-1} - 1 = 511$ at $g = 5$
 requires GCD reduction with $(2g)!$.
\end{enumerate}

\section{The $K3 \times E$ holographic datum $H(K3 \times E)$}
\label{sec:k3e-holographic-datum}

The seven-face programme of Chapter~\ref{ch:holographic-datum-master}
assigns to each CY3 geometry a holographic modular Koszul datum
$H(X) = (A_X, A_X^!, r_X(z), \Theta_X, \kappa_{\mathrm{ch},X}, \nabla^{\mathrm{hol}}_X, \mathcal{G}_X)$
packaging boundary algebra, Koszul dual, $R$-matrix, MC element,
modular characteristic, holographic connection, and quantum group
into a single coherent object. The $K3 \times E$ tower specializes
this datum completely.

\begin{construction}[The $K3 \times E$ holographic datum]
\label{constr:k3e-holographic-datum}
The seven faces of $H(K3 \times E)$ are:
\begin{enumerate}[label=\textup{(\roman*)}]

thinking
**Inspecting formatting issues**

I'm considering how to inspect for possible multiple spaces or tabs in the text. It seems like checking with line breaks might help, so I could use a command like 'nl' to visualize line numbers. Plus, using 'sed -n' might assist in extracting specific lines or patterns. Okay, I'll go with that approach to ensure I get the formatting sorted out properly. Let's see if that gives me the clarity I need!
codex
The same orphan example line wrapped differently than the plain-text preview suggested. I’m grabbing the numbered lines and applying the edit in two smaller hunks so the rest of the patch stays unchanged.
exec
/bin/zsh -lc "nl -ba chapters/examples/k3_times_e.tex | sed -n '1584,1594p'" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "nl -ba chapters/examples/k3_times_e.tex | sed -n '1024,1100p'" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "nl -ba chapters/examples/k3_times_e.tex | sed -n '1428,1446p'" in /Users/raeez/calabi-yau-quantum-groups succeeded in 51ms:
  1584	\begin{proof}[Derivation (conditional on CY-A$_3$)]
  1585	At $\sigma_3 = 0$, the Omega-background is trivial and the
  1586	topological $E_3$-factorization algebra reduces to a free (abelian)
  1587	factorization algebra. The classical fields are sections of
  1588	the Lie conformal algebra $\frakL_S$ of
  1589	Example~\ref{ex:k3-step1}: the current algebra of
  1590	$\HH^*(\cC)$ with the Gerstenhaber bracket set to zero
  1591	(class~G, free-field approximation).
  1592	
  1593	The factorization homology of a free factorization algebra
  1594	on a manifold $M$ is computed by the Hochschild--Kostant--Rosenberg
 succeeded in 51ms:
  1024	\label{sec:k3e-holographic-datum}
  1025	
  1026	The seven-face programme of Chapter~\ref{ch:holographic-datum-master}
  1027	assigns to each CY3 geometry a holographic modular Koszul datum
  1028	$H(X) = (A_X, A_X^!, r_X(z), \Theta_X, \kappa_{\mathrm{ch},X}, \nabla^{\mathrm{hol}}_X, \mathcal{G}_X)$
  1029	packaging boundary algebra, Koszul dual, $R$-matrix, MC element,
  1030	modular characteristic, holographic connection, and quantum group
  1031	into a single coherent object. The $K3 \times E$ tower specializes
  1032	this datum completely.
  1033	
  1034	\begin{construction}[The $K3 \times E$ holographic datum]
  1035	\label{constr:k3e-holographic-datum}
  1036	The seven faces of $H(K3 \times E)$ are:
  1037	\begin{enumerate}[label=\textup{(\roman*)}]
  1038	 \item \emph{Boundary algebra} $A_{K3 \times E}$. The chiral algebra
  1039	 of the K3 sigma model tensored with the free boson on $E$,
  1040	 carrying central charge $c = 6$ and conformal weights
  1041	 $(h_1, h_2, h_3) = (1, 1, 1)$ from the three complex directions.
  1042	 The sigma model factor $V_{K3}$ is multi-weight;
  1043	 the elliptic factor contributes a single Heisenberg generator.
 succeeded in 51ms:
  1428	so the Maurer--Cartan obstruction tower terminates at depth~$2$:
  1429	$S_3 = S_4 = 0$ forces all higher shadows to vanish by the
  1430	Vol~I recursion
  1431	(Theorem~\ref{thm:obstruction-recursion}).
  1432	The exponent~$24$ in the bar Euler product equals
  1433	$\dim H_{\mathrm{Muk}}^{\mathrm{ab}} = \dim H^*(S, \bC) = 24$:
  1434	each energy level $n \geq 1$ contributes $24$ bosonic oscillators
  1435	to the Chevalley--Eilenberg complex, and the Euler characteristic
  1436	of each exterior algebra $\Lambda^{\bullet}(\bC^{24})$ gives
  1437	the factor $(1 - q^n)^{24}$.
  1438	\end{proof}
  1439	
  1440	\begin{remark}[Rank coincidence with the Leech lattice VOA]
  1441	\label{rem:k3-heisenberg-leech}
  1442	The bar Euler product~\eqref{eq:k3-heisenberg-bar-euler} agrees with
  1443	that of the Leech lattice VOA $V_{\Lambda_{24}}$ of rank~$24$
  1444	(see Theorem~\ref{thm:denom-bar-euler}).
  1445	Both produce $\eta(q)^{24}/q = \Delta(q)/q^2$.
  1446	This agreement is a consequence of rank universality: the

thinking
**Considering patch issues**

I’m thinking that the patch might have failed because the earlier apply_patch wasn’t matching due to previous hunks. It seems like a good idea to create a smaller patch with precise line blocks. Maybe I could also consider using two updates in one patch for the same file. That way, I can keep it manageable and hopefully avoid further mismatches! It's all about making the process smoother.
file update
M /Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3_times_e.tex
@@ -1025,3 +1025,3 @@
 
-The seven-face programme of Chapter~\ref{ch:holographic-datum-master}
+The seven-face programme of Chapter~\ref{ch:cy-holographic-datum-master}
 assigns to each CY3 geometry a holographic modular Koszul datum
@@ -1061,3 +1061,3 @@
  $K3 \times E$, this is the Maulik--Okounkov $R$-matrix
- $R^{\mathrm{MO}}(z)$ of Section~\ref{sec:mo-r-matrix},
+ $R^{\mathrm{MO}}(z)$ of Section~\ref{sec:k3e-mo-rmatrix},
  acting on the BPS Fock space. The $R$-matrix controls the
@@ -1070,3 +1070,3 @@
  \item \emph{MC element} $\Theta_{K3 \times E}$. The bar-intrinsic
- construction (cf.\ Vol~I, Chapter~\ref{ch:holographic-datum-master})
+ construction (cf.\ Chapter~\ref{ch:cy-holographic-datum-master})
  gives $\Theta_A := D_A - d_0 \in \mathrm{MC}(\mathfrak{g}^{\mathrm{mod}}_{A})$.
@@ -1096,3 +1096,3 @@
  gauge transformation of
- Theorem~\ref{thm:k3e-wall-crossing-mc}.
+ Theorem~\ref{thm:ks-mc-gauge}.
 
@@ -1430,3 +1430,3 @@
 Vol~I recursion
-(Theorem~\ref{thm:obstruction-recursion}).
+(Theorem~\ref{thm:riccati-algebraicity}).
 The exponent~$24$ in the bar Euler product equals
@@ -1443,3 +1443,3 @@
 that of the Leech lattice VOA $V_{\Lambda_{24}}$ of rank~$24$
-(see Theorem~\ref{thm:denom-bar-euler}).
+(see Theorem~\ref{thm:lattice-voa-bar}).
 Both produce $\eta(q)^{24}/q = \Delta(q)/q^2$.
apply_patch(auto_approved=true) exited 0 in 21ms:
Success. Updated the following files:
M /Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3_times_e.tex
file update:
diff --git a/chapters/examples/k3_times_e.tex b/chapters/examples/k3_times_e.tex
index bee9416b63e4a821b9403dbf1aecac2dc101b7dd..6675f735c7aaca4c22f6a84b42fecf8ed3c52982
--- a/chapters/examples/k3_times_e.tex
+++ b/chapters/examples/k3_times_e.tex
@@ -1023,7 +1023,7 @@
 \section{The $K3 \times E$ holographic datum $H(K3 \times E)$}
 \label{sec:k3e-holographic-datum}
 
-The seven-face programme of Chapter~\ref{ch:holographic-datum-master}
+The seven-face programme of Chapter~\ref{ch:cy-holographic-datum-master}
 assigns to each CY3 geometry a holographic modular Koszul datum
 $H(X) = (A_X, A_X^!, r_X(z), \Theta_X, \kappa_{\mathrm{ch},X}, \nabla^{\mathrm{hol}}_X, \mathcal{G}_X)$
 packaging boundary algebra, Koszul dual, $R$-matrix, MC element,
@@ -1059,7 +1059,7 @@
  residue $r(z) = \operatorname{Res}^{\mathrm{coll}}_{0,2}(\Theta_A)$
  is the binary genus-$0$ shadow of the full MC element. For
  $K3 \times E$, this is the Maulik--Okounkov $R$-matrix
- $R^{\mathrm{MO}}(z)$ of Section~\ref{sec:mo-r-matrix},
+ $R^{\mathrm{MO}}(z)$ of Section~\ref{sec:k3e-mo-rmatrix},
  acting on the BPS Fock space. The $R$-matrix controls the
  Yangian structure of the BKM superalgebra: $R^{\mathrm{MO}}(z)$
  satisfies the Yang--Baxter equation with spectral parameter
@@ -1068,7 +1068,7 @@
  moduli of sheaves.
 
  \item \emph{MC element} $\Theta_{K3 \times E}$. The bar-intrinsic
- construction (cf.\ Vol~I, Chapter~\ref{ch:holographic-datum-master})
+ construction (cf.\ Chapter~\ref{ch:cy-holographic-datum-master})
  gives $\Theta_A := D_A - d_0 \in \mathrm{MC}(\mathfrak{g}^{\mathrm{mod}}_{A})$.
  The projections yield: $\kappa_{\mathrm{ch}} = 3$ at degree~$2$
  (from $\kappa_{\mathrm{ch}}(K3) + \kappa_{\mathrm{ch}}(E) = 2 + 1$), the cubic
@@ -1094,7 +1094,7 @@
  is the wall-crossing divisor of Section~\ref{sec:k3e-wall-crossing};
  the monodromy around each wall is the Kontsevich--Soibelman
  gauge transformation of
- Theorem~\ref{thm:k3e-wall-crossing-mc}.
+ Theorem~\ref{thm:ks-mc-gauge}.
 
  \item \emph{Quantum group} $\mathcal{G}(K3 \times E)$.
  The quantum vertex chiral group of
@@ -1428,7 +1428,7 @@
 so the Maurer--Cartan obstruction tower terminates at depth~$2$:
 $S_3 = S_4 = 0$ forces all higher shadows to vanish by the
 Vol~I recursion
-(Theorem~\ref{thm:obstruction-recursion}).
+(Theorem~\ref{thm:riccati-algebraicity}).
 The exponent~$24$ in the bar Euler product equals
 $\dim H_{\mathrm{Muk}}^{\mathrm{ab}} = \dim H^*(S, \bC) = 24$:
 each energy level $n \geq 1$ contributes $24$ bosonic oscillators
@@ -1441,7 +1441,7 @@
 \label{rem:k3-heisenberg-leech}
 The bar Euler product~\eqref{eq:k3-heisenberg-bar-euler} agrees with
 that of the Leech lattice VOA $V_{\Lambda_{24}}$ of rank~$24$
-(see Theorem~\ref{thm:denom-bar-euler}).
+(see Theorem~\ref{thm:lattice-voa-bar}).
 Both produce $\eta(q)^{24}/q = \Delta(q)/q^2$.
 This agreement is a consequence of rank universality: the
 energy-graded bar Euler product of any rank-$r$ lattice VOA or

file update:
diff --git a/chapters/examples/k3_times_e.tex b/chapters/examples/k3_times_e.tex
index bee9416b63e4a821b9403dbf1aecac2dc101b7dd..6675f735c7aaca4c22f6a84b42fecf8ed3c52982
--- a/chapters/examples/k3_times_e.tex
+++ b/chapters/examples/k3_times_e.tex
@@ -1023,7 +1023,7 @@
 \section{The $K3 \times E$ holographic datum $H(K3 \times E)$}
 \label{sec:k3e-holographic-datum}
 
-The seven-face programme of Chapter~\ref{ch:holographic-datum-master}
+The seven-face programme of Chapter~\ref{ch:cy-holographic-datum-master}
 assigns to each CY3 geometry a holographic modular Koszul datum
 $H(X) = (A_X, A_X^!, r_X(z), \Theta_X, \kappa_{\mathrm{ch},X}, \nabla^{\mathrm{hol}}_X, \mathcal{G}_X)$
 packaging boundary algebra, Koszul dual, $R$-matrix, MC element,
@@ -1059,7 +1059,7 @@
  residue $r(z) = \operatorname{Res}^{\mathrm{coll}}_{0,2}(\Theta_A)$
  is the binary genus-$0$ shadow of the full MC element. For
  $K3 \times E$, this is the Maulik--Okounkov $R$-matrix
- $R^{\mathrm{MO}}(z)$ of Section~\ref{sec:mo-r-matrix},
+ $R^{\mathrm{MO}}(z)$ of Section~\ref{sec:k3e-mo-rmatrix},
  acting on the BPS Fock space. The $R$-matrix controls the
  Yangian structure of the BKM superalgebra: $R^{\mathrm{MO}}(z)$
  satisfies the Yang--Baxter equation with spectral parameter
@@ -1068,7 +1068,7 @@
  moduli of sheaves.
 
  \item \emph{MC element} $\Theta_{K3 \times E}$. The bar-intrinsic
- construction (cf.\ Vol~I, Chapter~\ref{ch:holographic-datum-master})
+ construction (cf.\ Chapter~\ref{ch:cy-holographic-datum-master})
  gives $\Theta_A := D_A - d_0 \in \mathrm{MC}(\mathfrak{g}^{\mathrm{mod}}_{A})$.
  The projections yield: $\kappa_{\mathrm{ch}} = 3$ at degree~$2$
  (from $\kappa_{\mathrm{ch}}(K3) + \kappa_{\mathrm{ch}}(E) = 2 + 1$), the cubic
@@ -1094,7 +1094,7 @@
  is the wall-crossing divisor of Section~\ref{sec:k3e-wall-crossing};
  the monodromy around each wall is the Kontsevich--Soibelman
  gauge transformation of
- Theorem~\ref{thm:k3e-wall-crossing-mc}.
+ Theorem~\ref{thm:ks-mc-gauge}.
 
  \item \emph{Quantum group} $\mathcal{G}(K3 \times E)$.
  The quantum vertex chiral group of
@@ -1428,7 +1428,7 @@
 so the Maurer--Cartan obstruction tower terminates at depth~$2$:
 $S_3 = S_4 = 0$ forces all higher shadows to vanish by the
 Vol~I recursion
-(Theorem~\ref{thm:obstruction-recursion}).
+(Theorem~\ref{thm:riccati-algebraicity}).
 The exponent~$24$ in the bar Euler product equals
 $\dim H_{\mathrm{Muk}}^{\mathrm{ab}} = \dim H^*(S, \bC) = 24$:
 each energy level $n \geq 1$ contributes $24$ bosonic oscillators
@@ -1441,7 +1441,7 @@
 \label{rem:k3-heisenberg-leech}
 The bar Euler product~\eqref{eq:k3-heisenberg-bar-euler} agrees with
 that of the Leech lattice VOA $V_{\Lambda_{24}}$ of rank~$24$
-(see Theorem~\ref{thm:denom-bar-euler}).
+(see Theorem~\ref{thm:lattice-voa-bar}).
 Both produce $\eta(q)^{24}/q = \Delta(q)/q^2$.
 This agreement is a consequence of rank universality: the
 energy-graded bar Euler product of any rank-$r$ lattice VOA or

file update
M /Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3_times_e.tex
@@ -1587,4 +1587,3 @@
 factorization algebra. The classical fields are sections of
-the Lie conformal algebra $\frakL_S$ of
-Example~\ref{ex:k3-step1}: the current algebra of
+the Lie conformal algebra $\frakL_S$: the current algebra of
 $\HH^*(\cC)$ with the Gerstenhaber bracket set to zero
apply_patch(auto_approved=true) exited 0 in 20ms:
Success. Updated the following files:
M /Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3_times_e.tex
file update:
diff --git a/chapters/examples/k3_times_e.tex b/chapters/examples/k3_times_e.tex
index bee9416b63e4a821b9403dbf1aecac2dc101b7dd..071fdbb01c23e43e1db7a272d12e2aa17215906e
--- a/chapters/examples/k3_times_e.tex
+++ b/chapters/examples/k3_times_e.tex
@@ -1023,7 +1023,7 @@
 \section{The $K3 \times E$ holographic datum $H(K3 \times E)$}
 \label{sec:k3e-holographic-datum}
 
-The seven-face programme of Chapter~\ref{ch:holographic-datum-master}
+The seven-face programme of Chapter~\ref{ch:cy-holographic-datum-master}
 assigns to each CY3 geometry a holographic modular Koszul datum
 $H(X) = (A_X, A_X^!, r_X(z), \Theta_X, \kappa_{\mathrm{ch},X}, \nabla^{\mathrm{hol}}_X, \mathcal{G}_X)$
 packaging boundary algebra, Koszul dual, $R$-matrix, MC element,
@@ -1059,7 +1059,7 @@
  residue $r(z) = \operatorname{Res}^{\mathrm{coll}}_{0,2}(\Theta_A)$
  is the binary genus-$0$ shadow of the full MC element. For
  $K3 \times E$, this is the Maulik--Okounkov $R$-matrix
- $R^{\mathrm{MO}}(z)$ of Section~\ref{sec:mo-r-matrix},
+ $R^{\mathrm{MO}}(z)$ of Section~\ref{sec:k3e-mo-rmatrix},
  acting on the BPS Fock space. The $R$-matrix controls the
  Yangian structure of the BKM superalgebra: $R^{\mathrm{MO}}(z)$
  satisfies the Yang--Baxter equation with spectral parameter
@@ -1068,7 +1068,7 @@
  moduli of sheaves.
 
  \item \emph{MC element} $\Theta_{K3 \times E}$. The bar-intrinsic
- construction (cf.\ Vol~I, Chapter~\ref{ch:holographic-datum-master})
+ construction (cf.\ Chapter~\ref{ch:cy-holographic-datum-master})
  gives $\Theta_A := D_A - d_0 \in \mathrm{MC}(\mathfrak{g}^{\mathrm{mod}}_{A})$.
  The projections yield: $\kappa_{\mathrm{ch}} = 3$ at degree~$2$
  (from $\kappa_{\mathrm{ch}}(K3) + \kappa_{\mathrm{ch}}(E) = 2 + 1$), the cubic
@@ -1094,7 +1094,7 @@
  is the wall-crossing divisor of Section~\ref{sec:k3e-wall-crossing};
  the monodromy around each wall is the Kontsevich--Soibelman
  gauge transformation of
- Theorem~\ref{thm:k3e-wall-crossing-mc}.
+ Theorem~\ref{thm:ks-mc-gauge}.
 
  \item \emph{Quantum group} $\mathcal{G}(K3 \times E)$.
  The quantum vertex chiral group of
@@ -1428,7 +1428,7 @@
 so the Maurer--Cartan obstruction tower terminates at depth~$2$:
 $S_3 = S_4 = 0$ forces all higher shadows to vanish by the
 Vol~I recursion
-(Theorem~\ref{thm:obstruction-recursion}).
+(Theorem~\ref{thm:riccati-algebraicity}).
 The exponent~$24$ in the bar Euler product equals
 $\dim H_{\mathrm{Muk}}^{\mathrm{ab}} = \dim H^*(S, \bC) = 24$:
 each energy level $n \geq 1$ contributes $24$ bosonic oscillators
@@ -1441,7 +1441,7 @@
 \label{rem:k3-heisenberg-leech}
 The bar Euler product~\eqref{eq:k3-heisenberg-bar-euler} agrees with
 that of the Leech lattice VOA $V_{\Lambda_{24}}$ of rank~$24$
-(see Theorem~\ref{thm:denom-bar-euler}).
+(see Theorem~\ref{thm:lattice-voa-bar}).
 Both produce $\eta(q)^{24}/q = \Delta(q)/q^2$.
 This agreement is a consequence of rank universality: the
 energy-graded bar Euler product of any rank-$r$ lattice VOA or
@@ -1585,8 +1585,7 @@
 At $\sigma_3 = 0$, the Omega-background is trivial and the
 topological $E_3$-factorization algebra reduces to a free (abelian)
 factorization algebra. The classical fields are sections of
-the Lie conformal algebra $\frakL_S$ of
-Example~\ref{ex:k3-step1}: the current algebra of
+the Lie conformal algebra $\frakL_S$: the current algebra of
 $\HH^*(\cC)$ with the Gerstenhaber bracket set to zero
 (class~G, free-field approximation).
 

file update:
diff --git a/chapters/examples/k3_times_e.tex b/chapters/examples/k3_times_e.tex
index bee9416b63e4a821b9403dbf1aecac2dc101b7dd..071fdbb01c23e43e1db7a272d12e2aa17215906e
--- a/chapters/examples/k3_times_e.tex
+++ b/chapters/examples/k3_times_e.tex
@@ -1023,7 +1023,7 @@
 \section{The $K3 \times E$ holographic datum $H(K3 \times E)$}
 \label{sec:k3e-holographic-datum}
 
-The seven-face programme of Chapter~\ref{ch:holographic-datum-master}
+The seven-face programme of Chapter~\ref{ch:cy-holographic-datum-master}
 assigns to each CY3 geometry a holographic modular Koszul datum
 $H(X) = (A_X, A_X^!, r_X(z), \Theta_X, \kappa_{\mathrm{ch},X}, \nabla^{\mathrm{hol}}_X, \mathcal{G}_X)$
 packaging boundary algebra, Koszul dual, $R$-matrix, MC element,
@@ -1059,7 +1059,7 @@
  residue $r(z) = \operatorname{Res}^{\mathrm{coll}}_{0,2}(\Theta_A)$
  is the binary genus-$0$ shadow of the full MC element. For
  $K3 \times E$, this is the Maulik--Okounkov $R$-matrix
- $R^{\mathrm{MO}}(z)$ of Section~\ref{sec:mo-r-matrix},
+ $R^{\mathrm{MO}}(z)$ of Section~\ref{sec:k3e-mo-rmatrix},
  acting on the BPS Fock space. The $R$-matrix controls the
  Yangian structure of the BKM superalgebra: $R^{\mathrm{MO}}(z)$
  satisfies the Yang--Baxter equation with spectral parameter
@@ -1068,7 +1068,7 @@
  moduli of sheaves.
 
  \item \emph{MC element} $\Theta_{K3 \times E}$. The bar-intrinsic
- construction (cf.\ Vol~I, Chapter~\ref{ch:holographic-datum-master})
+ construction (cf.\ Chapter~\ref{ch:cy-holographic-datum-master})
  gives $\Theta_A := D_A - d_0 \in \mathrm{MC}(\mathfrak{g}^{\mathrm{mod}}_{A})$.
  The projections yield: $\kappa_{\mathrm{ch}} = 3$ at degree~$2$
  (from $\kappa_{\mathrm{ch}}(K3) + \kappa_{\mathrm{ch}}(E) = 2 + 1$), the cubic
@@ -1094,7 +1094,7 @@
  is the wall-crossing divisor of Section~\ref{sec:k3e-wall-crossing};
  the monodromy around each wall is the Kontsevich--Soibelman
  gauge transformation of
- Theorem~\ref{thm:k3e-wall-crossing-mc}.
+ Theorem~\ref{thm:ks-mc-gauge}.
 
  \item \emph{Quantum group} $\mathcal{G}(K3 \times E)$.
  The quantum vertex chiral group of
@@ -1428,7 +1428,7 @@
 so the Maurer--Cartan obstruction tower terminates at depth~$2$:
 $S_3 = S_4 = 0$ forces all higher shadows to vanish by the
 Vol~I recursion
-(Theorem~\ref{thm:obstruction-recursion}).
+(Theorem~\ref{thm:riccati-algebraicity}).
 The exponent~$24$ in the bar Euler product equals
 $\dim H_{\mathrm{Muk}}^{\mathrm{ab}} = \dim H^*(S, \bC) = 24$:
 each energy level $n \geq 1$ contributes $24$ bosonic oscillators
@@ -1441,7 +1441,7 @@
 \label{rem:k3-heisenberg-leech}
 The bar Euler product~\eqref{eq:k3-heisenberg-bar-euler} agrees with
 that of the Leech lattice VOA $V_{\Lambda_{24}}$ of rank~$24$
-(see Theorem~\ref{thm:denom-bar-euler}).
+(see Theorem~\ref{thm:lattice-voa-bar}).
 Both produce $\eta(q)^{24}/q = \Delta(q)/q^2$.
 This agreement is a consequence of rank universality: the
 energy-graded bar Euler product of any rank-$r$ lattice VOA or
@@ -1585,8 +1585,7 @@
 At $\sigma_3 = 0$, the Omega-background is trivial and the
 topological $E_3$-factorization algebra reduces to a free (abelian)
 factorization algebra. The classical fields are sections of
-the Lie conformal algebra $\frakL_S$ of
-Example~\ref{ex:k3-step1}: the current algebra of
+the Lie conformal algebra $\frakL_S$: the current algebra of
 $\HH^*(\cC)$ with the Gerstenhaber bracket set to zero
 (class~G, free-field approximation).
 

codex
The patch is in. I’m re-reading the touched spans to make sure the new targets fit the surrounding claims, then I’ll run a full missing-label check on the live build surface.
exec
/bin/zsh -lc "sed -n '1024,1098p' chapters/examples/k3_times_e.tex" in /Users/raeez/calabi-yau-quantum-groups succeeded in 52ms:
\label{sec:k3e-holographic-datum}

The seven-face programme of Chapter~\ref{ch:cy-holographic-datum-master}
assigns to each CY3 geometry a holographic modular Koszul datum
$H(X) = (A_X, A_X^!, r_X(z), \Theta_X, \kappa_{\mathrm{ch},X}, \nabla^{\mathrm{hol}}_X, \mathcal{G}_X)$
packaging boundary algebra, Koszul dual, $R$-matrix, MC element,
modular characteristic, holographic connection, and quantum group
into a single coherent object. The $K3 \times E$ tower specializes
this datum completely.

\begin{construction}[The $K3 \times E$ holographic datum]
\label{constr:k3e-holographic-datum}
The seven faces of $H(K3 \times E)$ are:
\begin{enumerate}[label=\textup{(\roman*)}]
 \item \emph{Boundary algebra} $A_{K3 \times E}$. The chiral algebra
 of the K3 sigma model tensored with the free boson on $E$,
 carrying central charge $c = 6$ and conformal weights
 $(h_1, h_2, h_3) = (1, 1, 1)$ from the three complex directions.
 The sigma model factor $V_{K3}$ is multi-weight;
 the elliptic factor contributes a single Heisenberg generator.
exec
/bin/zsh -lc "sed -n '1428,1446p' chapters/examples/k3_times_e.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "sed -n '1584,1592p' chapters/examples/k3_times_e.tex" in /Users/raeez/calabi-yau-quantum-groups succeeded in 51ms:
\begin{proof}[Derivation (conditional on CY-A$_3$)]
At $\sigma_3 = 0$, the Omega-background is trivial and the
topological $E_3$-factorization algebra reduces to a free (abelian)
factorization algebra. The classical fields are sections of
the Lie conformal algebra $\frakL_S$: the current algebra of
$\HH^*(\cC)$ with the Gerstenhaber bracket set to zero
(class~G, free-field approximation).

The factorization homology of a free factorization algebra
 succeeded in 51ms:
so the Maurer--Cartan obstruction tower terminates at depth~$2$:
$S_3 = S_4 = 0$ forces all higher shadows to vanish by the
Vol~I recursion
(Theorem~\ref{thm:riccati-algebraicity}).
The exponent~$24$ in the bar Euler product equals
$\dim H_{\mathrm{Muk}}^{\mathrm{ab}} = \dim H^*(S, \bC) = 24$:
each energy level $n \geq 1$ contributes $24$ bosonic oscillators
to the Chevalley--Eilenberg complex, and the Euler characteristic
of each exterior algebra $\Lambda^{\bullet}(\bC^{24})$ gives
the factor $(1 - q^n)^{24}$.
\end{proof}

\begin{remark}[Rank coincidence with the Leech lattice VOA]
\label{rem:k3-heisenberg-leech}
The bar Euler product~\eqref{eq:k3-heisenberg-bar-euler} agrees with
that of the Leech lattice VOA $V_{\Lambda_{24}}$ of rank~$24$
(see Theorem~\ref{thm:lattice-voa-bar}).
Both produce $\eta(q)^{24}/q = \Delta(q)/q^2$.
This agreement is a consequence of rank universality: the
file update:
diff --git a/chapters/examples/k3_times_e.tex b/chapters/examples/k3_times_e.tex
index bee9416b63e4a821b9403dbf1aecac2dc101b7dd..071fdbb01c23e43e1db7a272d12e2aa17215906e
--- a/chapters/examples/k3_times_e.tex
+++ b/chapters/examples/k3_times_e.tex
@@ -1023,7 +1023,7 @@
 \section{The $K3 \times E$ holographic datum $H(K3 \times E)$}
 \label{sec:k3e-holographic-datum}
 
-The seven-face programme of Chapter~\ref{ch:holographic-datum-master}
+The seven-face programme of Chapter~\ref{ch:cy-holographic-datum-master}
 assigns to each CY3 geometry a holographic modular Koszul datum
 $H(X) = (A_X, A_X^!, r_X(z), \Theta_X, \kappa_{\mathrm{ch},X}, \nabla^{\mathrm{hol}}_X, \mathcal{G}_X)$
 packaging boundary algebra, Koszul dual, $R$-matrix, MC element,
@@ -1059,7 +1059,7 @@
  residue $r(z) = \operatorname{Res}^{\mathrm{coll}}_{0,2}(\Theta_A)$
  is the binary genus-$0$ shadow of the full MC element. For
  $K3 \times E$, this is the Maulik--Okounkov $R$-matrix
- $R^{\mathrm{MO}}(z)$ of Section~\ref{sec:mo-r-matrix},
+ $R^{\mathrm{MO}}(z)$ of Section~\ref{sec:k3e-mo-rmatrix},
  acting on the BPS Fock space. The $R$-matrix controls the
  Yangian structure of the BKM superalgebra: $R^{\mathrm{MO}}(z)$
  satisfies the Yang--Baxter equation with spectral parameter
@@ -1068,7 +1068,7 @@
  moduli of sheaves.
 
  \item \emph{MC element} $\Theta_{K3 \times E}$. The bar-intrinsic
- construction (cf.\ Vol~I, Chapter~\ref{ch:holographic-datum-master})
+ construction (cf.\ Chapter~\ref{ch:cy-holographic-datum-master})
  gives $\Theta_A := D_A - d_0 \in \mathrm{MC}(\mathfrak{g}^{\mathrm{mod}}_{A})$.
  The projections yield: $\kappa_{\mathrm{ch}} = 3$ at degree~$2$
  (from $\kappa_{\mathrm{ch}}(K3) + \kappa_{\mathrm{ch}}(E) = 2 + 1$), the cubic
@@ -1094,7 +1094,7 @@
  is the wall-crossing divisor of Section~\ref{sec:k3e-wall-crossing};
  the monodromy around each wall is the Kontsevich--Soibelman
  gauge transformation of
- Theorem~\ref{thm:k3e-wall-crossing-mc}.
+ Theorem~\ref{thm:ks-mc-gauge}.
 
  \item \emph{Quantum group} $\mathcal{G}(K3 \times E)$.
  The quantum vertex chiral group of
@@ -1428,7 +1428,7 @@
 so the Maurer--Cartan obstruction tower terminates at depth~$2$:
 $S_3 = S_4 = 0$ forces all higher shadows to vanish by the
 Vol~I recursion
-(Theorem~\ref{thm:obstruction-recursion}).
+(Theorem~\ref{thm:riccati-algebraicity}).
 The exponent~$24$ in the bar Euler product equals
 $\dim H_{\mathrm{Muk}}^{\mathrm{ab}} = \dim H^*(S, \bC) = 24$:
 each energy level $n \geq 1$ contributes $24$ bosonic oscillators
@@ -1441,7 +1441,7 @@
 \label{rem:k3-heisenberg-leech}
 The bar Euler product~\eqref{eq:k3-heisenberg-bar-euler} agrees with
 that of the Leech lattice VOA $V_{\Lambda_{24}}$ of rank~$24$
-(see Theorem~\ref{thm:denom-bar-euler}).
+(see Theorem~\ref{thm:lattice-voa-bar}).
 Both produce $\eta(q)^{24}/q = \Delta(q)/q^2$.
 This agreement is a consequence of rank universality: the
 energy-graded bar Euler product of any rank-$r$ lattice VOA or
@@ -1585,8 +1585,7 @@
 At $\sigma_3 = 0$, the Omega-background is trivial and the
 topological $E_3$-factorization algebra reduces to a free (abelian)
 factorization algebra. The classical fields are sections of
-the Lie conformal algebra $\frakL_S$ of
-Example~\ref{ex:k3-step1}: the current algebra of
+the Lie conformal algebra $\frakL_S$: the current algebra of
 $\HH^*(\cC)$ with the Gerstenhaber bracket set to zero
 (class~G, free-field approximation).
 

codex
The local reread is coherent. I’m now running two falsifiers: a direct missing-label scan over `main.tex + chapters + appendices`, and a grep to ensure the stale labels are gone from the modified file.
exec
/bin/zsh -lc "rg -n 'ch:holographic-datum-master|sec:mo-r-matrix|thm:k3e-wall-crossing-mc|thm:obstruction-recursion|thm:denom-bar-euler|ex:k3-step1' chapters/examples/k3_times_e.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "python3 - <<'PY'
import re, pathlib
roots = [pathlib.Path('main.tex'), pathlib.Path('chapters'), pathlib.Path('appendices')]
label_re = re.compile(r'\\\\label\\{(["'^}]+)'"\\}')
ref_re = re.compile(r'\\\\(?:ref|eqref|autoref|cref|Cref|pageref|nameref|vref|Vref)\\{(["'^}]+)'"\\}')
files = []
for root in roots:
    if root.is_file():
        files.append(root)
    else:
        files.extend(sorted(root.rglob('*.tex')))
labels = {}
for p in files:
    text = p.read_text()
    for m in label_re.finditer(text):
        labels.setdefault(m.group(1), []).append(str(p))
refs = {}
for p in files:
    text = p.read_text()
    for m in ref_re.finditer(text):
        for key in [s.strip() for s in m.group(1).split(',')]:
            if key:
                refs.setdefault(key, []).append(str(p))
missing = sorted(k for k in refs if k not in labels)
print('MISSING', len(missing))
for k in missing:
    print(k, '::', ', '.join(refs[k][:8]))
PY" in /Users/raeez/calabi-yau-quantum-groups exited 1 in 51ms:

 succeeded in 51ms:
MISSING 0
file update:
diff --git a/chapters/examples/k3_times_e.tex b/chapters/examples/k3_times_e.tex
index bee9416b63e4a821b9403dbf1aecac2dc101b7dd..071fdbb01c23e43e1db7a272d12e2aa17215906e
--- a/chapters/examples/k3_times_e.tex
+++ b/chapters/examples/k3_times_e.tex
@@ -1023,7 +1023,7 @@
 \section{The $K3 \times E$ holographic datum $H(K3 \times E)$}
 \label{sec:k3e-holographic-datum}
 
-The seven-face programme of Chapter~\ref{ch:holographic-datum-master}
+The seven-face programme of Chapter~\ref{ch:cy-holographic-datum-master}
 assigns to each CY3 geometry a holographic modular Koszul datum
 $H(X) = (A_X, A_X^!, r_X(z), \Theta_X, \kappa_{\mathrm{ch},X}, \nabla^{\mathrm{hol}}_X, \mathcal{G}_X)$
 packaging boundary algebra, Koszul dual, $R$-matrix, MC element,
@@ -1059,7 +1059,7 @@
  residue $r(z) = \operatorname{Res}^{\mathrm{coll}}_{0,2}(\Theta_A)$
  is the binary genus-$0$ shadow of the full MC element. For
  $K3 \times E$, this is the Maulik--Okounkov $R$-matrix
- $R^{\mathrm{MO}}(z)$ of Section~\ref{sec:mo-r-matrix},
+ $R^{\mathrm{MO}}(z)$ of Section~\ref{sec:k3e-mo-rmatrix},
  acting on the BPS Fock space. The $R$-matrix controls the
  Yangian structure of the BKM superalgebra: $R^{\mathrm{MO}}(z)$
  satisfies the Yang--Baxter equation with spectral parameter
@@ -1068,7 +1068,7 @@
  moduli of sheaves.
 
  \item \emph{MC element} $\Theta_{K3 \times E}$. The bar-intrinsic
- construction (cf.\ Vol~I, Chapter~\ref{ch:holographic-datum-master})
+ construction (cf.\ Chapter~\ref{ch:cy-holographic-datum-master})
  gives $\Theta_A := D_A - d_0 \in \mathrm{MC}(\mathfrak{g}^{\mathrm{mod}}_{A})$.
  The projections yield: $\kappa_{\mathrm{ch}} = 3$ at degree~$2$
  (from $\kappa_{\mathrm{ch}}(K3) + \kappa_{\mathrm{ch}}(E) = 2 + 1$), the cubic
@@ -1094,7 +1094,7 @@
  is the wall-crossing divisor of Section~\ref{sec:k3e-wall-crossing};
  the monodromy around each wall is the Kontsevich--Soibelman
  gauge transformation of
- Theorem~\ref{thm:k3e-wall-crossing-mc}.
+ Theorem~\ref{thm:ks-mc-gauge}.
 
  \item \emph{Quantum group} $\mathcal{G}(K3 \times E)$.
  The quantum vertex chiral group of
@@ -1428,7 +1428,7 @@
 so the Maurer--Cartan obstruction tower terminates at depth~$2$:
 $S_3 = S_4 = 0$ forces all higher shadows to vanish by the
 Vol~I recursion
-(Theorem~\ref{thm:obstruction-recursion}).
+(Theorem~\ref{thm:riccati-algebraicity}).
 The exponent~$24$ in the bar Euler product equals
 $\dim H_{\mathrm{Muk}}^{\mathrm{ab}} = \dim H^*(S, \bC) = 24$:
 each energy level $n \geq 1$ contributes $24$ bosonic oscillators
@@ -1441,7 +1441,7 @@
 \label{rem:k3-heisenberg-leech}
 The bar Euler product~\eqref{eq:k3-heisenberg-bar-euler} agrees with
 that of the Leech lattice VOA $V_{\Lambda_{24}}$ of rank~$24$
-(see Theorem~\ref{thm:denom-bar-euler}).
+(see Theorem~\ref{thm:lattice-voa-bar}).
 Both produce $\eta(q)^{24}/q = \Delta(q)/q^2$.
 This agreement is a consequence of rank universality: the
 energy-graded bar Euler product of any rank-$r$ lattice VOA or
@@ -1585,8 +1585,7 @@
 At $\sigma_3 = 0$, the Omega-background is trivial and the
 topological $E_3$-factorization algebra reduces to a free (abelian)
 factorization algebra. The classical fields are sections of
-the Lie conformal algebra $\frakL_S$ of
-Example~\ref{ex:k3-step1}: the current algebra of
+the Lie conformal algebra $\frakL_S$: the current algebra of
 $\HH^*(\cC)$ with the Gerstenhaber bracket set to zero
 (class~G, free-field approximation).
 


thinking
**Considering the build process**

I need to run a build to ensure there are no undefined references, especially since the user asked me to check each reference. The static missing-label check shows everything is fine, but the build might still be stale due to multi-pass issues. I should run `make fast` or at least look through `main.log`. It’s possible that one changed file isn’t updated. I’ll need to inspect the Makefile and then proceed with `make fast`. I'll also run `pkill` beforehand to clear any background processes.
codex
The label graph is clean now. I’m running the manuscript falsifier next so this isn’t just a static grep pass: a fresh fast build after clearing any stray TeX processes.
exec
/bin/zsh -lc 'pkill -9 -f pdflatex' in /Users/raeez/calabi-yau-quantum-groups exited 3 in 52ms:
sysmon request failed with error: sysmond service not found
pkill: Cannot get process list
file update:
diff --git a/chapters/examples/k3_times_e.tex b/chapters/examples/k3_times_e.tex
index bee9416b63e4a821b9403dbf1aecac2dc101b7dd..071fdbb01c23e43e1db7a272d12e2aa17215906e
--- a/chapters/examples/k3_times_e.tex
+++ b/chapters/examples/k3_times_e.tex
@@ -1023,7 +1023,7 @@
 \section{The $K3 \times E$ holographic datum $H(K3 \times E)$}
 \label{sec:k3e-holographic-datum}
 
-The seven-face programme of Chapter~\ref{ch:holographic-datum-master}
+The seven-face programme of Chapter~\ref{ch:cy-holographic-datum-master}
 assigns to each CY3 geometry a holographic modular Koszul datum
 $H(X) = (A_X, A_X^!, r_X(z), \Theta_X, \kappa_{\mathrm{ch},X}, \nabla^{\mathrm{hol}}_X, \mathcal{G}_X)$
 packaging boundary algebra, Koszul dual, $R$-matrix, MC element,
@@ -1059,7 +1059,7 @@
  residue $r(z) = \operatorname{Res}^{\mathrm{coll}}_{0,2}(\Theta_A)$
  is the binary genus-$0$ shadow of the full MC element. For
  $K3 \times E$, this is the Maulik--Okounkov $R$-matrix
- $R^{\mathrm{MO}}(z)$ of Section~\ref{sec:mo-r-matrix},
+ $R^{\mathrm{MO}}(z)$ of Section~\ref{sec:k3e-mo-rmatrix},
  acting on the BPS Fock space. The $R$-matrix controls the
  Yangian structure of the BKM superalgebra: $R^{\mathrm{MO}}(z)$
  satisfies the Yang--Baxter equation with spectral parameter
@@ -1068,7 +1068,7 @@
  moduli of sheaves.
 
  \item \emph{MC element} $\Theta_{K3 \times E}$. The bar-intrinsic
- construction (cf.\ Vol~I, Chapter~\ref{ch:holographic-datum-master})
+ construction (cf.\ Chapter~\ref{ch:cy-holographic-datum-master})
  gives $\Theta_A := D_A - d_0 \in \mathrm{MC}(\mathfrak{g}^{\mathrm{mod}}_{A})$.
  The projections yield: $\kappa_{\mathrm{ch}} = 3$ at degree~$2$
  (from $\kappa_{\mathrm{ch}}(K3) + \kappa_{\mathrm{ch}}(E) = 2 + 1$), the cubic
@@ -1094,7 +1094,7 @@
  is the wall-crossing divisor of Section~\ref{sec:k3e-wall-crossing};
  the monodromy around each wall is the Kontsevich--Soibelman
  gauge transformation of
- Theorem~\ref{thm:k3e-wall-crossing-mc}.
+ Theorem~\ref{thm:ks-mc-gauge}.
 
  \item \emph{Quantum group} $\mathcal{G}(K3 \times E)$.
  The quantum vertex chiral group of
@@ -1428,7 +1428,7 @@
 so the Maurer--Cartan obstruction tower terminates at depth~$2$:
 $S_3 = S_4 = 0$ forces all higher shadows to vanish by the
 Vol~I recursion
-(Theorem~\ref{thm:obstruction-recursion}).
+(Theorem~\ref{thm:riccati-algebraicity}).
 The exponent~$24$ in the bar Euler product equals
 $\dim H_{\mathrm{Muk}}^{\mathrm{ab}} = \dim H^*(S, \bC) = 24$:
 each energy level $n \geq 1$ contributes $24$ bosonic oscillators
@@ -1441,7 +1441,7 @@
 \label{rem:k3-heisenberg-leech}
 The bar Euler product~\eqref{eq:k3-heisenberg-bar-euler} agrees with
 that of the Leech lattice VOA $V_{\Lambda_{24}}$ of rank~$24$
-(see Theorem~\ref{thm:denom-bar-euler}).
+(see Theorem~\ref{thm:lattice-voa-bar}).
 Both produce $\eta(q)^{24}/q = \Delta(q)/q^2$.
 This agreement is a consequence of rank universality: the
 energy-graded bar Euler product of any rank-$r$ lattice VOA or
@@ -1585,8 +1585,7 @@
 At $\sigma_3 = 0$, the Omega-background is trivial and the
 topological $E_3$-factorization algebra reduces to a free (abelian)
 factorization algebra. The classical fields are sections of
-the Lie conformal algebra $\frakL_S$ of
-Example~\ref{ex:k3-step1}: the current algebra of
+the Lie conformal algebra $\frakL_S$: the current algebra of
 $\HH^*(\cC)$ with the Gerstenhaber bracket set to zero
 (class~G, free-field approximation).
 


thinking
**Addressing execution issues**

I had an issue with the process because it got blocked by the sandbox. I should mention that. Now, I need to focus on trying to run the command "make fast" to move forward. It seems like there's a clear next step here, so I'll get that sorted out quickly. I wonder if there'll be any other issues to tackle.
codex
Process cleanup isn’t available in this sandbox, so I’m proceeding directly to the fast build and treating the build result itself as the decisive check.
exec
/bin/zsh -lc 'make fast' in /Users/raeez/calabi-yau-quantum-groupsfile update:
diff --git a/chapters/examples/k3_times_e.tex b/chapters/examples/k3_times_e.tex
index bee9416b63e4a821b9403dbf1aecac2dc101b7dd..071fdbb01c23e43e1db7a272d12e2aa17215906e
--- a/chapters/examples/k3_times_e.tex
+++ b/chapters/examples/k3_times_e.tex
@@ -1023,7 +1023,7 @@
 \section{The $K3 \times E$ holographic datum $H(K3 \times E)$}
 \label{sec:k3e-holographic-datum}
 
-The seven-face programme of Chapter~\ref{ch:holographic-datum-master}
+The seven-face programme of Chapter~\ref{ch:cy-holographic-datum-master}
 assigns to each CY3 geometry a holographic modular Koszul datum
 $H(X) = (A_X, A_X^!, r_X(z), \Theta_X, \kappa_{\mathrm{ch},X}, \nabla^{\mathrm{hol}}_X, \mathcal{G}_X)$
 packaging boundary algebra, Koszul dual, $R$-matrix, MC element,
@@ -1059,7 +1059,7 @@
  residue $r(z) = \operatorname{Res}^{\mathrm{coll}}_{0,2}(\Theta_A)$
  is the binary genus-$0$ shadow of the full MC element. For
  $K3 \times E$, this is the Maulik--Okounkov $R$-matrix
- $R^{\mathrm{MO}}(z)$ of Section~\ref{sec:mo-r-matrix},
+ $R^{\mathrm{MO}}(z)$ of Section~\ref{sec:k3e-mo-rmatrix},
  acting on the BPS Fock space. The $R$-matrix controls the
  Yangian structure of the BKM superalgebra: $R^{\mathrm{MO}}(z)$
  satisfies the Yang--Baxter equation with spectral parameter
@@ -1068,7 +1068,7 @@
  moduli of sheaves.
 
  \item \emph{MC element} $\Theta_{K3 \times E}$. The bar-intrinsic
- construction (cf.\ Vol~I, Chapter~\ref{ch:holographic-datum-master})
+ construction (cf.\ Chapter~\ref{ch:cy-holographic-datum-master})
  gives $\Theta_A := D_A - d_0 \in \mathrm{MC}(\mathfrak{g}^{\mathrm{mod}}_{A})$.
  The projections yield: $\kappa_{\mathrm{ch}} = 3$ at degree~$2$
  (from $\kappa_{\mathrm{ch}}(K3) + \kappa_{\mathrm{ch}}(E) = 2 + 1$), the cubic
@@ -1094,7 +1094,7 @@
  is the wall-crossing divisor of Section~\ref{sec:k3e-wall-crossing};
  the monodromy around each wall is the Kontsevich--Soibelman
  gauge transformation of
- Theorem~\ref{thm:k3e-wall-crossing-mc}.
+ Theorem~\ref{thm:ks-mc-gauge}.
 
  \item \emph{Quantum group} $\mathcal{G}(K3 \times E)$.
  The quantum vertex chiral group of
@@ -1428,7 +1428,7 @@
 so the Maurer--Cartan obstruction tower terminates at depth~$2$:
 $S_3 = S_4 = 0$ forces all higher shadows to vanish by the
 Vol~I recursion
-(Theorem~\ref{thm:obstruction-recursion}).
+(Theorem~\ref{thm:riccati-algebraicity}).
 The exponent~$24$ in the bar Euler product equals
 $\dim H_{\mathrm{Muk}}^{\mathrm{ab}} = \dim H^*(S, \bC) = 24$:
 each energy level $n \geq 1$ contributes $24$ bosonic oscillators
@@ -1441,7 +1441,7 @@
 \label{rem:k3-heisenberg-leech}
 The bar Euler product~\eqref{eq:k3-heisenberg-bar-euler} agrees with
 that of the Leech lattice VOA $V_{\Lambda_{24}}$ of rank~$24$
-(see Theorem~\ref{thm:denom-bar-euler}).
+(see Theorem~\ref{thm:lattice-voa-bar}).
 Both produce $\eta(q)^{24}/q = \Delta(q)/q^2$.
 This agreement is a consequence of rank universality: the
 energy-graded bar Euler product of any rank-$r$ lattice VOA or
@@ -1585,8 +1585,7 @@
 At $\sigma_3 = 0$, the Omega-background is trivial and the
 topological $E_3$-factorization algebra reduces to a free (abelian)
 factorization algebra. The classical fields are sections of
-the Lie conformal algebra $\frakL_S$ of
-Example~\ref{ex:k3-step1}: the current algebra of
+the Lie conformal algebra $\frakL_S$: the current algebra of
 $\HH^*(\cC)$ with the Gerstenhaber bracket set to zero
 (class~G, free-field approximation).
 

file update:
diff --git a/chapters/examples/k3_times_e.tex b/chapters/examples/k3_times_e.tex
index bee9416b63e4a821b9403dbf1aecac2dc101b7dd..071fdbb01c23e43e1db7a272d12e2aa17215906e
--- a/chapters/examples/k3_times_e.tex
+++ b/chapters/examples/k3_times_e.tex
@@ -1023,7 +1023,7 @@
 \section{The $K3 \times E$ holographic datum $H(K3 \times E)$}
 \label{sec:k3e-holographic-datum}
 
-The seven-face programme of Chapter~\ref{ch:holographic-datum-master}
+The seven-face programme of Chapter~\ref{ch:cy-holographic-datum-master}
 assigns to each CY3 geometry a holographic modular Koszul datum
 $H(X) = (A_X, A_X^!, r_X(z), \Theta_X, \kappa_{\mathrm{ch},X}, \nabla^{\mathrm{hol}}_X, \mathcal{G}_X)$
 packaging boundary algebra, Koszul dual, $R$-matrix, MC element,
@@ -1059,7 +1059,7 @@
  residue $r(z) = \operatorname{Res}^{\mathrm{coll}}_{0,2}(\Theta_A)$
  is the binary genus-$0$ shadow of the full MC element. For
  $K3 \times E$, this is the Maulik--Okounkov $R$-matrix
- $R^{\mathrm{MO}}(z)$ of Section~\ref{sec:mo-r-matrix},
+ $R^{\mathrm{MO}}(z)$ of Section~\ref{sec:k3e-mo-rmatrix},
  acting on the BPS Fock space. The $R$-matrix controls the
  Yangian structure of the BKM superalgebra: $R^{\mathrm{MO}}(z)$
  satisfies the Yang--Baxter equation with spectral parameter
@@ -1068,7 +1068,7 @@
  moduli of sheaves.
 
  \item \emph{MC element} $\Theta_{K3 \times E}$. The bar-intrinsic
- construction (cf.\ Vol~I, Chapter~\ref{ch:holographic-datum-master})
+ construction (cf.\ Chapter~\ref{ch:cy-holographic-datum-master})
  gives $\Theta_A := D_A - d_0 \in \mathrm{MC}(\mathfrak{g}^{\mathrm{mod}}_{A})$.
  The projections yield: $\kappa_{\mathrm{ch}} = 3$ at degree~$2$
  (from $\kappa_{\mathrm{ch}}(K3) + \kappa_{\mathrm{ch}}(E) = 2 + 1$), the cubic
@@ -1094,7 +1094,7 @@
  is the wall-crossing divisor of Section~\ref{sec:k3e-wall-crossing};
  the monodromy around each wall is the Kontsevich--Soibelman
  gauge transformation of
- Theorem~\ref{thm:k3e-wall-crossing-mc}.
+ Theorem~\ref{thm:ks-mc-gauge}.
 
  \item \emph{Quantum group} $\mathcal{G}(K3 \times E)$.
  The quantum vertex chiral group of
@@ -1428,7 +1428,7 @@
 so the Maurer--Cartan obstruction tower terminates at depth~$2$:
 $S_3 = S_4 = 0$ forces all higher shadows to vanish by the
 Vol~I recursion
-(Theorem~\ref{thm:obstruction-recursion}).
+(Theorem~\ref{thm:riccati-algebraicity}).
 The exponent~$24$ in the bar Euler product equals
 $\dim H_{\mathrm{Muk}}^{\mathrm{ab}} = \dim H^*(S, \bC) = 24$:
 each energy level $n \geq 1$ contributes $24$ bosonic oscillators
@@ -1441,7 +1441,7 @@
 \label{rem:k3-heisenberg-leech}
 The bar Euler product~\eqref{eq:k3-heisenberg-bar-euler} agrees with
 that of the Leech lattice VOA $V_{\Lambda_{24}}$ of rank~$24$
-(see Theorem~\ref{thm:denom-bar-euler}).
+(see Theorem~\ref{thm:lattice-voa-bar}).
 Both produce $\eta(q)^{24}/q = \Delta(q)/q^2$.
 This agreement is a consequence of rank universality: the
 energy-graded bar Euler product of any rank-$r$ lattice VOA or
@@ -1585,8 +1585,7 @@
 At $\sigma_3 = 0$, the Omega-background is trivial and the
 topological $E_3$-factorization algebra reduces to a free (abelian)
 factorization algebra. The classical fields are sections of
-the Lie conformal algebra $\frakL_S$ of
-Example~\ref{ex:k3-step1}: the current algebra of
+the Lie conformal algebra $\frakL_S$: the current algebra of
 $\HH^*(\cC)$ with the Gerstenhaber bracket set to zero
 (class~G, free-field approximation).
 

 succeeded in 11.42s:
Creating build dir: /tmp/mkd-calabi-yau-quantum-groups-20260413184836-99597
Building main.tex (up to 4 passes) [NS=20260413184836-99597]
── Pass 1 / 4 ──
   371pp, 0 undef citations, 0 undef references, 2 rerun requests, 24 overfull, 52 underfull
── Pass 2 / 4 ──
   371pp, 0 undef citations, 0 undef references, 0 rerun requests, 24 overfull, 52 underfull
✓ Converged after 2 passes.
     Logs: .build_logs/tex-build.stdout.log and main.log
file update:
diff --git a/chapters/examples/k3_times_e.tex b/chapters/examples/k3_times_e.tex
index bee9416b63e4a821b9403dbf1aecac2dc101b7dd..071fdbb01c23e43e1db7a272d12e2aa17215906e
--- a/chapters/examples/k3_times_e.tex
+++ b/chapters/examples/k3_times_e.tex
@@ -1023,7 +1023,7 @@
 \section{The $K3 \times E$ holographic datum $H(K3 \times E)$}
 \label{sec:k3e-holographic-datum}
 
-The seven-face programme of Chapter~\ref{ch:holographic-datum-master}
+The seven-face programme of Chapter~\ref{ch:cy-holographic-datum-master}
 assigns to each CY3 geometry a holographic modular Koszul datum
 $H(X) = (A_X, A_X^!, r_X(z), \Theta_X, \kappa_{\mathrm{ch},X}, \nabla^{\mathrm{hol}}_X, \mathcal{G}_X)$
 packaging boundary algebra, Koszul dual, $R$-matrix, MC element,
@@ -1059,7 +1059,7 @@
  residue $r(z) = \operatorname{Res}^{\mathrm{coll}}_{0,2}(\Theta_A)$
  is the binary genus-$0$ shadow of the full MC element. For
  $K3 \times E$, this is the Maulik--Okounkov $R$-matrix
- $R^{\mathrm{MO}}(z)$ of Section~\ref{sec:mo-r-matrix},
+ $R^{\mathrm{MO}}(z)$ of Section~\ref{sec:k3e-mo-rmatrix},
  acting on the BPS Fock space. The $R$-matrix controls the
  Yangian structure of the BKM superalgebra: $R^{\mathrm{MO}}(z)$
  satisfies the Yang--Baxter equation with spectral parameter
@@ -1068,7 +1068,7 @@
  moduli of sheaves.
 
  \item \emph{MC element} $\Theta_{K3 \times E}$. The bar-intrinsic
- construction (cf.\ Vol~I, Chapter~\ref{ch:holographic-datum-master})
+ construction (cf.\ Chapter~\ref{ch:cy-holographic-datum-master})
  gives $\Theta_A := D_A - d_0 \in \mathrm{MC}(\mathfrak{g}^{\mathrm{mod}}_{A})$.
  The projections yield: $\kappa_{\mathrm{ch}} = 3$ at degree~$2$
  (from $\kappa_{\mathrm{ch}}(K3) + \kappa_{\mathrm{ch}}(E) = 2 + 1$), the cubic
@@ -1094,7 +1094,7 @@
  is the wall-crossing divisor of Section~\ref{sec:k3e-wall-crossing};
  the monodromy around each wall is the Kontsevich--Soibelman
  gauge transformation of
- Theorem~\ref{thm:k3e-wall-crossing-mc}.
+ Theorem~\ref{thm:ks-mc-gauge}.
 
  \item \emph{Quantum group} $\mathcal{G}(K3 \times E)$.
  The quantum vertex chiral group of
@@ -1428,7 +1428,7 @@
 so the Maurer--Cartan obstruction tower terminates at depth~$2$:
 $S_3 = S_4 = 0$ forces all higher shadows to vanish by the
 Vol~I recursion
-(Theorem~\ref{thm:obstruction-recursion}).
+(Theorem~\ref{thm:riccati-algebraicity}).
 The exponent~$24$ in the bar Euler product equals
 $\dim H_{\mathrm{Muk}}^{\mathrm{ab}} = \dim H^*(S, \bC) = 24$:
 each energy level $n \geq 1$ contributes $24$ bosonic oscillators
@@ -1441,7 +1441,7 @@
 \label{rem:k3-heisenberg-leech}
 The bar Euler product~\eqref{eq:k3-heisenberg-bar-euler} agrees with
 that of the Leech lattice VOA $V_{\Lambda_{24}}$ of rank~$24$
-(see Theorem~\ref{thm:denom-bar-euler}).
+(see Theorem~\ref{thm:lattice-voa-bar}).
 Both produce $\eta(q)^{24}/q = \Delta(q)/q^2$.
 This agreement is a consequence of rank universality: the
 energy-graded bar Euler product of any rank-$r$ lattice VOA or
@@ -1585,8 +1585,7 @@
 At $\sigma_3 = 0$, the Omega-background is trivial and the
 topological $E_3$-factorization algebra reduces to a free (abelian)
 factorization algebra. The classical fields are sections of
-the Lie conformal algebra $\frakL_S$ of
-Example~\ref{ex:k3-step1}: the current algebra of
+the Lie conformal algebra $\frakL_S$: the current algebra of
 $\HH^*(\cC)$ with the Gerstenhaber bracket set to zero
 (class~G, free-field approximation).
 





thinking
**Summarizing build status**

I need to provide a concise list of broken references along with their statuses. I should mention that the static scan indicates "MISSING 0," and "make fast" converged after two passes with no undefined references. It might be useful to include a file link, specifically for the modified file. Interestingly, `grep` for old labels returned no matches, and while `pkill` wasn't available, the build still succeeded with no blockers. Maybe I should note "FIXED" statuses individually.
thinking
**Addressing stale labels**

I need to address the stale labels in my report. There's a specific case: `ch:holographic-datum-master` has been changed to `ch:cy-holographic-datum-master`, with two occurrences. I might be wondering if I should count them as one finding since they're the same issue, but it's probably best to state that both occurrences have been fixed. That keeps things clear for anyone reviewing the changes.
thinking
**Organizing report structure**

I need to mention "MISSING 0" from the static label scan across `main.tex`, chapters, and appendices. The `make fast` command converged after two passes with zero undefined references, which is a good sign. 

I’m thinking of structuring the final report with a short paragraph detailing file changes and outcomes, followed by a flat list of fixed statuses. For verification, I want to keep things concise, perhaps creating two sections titled "**Status**" and "**Verification**", ensuring no nested bullets. I should avoid starting with "Done."
thinking
**Considering audit findings**

I should only list the actual broken references. I think it’s worth mentioning that the part or appendix candidates flagged were just false positives from the chapter-only label scan, so no fix is required. However, I don't have the actual findings list from the audit handy. It would make sense to list only the ones that have been fixed. Do I need to mention the build logs path? Probably not, but I’ll keep the response concise.
codex
Updated [chapters/examples/k3_times_e.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3_times_e.tex).

- `FIXED` `ch:holographic-datum-master` at both broken sites by retargeting to `ch:cy-holographic-datum-master`.
- `FIXED` `sec:mo-r-matrix` by retargeting it to `sec:k3e-mo-rmatrix`.
- `FIXED` `thm:k3e-wall-crossing-mc` by retargeting it to the live MC-gauge theorem `thm:ks-mc-gauge`.
- `FIXED` `thm:obstruction-recursion` by retargeting it to the live Vol I stub label `thm:riccati-algebraicity`.
- `FIXED` `thm:denom-bar-euler` by retargeting it to the live Vol I stub label `thm:lattice-voa-bar`.
- `FIXED` `ex:k3-step1` by removing the dead note-only reference and inlining the sentence’s actual content.

Verification passed:
- Static label scan over `main.tex`, `chapters/`, and `appendices/`: `MISSING 0`.
- Grep for the stale labels in the modified file: no matches.
- `make fast`: converged after 2 passes with `0 undef references` and `0 undef citations`.

No blockers.
file update:
diff --git a/chapters/examples/k3_times_e.tex b/chapters/examples/k3_times_e.tex
index bee9416b63e4a821b9403dbf1aecac2dc101b7dd..071fdbb01c23e43e1db7a272d12e2aa17215906e
--- a/chapters/examples/k3_times_e.tex
+++ b/chapters/examples/k3_times_e.tex
@@ -1023,7 +1023,7 @@
 \section{The $K3 \times E$ holographic datum $H(K3 \times E)$}
 \label{sec:k3e-holographic-datum}
 
-The seven-face programme of Chapter~\ref{ch:holographic-datum-master}
+The seven-face programme of Chapter~\ref{ch:cy-holographic-datum-master}
 assigns to each CY3 geometry a holographic modular Koszul datum
 $H(X) = (A_X, A_X^!, r_X(z), \Theta_X, \kappa_{\mathrm{ch},X}, \nabla^{\mathrm{hol}}_X, \mathcal{G}_X)$
 packaging boundary algebra, Koszul dual, $R$-matrix, MC element,
@@ -1059,7 +1059,7 @@
  residue $r(z) = \operatorname{Res}^{\mathrm{coll}}_{0,2}(\Theta_A)$
  is the binary genus-$0$ shadow of the full MC element. For
  $K3 \times E$, this is the Maulik--Okounkov $R$-matrix
- $R^{\mathrm{MO}}(z)$ of Section~\ref{sec:mo-r-matrix},
+ $R^{\mathrm{MO}}(z)$ of Section~\ref{sec:k3e-mo-rmatrix},
  acting on the BPS Fock space. The $R$-matrix controls the
  Yangian structure of the BKM superalgebra: $R^{\mathrm{MO}}(z)$
  satisfies the Yang--Baxter equation with spectral parameter
@@ -1068,7 +1068,7 @@
  moduli of sheaves.
 
  \item \emph{MC element} $\Theta_{K3 \times E}$. The bar-intrinsic
- construction (cf.\ Vol~I, Chapter~\ref{ch:holographic-datum-master})
+ construction (cf.\ Chapter~\ref{ch:cy-holographic-datum-master})
  gives $\Theta_A := D_A - d_0 \in \mathrm{MC}(\mathfrak{g}^{\mathrm{mod}}_{A})$.
  The projections yield: $\kappa_{\mathrm{ch}} = 3$ at degree~$2$
  (from $\kappa_{\mathrm{ch}}(K3) + \kappa_{\mathrm{ch}}(E) = 2 + 1$), the cubic
@@ -1094,7 +1094,7 @@
  is the wall-crossing divisor of Section~\ref{sec:k3e-wall-crossing};
  the monodromy around each wall is the Kontsevich--Soibelman
  gauge transformation of
- Theorem~\ref{thm:k3e-wall-crossing-mc}.
+ Theorem~\ref{thm:ks-mc-gauge}.
 
  \item \emph{Quantum group} $\mathcal{G}(K3 \times E)$.
  The quantum vertex chiral group of
@@ -1428,7 +1428,7 @@
 so the Maurer--Cartan obstruction tower terminates at depth~$2$:
 $S_3 = S_4 = 0$ forces all higher shadows to vanish by the
 Vol~I recursion
-(Theorem~\ref{thm:obstruction-recursion}).
+(Theorem~\ref{thm:riccati-algebraicity}).
 The exponent~$24$ in the bar Euler product equals
 $\dim H_{\mathrm{Muk}}^{\mathrm{ab}} = \dim H^*(S, \bC) = 24$:
 each energy level $n \geq 1$ contributes $24$ bosonic oscillators
@@ -1441,7 +1441,7 @@
 \label{rem:k3-heisenberg-leech}
 The bar Euler product~\eqref{eq:k3-heisenberg-bar-euler} agrees with
 that of the Leech lattice VOA $V_{\Lambda_{24}}$ of rank~$24$
-(see Theorem~\ref{thm:denom-bar-euler}).
+(see Theorem~\ref{thm:lattice-voa-bar}).
 Both produce $\eta(q)^{24}/q = \Delta(q)/q^2$.
 This agreement is a consequence of rank universality: the
 energy-graded bar Euler product of any rank-$r$ lattice VOA or
@@ -1585,8 +1585,7 @@
 At $\sigma_3 = 0$, the Omega-background is trivial and the
 topological $E_3$-factorization algebra reduces to a free (abelian)
 factorization algebra. The classical fields are sections of
-the Lie conformal algebra $\frakL_S$ of
-Example~\ref{ex:k3-step1}: the current algebra of
+the Lie conformal algebra $\frakL_S$: the current algebra of
 $\HH^*(\cC)$ with the Gerstenhaber bracket set to zero
 (class~G, free-field approximation).
 

tokens used
104,119
