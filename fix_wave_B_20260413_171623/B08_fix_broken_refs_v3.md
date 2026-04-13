# B08_fix_broken_refs_v3 (805s)

All broken Vol III references that were surfacing in `main.log` are fixed. `make fast` now completes 4 passes with `0 undef refs` and `6 undef cites` remaining. I also grepped the edited files for the exact old broken `\ref{...}` patterns; there were no matches.

Per finding:
- `thm:miura-cross-universality` FIXED by retargeting the preface to `prop:universal-coproduct`.
- `sec:e1-chiral-bialgebra` FIXED by correcting the stale singular label to `sec:e1-chiral-bialgebras`.
- `sec:analytic-sewing` FIXED by replacing both impossible cross-volume refs with plain Vol I prose.
- `def:k3-double-current-algebra` FIXED by removing all stale `Definition~\ref{...}` calls after the K3 material was merged; the text now names the object directly.
- `prop:e1-descent-unobstructed` FIXED by retargeting to the live toric descent theorem `thm:toric-chart-gluing`.
- `sec:working-notes` FIXED by removing the dead cross-document section ref and using plain prose.
- `ch:k3` FIXED by retargeting to `ch:k3-times-e`.
- `ch:coha` FIXED by retargeting to `ch:toric-coha`.
- `thm:topologization` FIXED by replacing the dead Vol I label ref with plain theorem prose.
- `ch:cy-chiral-functor` FIXED by retargeting both occurrences to `ch:cy-to-chiral`.
- `ch:cha-yangian` FIXED by retargeting to `ch:toric-coha`.
- `sec:k3-perturbative-fact-homology` FIXED by retargeting to `subsec:fact-homology-k3xe`.
- `part:e1-core` FIXED by replacing the dead part ref with plain `Part I of \cite{VolII}` prose.
- `thm:htt-general` FIXED by replacing the dead theorem ref with plain HTT prose.
- `subsec:k3-three-algebraizations` FIXED by removing the stale merged-chapter subsection ref and using chapter-level prose.
- `thm:e1-stabilization` FIXED by retargeting to `thm:e1-stabilization-cy`.
- `thm:w-infty-chiral-qg` FIXED by retargeting to `prop:universal-coproduct`.
- `subsec:quantum-chiral-algebras-6d` FIXED by retargeting to `subsec:chiral-qg-wilson`.
- `rem:toric-structural-patterns` FIXED by retargeting to `rem:toric-kappa-patterns`.
- `thm:chiral-qg-equiv` FIXED by removing all three dead Vol I label refs and rewriting them as plain cross-volume prose.
- `ch:toroidal-elliptic` FIXED by correcting it to `chap:toroidal-elliptic`.
- `thm:cy-seven-face-master` FIXED by correcting the claim-state mismatch to `conj:cy-seven-face-master`.
- `part:3d-qg` FIXED by replacing the dead part ref with plain `Part III of Vol. II` prose.

Files changed were the 12 directly affected surfaces in `chapters/` and `chapters/frame/`. No blockers.


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
session id: 019d8772-b049-7c42-ba4f-aca976e6aabf
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
**Evaluating LaTeX Verification Tools**

I'm considering the task that revolves around LaTeX verification. I might explore using vol3-build-surface and assess if vol3-cross-volume-propagation is necessary, but I'm leaning towards the minimal approach. There's also the possibility of using vol3-beilinson-loop for rectification and convergence. However, the primary focus seems to be fixing broken references, which requires checking their validity. I need to inspect the skill file and update commentary accordingly, while using a commentary channel for clear updates.
codex
Using `vol3-build-surface` because this is a targeted manuscript verification/fix task around LaTeX reference integrity. I’m locking the modified surface first: current diff, the skill instructions, and the actual `\ref{}` usage/label surface before making any edits.
exec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/vol3-build-surface/SKILL.md" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "grep -rn '\\\\ref{' chapters/ | head -80" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc 'git status --short' in /Users/raeez/calabi-yau-quantum-groups succeeded in 50ms:
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
 succeeded in 51ms:
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
 succeeded in 51ms:


thinking
**Fixing broken references**

I need to fix all broken references and gather all refs and labels to find any missing ones. It seems there are many references to Theorem CY-A$_d$ that might not follow standard formatting. I’ll need to inspect all labels and potentially use shell commands, avoiding Python for file reading/writing. Gathering definitions may require running rg commands. I might collect undefined refs using `make fast`. Also, I need to check for labels with `rg -n "\\\\label\\{...`. I'll plan my next steps accordingly.
codex
I have the reference surface and the repo appears clean, so the next step is classification rather than editing. I’m checking the actual unresolved-label set from the live sources and a narrow Vol III build/log surface so I can make only the minimal fixes instead of touching every reference site.
exec
/bin/zsh -lc 'ls -1' in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n '"'^fast:|latexmk|pdflatex|xelatex|lualatex'"' Makefile makefile GNUmakefile -S" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n --no-heading '\\\\(label|bibitem)\\{' chapters main.tex" in /Users/raeez/calabi-yau-quantum-groups succeeded in 51ms:
AGENTS.md
CLAUDE.md
FRONTIER.md
Makefile
README.md
appendices
bibliography
calabi_yau_quantum_groups.pdf
chapters
compute
main.aux
main.log
main.out
main.pdf
main.tex
main.toc
notes
out
scripts
working_notes.aux
 exited 2 in 50ms:
rg: GNUmakefile: No such file or directory (os error 2)
makefile:20:TEX       := pdflatex
makefile:47:AUX_EXTS  := aux log out toc synctex.gz fdb_latexmk fls bbl blg \
makefile:81:fast:
Makefile:20:TEX       := pdflatex
Makefile:47:AUX_EXTS  := aux log out toc synctex.gz fdb_latexmk fls bbl blg \
Makefile:81:fast:
 succeeded in 51ms:
Total output lines: 1431

main.tex:416:\label{part:cy-categories}
main.tex:431:\label{part:bridge}
main.tex:452:\label{part:examples}
main.tex:467:\label{part:connections}
main.tex:478:\label{part:frontier}
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

thinking
**Inspecting unresolved references**

I need actual unresolved references to work with. I think using the command `make fast` might help, but before that, it seems like I should parse the .aux/labels file. I'm wondering if there are already unresolved references logged in main.log, so I’ll have to check for any undefined reference warnings. Let's see what I can uncover!
codex
I have the full label inventory. Now I’m classifying whether the broken references are true label drift or just stale aux/build noise by reading the current log and, if needed, rerunning the narrowest build target.
exec
/bin/zsh -lc "rg -n 'undefined|Reference|Citation|multiply defined' main.log out/main.log -S" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "sed -n '1,180p' Makefile" in /Users/raeez/calabi-yau-quantum-groups exited 2 in 51ms:
rg: out/main.log: No such file or directory (os error 2)
main.log:1639:LaTeX Warning: Reference `thm:miura-cross-universality' on page 6 undefined on 
main.log:1643:LaTeX Warning: Reference `sec:e1-chiral-bialgebra' on page 6 undefined on input
main.log:1905:LaTeX Warning: Reference `sec:analytic-sewing' on page 6 undefined on input lin
main.log:1934:LaTeX Warning: Reference `def:k3-double-current-algebra' on page 9 undefined on
main.log:1956:LaTeX Warning: Reference `prop:e1-descent-unobstructed' on page 11 undefined on
main.log:1963:LaTeX Warning: Reference `def:k3-double-current-algebra' on page 12 undefined o
main.log:1967:LaTeX Warning: Reference `sec:working-notes' on page 12 undefined on input line
main.log:2011:LaTeX Warning: Reference `ch:k3' on page 18 undefined on input line 169.
main.log:2028:LaTeX Warning: Reference `ch:coha' on page 18 undefined on input line 197.
main.log:2128:and I'll forget about whatever was undefined.
main.log:2137:and I'll forget about whatever was undefined.
main.log:2310:and I'll forget about whatever was undefined.
main.log:2322:LaTeX Warning: Reference `thm:topologization' on page 34 undefined on input lin
main.log:2354:LaTeX Warning: Reference `ch:cy-chiral-functor' on page 35 undefined on input l
main.log:2373:LaTeX Warning: Reference `ch:cha-yangian' on page 36 undefined on input line 15
main.log:2392:and I'll forget about whatever was undefined.
main.log:2403:and I'll forget about whatever was undefined.
main.log:2414:and I'll forget about whatever was undefined.
main.log:2433:LaTeX Warning: Citation `Li' on page 37 undefined on input line 236.
 succeeded in 51ms:
# ============================================================================
#  Makefile — Calabi-Yau Quantum Groups
# ============================================================================
#
#  Usage:
#    make               Full converging build → main.pdf
#    make fast           Quick build (up to 4 passes)
#    make clean          Remove LaTeX build artifacts
#    make veryclean      Remove artifacts AND compiled PDFs
#    make count          Line counts and page estimate
#    make check          Halt-on-error validation
#    make test           Run compute test suite
#    make help           Show available targets
#
# ============================================================================

# --- Configuration -----------------------------------------------------------

MAIN      := main
TEX       := pdflatex
codex
The current log has true undefined-reference warnings, but logs can still contain stale noise. I’m computing the exact missing label set directly from source now, which will let me fix only genuine label drift and ignore pass-order artifacts.
exec
/bin/zsh -lc "rg -n 'thm:miura-cross-universality|sec:e1-chiral-bialgebra|sec:analytic-sewing|def:k3-double-current-algebra|prop:e1-descent-unobstructed|sec:working-notes|ch:k3|ch:coha|thm:topologization|ch:cy-chiral-functor|ch:cha-yangian|sec:k3-perturbative-fact-homology|part:e1-core|thm:htt-general|subsec:k3-three-algebraizations|thm:e1-stabilization|thm:w-infty-chiral-qg|subsec:quantum-chiral-algebras-6d|rem:toric-structural-patterns|thm:chiral-qg-equiv|ch:toroidal-elliptic|thm:cy-seven-face-master|part:3d-qg' chapters main.tex -S" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "python3 - <<'PY'
import re, pathlib
root = pathlib.Path('.')
text_paths = list(root.glob('chapters/**/*.tex')) + [root/'main.tex']
label_re = re.compile(r'\\\\label\\{(["'^}]+)'"\\}')
ref_re = re.compile(r'\\\\(?:eq)?ref\\{(["'^}]+)'"\\}')
labels = {}
refs = {}
for path in text_paths:
    text = path.read_text()
    for i,line in enumerate(text.splitlines(),1):
        for m in label_re.finditer(line):
            labels.setdefault(m.group(1), []).append((str(path), i))
        for m in ref_re.finditer(line):
            refs.setdefault(m.group(1), []).append((str(path), i, line.strip()))
missing = sorted(k for k in refs if k not in labels)
print('MISSING', len(missing))
for k in missing:
    print(f'LABEL {k}')
    for path, i, line in refs[k][:5]:
        print(f'  REF {path}:{i}: {line}')
PY" in /Users/raeez/calabi-yau-quantum-groups succeeded in 52ms:
chapters/examples/quantum_group_reps.tex:506: formula (Chapter~\ref{ch:toroidal-elliptic}; distinct from
chapters/examples/toric_cy3_coha.tex:208:(i) The compact base $\bP^1 \times \bP^1$ has $\chi(\bP^1 \times \bP^1) = 4$ (each factor contributes $\chi(\bP^1) = 2$), so $\kappa_{\mathrm{ch}} = \chi/2 = 2$ by the general local-surface formula (Remark~\ref{rem:toric-structural-patterns}).
chapters/examples/toric_cy3_coha.tex:657:(Theorem~\ref{thm:chiral-qg-equiv}) asserts that three of them
chapters/examples/toric_cy3_coha.tex:750:Theorem~\ref{thm:chiral-qg-equiv} of Vol~I, proved for any
chapters/examples/toric_cy3_coha.tex:758:(Theorem~\ref{thm:chiral-qg-equiv}(I)). For toric CY3, the
chapters/examples/toroidal_elliptic.tex:4693:\phantomsection\label{ch:k3-times-e}
chapters/examples/toroidal_elliptic.tex:5943:(Chapter~\ref{ch:k3-times-e},
chapters/examples/toroidal_elliptic.tex:5944:Definition~\ref{def:k3-double-current-algebra}) substitutes
chapters/examples/toroidal_elliptic.tex:6021:  of Theorem~\textup{\ref{thm:w-infty-chiral-qg}}.
chapters/examples/toroidal_elliptic.tex:6037:  \S\ref{subsec:quantum-chiral-algebras-6d}.
chapters/theory/cy_categories.tex:169:At $d = 2$ the enhancement is explicit enough to compute directly; it drives the $K3$ computations feeding the Borcherds denominator (Vol~III Chapter~\ref{ch:k3}). At $d = 3$ the enhancement was constructed by Sheridan~\cite{Sheridan2015} for the quintic threefold, as part of the HMS proof; the general $d = 3$ construction remains programme-level (conditional on $\bS^3$-framing, see AP-CY6).
chapters/theory/cy_categories.tex:197:Not every invariant of $\cC$ survives the passage through $\Phi$. The functor retains the cyclic $\Ainf$-structure and the Gerstenhaber bracket; it loses the fine structure of the triangulated / $\Ainf$ category (individual objects, t-structures, stability conditions) that is visible only via the fuller categorical CoHA construction of Chapter~\ref{ch:coha}. The kappa-spectrum (Vol~III CLAUDE.md) encodes which invariants survive: $\kappa_\mathrm{cat}$ is always present, $\kappa_\mathrm{ch}$ exists only when $\Phi$ is defined, and $\kappa_\mathrm{BKM}$ records the Borcherds-side lift for $K3 \times E$.
chapters/connections/cy_holographic_datum_master.tex:242:Chapter~\ref{ch:k3-times-e}. AP-CY8 forbids calling this an identity at
chapters/connections/cy_holographic_datum_master.tex:946:(Theorem~\ref{thm:cy-seven-face-master} above).
chapters/examples/k3_times_e.tex:2:\label{ch:k3-times-e}
chapters/examples/k3_times_e.tex:8:This chapter treats $K3 \times E$ as the prototype for the $d = 3$ programme. The concrete object of study is the BKM superalgebra $\mathfrak{g}_{\Delta_5}$ attached to $X = (S \times E)/(\mathbb{Z}/N\mathbb{Z})$, together with the Oberdieck--Pixton theorem identifying its denominator with the Igusa cusp form. The goal is to understand how much of the Vol~I bar-cobar apparatus survives in the $d = 3$ regime, where the CY-to-chiral functor is conjectural: which identities among root multiplicities, genus-$g$ partition functions, and lattice theta series are genuinely theorems versus conjectural identifications awaiting the $d = 3$ functor. The chapter concludes with the K3 double current algebra $\fg_{K3}$ (Definition~\ref{def:k3-double-current-algebra}), the K3 analogue of the double current algebra $\fg \otimes \bC[u,v]$ in which the polynomial ring is replaced by $H^*(S,\bC)$ and the polynomial residue pairing by the Mukai pairing; the resulting finite-dimensional Lie algebra serves as the classical limit of the conjectural ``K3 Yangian'' whose quantization is governed by the Maulik--Okounkov $R$-matrix (Theorem~\ref{thm:k3e-mo-rmatrix}).
chapters/examples/k3_times_e.tex:469:\label{subsec:k3-three-algebraizations}
chapters/examples/k3_times_e.tex:1170:\label{def:k3-double-current-algebra}
chapters/examples/k3_times_e.tex:1346:$\fg_{K3}$ of Definition~\ref{def:k3-double-current-algebra} reduces to
chapters/examples/k3_times_e.tex:1532:\label{sec:k3-perturbative-fact-homology}
 succeeded in 50ms:
MISSING 26
LABEL app:conventions
  REF chapters/theory/introduction.tex:407: This volume inherits the conventions of Volumes~I and~II; we record here the points where the CY setting introduces additional notation or where conventions differ across the literature. A comprehensive conventions appendix is Appendix~\ref{app:conventions}.
  REF chapters/theory/cyclic_ainf.tex:20: where $\dagger(i,p,q) = (i-1)(q-1) + q \sum_{j=1}^{i-1}|a_j|$ follows the Koszul sign rule (see Appendix~\ref{app:conventions}).
LABEL ch:cha-yangian
  REF chapters/theory/e1_chiral_algebras.tex:156: The conjecture is conditional on the chain-level framing; the unconditional statement requires the full CY-A$_3$ programme. Every downstream result in \ref{part:examples} and \ref{part:connections} that uses the BPS Yangian inherits this conditionality. The connection to Maulik-Okounkov and Costello-Witten cohomological Hall algebras is traced in Chapter~\ref{ch:cha-yangian}.
LABEL ch:coha
  REF chapters/theory/cy_categories.tex:197: Not every invariant of $\cC$ survives the passage through $\Phi$. The functor retains the cyclic $\Ainf$-structure and the Gerstenhaber bracket; it loses the fine structure of the triangulated / $\Ainf$ category (individual objects, t-structures, stability conditions) that is visible only via the fuller categorical CoHA construction of Chapter~\ref{ch:coha}. The kappa-spectrum (Vol~III CLAUDE.md) encodes which invariants survive: $\kappa_\mathrm{cat}$ is always present, $\kappa_\mathrm{ch}$ exists only when $\Phi$ is defined, and $\kappa_\mathrm{BKM}$ records the Borcherds-side lift for $K3 \times E$.
LABEL ch:cy-chiral-functor
  REF chapters/theory/e1_chiral_algebras.tex:131: The CY-to-chiral functor $\Phi$ of Chapter~\ref{ch:cy-chiral-functor} has three natural composites. $\Phi_{E_1}$ produces $B^{\mathrm{ord}}(A_C)$; this is the ordered bar sensed by the Yangian. $\mathrm{av} \circ \Phi_{E_1}$ produces $B^{\Sigma}(A_C)$; this is the symmetric bar sensed by the modular characteristic $\kappa_{\mathrm{ch}}$. The full $E_2$ enhancement $\Phi_{E_2}$ produces the Drinfeld-centered bar $B^{E_2}(A_C) = \cZ(B^{\mathrm{ord}}(A_C))$; this is the braided bar sensed by the quantum group. All three factor through $\Phi_{E_1}$. This is the volume's motto: the ordered bar is the primitive.
  REF chapters/theory/e1_chiral_algebras.tex:321: Chapters~\ref{ch:braided-factorization}, \ref{ch:drinfeld-center}, and \ref{ch:quantum-group-reps} use this chapter as the source of the ordered bar coalgebra and the averaging map. Chapter~\ref{ch:cy-chiral-functor} uses Proposition~\ref{prop:e1-sector-d2} as the $d=2$ existence statement for $A_\cC$. Every braided monoidal category that appears later is the Drinfeld center of an underlying ordered one.
LABEL ch:holographic-datum-master
  REF chapters/examples/k3_times_e.tex:1026: The seven-face programme of Chapter~\ref{ch:holographic-datum-master}
  REF chapters/examples/k3_times_e.tex:1071: construction (cf.\ Vol~I, Chapter~\ref{ch:holographic-datum-master})
LABEL ch:k3
  REF chapters/theory/cy_categories.tex:169: At $d = 2$ the enhancement is explicit enough to compute directly; it drives the $K3$ computations feeding the Borcherds denominator (Vol~III Chapter~\ref{ch:k3}). At $d = 3$ the enhancement was constructed by Sheridan~\cite{Sheridan2015} for the quintic threefold, as part of the HMS proof; the general $d = 3$ construction remains programme-level (conditional on $\bS^3$-framing, see AP-CY6).
LABEL ch:toroidal-elliptic
  REF chapters/examples/quantum_group_reps.tex:506: formula (Chapter~\ref{ch:toroidal-elliptic}; distinct from
LABEL ex:k3-step1
  REF chapters/examples/k3_times_e.tex:1589: Example~\ref{ex:k3-step1}: the current algebra of

thinking
**Assessing missing references**

I’m focusing on the static missing set, which includes references to labels in other volumes or appendices. Should I fix all broken references in Volume III? It seems we only need references from this repo, and Volume III shouldn't refer to others unless the labels are in the appendices or the main text. I wonder if the static misses occurred because I only scanned the main chapters and not the appendices. Let’s recompute and include everything to get the actual missing set.
codex
The first pass exposed real drift, but it also treated appendix/frame labels as missing because I constrained the scan too narrowly. I’m widening it to the full Vol III `.tex` surface now so I don’t “fix” valid references by mistake.
exec
/bin/zsh -lc "rg -n '\\\\label\\{app:conventions\\}|\\\\label\\{sec:working-notes\\}|\\\\label\\{sec:mo-r-matrix\\}|\\\\label\\{thm:denom-bar-euler\\}|\\\\label\\{thm:k3e-wall-crossing-mc\\}|\\\\label\\{thm:obstruction-recursion\\}|\\\\label\\{thm:miura-cross-universality\\}|\\\\label\\{thm:e1-stabilization\\}|\\\\label\\{thm:cy-seven-face-master\\}' . -S" in /Users/raeez/calabi-yau-quantum-groups succeeded in 52ms:
./notes/theory_denominator_bar_euler.tex:678:\label{thm:denom-bar-euler}
./appendices/conventions.tex:2:\label{app:conventions}
exec
/bin/zsh -lc "python3 - <<'PY'
import re, pathlib
root = pathlib.Path('.')
text_paths = sorted(p for p in root.rglob('*.tex') if '.git' not in p.parts)
label_re = re.compile(r'\\\\label\\{(["'^}]+)'"\\}')
ref_re = re.compile(r'\\\\(?:eq)?ref\\{(["'^}]+)'"\\}')
labels = {}
refs = {}
for path in text_paths:
    text = path.read_text()
    for i,line in enumerate(text.splitlines(),1):
        for m in label_re.finditer(line):
            labels.setdefault(m.group(1), []).append((str(path), i))
        for m in ref_re.finditer(line):
            refs.setdefault(m.group(1), []).append((str(path), i, line.strip()))
missing = sorted(k for k in refs if k not in labels)
print('MISSING', len(missing))
for k in missing:
    print(f'LABEL {k}')
    for path, i, line in refs[k][:10]:
        print(f'  REF {path}:{i}: {line}')
PY" in /Users/raeez/calabi-yau-quantum-groups succeeded in 113ms:
MISSING 27
LABEL ch:cha-yangian
  REF chapters/theory/e1_chiral_algebras.tex:156: The conjecture is conditional on the chain-level framing; the unconditional statement requires the full CY-A$_3$ programme. Every downstream result in \ref{part:examples} and \ref{part:connections} that uses the BPS Yangian inherits this conditionality. The connection to Maulik-Okounkov and Costello-Witten cohomological Hall algebras is traced in Chapter~\ref{ch:cha-yangian}.
LABEL ch:coha
  REF chapters/theory/cy_categories.tex:197: Not every invariant of $\cC$ survives the passage through $\Phi$. The functor retains the cyclic $\Ainf$-structure and the Gerstenhaber bracket; it loses the fine structure of the triangulated / $\Ainf$ category (individual objects, t-structures, stability conditions) that is visible only via the fuller categorical CoHA construction of Chapter~\ref{ch:coha}. The kappa-spectrum (Vol~III CLAUDE.md) encodes which invariants survive: $\kappa_\mathrm{cat}$ is always present, $\kappa_\mathrm{ch}$ exists only when $\Phi$ is defined, and $\kappa_\mathrm{BKM}$ records the Borcherds-side lift for $K3 \times E$.
LABEL ch:cy-chiral-functor
  REF chapters/theory/e1_chiral_algebras.tex:131: The CY-to-chiral functor $\Phi$ of Chapter~\ref{ch:cy-chiral-functor} has three natural composites. $\Phi_{E_1}$ produces $B^{\mathrm{ord}}(A_C)$; this is the ordered bar sensed by the Yangian. $\mathrm{av} \circ \Phi_{E_1}$ produces $B^{\Sigma}(A_C)$; this is the symmetric bar sensed by the modular characteristic $\kappa_{\mathrm{ch}}$. The full $E_2$ enhancement $\Phi_{E_2}$ produces the Drinfeld-centered bar $B^{E_2}(A_C) = \cZ(B^{\mathrm{ord}}(A_C))$; this is the braided bar sensed by the quantum group. All three factor through $\Phi_{E_1}$. This is the volume's motto: the ordered bar is the primitive.
  REF chapters/theory/e1_chiral_algebras.tex:321: Chapters~\ref{ch:braided-factorization}, \ref{ch:drinfeld-center}, and \ref{ch:quantum-group-reps} use this chapter as the source of the ordered bar coalgebra and the averaging map. Chapter~\ref{ch:cy-chiral-functor} uses Proposition~\ref{prop:e1-sector-d2} as the $d=2$ existence statement for $A_\cC$. Every braided monoidal category that appears later is the Drinfeld center of an underlying ordered one.
LABEL ch:holographic-datum-master
  REF chapters/examples/k3_times_e.tex:1026: The seven-face programme of Chapter~\ref{ch:holographic-datum-master}
  REF chapters/examples/k3_times_e.tex:1071: construction (cf.\ Vol~I, Chapter~\ref{ch:holographic-datum-master})
LABEL ch:k3
  REF chapters/theory/cy_categories.tex:169: At $d = 2$ the enhancement is explicit enough to compute directly; it drives the $K3$ computations feeding the Borcherds denominator (Vol~III Chapter~\ref{ch:k3}). At $d = 3$ the enhancement was constructed by Sheridan~\cite{Sheridan2015} for the quintic threefold, as part of the HMS proof; the general $d = 3$ construction remains programme-level (conditional on $\bS^3$-framing, see AP-CY6).
LABEL ch:toroidal-elliptic
  REF chapters/examples/quantum_group_reps.tex:506: formula (Chapter~\ref{ch:toroidal-elliptic}; distinct from
LABEL def:e1-chiral-algebra
  REF notes/theory_kl_e2_chiral.tex:180: $\mathbb{C} \times \mathbb{R}$ in the sense of Definition~\ref{def:e1-chiral-algebra}
LABEL part:3d-qg
  REF chapters/connections/modular_koszul_bridge.tex:237: Parts (i), (iii), (iv) are Vol~I/II results (\S\ref{sec:k3e-cross-volume}, items K3-1 through K3-13, proved in the K3 modular-tower chapter of Vol~I and in the Vol~II 3D quantum gravity treatment, \ref{part:3d-qg} there). Part (ii) is the Borcherds lift of Borcherds (1998); its use as a modular characteristic is the observation of AP-CY8, not a theorem of Vol~III. The conditionality on propagates from Theorem~\ref{thm:cy-shadow-cohft}.
LABEL part:e1-core
codex
I’ve narrowed the likely real fixes to a small set of mislabeled local refs plus a handful of cross-volume refs that should not have been `\ref` calls in Vol III. I’m refreshing the live build once before editing so I can use the final undefined-reference list as the source of truth.
exec
/bin/zsh -lc 'pkill -9 -f pdflatex 2>/dev/null || true
sleep 2
make fast' in /Users/raeez/calabi-yau-quantum-groupscodex
The build is running. Once it settles, I’ll use the final undefined-reference warnings to decide which refs need actual edits and which are just off-document cross-volume pointers that should be de-referenced.
 succeeded in 22.45s:
  -- Fast build (up to 4 passes) --
Building main.tex (up to 4 passes)
-- Pass 1 / 4 --
  Pass 1: 0 errors, 26 undef refs, 6 undef cites, 0 rerun warnings
-- Pass 2 / 4 --
  Pass 2: 0 errors, 26 undef refs, 6 undef cites, 0 rerun warnings
-- Pass 3 / 4 --
  Pass 3: 0 errors, 26 undef refs, 6 undef cites, 0 rerun warnings
-- Pass 4 / 4 --
  Pass 4: 0 errors, 26 undef refs, 6 undef cites, 0 rerun warnings
  main.pdf built successfully.
     Logs: .build_logs/tex-build.stdout.log and main.log
exec
/bin/zsh -lc "rg -n 'LaTeX Warning: Reference "'`[''^`]+`'"' main.log -o" in /Users/raeez/calabi-yau-quantum-groups exited 1 in 52ms:

exec
/bin/zsh -lc "grep -n 'LaTeX Warning: Reference "'`'"' main.log" in /Users/raeez/calabi-yau-quantum-groups succeeded in 51ms:
1639:LaTeX Warning: Reference `thm:miura-cross-universality' on page 6 undefined on 
1643:LaTeX Warning: Reference `sec:e1-chiral-bialgebra' on page 6 undefined on input
1905:LaTeX Warning: Reference `sec:analytic-sewing' on page 6 undefined on input lin
1934:LaTeX Warning: Reference `def:k3-double-current-algebra' on page 9 undefined on
1956:LaTeX Warning: Reference `prop:e1-descent-unobstructed' on page 11 undefined on
1963:LaTeX Warning: Reference `def:k3-double-current-algebra' on page 12 undefined o
1967:LaTeX Warning: Reference `sec:working-notes' on page 12 undefined on input line
2011:LaTeX Warning: Reference `ch:k3' on page 18 undefined on input line 169.
2028:LaTeX Warning: Reference `ch:coha' on page 18 undefined on input line 197.
2322:LaTeX Warning: Reference `thm:topologization' on page 34 undefined on input lin
2354:LaTeX Warning: Reference `ch:cy-chiral-functor' on page 35 undefined on input l
2373:LaTeX Warning: Reference `ch:cha-yangian' on page 36 undefined on input line 15
2476:LaTeX Warning: Reference `ch:cy-chiral-functor' on page 38 undefined on input l
2997:LaTeX Warning: Reference `sec:k3-perturbative-fact-homology' on page 52 undefin
3207:LaTeX Warning: Reference `part:e1-core' on page 57 undefined on input line 197.
4316:LaTeX Warning: Reference `thm:htt-general' on page 99 undefined on input line 6
4327:LaTeX Warning: Reference `sec:analytic-sewing' on page 99 undefined on input li
4818:LaTeX Warning: Reference `subsec:k3-three-algebraizations' on page 130 undefine
5913:LaTeX Warning: Reference `thm:e1-stabilization' on page 178 undefined on input 
6717:LaTeX Warning: Reference `def:k3-double-current-algebra' on page 249 undefined 
exec
/bin/zsh -lc "rg -n '\\\\input\\{|\\\\include\\{' main.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n 'def:k3-double-current-algebra|ch:k3-times-e|chap:toroidal-elliptic|thm:cy-seven-face-master|label\\{ch:holographic|label\\{thm:cy-seven-face|label\\{subsec:quantum-chiral-algebras-6d|label\\{thm:w-infty-chiral-qg|label\\{thm:k3e-wall-crossing-mc|label\\{thm:obstruction-recursion|label\\{sec:mo-rmatrix-comparison|label\\{rem:toric-kappa-patterns|label\\{prop:e1-descent-unobstructed' chapters frame appendices main.tex -S" in /Users/raeez/calabi-yau-quantum-groups succeeded in 52ms:
396:\input{chapters/frame/preface}
418:\input{chapters/theory/introduction}
419:\input{chapters/theory/cy_categories}
420:\input{chapters/theory/cyclic_ainf}
421:\input{chapters/theory/hochschild_calculus}
422:\input{chapters/theory/e1_chiral_algebras}
423:\input{chapters/theory/e2_chiral_algebras}
424:\input{chapters/theory/en_factorization}
433:\input{chapters/theory/cy_to_chiral}
434:\input{chapters/theory/quantum_chiral_algebras}
435:\input{chapters/theory/modular_trace}
443:\input{chapters/theory/quantum_groups_foundations}
444:\input{chapters/theory/braided_factorization}
445:\input{chapters/theory/drinfeld_center}
454:\input{chapters/examples/toroidal_elliptic}
455:% \input{chapters/examples/k3_times_e} % Merged into toroidal_elliptic.tex
456:\input{chapters/examples/toric_cy3_coha}
457:\input{chapters/examples/fukaya_categories}
458:\input{chapters/examples/derived_categories_cy}
459:\input{chapters/examples/matrix_factorizations}
 exited 2 in 51ms:
rg: frame: No such file or directory (os error 2)
chapters/examples/toric_cy3_coha.tex:302:\label{rem:toric-kappa-patterns}
chapters/examples/k3_times_e.tex:2:\label{ch:k3-times-e}
chapters/examples/k3_times_e.tex:8:This chapter treats $K3 \times E$ as the prototype for the $d = 3$ programme. The concrete object of study is the BKM superalgebra $\mathfrak{g}_{\Delta_5}$ attached to $X = (S \times E)/(\mathbb{Z}/N\mathbb{Z})$, together with the Oberdieck--Pixton theorem identifying its denominator with the Igusa cusp form. The goal is to understand how much of the Vol~I bar-cobar apparatus survives in the $d = 3$ regime, where the CY-to-chiral functor is conjectural: which identities among root multiplicities, genus-$g$ partition functions, and lattice theta series are genuinely theorems versus conjectural identifications awaiting the $d = 3$ functor. The chapter concludes with the K3 double current algebra $\fg_{K3}$ (Definition~\ref{def:k3-double-current-algebra}), the K3 analogue of the double current algebra $\fg \otimes \bC[u,v]$ in which the polynomial ring is replaced by $H^*(S,\bC)$ and the polynomial residue pairing by the Mukai pairing; the resulting finite-dimensional Lie algebra serves as the classical limit of the conjectural ``K3 Yangian'' whose quantization is governed by the Maulik--Okounkov $R$-matrix (Theorem~\ref{thm:k3e-mo-rmatrix}).
chapters/examples/k3_times_e.tex:1170:\label{def:k3-double-current-algebra}
chapters/examples/k3_times_e.tex:1316:(Chapter~\ref{chap:toroidal-elliptic},
chapters/examples/k3_times_e.tex:1346:$\fg_{K3}$ of Definition~\ref{def:k3-double-current-algebra} reduces to
chapters/examples/k3_times_e.tex:1667:Definition~\textup{\ref{def:k3-double-current-algebra}})
chapters/frame/preface.tex:535:Chapter~\ref{chap:toroidal-elliptic}: (A)~constructive CY gluing
chapters/connections/cy_holographic_datum_master.tex:242:Chapter~\ref{ch:k3-times-e}. AP-CY8 forbids calling this an identity at
chapters/connections/cy_holographic_datum_master.tex:946:(Theorem~\ref{thm:cy-seven-face-master} above).
chapters/theory/en_factorization.tex:630:where $\cF$ is the local $E_3$-algebra of observables. For $M = \C^3$, the integral is expected to recover the quantum toroidal algebra $U_{q,t}(\widehat{\widehat{\fgl}}_1)$ (conditional on Conjecture~\ref{conj:topological-e3-comparison}). For $M = K3 \times E$ (the CY case), the integral should recover the BKM-related chiral algebra of Chapter~\ref{ch:k3-times-e}; this is conditional on CY-A$_3$ and on the 6d algebraic framework for compact manifolds.
chapters/theory/e2_chiral_algebras.tex:158:Chapter~\ref{ch:k3-times-e} (see also Theorem~\ref{thm:k3e-scattering-bkm}).
chapters/theory/quantum_groups_foundations.tex:213: \item \emph{Elliptic: the elliptic quantum group $E_{q,p}(\frakg)$.} Spectral parameter $u \in E_\tau$ (elliptic curve). The Belavin $R$-matrix is the unique (up to gauge) solution of the QYBE with doubly-periodic meromorphic dependence on the spectral parameter. The propagator becomes $d\!\log\theta_1(z \mid \tau)$, and the Arnold relation lifts to the Fay trisecant identity. See Chapter~\ref{chap:toroidal-elliptic} for the bar-cobar treatment.
chapters/theory/quantum_groups_foundations.tex:246: \item $d = 2$ (K$3$ and abelian surface cases): the functor $\Phi$ is constructed (Theorem~CY-A$_2$), so $A_\cC$ is defined, and CY-C reduces to a semisimplification plus reconstruction statement. The BKM route (Borcherds--Gritsenko--Nikulin) provides partial evidence; see Chapter~\ref{ch:k3-times-e} and the toroidal elliptic computation in Chapter~\ref{chap:toroidal-elliptic}. At $d = 2$, $\kappa_{\mathrm{cat}} = \chi(\cO_{K3}) = 2$, while $\kappa_{\mathrm{BKM}} = 5$ is the weight of $\Delta_5$: forbids conflation.
chapters/theory/introduction.tex:280: \item The K3 double current algebra $\fg_{K3}$ (Definition~\ref{def:k3-double-current-algebra}): the finite-dimensional analogue of the DDCA in which $\bC[u,v]$ is replaced by $H^*(S,\bC)$ with the Mukai pairing.
chapters/theory/introduction.tex:308:The $K3 \times E$ prototype generates ten research programmes, each with formal conjectures grounded in the 90+ compute engines. The formal development is in Chapter~\ref{chap:toroidal-elliptic}.
chapters/theory/introduction.tex:397:In addition to the four standard families, the toroidal and elliptic algebras chapter (Chapter~\ref{chap:toroidal-elliptic}) develops the $K3 \times E$ programme in full: the generalized root datum, the BKM superalgebra $\mathfrak{g}_{\Delta_5}$ with its Igusa cusp form denominator identity, the shadow--Siegel gap theorem, thirteen structural results (K3-1 through K3-13), all ten research programmes (A through J), and the DDCA--toroidal bridge identifying the deformed double current algebra as the rational degeneration of the quantum toroidal algebra (Conjecture~\ref{conj:ddca-toroidal-bridge}). The K3 double current algebra $\fg_{K3}$ (Chapter~\ref{ch:k3-times-e}, Definition~\ref{def:k3-double-current-algebra}) provides the K3 analogue of the DDCA, replacing $\bC[u,v]$ with $H^*(S,\bC)$. The toric CY$_3$ CoHA chapter (Chapter~\ref{ch:toric-coha}) develops the affine Yangian and $\mathcal{W}_{1+\infty}$ side: the Jordan quiver gives $Y(\widehat{\mathfrak{gl}}_1) \simeq \mathcal{W}_{1+\infty}$, the toric fan is the Dynkin data, and the shuffle algebra presentation connects to the KZ equations of Volume~I.
chapters/examples/toroidal_elliptic.tex:55:\label{chap:toroidal-elliptic}
chapters/examples/toroidal_elliptic.tex:4693:\phantomsection\label{ch:k3-times-e}
codex
One build detail mattered: `k3_times_e.tex` is not included in `main.tex`, so any references still pointing at labels defined only there are genuinely broken, not rerun noise. I’m mapping those merged-chapter references to the labels that actually exist in `toroidal_elliptic.tex` before patching.
exec
/bin/zsh -lc "sed -n '1150,1215p' chapters/examples/toroidal_elliptic.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "sed -n '5920,6055p' chapters/examples/toroidal_elliptic.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n 'def:k3-double-current-algebra|thm:k3e-wall-crossing-mc|thm:obstruction-recursion|thm:w-infty-chiral-qg|subsec:quantum-chiral-algebras-6d|label\\{ch:cy-holographic|label\\{thm:cy-seven-face-master|label\\{thm:seven-face|label\\{ch:cha-yangian|label\\{ch:coha|label\\{ch:cy-chiral-functor|label\\{thm:miura-cross-universality|label\\{prop:e1-descent-unobstructed' chapters/examples/toroidal_elliptic.tex chapters/connections/cy_holographic_datum_master.tex chapters/theory/*.tex chapters/frame/preface.tex -S" in /Users/raeez/calabi-yau-quantum-groups succeeded in 50ms:
\frac{[v][\lambda{-}1{+}\eta]}{[\eta][\lambda{-}1]}
\cdot
\frac{[u{+}v][\lambda{+}\eta]}{[\eta][\lambda]}
\cdot
\frac{[u{+}\eta]}{[\eta]} \;+\;
\frac{[v{-}\lambda{+}1][\eta]}{[-\lambda{+}1][v{+}\eta]}
\cdot
\frac{[u{+}v{+}\lambda][\eta]}{[\lambda][u{+}v{+}\eta]}
\cdot
\frac{[u{+}\eta]}{[\eta]}.
\end{align}
After cancelling common factors $[u{+}\eta]/([\eta]^3\,[\lambda]\,
[\lambda{-}1])$ from both sides and clearing denominators, the
equation reduces to an identity among products of theta functions
evaluated at the six arguments $\{u, v, u{+}v, \lambda,
\lambda{+}\eta, \lambda{-}1{+}\eta\}$.
\end{computation}

\begin{proposition}[DYBE reduces to Fay; \ClaimStatusProvedHere]
\label{prop:dybe-reduces-to-fay}
 succeeded in 50ms:
of the DDCA (Vol~II, Theorem~\ref{thm:DDCA-m2}) is a finite polynomial in
two $\lambda$-variables. The toroidal algebra has a central extension
governed by the two central elements $C, C'$ (the level and dual level).
In the rational limit, the toroidal central extension collapses to
a polynomial in the mode numbers, reproducing the DDCA central
extension structure. The precise coefficient matching is the content
of item~(i) of the conjecture.

\emph{(4) Physical origin.}
Both algebras arise from the same M-theory geometry.
The DDCA is the boundary algebra of 5d holomorphic Chern--Simons
on $\mathbb{R}_t \times \bC^2$ (Vol~II, \S\ref{subsec:DDCA-ainfty}).
The quantum toroidal algebra acts on the equivariant K-theory of
$\mathrm{Hilb}(\bC^2)$, which is the moduli space of M2-brane
instantons in the same 5d theory. The passage from the boundary
algebra to the instanton moduli algebra is the passage from the
rational ($\hbar \to 0$) to the quantum ($\hbar \neq 0$) regime.
Maulik--Okounkov identify the quantum toroidal algebra as the
symmetry algebra of the instanton moduli space; the DDCA is its
rational shadow on the boundary.
 succeeded in 52ms:
chapters/theory/introduction.tex:280: \item The K3 double current algebra $\fg_{K3}$ (Definition~\ref{def:k3-double-current-algebra}): the finite-dimensional analogue of the DDCA in which $\bC[u,v]$ is replaced by $H^*(S,\bC)$ with the Mukai pairing.
chapters/theory/introduction.tex:397:In addition to the four standard families, the toroidal and elliptic algebras chapter (Chapter~\ref{chap:toroidal-elliptic}) develops the $K3 \times E$ programme in full: the generalized root datum, the BKM superalgebra $\mathfrak{g}_{\Delta_5}$ with its Igusa cusp form denominator identity, the shadow--Siegel gap theorem, thirteen structural results (K3-1 through K3-13), all ten research programmes (A through J), and the DDCA--toroidal bridge identifying the deformed double current algebra as the rational degeneration of the quantum toroidal algebra (Conjecture~\ref{conj:ddca-toroidal-bridge}). The K3 double current algebra $\fg_{K3}$ (Chapter~\ref{ch:k3-times-e}, Definition~\ref{def:k3-double-current-algebra}) provides the K3 analogue of the DDCA, replacing $\bC[u,v]$ with $H^*(S,\bC)$. The toric CY$_3$ CoHA chapter (Chapter~\ref{ch:toric-coha}) develops the affine Yangian and $\mathcal{W}_{1+\infty}$ side: the Jordan quiver gives $Y(\widehat{\mathfrak{gl}}_1) \simeq \mathcal{W}_{1+\infty}$, the toric fan is the Dynkin data, and the shuffle algebra presentation connects to the KZ equations of Volume~I.
chapters/connections/cy_holographic_datum_master.tex:24:\label{ch:cy-holographic-datum-master}
chapters/examples/toroidal_elliptic.tex:5944:Definition~\ref{def:k3-double-current-algebra}) substitutes
chapters/examples/toroidal_elliptic.tex:6021:  of Theorem~\textup{\ref{thm:w-infty-chiral-qg}}.
chapters/examples/toroidal_elliptic.tex:6037:  \S\ref{subsec:quantum-chiral-algebras-6d}.

thinking
**Looking for missing labels**

The search results didn't show an actual label in the toroidal_elliptic section, and it might be missing entirely. I need to inspect around 1170, but that’s in the k3_times_e file, which isn’t included. So, the `def:k3-double-current-algebra` seems to be totally absent in the main file. I’ll have to find an equivalent label in the toroidal_elliptic merged chapter, maybe something like `def:ddca-k3` or similar. I should search within toroidal_elliptic for "double current algebra."
exec
/bin/zsh -lc "rg -n 'double current algebra|K3 double current algebra|DDCA|quantum-chiral-algebras-6d|W_{1\\+\\infty}|Miura|seven-face|wall-crossing.*MC|obstruction recursion|descent unobstructed|topologization' chapters/examples/toroidal_elliptic.tex chapters/connections/cy_holographic_datum_master.tex chapters/theory/*.tex chapters/frame/preface.tex appendices/conventions.tex -S" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "sed -n '1000,1125p' chapters/examples/k3_times_e.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "sed -n '330,380p' chapters/theory/introduction.tex" in /Users/raeez/calabi-yau-quantum-groups exited 2 in 52ms:
rg: regex parse error:
    (?:double current algebra|K3 double current algebra|DDCA|quantum-chiral-algebras-6d|W_{1\+\infty}|Miura|seven-face|wall-crossing.*MC|obstruction recursion|descent unobstructed|topologization)
                                                                                          ^^
error: unclosed counted repetition
 succeeded in 50ms:
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
 = \kappa_{\mathrm{cat}}(S) + \kappa_{\mathrm{ch}}(S \times E)$ expresses the weight
 of the automorphic form as a sum of fiber and global
 modular characteristics.
\item \emph{Schottky shadow programme.}
 At $g \leq 3$, the shadow obstruction tower sees nearly all
 of the moduli. At $g \geq 4$, the Schottky locus has
 positive codimension and the shadow is imprisoned in
 tautological classes. The programme: characterise the
 tautological projection of Siegel modular forms, and
 determine whether the shadow tower generates the image of
 $S_*(\Sp_{2g}(\Z)) \to R^*(\overline{\cM}_g)$.
\item \emph{Mock modularity and the bar complex.}
 The 1/4-BPS counting function is a mock modular form with
 shadow $24\,\eta^3$. The factor $24 = \chi(K3)$ is
 the surface announcing its existence. The programme:
 construct a half-integral-weight metaplectic bar complex
 whose shadow obstruction tower produces the mock modular
 completion.
\item \emph{Modular factorization envelope.}
 Construct the universal modular factorization envelope

thinking
**Inspecting search patterns**

It looks like the `rg` command didn’t work due to regex issues. I might need to try more targeted searches with something like `rg -n 'label\\{.*' ...` to get actual labels. It sounds like I should check different contexts and possibly focus on searching in `toroidal_elliptic` for specific phrases. So, I think I'll redo the searches using simpler patterns one at a time to isolate the problem.
codex
I’ve confirmed one structural source of breakage: the merged K3 material still points at labels that only exist in the retired `k3_times_e.tex`, not in the live `toroidal_elliptic.tex`. I’m locating the corresponding live anchors now so the fixes stay local and truthful.
exec
/bin/zsh -lc "rg -n 'K3 double current algebra|double current algebra|wall-crossing divisor|Section~\\\\ref\\{sec:k3e-qvcg\\}|W_\\{1\\+\\\\infty\\}|quantum chiral algebras.*6d|Maulik--Okounkov' chapters/examples/toroidal_elliptic.tex -S" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n 'label\\{["'^}]+'"\\}' chapters/examples/toroidal_elliptic.tex | sed -n '160,260p'" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n 'label\\{["'^}]+'"\\}' chapters/connections/cy_holographic_datum_master.tex chapters/theory/cy_to_chiral.tex chapters/theory/e1_chiral_algebras.tex chapters/frame/preface.tex chapters/theory/introduction.tex chapters/examples/toric_cy3_coha.tex chapters/theory/drinfeld_center.tex chapters/theory/e2_chiral_algebras.tex -S" in /Users/raeez/calabi-yau-quantum-groups succeeded in 51ms:
4935:The braided monoidal structure on $\Rep^{E_2}(G(K3 \times E))$ is governed by the Maulik--Okounkov $R$-matrix of the affine Yangian $Y(\widehat{\mathfrak{g}}_{\Delta_5})$. This Yangian acts on the equivariant cohomology of the Hilbert scheme of curves on $K3 \times E$ and satisfies the CY involution
5035:\section{The Maulik--Okounkov $R$-matrix}
5041:The Maulik--Okounkov $R$-matrix for $K3 \times E$ is the generating function
5786:The deformed double current algebra
5803:\index{deformed double current algebra!toroidal bridge}
5811: The deformed double current algebra
5937:Maulik--Okounkov identify the quantum toroidal algebra as the
5942:surface~$S$: the K3 double current algebra $\fg_{K3}$
 succeeded in 52ms:
2044:\label{rem:factor-2-is-kappa}
2051:\begin{equation}\label{eq:moonshine-multiplier}
2075:\label{rem:twining-genera}
2129:\label{subsec:lattice-gepner}
2132:\label{rem:lattice-voa-k3}
2153:\label{rem:gepner-model-k3}
2169:\label{subsec:cdr-k3}
2172:\label{rem:cdr-k3}
2192:\label{subsec:koszul-dual-k3}
2195:\label{prop:koszul-dual-k3}
2222:\label{subsec:pushforward-k3}
2230:\label{constr:pushforward-chiral-algebra}
2278:\label{prop:pushforward-ope}
2308:\label{rem:kappa-collapse}
2364:\label{sec:k3xe-geometry}
2368:\label{subsec:hodge-k3xe}
2372:\label{prop:hodge-k3xe}
2408:\label{subsec:hkr-k3xe}
2412:\label{prop:hkr-k3xe}
2436:\label{subsec:nc-brauer}
 succeeded in 50ms:
chapters/theory/e2_chiral_algebras.tex:2:\label{ch:e2-chiral}
chapters/theory/e2_chiral_algebras.tex:12:\label{sec:e2-operad}
chapters/theory/e2_chiral_algebras.tex:15:\label{def:e2-operad}
chapters/theory/e2_chiral_algebras.tex:26:\label{thm:lurie-e2-braided}
chapters/theory/e2_chiral_algebras.tex:40:\label{def:e2-chiral-algebra}
chapters/theory/e2_chiral_algebras.tex:51:\label{rem:deligne-hochschild}
chapters/theory/e2_chiral_algebras.tex:61:\label{sec:e2-from-cyclic-ainf}
chapters/theory/e2_chiral_algebras.tex:68:\label{thm:ks-tamarkin-cyclic-e2}
chapters/theory/e2_chiral_algebras.tex:81:\label{rem:cy-dim-shift}
chapters/theory/e2_chiral_algebras.tex:90:\label{cor:e2-chiral-from-cy2}
chapters/theory/e2_chiral_algebras.tex:124:\label{conj:e2-chiral-from-cy3}
chapters/theory/e2_chiral_algebras.tex:134:\label{sec:braided-tensor-from-e2}
chapters/theory/e2_chiral_algebras.tex:142:\label{def:mtc-e2-chiral}
chapters/theory/e2_chiral_algebras.tex:150:\label{prop:mtc-k3}
chapters/theory/e2_chiral_algebras.tex:184:\label{conj:mtc-cy3-coha}
chapters/theory/e2_chiral_algebras.tex:194:\label{sec:drinfeld-center-bridge}
chapters/theory/e2_chiral_algebras.tex:204:\label{conj:phi-e2-drinfeld-center}
chapters/theory/e2_chiral_algebras.tex:221:\label{rem:ap34-four-functors}
chapters/theory/e2_chiral_algebras.tex:236:\label{rem:v2ap-cross-reference}
chapters/theory/e2_chiral_algebras.tex:248:\label{sec:e2-koszul-and-bar}
exec
/bin/zsh -lc "sed -n '810,845p' chapters/connections/cy_holographic_datum_master.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "sed -n '5005,5065p' chapters/examples/toroidal_elliptic.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "sed -n '5768,5835p' chapters/examples/toroidal_elliptic.tex" in /Users/raeez/calabi-yau-quantum-groups succeeded in 52ms:

%% =====================================================================
%% SECTION 9: The seven-face master theorem
%% =====================================================================

\section{The seven-face master theorem in the CY setting}
\label{sec:cy-seven-face-master}

The preceding seven sections each realize the binary CY collision residue
in one geometric language. The master theorem asserts that all seven
realizations are canonically equivalent, with the equivalences given by
explicit specialization or limit, and with the limit/specialization data
recorded by the seven-face commuting diagram of Vol~I.

\begin{conjecture}[Seven faces of $r_{CY}(z)$]
\label{conj:cy-seven-face-master}
Let $\cC$ be a Calabi--Yau category of dimension $d \in \{2, 3\}$, and
let $A_\cC$ be its chiral algebraization (proved for $d = 2$; conditional
on Conjecture~CY-A$_3$ for $d = 3$). Then the seven realizations
\[
 succeeded in 52ms:

\noindent\textit{Verification}: 81 tests in \texttt{k3\_relative\_chiral.py} covering the five $\kappa_{\mathrm{ch}}$-verification paths, total root multiplicity at levels $1$--$30$, and shadow-to-BKM bridge consistency.

\section{From fiber $\kappa_{\mathrm{ch}}$ to global $\kappa_{\mathrm{ch}}$: the Borcherds lift}
\label{sec:k3e-fiber-to-global}

The fiber lattice-rank invariant $\kappa_{\mathrm{fiber}} = 24$ (from the $24$ free bosons of the K3 fiber) and the BKM modular characteristic $\kappa_{\mathrm{BKM}} = 5$ (from the Borcherds lift weight) are related by a precise arithmetic mechanism.

\begin{theorem}[Fiber-to-global descent]
\label{thm:k3e-fiber-global}
\ClaimStatusProvedHere
Let $A_0 = \cH_{24}$ be the rank-$0$ Heisenberg chiral algebra with $\kappa_{\mathrm{ch}}(A_0) = 24$, and let $\kappa_{\mathrm{BKM}} = \mathrm{wt}(\Delta_5) = 5$. Then:
\begin{enumerate}[label=(\roman*)]
 \item The Borcherds additive lift $\phi_{0,1} \mapsto \Delta_5$ maps the fiber shadow data to the global automorphic form, with the weight formula $\mathrm{wt}(\Delta_5) = c(0)/2 = 10/2 = 5$.
 \item The ``lost'' $19 = 24 - 5$ units of $\kappa_{\mathrm{ch}}$ enter the imaginary root structure of $\mathfrak{g}_{\Delta_5}$: the $19$-dimensional space $\ker(\Lambda_{K3} \to \Lambda^{3,2})$ contributes imaginary simple roots whose total multiplicity accounts for the $\kappa_{\mathrm{ch}}$-deficit.
 \item The shadow depth upgrades from class G (Gaussian, rank-$0$ Heisenberg) to class M (mixed, infinite tower) in the passage from fiber to global: the fiber theory terminates at degree $2$, while the global BKM algebra has infinite shadow depth.
\end{enumerate}
\ClaimStatusProvedHere
\end{theorem}

 succeeded in 51ms:
The four-fold matching of
Conjecture~\ref{conj:m2-four-fold-matching} ensures that no
information is lost: sector, level, rank, and genus all transfer
across the duality.

This is the natural culmination of the chapter. The degeneration
chain~\eqref{eq:degeneration-chain} (elliptic $\to$ trigonometric
$\to$ rational) is supplemented by a fourth vertex: the double-loop
regime, in which the base geometry $\bC^* \times \bC^*$ supports a
genuine surface factorization algebra, and in which bar-cobar duality
acquires a direct physical interpretation as the AdS/CFT
correspondence for M2-branes.
\end{remark}


\subsection{The DDCA--toroidal bridge}
\label{subsec:ddca-toroidal-bridge}

The deformed double current algebra
$\mathrm{DDCA}_k(\mathfrak{gl}_K) = U(\mathfrak{gl}_K \otimes \bC[u,v])$


thinking
**Evaluating theorem labeling**

I think the reference to `thm:cy-seven-face-master` should be changed to `conj:cy-seven-face-master`, or maybe it needs a section label instead. The text refers to "Theorem above," but upon closer inspection, it seems like it's actually referring to a conjecture. I need to check the surrounding context around line 946 to confirm this. It’s important to get the labeling right!
thinking
**Reviewing references and context**

I think I need to fix some wording in my file, particularly with a minimal change to "Conjecture\ref{conj:cy-seven-face-master} above." That sounds good! I also want to inspect the introduction around `prop:e1-descent-unobstructed` to see if it should refer to `thm:e1-descent-degeneration` or `thm:toric-chart-gluing`. It feels important to check the context carefully. Maybe a search for the phrase "unobstructed" will help clarify things further.
exec
/bin/zsh -lc "sed -n '612,640p' chapters/theory/drinfeld_center.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "sed -n '1328,1355p' chapters/theory/cy_to_chiral.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n 'unobstructed|descent theorem|chart-atlas regime|open for compact CY3' chapters/theory/cy_to_chiral.tex chapters/theory/introduction.tex -S" in /Users/raeez/calabi-yau-quantum-groups succeeded in 50ms:
verified at the level of numerical invariants. The Drinfeld
double is $\mathrm{Drin}(H_k) = H_k \otimes H_{-k} / (c = c')$,
dimension~$3$, with brackets $[J, J'] = k \cdot c$.
The naive Lie centre $Z(\mathrm{Drin}(H_k))$ has dimension~$1$
at generic~$k$.
The chiral derived centre is
$Z^{\mathrm{der}}_{\mathrm{ch}}(H_k) \cong
\bC \oplus \bC[-1] \oplus \bC[-2]$, dimension~$3$:
the discrepancy ($1$ vs $3$) reflects $\mathrm{Ext}^1$
($J$, the derivation) and $\mathrm{Ext}^2$ ($:JJ:$, the
level deformation) invisible to the commutant.
Five consistency checks match across both sides:
$r$-matrix coefficient $= k$, $\kappa_{\mathrm{ch}} = k$,
$\chi = 1$, shadow class $G$ / depth~$2$,
complementarity $k + (-k) = 0$. Verified at $6$ level
values ($k = 0, 1, -1, 1/2, 7, -3/2$) with $72$ compute
tests. For class~$G$ the $\Etwo$ structure on both sides is
determined by the single parameter~$k$, so the conjecture
verification reduces to matching this one numerical
invariant.
 succeeded in 50ms:
The $E_2$-page is the \v{C}ech cohomology of the presheaf $\alpha \mapsto H^\bullet(\CoHA(Q_\alpha, W_\alpha))$:
\begin{equation}
\label{eq:e2-page}
 E_2^{p,q} \;=\; \check{H}^p\!\bigl(I;\, \alpha \mapsto H^q(\CoHA(Q_\alpha, W_\alpha))\bigr).
\end{equation}
\end{definition}

The following theorem is the structural heart of the $\Eone$ descent theory.

\begin{theorem}[$\Eone$ descent degeneration]
\label{thm:e1-descent-degeneration}
\ClaimStatusProvedHere{}
For $\Eone$-algebras, the \v{C}ech descent spectral sequence~\eqref{eq:e1-descent-ss} degenerates at $E_2$. That is:
\begin{equation}
\label{eq:e1-degeneration}
 E_2^{p,q} \;=\; 0 \qquad \text{for all } p \geq 2 \text{ and all } q,
\end{equation}
and consequently the spectral sequence collapses to a short exact sequence
\[
 0 \;\to\; E_2^{1,q-1} \;\to\; H^q(A_\cC) \;\to\; E_2^{0,q} \;\to\; 0.
 succeeded in 52ms:
chapters/theory/introduction.tex:363: (Proposition~\ref{prop:e1-descent-unobstructed}); open for
chapters/theory/introduction.tex:364: compact CY3 beyond the chart-atlas regime.
chapters/theory/cy_to_chiral.tex:439: \item \emph{Step~2}: $\HH^2(\mathrm{PV}^*(\C^3)) = 1$, so the deformation is unique, spanned by $\sigma_3$ (Theorem~\textup{\ref{thm:c3-hochschild}}). $\HH^3 = 0$ by Bogomolov--Tian--Todorov, so the deformation is unobstructed.
chapters/theory/cy_to_chiral.tex:487: \item $\HH^3(\mathrm{PV}^*(\C^3)) = 0$: the Bogomolov--Tian--Todorov theorem guarantees unobstructedness.
chapters/theory/cy_to_chiral.tex:499:The vanishing $\HH^3 = 0$ is the Bogomolov--Tian--Todorov unobstructedness theorem for the CY$_3$ moduli problem: the Kodaira--Spencer dga of $\C^3$ is formal, and the Maurer--Cartan moduli space is smooth. This guarantees that the $\Omega$-deformation determined by $\sigma_3$ extends to all orders.
chapters/theory/cy_to_chiral.tex:982: \item \emph{Topological framing is unobstructed.}
chapters/theory/cy_to_chiral.tex:1408:The pattern $E_n = E_{d-2}$ (for $d \geq 3$) suggests a Bott periodicity phenomenon: the $E_n$ level of the CY$_d$ chiral algebra is controlled by $\pi_1(\Conf_2(\R^{d-2}))$, which is $\Z$ for $d - 2$ even and $0$ for $d - 2$ odd. For $d = 3$: $d - 2 = 1$, $\pi_1(\Conf_2(\R^1)) = 0$ (the real line has trivially ordered configuration space), and the descent is unobstructed. For $d = 4$: $d - 2 = 2$, $\pi_1(\Conf_2(\R^2)) = \Z$ (the braid group), and the descent requires higher coherences.
chapters/theory/cy_to_chiral.tex:1453:The descent theorem (Theorem~\ref{thm:e1-descent-degeneration}) translates this homotopy-theoretic fact into a concrete computational advantage: the quiver-chart atlas of a CY$_3$ category glues via a \emph{single system of transition maps} (the wall-crossing automorphisms $K_\gamma$), with no higher coherence data. The global $\Eone$-chiral algebra
chapters/theory/cy_to_chiral.tex:1457:is assembled cleanly from pairwise gluing data, and the hocolim works precisely because $\Eone$ descent is unobstructed.

thinking
**Researching introduction props**

I think the introduction prop should be thm:e1-descent-degeneration, and I feel good about that choice. I’m considering whether I might also need thm:topologization cross-volume. It seems like I need to search for context regarding e1_chiral line 66. Okay, my plan is to gather that information to solidify my perspective. I’ll make sure to clarify that when I look it up. Let’s see what I find!
exec
/bin/zsh -lc "sed -n '315,338p' chapters/frame/preface.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "sed -n '188,205p' chapters/theory/e2_chiral_algebras.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "sed -n '56,74p' chapters/theory/e1_chiral_algebras.tex" in /Users/raeez/calabi-yau-quantum-groups succeeded in 51ms:
braided structure: BPS indices as simples, braiding computing refined
DT wall-crossing. Conditional on CY-A$_3$; AP-CY11
propagates: downstream uses inherit the CY-A$_3$ dependency.
\end{conjecture}

\section{Connection to Volume~II: the Drinfeld center}
\label{sec:drinfeld-center-bridge}

Volume~II constructs $\Phi_{E_1}$ and proves $E_1$-chiral Koszul
duality (see \ref{part:e1-core} of \cite{VolII}). The Drinfeld center
$Z\colon E_1\text{-}\Cat \xrightarrow{\sim} E_2\text{-}\Cat$
(under dualizability) is the categorical passage from ordered
monoidal data to braided monoidal data. On the bar side it matches the
symmetrization map $\mathrm{av}\colon B^{\mathrm{ord}} \to B^\Sigma$.

\begin{conjecture}[Volume~III central conjecture: $\Phi_{E_2} = Z^{\mathrm{ch}} \circ \Phi_{E_1}$]
\label{conj:phi-e2-drinfeld-center}
\ClaimStatusConjectured
 succeeded in 51ms:

$\mathrm{SC}^{\mathrm{ch},\mathrm{top}}$ is \emph{not} the
tensor product $E_1 \otimes E_2$: the directionality constraint
(no open-to-closed) and the mixed operations make it a genuinely
two-coloured operad. Dunn additivity does not apply.
The $E_3$-chiral upgrade requires a 3d
holomorphic-topological theory (proved for Kac--Moody
via holomorphic Chern--Simons; conjectural in general).
The further $E_3$-topological upgrade requires a conformal
vector at non-critical level
(Volume~I, Theorem~\textup{\ref*{thm:topologization}}).
\end{definition}

The closed colour carries $E_2$ structure from
$\mathrm{FM}_k(\mathbb{C})$: holomorphic, braided, and the
home of the chiral algebra. The open colour carries $E_1$
structure from ordered real configurations: topological,
noncommutative, and the home of the ordered bar complex.
Standard Beilinson--Drinfeld chiral algebras are
 succeeded in 51ms:
coefficients $\delta^{(r)}$: the shadow tower encodes the
coproduct corrections of the chiral quantum group.

The universal coproduct $\Delta_z(e_s) = \sum C(N_R{-}b, k)\,
z^k\, e_a^L \cdot e_b^R$ (all spins, closed form) extends the
Drinfeld coproduct from spin~$2$ to arbitrary spin, with the
universal Miura coefficient $(\Psi{-}1)/\Psi$ on the leading
cross-term $J \otimes W_{s-1}$ at every spin $s \ge 2$
(Theorem~\ref{thm:miura-cross-universality}).

\bigskip

\noindent\textbf{The $E_1$-chiral bialgebra.}
Volume~I defines $E_1$-chiral quantum groups abstractly. This
volume constructs them concretely from CY geometry. The
$E_1$-chiral bialgebra axioms (formalized in
\S\ref{sec:e1-chiral-bialgebra}) require: (H1)~an $E_1$-chiral
algebra $A$ on a curve $X$; (H2)~a spectral coproduct
$\Delta_z \colon A \to A \otimes A$ (living on the OPEN/$E_1$
colour); (H3)~an $R$-matrix $R(z)$ satisfying YBE; (H4)~RTT
codex
I’ve split the failures into two types: local label drift, which I can repair with aliases or retargeted refs, and off-document cross-volume refs, which need to become plain/cited prose because those labels do not exist in Vol III. I’m reading each live line now and then I’ll patch the smallest honest change per case.
exec
/bin/zsh -lc "sed -n '150,205p' chapters/theory/cy_categories.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "sed -n '120,170p' chapters/theory/e1_chiral_algebras.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n 'thm:miura-cross-universality|sec:e1-chiral-bialgebra|sec:analytic-sewing|def:k3-double-current-algebra|prop:e1-descent-unobstructed|sec:working-notes|ch:k3\\}|ch:coha|thm:topologization|ch:cy-chiral-functor|ch:cha-yangian|sec:k3-perturbative-fact-homology|part:e1-core|thm:htt-general|subsec:k3-three-algebraizations|thm:e1-stabilization|thm:w-infty-chiral-qg|subsec:quantum-chiral-algebras-6d|rem:toric-structural-patterns|thm:chiral-qg-equiv|ch:toroidal-elliptic|thm:cy-seven-face-master|part:3d-qg' chapters frame main.tex -S" in /Users/raeez/calabi-yau-quantum-groups succeeded in 51ms:
\]
for all $n \geq 2$, where $\epsilon$ is the Koszul sign determined by the degrees of the $f_i$.
\end{definition}

\begin{definition}[Negative cyclic CY class]
\label{def:negcyc-cy}
A \emph{$d$-dimensional CY structure} on a smooth dg category $\cC$ is a class
\[
 [\sigma] \in \HC^-_{d}(\cC)
\]
in the negative cyclic homology, whose image under the canonical map $\HC^- \to \HH$ is a non-degenerate trace $\Tr \colon \HH_d(\cC) \to k$. The lift to $\HC^-$ is essential for the $\bS^d$-framing used in Chapter~\ref{ch:cy-to-chiral}; see AP-CY2.
\end{definition}

\begin{theorem}[Cyclic $\Ainf$ enhancement]
\label{thm:cyclic-ainf-enhancement}
\ClaimStatusProvedElsewhere{}
Every smooth proper CY$_d$ category admits a cyclic $\Ainf$-enhancement, unique up to $\Ainf$-quasi-isomorphism preserving the pairing. The proof is due to Kontsevich--Soibelman in the formal case, Costello~\cite{Costello2005} for the TCFT enhancement, and Seidel~\cite{Seidel2008} for the Fukaya case.
\end{theorem}

At $d = 2$ the enhancement is explicit enough to compute directly; it drives the $K3$ computations feeding the Borcherds denominator (Vol~III Chapter~\ref{ch:k3}). At $d = 3$ the enhancement was constructed by Sheridan~\cite{Sheridan2015} for the quintic threefold, as part of the HMS proof; the general $d = 3$ construction remains programme-level (conditional on $\bS^3$-framing, see AP-CY6).
 succeeded in 51ms:
 \qquad a_1 \otimes \dots \otimes a_n \longmapsto \tfrac{1}{n!}\sum_{\sigma \in S_n} a_{\sigma(1)} \otimes \dots \otimes a_{\sigma(n)}
\]
is a morphism of cochain complexes and sends the $E_1$ structure to the $E_\infty$ structure. It is lossy: the kernel contains the $R$-matrix data of the holomorphic factor, and on degree two $\mathrm{av}(r(z)) = \kappa_{\mathrm{ch}}$.
\end{proposition}

Volume~I establishes the map; Volume~II identifies it as the $E_1 \to E_\infty$ symmetrization. For Volume~III purposes, the two consequences that matter are: (a) Yangians and quantum groups live on the $E_1$ side and are quotiented by averaging; (b) the symmetric bar $B^\Sigma$ is sufficient for computing the modular characteristic but insufficient for reconstructing the $R$-matrix.

Averaging the degree-two generator $r(z)$ returns the scalar $\kappa_{\mathrm{ch}}$, the unique $S_2$-coinvariant of the collision residue. When the same $r(z)$ comes from the CY-to-chiral functor applied to $D^b(\Coh(K3 \times E))$, the scalar is $\kappa_{\mathrm{ch}} = 3$ by additivity: $\kappa_{\mathrm{ch}}(K3) + \kappa_{\mathrm{ch}}(E) = 2 + 1$. This differs from the categorical Euler characteristic $\kappa_{\mathrm{cat}} = 2$, the lattice-rank invariant $\kappa_{\mathrm{fiber}} = 24$, and the BKM weight $\kappa_{\mathrm{BKM}} = 5$. An unsubscripted symbol would conflate distinct invariants.

\begin{remark}[Three bars, one functor]
\label{rem:three-bars-vol3}
The CY-to-chiral functor $\Phi$ of Chapter~\ref{ch:cy-chiral-functor} has three natural composites. $\Phi_{E_1}$ produces $B^{\mathrm{ord}}(A_C)$; this is the ordered bar sensed by the Yangian. $\mathrm{av} \circ \Phi_{E_1}$ produces $B^{\Sigma}(A_C)$; this is the symmetric bar sensed by the modular characteristic $\kappa_{\mathrm{ch}}$. The full $E_2$ enhancement $\Phi_{E_2}$ produces the Drinfeld-centered bar $B^{E_2}(A_C) = \cZ(B^{\mathrm{ord}}(A_C))$; this is the braided bar sensed by the quantum group. All three factor through $\Phi_{E_1}$. This is the volume's motto: the ordered bar is the primitive.
\end{remark}

\section{$E_1$-chiral algebras from CY categories}
\label{sec:e1-from-cy}

The CY input has to produce an ordered chiral object before any braided output can exist. For a CY$_d$ category $\cC$ in the sense of Kontsevich-Soibelman, the trace lives in $\mathrm{HC}^-_d(\cC)$, not merely in Hochschild homology, and that trace feeds the ordered $E_1$ structure first.

\begin{proposition}[$E_1$ sector at $d=2$]
 exited 2 in 51ms:
rg: frame: No such file or directory (os error 2)
chapters/examples/quantum_group_reps.tex:506: formula (Chapter~\ref{ch:toroidal-elliptic}; distinct from
chapters/examples/toric_cy3_coha.tex:208:(i) The compact base $\bP^1 \times \bP^1$ has $\chi(\bP^1 \times \bP^1) = 4$ (each factor contributes $\chi(\bP^1) = 2$), so $\kappa_{\mathrm{ch}} = \chi/2 = 2$ by the general local-surface formula (Remark~\ref{rem:toric-structural-patterns}).
chapters/examples/toric_cy3_coha.tex:657:(Theorem~\ref{thm:chiral-qg-equiv}) asserts that three of them
chapters/examples/toric_cy3_coha.tex:750:Theorem~\ref{thm:chiral-qg-equiv} of Vol~I, proved for any
chapters/examples/toric_cy3_coha.tex:758:(Theorem~\ref{thm:chiral-qg-equiv}(I)). For toric CY3, the
chapters/connections/cy_holographic_datum_master.tex:946:(Theorem~\ref{thm:cy-seven-face-master} above).
chapters/theory/cy_categories.tex:169:At $d = 2$ the enhancement is explicit enough to compute directly; it drives the $K3$ computations feeding the Borcherds denominator (Vol~III Chapter~\ref{ch:k3}). At $d = 3$ the enhancement was constructed by Sheridan~\cite{Sheridan2015} for the quintic threefold, as part of the HMS proof; the general $d = 3$ construction remains programme-level (conditional on $\bS^3$-framing, see AP-CY6).
chapters/theory/cy_categories.tex:197:Not every invariant of $\cC$ survives the passage through $\Phi$. The functor retains the cyclic $\Ainf$-structure and the Gerstenhaber bracket; it loses the fine structure of the triangulated / $\Ainf$ category (individual objects, t-structures, stability conditions) that is visible only via the fuller categorical CoHA construction of Chapter~\ref{ch:coha}. The kappa-spectrum (Vol~III CLAUDE.md) encodes which invariants survive: $\kappa_\mathrm{cat}$ is always present, $\kappa_\mathrm{ch}$ exists only when $\Phi$ is defined, and $\kappa_\mathrm{BKM}$ records the Borcherds-side lift for $K3 \times E$.
chapters/frame/preface.tex:323:(Theorem~\ref{thm:miura-cross-universality}).
chapters/frame/preface.tex:331:\S\ref{sec:e1-chiral-bialgebra}) require: (H1)~an $E_1$-chiral
chapters/connections/modular_koszul_bridge.tex:237:Parts (i), (iii), (iv) are Vol~I/II results (\S\ref{sec:k3e-cross-volume}, items K3-1 through K3-13, proved in the K3 modular-tower chapter of Vol~I and in the Vol~II 3D quantum gravity treatment, \ref{part:3d-qg} there). Part (ii) is the Borcherds lift of Borcherds (1998); its use as a modular characteristic is the observation of AP-CY8, not a theorem of Vol~III. The conditionality on propagates from Theorem~\ref{thm:cy-shadow-cohft}.
chapters/theory/drinfeld_center.tex:729:Theorem~\ref{thm:e1-stabilization}).
chapters/theory/en_factorization.tex:8:The answer is Bott periodicity. The framing obstruction lives in $\pi_d(BU)$ or $\pi_d(BO)$ or $\pi_d(B\Sp)$ depending on the parity and reduction of the structure group of the CY pairing. For the unitary path, $\pi_d(BU) = \Z$ when $d$ is even and vanishes when $d$ is odd. For the symplectic/orthogonal path, the 8-fold periodicity of the classical groups produces a richer pattern, with refinements at $d \equiv 5 \pmod 8$. The main result of this chapter (Theorem~\ref{thm:e1-stabilization-cy}) assembles these obstruction computations into a single statement: the framing obstruction is trivial precisely when $d \bmod 8 \in \{1, 3, 7\}$, and the CY chiral algebra is $\Eone$-stabilized with additional shifted structure controlled by $\pi_d(BU)$ elsewhere.
chapters/theory/en_factorization.tex:70:\label{thm:e1-stabilization-cy}
chapters/theory/en_factorization.tex:155:Parts~(i) and~(ii) follow from Theorem~\ref{thm:e1-stabilization-cy} at $d = 4$. For part~(ii), the three paths:
chapters/theory/en_factorization.tex:186:Parts~(i)--(iii) follow from Theorem~\ref{thm:e1-stabilization-cy} at $d = 5$, using the Bott periodicity table: $\pi_4(\Sp) = \Z_2$ (verified independently via the computation $\pi_4(\Sp) = \pi_4(\Sp(4)) = \Z_2$ in the stable range).
chapters/theory/en_factorization.tex:322:The $\Eone$ stabilization theorem (Theorem~\ref{thm:e1-stabilization-cy}) concerns the CY-to-chiral functor $\Phi$ and shows that $d \geq 3$ produces at most $\Eone$-chiral algebras. A distinct source of higher $\En$ structure exists: the holomorphic Chern--Simons programme of Costello and Costello--Francis--Gwilliam, where the $\En$ level is set by the \emph{complex dimension of the ambient space}, not by the CY dimension of the category. The ambient $E_3$ structure on $\C^3$ does not contradict $\Eone$ stabilization: it is a structure on the \emph{observables of the field theory}, not on the CY chiral algebra $\Phi(\cC)$. The two are related by the bulk-boundary correspondence (Vol~I Theorem~H, Vol~II bulk-boundary duality), but they live on different objects.
chapters/theory/en_factorization.tex:434:Theorem~\ref{thm:zte-failure} proves that the $E_3$ coherence condition is \emph{genuinely nontrivial}: the na\"ive factorization $S_{ijk} = R_{ij} R_{ik} R_{jk}$ from pairwise Yang--Baxter solutions does \emph{not} produce a tetrahedron solution. The correct $3$-particle $S$-operator for $U_{q,t}(\widehat{\widehat{\fgl}}_1)$ must include corrections beyond the pairwise product, controlled by the $E_3$ structure of holomorphic Chern--Simons on $\C^3$. At the level of the $A_\infty$ bar complex, these corrections are the shadow tower contributions $\delta^{(k)}$ from the higher operations $m_k$ (Section~\ref{sec:e1-chiral-bialgebras}).
chapters/theory/en_factorization.tex:824:At $n = 1$ this is Vol~II; at $n = 2$ this is Conjecture~\ref{conj:e2-koszul} (proved for the Heisenberg in Theorem~\ref{thm:e2-koszul-heisenberg}); at $n = 3$ this is Conjecture~\ref{conj:e3-koszul-duality} (conditional on CY-A$_3$). For $n \geq 4$, any CY chiral algebra that exists is $\Eone$-stabilized (Theorem~\ref{thm:e1-stabilization-cy}), so the cascade terminates at $n = 3$ for CY-geometric inputs.

thinking
**Considering cross-volume editing**

This task involves cross-volume conventions, which may not be high-risk, but I see that AGENTS advise using `vol3-pre-edit-verification` before making any edits to cross-volume parts. So, it's clear I need to proceed with care and use the necessary skills. I'll ensure I open the SKILL just enough to tackle this effectively. Let’s go ahead and do that!
codex
Before I patch, I’m running the repo’s pre-edit verification discipline because a few of these fixes touch cross-volume Part references and theorem/conjecture anchors. That keeps the edits minimal and prevents “fixing” a broken ref by pointing it at the wrong object.
exec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/vol3-pre-edit-verification/SKILL.md" in /Users/raeez/calabi-yau-quantum-groups succeeded in 51ms:
---
name: vol3-pre-edit-verification
description: Use before editing any high-risk Vol III formula, theorem status, d=3 existence claim, compute oracle, or cross-volume convention bridge. This is the Codex-native analogue of the Claude-side pre-edit verification templates.
---

# Vol III Pre-Edit Verification

Before editing a high-risk surface, fill in a fenced `PRE-EDIT` block in commentary and end with `verdict: ACCEPT` or `verdict: REJECT`.

If a required source is blank or any boundary check fails, do not edit yet.

## Triggers

- `r`-matrix or OPE/lambda-bracket edit
- `kappa` or modular-characteristic edit
- bar/cobar/desuspension formula
- theorem environment or claim-status edit touching d=3 objects
- shadow-class or SC-formality edit
- `MF(W)` CY-dimension edit
- cross-volume Part reference or copied formula
codex
```text
## PRE-EDIT: cross-volume refs
object: broken `\ref` calls to Vol I/II parts/sections/theorems and stale in-volume alias labels
source: live labels in `main.tex` input graph; current undefined-ref set from `make fast` (26 unresolved refs after 4 passes)
boundary checks: only retarget to an existing in-volume label when the object is the same surface; otherwise replace `\ref` with plain cross-volume prose or existing chapter labels
wrong variants avoided: inventing new theorem labels for Vol I/II material; pointing a cross-volume theorem ref at a similarly named but different Vol III object
verdict: ACCEPT
```

```text
## PRE-EDIT: d=3 status
statement: `thm:cy-seven-face-master` is referenced as a theorem, but the live object in `cy_holographic_datum_master.tex` is `conj:cy-seven-face-master`
depends on unconstructed object?: yes, the statement is conditional on CY-A_3 in the live text
environment: conjecture
claim status: conjectural; no strengthening permitted
dependency chain: live label scan -> `\label{conj:cy-seven-face-master}` in the section "The seven-face master theorem in the CY setting"
verdict: ACCEPT
```

thinking
**Considering subsection references**

I think I could add a label like `subsec:ddca-toroidal-bridge` and refer to that existing subsection. It makes sense to mention it clearly, so I might say something like, "in the DDCA--toroidal bridge subsection." Doing this could help clarify where the information is found, and I want to ensure that the user has the best understanding possible. It's all about making things clearer and more organized!
exec
/bin/zsh -lc "sed -n '1438,1460p' chapters/theory/e1_chiral_algebras.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "sed -n '2468,2480p' chapters/examples/toroidal_elliptic.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "sed -n '4928,5055p' chapters/examples/toroidal_elliptic.tex" in /Users/raeez/calabi-yau-quantum-groups succeeded in 51ms:
  \int_{U_1} \cF \;\otimes_{\int_{N \times \R} \cF}\;
  \int_{U_2} \cF.
\]
No mode expansion or Miura-type factorization is needed:
the excision gluing data is carried by the cosheaf structure of $\cF$
on $\Ran(\C^3)$.

\medskip
\noindent\textbf{(2) $K3 \times E$: the $E$-direction coproduct from
cutting the elliptic curve.}
For the product CY$_3$ manifold $X = K3 \times E$, the factorization
homology integral $\int_{K3} \cF|_{K3}$ of
Section~\ref{sec:k3-perturbative-fact-homology} produces a chiral algebra
$A_E$ on the residual elliptic curve $E$.  The coproduct on $A_E$ arises
from cutting $E$ into two intervals via excision.  Concretely, choose a
collar-gluing decomposition $E = I_1 \cup_{S^0 \times \R} I_2$ (cutting
$E$ at two points into two intervals $I_1, I_2$ with collar
neighbourhoods).  The excision equivalence gives
\begin{equation}\label{eq:k3xe-excision-coproduct}
  \int_E A_E \;\simeq\;
 succeeded in 51ms:
vanishes: $\mathrm{vdim} = -\chi(\cE,\cE) = 0$.
\end{proposition}

\subsection{Factorization homology}
\label{subsec:fact-homology-k3xe}

\begin{remark}[Factorization homology on $K3 \times E$]
\label{rem:fact-homology-k3xe}
\index{factorization homology!K3 x E}
The factorization homology of the HT-twisted sigma model:
$\int_{K3 \times E} A^{\mathrm{HT}} \simeq
H^*(K3 \times E,\, \Omega^{\mathrm{ch}})$.
The CDR character gives $\chi(\Omega^{\mathrm{ch}}) = 0$, but the
 succeeded in 51ms:
\label{rem:k3e-rank0}
At rank $0$ (curve class $\beta = 0$), the DT theory of $K3 \times E$ reduces to the MacMahon function weighted by $q^{1/24} \prod_{n \geq 1}(1 - q^n)^{-24}$, i.e.\ the reciprocal of $\eta(q)^{24} / q$. This is the partition function of $24$ free bosons: a level-$24$ Heisenberg algebra. The rank-$0$ sector is thus controlled by $\cH_{24}$, with $\kappa_{\mathrm{ch}}(\cH_{24}) = 24$.
\end{remark}

\begin{theorem}[Yangian via MO $R$-matrix]
\label{thm:k3e-yangian}
\ClaimStatusProvedElsewhere
The braided monoidal structure on $\Rep^{E_2}(G(K3 \times E))$ is governed by the Maulik--Okounkov $R$-matrix of the affine Yangian $Y(\widehat{\mathfrak{g}}_{\Delta_5})$. This Yangian acts on the equivariant cohomology of the Hilbert scheme of curves on $K3 \times E$ and satisfies the CY involution
\[
 g(z) \, g(-z) = 1
\]
where $g(z) = 1 + \sum_{n \geq 1} g_n z^{-n}$ is the generating series of Yangian generators.
\ClaimStatusProvedElsewhere
\end{theorem}

\begin{remark}[CY involution]
\label{rem:k3e-cy-involution}
The functional equation $g(z)g(-z) = 1$ is the Yangian-level manifestation of the CY$_3$ Serre duality $\Ext^i(E,F) \simeq \Ext^{3-i}(F,E)^*$. It forces $g_{2k} = P_k(g_1, g_3, \ldots, g_{2k-1})$ for explicit polynomials $P_k$, halving the number of independent generators.
\end{remark}

exec
/bin/zsh -lc "rg -n '12, 24|12\\}|24\\}|trichotomy|alternative algebraization|three algebraizations|Monster orbifold|moonshine multiplier' chapters/examples/toroidal_elliptic.tex -S" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "sed -n '1960,1995p' chapters/theory/cy_to_chiral.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "sed -n '486,520p' chapters/examples/quantum_group_reps.tex" in /Users/raeez/calabi-yau-quantum-groups succeeded in 52ms:
131:\item The Arnold relation $K_{12}K_{23} + K_{23}K_{31} + K_{31}K_{12} = 0$ (Fay identity) specializes the CYBE to the elliptic regime.
241:\sigma_{12} \circ \mu(e_i(z), e_j(w))
516:the $2$-form $\eta_{12}^{\mathrm{ell}} \wedge \eta_{23}^{\mathrm{ell}}
518:+ \eta_{31}^{\mathrm{ell}} \wedge \eta_{12}^{\mathrm{ell}}$,
522:The rational Arnold relation $\eta_{12} \wedge \eta_{23}
523:+ \eta_{23} \wedge \eta_{31} + \eta_{31} \wedge \eta_{12} = 0$
575:$\eta_{12} \wedge \eta_{23} + \eta_{23} \wedge \eta_{31} +
576:\eta_{31} \wedge \eta_{12} = 0$
590:\eta_{12} = d\log\theta(z_1 - z_2 | \tau)
596:d_{\text{res}}([a|b] \otimes \eta_{12}) = \sum_{\theta(z_0) = 0} \Res_{z_1 = z_0 + z_2}[\cdots]
823:[a_m | a_n] \otimes \eta_{12}^{\mathrm{ell}}
826:where $\eta_{12}^{\mathrm{ell}} = \zeta_\tau(z_1 - z_2)\,(dz_1 - dz_2)$.
829:d^{\mathrm{ell}}([a_m | a_n] \otimes \eta_{12}^{\mathrm{ell}})
831:a_m(z_1)\,a_n(z_2)\,\eta_{12}^{\mathrm{ell}}
877:d^{\mathrm{ell}}([a_m | a_n] \otimes \eta_{12}^{\mathrm{ell}})
945:$7$ & $0$ & $-\frac{1382\kappa_{\mathrm{ch}}\pi^{12}}{638512875}\,E_{12}(\tau)$
946:& $E_{12}(\tau)$ (modular, wt~$12$) \\
1063:R_{12}(u, \lambda)\,
1069:R_{12}(u, \lambda - h^{(3)})
1264:d([L_{ij}(u) | L_{kl}(v)] \otimes \eta_{12}^{\mathrm{ell}})
 succeeded in 51ms:
 \toprule
 \textbf{CY variety} & $\chi_{\mathrm{top}}/24$ & $\kappa_{\mathrm{ch}}$ & \textbf{Match?} \\
 \midrule
 Elliptic curve $E$ ($\CY_1$) & $0$ & $1$ & No \\
 K3 surface ($\CY_2$) & $1$ & $2$\rlap{$^*$} & No \\
 $K3 \times E$ ($\CY_3$) & $0$ & $3$\rlap{$^\dagger$} & No \\
 Resolved conifold & $1/12$ & $1$ & No \\
 Local $\bP^2$ & $1/8$ & $3/2$ & No \\
 \midrule
 Quintic ($\chi = -200$) & $-25/3$ & $-25/3$ & Yes \\
 $\bP^5[3,3]$ ($\chi = -144$) & $-6$ & $-6$ & Yes \\
 $\bP^5[2,4]$ ($\chi = -176$) & $-22/3$ & $-22/3$ & Yes \\
 \bottomrule
\end{tabular}
\end{center}
{\footnotesize $^*$The K3 entry records $\kappa_{\mathrm{ch}} = \chi(\cO_{\mathrm{K3}}) = 2$ (Proposition~\ref{prop:cy-kappa-d2}; verified via chiral de Rham, Chapter~\ref{ch:k3-times-e}). The distinct quantity $\dim \HH_*(D^b(\mathrm{K3}))/2 = 12$ arises from an alternative algebraization (the Monster orbifold); the full trichotomy ($\kappa_{\mathrm{ch}} \in \{2, 12, 24\}$) is developed in Section~\ref{subsec:k3-three-algebraizations} of Chapter~\ref{ch:k3-times-e}.

$^\dagger$The $K3 \times E$ entry records $\kappa_{\mathrm{ch}} = 3$ by additivity (Proposition~\ref{prop:categorical-euler}: $\kappa_{\mathrm{ch}}(\mathrm{K3}) + \kappa_{\mathrm{ch}}(E) = 2 + 1$). The Borcherds automorphic weight is $\kappa_{\mathrm{BKM}} = 5 = \mathrm{wt}(\Delta_5)$, a distinct invariant.}

\smallskip
 succeeded in 51ms:
 \bottomrule
\end{tabular}
\end{center}
%: kappa != S_2 for non-Virasoro families.
%: each formula recomputed from dim(g)(k+h^v)/(2h^v).
\end{proposition}

\begin{remark}[$\kappa_{\mathrm{cat}}$ versus other invariants]
\label{rem:kappa-cat-vs-others}
Three distinct invariants must be distinguished:
\begin{enumerate}[label=(\roman*)]
 \item $\kappa_{\mathrm{cat}}$: the modular characteristic of the
 CY category, equal to the genus-$1$ Hodge class coefficient of
 the associated chiral algebra (Volume~I, Theorem~D);
 \item $\kappa_{\mathrm{ch}}$: the modular characteristic computed
 from the chiral algebra directly (may differ from
 $\kappa_{\mathrm{cat}}$ when the CY-to-chiral functor involves
 additional data);
 \item $\kappa_{\mathrm{BKM}}$: the BKM modular weight, a
 number-theoretic invariant arising from the BKM denominator
exec
/bin/zsh -lc "sed -n '6008,6030p' chapters/examples/toroidal_elliptic.tex" in /Users/raeez/calabi-yau-quantum-groups succeeded in 52ms:
\item \textup{(Coassociativity with shifted parameters.)}
  $(\Delta_{z_1,w_1} \otimes \id) \circ
  \Delta_{z_1+z_2,\, w_1+w_2}
  = (\id \otimes \Delta_{z_2,w_2}) \circ
  \Delta_{z_1,w_1}$.
\item \textup{(Miki equivariance.)}
  The Miki automorphism $S$ exchanges the two spectral
  parameters:
  $S \circ \Delta_{z,w} = \Delta_{w,z} \circ S$.
\item \textup{(Degeneration.)}
  At $t \to 1$: the second parameter $w$ decouples and
  $\Delta_{z,w}$ reduces to the single-parameter
  Drinfeld coproduct $\Delta_z(T(u)) = T(u) \otimes T(u - z)$
  of Theorem~\textup{\ref{thm:w-infty-chiral-qg}}.
\end{enumerate}
No two-parameter coproduct $\Delta_{z,w}$ currently exists in
the literature or in this programme's compute infrastructure.
The conjecture is formulated from the structural requirement
that the $\bC^* \times \bC^*$ equivariance of the toric CY$_3$
action extend to the coalgebra level.
exec
/bin/zsh -lc "sed -n '410,450p' chapters/examples/toric_cy3_coha.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "sed -n '650,690p' chapters/examples/toric_cy3_coha.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n 'Drinfeld coproduct|Delta_z|single-parameter|W_\\{1\\+\\\\infty\\}|chiral quantum group equivariance|equivariance theorem' chapters/examples/toric_cy3_coha.tex -S" in /Users/raeez/calabi-yau-quantum-groups succeeded in 51ms:
these components into a single chiral quantum group structure for
all toric CY3 without compact $4$-cycles. For $\C^3$ the
five-step functor chain (Theorem~\ref{thm:c3-functor-chain}) verifies
every step end-to-end; the general toric case inherits the algebraic
structure from the RSYZ identification and the chart-gluing theorem,
with the Drinfeld center identification conditional on Conjecture~CY-C
outside $\C^3$.

\begin{theorem}[Chiral quantum group structure for toric CY3]
\label{thm:toric-cy3-chiral-qg}
\ClaimStatusProvedHere{}
Let $X = X_\Sigma$ be a smooth toric CY3 without compact $4$-cycles,
with toric quiver with potential $(Q_X, W_X)$.
The following five-component chiral quantum group datum
$\mathcal{G}(X)$ exists and is uniquely determined by the
toric fan $\Sigma$:
\begin{enumerate}[label=\textup{(\Roman*)}]
 \item \textbf{$\Eone$-bialgebra \textup{(}CoHA\textup{)}.}
  The critical CoHA
  \[
 succeeded in 51ms:
220:The 5d holomorphic Chern--Simons theory on a toric CY3 $X$ realizes the CoHA physically and connects Feynman diagrams, shuffle algebras, and $\cW_{1+\infty}$.
229: \item \emph{$\cW_{1+\infty}$ algebra}: the Miura transform identifies the mode algebra of $\cW_{1+\infty}$ at the self-dual level $\psi = 1$ with the Yangian $Y(\widehat{\fgl}_1)$, hence with the CoHA.
364:in the context of $\cW_{1+\infty}$ at the self-dual level.
482:  For $\C^3$: $Y(\widehat{\fgl}_1) \simeq \cW_{1+\infty}$
634:  \simeq \Rep^{\Etwo}(\cW_{1+\infty})$. For general toric
636: \item The output algebra $\cW_{1+\infty}$ has a vertex algebra
830:  \simeq \cW_{1+\infty}$
 succeeded in 51ms:
of the chiral quantum group datum for toric CY3 without compact
$4$-cycles. The components are proved independently: the CoHA
bialgebra by Schiffmann--Vasserot and RSYZ, the $R$-matrix by
Maulik--Okounkov, the Drinfeld double by triangular decomposition,
the chart gluing by descent, the shadow tower by the MC equation.
These components are \emph{a priori} separate structures on the
same algebra. The Vol~I chiral quantum group equivalence
(Theorem~\ref{thm:chiral-qg-equiv}) asserts that three of them
(the vertex $R$-matrix, the chiral $A_\infty$-structure, and the
chiral coproduct) determine each other on the Koszul locus. The theorem
below specializes the abstract equivalence to the toric CY3 setting,
where both sides are independently known, yielding the strongest
unconditional statement: the RSYZ bialgebra coproduct, the MO
$R$-matrix, and the bar-differential $A_\infty$-structure are three
faces of a single object.

\begin{theorem}[Chiral quantum group equivalence for toric CY3]
\label{thm:toric-chiral-qg-specialization}
\ClaimStatusProvedHere{}
Let $X = X_\Sigma$ be a smooth toric CY3 without compact $4$-cycles,
exec
/bin/zsh -lc "rg -n '\\\\Delta_z\\(|T\\(u\\) \\\\otimes T\\(u - z\\)|single-parameter|Drinfeld coproduct' chapters/examples/toric_cy3_coha.tex chapters/theory/*.tex -S" in /Users/raeez/calabi-yau-quantum-groups succeeded in 52ms:
chapters/theory/quantum_chiral_algebras.tex:431:The level $\Psi = -\sigma_2$ is a scalar extracted from the full Omega-background: it is the residue of the classical $r$-matrix $r(u) = -\sigma_2/u$ of the affine Yangian (holomorphic\_cs\_chiral\_engine.py, line~127). The passage from the two-parameter $R$-matrix $R_{\mathrm{ch}}(u, v)$ of Conjecture~\ref{conj:chiral-qg-c3}(ii) to the single-parameter Yangian $R$-matrix is the projection $\C^3 \to \C^2$; the further projection $\C^2 \to C$ forgets the spectral parameter entirely, leaving only the defect algebra with its level $\Psi$.
chapters/theory/e1_chiral_algebras.tex:222: $R$-matrix, the Hopf structure, and the Drinfeld coproduct all
chapters/theory/e1_chiral_algebras.tex:247:$R$-matrix $R(z)$ and Drinfeld coproduct $\Delta_z$. The forgetful
chapters/theory/e1_chiral_algebras.tex:1130:Let $A = W_{1+\infty}$ at level $\Psi$ with transfer matrix $T(u) = \sum_{s \geq 0} (-1)^s \psi_s \, u^{-s}$, where $\psi_s = e_s(\phi_1, \ldots, \phi_N)$ is the $s$-th elementary symmetric polynomial in the free bosons. The Miura coproduct $\Delta_z(T(u)) = T_L(u) \cdot T_R(u - z)$ gives:
chapters/theory/e1_chiral_algebras.tex:1132: \Delta_z(\psi_s) \;=\; \sum_{\substack{a + b + k = s \\ a, b, k \geq 0}} (-1)^k \binom{N_R - b}{k} z^k \, \psi_a^L \cdot \psi_b^R.
chapters/theory/e1_chiral_algebras.tex:1227:= \sum \Delta_z(a)_{(2)} \cdot n \otimes \Delta_z(a)_{(1)}$
chapters/theory/e1_chiral_algebras.tex:1234:= \sum S(\Delta_z(a)_{(1)}) \cdot n \otimes \Delta_z(a)_{(2)}$,
chapters/theory/e1_chiral_algebras.tex:1257: \item Coproduct: $\Delta_z(J) = J \otimes 1 + 1 \otimes J$ (primitive).
chapters/theory/e1_chiral_algebras.tex:1279: transfer matrix), $\Delta_z(T(u)) = T(u) \otimes T(u)$
chapters/theory/e1_chiral_algebras.tex:1283: $\Delta_z(W_n) = W_n \otimes 1 + K_{\mathcal{A}}(z) \otimes W_n + \ldots$
chapters/theory/e1_chiral_algebras.tex:1521:  the $\Eone$-sector, coincides with the Drinfeld coproduct
chapters/theory/e1_chiral_algebras.tex:1524:  and gauge algebra $\fgl_1$, the Drinfeld coproduct on the affine
chapters/theory/e1_chiral_algebras.tex:1534:Yangian specifically, the Drinfeld coproduct is constructed
exec
/bin/zsh -lc "sed -n '1120,1140p' chapters/theory/e1_chiral_algebras.tex" in /Users/raeez/calabi-yau-quantum-groups succeeded in 52ms:
 + \hbar^2 \cdot \delta^{(3)}(T)
 + \hbar^3 \cdot \delta^{(4)}(T)
 + \cdots
\]
where $\delta^{(k)}$ is the correction from the $A_\infty$ operation $m_k$, with coefficient equal to the shadow invariant $S_k$. Concretely (\texttt{a\_infinity\_bar\_w1inf.py}): $m_3(T,T,T) = -2T$ gives $\delta^{(3)}$ with coefficient $\alpha = 2$; $m_4(T,T,T,T) = \tfrac{40}{27}T$ gives $\delta^{(4)}$ with coefficient $S_4 = \tfrac{10}{27}$. For class~$G$ (Heisenberg): all $m_k = 0$ for $k \geq 3$, so the truncation is exact. For class~$L$ (Yangian): $S_4 = 0$, so the truncation terminates at finite depth. For class~$M$ (Virasoro): all $S_k \neq 0$, and the coproduct has genuinely infinite complexity. The shadow tower is therefore not merely a classification invariant: it encodes the $A_\infty$ corrections to the chiral coproduct.
\end{remark}

\begin{proposition}[Universal coproduct formula from the Miura factorization]
\label{prop:universal-coproduct}
\ClaimStatusProvedHere{}
Let $A = W_{1+\infty}$ at level $\Psi$ with transfer matrix $T(u) = \sum_{s \geq 0} (-1)^s \psi_s \, u^{-s}$, where $\psi_s = e_s(\phi_1, \ldots, \phi_N)$ is the $s$-th elementary symmetric polynomial in the free bosons. The Miura coproduct $\Delta_z(T(u)) = T_L(u) \cdot T_R(u - z)$ gives:
\[
 \Delta_z(\psi_s) \;=\; \sum_{\substack{a + b + k = s \\ a, b, k \geq 0}} (-1)^k \binom{N_R - b}{k} z^k \, \psi_a^L \cdot \psi_b^R.
\]
The coproduct at spin $s$ is a polynomial in $z$ of degree exactly $s$, with $\tfrac{s(s+1)}{2}$ operator-product terms. The number of terms at $z$-power $p$ is $N(s,p) = s - p$, with generating function
\[
 F(x,y) \;=\; \sum_{s \geq 1} \sum_{p=0}^{s-1} N(s,p) \, x^s y^p \;=\; \frac{x}{(1-x)^2(1-xy)}.
\]
The leading $z^{s-1}$ coefficient is $\psi_1^R = J^R$ (single term). The subleading $z^{s-2}$ coefficient is $(s-1)\psi_2^R + \sum_k J_k^L J_{n-k}^R$ (universal at all spins).
\end{proposition}
exec
/bin/zsh -lc "sed -n '612,660p' chapters/theory/cy_to_chiral.tex" in /Users/raeez/calabi-yau-quantum-groups succeeded in 52ms:
 s^2 = 0, \qquad
 s \circ i = 0, \qquad
 p \circ s = 0,
\]
where $i \colon H^*(\check{C}^\bullet) \hookrightarrow \check{C}^\bullet$
is the inclusion of cohomology and $p$ is the projection. The contracting
homotopy is purely algebraic: it acts by
$s(f_{i_0 \cdots i_q}) = f_{0 i_0 \cdots i_q}$ on \v{C}ech cochains and
involves no PDE solving. The SDR data $(i, p, s)$ interfaces directly
with the homotopy transfer theorem
\textup{(}HTT, Theorem~\textup{\ref{thm:htt-general}}\textup{)},
transferring the $\Ainf$-structure from $\check{C}^\bullet(\cE nd(\cE))$
to its cohomology $\Ext^\bullet(\cE, \cE)$.
\end{theorem}

\begin{proof}
The \v{C}ech complex of a quasi-coherent sheaf on $\bP^4$ with respect
to the standard affine cover $\{U_i\}_{i=0}^4$ is acyclic in positive
\v{C}ech degree (Leray's theorem: each finite intersection
$U_{i_0} \cap \cdots \cap U_{i_q}$ is affine, and affine varieties
exec
/bin/zsh -lc "sed -n '452,505p' chapters/examples/k3_times_e.tex" in /Users/raeez/calabi-yau-quantum-groups succeeded in 52ms:
\label{warn:k3e-chi-kappa}
The topological Euler characteristic $\chi_{\mathrm{top}}(K3 \times E) = \chi(K3) \cdot \chi(E) = 24 \cdot 0 = 0$ vanishes because $\chi(E) = 0$. However, the CY Euler characteristic relevant to the modular characteristic is the \emph{holomorphic} (or motivic) Euler characteristic
\[
 \chi^{\CY}(K3 \times E) = \sum_{p,q} (-1)^{p+q} h^{p,q}(K3 \times E) \cdot (\text{weight factor}),
\]
which accounts for the Hodge filtration. The formula $\kappa_{\mathrm{ch}} = \chi_{\mathrm{top}}/24$ already \emph{fails} for $E$ and K3 individually: $\chi_{\mathrm{top}}(E)/24 = 0$ but $\kappa_{\mathrm{ch}}(E) = 1$; $\chi_{\mathrm{top}}(K3)/24 = 1$ but $\kappa_{\mathrm{ch}}(K3) = 2$ (Proposition~\ref{prop:chi-kappa-discrepancy}). It also fails for $K3 \times E$ against both modular invariants:
\[
 \frac{\chi_{\mathrm{top}}(K3 \times E)}{24} = 0 \neq 3 = \kappa_{\mathrm{ch}}(K3 \times E), \qquad
 0 \neq 5 = \kappa_{\mathrm{BKM}}(K3 \times E).
\]
The correct chiral value $\kappa_{\mathrm{ch}} = 3$ comes from additivity ($\kappa_{\mathrm{ch}}(K3) + \kappa_{\mathrm{ch}}(E) = 2 + 1$), while $\kappa_{\mathrm{BKM}} = 5$ comes from the Borcherds lift weight $c(0)/2$ (Proposition~\ref{thm:k3e-fiber-global}). Neither is determined by the topological Euler characteristic.
\end{warning}

\noindent\textit{Verification}: 86 tests in \texttt{k3e\_coha\_structure.py} (G1 subsuite) covering $\chi/24$ vs $\kappa_{\mathrm{ch}}$ comparison for $K3$, $E$, $K3 \times E$, and all eight $X_N$ families.


\subsection{The three algebraizations of K3}
\label{subsec:k3-three-algebraizations}

% FOUR OBJECTS:

thinking
**Searching for algebraizations**

I need to find an equivalent section in toroidal elliptic, but it might not be included. I'm thinking about searching for terms like "trichotomy" or "three algebraizations" within the toroidal context. There's a lot to unpack here, and I want to ensure I’m looking in the right areas for relevant information. Let’s see if these terms yield any useful results related to what I’m trying to find.
exec
/bin/zsh -lc "rg -n 'three algebraizations|trichotomy|Monster orbifold|Leech lattice|V\\"'^'"\\\\natural|V_\\\\Lambda|24\\} are pairwise distinct|modular characteristics \\"'$2'"\\"'$, '"\\"'$12'"\\"'$, '"\\"'$24'"\\"'$'"' chapters/examples/toroidal_elliptic.tex -S" in /Users/raeez/calabi-yau-quantum-groups succeeded in 52ms:
2299:$V_\Lambda$ with $\Lambda$ determined by the fiber cohomology
2301:theorem, $\kappa_{\mathrm{ch}}(V_\Lambda) = \mathrm{rank}(\Lambda)$ for any
2322:$\kappa_{\mathrm{ch}}(V_\Lambda) = \mathrm{rank}(\Lambda)$ for all lattice VAs
2817:\index{Leech lattice!K3 connection}
2820:Leech lattice VOA $V_\Lambda$ through order $q^1$:
2822:$V_\Lambda$ has $\dim (V_\Lambda)_1 = 0$ and
2823:$\dim (V_\Lambda)_2 = 196560$. The two diverge at
2824:order~$q^2$: the $196560$ vectors of the Leech lattice have
2827:The Leech lattice has $\kappa_{\mathrm{ch}}(V_\Lambda) = 24 = \kappa_{\mathrm{ch}}(A_E)$
3427: $V^\natural$ ($c = 24$, $\kappa_{\mathrm{ch}}(V^\natural) = 12$ by
3430: Leech lattice construction):
3431: does $A_n^{\text{Monster}} = \kappa_{\mathrm{ch}}(V^\natural) \cdot
3442: The Conway group $Co_0$ acts on the Leech lattice;
3735:\item \emph{The Leech divergence.} The Leech lattice
3743: structure of the Leech lattice VOA beyond free fields.
exec
/bin/zsh -lc "sed -n '352,366p' chapters/theory/introduction.tex" in /Users/raeez/calabi-yau-quantum-groups succeeded in 53ms:
 tower. This would give the left adjoint of the modular
 primitive-current functor.
\item \emph{BKM algebras and scattering diagrams.}
 The Gross--Siebert scattering diagram consistency condition
 IS the $E_1$ Maurer--Cartan equation
 (Theorem~\ref{thm:scattering-mc}). The programme: lift
 this identification to the full motivic Hall algebra level
 (where naive BCH is insufficient).
\item \emph{Descent theorem.}
 \v{C}ech descent for $E_1$-algebras over the Bridgeland
 stability manifold. Proved for toric CY3
 (Proposition~\ref{prop:e1-descent-unobstructed}); open for
 compact CY3 beyond the chart-atlas regime.
\item \emph{Higher-dimensional CY shadows.}
 The $E_n$ stabilization theorem

thinking
**Exploring descent degeneration**

I'm noticing that the local theorem about E1 descent degeneration is applied generally, not just in toric contexts. There’s also a theorem regarding toric chart gluing, which might be focused more on toric Calabi-Yau threefolds. It sounds like I should search around the year 1121 to find the statement of that theorem. There's definitely more to unpack here, and I'm curious to see how these theorems connect!
exec
/bin/zsh -lc "sed -n '1116,1148p' chapters/theory/cy_to_chiral.tex" in /Users/raeez/calabi-yau-quantum-groups succeeded in 53ms:
The conjecture asserts two structural claims. First, the transition mutations induce $\Eone$-algebra maps between the CoHAs, so the diagram is well-defined. Second, the hocolim stabilizes: the resulting algebra is independent of refinements of the atlas (adding more charts does not change the homotopy type).

For general CY$_3$ categories, the conjecture chains through the Bridgeland finiteness conjecture (Conjecture~\ref{conj:tilting-chart-cover}). For toric CY$_3$ varieties, all ingredients are unconditional, and the construction is a theorem.

\begin{theorem}[Quiver-chart gluing for toric CY$_3$]
\label{thm:toric-chart-gluing}
\ClaimStatusProvedHere{}
Let $X = X_\Sigma$ be a smooth toric CY$_3$ variety with toric fan $\Sigma$. Then:
\begin{enumerate}[label=\textup{(\roman*)}]
 \item \textbf{Atlas.} The toric fan determines a quiver-chart atlas $\cA = \{(Q_\alpha, W_\alpha, \Psi_\alpha)\}_{\alpha \in \Sigma(3)}$ with $|\Sigma(3)|$ charts \textup{(}one per maximal cone\textup{)}, where each $(Q_\alpha, W_\alpha)$ is the McKay quiver with potential of the toric patch $\C^3/G_\alpha$, $G_\alpha \subset \SL(3,\C)$ finite abelian. The transition data is given by flop functors between adjacent patches, and the cocycle condition follows from the associativity of the toric fan. \textup{(}Remark after Conjecture~\textup{\ref{conj:tilting-chart-cover}; McKay correspondence: Bridgeland--King--Reid; flops: Bondal--Orlov.)}
 \item \textbf{Transitions.} Each wall-crossing mutation $\mu_{\alpha\beta}$ between adjacent charts induces an $\Eone$-algebra quasi-isomorphism $\mu_{\alpha\beta}^* \colon \CoHA(Q_\alpha, W_\alpha) \xrightarrow{\simeq_{E_1}} \CoHA(Q_\beta, W_\beta)$, so the hocolim diagram $\Sigma(3) \to \Eone\text{-}\mathrm{ChirAlg}$ is well-defined. \textup{(}Proposition~\textup{\ref{prop:mutation-e1-equivalence}.)}
 \item \textbf{Descent.} The $\Eone$ descent spectral sequence of the atlas degenerates at $E_2$ \textup{(}Theorem~\textup{\ref{thm:e1-descent-degeneration})}, so the homotopy colimit
 \begin{equation}
 \label{eq:toric-global-e1}
  A_{X_\Sigma} \;:=\; \operatorname{hocolim}_{\Sigma(3)} \CoHA(Q_\alpha, W_\alpha)
 \end{equation}
 is assembled from pairwise wall-crossing data alone, with no higher coherences required. The resulting $\Eone$-chiral algebra is independent of the choice of atlas refinement.
 \item \textbf{Costello--Li comparison.} There exists an $\Eone$ quasi-isomorphism
 \[
  \Psi \colon A_{X_\Sigma}^{\mathrm{hocolim}} \;\xrightarrow{\;\simeq_{E_1}\;}\; A_{X_\Sigma}^{\mathrm{CL}} \;=\; U^{\mathrm{ch}}(\mathfrak{L}_{X_\Sigma}),
exec
/bin/zsh -lc "sed -n '532,556p' chapters/theory/quantum_chiral_algebras.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "sed -n '938,952p' chapters/connections/cy_holographic_datum_master.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n 'R_\\{\\\\mathrm\\{ch\\}\\}\\(u, v\\)|two-parameter|6d|C\\"'^3.*R-matrix|spectral parameter.*v|R'"\\(u, v\\)' chapters/theory/quantum_chiral_algebras.tex -S" in /Users/raeez/calabi-yau-quantum-groups succeeded in 51ms:
\subsection{Chiral quantum groups from defect Wilson lines}
\label{subsec:chiral-qg-wilson}

The chiral quantum group is the Hopf-algebra-like structure on the defect algebra $A^!$ extracted from the holomorphic Wilson lines of the ambient CS theory.

\begin{conjecture}[Chiral quantum group on $\C^3$]
\label{conj:chiral-qg-c3}
\ClaimStatusConjectured
For the 6d holomorphic theory on $\C^3$ with $\fgl_1$ gauge algebra and Omega-background $(h_1, h_2, h_3)$:
\begin{enumerate}[label=\textup{(\roman*)}]
 \item The defect algebra $A^!_{\C^3}$ carries a coproduct
 \[
  \Delta_{\mathrm{ch}} \colon A^!_{\C^3} \;\longrightarrow\; A^!_{\C^3} \hat{\otimes} A^!_{\C^3}
 \]
 induced by the collision of two parallel Wilson lines in $\C^3$. The coproduct is coassociative and compatible with the $E_3$-chiral structure.
 \item The $R$-matrix is the universal braiding of the $E_3$ theory:
 \[
  R_{\mathrm{ch}}(u, v) \in A^!_{\C^3} \hat{\otimes} A^!_{\C^3}((u))((v))
 \]
 with $(u, v)$ the two spectral parameters from the two extra directions of $\C^3$ beyond the Wilson line. This $R$-matrix satisfies the parametric Yang--Baxter equation in \emph{two} spectral variables.
 succeeded in 51ms:
brace algebra, derived center, twisted holography boundary, line
defect, Wilson line $R$-matrix, soft graviton coupling, Yangian double
(cf.\ Vol~II, Theorem~\ref{thm:vol2-seven-face-master}).
\item \emph{Vol~III, this chapter:} the binary CY collision residue of a
Calabi--Yau chiral algebra, in seven CY-specific languages: CY
bar-cobar, CoHA / perverse coherent sheaves, classical CY Poisson
coisson, MO stable envelope, affine super Yangian for toric CY$_3$,
elliptic Sklyanin for toroidal CY, Gaudin from CY$_3$
(Theorem~\ref{thm:cy-seven-face-master} above).
\end{enumerate}
The three master theorems are mutually compatible: under the CY-to-chiral
functor $\Phi$, face~$i$ of Vol~III maps to a specialization of face~$i$
of Vol~I, and similarly for Vol~II. The CY setting is the most
constrained: each face acquires geometric content that the abstract
chiral algebra setting does not see (DT counts, plane partitions,
 succeeded in 51ms:
214: \item \emph{6d holomorphic theory on $\C^3$} (Costello~2017, ``M-theory in the Omega-background and 5-dimensional non-commutative gauge theory''; Costello--Francis--Gwilliam~2024, ``Chern--Simons theory and factorisation homology''):
219:\begin{remark}[6d theory is not standard holomorphic CS]
220:\label{rem:6d-not-lagrangian}
221:The 6d regime (iii) is not literally the holomorphic Chern--Simons action $S_{\mathrm{hCS}}$ on $\C^3$: for $\dim_\C M = 3$, the action requires a holomorphic $3$-form $\Omega$, but the kinetic term $\Omega \wedge A \wedge \dbar A$ produces a $(3,2)$-form, which is a top form on a $5$-real-dimensional space, not on $\C^3$ (real dimension $6$). The correct 6d formulation passes through either (a) the holomorphic twist of the 6d $(2,0)$ superconformal theory on the M5-brane worldvolume, or (b) the Costello--Li perturbative framework for partially holomorphic theories, or (c) the factorization homology formulation of Costello--Francis--Gwilliam applied to the $E_3$-algebra of local observables. Route~(c) is the most algebraic and is the one used here. The 3d and 5d cases are Lagrangian; the 6d case is non-Lagrangian.
235:\label{conj:6d-boundary-toroidal}
237:The $E_3$-factorization algebra of 6d holomorphic observables on $\C^3_{h_1, h_2, h_3}$ (with $h_1 + h_2 + h_3 = 0$, via the Costello--Francis--Gwilliam algebraic formulation), projected to an $\Eone$-chiral algebra on a curve $C \subset \C^3$, is the quantum toroidal algebra $U_{q,t}(\widehat{\widehat{\fgl}}_1)$ with parameters $q = e^{2\pi i h_1/h_3}$, $t = e^{-2\pi i h_2/h_3}$. The intermediate $\Etwo$-projection to $\C^2 \subset \C^3$ should recover the affine Yangian $Y(\widehat{\fgl}_1)$ of Theorem~\ref{thm:5d-boundary-yangian}; this compatibility between the 6d projection and the independent 5d construction is itself part of the conjecture. The $E_3$ structure on $\C^3$ is the \emph{source} of the second affinization (the second hat in $\widehat{\widehat{\fgl}}_1$); the first affinization comes from the $\Etwo$ factorization on $\C^2$.
292:In the 5d case ($M = \C^2 \times \R$), the universal defect algebra is the Koszul dual of the affine Yangian. For $\frakg = \fgl_1$, the defect algebra $A^!$ encodes the Wilson lines of the 5d theory; the RTT formalism applied to the defect $R$-matrix generates the dual Yangian presentation. (The quantum toroidal algebra arises from the \emph{6d} theory on $\C^3$, not from 5d; see Conjecture~\ref{conj:6d-boundary-toroidal}.) The Drinfeld center of the defect module category recovers the $\Etwo$ braided structure:
298:\begin{conjecture}[6d universal defect and chiral quantum groups on $\C^3$]
299:\label{conj:6d-defect-c3}
301:For the 6d holomorphic theory on $\C^3$ with gauge algebra $\fgl_1$, the universal defect algebra $A^!_{\C^3}$ (the Koszul dual of the quantum toroidal boundary algebra $U_{q,t}(\widehat{\widehat{\fgl}}_1)$) satisfies:
308:The conjecture composites three constructions (6d $E_3$ factorization, Koszul duality, Drinfeld center), each of which is independently established at lower dimension; the composite arrow at 6d is conjectural (AP150).
311:\begin{conjecture}[6d holomorphic theory on $K3 \times E$ and the BKM chiral algebra]
312:\label{conj:6d-k3xe}
314:Let $X = K3 \times E$ with $E$ an elliptic curve. The 6d holomorphic theory on $X$ (via the algebraic surrogate of Costello--Francis--Gwilliam factorization homology) should produce (conditional on the non-Lagrangian 6d framework and CY-A$_3$):
321:This conjecture depends on: (a) the existence of the 6d algebraic framework for $K3 \times E$ (non-Lagrangian; Remark~\ref{rem:6d-not-lagrangian}), (b) the CY-A$_3$ programme for the $\Eone$ projection, and (c) the identification of the BPS root datum with the Borcherds--Kac--Moody root system of $\mathfrak{g}_{\Delta_5}$ (Chapter~\ref{ch:k3-times-e}). Each dependency is independent; (b) is the bottleneck.
324:\begin{remark}[What the 6d theory adds to the existing $K3 \times E$ story]
325:\label{rem:6d-adds-to-k3xe}
326:Chapters~\ref{ch:k3-times-e} and~\ref{chap:toroidal-elliptic} develop the \emph{conjectural} $K3 \times E$ chiral algebra programme: the first via the CY-to-chiral functor $\Phi$ (conditional on CY-A$_3$), the second via the toroidal/elliptic quantum group presentation (conditional on Conjecture~\ref{conj:toroidal-e1}). Conjecture~\ref{conj:6d-k3xe} adds a third conjectural construction pathway: the holomorphic CS / factorization homology route. The three pathways should agree if all three programmes are realized:
335: 6d holomorphic theory & $K3 \times E$ as ambient & $\Eone$-chiral on $E$ \\
339:The agreement of the three is itself conjectural. The 6d pathway provides the geometric origin of the quantum toroidal parameters $(q, t)$: they come from the K3 complex structure moduli through the Omega-background identification.
exec
/bin/zsh -lc "sed -n '648,766p' chapters/examples/toric_cy3_coha.tex" in /Users/raeez/calabi-yau-quantum-groups succeeded in 54ms:

Theorem~\ref{thm:toric-cy3-chiral-qg} assembles five components
of the chiral quantum group datum for toric CY3 without compact
$4$-cycles. The components are proved independently: the CoHA
bialgebra by Schiffmann--Vasserot and RSYZ, the $R$-matrix by
Maulik--Okounkov, the Drinfeld double by triangular decomposition,
the chart gluing by descent, the shadow tower by the MC equation.
These components are \emph{a priori} separate structures on the
same algebra. The Vol~I chiral quantum group equivalence
(Theorem~\ref{thm:chiral-qg-equiv}) asserts that three of them
(the vertex $R$-matrix, the chiral $A_\infty$-structure, and the
chiral coproduct) determine each other on the Koszul locus. The theorem
below specializes the abstract equivalence to the toric CY3 setting,
where both sides are independently known, yielding the strongest
unconditional statement: the RSYZ bialgebra coproduct, the MO
$R$-matrix, and the bar-differential $A_\infty$-structure are three
faces of a single object.

\begin{theorem}[Chiral quantum group equivalence for toric CY3]
\label{thm:toric-chiral-qg-specialization}
exec
/bin/zsh -lc "sed -n '228,241p' chapters/connections/modular_koszul_bridge.tex" in /Users/raeez/calabi-yau-quantum-groups succeeded in 51ms:
 \qquad \mathrm{wt}(\Phi_{10}) = 10,
 \]
 where $\phi_{-2, 1}$ is the weak Jacobi form of weight $-2$ and index $1$; this is the Igusa cusp form, \S\ref{subsec:k3e-yau-zaslow} and chapters/examples/toroidal\_elliptic.tex equation~(5.1).
 \item The BPS modular characteristic $\kappa_{\mathrm{BKM}} = 5 = \mathrm{wt}(\Phi_{10})/2$ is distinct from the chiral characteristic $\kappa_{\mathrm{ch}} = 3$ (the $\kappa_\bullet$-spectrum polysemy, Remark~\ref{rem:cy3-kappa-polysemy}; neither value is universal).
 \item The shadow obstruction tower of $\cA_{K3} \otimes H_1$ does \emph{not} by itself reproduce $\Phi_{10}$: four obstructions (K3-4 of \S\ref{sec:k3e-cross-volume}) separate the shadow tower output from $\Phi_{10}$. Namely, (O1) a categorical obstruction, (O2) the $\kappa_{\mathrm{ch}}/\kappa_{\mathrm{BKM}}$ mismatch $3 \neq 5$, (O3) second quantization (the Hilbert--Chow exceptional divisor), and (O4) the Schottky obstruction at $g \geq 4$ of codimension $(g-2)(g-3)/2$. The Borcherds lift supplies precisely the combinatorial data needed to bridge these four obstructions.
\end{enumerate}
\end{theorem}

\begin{proof}[Attribution]
Parts (i), (iii), (iv) are Vol~I/II results (\S\ref{sec:k3e-cross-volume}, items K3-1 through K3-13, proved in the K3 modular-tower chapter of Vol~I and in the Vol~II 3D quantum gravity treatment, \ref{part:3d-qg} there). Part (ii) is the Borcherds lift of Borcherds (1998); its use as a modular characteristic is the observation of AP-CY8, not a theorem of Vol~III. The conditionality on propagates from Theorem~\ref{thm:cy-shadow-cohft}.
\end{proof}

\begin{remark}[Kappa-spectrum verification for $K3 \times E$]
\label{rem:kappa-spectrum-k3xe-bridge}



thinking
**Inspecting labels in documents**

I think I should check for old broken labels or unresolved labels like `\ref{...}` to ensure none are left. It might also help to look for `??`. I’ll inspect `chapters/examples/toroidal_elliptic.tex` for the chapter label `chap:toroidal-elliptic` and see if I can add an alias like `\label{ch:toroidal-elliptic}`. I might need several aliases alongside `\phantomsection`, especially since labels in text without a counter might need recommendations here. A few more labels need to be checked for consistency and placement too.
thinking
**Adding and updating labels**

I think I should add an alias `\label{ch:toroidal-elliptic}` close to `chap:toroidal-elliptic`. I also need to consider adding `\label{thm:e1-stabilization}` near `thm:e1-stabilization-cy`, although maybe the theorem label works fine as is. If the call-site changes for `sec:e1-chiral-bialgebra`, an alias might not be necessary. For `rem:toric-structural-patterns`, I could add an alias near `rem:toric-kappa-patterns`. Concerning `thm:cy-seven-face-master`, I wonder if it could be linked to a conjecture, but maybe it's better to just update the call-site since it’s only one line.
thinking
**Considering introduction edits**

I'm thinking about adjusting the introduction line 397. It currently says "The K3 double current algebra $\fg_{K3}$ (Chapter..., Definition...)" and I believe it would be clearer as "The K3 double current algebra $\fg_{K3}$, discussed in the DDCA--toroidal bridge of Chapter\ref{ch:k3-times-e},". That seems like a good change. I should also look at line 280 to make sure it aligns in a similar way with the bullet points.
exec
/bin/zsh -lc "sed -n '724,734p' chapters/theory/drinfeld_center.tex" in /Users/raeez/calabi-yau-quantum-groups succeeded in 52ms:
$\Eone$-monoidal input. This is a fundamentally different
mechanism from the $E_3 \to \Etwo$ restriction, which
produces only symmetric braiding. The distinction is the
deep reason for the $\Eone$ stabilization theorem
(Chapter~\ref{ch:cy-to-chiral},
Theorem~\ref{thm:e1-stabilization}).

\begin{proposition}[$E_3$ restriction gives symmetric braiding]
\label{prop:e3-symmetric-braiding}
\ClaimStatusProvedElsewhere
Let $\cC$ be an $E_3$-monoidal category. The restriction of the
codex
I’ve finished classification. The patch is limited to the files that actually contain the broken calls, and each change is either a direct retarget to the live local label or a conversion from an impossible cross-volume `\ref` into plain truthful prose.
file update
M /Users/raeez/calabi-yau-quantum-groups/chapters/examples/toric_cy3_coha.tex
@@ -207,3 +207,3 @@
 \begin{proof}
-(i) The compact base $\bP^1 \times \bP^1$ has $\chi(\bP^1 \times \bP^1) = 4$ (each factor contributes $\chi(\bP^1) = 2$), so $\kappa_{\mathrm{ch}} = \chi/2 = 2$ by the general local-surface formula (Remark~\ref{rem:toric-structural-patterns}).
+(i) The compact base $\bP^1 \times \bP^1$ has $\chi(\bP^1 \times \bP^1) = 4$ (each factor contributes $\chi(\bP^1) = 2$), so $\kappa_{\mathrm{ch}} = \chi/2 = 2$ by the general local-surface formula (Remark~\ref{rem:toric-kappa-patterns}).
 
@@ -656,3 +656,3 @@
 same algebra. The Vol~I chiral quantum group equivalence
-(Theorem~\ref{thm:chiral-qg-equiv}) asserts that three of them
+asserts that three of them
 (the vertex $R$-matrix, the chiral $A_\infty$-structure, and the
@@ -748,4 +748,3 @@
 The abstract equivalence (I) $\leftrightarrow$ (II)
-$\leftrightarrow$ (III) is
-Theorem~\ref{thm:chiral-qg-equiv} of Vol~I, proved for any
+$\leftrightarrow$ (III) is the Vol~I chiral quantum group equivalence, proved for any
 $\Eone$-chiral algebra on the Koszul locus. The content of the
@@ -757,3 +756,3 @@
 $R$-matrix by the general theory
-(Theorem~\ref{thm:chiral-qg-equiv}(I)). For toric CY3, the
+(item~\textup{(I)} of that equivalence). For toric CY3, the
 Maulik--Okounkov stable-envelope construction provides an
M /Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_categories.tex
@@ -168,3 +168,3 @@
 
-At $d = 2$ the enhancement is explicit enough to compute directly; it drives the $K3$ computations feeding the Borcherds denominator (Vol~III Chapter~\ref{ch:k3}). At $d = 3$ the enhancement was constructed by Sheridan~\cite{Sheridan2015} for the quintic threefold, as part of the HMS proof; the general $d = 3$ construction remains programme-level (conditional on $\bS^3$-framing, see AP-CY6).
+At $d = 2$ the enhancement is explicit enough to compute directly; it drives the $K3$ computations feeding the Borcherds denominator (Vol~III Chapter~\ref{ch:k3-times-e}). At $d = 3$ the enhancement was constructed by Sheridan~\cite{Sheridan2015} for the quintic threefold, as part of the HMS proof; the general $d = 3$ construction remains programme-level (conditional on $\bS^3$-framing, see AP-CY6).
 
@@ -196,3 +196,3 @@
 \label{rem:phi-does-not-see}
-Not every invariant of $\cC$ survives the passage through $\Phi$. The functor retains the cyclic $\Ainf$-structure and the Gerstenhaber bracket; it loses the fine structure of the triangulated / $\Ainf$ category (individual objects, t-structures, stability conditions) that is visible only via the fuller categorical CoHA construction of Chapter~\ref{ch:coha}. The kappa-spectrum (Vol~III CLAUDE.md) encodes which invariants survive: $\kappa_\mathrm{cat}$ is always present, $\kappa_\mathrm{ch}$ exists only when $\Phi$ is defined, and $\kappa_\mathrm{BKM}$ records the Borcherds-side lift for $K3 \times E$.
+Not every invariant of $\cC$ survives the passage through $\Phi$. The functor retains the cyclic $\Ainf$-structure and the Gerstenhaber bracket; it loses the fine structure of the triangulated / $\Ainf$ category (individual objects, t-structures, stability conditions) that is visible only via the fuller categorical CoHA construction of Chapter~\ref{ch:toric-coha}. The kappa-spectrum (Vol~III CLAUDE.md) encodes which invariants survive: $\kappa_\mathrm{cat}$ is always present, $\kappa_\mathrm{ch}$ exists only when $\Phi$ is defined, and $\kappa_\mathrm{BKM}$ records the Borcherds-side lift for $K3 \times E$.
 \end{remark}
M /Users/raeez/calabi-yau-quantum-groups/chapters/connections/cy_holographic_datum_master.tex
@@ -945,3 +945,3 @@
 elliptic Sklyanin for toroidal CY, Gaudin from CY$_3$
-(Theorem~\ref{thm:cy-seven-face-master} above).
+(Conjecture~\ref{conj:cy-seven-face-master} above).
 \end{enumerate}
M /Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex
@@ -236,3 +236,3 @@
 \begin{proof}[Attribution]
-Parts (i), (iii), (iv) are Vol~I/II results (\S\ref{sec:k3e-cross-volume}, items K3-1 through K3-13, proved in the K3 modular-tower chapter of Vol~I and in the Vol~II 3D quantum gravity treatment, \ref{part:3d-qg} there). Part (ii) is the Borcherds lift of Borcherds (1998); its use as a modular characteristic is the observation of AP-CY8, not a theorem of Vol~III. The conditionality on propagates from Theorem~\ref{thm:cy-shadow-cohft}.
+Parts (i), (iii), (iv) are Vol~I/II results (\S\ref{sec:k3e-cross-volume}, items K3-1 through K3-13, proved in the K3 modular-tower chapter of Vol~I and in Part~III of Vol~II's 3D quantum gravity treatment). Part (ii) is the Borcherds lift of Borcherds (1998); its use as a modular characteristic is the observation of AP-CY8, not a theorem of Vol~III. The conditionality on propagates from Theorem~\ref{thm:cy-shadow-cohft}.
 \end{proof}
M /Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex
@@ -505,3 +505,3 @@
  number-theoretic invariant arising from the BKM denominator
- formula (Chapter~\ref{ch:toroidal-elliptic}; distinct from
+ formula (Chapter~\ref{chap:toroidal-elliptic}; distinct from
  both $\kappa_{\mathrm{cat}}$ and $\kappa_{\mathrm{ch}}$).
M /Users/raeez/calabi-yau-quantum-groups/chapters/theory/drinfeld_center.tex
@@ -728,3 +728,3 @@
 (Chapter~\ref{ch:cy-to-chiral},
-Theorem~\ref{thm:e1-stabilization}).
+Theorem~\ref{thm:e1-stabilization-cy}).
 
M /Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex
@@ -620,4 +620,4 @@
 involves no PDE solving. The SDR data $(i, p, s)$ interfaces directly
-with the homotopy transfer theorem
-\textup{(}HTT, Theorem~\textup{\ref{thm:htt-general}}\textup{)},
+with the standard homotopy transfer theorem
+\textup{(}HTT\textup{)},
 transferring the $\Ainf$-structure from $\check{C}^\bullet(\cE nd(\cE))$
@@ -654,3 +654,3 @@
 the analytic completion programme (MC5,
-\S\ref{sec:analytic-sewing} of Vol~I). Specifically: the HTT
+the analytic sewing section of Vol~I). Specifically: the HTT
 produces transferred operations $\mu_k^{\mathrm{ch}}$ whose
@@ -1974,3 +1974,3 @@
 \end{center}
-{\footnotesize $^*$The K3 entry records $\kappa_{\mathrm{ch}} = \chi(\cO_{\mathrm{K3}}) = 2$ (Proposition~\ref{prop:cy-kappa-d2}; verified via chiral de Rham, Chapter~\ref{ch:k3-times-e}). The distinct quantity $\dim \HH_*(D^b(\mathrm{K3}))/2 = 12$ arises from an alternative algebraization (the Monster orbifold); the full trichotomy ($\kappa_{\mathrm{ch}} \in \{2, 12, 24\}$) is developed in Section~\ref{subsec:k3-three-algebraizations} of Chapter~\ref{ch:k3-times-e}.
+{\footnotesize $^*$The K3 entry records $\kappa_{\mathrm{ch}} = \chi(\cO_{\mathrm{K3}}) = 2$ (Proposition~\ref{prop:cy-kappa-d2}; verified via chiral de Rham, Chapter~\ref{ch:k3-times-e}). The distinct quantity $\dim \HH_*(D^b(\mathrm{K3}))/2 = 12$ arises from an alternative algebraization (the Monster orbifold); the full trichotomy ($\kappa_{\mathrm{ch}} \in \{2, 12, 24\}$) is developed in the K3 discussion of Chapter~\ref{ch:k3-times-e}.
 
M /Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex
@@ -5942,4 +5942,3 @@
 surface~$S$: the K3 double current algebra $\fg_{K3}$
-(Chapter~\ref{ch:k3-times-e},
-Definition~\ref{def:k3-double-current-algebra}) substitutes
+substitutes
 $H^*(S,\bC)$ for $\bC[u,v]$ and the Mukai pairing for the
@@ -6020,3 +6019,3 @@
   Drinfeld coproduct $\Delta_z(T(u)) = T(u) \otimes T(u - z)$
-  of Theorem~\textup{\ref{thm:w-infty-chiral-qg}}.
+  of Proposition~\textup{\ref{prop:universal-coproduct}}.
 \end{enumerate}
@@ -6036,3 +6035,3 @@
   formula aligned with the $R(u,v)$ surface in
-  \S\ref{subsec:quantum-chiral-algebras-6d}.
+  \S\ref{subsec:chiral-qg-wilson}.
 \item Build a compute witness at low modes: $w = 0$ reduces
M /Users/raeez/calabi-yau-quantum-groups/chapters/theory/e2_chiral_algebras.tex
@@ -196,3 +196,3 @@
 Volume~II constructs $\Phi_{E_1}$ and proves $E_1$-chiral Koszul
-duality (see \ref{part:e1-core} of \cite{VolII}). The Drinfeld center
+duality (see Part~I of \cite{VolII}). The Drinfeld center
 $Z\colon E_1\text{-}\Cat \xrightarrow{\sim} E_2\text{-}\Cat$
M /Users/raeez/calabi-yau-quantum-groups/chapters/theory/introduction.tex
@@ -203,3 +203,3 @@
 
-The scope is perturbative: the \v{C}ech homotopy produces an algebraic $A_\infty$-structure on the Ext algebra, but convergence of the resulting series to holomorphic functions (the non-perturbative statement) requires separate input from the analytic completion programme of Volume~I (MC5, \S\ref{sec:analytic-sewing}). The perturbative statement suffices for the formal CY-to-chiral functor and for all combinatorial applications in this volume. The full construction, including the proof that the SDR conditions hold and the scope qualification, is Theorem~\ref{thm:cech-contracting-homotopy} in Chapter~\ref{ch:cy-to-chiral}.
+The scope is perturbative: the \v{C}ech homotopy produces an algebraic $A_\infty$-structure on the Ext algebra, but convergence of the resulting series to holomorphic functions (the non-perturbative statement) requires separate input from the analytic completion programme of Volume~I (MC5, the analytic sewing section there). The perturbative statement suffices for the formal CY-to-chiral functor and for all combinatorial applications in this volume. The full construction, including the proof that the SDR conditions hold and the scope qualification, is Theorem~\ref{thm:cech-contracting-homotopy} in Chapter~\ref{ch:cy-to-chiral}.
 
@@ -279,3 +279,3 @@
  \item Quiver-chart gluing for toric CY$_3$ (Theorem~\ref{thm:toric-chart-gluing}): the global $\Eone$-chiral algebra is assembled as a homotopy colimit of McKay-chart CoHAs, with $E_2$ descent degeneration and Costello--Li comparison.
- \item The K3 double current algebra $\fg_{K3}$ (Definition~\ref{def:k3-double-current-algebra}): the finite-dimensional analogue of the DDCA in which $\bC[u,v]$ is replaced by $H^*(S,\bC)$ with the Mukai pairing.
+ \item The K3 double current algebra $\fg_{K3}$: the finite-dimensional analogue of the DDCA in which $\bC[u,v]$ is replaced by $H^*(S,\bC)$ with the Mukai pairing.
  \item Forty-two CY/BKM compute engines with $5{,}700{+}$ tests across the standard CY landscape.
@@ -362,3 +362,3 @@
  stability manifold. Proved for toric CY3
- (Proposition~\ref{prop:e1-descent-unobstructed}); open for
+ (Theorem~\ref{thm:toric-chart-gluing}); open for
  compact CY3 beyond the chart-atlas regime.
@@ -396,3 +396,3 @@
 
-In addition to the four standard families, the toroidal and elliptic algebras chapter (Chapter~\ref{chap:toroidal-elliptic}) develops the $K3 \times E$ programme in full: the generalized root datum, the BKM superalgebra $\mathfrak{g}_{\Delta_5}$ with its Igusa cusp form denominator identity, the shadow--Siegel gap theorem, thirteen structural results (K3-1 through K3-13), all ten research programmes (A through J), and the DDCA--toroidal bridge identifying the deformed double current algebra as the rational degeneration of the quantum toroidal algebra (Conjecture~\ref{conj:ddca-toroidal-bridge}). The K3 double current algebra $\fg_{K3}$ (Chapter~\ref{ch:k3-times-e}, Definition~\ref{def:k3-double-current-algebra}) provides the K3 analogue of the DDCA, replacing $\bC[u,v]$ with $H^*(S,\bC)$. The toric CY$_3$ CoHA chapter (Chapter~\ref{ch:toric-coha}) develops the affine Yangian and $\mathcal{W}_{1+\infty}$ side: the Jordan quiver gives $Y(\widehat{\mathfrak{gl}}_1) \simeq \mathcal{W}_{1+\infty}$, the toric fan is the Dynkin data, and the shuffle algebra presentation connects to the KZ equations of Volume~I.
+In addition to the four standard families, the toroidal and elliptic algebras chapter (Chapter~\ref{chap:toroidal-elliptic}) develops the $K3 \times E$ programme in full: the generalized root datum, the BKM superalgebra $\mathfrak{g}_{\Delta_5}$ with its Igusa cusp form denominator identity, the shadow--Siegel gap theorem, thirteen structural results (K3-1 through K3-13), all ten research programmes (A through J), and the DDCA--toroidal bridge identifying the deformed double current algebra as the rational degeneration of the quantum toroidal algebra (Conjecture~\ref{conj:ddca-toroidal-bridge}). The K3 double current algebra $\fg_{K3}$, discussed in the DDCA--toroidal bridge of Chapter~\ref{ch:k3-times-e}, provides the K3 analogue of the DDCA, replacing $\bC[u,v]$ with $H^*(S,\bC)$. The toric CY$_3$ CoHA chapter (Chapter~\ref{ch:toric-coha}) develops the affine Yangian and $\mathcal{W}_{1+\infty}$ side: the Jordan quiver gives $Y(\widehat{\mathfrak{gl}}_1) \simeq \mathcal{W}_{1+\infty}$, the toric fan is the Dynkin data, and the shuffle algebra presentation connects to the KZ equations of Volume~I.
 
@@ -401,3 +401,3 @@
 
-Part~\ref{part:cy-categories} establishes the categorical foundations: CY categories, cyclic $\Ainf$-structures, the Hochschild calculus, and the $E_1$/$E_2$/$E_n$ chiral hierarchy with the framing obstruction tower. Part~\ref{part:bridge} constructs the bridge functor $\Phi$ from CY categories to quantum chiral algebras and proves Theorems CY-A (for $d = 2$) and CY-D, with the identification of automorphic correction and shadow obstruction tower as the central result. Part~\ref{part:examples} treats quantum groups and their braided factorization structure, including the Drinfeld center as the bulk algebra. Part~\ref{part:connections} works through the standard landscape: the toroidal and elliptic algebras chapter develops the $K3 \times E$ programme (K3-1 through K3-13, programmes A through J), alongside toric CY3 CoHAs, Fukaya categories, derived categories, matrix factorizations (ADE singularities and W-algebras), and quantum group representations (Kazhdan--Lusztig, affine Yangians, critical CoHAs). Part~\ref{part:frontier} connects to the geometric Langlands programme and to Volumes~I and~II via the bar-cobar bridge and the modular Koszul bridge. The working notes (\S\ref{sec:working-notes}) record the research frontier.
+Part~\ref{part:cy-categories} establishes the categorical foundations: CY categories, cyclic $\Ainf$-structures, the Hochschild calculus, and the $E_1$/$E_2$/$E_n$ chiral hierarchy with the framing obstruction tower. Part~\ref{part:bridge} constructs the bridge functor $\Phi$ from CY categories to quantum chiral algebras and proves Theorems CY-A (for $d = 2$) and CY-D, with the identification of automorphic correction and shadow obstruction tower as the central result. Part~\ref{part:examples} treats quantum groups and their braided factorization structure, including the Drinfeld center as the bulk algebra. Part~\ref{part:connections} works through the standard landscape: the toroidal and elliptic algebras chapter develops the $K3 \times E$ programme (K3-1 through K3-13, programmes A through J), alongside toric CY3 CoHAs, Fukaya categories, derived categories, matrix factorizations (ADE singularities and W-algebras), and quantum group representations (Kazhdan--Lusztig, affine Yangians, critical CoHAs). Part~\ref{part:frontier} connects to the geometric Langlands programme and to Volumes~I and~II via the bar-cobar bridge and the modular Koszul bridge. The separate working notes record the research frontier.
 
M /Users/raeez/calabi-yau-quantum-groups/chapters/frame/preface.tex
@@ -322,3 +322,3 @@
 cross-term $J \otimes W_{s-1}$ at every spin $s \ge 2$
-(Theorem~\ref{thm:miura-cross-universality}).
+(Proposition~\ref{prop:universal-coproduct}).
 
@@ -330,3 +330,3 @@
 $E_1$-chiral bialgebra axioms (formalized in
-\S\ref{sec:e1-chiral-bialgebra}) require: (H1)~an $E_1$-chiral
+\S\ref{sec:e1-chiral-bialgebras}) require: (H1)~an $E_1$-chiral
 algebra $A$ on a curve $X$; (H2)~a spectral coproduct
M /Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex
@@ -65,3 +65,3 @@
 vector at non-critical level
-(Volume~I, Theorem~\textup{\ref*{thm:topologization}}).
+(Volume~I, the topologization theorem).
 \end{definition}
@@ -130,3 +130,3 @@
 \label{rem:three-bars-vol3}
-The CY-to-chiral functor $\Phi$ of Chapter~\ref{ch:cy-chiral-functor} has three natural composites. $\Phi_{E_1}$ produces $B^{\mathrm{ord}}(A_C)$; this is the ordered bar sensed by the Yangian. $\mathrm{av} \circ \Phi_{E_1}$ produces $B^{\Sigma}(A_C)$; this is the symmetric bar sensed by the modular characteristic $\kappa_{\mathrm{ch}}$. The full $E_2$ enhancement $\Phi_{E_2}$ produces the Drinfeld-centered bar $B^{E_2}(A_C) = \cZ(B^{\mathrm{ord}}(A_C))$; this is the braided bar sensed by the quantum group. All three factor through $\Phi_{E_1}$. This is the volume's motto: the ordered bar is the primitive.
+The CY-to-chiral functor $\Phi$ of Chapter~\ref{ch:cy-to-chiral} has three natural composites. $\Phi_{E_1}$ produces $B^{\mathrm{ord}}(A_C)$; this is the ordered bar sensed by the Yangian. $\mathrm{av} \circ \Phi_{E_1}$ produces $B^{\Sigma}(A_C)$; this is the symmetric bar sensed by the modular characteristic $\kappa_{\mathrm{ch}}$. The full $E_2$ enhancement $\Phi_{E_2}$ produces the Drinfeld-centered bar $B^{E_2}(A_C) = \cZ(B^{\mathrm{ord}}(A_C))$; this is the braided bar sensed by the quantum group. All three factor through $\Phi_{E_1}$. This is the volume's motto: the ordered bar is the primitive.
 \end{remark}
@@ -155,3 +155,3 @@
 
-The conjecture is conditional on the chain-level framing; the unconditional statement requires the full CY-A$_3$ programme. Every downstream result in \ref{part:examples} and \ref{part:connections} that uses the BPS Yangian inherits this conditionality. The connection to Maulik-Okounkov and Costello-Witten cohomological Hall algebras is traced in Chapter~\ref{ch:cha-yangian}.
+The conjecture is conditional on the chain-level framing; the unconditional statement requires the full CY-A$_3$ programme. Every downstream result in \ref{part:examples} and \ref{part:connections} that uses the BPS Yangian inherits this conditionality. The connection to Maulik-Okounkov and Costello-Witten cohomological Hall algebras is traced in Chapter~\ref{ch:toric-coha}.
 
@@ -320,3 +320,3 @@
 \label{rem:downstream-usage}
-Chapters~\ref{ch:braided-factorization}, \ref{ch:drinfeld-center}, and \ref{ch:quantum-group-reps} use this chapter as the source of the ordered bar coalgebra and the averaging map. Chapter~\ref{ch:cy-chiral-functor} uses Proposition~\ref{prop:e1-sector-d2} as the $d=2$ existence statement for $A_\cC$. Every braided monoidal category that appears later is the Drinfeld center of an underlying ordered one.
+Chapters~\ref{ch:braided-factorization}, \ref{ch:drinfeld-center}, and \ref{ch:quantum-group-reps} use this chapter as the source of the ordered bar coalgebra and the averaging map. Chapter~\ref{ch:cy-to-chiral} uses Proposition~\ref{prop:e1-sector-d2} as the $d=2$ existence statement for $A_\cC$. Every braided monoidal category that appears later is the Drinfeld center of an underlying ordered one.
 \end{remark}
@@ -1449,3 +1449,3 @@
 homology integral $\int_{K3} \cF|_{K3}$ of
-Section~\ref{sec:k3-perturbative-fact-homology} produces a chiral algebra
+Section~\ref{subsec:fact-homology-k3xe} produces a chiral algebra
 $A_E$ on the residual elliptic curve $E$.  The coproduct on $A_E$ arises
apply_patch(auto_approved=true) exited 0 in 83ms:
Success. Updated the following files:
M chapters/frame/preface.tex
M chapters/theory/introduction.tex
M chapters/theory/cy_categories.tex
M chapters/theory/e1_chiral_algebras.tex
M chapters/theory/e2_chiral_algebras.tex
M chapters/theory/cy_to_chiral.tex
M chapters/theory/drinfeld_center.tex
M chapters/examples/toric_cy3_coha.tex
M chapters/examples/quantum_group_reps.tex
M chapters/examples/toroidal_elliptic.tex
M chapters/connections/cy_holographic_datum_master.tex
M chapters/connections/modular_koszul_bridge.tex
file update:
diff --git a/chapters/connections/cy_holographic_datum_master.tex b/chapters/connections/cy_holographic_datum_master.tex
index 2a66e8a0ca86f097e30b0de99c082498014430c6..b0ef34640300f22c24d57ee10a207c331065f31d
--- a/chapters/connections/cy_holographic_datum_master.tex
+++ b/chapters/connections/cy_holographic_datum_master.tex
@@ -943,7 +943,7 @@
 bar-cobar, CoHA / perverse coherent sheaves, classical CY Poisson
 coisson, MO stable envelope, affine super Yangian for toric CY$_3$,
 elliptic Sklyanin for toroidal CY, Gaudin from CY$_3$
-(Theorem~\ref{thm:cy-seven-face-master} above).
+(Conjecture~\ref{conj:cy-seven-face-master} above).
 \end{enumerate}
 The three master theorems are mutually compatible: under the CY-to-chiral
 functor $\Phi$, face~$i$ of Vol~III maps to a specialization of face~$i$
diff --git a/chapters/connections/modular_koszul_bridge.tex b/chapters/connections/modular_koszul_bridge.tex
index 1199c5aaa32e71f085dd3b7131c8f9aeadb1148c..a423d35b2ce162a9f56bb568768ae1bed7bef2f6
--- a/chapters/connections/modular_koszul_bridge.tex
+++ b/chapters/connections/modular_koszul_bridge.tex
@@ -234,7 +234,7 @@
 \end{theorem}
 
 \begin{proof}[Attribution]
-Parts (i), (iii), (iv) are Vol~I/II results (\S\ref{sec:k3e-cross-volume}, items K3-1 through K3-13, proved in the K3 modular-tower chapter of Vol~I and in the Vol~II 3D quantum gravity treatment, \ref{part:3d-qg} there). Part (ii) is the Borcherds lift of Borcherds (1998); its use as a modular characteristic is the observation of AP-CY8, not a theorem of Vol~III. The conditionality on propagates from Theorem~\ref{thm:cy-shadow-cohft}.
+Parts (i), (iii), (iv) are Vol~I/II results (\S\ref{sec:k3e-cross-volume}, items K3-1 through K3-13, proved in the K3 modular-tower chapter of Vol~I and in Part~III of Vol~II's 3D quantum gravity treatment). Part (ii) is the Borcherds lift of Borcherds (1998); its use as a modular characteristic is the observation of AP-CY8, not a theorem of Vol~III. The conditionality on propagates from Theorem~\ref{thm:cy-shadow-cohft}.
 \end{proof}
 
 \begin{remark}[Kappa-spectrum verification for $K3 \times E$]
diff --git a/chapters/examples/quantum_group_reps.tex b/chapters/examples/quantum_group_reps.tex
index e6b19a4c52de09f17af4b5f794d5f7269f4076b4..5213e6bfc9cb828c11c98b50aa32549aa228cfbf
--- a/chapters/examples/quantum_group_reps.tex
+++ b/chapters/examples/quantum_group_reps.tex
@@ -503,7 +503,7 @@
  additional data);
  \item $\kappa_{\mathrm{BKM}}$: the BKM modular weight, a
  number-theoretic invariant arising from the BKM denominator
- formula (Chapter~\ref{ch:toroidal-elliptic}; distinct from
+ formula (Chapter~\ref{chap:toroidal-elliptic}; distinct from
  both $\kappa_{\mathrm{cat}}$ and $\kappa_{\mathrm{ch}}$).
 \end{enumerate}
 For CY$_2$ categories with $\frakg$-symmetry, all three can be
diff --git a/chapters/examples/toric_cy3_coha.tex b/chapters/examples/toric_cy3_coha.tex
index 2b8821c0fd545c77e9d18a4180e8e67d3c4459be..94da66b26dadb3a8dcd2e91287fd7092ea5a944c
--- a/chapters/examples/toric_cy3_coha.tex
+++ b/chapters/examples/toric_cy3_coha.tex
@@ -205,7 +205,7 @@
 \end{theorem}
 
 \begin{proof}
-(i) The compact base $\bP^1 \times \bP^1$ has $\chi(\bP^1 \times \bP^1) = 4$ (each factor contributes $\chi(\bP^1) = 2$), so $\kappa_{\mathrm{ch}} = \chi/2 = 2$ by the general local-surface formula (Remark~\ref{rem:toric-structural-patterns}).
+(i) The compact base $\bP^1 \times \bP^1$ has $\chi(\bP^1 \times \bP^1) = 4$ (each factor contributes $\chi(\bP^1) = 2$), so $\kappa_{\mathrm{ch}} = \chi/2 = 2$ by the general local-surface formula (Remark~\ref{rem:toric-kappa-patterns}).
 
 (ii) The intersection form on $H^2(\bP^1 \times \bP^1)$ in the basis $\{e_1, e_2\}$ is $\langle e_i, e_j \rangle = \delta_{ij}$ (the two rulings are orthogonal with self-intersection $0$ in the total space, but the relevant inner product for the shadow metric is the Euler pairing $\chi(e_i, e_j) = \delta_{ij}$).
 
@@ -654,7 +654,7 @@
 the chart gluing by descent, the shadow tower by the MC equation.
 These components are \emph{a priori} separate structures on the
 same algebra. The Vol~I chiral quantum group equivalence
-(Theorem~\ref{thm:chiral-qg-equiv}) asserts that three of them
+asserts that three of them
 (the vertex $R$-matrix, the chiral $A_\infty$-structure, and the
 chiral coproduct) determine each other on the Koszul locus. The theorem
 below specializes the abstract equivalence to the toric CY3 setting,
@@ -746,8 +746,7 @@
 
 \begin{proof}
 The abstract equivalence (I) $\leftrightarrow$ (II)
-$\leftrightarrow$ (III) is
-Theorem~\ref{thm:chiral-qg-equiv} of Vol~I, proved for any
+$\leftrightarrow$ (III) is the Vol~I chiral quantum group equivalence, proved for any
 $\Eone$-chiral algebra on the Koszul locus. The content of the
 present theorem is the identification of each abstract vertex
 with the independently constructed toric CY3 structure.
@@ -755,7 +754,7 @@
 \textit{Component~\textup{(I)}: $R$-matrix.}
 The $\Eone$-chiral algebra $A_X$ carries a vertex
 $R$-matrix by the general theory
-(Theorem~\ref{thm:chiral-qg-equiv}(I)). For toric CY3, the
+(item~\textup{(I)} of that equivalence). For toric CY3, the
 Maulik--Okounkov stable-envelope construction provides an
 independent $R$-matrix on $Y^+(\widehat{\fg}_{Q_X})$-modules.
 The two coincide because both solve the same Yang--Baxter
diff --git a/chapters/examples/toroidal_elliptic.tex b/chapters/examples/toroidal_elliptic.tex
index 8fcef3a49b8fe0bd45c3ae248676e994ece0ca7e..0a15b2c062f601ea29e50e3e3771b3eb1544db50
--- a/chapters/examples/toroidal_elliptic.tex
+++ b/chapters/examples/toroidal_elliptic.tex
@@ -5940,8 +5940,7 @@
 
 The K3 analogue of this picture replaces $\bC^2$ by a K3
 surface~$S$: the K3 double current algebra $\fg_{K3}$
-(Chapter~\ref{ch:k3-times-e},
-Definition~\ref{def:k3-double-current-algebra}) substitutes
+substitutes
 $H^*(S,\bC)$ for $\bC[u,v]$ and the Mukai pairing for the
 polynomial residue. Its quantization should produce a
 ``K3 Yangian'' standing in the same relation to $\fg_{K3}$ as the
@@ -6018,7 +6017,7 @@
   At $t \to 1$: the second parameter $w$ decouples and
   $\Delta_{z,w}$ reduces to the single-parameter
   Drinfeld coproduct $\Delta_z(T(u)) = T(u) \otimes T(u - z)$
-  of Theorem~\textup{\ref{thm:w-infty-chiral-qg}}.
+  of Proposition~\textup{\ref{prop:universal-coproduct}}.
 \end{enumerate}
 No two-parameter coproduct $\Delta_{z,w}$ currently exists in
 the literature or in this programme's compute infrastructure.
@@ -6034,7 +6033,7 @@
   $(q_1,q_2,q_3)$.
 \item Promote the DDCA shadow to an explicit $\Delta_{z,w}$
   formula aligned with the $R(u,v)$ surface in
-  \S\ref{subsec:quantum-chiral-algebras-6d}.
+  \S\ref{subsec:chiral-qg-wilson}.
 \item Build a compute witness at low modes: $w = 0$ reduces
   to existing $\Delta_z$; rational limit gives the DDCA
   shift; Miki sends $\Delta_{z,w} \to \Delta_{w,z}$.
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index ddbdfe60d9c9df04ba6f3acf48deee73523a64dc..3ce4e679084f2f25672104c7a00684df5e9f3b26
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -320,7 +320,7 @@
 Drinfeld coproduct from spin~$2$ to arbitrary spin, with the
 universal Miura coefficient $(\Psi{-}1)/\Psi$ on the leading
 cross-term $J \otimes W_{s-1}$ at every spin $s \ge 2$
-(Theorem~\ref{thm:miura-cross-universality}).
+(Proposition~\ref{prop:universal-coproduct}).
 
 \bigskip
 
@@ -328,7 +328,7 @@
 Volume~I defines $E_1$-chiral quantum groups abstractly. This
 volume constructs them concretely from CY geometry. The
 $E_1$-chiral bialgebra axioms (formalized in
-\S\ref{sec:e1-chiral-bialgebra}) require: (H1)~an $E_1$-chiral
+\S\ref{sec:e1-chiral-bialgebras}) require: (H1)~an $E_1$-chiral
 algebra $A$ on a curve $X$; (H2)~a spectral coproduct
 $\Delta_z \colon A \to A \otimes A$ (living on the OPEN/$E_1$
 colour); (H3)~an $R$-matrix $R(z)$ satisfying YBE; (H4)~RTT
diff --git a/chapters/theory/cy_categories.tex b/chapters/theory/cy_categories.tex
index f9b51871c44fa18a574c02fce8aaa49a49aa9c61..00d723a1cb5d4f2355a10cb2d9d3f86688259f09
--- a/chapters/theory/cy_categories.tex
+++ b/chapters/theory/cy_categories.tex
@@ -166,7 +166,7 @@
 Every smooth proper CY$_d$ category admits a cyclic $\Ainf$-enhancement, unique up to $\Ainf$-quasi-isomorphism preserving the pairing. The proof is due to Kontsevich--Soibelman in the formal case, Costello~\cite{Costello2005} for the TCFT enhancement, and Seidel~\cite{Seidel2008} for the Fukaya case.
 \end{theorem}
 
-At $d = 2$ the enhancement is explicit enough to compute directly; it drives the $K3$ computations feeding the Borcherds denominator (Vol~III Chapter~\ref{ch:k3}). At $d = 3$ the enhancement was constructed by Sheridan~\cite{Sheridan2015} for the quintic threefold, as part of the HMS proof; the general $d = 3$ construction remains programme-level (conditional on $\bS^3$-framing, see AP-CY6).
+At $d = 2$ the enhancement is explicit enough to compute directly; it drives the $K3$ computations feeding the Borcherds denominator (Vol~III Chapter~\ref{ch:k3-times-e}). At $d = 3$ the enhancement was constructed by Sheridan~\cite{Sheridan2015} for the quintic threefold, as part of the HMS proof; the general $d = 3$ construction remains programme-level (conditional on $\bS^3$-framing, see AP-CY6).
 
 \section{Interface with the CY-to-chiral functor $\Phi$}
 \label{sec:cy-cat-phi-interface}
@@ -194,7 +194,7 @@
 
 \begin{remark}[What $\Phi$ does not see]
 \label{rem:phi-does-not-see}
-Not every invariant of $\cC$ survives the passage through $\Phi$. The functor retains the cyclic $\Ainf$-structure and the Gerstenhaber bracket; it loses the fine structure of the triangulated / $\Ainf$ category (individual objects, t-structures, stability conditions) that is visible only via the fuller categorical CoHA construction of Chapter~\ref{ch:coha}. The kappa-spectrum (Vol~III CLAUDE.md) encodes which invariants survive: $\kappa_\mathrm{cat}$ is always present, $\kappa_\mathrm{ch}$ exists only when $\Phi$ is defined, and $\kappa_\mathrm{BKM}$ records the Borcherds-side lift for $K3 \times E$.
+Not every invariant of $\cC$ survives the passage through $\Phi$. The functor retains the cyclic $\Ainf$-structure and the Gerstenhaber bracket; it loses the fine structure of the triangulated / $\Ainf$ category (individual objects, t-structures, stability conditions) that is visible only via the fuller categorical CoHA construction of Chapter~\ref{ch:toric-coha}. The kappa-spectrum (Vol~III CLAUDE.md) encodes which invariants survive: $\kappa_\mathrm{cat}$ is always present, $\kappa_\mathrm{ch}$ exists only when $\Phi$ is defined, and $\kappa_\mathrm{BKM}$ records the Borcherds-side lift for $K3 \times E$.
 \end{remark}
 
 \begin{remark}[Cross-volume conventions]
diff --git a/chapters/theory/cy_to_chiral.tex b/chapters/theory/cy_to_chiral.tex
index 030fed4a9a2a7009ae05fdb0f3c431c8aed1fc83..14526e0aba63169841056220749304799a57fe10
--- a/chapters/theory/cy_to_chiral.tex
+++ b/chapters/theory/cy_to_chiral.tex
@@ -618,8 +618,8 @@
 homotopy is purely algebraic: it acts by
 $s(f_{i_0 \cdots i_q}) = f_{0 i_0 \cdots i_q}$ on \v{C}ech cochains and
 involves no PDE solving. The SDR data $(i, p, s)$ interfaces directly
-with the homotopy transfer theorem
-\textup{(}HTT, Theorem~\textup{\ref{thm:htt-general}}\textup{)},
+with the standard homotopy transfer theorem
+\textup{(}HTT\textup{)},
 transferring the $\Ainf$-structure from $\check{C}^\bullet(\cE nd(\cE))$
 to its cohomology $\Ext^\bullet(\cE, \cE)$.
 \end{theorem}
@@ -652,7 +652,7 @@
 (whether the formal series in the OPE coefficients converges to
 define honest holomorphic functions) requires separate input from
 the analytic completion programme (MC5,
-\S\ref{sec:analytic-sewing} of Vol~I). Specifically: the HTT
+the analytic sewing section of Vol~I). Specifically: the HTT
 produces transferred operations $\mu_k^{\mathrm{ch}}$ whose
 coefficients involve iterated applications of~$s$; each application
 introduces rational functions on the intersections $U_{i_0} \cap
@@ -1972,7 +1972,7 @@
  \bottomrule
 \end{tabular}
 \end{center}
-{\footnotesize $^*$The K3 entry records $\kappa_{\mathrm{ch}} = \chi(\cO_{\mathrm{K3}}) = 2$ (Proposition~\ref{prop:cy-kappa-d2}; verified via chiral de Rham, Chapter~\ref{ch:k3-times-e}). The distinct quantity $\dim \HH_*(D^b(\mathrm{K3}))/2 = 12$ arises from an alternative algebraization (the Monster orbifold); the full trichotomy ($\kappa_{\mathrm{ch}} \in \{2, 12, 24\}$) is developed in Section~\ref{subsec:k3-three-algebraizations} of Chapter~\ref{ch:k3-times-e}.
+{\footnotesize $^*$The K3 entry records $\kappa_{\mathrm{ch}} = \chi(\cO_{\mathrm{K3}}) = 2$ (Proposition~\ref{prop:cy-kappa-d2}; verified via chiral de Rham, Chapter~\ref{ch:k3-times-e}). The distinct quantity $\dim \HH_*(D^b(\mathrm{K3}))/2 = 12$ arises from an alternative algebraization (the Monster orbifold); the full trichotomy ($\kappa_{\mathrm{ch}} \in \{2, 12, 24\}$) is developed in the K3 discussion of Chapter~\ref{ch:k3-times-e}.
 
 $^\dagger$The $K3 \times E$ entry records $\kappa_{\mathrm{ch}} = 3$ by additivity (Proposition~\ref{prop:categorical-euler}: $\kappa_{\mathrm{ch}}(\mathrm{K3}) + \kappa_{\mathrm{ch}}(E) = 2 + 1$). The Borcherds automorphic weight is $\kappa_{\mathrm{BKM}} = 5 = \mathrm{wt}(\Delta_5)$, a distinct invariant.}
 
diff --git a/chapters/theory/drinfeld_center.tex b/chapters/theory/drinfeld_center.tex
index ac67d4e3a2ed8fab94fcb3fc63933d8650a92ac9..a711d853438f9e6a0e6fdd4e5dac61154b7b3c24
--- a/chapters/theory/drinfeld_center.tex
+++ b/chapters/theory/drinfeld_center.tex
@@ -726,7 +726,7 @@
 produces only symmetric braiding. The distinction is the
 deep reason for the $\Eone$ stabilization theorem
 (Chapter~\ref{ch:cy-to-chiral},
-Theorem~\ref{thm:e1-stabilization}).
+Theorem~\ref{thm:e1-stabilization-cy}).
 
 \begin{proposition}[$E_3$ restriction gives symmetric braiding]
 \label{prop:e3-symmetric-braiding}
diff --git a/chapters/theory/e1_chiral_algebras.tex b/chapters/theory/e1_chiral_algebras.tex
index 75484d2fff759dc21313b5595a8abade7d55d203..b533b2f5640db9eba4046a61106787f2c19a0d53
--- a/chapters/theory/e1_chiral_algebras.tex
+++ b/chapters/theory/e1_chiral_algebras.tex
@@ -63,7 +63,7 @@
 via holomorphic Chern--Simons; conjectural in general).
 The further $E_3$-topological upgrade requires a conformal
 vector at non-critical level
-(Volume~I, Theorem~\textup{\ref*{thm:topologization}}).
+(Volume~I, the topologization theorem).
 \end{definition}
 
 The closed colour carries $E_2$ structure from
@@ -128,7 +128,7 @@
 
 \begin{remark}[Three bars, one functor]
 \label{rem:three-bars-vol3}
-The CY-to-chiral functor $\Phi$ of Chapter~\ref{ch:cy-chiral-functor} has three natural composites. $\Phi_{E_1}$ produces $B^{\mathrm{ord}}(A_C)$; this is the ordered bar sensed by the Yangian. $\mathrm{av} \circ \Phi_{E_1}$ produces $B^{\Sigma}(A_C)$; this is the symmetric bar sensed by the modular characteristic $\kappa_{\mathrm{ch}}$. The full $E_2$ enhancement $\Phi_{E_2}$ produces the Drinfeld-centered bar $B^{E_2}(A_C) = \cZ(B^{\mathrm{ord}}(A_C))$; this is the braided bar sensed by the quantum group. All three factor through $\Phi_{E_1}$. This is the volume's motto: the ordered bar is the primitive.
+The CY-to-chiral functor $\Phi$ of Chapter~\ref{ch:cy-to-chiral} has three natural composites. $\Phi_{E_1}$ produces $B^{\mathrm{ord}}(A_C)$; this is the ordered bar sensed by the Yangian. $\mathrm{av} \circ \Phi_{E_1}$ produces $B^{\Sigma}(A_C)$; this is the symmetric bar sensed by the modular characteristic $\kappa_{\mathrm{ch}}$. The full $E_2$ enhancement $\Phi_{E_2}$ produces the Drinfeld-centered bar $B^{E_2}(A_C) = \cZ(B^{\mathrm{ord}}(A_C))$; this is the braided bar sensed by the quantum group. All three factor through $\Phi_{E_1}$. This is the volume's motto: the ordered bar is the primitive.
 \end{remark}
 
 \section{$E_1$-chiral algebras from CY categories}
@@ -153,7 +153,7 @@
 Let $\cC$ be a CY$_3$ category with a chain-level $S^3$-framing on $\mathrm{HC}^-_3(\cC)$ (the condition of Conjecture~CY-A$_3$). Then the ordered bar complex of the cyclic $A_\infty$ algebra $A_\cC$ carries an $E_1$-chiral structure whose representation category is a braided monoidal refinement of the BPS Yangian of $\cC$.
 \end{conjecture}
 
-The conjecture is conditional on the chain-level framing; the unconditional statement requires the full CY-A$_3$ programme. Every downstream result in \ref{part:examples} and \ref{part:connections} that uses the BPS Yangian inherits this conditionality. The connection to Maulik-Okounkov and Costello-Witten cohomological Hall algebras is traced in Chapter~\ref{ch:cha-yangian}.
+The conjecture is conditional on the chain-level framing; the unconditional statement requires the full CY-A$_3$ programme. Every downstream result in \ref{part:examples} and \ref{part:connections} that uses the BPS Yangian inherits this conditionality. The connection to Maulik-Okounkov and Costello-Witten cohomological Hall algebras is traced in Chapter~\ref{ch:toric-coha}.
 
 \begin{proposition}[$E_2$ enhancement via Drinfeld center]
 \label{prop:e2-enhancement-drinfeld}
@@ -318,7 +318,7 @@
 
 \begin{remark}[How this chapter is used downstream]
 \label{rem:downstream-usage}
-Chapters~\ref{ch:braided-factorization}, \ref{ch:drinfeld-center}, and \ref{ch:quantum-group-reps} use this chapter as the source of the ordered bar coalgebra and the averaging map. Chapter~\ref{ch:cy-chiral-functor} uses Proposition~\ref{prop:e1-sector-d2} as the $d=2$ existence statement for $A_\cC$. Every braided monoidal category that appears later is the Drinfeld center of an underlying ordered one.
+Chapters~\ref{ch:braided-factorization}, \ref{ch:drinfeld-center}, and \ref{ch:quantum-group-reps} use this chapter as the source of the ordered bar coalgebra and the averaging map. Chapter~\ref{ch:cy-to-chiral} uses Proposition~\ref{prop:e1-sector-d2} as the $d=2$ existence statement for $A_\cC$. Every braided monoidal category that appears later is the Drinfeld center of an underlying ordered one.
 \end{remark}
 
 \section{Operadic dictionary for the CY reader}
@@ -1447,7 +1447,7 @@
 cutting the elliptic curve.}
 For the product CY$_3$ manifold $X = K3 \times E$, the factorization
 homology integral $\int_{K3} \cF|_{K3}$ of
-Section~\ref{sec:k3-perturbative-fact-homology} produces a chiral algebra
+Section~\ref{subsec:fact-homology-k3xe} produces a chiral algebra
 $A_E$ on the residual elliptic curve $E$.  The coproduct on $A_E$ arises
 from cutting $E$ into two intervals via excision.  Concretely, choose a
 collar-gluing decomposition $E = I_1 \cup_{S^0 \times \R} I_2$ (cutting
diff --git a/chapters/theory/e2_chiral_algebras.tex b/chapters/theory/e2_chiral_algebras.tex
index 4d9c49d33b9b71c9728719844b5387b9c256ec23..8a25a3037dc9569752a97c0fc75347a4033380af
--- a/chapters/theory/e2_chiral_algebras.tex
+++ b/chapters/theory/e2_chiral_algebras.tex
@@ -194,7 +194,7 @@
 \label{sec:drinfeld-center-bridge}
 
 Volume~II constructs $\Phi_{E_1}$ and proves $E_1$-chiral Koszul
-duality (see \ref{part:e1-core} of \cite{VolII}). The Drinfeld center
+duality (see Part~I of \cite{VolII}). The Drinfeld center
 $Z\colon E_1\text{-}\Cat \xrightarrow{\sim} E_2\text{-}\Cat$
 (under dualizability) is the categorical passage from ordered
 monoidal data to braided monoidal data. On the bar side it matches the
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 30392e44f20b6614f1f54981964db6c0329363e5..69d953d96d354add714abf2eec933a753336234a
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -201,7 +201,7 @@
 \]
 The SDR data $(i, p, s)$ interfaces directly with the homotopy transfer theorem (HTT), transferring the $A_\infty$-structure from \v{C}ech cochains $\check{C}^\bullet(\mathcal{E}nd(\mathcal{E}))$ to its cohomology $\mathrm{Ext}^\bullet(\mathcal{E}, \mathcal{E})$. The transferred operations $\mu_k^{\mathrm{ch}}$ are given by sums over planar trees whose internal edges are decorated by the homotopy~$s$; each application of~$s$ introduces rational functions on the affine intersections, and the resulting chiral operations are well-defined as formal power series.
 
-The scope is perturbative: the \v{C}ech homotopy produces an algebraic $A_\infty$-structure on the Ext algebra, but convergence of the resulting series to holomorphic functions (the non-perturbative statement) requires separate input from the analytic completion programme of Volume~I (MC5, \S\ref{sec:analytic-sewing}). The perturbative statement suffices for the formal CY-to-chiral functor and for all combinatorial applications in this volume. The full construction, including the proof that the SDR conditions hold and the scope qualification, is Theorem~\ref{thm:cech-contracting-homotopy} in Chapter~\ref{ch:cy-to-chiral}.
+The scope is perturbative: the \v{C}ech homotopy produces an algebraic $A_\infty$-structure on the Ext algebra, but convergence of the resulting series to holomorphic functions (the non-perturbative statement) requires separate input from the analytic completion programme of Volume~I (MC5, the analytic sewing section there). The perturbative statement suffices for the formal CY-to-chiral functor and for all combinatorial applications in this volume. The full construction, including the proof that the SDR conditions hold and the scope qualification, is Theorem~\ref{thm:cech-contracting-homotopy} in Chapter~\ref{ch:cy-to-chiral}.
 
 Three independent consistency checks confirm the resulting chiral data for the quintic: the Gepner model matrix factorization (via mirror symmetry, $\mathrm{MF}(x_1^5 + \cdots + x_5^5)$), the large-volume Hodge--Kodaira--Rosenberg limit ($\mathrm{HKR}$ degeneration of $\mathrm{Ext}^\bullet$ to Dolbeault cohomology), and the Gopakumar--Vafa integrality of the resulting genus-$g$ amplitudes. All three produce the same modular characteristic $\chi/2 = -100$ (the MacMahon-normalised form of $\kappa_{\mathrm{cat}}$ at $d=3$).
 
@@ -277,7 +277,7 @@
  \item The moonshine multiplier: $A_n = \kappa_{\mathrm{cat}} \cdot \dim(\rho_n)$ identifies the factor $2$ in $Z_{K3} = 2\,\phi_{0,1}$.
  \item The categorical $\Etwo$-obstruction for CY$_3$ (Proposition~\ref{prop:e1-obstruction-categorical}): Serre duality forces antisymmetry of the Euler form, universally obstructing $\Etwo$-enhancement without torus hypotheses.
  \item Quiver-chart gluing for toric CY$_3$ (Theorem~\ref{thm:toric-chart-gluing}): the global $\Eone$-chiral algebra is assembled as a homotopy colimit of McKay-chart CoHAs, with $E_2$ descent degeneration and Costello--Li comparison.
- \item The K3 double current algebra $\fg_{K3}$ (Definition~\ref{def:k3-double-current-algebra}): the finite-dimensional analogue of the DDCA in which $\bC[u,v]$ is replaced by $H^*(S,\bC)$ with the Mukai pairing.
+ \item The K3 double current algebra $\fg_{K3}$: the finite-dimensional analogue of the DDCA in which $\bC[u,v]$ is replaced by $H^*(S,\bC)$ with the Mukai pairing.
  \item Forty-two CY/BKM compute engines with $5{,}700{+}$ tests across the standard CY landscape.
 \end{itemize}
 
@@ -360,7 +360,7 @@
 \item \emph{Descent theorem.}
  \v{C}ech descent for $E_1$-algebras over the Bridgeland
  stability manifold. Proved for toric CY3
- (Proposition~\ref{prop:e1-descent-unobstructed}); open for
+ (Theorem~\ref{thm:toric-chart-gluing}); open for
  compact CY3 beyond the chart-atlas regime.
 \item \emph{Higher-dimensional CY shadows.}
  The $E_n$ stabilization theorem
@@ -394,12 +394,12 @@
 
 \emph{Quantum group representations} (Chapter~\ref{ch:quantum-group-reps}). The representation-theoretic target. The braided monoidal category $\mathrm{Rep}_q(\mathfrak{g})$ is what the CY programme aims to realize: Conjecture~CY-C predicts that $\mathrm{Rep}_q(\mathfrak{g}) \simeq \mathrm{Rep}^{E_2}(A_\cC)$ for a CY category $\cC(\mathfrak{g}, q)$. The Kazhdan--Lusztig equivalence $\mathrm{Rep}_q(\mathfrak{g}) \simeq \mathrm{KL}_k(\mathfrak{g})$ at roots of unity is the prototype: the Volume~I bar complex $B(V_k(\mathfrak{g}))$ encodes the quantum group $R$-matrix in its degree-$(1,1)$ component, and the DK bridge (Volume~II, MC3 for all simple types) recovers the quantum group categorical structure. The affine Yangian realization (Chapter~\ref{ch:toric-coha}) provides the $E_1$-sector; the Drinfeld center (Chapter~\ref{ch:drinfeld-center}) provides the $E_2$-enhancement.
 
-In addition to the four standard families, the toroidal and elliptic algebras chapter (Chapter~\ref{chap:toroidal-elliptic}) develops the $K3 \times E$ programme in full: the generalized root datum, the BKM superalgebra $\mathfrak{g}_{\Delta_5}$ with its Igusa cusp form denominator identity, the shadow--Siegel gap theorem, thirteen structural results (K3-1 through K3-13), all ten research programmes (A through J), and the DDCA--toroidal bridge identifying the deformed double current algebra as the rational degeneration of the quantum toroidal algebra (Conjecture~\ref{conj:ddca-toroidal-bridge}). The K3 double current algebra $\fg_{K3}$ (Chapter~\ref{ch:k3-times-e}, Definition~\ref{def:k3-double-current-algebra}) provides the K3 analogue of the DDCA, replacing $\bC[u,v]$ with $H^*(S,\bC)$. The toric CY$_3$ CoHA chapter (Chapter~\ref{ch:toric-coha}) develops the affine Yangian and $\mathcal{W}_{1+\infty}$ side: the Jordan quiver gives $Y(\widehat{\mathfrak{gl}}_1) \simeq \mathcal{W}_{1+\infty}$, the toric fan is the Dynkin data, and the shuffle algebra presentation connects to the KZ equations of Volume~I.
+In addition to the four standard families, the toroidal and elliptic algebras chapter (Chapter~\ref{chap:toroidal-elliptic}) develops the $K3 \times E$ programme in full: the generalized root datum, the BKM superalgebra $\mathfrak{g}_{\Delta_5}$ with its Igusa cusp form denominator identity, the shadow--Siegel gap theorem, thirteen structural results (K3-1 through K3-13), all ten research programmes (A through J), and the DDCA--toroidal bridge identifying the deformed double current algebra as the rational degeneration of the quantum toroidal algebra (Conjecture~\ref{conj:ddca-toroidal-bridge}). The K3 double current algebra $\fg_{K3}$, discussed in the DDCA--toroidal bridge of Chapter~\ref{ch:k3-times-e}, provides the K3 analogue of the DDCA, replacing $\bC[u,v]$ with $H^*(S,\bC)$. The toric CY$_3$ CoHA chapter (Chapter~\ref{ch:toric-coha}) develops the affine Yangian and $\mathcal{W}_{1+\infty}$ side: the Jordan quiver gives $Y(\widehat{\mathfrak{gl}}_1) \simeq \mathcal{W}_{1+\infty}$, the toric fan is the Dynkin data, and the shuffle algebra presentation connects to the KZ equations of Volume~I.
 
 \section{Guide for the reader}
 \label{sec:guide}
 
-Part~\ref{part:cy-categories} establishes the categorical foundations: CY categories, cyclic $\Ainf$-structures, the Hochschild calculus, and the $E_1$/$E_2$/$E_n$ chiral hierarchy with the framing obstruction tower. Part~\ref{part:bridge} constructs the bridge functor $\Phi$ from CY categories to quantum chiral algebras and proves Theorems CY-A (for $d = 2$) and CY-D, with the identification of automorphic correction and shadow obstruction tower as the central result. Part~\ref{part:examples} treats quantum groups and their braided factorization structure, including the Drinfeld center as the bulk algebra. Part~\ref{part:connections} works through the standard landscape: the toroidal and elliptic algebras chapter develops the $K3 \times E$ programme (K3-1 through K3-13, programmes A through J), alongside toric CY3 CoHAs, Fukaya categories, derived categories, matrix factorizations (ADE singularities and W-algebras), and quantum group representations (Kazhdan--Lusztig, affine Yangians, critical CoHAs). Part~\ref{part:frontier} connects to the geometric Langlands programme and to Volumes~I and~II via the bar-cobar bridge and the modular Koszul bridge. The working notes (\S\ref{sec:working-notes}) record the research frontier.
+Part~\ref{part:cy-categories} establishes the categorical foundations: CY categories, cyclic $\Ainf$-structures, the Hochschild calculus, and the $E_1$/$E_2$/$E_n$ chiral hierarchy with the framing obstruction tower. Part~\ref{part:bridge} constructs the bridge functor $\Phi$ from CY categories to quantum chiral algebras and proves Theorems CY-A (for $d = 2$) and CY-D, with the identification of automorphic correction and shadow obstruction tower as the central result. Part~\ref{part:examples} treats quantum groups and their braided factorization structure, including the Drinfeld center as the bulk algebra. Part~\ref{part:connections} works through the standard landscape: the toroidal and elliptic algebras chapter develops the $K3 \times E$ programme (K3-1 through K3-13, programmes A through J), alongside toric CY3 CoHAs, Fukaya categories, derived categories, matrix factorizations (ADE singularities and W-algebras), and quantum group representations (Kazhdan--Lusztig, affine Yangians, critical CoHAs). Part~\ref{part:frontier} connects to the geometric Langlands programme and to Volumes~I and~II via the bar-cobar bridge and the modular Koszul bridge. The separate working notes record the research frontier.
 
 \section{Conventions and notation}
 \label{sec:conventions-intro}

file update:
diff --git a/chapters/connections/cy_holographic_datum_master.tex b/chapters/connections/cy_holographic_datum_master.tex
index 2a66e8a0ca86f097e30b0de99c082498014430c6..b0ef34640300f22c24d57ee10a207c331065f31d
--- a/chapters/connections/cy_holographic_datum_master.tex
+++ b/chapters/connections/cy_holographic_datum_master.tex
@@ -943,7 +943,7 @@
 bar-cobar, CoHA / perverse coherent sheaves, classical CY Poisson
 coisson, MO stable envelope, affine super Yangian for toric CY$_3$,
 elliptic Sklyanin for toroidal CY, Gaudin from CY$_3$
-(Theorem~\ref{thm:cy-seven-face-master} above).
+(Conjecture~\ref{conj:cy-seven-face-master} above).
 \end{enumerate}
 The three master theorems are mutually compatible: under the CY-to-chiral
 functor $\Phi$, face~$i$ of Vol~III maps to a specialization of face~$i$
diff --git a/chapters/connections/modular_koszul_bridge.tex b/chapters/connections/modular_koszul_bridge.tex
index 1199c5aaa32e71f085dd3b7131c8f9aeadb1148c..a423d35b2ce162a9f56bb568768ae1bed7bef2f6
--- a/chapters/connections/modular_koszul_bridge.tex
+++ b/chapters/connections/modular_koszul_bridge.tex
@@ -234,7 +234,7 @@
 \end{theorem}
 
 \begin{proof}[Attribution]
-Parts (i), (iii), (iv) are Vol~I/II results (\S\ref{sec:k3e-cross-volume}, items K3-1 through K3-13, proved in the K3 modular-tower chapter of Vol~I and in the Vol~II 3D quantum gravity treatment, \ref{part:3d-qg} there). Part (ii) is the Borcherds lift of Borcherds (1998); its use as a modular characteristic is the observation of AP-CY8, not a theorem of Vol~III. The conditionality on propagates from Theorem~\ref{thm:cy-shadow-cohft}.
+Parts (i), (iii), (iv) are Vol~I/II results (\S\ref{sec:k3e-cross-volume}, items K3-1 through K3-13, proved in the K3 modular-tower chapter of Vol~I and in Part~III of Vol~II's 3D quantum gravity treatment). Part (ii) is the Borcherds lift of Borcherds (1998); its use as a modular characteristic is the observation of AP-CY8, not a theorem of Vol~III. The conditionality on propagates from Theorem~\ref{thm:cy-shadow-cohft}.
 \end{proof}
 
 \begin{remark}[Kappa-spectrum verification for $K3 \times E$]
diff --git a/chapters/examples/quantum_group_reps.tex b/chapters/examples/quantum_group_reps.tex
index e6b19a4c52de09f17af4b5f794d5f7269f4076b4..5213e6bfc9cb828c11c98b50aa32549aa228cfbf
--- a/chapters/examples/quantum_group_reps.tex
+++ b/chapters/examples/quantum_group_reps.tex
@@ -503,7 +503,7 @@
  additional data);
  \item $\kappa_{\mathrm{BKM}}$: the BKM modular weight, a
  number-theoretic invariant arising from the BKM denominator
- formula (Chapter~\ref{ch:toroidal-elliptic}; distinct from
+ formula (Chapter~\ref{chap:toroidal-elliptic}; distinct from
  both $\kappa_{\mathrm{cat}}$ and $\kappa_{\mathrm{ch}}$).
 \end{enumerate}
 For CY$_2$ categories with $\frakg$-symmetry, all three can be
diff --git a/chapters/examples/toric_cy3_coha.tex b/chapters/examples/toric_cy3_coha.tex
index 2b8821c0fd545c77e9d18a4180e8e67d3c4459be..94da66b26dadb3a8dcd2e91287fd7092ea5a944c
--- a/chapters/examples/toric_cy3_coha.tex
+++ b/chapters/examples/toric_cy3_coha.tex
@@ -205,7 +205,7 @@
 \end{theorem}
 
 \begin{proof}
-(i) The compact base $\bP^1 \times \bP^1$ has $\chi(\bP^1 \times \bP^1) = 4$ (each factor contributes $\chi(\bP^1) = 2$), so $\kappa_{\mathrm{ch}} = \chi/2 = 2$ by the general local-surface formula (Remark~\ref{rem:toric-structural-patterns}).
+(i) The compact base $\bP^1 \times \bP^1$ has $\chi(\bP^1 \times \bP^1) = 4$ (each factor contributes $\chi(\bP^1) = 2$), so $\kappa_{\mathrm{ch}} = \chi/2 = 2$ by the general local-surface formula (Remark~\ref{rem:toric-kappa-patterns}).
 
 (ii) The intersection form on $H^2(\bP^1 \times \bP^1)$ in the basis $\{e_1, e_2\}$ is $\langle e_i, e_j \rangle = \delta_{ij}$ (the two rulings are orthogonal with self-intersection $0$ in the total space, but the relevant inner product for the shadow metric is the Euler pairing $\chi(e_i, e_j) = \delta_{ij}$).
 
@@ -654,7 +654,7 @@
 the chart gluing by descent, the shadow tower by the MC equation.
 These components are \emph{a priori} separate structures on the
 same algebra. The Vol~I chiral quantum group equivalence
-(Theorem~\ref{thm:chiral-qg-equiv}) asserts that three of them
+asserts that three of them
 (the vertex $R$-matrix, the chiral $A_\infty$-structure, and the
 chiral coproduct) determine each other on the Koszul locus. The theorem
 below specializes the abstract equivalence to the toric CY3 setting,
@@ -746,8 +746,7 @@
 
 \begin{proof}
 The abstract equivalence (I) $\leftrightarrow$ (II)
-$\leftrightarrow$ (III) is
-Theorem~\ref{thm:chiral-qg-equiv} of Vol~I, proved for any
+$\leftrightarrow$ (III) is the Vol~I chiral quantum group equivalence, proved for any
 $\Eone$-chiral algebra on the Koszul locus. The content of the
 present theorem is the identification of each abstract vertex
 with the independently constructed toric CY3 structure.
@@ -755,7 +754,7 @@
 \textit{Component~\textup{(I)}: $R$-matrix.}
 The $\Eone$-chiral algebra $A_X$ carries a vertex
 $R$-matrix by the general theory
-(Theorem~\ref{thm:chiral-qg-equiv}(I)). For toric CY3, the
+(item~\textup{(I)} of that equivalence). For toric CY3, the
 Maulik--Okounkov stable-envelope construction provides an
 independent $R$-matrix on $Y^+(\widehat{\fg}_{Q_X})$-modules.
 The two coincide because both solve the same Yang--Baxter
diff --git a/chapters/examples/toroidal_elliptic.tex b/chapters/examples/toroidal_elliptic.tex
index 8fcef3a49b8fe0bd45c3ae248676e994ece0ca7e..0a15b2c062f601ea29e50e3e3771b3eb1544db50
--- a/chapters/examples/toroidal_elliptic.tex
+++ b/chapters/examples/toroidal_elliptic.tex
@@ -5940,8 +5940,7 @@
 
 The K3 analogue of this picture replaces $\bC^2$ by a K3
 surface~$S$: the K3 double current algebra $\fg_{K3}$
-(Chapter~\ref{ch:k3-times-e},
-Definition~\ref{def:k3-double-current-algebra}) substitutes
+substitutes
 $H^*(S,\bC)$ for $\bC[u,v]$ and the Mukai pairing for the
 polynomial residue. Its quantization should produce a
 ``K3 Yangian'' standing in the same relation to $\fg_{K3}$ as the
@@ -6018,7 +6017,7 @@
   At $t \to 1$: the second parameter $w$ decouples and
   $\Delta_{z,w}$ reduces to the single-parameter
   Drinfeld coproduct $\Delta_z(T(u)) = T(u) \otimes T(u - z)$
-  of Theorem~\textup{\ref{thm:w-infty-chiral-qg}}.
+  of Proposition~\textup{\ref{prop:universal-coproduct}}.
 \end{enumerate}
 No two-parameter coproduct $\Delta_{z,w}$ currently exists in
 the literature or in this programme's compute infrastructure.
@@ -6034,7 +6033,7 @@
   $(q_1,q_2,q_3)$.
 \item Promote the DDCA shadow to an explicit $\Delta_{z,w}$
   formula aligned with the $R(u,v)$ surface in
-  \S\ref{subsec:quantum-chiral-algebras-6d}.
+  \S\ref{subsec:chiral-qg-wilson}.
 \item Build a compute witness at low modes: $w = 0$ reduces
   to existing $\Delta_z$; rational limit gives the DDCA
   shift; Miki sends $\Delta_{z,w} \to \Delta_{w,z}$.
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index ddbdfe60d9c9df04ba6f3acf48deee73523a64dc..3ce4e679084f2f25672104c7a00684df5e9f3b26
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -320,7 +320,7 @@
 Drinfeld coproduct from spin~$2$ to arbitrary spin, with the
 universal Miura coefficient $(\Psi{-}1)/\Psi$ on the leading
 cross-term $J \otimes W_{s-1}$ at every spin $s \ge 2$
-(Theorem~\ref{thm:miura-cross-universality}).
+(Proposition~\ref{prop:universal-coproduct}).
 
 \bigskip
 
@@ -328,7 +328,7 @@
 Volume~I defines $E_1$-chiral quantum groups abstractly. This
 volume constructs them concretely from CY geometry. The
 $E_1$-chiral bialgebra axioms (formalized in
-\S\ref{sec:e1-chiral-bialgebra}) require: (H1)~an $E_1$-chiral
+\S\ref{sec:e1-chiral-bialgebras}) require: (H1)~an $E_1$-chiral
 algebra $A$ on a curve $X$; (H2)~a spectral coproduct
 $\Delta_z \colon A \to A \otimes A$ (living on the OPEN/$E_1$
 colour); (H3)~an $R$-matrix $R(z)$ satisfying YBE; (H4)~RTT
diff --git a/chapters/theory/cy_categories.tex b/chapters/theory/cy_categories.tex
index f9b51871c44fa18a574c02fce8aaa49a49aa9c61..00d723a1cb5d4f2355a10cb2d9d3f86688259f09
--- a/chapters/theory/cy_categories.tex
+++ b/chapters/theory/cy_categories.tex
@@ -166,7 +166,7 @@
 Every smooth proper CY$_d$ category admits a cyclic $\Ainf$-enhancement, unique up to $\Ainf$-quasi-isomorphism preserving the pairing. The proof is due to Kontsevich--Soibelman in the formal case, Costello~\cite{Costello2005} for the TCFT enhancement, and Seidel~\cite{Seidel2008} for the Fukaya case.
 \end{theorem}
 
-At $d = 2$ the enhancement is explicit enough to compute directly; it drives the $K3$ computations feeding the Borcherds denominator (Vol~III Chapter~\ref{ch:k3}). At $d = 3$ the enhancement was constructed by Sheridan~\cite{Sheridan2015} for the quintic threefold, as part of the HMS proof; the general $d = 3$ construction remains programme-level (conditional on $\bS^3$-framing, see AP-CY6).
+At $d = 2$ the enhancement is explicit enough to compute directly; it drives the $K3$ computations feeding the Borcherds denominator (Vol~III Chapter~\ref{ch:k3-times-e}). At $d = 3$ the enhancement was constructed by Sheridan~\cite{Sheridan2015} for the quintic threefold, as part of the HMS proof; the general $d = 3$ construction remains programme-level (conditional on $\bS^3$-framing, see AP-CY6).
 
 \section{Interface with the CY-to-chiral functor $\Phi$}
 \label{sec:cy-cat-phi-interface}
@@ -194,7 +194,7 @@
 
 \begin{remark}[What $\Phi$ does not see]
 \label{rem:phi-does-not-see}
-Not every invariant of $\cC$ survives the passage through $\Phi$. The functor retains the cyclic $\Ainf$-structure and the Gerstenhaber bracket; it loses the fine structure of the triangulated / $\Ainf$ category (individual objects, t-structures, stability conditions) that is visible only via the fuller categorical CoHA construction of Chapter~\ref{ch:coha}. The kappa-spectrum (Vol~III CLAUDE.md) encodes which invariants survive: $\kappa_\mathrm{cat}$ is always present, $\kappa_\mathrm{ch}$ exists only when $\Phi$ is defined, and $\kappa_\mathrm{BKM}$ records the Borcherds-side lift for $K3 \times E$.
+Not every invariant of $\cC$ survives the passage through $\Phi$. The functor retains the cyclic $\Ainf$-structure and the Gerstenhaber bracket; it loses the fine structure of the triangulated / $\Ainf$ category (individual objects, t-structures, stability conditions) that is visible only via the fuller categorical CoHA construction of Chapter~\ref{ch:toric-coha}. The kappa-spectrum (Vol~III CLAUDE.md) encodes which invariants survive: $\kappa_\mathrm{cat}$ is always present, $\kappa_\mathrm{ch}$ exists only when $\Phi$ is defined, and $\kappa_\mathrm{BKM}$ records the Borcherds-side lift for $K3 \times E$.
 \end{remark}
 
 \begin{remark}[Cross-volume conventions]
diff --git a/chapters/theory/cy_to_chiral.tex b/chapters/theory/cy_to_chiral.tex
index 030fed4a9a2a7009ae05fdb0f3c431c8aed1fc83..14526e0aba63169841056220749304799a57fe10
--- a/chapters/theory/cy_to_chiral.tex
+++ b/chapters/theory/cy_to_chiral.tex
@@ -618,8 +618,8 @@
 homotopy is purely algebraic: it acts by
 $s(f_{i_0 \cdots i_q}) = f_{0 i_0 \cdots i_q}$ on \v{C}ech cochains and
 involves no PDE solving. The SDR data $(i, p, s)$ interfaces directly
-with the homotopy transfer theorem
-\textup{(}HTT, Theorem~\textup{\ref{thm:htt-general}}\textup{)},
+with the standard homotopy transfer theorem
+\textup{(}HTT\textup{)},
 transferring the $\Ainf$-structure from $\check{C}^\bullet(\cE nd(\cE))$
 to its cohomology $\Ext^\bullet(\cE, \cE)$.
 \end{theorem}
@@ -652,7 +652,7 @@
 (whether the formal series in the OPE coefficients converges to
 define honest holomorphic functions) requires separate input from
 the analytic completion programme (MC5,
-\S\ref{sec:analytic-sewing} of Vol~I). Specifically: the HTT
+the analytic sewing section of Vol~I). Specifically: the HTT
 produces transferred operations $\mu_k^{\mathrm{ch}}$ whose
 coefficients involve iterated applications of~$s$; each application
 introduces rational functions on the intersections $U_{i_0} \cap
@@ -1972,7 +1972,7 @@
  \bottomrule
 \end{tabular}
 \end{center}
-{\footnotesize $^*$The K3 entry records $\kappa_{\mathrm{ch}} = \chi(\cO_{\mathrm{K3}}) = 2$ (Proposition~\ref{prop:cy-kappa-d2}; verified via chiral de Rham, Chapter~\ref{ch:k3-times-e}). The distinct quantity $\dim \HH_*(D^b(\mathrm{K3}))/2 = 12$ arises from an alternative algebraization (the Monster orbifold); the full trichotomy ($\kappa_{\mathrm{ch}} \in \{2, 12, 24\}$) is developed in Section~\ref{subsec:k3-three-algebraizations} of Chapter~\ref{ch:k3-times-e}.
+{\footnotesize $^*$The K3 entry records $\kappa_{\mathrm{ch}} = \chi(\cO_{\mathrm{K3}}) = 2$ (Proposition~\ref{prop:cy-kappa-d2}; verified via chiral de Rham, Chapter~\ref{ch:k3-times-e}). The distinct quantity $\dim \HH_*(D^b(\mathrm{K3}))/2 = 12$ arises from an alternative algebraization (the Monster orbifold); the full trichotomy ($\kappa_{\mathrm{ch}} \in \{2, 12, 24\}$) is developed in the K3 discussion of Chapter~\ref{ch:k3-times-e}.
 
 $^\dagger$The $K3 \times E$ entry records $\kappa_{\mathrm{ch}} = 3$ by additivity (Proposition~\ref{prop:categorical-euler}: $\kappa_{\mathrm{ch}}(\mathrm{K3}) + \kappa_{\mathrm{ch}}(E) = 2 + 1$). The Borcherds automorphic weight is $\kappa_{\mathrm{BKM}} = 5 = \mathrm{wt}(\Delta_5)$, a distinct invariant.}
 
diff --git a/chapters/theory/drinfeld_center.tex b/chapters/theory/drinfeld_center.tex
index ac67d4e3a2ed8fab94fcb3fc63933d8650a92ac9..a711d853438f9e6a0e6fdd4e5dac61154b7b3c24
--- a/chapters/theory/drinfeld_center.tex
+++ b/chapters/theory/drinfeld_center.tex
@@ -726,7 +726,7 @@
 produces only symmetric braiding. The distinction is the
 deep reason for the $\Eone$ stabilization theorem
 (Chapter~\ref{ch:cy-to-chiral},
-Theorem~\ref{thm:e1-stabilization}).
+Theorem~\ref{thm:e1-stabilization-cy}).
 
 \begin{proposition}[$E_3$ restriction gives symmetric braiding]
 \label{prop:e3-symmetric-braiding}
diff --git a/chapters/theory/e1_chiral_algebras.tex b/chapters/theory/e1_chiral_algebras.tex
index 75484d2fff759dc21313b5595a8abade7d55d203..b533b2f5640db9eba4046a61106787f2c19a0d53
--- a/chapters/theory/e1_chiral_algebras.tex
+++ b/chapters/theory/e1_chiral_algebras.tex
@@ -63,7 +63,7 @@
 via holomorphic Chern--Simons; conjectural in general).
 The further $E_3$-topological upgrade requires a conformal
 vector at non-critical level
-(Volume~I, Theorem~\textup{\ref*{thm:topologization}}).
+(Volume~I, the topologization theorem).
 \end{definition}
 
 The closed colour carries $E_2$ structure from
@@ -128,7 +128,7 @@
 
 \begin{remark}[Three bars, one functor]
 \label{rem:three-bars-vol3}
-The CY-to-chiral functor $\Phi$ of Chapter~\ref{ch:cy-chiral-functor} has three natural composites. $\Phi_{E_1}$ produces $B^{\mathrm{ord}}(A_C)$; this is the ordered bar sensed by the Yangian. $\mathrm{av} \circ \Phi_{E_1}$ produces $B^{\Sigma}(A_C)$; this is the symmetric bar sensed by the modular characteristic $\kappa_{\mathrm{ch}}$. The full $E_2$ enhancement $\Phi_{E_2}$ produces the Drinfeld-centered bar $B^{E_2}(A_C) = \cZ(B^{\mathrm{ord}}(A_C))$; this is the braided bar sensed by the quantum group. All three factor through $\Phi_{E_1}$. This is the volume's motto: the ordered bar is the primitive.
+The CY-to-chiral functor $\Phi$ of Chapter~\ref{ch:cy-to-chiral} has three natural composites. $\Phi_{E_1}$ produces $B^{\mathrm{ord}}(A_C)$; this is the ordered bar sensed by the Yangian. $\mathrm{av} \circ \Phi_{E_1}$ produces $B^{\Sigma}(A_C)$; this is the symmetric bar sensed by the modular characteristic $\kappa_{\mathrm{ch}}$. The full $E_2$ enhancement $\Phi_{E_2}$ produces the Drinfeld-centered bar $B^{E_2}(A_C) = \cZ(B^{\mathrm{ord}}(A_C))$; this is the braided bar sensed by the quantum group. All three factor through $\Phi_{E_1}$. This is the volume's motto: the ordered bar is the primitive.
 \end{remark}
 
 \section{$E_1$-chiral algebras from CY categories}
@@ -153,7 +153,7 @@
 Let $\cC$ be a CY$_3$ category with a chain-level $S^3$-framing on $\mathrm{HC}^-_3(\cC)$ (the condition of Conjecture~CY-A$_3$). Then the ordered bar complex of the cyclic $A_\infty$ algebra $A_\cC$ carries an $E_1$-chiral structure whose representation category is a braided monoidal refinement of the BPS Yangian of $\cC$.
 \end{conjecture}
 
-The conjecture is conditional on the chain-level framing; the unconditional statement requires the full CY-A$_3$ programme. Every downstream result in \ref{part:examples} and \ref{part:connections} that uses the BPS Yangian inherits this conditionality. The connection to Maulik-Okounkov and Costello-Witten cohomological Hall algebras is traced in Chapter~\ref{ch:cha-yangian}.
+The conjecture is conditional on the chain-level framing; the unconditional statement requires the full CY-A$_3$ programme. Every downstream result in \ref{part:examples} and \ref{part:connections} that uses the BPS Yangian inherits this conditionality. The connection to Maulik-Okounkov and Costello-Witten cohomological Hall algebras is traced in Chapter~\ref{ch:toric-coha}.
 
 \begin{proposition}[$E_2$ enhancement via Drinfeld center]
 \label{prop:e2-enhancement-drinfeld}
@@ -318,7 +318,7 @@
 
 \begin{remark}[How this chapter is used downstream]
 \label{rem:downstream-usage}
-Chapters~\ref{ch:braided-factorization}, \ref{ch:drinfeld-center}, and \ref{ch:quantum-group-reps} use this chapter as the source of the ordered bar coalgebra and the averaging map. Chapter~\ref{ch:cy-chiral-functor} uses Proposition~\ref{prop:e1-sector-d2} as the $d=2$ existence statement for $A_\cC$. Every braided monoidal category that appears later is the Drinfeld center of an underlying ordered one.
+Chapters~\ref{ch:braided-factorization}, \ref{ch:drinfeld-center}, and \ref{ch:quantum-group-reps} use this chapter as the source of the ordered bar coalgebra and the averaging map. Chapter~\ref{ch:cy-to-chiral} uses Proposition~\ref{prop:e1-sector-d2} as the $d=2$ existence statement for $A_\cC$. Every braided monoidal category that appears later is the Drinfeld center of an underlying ordered one.
 \end{remark}
 
 \section{Operadic dictionary for the CY reader}
@@ -1447,7 +1447,7 @@
 cutting the elliptic curve.}
 For the product CY$_3$ manifold $X = K3 \times E$, the factorization
 homology integral $\int_{K3} \cF|_{K3}$ of
-Section~\ref{sec:k3-perturbative-fact-homology} produces a chiral algebra
+Section~\ref{subsec:fact-homology-k3xe} produces a chiral algebra
 $A_E$ on the residual elliptic curve $E$.  The coproduct on $A_E$ arises
 from cutting $E$ into two intervals via excision.  Concretely, choose a
 collar-gluing decomposition $E = I_1 \cup_{S^0 \times \R} I_2$ (cutting
diff --git a/chapters/theory/e2_chiral_algebras.tex b/chapters/theory/e2_chiral_algebras.tex
index 4d9c49d33b9b71c9728719844b5387b9c256ec23..8a25a3037dc9569752a97c0fc75347a4033380af
--- a/chapters/theory/e2_chiral_algebras.tex
+++ b/chapters/theory/e2_chiral_algebras.tex
@@ -194,7 +194,7 @@
 \label{sec:drinfeld-center-bridge}
 
 Volume~II constructs $\Phi_{E_1}$ and proves $E_1$-chiral Koszul
-duality (see \ref{part:e1-core} of \cite{VolII}). The Drinfeld center
+duality (see Part~I of \cite{VolII}). The Drinfeld center
 $Z\colon E_1\text{-}\Cat \xrightarrow{\sim} E_2\text{-}\Cat$
 (under dualizability) is the categorical passage from ordered
 monoidal data to braided monoidal data. On the bar side it matches the
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 30392e44f20b6614f1f54981964db6c0329363e5..69d953d96d354add714abf2eec933a753336234a
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -201,7 +201,7 @@
 \]
 The SDR data $(i, p, s)$ interfaces directly with the homotopy transfer theorem (HTT), transferring the $A_\infty$-structure from \v{C}ech cochains $\check{C}^\bullet(\mathcal{E}nd(\mathcal{E}))$ to its cohomology $\mathrm{Ext}^\bullet(\mathcal{E}, \mathcal{E})$. The transferred operations $\mu_k^{\mathrm{ch}}$ are given by sums over planar trees whose internal edges are decorated by the homotopy~$s$; each application of~$s$ introduces rational functions on the affine intersections, and the resulting chiral operations are well-defined as formal power series.
 
-The scope is perturbative: the \v{C}ech homotopy produces an algebraic $A_\infty$-structure on the Ext algebra, but convergence of the resulting series to holomorphic functions (the non-perturbative statement) requires separate input from the analytic completion programme of Volume~I (MC5, \S\ref{sec:analytic-sewing}). The perturbative statement suffices for the formal CY-to-chiral functor and for all combinatorial applications in this volume. The full construction, including the proof that the SDR conditions hold and the scope qualification, is Theorem~\ref{thm:cech-contracting-homotopy} in Chapter~\ref{ch:cy-to-chiral}.
+The scope is perturbative: the \v{C}ech homotopy produces an algebraic $A_\infty$-structure on the Ext algebra, but convergence of the resulting series to holomorphic functions (the non-perturbative statement) requires separate input from the analytic completion programme of Volume~I (MC5, the analytic sewing section there). The perturbative statement suffices for the formal CY-to-chiral functor and for all combinatorial applications in this volume. The full construction, including the proof that the SDR conditions hold and the scope qualification, is Theorem~\ref{thm:cech-contracting-homotopy} in Chapter~\ref{ch:cy-to-chiral}.
 
 Three independent consistency checks confirm the resulting chiral data for the quintic: the Gepner model matrix factorization (via mirror symmetry, $\mathrm{MF}(x_1^5 + \cdots + x_5^5)$), the large-volume Hodge--Kodaira--Rosenberg limit ($\mathrm{HKR}$ degeneration of $\mathrm{Ext}^\bullet$ to Dolbeault cohomology), and the Gopakumar--Vafa integrality of the resulting genus-$g$ amplitudes. All three produce the same modular characteristic $\chi/2 = -100$ (the MacMahon-normalised form of $\kappa_{\mathrm{cat}}$ at $d=3$).
 
@@ -277,7 +277,7 @@
  \item The moonshine multiplier: $A_n = \kappa_{\mathrm{cat}} \cdot \dim(\rho_n)$ identifies the factor $2$ in $Z_{K3} = 2\,\phi_{0,1}$.
  \item The categorical $\Etwo$-obstruction for CY$_3$ (Proposition~\ref{prop:e1-obstruction-categorical}): Serre duality forces antisymmetry of the Euler form, universally obstructing $\Etwo$-enhancement without torus hypotheses.
  \item Quiver-chart gluing for toric CY$_3$ (Theorem~\ref{thm:toric-chart-gluing}): the global $\Eone$-chiral algebra is assembled as a homotopy colimit of McKay-chart CoHAs, with $E_2$ descent degeneration and Costello--Li comparison.
- \item The K3 double current algebra $\fg_{K3}$ (Definition~\ref{def:k3-double-current-algebra}): the finite-dimensional analogue of the DDCA in which $\bC[u,v]$ is replaced by $H^*(S,\bC)$ with the Mukai pairing.
+ \item The K3 double current algebra $\fg_{K3}$: the finite-dimensional analogue of the DDCA in which $\bC[u,v]$ is replaced by $H^*(S,\bC)$ with the Mukai pairing.
  \item Forty-two CY/BKM compute engines with $5{,}700{+}$ tests across the standard CY landscape.
 \end{itemize}
 
@@ -360,7 +360,7 @@
 \item \emph{Descent theorem.}
  \v{C}ech descent for $E_1$-algebras over the Bridgeland
  stability manifold. Proved for toric CY3
- (Proposition~\ref{prop:e1-descent-unobstructed}); open for
+ (Theorem~\ref{thm:toric-chart-gluing}); open for
  compact CY3 beyond the chart-atlas regime.
 \item \emph{Higher-dimensional CY shadows.}
  The $E_n$ stabilization theorem
@@ -394,12 +394,12 @@
 
 \emph{Quantum group representations} (Chapter~\ref{ch:quantum-group-reps}). The representation-theoretic target. The braided monoidal category $\mathrm{Rep}_q(\mathfrak{g})$ is what the CY programme aims to realize: Conjecture~CY-C predicts that $\mathrm{Rep}_q(\mathfrak{g}) \simeq \mathrm{Rep}^{E_2}(A_\cC)$ for a CY category $\cC(\mathfrak{g}, q)$. The Kazhdan--Lusztig equivalence $\mathrm{Rep}_q(\mathfrak{g}) \simeq \mathrm{KL}_k(\mathfrak{g})$ at roots of unity is the prototype: the Volume~I bar complex $B(V_k(\mathfrak{g}))$ encodes the quantum group $R$-matrix in its degree-$(1,1)$ component, and the DK bridge (Volume~II, MC3 for all simple types) recovers the quantum group categorical structure. The affine Yangian realization (Chapter~\ref{ch:toric-coha}) provides the $E_1$-sector; the Drinfeld center (Chapter~\ref{ch:drinfeld-center}) provides the $E_2$-enhancement.
 
-In addition to the four standard families, the toroidal and elliptic algebras chapter (Chapter~\ref{chap:toroidal-elliptic}) develops the $K3 \times E$ programme in full: the generalized root datum, the BKM superalgebra $\mathfrak{g}_{\Delta_5}$ with its Igusa cusp form denominator identity, the shadow--Siegel gap theorem, thirteen structural results (K3-1 through K3-13), all ten research programmes (A through J), and the DDCA--toroidal bridge identifying the deformed double current algebra as the rational degeneration of the quantum toroidal algebra (Conjecture~\ref{conj:ddca-toroidal-bridge}). The K3 double current algebra $\fg_{K3}$ (Chapter~\ref{ch:k3-times-e}, Definition~\ref{def:k3-double-current-algebra}) provides the K3 analogue of the DDCA, replacing $\bC[u,v]$ with $H^*(S,\bC)$. The toric CY$_3$ CoHA chapter (Chapter~\ref{ch:toric-coha}) develops the affine Yangian and $\mathcal{W}_{1+\infty}$ side: the Jordan quiver gives $Y(\widehat{\mathfrak{gl}}_1) \simeq \mathcal{W}_{1+\infty}$, the toric fan is the Dynkin data, and the shuffle algebra presentation connects to the KZ equations of Volume~I.
+In addition to the four standard families, the toroidal and elliptic algebras chapter (Chapter~\ref{chap:toroidal-elliptic}) develops the $K3 \times E$ programme in full: the generalized root datum, the BKM superalgebra $\mathfrak{g}_{\Delta_5}$ with its Igusa cusp form denominator identity, the shadow--Siegel gap theorem, thirteen structural results (K3-1 through K3-13), all ten research programmes (A through J), and the DDCA--toroidal bridge identifying the deformed double current algebra as the rational degeneration of the quantum toroidal algebra (Conjecture~\ref{conj:ddca-toroidal-bridge}). The K3 double current algebra $\fg_{K3}$, discussed in the DDCA--toroidal bridge of Chapter~\ref{ch:k3-times-e}, provides the K3 analogue of the DDCA, replacing $\bC[u,v]$ with $H^*(S,\bC)$. The toric CY$_3$ CoHA chapter (Chapter~\ref{ch:toric-coha}) develops the affine Yangian and $\mathcal{W}_{1+\infty}$ side: the Jordan quiver gives $Y(\widehat{\mathfrak{gl}}_1) \simeq \mathcal{W}_{1+\infty}$, the toric fan is the Dynkin data, and the shuffle algebra presentation connects to the KZ equations of Volume~I.
 
 \section{Guide for the reader}
 \label{sec:guide}
 
-Part~\ref{part:cy-categories} establishes the categorical foundations: CY categories, cyclic $\Ainf$-structures, the Hochschild calculus, and the $E_1$/$E_2$/$E_n$ chiral hierarchy with the framing obstruction tower. Part~\ref{part:bridge} constructs the bridge functor $\Phi$ from CY categories to quantum chiral algebras and proves Theorems CY-A (for $d = 2$) and CY-D, with the identification of automorphic correction and shadow obstruction tower as the central result. Part~\ref{part:examples} treats quantum groups and their braided factorization structure, including the Drinfeld center as the bulk algebra. Part~\ref{part:connections} works through the standard landscape: the toroidal and elliptic algebras chapter develops the $K3 \times E$ programme (K3-1 through K3-13, programmes A through J), alongside toric CY3 CoHAs, Fukaya categories, derived categories, matrix factorizations (ADE singularities and W-algebras), and quantum group representations (Kazhdan--Lusztig, affine Yangians, critical CoHAs). Part~\ref{part:frontier} connects to the geometric Langlands programme and to Volumes~I and~II via the bar-cobar bridge and the modular Koszul bridge. The working notes (\S\ref{sec:working-notes}) record the research frontier.
+Part~\ref{part:cy-categories} establishes the categorical foundations: CY categories, cyclic $\Ainf$-structures, the Hochschild calculus, and the $E_1$/$E_2$/$E_n$ chiral hierarchy with the framing obstruction tower. Part~\ref{part:bridge} constructs the bridge functor $\Phi$ from CY categories to quantum chiral algebras and proves Theorems CY-A (for $d = 2$) and CY-D, with the identification of automorphic correction and shadow obstruction tower as the central result. Part~\ref{part:examples} treats quantum groups and their braided factorization structure, including the Drinfeld center as the bulk algebra. Part~\ref{part:connections} works through the standard landscape: the toroidal and elliptic algebras chapter develops the $K3 \times E$ programme (K3-1 through K3-13, programmes A through J), alongside toric CY3 CoHAs, Fukaya categories, derived categories, matrix factorizations (ADE singularities and W-algebras), and quantum group representations (Kazhdan--Lusztig, affine Yangians, critical CoHAs). Part~\ref{part:frontier} connects to the geometric Langlands programme and to Volumes~I and~II via the bar-cobar bridge and the modular Koszul bridge. The separate working notes record the research frontier.
 
 \section{Conventions and notation}
 \label{sec:conventions-intro}

codex
The patch is in. I’m doing a coherence read on the touched paragraphs now, then I’ll rerun the narrow build and grep the edited files for the previously broken label names so the fix is evidence-backed, not assumed.
exec
/bin/zsh -lc "sed -n '320,336p' chapters/frame/preface.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "sed -n '198,206p' chapters/theory/introduction.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "sed -n '360,404p' chapters/theory/introduction.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "sed -n '278,284p' chapters/theory/introduction.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "sed -n '60,68p' chapters/theory/e1_chiral_algebras.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "sed -n '650,766p' chapters/examples/toric_cy3_coha.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "sed -n '1438,1454p' chapters/theory/e1_chiral_algebras.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "sed -n '127,158p' chapters/theory/e1_chiral_algebras.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "sed -n '232,240p' chapters/connections/modular_koszul_bridge.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "sed -n '5938,6042p' chapters/examples/toroidal_elliptic.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "sed -n '938,948p' chapters/connections/cy_holographic_datum_master.tex" in /Users/raeez/calabi-yau-quantum-groups succeeded in 51ms:
Drinfeld coproduct from spin~$2$ to arbitrary spin, with the
universal Miura coefficient $(\Psi{-}1)/\Psi$ on the leading
cross-term $J \otimes W_{s-1}$ at every spin $s \ge 2$
(Proposition~\ref{prop:universal-coproduct}).

\bigskip

\noindent\textbf{The $E_1$-chiral bialgebra.}
Volume~I defines $E_1$-chiral quantum groups abstractly. This
volume constructs them concretely from CY geometry. The
$E_1$-chiral bialgebra axioms (formalized in
\S\ref{sec:e1-chiral-bialgebras}) require: (H1)~an $E_1$-chiral
algebra $A$ on a curve $X$; (H2)~a spectral coproduct
$\Delta_z \colon A \to A \otimes A$ (living on the OPEN/$E_1$
colour); (H3)~an $R$-matrix $R(z)$ satisfying YBE; (H4)~RTT
compatibility; (H5)~a modular MC tower extending to all genera.
The ordered bar $B^{\mathrm{ord}}(A)$ preserves the $R$-matrix;
 succeeded in 50ms:
 s^2 = 0, \qquad
 s \circ i = 0, \qquad
 p \circ s = 0.
\]
The SDR data $(i, p, s)$ interfaces directly with the homotopy transfer theorem (HTT), transferring the $A_\infty$-structure from \v{C}ech cochains $\check{C}^\bullet(\mathcal{E}nd(\mathcal{E}))$ to its cohomology $\mathrm{Ext}^\bullet(\mathcal{E}, \mathcal{E})$. The transferred operations $\mu_k^{\mathrm{ch}}$ are given by sums over planar trees whose internal edges are decorated by the homotopy~$s$; each application of~$s$ introduces rational functions on the affine intersections, and the resulting chiral operations are well-defined as formal power series.

The scope is perturbative: the \v{C}ech homotopy produces an algebraic $A_\infty$-structure on the Ext algebra, but convergence of the resulting series to holomorphic functions (the non-perturbative statement) requires separate input from the analytic completion programme of Volume~I (MC5, the analytic sewing section there). The perturbative statement suffices for the formal CY-to-chiral functor and for all combinatorial applications in this volume. The full construction, including the proof that the SDR conditions hold and the scope qualification, is Theorem~\ref{thm:cech-contracting-homotopy} in Chapter~\ref{ch:cy-to-chiral}.

Three independent consistency checks confirm the resulting chiral data for the quintic: the Gepner model matrix factorization (via mirror symmetry, $\mathrm{MF}(x_1^5 + \cdots + x_5^5)$), the large-volume Hodge--Kodaira--Rosenberg limit ($\mathrm{HKR}$ degeneration of $\mathrm{Ext}^\bullet$ to Dolbeault cohomology), and the Gopakumar--Vafa integrality of the resulting genus-$g$ amplitudes. All three produce the same modular characteristic $\chi/2 = -100$ (the MacMahon-normalised form of $\kappa_{\mathrm{cat}}$ at $d=3$).
 succeeded in 52ms:
 \item The categorical $\Etwo$-obstruction for CY$_3$ (Proposition~\ref{prop:e1-obstruction-categorical}): Serre duality forces antisymmetry of the Euler form, universally obstructing $\Etwo$-enhancement without torus hypotheses.
 \item Quiver-chart gluing for toric CY$_3$ (Theorem~\ref{thm:toric-chart-gluing}): the global $\Eone$-chiral algebra is assembled as a homotopy colimit of McKay-chart CoHAs, with $E_2$ descent degeneration and Costello--Li comparison.
 \item The K3 double current algebra $\fg_{K3}$: the finite-dimensional analogue of the DDCA in which $\bC[u,v]$ is replaced by $H^*(S,\bC)$ with the Mukai pairing.
 \item Forty-two CY/BKM compute engines with $5{,}700{+}$ tests across the standard CY landscape.
\end{itemize}

\noindent\textbf{Rigorous proof sketches (completable with effort):}
 succeeded in 52ms:
\item \emph{Descent theorem.}
 \v{C}ech descent for $E_1$-algebras over the Bridgeland
 stability manifold. Proved for toric CY3
 (Theorem~\ref{thm:toric-chart-gluing}); open for
 compact CY3 beyond the chart-atlas regime.
\item \emph{Higher-dimensional CY shadows.}
 The $E_n$ stabilization theorem
 (Theorem~\ref{thm:e1-stabilization-cy}) gives a Bott-periodic
 8-fold pattern. For CY4: the $p_1$ Pontryagin class controls
 the shifted symplectic structure.
 For $K3 \times K3$: the Hopf decomposition
 $\mathbb{S}^4 = \mathbb{S}^2 \times \mathbb{S}^2$
 gives $E_2$ by Dunn additivity.
\item \emph{Convergence vs divergence.}
 The shadow partition function converges with radius $2\pi$
 (Bernoulli decay); the topological string diverges
 (Gevrey-$1$). The programme: quantify the instanton gap
 $F_g^{\mathrm{top}} - F_g^{\mathrm{sh}}$ at each genus, and
 determine whether the shadow tower is Borel-summable to the
 full amplitude.
 succeeded in 51ms:
two-coloured operad. Dunn additivity does not apply.
The $E_3$-chiral upgrade requires a 3d
holomorphic-topological theory (proved for Kac--Moody
via holomorphic Chern--Simons; conjectural in general).
The further $E_3$-topological upgrade requires a conformal
vector at non-critical level
(Volume~I, the topologization theorem).
\end{definition}

 succeeded in 52ms:
  \int_{U_1} \cF \;\otimes_{\int_{N \times \R} \cF}\;
  \int_{U_2} \cF.
\]
No mode expansion or Miura-type factorization is needed:
the excision gluing data is carried by the cosheaf structure of $\cF$
on $\Ran(\C^3)$.

\medskip
\noindent\textbf{(2) $K3 \times E$: the $E$-direction coproduct from
cutting the elliptic curve.}
For the product CY$_3$ manifold $X = K3 \times E$, the factorization
homology integral $\int_{K3} \cF|_{K3}$ of
Section~\ref{subsec:fact-homology-k3xe} produces a chiral algebra
$A_E$ on the residual elliptic curve $E$.  The coproduct on $A_E$ arises
from cutting $E$ into two intervals via excision.  Concretely, choose a
collar-gluing decomposition $E = I_1 \cup_{S^0 \times \R} I_2$ (cutting
$E$ at two points into two intervals $I_1, I_2$ with collar
 succeeded in 52ms:
of the chiral quantum group datum for toric CY3 without compact
$4$-cycles. The components are proved independently: the CoHA
bialgebra by Schiffmann--Vasserot and RSYZ, the $R$-matrix by
Maulik--Okounkov, the Drinfeld double by triangular decomposition,
the chart gluing by descent, the shadow tower by the MC equation.
These components are \emph{a priori} separate structures on the
same algebra. The Vol~I chiral quantum group equivalence
asserts that three of them
(the vertex $R$-matrix, the chiral $A_\infty$-structure, and the
chiral coproduct) determine each other on the Koszul locus. The theorem
below specializes the abstract equivalence to the toric CY3 setting,
where both sides are independently known, yielding the strongest
unconditional statement: the RSYZ bialgebra coproduct, the MO
$R$-matrix, and the bar-differential $A_\infty$-structure are three
faces of a single object.

\begin{theorem}[Chiral quantum group equivalence for toric CY3]
\label{thm:toric-chiral-qg-specialization}
\ClaimStatusProvedHere{}
Let $X = X_\Sigma$ be a smooth toric CY3 without compact $4$-cycles,
 succeeded in 52ms:
Averaging the degree-two generator $r(z)$ returns the scalar $\kappa_{\mathrm{ch}}$, the unique $S_2$-coinvariant of the collision residue. When the same $r(z)$ comes from the CY-to-chiral functor applied to $D^b(\Coh(K3 \times E))$, the scalar is $\kappa_{\mathrm{ch}} = 3$ by additivity: $\kappa_{\mathrm{ch}}(K3) + \kappa_{\mathrm{ch}}(E) = 2 + 1$. This differs from the categorical Euler characteristic $\kappa_{\mathrm{cat}} = 2$, the lattice-rank invariant $\kappa_{\mathrm{fiber}} = 24$, and the BKM weight $\kappa_{\mathrm{BKM}} = 5$. An unsubscripted symbol would conflate distinct invariants.

\begin{remark}[Three bars, one functor]
\label{rem:three-bars-vol3}
The CY-to-chiral functor $\Phi$ of Chapter~\ref{ch:cy-to-chiral} has three natural composites. $\Phi_{E_1}$ produces $B^{\mathrm{ord}}(A_C)$; this is the ordered bar sensed by the Yangian. $\mathrm{av} \circ \Phi_{E_1}$ produces $B^{\Sigma}(A_C)$; this is the symmetric bar sensed by the modular characteristic $\kappa_{\mathrm{ch}}$. The full $E_2$ enhancement $\Phi_{E_2}$ produces the Drinfeld-centered bar $B^{E_2}(A_C) = \cZ(B^{\mathrm{ord}}(A_C))$; this is the braided bar sensed by the quantum group. All three factor through $\Phi_{E_1}$. This is the volume's motto: the ordered bar is the primitive.
\end{remark}

\section{$E_1$-chiral algebras from CY categories}
\label{sec:e1-from-cy}

The CY input has to produce an ordered chiral object before any braided output can exist. For a CY$_d$ category $\cC$ in the sense of Kontsevich-Soibelman, the trace lives in $\mathrm{HC}^-_d(\cC)$, not merely in Hochschild homology, and that trace feeds the ordered $E_1$ structure first.

\begin{proposition}[$E_1$ sector at $d=2$]
\label{prop:e1-sector-d2}
\ClaimStatusProvedHere
Let $\cC$ be a CY$_2$ category with cyclic $A_\infty$ structure and negative-cyclic trace. The ordered bar complex of the cyclic $A_\infty$ algebra $A_\cC$ carries a natural $E_1$-chiral structure whose holomorphic direction matches the Hochschild differential and whose ordered direction matches the cyclic action on the bar coalgebra.
\end{proposition}

\begin{proof}
The cyclic $\Ainf$-structure on $\cC$ provides an associative product on the bar coalgebra $B^{\mathrm{ord}}(A_\cC) = T^c(s^{-1}\bar{A}_\cC)$ via OPE residues (Step~1 of the cyclic-to-chiral passage, Section~\ref{sec:cyclic-to-chiral} of Chapter~\ref{ch:cy-to-chiral}). The holomorphic direction is the Hochschild differential $b \colon \mathrm{CC}_\bullet(\cC) \to \mathrm{CC}_{\bullet-1}(\cC)$, which descends to the bar differential $d_{\mathrm{bar}}$ on $B^{\mathrm{ord}}(A_\cC)$ via the standard identification of the bar construction with the Hochschild chain complex. The ordered direction is the $S^1$-action on the cyclic bar complex: the Connes $B$-operator cyclically permutes the bar entries, and its restriction to the ordered bar preserves the deconcatenation coproduct. The $E_1$-chiral structure is the factorization algebra on $C$ obtained by the factorization envelope of the Lie conformal algebra $\mathfrak{L}_\cC$ (Step~2), with the negative-cyclic trace in $\mathrm{HC}^-_2(\cC)$ providing the quantization datum (Step~4). At $d=2$, no framing obstruction arises: the $\bS^2$-framing is automatic (Kontsevich--Vlassopoulos). The full construction is Theorem~\ref{thm:cy-to-chiral} of Chapter~\ref{ch:cy-to-chiral}.
 succeeded in 51ms:
brace algebra, derived center, twisted holography boundary, line
defect, Wilson line $R$-matrix, soft graviton coupling, Yangian double
(cf.\ Vol~II, Theorem~\ref{thm:vol2-seven-face-master}).
\item \emph{Vol~III, this chapter:} the binary CY collision residue of a
Calabi--Yau chiral algebra, in seven CY-specific languages: CY
bar-cobar, CoHA / perverse coherent sheaves, classical CY Poisson
coisson, MO stable envelope, affine super Yangian for toric CY$_3$,
elliptic Sklyanin for toroidal CY, Gaudin from CY$_3$
(Conjecture~\ref{conj:cy-seven-face-master} above).
\end{enumerate}
The three master theorems are mutually compatible: under the CY-to-chiral
 succeeded in 52ms:
 \item The shadow obstruction tower of $\cA_{K3} \otimes H_1$ does \emph{not} by itself reproduce $\Phi_{10}$: four obstructions (K3-4 of \S\ref{sec:k3e-cross-volume}) separate the shadow tower output from $\Phi_{10}$. Namely, (O1) a categorical obstruction, (O2) the $\kappa_{\mathrm{ch}}/\kappa_{\mathrm{BKM}}$ mismatch $3 \neq 5$, (O3) second quantization (the Hilbert--Chow exceptional divisor), and (O4) the Schottky obstruction at $g \geq 4$ of codimension $(g-2)(g-3)/2$. The Borcherds lift supplies precisely the combinatorial data needed to bridge these four obstructions.
\end{enumerate}
\end{theorem}

\begin{proof}[Attribution]
Parts (i), (iii), (iv) are Vol~I/II results (\S\ref{sec:k3e-cross-volume}, items K3-1 through K3-13, proved in the K3 modular-tower chapter of Vol~I and in Part~III of Vol~II's 3D quantum gravity treatment). Part (ii) is the Borcherds lift of Borcherds (1998); its use as a modular characteristic is the observation of AP-CY8, not a theorem of Vol~III. The conditionality on propagates from Theorem~\ref{thm:cy-shadow-cohft}.
\end{proof}

\begin{remark}[Kappa-spectrum verification for $K3 \times E$]
 succeeded in 52ms:
symmetry algebra of the instanton moduli space; the DDCA is its
rational shadow on the boundary.

The K3 analogue of this picture replaces $\bC^2$ by a K3
surface~$S$: the K3 double current algebra $\fg_{K3}$
substitutes
$H^*(S,\bC)$ for $\bC[u,v]$ and the Mukai pairing for the
polynomial residue. Its quantization should produce a
``K3 Yangian'' standing in the same relation to $\fg_{K3}$ as the
affine Yangian $Y(\widehat{\fg})$ stands to the classical DDCA.
\end{remark}

\begin{remark}[Miki automorphism and spectral exchange]
\label{rem:ddca-miki-shadow}
\index{Miki automorphism!DDCA shadow}
\index{SL2Z@$\mathrm{SL}_2(\bZ)$!toroidal automorphism}
The quantum toroidal algebra $U_{q,t}(\hat{\hat{\mathfrak{gl}}}_1)$
carries an $\mathrm{SL}_2(\bZ)$ automorphism group (the
\emph{Miki automorphism}), whose generator $S$ exchanges the
horizontal and vertical loop generators
file update:
diff --git a/chapters/connections/cy_holographic_datum_master.tex b/chapters/connections/cy_holographic_datum_master.tex
index 2a66e8a0ca86f097e30b0de99c082498014430c6..b0ef34640300f22c24d57ee10a207c331065f31d
--- a/chapters/connections/cy_holographic_datum_master.tex
+++ b/chapters/connections/cy_holographic_datum_master.tex
@@ -943,7 +943,7 @@
 bar-cobar, CoHA / perverse coherent sheaves, classical CY Poisson
 coisson, MO stable envelope, affine super Yangian for toric CY$_3$,
 elliptic Sklyanin for toroidal CY, Gaudin from CY$_3$
-(Theorem~\ref{thm:cy-seven-face-master} above).
+(Conjecture~\ref{conj:cy-seven-face-master} above).
 \end{enumerate}
 The three master theorems are mutually compatible: under the CY-to-chiral
 functor $\Phi$, face~$i$ of Vol~III maps to a specialization of face~$i$
diff --git a/chapters/connections/modular_koszul_bridge.tex b/chapters/connections/modular_koszul_bridge.tex
index 1199c5aaa32e71f085dd3b7131c8f9aeadb1148c..a423d35b2ce162a9f56bb568768ae1bed7bef2f6
--- a/chapters/connections/modular_koszul_bridge.tex
+++ b/chapters/connections/modular_koszul_bridge.tex
@@ -234,7 +234,7 @@
 \end{theorem}
 
 \begin{proof}[Attribution]
-Parts (i), (iii), (iv) are Vol~I/II results (\S\ref{sec:k3e-cross-volume}, items K3-1 through K3-13, proved in the K3 modular-tower chapter of Vol~I and in the Vol~II 3D quantum gravity treatment, \ref{part:3d-qg} there). Part (ii) is the Borcherds lift of Borcherds (1998); its use as a modular characteristic is the observation of AP-CY8, not a theorem of Vol~III. The conditionality on propagates from Theorem~\ref{thm:cy-shadow-cohft}.
+Parts (i), (iii), (iv) are Vol~I/II results (\S\ref{sec:k3e-cross-volume}, items K3-1 through K3-13, proved in the K3 modular-tower chapter of Vol~I and in Part~III of Vol~II's 3D quantum gravity treatment). Part (ii) is the Borcherds lift of Borcherds (1998); its use as a modular characteristic is the observation of AP-CY8, not a theorem of Vol~III. The conditionality on propagates from Theorem~\ref{thm:cy-shadow-cohft}.
 \end{proof}
 
 \begin{remark}[Kappa-spectrum verification for $K3 \times E$]
diff --git a/chapters/examples/quantum_group_reps.tex b/chapters/examples/quantum_group_reps.tex
index e6b19a4c52de09f17af4b5f794d5f7269f4076b4..5213e6bfc9cb828c11c98b50aa32549aa228cfbf
--- a/chapters/examples/quantum_group_reps.tex
+++ b/chapters/examples/quantum_group_reps.tex
@@ -503,7 +503,7 @@
  additional data);
  \item $\kappa_{\mathrm{BKM}}$: the BKM modular weight, a
  number-theoretic invariant arising from the BKM denominator
- formula (Chapter~\ref{ch:toroidal-elliptic}; distinct from
+ formula (Chapter~\ref{chap:toroidal-elliptic}; distinct from
  both $\kappa_{\mathrm{cat}}$ and $\kappa_{\mathrm{ch}}$).
 \end{enumerate}
 For CY$_2$ categories with $\frakg$-symmetry, all three can be
diff --git a/chapters/examples/toric_cy3_coha.tex b/chapters/examples/toric_cy3_coha.tex
index 2b8821c0fd545c77e9d18a4180e8e67d3c4459be..94da66b26dadb3a8dcd2e91287fd7092ea5a944c
--- a/chapters/examples/toric_cy3_coha.tex
+++ b/chapters/examples/toric_cy3_coha.tex
@@ -205,7 +205,7 @@
 \end{theorem}
 
 \begin{proof}
-(i) The compact base $\bP^1 \times \bP^1$ has $\chi(\bP^1 \times \bP^1) = 4$ (each factor contributes $\chi(\bP^1) = 2$), so $\kappa_{\mathrm{ch}} = \chi/2 = 2$ by the general local-surface formula (Remark~\ref{rem:toric-structural-patterns}).
+(i) The compact base $\bP^1 \times \bP^1$ has $\chi(\bP^1 \times \bP^1) = 4$ (each factor contributes $\chi(\bP^1) = 2$), so $\kappa_{\mathrm{ch}} = \chi/2 = 2$ by the general local-surface formula (Remark~\ref{rem:toric-kappa-patterns}).
 
 (ii) The intersection form on $H^2(\bP^1 \times \bP^1)$ in the basis $\{e_1, e_2\}$ is $\langle e_i, e_j \rangle = \delta_{ij}$ (the two rulings are orthogonal with self-intersection $0$ in the total space, but the relevant inner product for the shadow metric is the Euler pairing $\chi(e_i, e_j) = \delta_{ij}$).
 
@@ -654,7 +654,7 @@
 the chart gluing by descent, the shadow tower by the MC equation.
 These components are \emph{a priori} separate structures on the
 same algebra. The Vol~I chiral quantum group equivalence
-(Theorem~\ref{thm:chiral-qg-equiv}) asserts that three of them
+asserts that three of them
 (the vertex $R$-matrix, the chiral $A_\infty$-structure, and the
 chiral coproduct) determine each other on the Koszul locus. The theorem
 below specializes the abstract equivalence to the toric CY3 setting,
@@ -746,8 +746,7 @@
 
 \begin{proof}
 The abstract equivalence (I) $\leftrightarrow$ (II)
-$\leftrightarrow$ (III) is
-Theorem~\ref{thm:chiral-qg-equiv} of Vol~I, proved for any
+$\leftrightarrow$ (III) is the Vol~I chiral quantum group equivalence, proved for any
 $\Eone$-chiral algebra on the Koszul locus. The content of the
 present theorem is the identification of each abstract vertex
 with the independently constructed toric CY3 structure.
@@ -755,7 +754,7 @@
 \textit{Component~\textup{(I)}: $R$-matrix.}
 The $\Eone$-chiral algebra $A_X$ carries a vertex
 $R$-matrix by the general theory
-(Theorem~\ref{thm:chiral-qg-equiv}(I)). For toric CY3, the
+(item~\textup{(I)} of that equivalence). For toric CY3, the
 Maulik--Okounkov stable-envelope construction provides an
 independent $R$-matrix on $Y^+(\widehat{\fg}_{Q_X})$-modules.
 The two coincide because both solve the same Yang--Baxter
diff --git a/chapters/examples/toroidal_elliptic.tex b/chapters/examples/toroidal_elliptic.tex
index 8fcef3a49b8fe0bd45c3ae248676e994ece0ca7e..0a15b2c062f601ea29e50e3e3771b3eb1544db50
--- a/chapters/examples/toroidal_elliptic.tex
+++ b/chapters/examples/toroidal_elliptic.tex
@@ -5940,8 +5940,7 @@
 
 The K3 analogue of this picture replaces $\bC^2$ by a K3
 surface~$S$: the K3 double current algebra $\fg_{K3}$
-(Chapter~\ref{ch:k3-times-e},
-Definition~\ref{def:k3-double-current-algebra}) substitutes
+substitutes
 $H^*(S,\bC)$ for $\bC[u,v]$ and the Mukai pairing for the
 polynomial residue. Its quantization should produce a
 ``K3 Yangian'' standing in the same relation to $\fg_{K3}$ as the
@@ -6018,7 +6017,7 @@
   At $t \to 1$: the second parameter $w$ decouples and
   $\Delta_{z,w}$ reduces to the single-parameter
   Drinfeld coproduct $\Delta_z(T(u)) = T(u) \otimes T(u - z)$
-  of Theorem~\textup{\ref{thm:w-infty-chiral-qg}}.
+  of Proposition~\textup{\ref{prop:universal-coproduct}}.
 \end{enumerate}
 No two-parameter coproduct $\Delta_{z,w}$ currently exists in
 the literature or in this programme's compute infrastructure.
@@ -6034,7 +6033,7 @@
   $(q_1,q_2,q_3)$.
 \item Promote the DDCA shadow to an explicit $\Delta_{z,w}$
   formula aligned with the $R(u,v)$ surface in
-  \S\ref{subsec:quantum-chiral-algebras-6d}.
+  \S\ref{subsec:chiral-qg-wilson}.
 \item Build a compute witness at low modes: $w = 0$ reduces
   to existing $\Delta_z$; rational limit gives the DDCA
   shift; Miki sends $\Delta_{z,w} \to \Delta_{w,z}$.
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index ddbdfe60d9c9df04ba6f3acf48deee73523a64dc..3ce4e679084f2f25672104c7a00684df5e9f3b26
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -320,7 +320,7 @@
 Drinfeld coproduct from spin~$2$ to arbitrary spin, with the
 universal Miura coefficient $(\Psi{-}1)/\Psi$ on the leading
 cross-term $J \otimes W_{s-1}$ at every spin $s \ge 2$
-(Theorem~\ref{thm:miura-cross-universality}).
+(Proposition~\ref{prop:universal-coproduct}).
 
 \bigskip
 
@@ -328,7 +328,7 @@
 Volume~I defines $E_1$-chiral quantum groups abstractly. This
 volume constructs them concretely from CY geometry. The
 $E_1$-chiral bialgebra axioms (formalized in
-\S\ref{sec:e1-chiral-bialgebra}) require: (H1)~an $E_1$-chiral
+\S\ref{sec:e1-chiral-bialgebras}) require: (H1)~an $E_1$-chiral
 algebra $A$ on a curve $X$; (H2)~a spectral coproduct
 $\Delta_z \colon A \to A \otimes A$ (living on the OPEN/$E_1$
 colour); (H3)~an $R$-matrix $R(z)$ satisfying YBE; (H4)~RTT
diff --git a/chapters/theory/cy_categories.tex b/chapters/theory/cy_categories.tex
index f9b51871c44fa18a574c02fce8aaa49a49aa9c61..00d723a1cb5d4f2355a10cb2d9d3f86688259f09
--- a/chapters/theory/cy_categories.tex
+++ b/chapters/theory/cy_categories.tex
@@ -166,7 +166,7 @@
 Every smooth proper CY$_d$ category admits a cyclic $\Ainf$-enhancement, unique up to $\Ainf$-quasi-isomorphism preserving the pairing. The proof is due to Kontsevich--Soibelman in the formal case, Costello~\cite{Costello2005} for the TCFT enhancement, and Seidel~\cite{Seidel2008} for the Fukaya case.
 \end{theorem}
 
-At $d = 2$ the enhancement is explicit enough to compute directly; it drives the $K3$ computations feeding the Borcherds denominator (Vol~III Chapter~\ref{ch:k3}). At $d = 3$ the enhancement was constructed by Sheridan~\cite{Sheridan2015} for the quintic threefold, as part of the HMS proof; the general $d = 3$ construction remains programme-level (conditional on $\bS^3$-framing, see AP-CY6).
+At $d = 2$ the enhancement is explicit enough to compute directly; it drives the $K3$ computations feeding the Borcherds denominator (Vol~III Chapter~\ref{ch:k3-times-e}). At $d = 3$ the enhancement was constructed by Sheridan~\cite{Sheridan2015} for the quintic threefold, as part of the HMS proof; the general $d = 3$ construction remains programme-level (conditional on $\bS^3$-framing, see AP-CY6).
 
 \section{Interface with the CY-to-chiral functor $\Phi$}
 \label{sec:cy-cat-phi-interface}
@@ -194,7 +194,7 @@
 
 \begin{remark}[What $\Phi$ does not see]
 \label{rem:phi-does-not-see}
-Not every invariant of $\cC$ survives the passage through $\Phi$. The functor retains the cyclic $\Ainf$-structure and the Gerstenhaber bracket; it loses the fine structure of the triangulated / $\Ainf$ category (individual objects, t-structures, stability conditions) that is visible only via the fuller categorical CoHA construction of Chapter~\ref{ch:coha}. The kappa-spectrum (Vol~III CLAUDE.md) encodes which invariants survive: $\kappa_\mathrm{cat}$ is always present, $\kappa_\mathrm{ch}$ exists only when $\Phi$ is defined, and $\kappa_\mathrm{BKM}$ records the Borcherds-side lift for $K3 \times E$.
+Not every invariant of $\cC$ survives the passage through $\Phi$. The functor retains the cyclic $\Ainf$-structure and the Gerstenhaber bracket; it loses the fine structure of the triangulated / $\Ainf$ category (individual objects, t-structures, stability conditions) that is visible only via the fuller categorical CoHA construction of Chapter~\ref{ch:toric-coha}. The kappa-spectrum (Vol~III CLAUDE.md) encodes which invariants survive: $\kappa_\mathrm{cat}$ is always present, $\kappa_\mathrm{ch}$ exists only when $\Phi$ is defined, and $\kappa_\mathrm{BKM}$ records the Borcherds-side lift for $K3 \times E$.
 \end{remark}
 
 \begin{remark}[Cross-volume conventions]
diff --git a/chapters/theory/cy_to_chiral.tex b/chapters/theory/cy_to_chiral.tex
index 030fed4a9a2a7009ae05fdb0f3c431c8aed1fc83..14526e0aba63169841056220749304799a57fe10
--- a/chapters/theory/cy_to_chiral.tex
+++ b/chapters/theory/cy_to_chiral.tex
@@ -618,8 +618,8 @@
 homotopy is purely algebraic: it acts by
 $s(f_{i_0 \cdots i_q}) = f_{0 i_0 \cdots i_q}$ on \v{C}ech cochains and
 involves no PDE solving. The SDR data $(i, p, s)$ interfaces directly
-with the homotopy transfer theorem
-\textup{(}HTT, Theorem~\textup{\ref{thm:htt-general}}\textup{)},
+with the standard homotopy transfer theorem
+\textup{(}HTT\textup{)},
 transferring the $\Ainf$-structure from $\check{C}^\bullet(\cE nd(\cE))$
 to its cohomology $\Ext^\bullet(\cE, \cE)$.
 \end{theorem}
@@ -652,7 +652,7 @@
 (whether the formal series in the OPE coefficients converges to
 define honest holomorphic functions) requires separate input from
 the analytic completion programme (MC5,
-\S\ref{sec:analytic-sewing} of Vol~I). Specifically: the HTT
+the analytic sewing section of Vol~I). Specifically: the HTT
 produces transferred operations $\mu_k^{\mathrm{ch}}$ whose
 coefficients involve iterated applications of~$s$; each application
 introduces rational functions on the intersections $U_{i_0} \cap
@@ -1972,7 +1972,7 @@
  \bottomrule
 \end{tabular}
 \end{center}
-{\footnotesize $^*$The K3 entry records $\kappa_{\mathrm{ch}} = \chi(\cO_{\mathrm{K3}}) = 2$ (Proposition~\ref{prop:cy-kappa-d2}; verified via chiral de Rham, Chapter~\ref{ch:k3-times-e}). The distinct quantity $\dim \HH_*(D^b(\mathrm{K3}))/2 = 12$ arises from an alternative algebraization (the Monster orbifold); the full trichotomy ($\kappa_{\mathrm{ch}} \in \{2, 12, 24\}$) is developed in Section~\ref{subsec:k3-three-algebraizations} of Chapter~\ref{ch:k3-times-e}.
+{\footnotesize $^*$The K3 entry records $\kappa_{\mathrm{ch}} = \chi(\cO_{\mathrm{K3}}) = 2$ (Proposition~\ref{prop:cy-kappa-d2}; verified via chiral de Rham, Chapter~\ref{ch:k3-times-e}). The distinct quantity $\dim \HH_*(D^b(\mathrm{K3}))/2 = 12$ arises from an alternative algebraization (the Monster orbifold); the full trichotomy ($\kappa_{\mathrm{ch}} \in \{2, 12, 24\}$) is developed in the K3 discussion of Chapter~\ref{ch:k3-times-e}.
 
 $^\dagger$The $K3 \times E$ entry records $\kappa_{\mathrm{ch}} = 3$ by additivity (Proposition~\ref{prop:categorical-euler}: $\kappa_{\mathrm{ch}}(\mathrm{K3}) + \kappa_{\mathrm{ch}}(E) = 2 + 1$). The Borcherds automorphic weight is $\kappa_{\mathrm{BKM}} = 5 = \mathrm{wt}(\Delta_5)$, a distinct invariant.}
 
diff --git a/chapters/theory/drinfeld_center.tex b/chapters/theory/drinfeld_center.tex
index ac67d4e3a2ed8fab94fcb3fc63933d8650a92ac9..a711d853438f9e6a0e6fdd4e5dac61154b7b3c24
--- a/chapters/theory/drinfeld_center.tex
+++ b/chapters/theory/drinfeld_center.tex
@@ -726,7 +726,7 @@
 produces only symmetric braiding. The distinction is the
 deep reason for the $\Eone$ stabilization theorem
 (Chapter~\ref{ch:cy-to-chiral},
-Theorem~\ref{thm:e1-stabilization}).
+Theorem~\ref{thm:e1-stabilization-cy}).
 
 \begin{proposition}[$E_3$ restriction gives symmetric braiding]
 \label{prop:e3-symmetric-braiding}
diff --git a/chapters/theory/e1_chiral_algebras.tex b/chapters/theory/e1_chiral_algebras.tex
index 75484d2fff759dc21313b5595a8abade7d55d203..b533b2f5640db9eba4046a61106787f2c19a0d53
--- a/chapters/theory/e1_chiral_algebras.tex
+++ b/chapters/theory/e1_chiral_algebras.tex
@@ -63,7 +63,7 @@
 via holomorphic Chern--Simons; conjectural in general).
 The further $E_3$-topological upgrade requires a conformal
 vector at non-critical level
-(Volume~I, Theorem~\textup{\ref*{thm:topologization}}).
+(Volume~I, the topologization theorem).
 \end{definition}
 
 The closed colour carries $E_2$ structure from
@@ -128,7 +128,7 @@
 
 \begin{remark}[Three bars, one functor]
 \label{rem:three-bars-vol3}
-The CY-to-chiral functor $\Phi$ of Chapter~\ref{ch:cy-chiral-functor} has three natural composites. $\Phi_{E_1}$ produces $B^{\mathrm{ord}}(A_C)$; this is the ordered bar sensed by the Yangian. $\mathrm{av} \circ \Phi_{E_1}$ produces $B^{\Sigma}(A_C)$; this is the symmetric bar sensed by the modular characteristic $\kappa_{\mathrm{ch}}$. The full $E_2$ enhancement $\Phi_{E_2}$ produces the Drinfeld-centered bar $B^{E_2}(A_C) = \cZ(B^{\mathrm{ord}}(A_C))$; this is the braided bar sensed by the quantum group. All three factor through $\Phi_{E_1}$. This is the volume's motto: the ordered bar is the primitive.
+The CY-to-chiral functor $\Phi$ of Chapter~\ref{ch:cy-to-chiral} has three natural composites. $\Phi_{E_1}$ produces $B^{\mathrm{ord}}(A_C)$; this is the ordered bar sensed by the Yangian. $\mathrm{av} \circ \Phi_{E_1}$ produces $B^{\Sigma}(A_C)$; this is the symmetric bar sensed by the modular characteristic $\kappa_{\mathrm{ch}}$. The full $E_2$ enhancement $\Phi_{E_2}$ produces the Drinfeld-centered bar $B^{E_2}(A_C) = \cZ(B^{\mathrm{ord}}(A_C))$; this is the braided bar sensed by the quantum group. All three factor through $\Phi_{E_1}$. This is the volume's motto: the ordered bar is the primitive.
 \end{remark}
 
 \section{$E_1$-chiral algebras from CY categories}
@@ -153,7 +153,7 @@
 Let $\cC$ be a CY$_3$ category with a chain-level $S^3$-framing on $\mathrm{HC}^-_3(\cC)$ (the condition of Conjecture~CY-A$_3$). Then the ordered bar complex of the cyclic $A_\infty$ algebra $A_\cC$ carries an $E_1$-chiral structure whose representation category is a braided monoidal refinement of the BPS Yangian of $\cC$.
 \end{conjecture}
 
-The conjecture is conditional on the chain-level framing; the unconditional statement requires the full CY-A$_3$ programme. Every downstream result in \ref{part:examples} and \ref{part:connections} that uses the BPS Yangian inherits this conditionality. The connection to Maulik-Okounkov and Costello-Witten cohomological Hall algebras is traced in Chapter~\ref{ch:cha-yangian}.
+The conjecture is conditional on the chain-level framing; the unconditional statement requires the full CY-A$_3$ programme. Every downstream result in \ref{part:examples} and \ref{part:connections} that uses the BPS Yangian inherits this conditionality. The connection to Maulik-Okounkov and Costello-Witten cohomological Hall algebras is traced in Chapter~\ref{ch:toric-coha}.
 
 \begin{proposition}[$E_2$ enhancement via Drinfeld center]
 \label{prop:e2-enhancement-drinfeld}
@@ -318,7 +318,7 @@
 
 \begin{remark}[How this chapter is used downstream]
 \label{rem:downstream-usage}
-Chapters~\ref{ch:braided-factorization}, \ref{ch:drinfeld-center}, and \ref{ch:quantum-group-reps} use this chapter as the source of the ordered bar coalgebra and the averaging map. Chapter~\ref{ch:cy-chiral-functor} uses Proposition~\ref{prop:e1-sector-d2} as the $d=2$ existence statement for $A_\cC$. Every braided monoidal category that appears later is the Drinfeld center of an underlying ordered one.
+Chapters~\ref{ch:braided-factorization}, \ref{ch:drinfeld-center}, and \ref{ch:quantum-group-reps} use this chapter as the source of the ordered bar coalgebra and the averaging map. Chapter~\ref{ch:cy-to-chiral} uses Proposition~\ref{prop:e1-sector-d2} as the $d=2$ existence statement for $A_\cC$. Every braided monoidal category that appears later is the Drinfeld center of an underlying ordered one.
 \end{remark}
 
 \section{Operadic dictionary for the CY reader}
@@ -1447,7 +1447,7 @@
 cutting the elliptic curve.}
 For the product CY$_3$ manifold $X = K3 \times E$, the factorization
 homology integral $\int_{K3} \cF|_{K3}$ of
-Section~\ref{sec:k3-perturbative-fact-homology} produces a chiral algebra
+Section~\ref{subsec:fact-homology-k3xe} produces a chiral algebra
 $A_E$ on the residual elliptic curve $E$.  The coproduct on $A_E$ arises
 from cutting $E$ into two intervals via excision.  Concretely, choose a
 collar-gluing decomposition $E = I_1 \cup_{S^0 \times \R} I_2$ (cutting
diff --git a/chapters/theory/e2_chiral_algebras.tex b/chapters/theory/e2_chiral_algebras.tex
index 4d9c49d33b9b71c9728719844b5387b9c256ec23..8a25a3037dc9569752a97c0fc75347a4033380af
--- a/chapters/theory/e2_chiral_algebras.tex
+++ b/chapters/theory/e2_chiral_algebras.tex
@@ -194,7 +194,7 @@
 \label{sec:drinfeld-center-bridge}
 
 Volume~II constructs $\Phi_{E_1}$ and proves $E_1$-chiral Koszul
-duality (see \ref{part:e1-core} of \cite{VolII}). The Drinfeld center
+duality (see Part~I of \cite{VolII}). The Drinfeld center
 $Z\colon E_1\text{-}\Cat \xrightarrow{\sim} E_2\text{-}\Cat$
 (under dualizability) is the categorical passage from ordered
 monoidal data to braided monoidal data. On the bar side it matches the
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 30392e44f20b6614f1f54981964db6c0329363e5..69d953d96d354add714abf2eec933a753336234a
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -201,7 +201,7 @@
 \]
 The SDR data $(i, p, s)$ interfaces directly with the homotopy transfer theorem (HTT), transferring the $A_\infty$-structure from \v{C}ech cochains $\check{C}^\bullet(\mathcal{E}nd(\mathcal{E}))$ to its cohomology $\mathrm{Ext}^\bullet(\mathcal{E}, \mathcal{E})$. The transferred operations $\mu_k^{\mathrm{ch}}$ are given by sums over planar trees whose internal edges are decorated by the homotopy~$s$; each application of~$s$ introduces rational functions on the affine intersections, and the resulting chiral operations are well-defined as formal power series.
 
-The scope is perturbative: the \v{C}ech homotopy produces an algebraic $A_\infty$-structure on the Ext algebra, but convergence of the resulting series to holomorphic functions (the non-perturbative statement) requires separate input from the analytic completion programme of Volume~I (MC5, \S\ref{sec:analytic-sewing}). The perturbative statement suffices for the formal CY-to-chiral functor and for all combinatorial applications in this volume. The full construction, including the proof that the SDR conditions hold and the scope qualification, is Theorem~\ref{thm:cech-contracting-homotopy} in Chapter~\ref{ch:cy-to-chiral}.
+The scope is perturbative: the \v{C}ech homotopy produces an algebraic $A_\infty$-structure on the Ext algebra, but convergence of the resulting series to holomorphic functions (the non-perturbative statement) requires separate input from the analytic completion programme of Volume~I (MC5, the analytic sewing section there). The perturbative statement suffices for the formal CY-to-chiral functor and for all combinatorial applications in this volume. The full construction, including the proof that the SDR conditions hold and the scope qualification, is Theorem~\ref{thm:cech-contracting-homotopy} in Chapter~\ref{ch:cy-to-chiral}.
 
 Three independent consistency checks confirm the resulting chiral data for the quintic: the Gepner model matrix factorization (via mirror symmetry, $\mathrm{MF}(x_1^5 + \cdots + x_5^5)$), the large-volume Hodge--Kodaira--Rosenberg limit ($\mathrm{HKR}$ degeneration of $\mathrm{Ext}^\bullet$ to Dolbeault cohomology), and the Gopakumar--Vafa integrality of the resulting genus-$g$ amplitudes. All three produce the same modular characteristic $\chi/2 = -100$ (the MacMahon-normalised form of $\kappa_{\mathrm{cat}}$ at $d=3$).
 
@@ -277,7 +277,7 @@
  \item The moonshine multiplier: $A_n = \kappa_{\mathrm{cat}} \cdot \dim(\rho_n)$ identifies the factor $2$ in $Z_{K3} = 2\,\phi_{0,1}$.
  \item The categorical $\Etwo$-obstruction for CY$_3$ (Proposition~\ref{prop:e1-obstruction-categorical}): Serre duality forces antisymmetry of the Euler form, universally obstructing $\Etwo$-enhancement without torus hypotheses.
  \item Quiver-chart gluing for toric CY$_3$ (Theorem~\ref{thm:toric-chart-gluing}): the global $\Eone$-chiral algebra is assembled as a homotopy colimit of McKay-chart CoHAs, with $E_2$ descent degeneration and Costello--Li comparison.
- \item The K3 double current algebra $\fg_{K3}$ (Definition~\ref{def:k3-double-current-algebra}): the finite-dimensional analogue of the DDCA in which $\bC[u,v]$ is replaced by $H^*(S,\bC)$ with the Mukai pairing.
+ \item The K3 double current algebra $\fg_{K3}$: the finite-dimensional analogue of the DDCA in which $\bC[u,v]$ is replaced by $H^*(S,\bC)$ with the Mukai pairing.
  \item Forty-two CY/BKM compute engines with $5{,}700{+}$ tests across the standard CY landscape.
 \end{itemize}
 
@@ -360,7 +360,7 @@
 \item \emph{Descent theorem.}
  \v{C}ech descent for $E_1$-algebras over the Bridgeland
  stability manifold. Proved for toric CY3
- (Proposition~\ref{prop:e1-descent-unobstructed}); open for
+ (Theorem~\ref{thm:toric-chart-gluing}); open for
  compact CY3 beyond the chart-atlas regime.
 \item \emph{Higher-dimensional CY shadows.}
  The $E_n$ stabilization theorem
@@ -394,12 +394,12 @@
 
 \emph{Quantum group representations} (Chapter~\ref{ch:quantum-group-reps}). The representation-theoretic target. The braided monoidal category $\mathrm{Rep}_q(\mathfrak{g})$ is what the CY programme aims to realize: Conjecture~CY-C predicts that $\mathrm{Rep}_q(\mathfrak{g}) \simeq \mathrm{Rep}^{E_2}(A_\cC)$ for a CY category $\cC(\mathfrak{g}, q)$. The Kazhdan--Lusztig equivalence $\mathrm{Rep}_q(\mathfrak{g}) \simeq \mathrm{KL}_k(\mathfrak{g})$ at roots of unity is the prototype: the Volume~I bar complex $B(V_k(\mathfrak{g}))$ encodes the quantum group $R$-matrix in its degree-$(1,1)$ component, and the DK bridge (Volume~II, MC3 for all simple types) recovers the quantum group categorical structure. The affine Yangian realization (Chapter~\ref{ch:toric-coha}) provides the $E_1$-sector; the Drinfeld center (Chapter~\ref{ch:drinfeld-center}) provides the $E_2$-enhancement.
 
-In addition to the four standard families, the toroidal and elliptic algebras chapter (Chapter~\ref{chap:toroidal-elliptic}) develops the $K3 \times E$ programme in full: the generalized root datum, the BKM superalgebra $\mathfrak{g}_{\Delta_5}$ with its Igusa cusp form denominator identity, the shadow--Siegel gap theorem, thirteen structural results (K3-1 through K3-13), all ten research programmes (A through J), and the DDCA--toroidal bridge identifying the deformed double current algebra as the rational degeneration of the quantum toroidal algebra (Conjecture~\ref{conj:ddca-toroidal-bridge}). The K3 double current algebra $\fg_{K3}$ (Chapter~\ref{ch:k3-times-e}, Definition~\ref{def:k3-double-current-algebra}) provides the K3 analogue of the DDCA, replacing $\bC[u,v]$ with $H^*(S,\bC)$. The toric CY$_3$ CoHA chapter (Chapter~\ref{ch:toric-coha}) develops the affine Yangian and $\mathcal{W}_{1+\infty}$ side: the Jordan quiver gives $Y(\widehat{\mathfrak{gl}}_1) \simeq \mathcal{W}_{1+\infty}$, the toric fan is the Dynkin data, and the shuffle algebra presentation connects to the KZ equations of Volume~I.
+In addition to the four standard families, the toroidal and elliptic algebras chapter (Chapter~\ref{chap:toroidal-elliptic}) develops the $K3 \times E$ programme in full: the generalized root datum, the BKM superalgebra $\mathfrak{g}_{\Delta_5}$ with its Igusa cusp form denominator identity, the shadow--Siegel gap theorem, thirteen structural results (K3-1 through K3-13), all ten research programmes (A through J), and the DDCA--toroidal bridge identifying the deformed double current algebra as the rational degeneration of the quantum toroidal algebra (Conjecture~\ref{conj:ddca-toroidal-bridge}). The K3 double current algebra $\fg_{K3}$, discussed in the DDCA--toroidal bridge of Chapter~\ref{ch:k3-times-e}, provides the K3 analogue of the DDCA, replacing $\bC[u,v]$ with $H^*(S,\bC)$. The toric CY$_3$ CoHA chapter (Chapter~\ref{ch:toric-coha}) develops the affine Yangian and $\mathcal{W}_{1+\infty}$ side: the Jordan quiver gives $Y(\widehat{\mathfrak{gl}}_1) \simeq \mathcal{W}_{1+\infty}$, the toric fan is the Dynkin data, and the shuffle algebra presentation connects to the KZ equations of Volume~I.
 
 \section{Guide for the reader}
 \label{sec:guide}
 
-Part~\ref{part:cy-categories} establishes the categorical foundations: CY categories, cyclic $\Ainf$-structures, the Hochschild calculus, and the $E_1$/$E_2$/$E_n$ chiral hierarchy with the framing obstruction tower. Part~\ref{part:bridge} constructs the bridge functor $\Phi$ from CY categories to quantum chiral algebras and proves Theorems CY-A (for $d = 2$) and CY-D, with the identification of automorphic correction and shadow obstruction tower as the central result. Part~\ref{part:examples} treats quantum groups and their braided factorization structure, including the Drinfeld center as the bulk algebra. Part~\ref{part:connections} works through the standard landscape: the toroidal and elliptic algebras chapter develops the $K3 \times E$ programme (K3-1 through K3-13, programmes A through J), alongside toric CY3 CoHAs, Fukaya categories, derived categories, matrix factorizations (ADE singularities and W-algebras), and quantum group representations (Kazhdan--Lusztig, affine Yangians, critical CoHAs). Part~\ref{part:frontier} connects to the geometric Langlands programme and to Volumes~I and~II via the bar-cobar bridge and the modular Koszul bridge. The working notes (\S\ref{sec:working-notes}) record the research frontier.
+Part~\ref{part:cy-categories} establishes the categorical foundations: CY categories, cyclic $\Ainf$-structures, the Hochschild calculus, and the $E_1$/$E_2$/$E_n$ chiral hierarchy with the framing obstruction tower. Part~\ref{part:bridge} constructs the bridge functor $\Phi$ from CY categories to quantum chiral algebras and proves Theorems CY-A (for $d = 2$) and CY-D, with the identification of automorphic correction and shadow obstruction tower as the central result. Part~\ref{part:examples} treats quantum groups and their braided factorization structure, including the Drinfeld center as the bulk algebra. Part~\ref{part:connections} works through the standard landscape: the toroidal and elliptic algebras chapter develops the $K3 \times E$ programme (K3-1 through K3-13, programmes A through J), alongside toric CY3 CoHAs, Fukaya categories, derived categories, matrix factorizations (ADE singularities and W-algebras), and quantum group representations (Kazhdan--Lusztig, affine Yangians, critical CoHAs). Part~\ref{part:frontier} connects to the geometric Langlands programme and to Volumes~I and~II via the bar-cobar bridge and the modular Koszul bridge. The separate working notes record the research frontier.
 
 \section{Conventions and notation}
 \label{sec:conventions-intro}

codex
The local reread is coherent. I’m running the same narrow build target again now; the success criterion is simple: zero undefined references in `main.log`, even if the unrelated citation warnings remain.
exec
/bin/zsh -lc 'pkill -9 -f pdflatex 2>/dev/null || true
sleep 2
make fast' in /Users/raeez/calabi-yau-quantum-groupsfile update:
diff --git a/chapters/connections/cy_holographic_datum_master.tex b/chapters/connections/cy_holographic_datum_master.tex
index 2a66e8a0ca86f097e30b0de99c082498014430c6..b0ef34640300f22c24d57ee10a207c331065f31d
--- a/chapters/connections/cy_holographic_datum_master.tex
+++ b/chapters/connections/cy_holographic_datum_master.tex
@@ -943,7 +943,7 @@
 bar-cobar, CoHA / perverse coherent sheaves, classical CY Poisson
 coisson, MO stable envelope, affine super Yangian for toric CY$_3$,
 elliptic Sklyanin for toroidal CY, Gaudin from CY$_3$
-(Theorem~\ref{thm:cy-seven-face-master} above).
+(Conjecture~\ref{conj:cy-seven-face-master} above).
 \end{enumerate}
 The three master theorems are mutually compatible: under the CY-to-chiral
 functor $\Phi$, face~$i$ of Vol~III maps to a specialization of face~$i$
diff --git a/chapters/connections/modular_koszul_bridge.tex b/chapters/connections/modular_koszul_bridge.tex
index 1199c5aaa32e71f085dd3b7131c8f9aeadb1148c..a423d35b2ce162a9f56bb568768ae1bed7bef2f6
--- a/chapters/connections/modular_koszul_bridge.tex
+++ b/chapters/connections/modular_koszul_bridge.tex
@@ -234,7 +234,7 @@
 \end{theorem}
 
 \begin{proof}[Attribution]
-Parts (i), (iii), (iv) are Vol~I/II results (\S\ref{sec:k3e-cross-volume}, items K3-1 through K3-13, proved in the K3 modular-tower chapter of Vol~I and in the Vol~II 3D quantum gravity treatment, \ref{part:3d-qg} there). Part (ii) is the Borcherds lift of Borcherds (1998); its use as a modular characteristic is the observation of AP-CY8, not a theorem of Vol~III. The conditionality on propagates from Theorem~\ref{thm:cy-shadow-cohft}.
+Parts (i), (iii), (iv) are Vol~I/II results (\S\ref{sec:k3e-cross-volume}, items K3-1 through K3-13, proved in the K3 modular-tower chapter of Vol~I and in Part~III of Vol~II's 3D quantum gravity treatment). Part (ii) is the Borcherds lift of Borcherds (1998); its use as a modular characteristic is the observation of AP-CY8, not a theorem of Vol~III. The conditionality on propagates from Theorem~\ref{thm:cy-shadow-cohft}.
 \end{proof}
 
 \begin{remark}[Kappa-spectrum verification for $K3 \times E$]
diff --git a/chapters/examples/quantum_group_reps.tex b/chapters/examples/quantum_group_reps.tex
index e6b19a4c52de09f17af4b5f794d5f7269f4076b4..5213e6bfc9cb828c11c98b50aa32549aa228cfbf
--- a/chapters/examples/quantum_group_reps.tex
+++ b/chapters/examples/quantum_group_reps.tex
@@ -503,7 +503,7 @@
  additional data);
  \item $\kappa_{\mathrm{BKM}}$: the BKM modular weight, a
  number-theoretic invariant arising from the BKM denominator
- formula (Chapter~\ref{ch:toroidal-elliptic}; distinct from
+ formula (Chapter~\ref{chap:toroidal-elliptic}; distinct from
  both $\kappa_{\mathrm{cat}}$ and $\kappa_{\mathrm{ch}}$).
 \end{enumerate}
 For CY$_2$ categories with $\frakg$-symmetry, all three can be
diff --git a/chapters/examples/toric_cy3_coha.tex b/chapters/examples/toric_cy3_coha.tex
index 2b8821c0fd545c77e9d18a4180e8e67d3c4459be..94da66b26dadb3a8dcd2e91287fd7092ea5a944c
--- a/chapters/examples/toric_cy3_coha.tex
+++ b/chapters/examples/toric_cy3_coha.tex
@@ -205,7 +205,7 @@
 \end{theorem}
 
 \begin{proof}
-(i) The compact base $\bP^1 \times \bP^1$ has $\chi(\bP^1 \times \bP^1) = 4$ (each factor contributes $\chi(\bP^1) = 2$), so $\kappa_{\mathrm{ch}} = \chi/2 = 2$ by the general local-surface formula (Remark~\ref{rem:toric-structural-patterns}).
+(i) The compact base $\bP^1 \times \bP^1$ has $\chi(\bP^1 \times \bP^1) = 4$ (each factor contributes $\chi(\bP^1) = 2$), so $\kappa_{\mathrm{ch}} = \chi/2 = 2$ by the general local-surface formula (Remark~\ref{rem:toric-kappa-patterns}).
 
 (ii) The intersection form on $H^2(\bP^1 \times \bP^1)$ in the basis $\{e_1, e_2\}$ is $\langle e_i, e_j \rangle = \delta_{ij}$ (the two rulings are orthogonal with self-intersection $0$ in the total space, but the relevant inner product for the shadow metric is the Euler pairing $\chi(e_i, e_j) = \delta_{ij}$).
 
@@ -654,7 +654,7 @@
 the chart gluing by descent, the shadow tower by the MC equation.
 These components are \emph{a priori} separate structures on the
 same algebra. The Vol~I chiral quantum group equivalence
-(Theorem~\ref{thm:chiral-qg-equiv}) asserts that three of them
+asserts that three of them
 (the vertex $R$-matrix, the chiral $A_\infty$-structure, and the
 chiral coproduct) determine each other on the Koszul locus. The theorem
 below specializes the abstract equivalence to the toric CY3 setting,
@@ -746,8 +746,7 @@
 
 \begin{proof}
 The abstract equivalence (I) $\leftrightarrow$ (II)
-$\leftrightarrow$ (III) is
-Theorem~\ref{thm:chiral-qg-equiv} of Vol~I, proved for any
+$\leftrightarrow$ (III) is the Vol~I chiral quantum group equivalence, proved for any
 $\Eone$-chiral algebra on the Koszul locus. The content of the
 present theorem is the identification of each abstract vertex
 with the independently constructed toric CY3 structure.
@@ -755,7 +754,7 @@
 \textit{Component~\textup{(I)}: $R$-matrix.}
 The $\Eone$-chiral algebra $A_X$ carries a vertex
 $R$-matrix by the general theory
-(Theorem~\ref{thm:chiral-qg-equiv}(I)). For toric CY3, the
+(item~\textup{(I)} of that equivalence). For toric CY3, the
 Maulik--Okounkov stable-envelope construction provides an
 independent $R$-matrix on $Y^+(\widehat{\fg}_{Q_X})$-modules.
 The two coincide because both solve the same Yang--Baxter
diff --git a/chapters/examples/toroidal_elliptic.tex b/chapters/examples/toroidal_elliptic.tex
index 8fcef3a49b8fe0bd45c3ae248676e994ece0ca7e..0a15b2c062f601ea29e50e3e3771b3eb1544db50
--- a/chapters/examples/toroidal_elliptic.tex
+++ b/chapters/examples/toroidal_elliptic.tex
@@ -5940,8 +5940,7 @@
 
 The K3 analogue of this picture replaces $\bC^2$ by a K3
 surface~$S$: the K3 double current algebra $\fg_{K3}$
-(Chapter~\ref{ch:k3-times-e},
-Definition~\ref{def:k3-double-current-algebra}) substitutes
+substitutes
 $H^*(S,\bC)$ for $\bC[u,v]$ and the Mukai pairing for the
 polynomial residue. Its quantization should produce a
 ``K3 Yangian'' standing in the same relation to $\fg_{K3}$ as the
@@ -6018,7 +6017,7 @@
   At $t \to 1$: the second parameter $w$ decouples and
   $\Delta_{z,w}$ reduces to the single-parameter
   Drinfeld coproduct $\Delta_z(T(u)) = T(u) \otimes T(u - z)$
-  of Theorem~\textup{\ref{thm:w-infty-chiral-qg}}.
+  of Proposition~\textup{\ref{prop:universal-coproduct}}.
 \end{enumerate}
 No two-parameter coproduct $\Delta_{z,w}$ currently exists in
 the literature or in this programme's compute infrastructure.
@@ -6034,7 +6033,7 @@
   $(q_1,q_2,q_3)$.
 \item Promote the DDCA shadow to an explicit $\Delta_{z,w}$
   formula aligned with the $R(u,v)$ surface in
-  \S\ref{subsec:quantum-chiral-algebras-6d}.
+  \S\ref{subsec:chiral-qg-wilson}.
 \item Build a compute witness at low modes: $w = 0$ reduces
   to existing $\Delta_z$; rational limit gives the DDCA
   shift; Miki sends $\Delta_{z,w} \to \Delta_{w,z}$.
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index ddbdfe60d9c9df04ba6f3acf48deee73523a64dc..3ce4e679084f2f25672104c7a00684df5e9f3b26
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -320,7 +320,7 @@
 Drinfeld coproduct from spin~$2$ to arbitrary spin, with the
 universal Miura coefficient $(\Psi{-}1)/\Psi$ on the leading
 cross-term $J \otimes W_{s-1}$ at every spin $s \ge 2$
-(Theorem~\ref{thm:miura-cross-universality}).
+(Proposition~\ref{prop:universal-coproduct}).
 
 \bigskip
 
@@ -328,7 +328,7 @@
 Volume~I defines $E_1$-chiral quantum groups abstractly. This
 volume constructs them concretely from CY geometry. The
 $E_1$-chiral bialgebra axioms (formalized in
-\S\ref{sec:e1-chiral-bialgebra}) require: (H1)~an $E_1$-chiral
+\S\ref{sec:e1-chiral-bialgebras}) require: (H1)~an $E_1$-chiral
 algebra $A$ on a curve $X$; (H2)~a spectral coproduct
 $\Delta_z \colon A \to A \otimes A$ (living on the OPEN/$E_1$
 colour); (H3)~an $R$-matrix $R(z)$ satisfying YBE; (H4)~RTT
diff --git a/chapters/theory/cy_categories.tex b/chapters/theory/cy_categories.tex
index f9b51871c44fa18a574c02fce8aaa49a49aa9c61..00d723a1cb5d4f2355a10cb2d9d3f86688259f09
--- a/chapters/theory/cy_categories.tex
+++ b/chapters/theory/cy_categories.tex
@@ -166,7 +166,7 @@
 Every smooth proper CY$_d$ category admits a cyclic $\Ainf$-enhancement, unique up to $\Ainf$-quasi-isomorphism preserving the pairing. The proof is due to Kontsevich--Soibelman in the formal case, Costello~\cite{Costello2005} for the TCFT enhancement, and Seidel~\cite{Seidel2008} for the Fukaya case.
 \end{theorem}
 
-At $d = 2$ the enhancement is explicit enough to compute directly; it drives the $K3$ computations feeding the Borcherds denominator (Vol~III Chapter~\ref{ch:k3}). At $d = 3$ the enhancement was constructed by Sheridan~\cite{Sheridan2015} for the quintic threefold, as part of the HMS proof; the general $d = 3$ construction remains programme-level (conditional on $\bS^3$-framing, see AP-CY6).
+At $d = 2$ the enhancement is explicit enough to compute directly; it drives the $K3$ computations feeding the Borcherds denominator (Vol~III Chapter~\ref{ch:k3-times-e}). At $d = 3$ the enhancement was constructed by Sheridan~\cite{Sheridan2015} for the quintic threefold, as part of the HMS proof; the general $d = 3$ construction remains programme-level (conditional on $\bS^3$-framing, see AP-CY6).
 
 \section{Interface with the CY-to-chiral functor $\Phi$}
 \label{sec:cy-cat-phi-interface}
@@ -194,7 +194,7 @@
 
 \begin{remark}[What $\Phi$ does not see]
 \label{rem:phi-does-not-see}
-Not every invariant of $\cC$ survives the passage through $\Phi$. The functor retains the cyclic $\Ainf$-structure and the Gerstenhaber bracket; it loses the fine structure of the triangulated / $\Ainf$ category (individual objects, t-structures, stability conditions) that is visible only via the fuller categorical CoHA construction of Chapter~\ref{ch:coha}. The kappa-spectrum (Vol~III CLAUDE.md) encodes which invariants survive: $\kappa_\mathrm{cat}$ is always present, $\kappa_\mathrm{ch}$ exists only when $\Phi$ is defined, and $\kappa_\mathrm{BKM}$ records the Borcherds-side lift for $K3 \times E$.
+Not every invariant of $\cC$ survives the passage through $\Phi$. The functor retains the cyclic $\Ainf$-structure and the Gerstenhaber bracket; it loses the fine structure of the triangulated / $\Ainf$ category (individual objects, t-structures, stability conditions) that is visible only via the fuller categorical CoHA construction of Chapter~\ref{ch:toric-coha}. The kappa-spectrum (Vol~III CLAUDE.md) encodes which invariants survive: $\kappa_\mathrm{cat}$ is always present, $\kappa_\mathrm{ch}$ exists only when $\Phi$ is defined, and $\kappa_\mathrm{BKM}$ records the Borcherds-side lift for $K3 \times E$.
 \end{remark}
 
 \begin{remark}[Cross-volume conventions]
diff --git a/chapters/theory/cy_to_chiral.tex b/chapters/theory/cy_to_chiral.tex
index 030fed4a9a2a7009ae05fdb0f3c431c8aed1fc83..14526e0aba63169841056220749304799a57fe10
--- a/chapters/theory/cy_to_chiral.tex
+++ b/chapters/theory/cy_to_chiral.tex
@@ -618,8 +618,8 @@
 homotopy is purely algebraic: it acts by
 $s(f_{i_0 \cdots i_q}) = f_{0 i_0 \cdots i_q}$ on \v{C}ech cochains and
 involves no PDE solving. The SDR data $(i, p, s)$ interfaces directly
-with the homotopy transfer theorem
-\textup{(}HTT, Theorem~\textup{\ref{thm:htt-general}}\textup{)},
+with the standard homotopy transfer theorem
+\textup{(}HTT\textup{)},
 transferring the $\Ainf$-structure from $\check{C}^\bullet(\cE nd(\cE))$
 to its cohomology $\Ext^\bullet(\cE, \cE)$.
 \end{theorem}
@@ -652,7 +652,7 @@
 (whether the formal series in the OPE coefficients converges to
 define honest holomorphic functions) requires separate input from
 the analytic completion programme (MC5,
-\S\ref{sec:analytic-sewing} of Vol~I). Specifically: the HTT
+the analytic sewing section of Vol~I). Specifically: the HTT
 produces transferred operations $\mu_k^{\mathrm{ch}}$ whose
 coefficients involve iterated applications of~$s$; each application
 introduces rational functions on the intersections $U_{i_0} \cap
@@ -1972,7 +1972,7 @@
  \bottomrule
 \end{tabular}
 \end{center}
-{\footnotesize $^*$The K3 entry records $\kappa_{\mathrm{ch}} = \chi(\cO_{\mathrm{K3}}) = 2$ (Proposition~\ref{prop:cy-kappa-d2}; verified via chiral de Rham, Chapter~\ref{ch:k3-times-e}). The distinct quantity $\dim \HH_*(D^b(\mathrm{K3}))/2 = 12$ arises from an alternative algebraization (the Monster orbifold); the full trichotomy ($\kappa_{\mathrm{ch}} \in \{2, 12, 24\}$) is developed in Section~\ref{subsec:k3-three-algebraizations} of Chapter~\ref{ch:k3-times-e}.
+{\footnotesize $^*$The K3 entry records $\kappa_{\mathrm{ch}} = \chi(\cO_{\mathrm{K3}}) = 2$ (Proposition~\ref{prop:cy-kappa-d2}; verified via chiral de Rham, Chapter~\ref{ch:k3-times-e}). The distinct quantity $\dim \HH_*(D^b(\mathrm{K3}))/2 = 12$ arises from an alternative algebraization (the Monster orbifold); the full trichotomy ($\kappa_{\mathrm{ch}} \in \{2, 12, 24\}$) is developed in the K3 discussion of Chapter~\ref{ch:k3-times-e}.
 
 $^\dagger$The $K3 \times E$ entry records $\kappa_{\mathrm{ch}} = 3$ by additivity (Proposition~\ref{prop:categorical-euler}: $\kappa_{\mathrm{ch}}(\mathrm{K3}) + \kappa_{\mathrm{ch}}(E) = 2 + 1$). The Borcherds automorphic weight is $\kappa_{\mathrm{BKM}} = 5 = \mathrm{wt}(\Delta_5)$, a distinct invariant.}
 
diff --git a/chapters/theory/drinfeld_center.tex b/chapters/theory/drinfeld_center.tex
index ac67d4e3a2ed8fab94fcb3fc63933d8650a92ac9..a711d853438f9e6a0e6fdd4e5dac61154b7b3c24
--- a/chapters/theory/drinfeld_center.tex
+++ b/chapters/theory/drinfeld_center.tex
@@ -726,7 +726,7 @@
 produces only symmetric braiding. The distinction is the
 deep reason for the $\Eone$ stabilization theorem
 (Chapter~\ref{ch:cy-to-chiral},
-Theorem~\ref{thm:e1-stabilization}).
+Theorem~\ref{thm:e1-stabilization-cy}).
 
 \begin{proposition}[$E_3$ restriction gives symmetric braiding]
 \label{prop:e3-symmetric-braiding}
diff --git a/chapters/theory/e1_chiral_algebras.tex b/chapters/theory/e1_chiral_algebras.tex
index 75484d2fff759dc21313b5595a8abade7d55d203..b533b2f5640db9eba4046a61106787f2c19a0d53
--- a/chapters/theory/e1_chiral_algebras.tex
+++ b/chapters/theory/e1_chiral_algebras.tex
@@ -63,7 +63,7 @@
 via holomorphic Chern--Simons; conjectural in general).
 The further $E_3$-topological upgrade requires a conformal
 vector at non-critical level
-(Volume~I, Theorem~\textup{\ref*{thm:topologization}}).
+(Volume~I, the topologization theorem).
 \end{definition}
 
 The closed colour carries $E_2$ structure from
@@ -128,7 +128,7 @@
 
 \begin{remark}[Three bars, one functor]
 \label{rem:three-bars-vol3}
-The CY-to-chiral functor $\Phi$ of Chapter~\ref{ch:cy-chiral-functor} has three natural composites. $\Phi_{E_1}$ produces $B^{\mathrm{ord}}(A_C)$; this is the ordered bar sensed by the Yangian. $\mathrm{av} \circ \Phi_{E_1}$ produces $B^{\Sigma}(A_C)$; this is the symmetric bar sensed by the modular characteristic $\kappa_{\mathrm{ch}}$. The full $E_2$ enhancement $\Phi_{E_2}$ produces the Drinfeld-centered bar $B^{E_2}(A_C) = \cZ(B^{\mathrm{ord}}(A_C))$; this is the braided bar sensed by the quantum group. All three factor through $\Phi_{E_1}$. This is the volume's motto: the ordered bar is the primitive.
+The CY-to-chiral functor $\Phi$ of Chapter~\ref{ch:cy-to-chiral} has three natural composites. $\Phi_{E_1}$ produces $B^{\mathrm{ord}}(A_C)$; this is the ordered bar sensed by the Yangian. $\mathrm{av} \circ \Phi_{E_1}$ produces $B^{\Sigma}(A_C)$; this is the symmetric bar sensed by the modular characteristic $\kappa_{\mathrm{ch}}$. The full $E_2$ enhancement $\Phi_{E_2}$ produces the Drinfeld-centered bar $B^{E_2}(A_C) = \cZ(B^{\mathrm{ord}}(A_C))$; this is the braided bar sensed by the quantum group. All three factor through $\Phi_{E_1}$. This is the volume's motto: the ordered bar is the primitive.
 \end{remark}
 
 \section{$E_1$-chiral algebras from CY categories}
@@ -153,7 +153,7 @@
 Let $\cC$ be a CY$_3$ category with a chain-level $S^3$-framing on $\mathrm{HC}^-_3(\cC)$ (the condition of Conjecture~CY-A$_3$). Then the ordered bar complex of the cyclic $A_\infty$ algebra $A_\cC$ carries an $E_1$-chiral structure whose representation category is a braided monoidal refinement of the BPS Yangian of $\cC$.
 \end{conjecture}
 
-The conjecture is conditional on the chain-level framing; the unconditional statement requires the full CY-A$_3$ programme. Every downstream result in \ref{part:examples} and \ref{part:connections} that uses the BPS Yangian inherits this conditionality. The connection to Maulik-Okounkov and Costello-Witten cohomological Hall algebras is traced in Chapter~\ref{ch:cha-yangian}.
+The conjecture is conditional on the chain-level framing; the unconditional statement requires the full CY-A$_3$ programme. Every downstream result in \ref{part:examples} and \ref{part:connections} that uses the BPS Yangian inherits this conditionality. The connection to Maulik-Okounkov and Costello-Witten cohomological Hall algebras is traced in Chapter~\ref{ch:toric-coha}.
 
 \begin{proposition}[$E_2$ enhancement via Drinfeld center]
 \label{prop:e2-enhancement-drinfeld}
@@ -318,7 +318,7 @@
 
 \begin{remark}[How this chapter is used downstream]
 \label{rem:downstream-usage}
-Chapters~\ref{ch:braided-factorization}, \ref{ch:drinfeld-center}, and \ref{ch:quantum-group-reps} use this chapter as the source of the ordered bar coalgebra and the averaging map. Chapter~\ref{ch:cy-chiral-functor} uses Proposition~\ref{prop:e1-sector-d2} as the $d=2$ existence statement for $A_\cC$. Every braided monoidal category that appears later is the Drinfeld center of an underlying ordered one.
+Chapters~\ref{ch:braided-factorization}, \ref{ch:drinfeld-center}, and \ref{ch:quantum-group-reps} use this chapter as the source of the ordered bar coalgebra and the averaging map. Chapter~\ref{ch:cy-to-chiral} uses Proposition~\ref{prop:e1-sector-d2} as the $d=2$ existence statement for $A_\cC$. Every braided monoidal category that appears later is the Drinfeld center of an underlying ordered one.
 \end{remark}
 
 \section{Operadic dictionary for the CY reader}
@@ -1447,7 +1447,7 @@
 cutting the elliptic curve.}
 For the product CY$_3$ manifold $X = K3 \times E$, the factorization
 homology integral $\int_{K3} \cF|_{K3}$ of
-Section~\ref{sec:k3-perturbative-fact-homology} produces a chiral algebra
+Section~\ref{subsec:fact-homology-k3xe} produces a chiral algebra
 $A_E$ on the residual elliptic curve $E$.  The coproduct on $A_E$ arises
 from cutting $E$ into two intervals via excision.  Concretely, choose a
 collar-gluing decomposition $E = I_1 \cup_{S^0 \times \R} I_2$ (cutting
diff --git a/chapters/theory/e2_chiral_algebras.tex b/chapters/theory/e2_chiral_algebras.tex
index 4d9c49d33b9b71c9728719844b5387b9c256ec23..8a25a3037dc9569752a97c0fc75347a4033380af
--- a/chapters/theory/e2_chiral_algebras.tex
+++ b/chapters/theory/e2_chiral_algebras.tex
@@ -194,7 +194,7 @@
 \label{sec:drinfeld-center-bridge}
 
 Volume~II constructs $\Phi_{E_1}$ and proves $E_1$-chiral Koszul
-duality (see \ref{part:e1-core} of \cite{VolII}). The Drinfeld center
+duality (see Part~I of \cite{VolII}). The Drinfeld center
 $Z\colon E_1\text{-}\Cat \xrightarrow{\sim} E_2\text{-}\Cat$
 (under dualizability) is the categorical passage from ordered
 monoidal data to braided monoidal data. On the bar side it matches the
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 30392e44f20b6614f1f54981964db6c0329363e5..69d953d96d354add714abf2eec933a753336234a
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -201,7 +201,7 @@
 \]
 The SDR data $(i, p, s)$ interfaces directly with the homotopy transfer theorem (HTT), transferring the $A_\infty$-structure from \v{C}ech cochains $\check{C}^\bullet(\mathcal{E}nd(\mathcal{E}))$ to its cohomology $\mathrm{Ext}^\bullet(\mathcal{E}, \mathcal{E})$. The transferred operations $\mu_k^{\mathrm{ch}}$ are given by sums over planar trees whose internal edges are decorated by the homotopy~$s$; each application of~$s$ introduces rational functions on the affine intersections, and the resulting chiral operations are well-defined as formal power series.
 
-The scope is perturbative: the \v{C}ech homotopy produces an algebraic $A_\infty$-structure on the Ext algebra, but convergence of the resulting series to holomorphic functions (the non-perturbative statement) requires separate input from the analytic completion programme of Volume~I (MC5, \S\ref{sec:analytic-sewing}). The perturbative statement suffices for the formal CY-to-chiral functor and for all combinatorial applications in this volume. The full construction, including the proof that the SDR conditions hold and the scope qualification, is Theorem~\ref{thm:cech-contracting-homotopy} in Chapter~\ref{ch:cy-to-chiral}.
+The scope is perturbative: the \v{C}ech homotopy produces an algebraic $A_\infty$-structure on the Ext algebra, but convergence of the resulting series to holomorphic functions (the non-perturbative statement) requires separate input from the analytic completion programme of Volume~I (MC5, the analytic sewing section there). The perturbative statement suffices for the formal CY-to-chiral functor and for all combinatorial applications in this volume. The full construction, including the proof that the SDR conditions hold and the scope qualification, is Theorem~\ref{thm:cech-contracting-homotopy} in Chapter~\ref{ch:cy-to-chiral}.
 
 Three independent consistency checks confirm the resulting chiral data for the quintic: the Gepner model matrix factorization (via mirror symmetry, $\mathrm{MF}(x_1^5 + \cdots + x_5^5)$), the large-volume Hodge--Kodaira--Rosenberg limit ($\mathrm{HKR}$ degeneration of $\mathrm{Ext}^\bullet$ to Dolbeault cohomology), and the Gopakumar--Vafa integrality of the resulting genus-$g$ amplitudes. All three produce the same modular characteristic $\chi/2 = -100$ (the MacMahon-normalised form of $\kappa_{\mathrm{cat}}$ at $d=3$).
 
@@ -277,7 +277,7 @@
  \item The moonshine multiplier: $A_n = \kappa_{\mathrm{cat}} \cdot \dim(\rho_n)$ identifies the factor $2$ in $Z_{K3} = 2\,\phi_{0,1}$.
  \item The categorical $\Etwo$-obstruction for CY$_3$ (Proposition~\ref{prop:e1-obstruction-categorical}): Serre duality forces antisymmetry of the Euler form, universally obstructing $\Etwo$-enhancement without torus hypotheses.
  \item Quiver-chart gluing for toric CY$_3$ (Theorem~\ref{thm:toric-chart-gluing}): the global $\Eone$-chiral algebra is assembled as a homotopy colimit of McKay-chart CoHAs, with $E_2$ descent degeneration and Costello--Li comparison.
- \item The K3 double current algebra $\fg_{K3}$ (Definition~\ref{def:k3-double-current-algebra}): the finite-dimensional analogue of the DDCA in which $\bC[u,v]$ is replaced by $H^*(S,\bC)$ with the Mukai pairing.
+ \item The K3 double current algebra $\fg_{K3}$: the finite-dimensional analogue of the DDCA in which $\bC[u,v]$ is replaced by $H^*(S,\bC)$ with the Mukai pairing.
  \item Forty-two CY/BKM compute engines with $5{,}700{+}$ tests across the standard CY landscape.
 \end{itemize}
 
@@ -360,7 +360,7 @@
 \item \emph{Descent theorem.}
  \v{C}ech descent for $E_1$-algebras over the Bridgeland
  stability manifold. Proved for toric CY3
- (Proposition~\ref{prop:e1-descent-unobstructed}); open for
+ (Theorem~\ref{thm:toric-chart-gluing}); open for
  compact CY3 beyond the chart-atlas regime.
 \item \emph{Higher-dimensional CY shadows.}
  The $E_n$ stabilization theorem
@@ -394,12 +394,12 @@
 
 \emph{Quantum group representations} (Chapter~\ref{ch:quantum-group-reps}). The representation-theoretic target. The braided monoidal category $\mathrm{Rep}_q(\mathfrak{g})$ is what the CY programme aims to realize: Conjecture~CY-C predicts that $\mathrm{Rep}_q(\mathfrak{g}) \simeq \mathrm{Rep}^{E_2}(A_\cC)$ for a CY category $\cC(\mathfrak{g}, q)$. The Kazhdan--Lusztig equivalence $\mathrm{Rep}_q(\mathfrak{g}) \simeq \mathrm{KL}_k(\mathfrak{g})$ at roots of unity is the prototype: the Volume~I bar complex $B(V_k(\mathfrak{g}))$ encodes the quantum group $R$-matrix in its degree-$(1,1)$ component, and the DK bridge (Volume~II, MC3 for all simple types) recovers the quantum group categorical structure. The affine Yangian realization (Chapter~\ref{ch:toric-coha}) provides the $E_1$-sector; the Drinfeld center (Chapter~\ref{ch:drinfeld-center}) provides the $E_2$-enhancement.
 
-In addition to the four standard families, the toroidal and elliptic algebras chapter (Chapter~\ref{chap:toroidal-elliptic}) develops the $K3 \times E$ programme in full: the generalized root datum, the BKM superalgebra $\mathfrak{g}_{\Delta_5}$ with its Igusa cusp form denominator identity, the shadow--Siegel gap theorem, thirteen structural results (K3-1 through K3-13), all ten research programmes (A through J), and the DDCA--toroidal bridge identifying the deformed double current algebra as the rational degeneration of the quantum toroidal algebra (Conjecture~\ref{conj:ddca-toroidal-bridge}). The K3 double current algebra $\fg_{K3}$ (Chapter~\ref{ch:k3-times-e}, Definition~\ref{def:k3-double-current-algebra}) provides the K3 analogue of the DDCA, replacing $\bC[u,v]$ with $H^*(S,\bC)$. The toric CY$_3$ CoHA chapter (Chapter~\ref{ch:toric-coha}) develops the affine Yangian and $\mathcal{W}_{1+\infty}$ side: the Jordan quiver gives $Y(\widehat{\mathfrak{gl}}_1) \simeq \mathcal{W}_{1+\infty}$, the toric fan is the Dynkin data, and the shuffle algebra presentation connects to the KZ equations of Volume~I.
+In addition to the four standard families, the toroidal and elliptic algebras chapter (Chapter~\ref{chap:toroidal-elliptic}) develops the $K3 \times E$ programme in full: the generalized root datum, the BKM superalgebra $\mathfrak{g}_{\Delta_5}$ with its Igusa cusp form denominator identity, the shadow--Siegel gap theorem, thirteen structural results (K3-1 through K3-13), all ten research programmes (A through J), and the DDCA--toroidal bridge identifying the deformed double current algebra as the rational degeneration of the quantum toroidal algebra (Conjecture~\ref{conj:ddca-toroidal-bridge}). The K3 double current algebra $\fg_{K3}$, discussed in the DDCA--toroidal bridge of Chapter~\ref{ch:k3-times-e}, provides the K3 analogue of the DDCA, replacing $\bC[u,v]$ with $H^*(S,\bC)$. The toric CY$_3$ CoHA chapter (Chapter~\ref{ch:toric-coha}) develops the affine Yangian and $\mathcal{W}_{1+\infty}$ side: the Jordan quiver gives $Y(\widehat{\mathfrak{gl}}_1) \simeq \mathcal{W}_{1+\infty}$, the toric fan is the Dynkin data, and the shuffle algebra presentation connects to the KZ equations of Volume~I.
 
 \section{Guide for the reader}
 \label{sec:guide}
 
-Part~\ref{part:cy-categories} establishes the categorical foundations: CY categories, cyclic $\Ainf$-structures, the Hochschild calculus, and the $E_1$/$E_2$/$E_n$ chiral hierarchy with the framing obstruction tower. Part~\ref{part:bridge} constructs the bridge functor $\Phi$ from CY categories to quantum chiral algebras and proves Theorems CY-A (for $d = 2$) and CY-D, with the identification of automorphic correction and shadow obstruction tower as the central result. Part~\ref{part:examples} treats quantum groups and their braided factorization structure, including the Drinfeld center as the bulk algebra. Part~\ref{part:connections} works through the standard landscape: the toroidal and elliptic algebras chapter develops the $K3 \times E$ programme (K3-1 through K3-13, programmes A through J), alongside toric CY3 CoHAs, Fukaya categories, derived categories, matrix factorizations (ADE singularities and W-algebras), and quantum group representations (Kazhdan--Lusztig, affine Yangians, critical CoHAs). Part~\ref{part:frontier} connects to the geometric Langlands programme and to Volumes~I and~II via the bar-cobar bridge and the modular Koszul bridge. The working notes (\S\ref{sec:working-notes}) record the research frontier.
+Part~\ref{part:cy-categories} establishes the categorical foundations: CY categories, cyclic $\Ainf$-structures, the Hochschild calculus, and the $E_1$/$E_2$/$E_n$ chiral hierarchy with the framing obstruction tower. Part~\ref{part:bridge} constructs the bridge functor $\Phi$ from CY categories to quantum chiral algebras and proves Theorems CY-A (for $d = 2$) and CY-D, with the identification of automorphic correction and shadow obstruction tower as the central result. Part~\ref{part:examples} treats quantum groups and their braided factorization structure, including the Drinfeld center as the bulk algebra. Part~\ref{part:connections} works through the standard landscape: the toroidal and elliptic algebras chapter develops the $K3 \times E$ programme (K3-1 through K3-13, programmes A through J), alongside toric CY3 CoHAs, Fukaya categories, derived categories, matrix factorizations (ADE singularities and W-algebras), and quantum group representations (Kazhdan--Lusztig, affine Yangians, critical CoHAs). Part~\ref{part:frontier} connects to the geometric Langlands programme and to Volumes~I and~II via the bar-cobar bridge and the modular Koszul bridge. The separate working notes record the research frontier.
 
 \section{Conventions and notation}
 \label{sec:conventions-intro}

file update:
diff --git a/chapters/connections/cy_holographic_datum_master.tex b/chapters/connections/cy_holographic_datum_master.tex
index 2a66e8a0ca86f097e30b0de99c082498014430c6..b0ef34640300f22c24d57ee10a207c331065f31d
--- a/chapters/connections/cy_holographic_datum_master.tex
+++ b/chapters/connections/cy_holographic_datum_master.tex
@@ -943,7 +943,7 @@
 bar-cobar, CoHA / perverse coherent sheaves, classical CY Poisson
 coisson, MO stable envelope, affine super Yangian for toric CY$_3$,
 elliptic Sklyanin for toroidal CY, Gaudin from CY$_3$
-(Theorem~\ref{thm:cy-seven-face-master} above).
+(Conjecture~\ref{conj:cy-seven-face-master} above).
 \end{enumerate}
 The three master theorems are mutually compatible: under the CY-to-chiral
 functor $\Phi$, face~$i$ of Vol~III maps to a specialization of face~$i$
diff --git a/chapters/connections/modular_koszul_bridge.tex b/chapters/connections/modular_koszul_bridge.tex
index 1199c5aaa32e71f085dd3b7131c8f9aeadb1148c..a423d35b2ce162a9f56bb568768ae1bed7bef2f6
--- a/chapters/connections/modular_koszul_bridge.tex
+++ b/chapters/connections/modular_koszul_bridge.tex
@@ -234,7 +234,7 @@
 \end{theorem}
 
 \begin{proof}[Attribution]
-Parts (i), (iii), (iv) are Vol~I/II results (\S\ref{sec:k3e-cross-volume}, items K3-1 through K3-13, proved in the K3 modular-tower chapter of Vol~I and in the Vol~II 3D quantum gravity treatment, \ref{part:3d-qg} there). Part (ii) is the Borcherds lift of Borcherds (1998); its use as a modular characteristic is the observation of AP-CY8, not a theorem of Vol~III. The conditionality on propagates from Theorem~\ref{thm:cy-shadow-cohft}.
+Parts (i), (iii), (iv) are Vol~I/II results (\S\ref{sec:k3e-cross-volume}, items K3-1 through K3-13, proved in the K3 modular-tower chapter of Vol~I and in Part~III of Vol~II's 3D quantum gravity treatment). Part (ii) is the Borcherds lift of Borcherds (1998); its use as a modular characteristic is the observation of AP-CY8, not a theorem of Vol~III. The conditionality on propagates from Theorem~\ref{thm:cy-shadow-cohft}.
 \end{proof}
 
 \begin{remark}[Kappa-spectrum verification for $K3 \times E$]
diff --git a/chapters/examples/quantum_group_reps.tex b/chapters/examples/quantum_group_reps.tex
index e6b19a4c52de09f17af4b5f794d5f7269f4076b4..5213e6bfc9cb828c11c98b50aa32549aa228cfbf
--- a/chapters/examples/quantum_group_reps.tex
+++ b/chapters/examples/quantum_group_reps.tex
@@ -503,7 +503,7 @@
  additional data);
  \item $\kappa_{\mathrm{BKM}}$: the BKM modular weight, a
  number-theoretic invariant arising from the BKM denominator
- formula (Chapter~\ref{ch:toroidal-elliptic}; distinct from
+ formula (Chapter~\ref{chap:toroidal-elliptic}; distinct from
  both $\kappa_{\mathrm{cat}}$ and $\kappa_{\mathrm{ch}}$).
 \end{enumerate}
 For CY$_2$ categories with $\frakg$-symmetry, all three can be
diff --git a/chapters/examples/toric_cy3_coha.tex b/chapters/examples/toric_cy3_coha.tex
index 2b8821c0fd545c77e9d18a4180e8e67d3c4459be..94da66b26dadb3a8dcd2e91287fd7092ea5a944c
--- a/chapters/examples/toric_cy3_coha.tex
+++ b/chapters/examples/toric_cy3_coha.tex
@@ -205,7 +205,7 @@
 \end{theorem}
 
 \begin{proof}
-(i) The compact base $\bP^1 \times \bP^1$ has $\chi(\bP^1 \times \bP^1) = 4$ (each factor contributes $\chi(\bP^1) = 2$), so $\kappa_{\mathrm{ch}} = \chi/2 = 2$ by the general local-surface formula (Remark~\ref{rem:toric-structural-patterns}).
+(i) The compact base $\bP^1 \times \bP^1$ has $\chi(\bP^1 \times \bP^1) = 4$ (each factor contributes $\chi(\bP^1) = 2$), so $\kappa_{\mathrm{ch}} = \chi/2 = 2$ by the general local-surface formula (Remark~\ref{rem:toric-kappa-patterns}).
 
 (ii) The intersection form on $H^2(\bP^1 \times \bP^1)$ in the basis $\{e_1, e_2\}$ is $\langle e_i, e_j \rangle = \delta_{ij}$ (the two rulings are orthogonal with self-intersection $0$ in the total space, but the relevant inner product for the shadow metric is the Euler pairing $\chi(e_i, e_j) = \delta_{ij}$).
 
@@ -654,7 +654,7 @@
 the chart gluing by descent, the shadow tower by the MC equation.
 These components are \emph{a priori} separate structures on the
 same algebra. The Vol~I chiral quantum group equivalence
-(Theorem~\ref{thm:chiral-qg-equiv}) asserts that three of them
+asserts that three of them
 (the vertex $R$-matrix, the chiral $A_\infty$-structure, and the
 chiral coproduct) determine each other on the Koszul locus. The theorem
 below specializes the abstract equivalence to the toric CY3 setting,
@@ -746,8 +746,7 @@
 
 \begin{proof}
 The abstract equivalence (I) $\leftrightarrow$ (II)
-$\leftrightarrow$ (III) is
-Theorem~\ref{thm:chiral-qg-equiv} of Vol~I, proved for any
+$\leftrightarrow$ (III) is the Vol~I chiral quantum group equivalence, proved for any
 $\Eone$-chiral algebra on the Koszul locus. The content of the
 present theorem is the identification of each abstract vertex
 with the independently constructed toric CY3 structure.
@@ -755,7 +754,7 @@
 \textit{Component~\textup{(I)}: $R$-matrix.}
 The $\Eone$-chiral algebra $A_X$ carries a vertex
 $R$-matrix by the general theory
-(Theorem~\ref{thm:chiral-qg-equiv}(I)). For toric CY3, the
+(item~\textup{(I)} of that equivalence). For toric CY3, the
 Maulik--Okounkov stable-envelope construction provides an
 independent $R$-matrix on $Y^+(\widehat{\fg}_{Q_X})$-modules.
 The two coincide because both solve the same Yang--Baxter
diff --git a/chapters/examples/toroidal_elliptic.tex b/chapters/examples/toroidal_elliptic.tex
index 8fcef3a49b8fe0bd45c3ae248676e994ece0ca7e..0a15b2c062f601ea29e50e3e3771b3eb1544db50
--- a/chapters/examples/toroidal_elliptic.tex
+++ b/chapters/examples/toroidal_elliptic.tex
@@ -5940,8 +5940,7 @@
 
 The K3 analogue of this picture replaces $\bC^2$ by a K3
 surface~$S$: the K3 double current algebra $\fg_{K3}$
-(Chapter~\ref{ch:k3-times-e},
-Definition~\ref{def:k3-double-current-algebra}) substitutes
+substitutes
 $H^*(S,\bC)$ for $\bC[u,v]$ and the Mukai pairing for the
 polynomial residue. Its quantization should produce a
 ``K3 Yangian'' standing in the same relation to $\fg_{K3}$ as the
@@ -6018,7 +6017,7 @@
   At $t \to 1$: the second parameter $w$ decouples and
   $\Delta_{z,w}$ reduces to the single-parameter
   Drinfeld coproduct $\Delta_z(T(u)) = T(u) \otimes T(u - z)$
-  of Theorem~\textup{\ref{thm:w-infty-chiral-qg}}.
+  of Proposition~\textup{\ref{prop:universal-coproduct}}.
 \end{enumerate}
 No two-parameter coproduct $\Delta_{z,w}$ currently exists in
 the literature or in this programme's compute infrastructure.
@@ -6034,7 +6033,7 @@
   $(q_1,q_2,q_3)$.
 \item Promote the DDCA shadow to an explicit $\Delta_{z,w}$
   formula aligned with the $R(u,v)$ surface in
-  \S\ref{subsec:quantum-chiral-algebras-6d}.
+  \S\ref{subsec:chiral-qg-wilson}.
 \item Build a compute witness at low modes: $w = 0$ reduces
   to existing $\Delta_z$; rational limit gives the DDCA
   shift; Miki sends $\Delta_{z,w} \to \Delta_{w,z}$.
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index ddbdfe60d9c9df04ba6f3acf48deee73523a64dc..3ce4e679084f2f25672104c7a00684df5e9f3b26
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -320,7 +320,7 @@
 Drinfeld coproduct from spin~$2$ to arbitrary spin, with the
 universal Miura coefficient $(\Psi{-}1)/\Psi$ on the leading
 cross-term $J \otimes W_{s-1}$ at every spin $s \ge 2$
-(Theorem~\ref{thm:miura-cross-universality}).
+(Proposition~\ref{prop:universal-coproduct}).
 
 \bigskip
 
@@ -328,7 +328,7 @@
 Volume~I defines $E_1$-chiral quantum groups abstractly. This
 volume constructs them concretely from CY geometry. The
 $E_1$-chiral bialgebra axioms (formalized in
-\S\ref{sec:e1-chiral-bialgebra}) require: (H1)~an $E_1$-chiral
+\S\ref{sec:e1-chiral-bialgebras}) require: (H1)~an $E_1$-chiral
 algebra $A$ on a curve $X$; (H2)~a spectral coproduct
 $\Delta_z \colon A \to A \otimes A$ (living on the OPEN/$E_1$
 colour); (H3)~an $R$-matrix $R(z)$ satisfying YBE; (H4)~RTT
diff --git a/chapters/theory/cy_categories.tex b/chapters/theory/cy_categories.tex
index f9b51871c44fa18a574c02fce8aaa49a49aa9c61..00d723a1cb5d4f2355a10cb2d9d3f86688259f09
--- a/chapters/theory/cy_categories.tex
+++ b/chapters/theory/cy_categories.tex
@@ -166,7 +166,7 @@
 Every smooth proper CY$_d$ category admits a cyclic $\Ainf$-enhancement, unique up to $\Ainf$-quasi-isomorphism preserving the pairing. The proof is due to Kontsevich--Soibelman in the formal case, Costello~\cite{Costello2005} for the TCFT enhancement, and Seidel~\cite{Seidel2008} for the Fukaya case.
 \end{theorem}
 
-At $d = 2$ the enhancement is explicit enough to compute directly; it drives the $K3$ computations feeding the Borcherds denominator (Vol~III Chapter~\ref{ch:k3}). At $d = 3$ the enhancement was constructed by Sheridan~\cite{Sheridan2015} for the quintic threefold, as part of the HMS proof; the general $d = 3$ construction remains programme-level (conditional on $\bS^3$-framing, see AP-CY6).
+At $d = 2$ the enhancement is explicit enough to compute directly; it drives the $K3$ computations feeding the Borcherds denominator (Vol~III Chapter~\ref{ch:k3-times-e}). At $d = 3$ the enhancement was constructed by Sheridan~\cite{Sheridan2015} for the quintic threefold, as part of the HMS proof; the general $d = 3$ construction remains programme-level (conditional on $\bS^3$-framing, see AP-CY6).
 
 \section{Interface with the CY-to-chiral functor $\Phi$}
 \label{sec:cy-cat-phi-interface}
@@ -194,7 +194,7 @@
 
 \begin{remark}[What $\Phi$ does not see]
 \label{rem:phi-does-not-see}
-Not every invariant of $\cC$ survives the passage through $\Phi$. The functor retains the cyclic $\Ainf$-structure and the Gerstenhaber bracket; it loses the fine structure of the triangulated / $\Ainf$ category (individual objects, t-structures, stability conditions) that is visible only via the fuller categorical CoHA construction of Chapter~\ref{ch:coha}. The kappa-spectrum (Vol~III CLAUDE.md) encodes which invariants survive: $\kappa_\mathrm{cat}$ is always present, $\kappa_\mathrm{ch}$ exists only when $\Phi$ is defined, and $\kappa_\mathrm{BKM}$ records the Borcherds-side lift for $K3 \times E$.
+Not every invariant of $\cC$ survives the passage through $\Phi$. The functor retains the cyclic $\Ainf$-structure and the Gerstenhaber bracket; it loses the fine structure of the triangulated / $\Ainf$ category (individual objects, t-structures, stability conditions) that is visible only via the fuller categorical CoHA construction of Chapter~\ref{ch:toric-coha}. The kappa-spectrum (Vol~III CLAUDE.md) encodes which invariants survive: $\kappa_\mathrm{cat}$ is always present, $\kappa_\mathrm{ch}$ exists only when $\Phi$ is defined, and $\kappa_\mathrm{BKM}$ records the Borcherds-side lift for $K3 \times E$.
 \end{remark}
 
 \begin{remark}[Cross-volume conventions]
diff --git a/chapters/theory/cy_to_chiral.tex b/chapters/theory/cy_to_chiral.tex
index 030fed4a9a2a7009ae05fdb0f3c431c8aed1fc83..14526e0aba63169841056220749304799a57fe10
--- a/chapters/theory/cy_to_chiral.tex
+++ b/chapters/theory/cy_to_chiral.tex
@@ -618,8 +618,8 @@
 homotopy is purely algebraic: it acts by
 $s(f_{i_0 \cdots i_q}) = f_{0 i_0 \cdots i_q}$ on \v{C}ech cochains and
 involves no PDE solving. The SDR data $(i, p, s)$ interfaces directly
-with the homotopy transfer theorem
-\textup{(}HTT, Theorem~\textup{\ref{thm:htt-general}}\textup{)},
+with the standard homotopy transfer theorem
+\textup{(}HTT\textup{)},
 transferring the $\Ainf$-structure from $\check{C}^\bullet(\cE nd(\cE))$
 to its cohomology $\Ext^\bullet(\cE, \cE)$.
 \end{theorem}
@@ -652,7 +652,7 @@
 (whether the formal series in the OPE coefficients converges to
 define honest holomorphic functions) requires separate input from
 the analytic completion programme (MC5,
-\S\ref{sec:analytic-sewing} of Vol~I). Specifically: the HTT
+the analytic sewing section of Vol~I). Specifically: the HTT
 produces transferred operations $\mu_k^{\mathrm{ch}}$ whose
 coefficients involve iterated applications of~$s$; each application
 introduces rational functions on the intersections $U_{i_0} \cap
@@ -1972,7 +1972,7 @@
  \bottomrule
 \end{tabular}
 \end{center}
-{\footnotesize $^*$The K3 entry records $\kappa_{\mathrm{ch}} = \chi(\cO_{\mathrm{K3}}) = 2$ (Proposition~\ref{prop:cy-kappa-d2}; verified via chiral de Rham, Chapter~\ref{ch:k3-times-e}). The distinct quantity $\dim \HH_*(D^b(\mathrm{K3}))/2 = 12$ arises from an alternative algebraization (the Monster orbifold); the full trichotomy ($\kappa_{\mathrm{ch}} \in \{2, 12, 24\}$) is developed in Section~\ref{subsec:k3-three-algebraizations} of Chapter~\ref{ch:k3-times-e}.
+{\footnotesize $^*$The K3 entry records $\kappa_{\mathrm{ch}} = \chi(\cO_{\mathrm{K3}}) = 2$ (Proposition~\ref{prop:cy-kappa-d2}; verified via chiral de Rham, Chapter~\ref{ch:k3-times-e}). The distinct quantity $\dim \HH_*(D^b(\mathrm{K3}))/2 = 12$ arises from an alternative algebraization (the Monster orbifold); the full trichotomy ($\kappa_{\mathrm{ch}} \in \{2, 12, 24\}$) is developed in the K3 discussion of Chapter~\ref{ch:k3-times-e}.
 
 $^\dagger$The $K3 \times E$ entry records $\kappa_{\mathrm{ch}} = 3$ by additivity (Proposition~\ref{prop:categorical-euler}: $\kappa_{\mathrm{ch}}(\mathrm{K3}) + \kappa_{\mathrm{ch}}(E) = 2 + 1$). The Borcherds automorphic weight is $\kappa_{\mathrm{BKM}} = 5 = \mathrm{wt}(\Delta_5)$, a distinct invariant.}
 
diff --git a/chapters/theory/drinfeld_center.tex b/chapters/theory/drinfeld_center.tex
index ac67d4e3a2ed8fab94fcb3fc63933d8650a92ac9..a711d853438f9e6a0e6fdd4e5dac61154b7b3c24
--- a/chapters/theory/drinfeld_center.tex
+++ b/chapters/theory/drinfeld_center.tex
@@ -726,7 +726,7 @@
 produces only symmetric braiding. The distinction is the
 deep reason for the $\Eone$ stabilization theorem
 (Chapter~\ref{ch:cy-to-chiral},
-Theorem~\ref{thm:e1-stabilization}).
+Theorem~\ref{thm:e1-stabilization-cy}).
 
 \begin{proposition}[$E_3$ restriction gives symmetric braiding]
 \label{prop:e3-symmetric-braiding}
diff --git a/chapters/theory/e1_chiral_algebras.tex b/chapters/theory/e1_chiral_algebras.tex
index 75484d2fff759dc21313b5595a8abade7d55d203..b533b2f5640db9eba4046a61106787f2c19a0d53
--- a/chapters/theory/e1_chiral_algebras.tex
+++ b/chapters/theory/e1_chiral_algebras.tex
@@ -63,7 +63,7 @@
 via holomorphic Chern--Simons; conjectural in general).
 The further $E_3$-topological upgrade requires a conformal
 vector at non-critical level
-(Volume~I, Theorem~\textup{\ref*{thm:topologization}}).
+(Volume~I, the topologization theorem).
 \end{definition}
 
 The closed colour carries $E_2$ structure from
@@ -128,7 +128,7 @@
 
 \begin{remark}[Three bars, one functor]
 \label{rem:three-bars-vol3}
-The CY-to-chiral functor $\Phi$ of Chapter~\ref{ch:cy-chiral-functor} has three natural composites. $\Phi_{E_1}$ produces $B^{\mathrm{ord}}(A_C)$; this is the ordered bar sensed by the Yangian. $\mathrm{av} \circ \Phi_{E_1}$ produces $B^{\Sigma}(A_C)$; this is the symmetric bar sensed by the modular characteristic $\kappa_{\mathrm{ch}}$. The full $E_2$ enhancement $\Phi_{E_2}$ produces the Drinfeld-centered bar $B^{E_2}(A_C) = \cZ(B^{\mathrm{ord}}(A_C))$; this is the braided bar sensed by the quantum group. All three factor through $\Phi_{E_1}$. This is the volume's motto: the ordered bar is the primitive.
+The CY-to-chiral functor $\Phi$ of Chapter~\ref{ch:cy-to-chiral} has three natural composites. $\Phi_{E_1}$ produces $B^{\mathrm{ord}}(A_C)$; this is the ordered bar sensed by the Yangian. $\mathrm{av} \circ \Phi_{E_1}$ produces $B^{\Sigma}(A_C)$; this is the symmetric bar sensed by the modular characteristic $\kappa_{\mathrm{ch}}$. The full $E_2$ enhancement $\Phi_{E_2}$ produces the Drinfeld-centered bar $B^{E_2}(A_C) = \cZ(B^{\mathrm{ord}}(A_C))$; this is the braided bar sensed by the quantum group. All three factor through $\Phi_{E_1}$. This is the volume's motto: the ordered bar is the primitive.
 \end{remark}
 
 \section{$E_1$-chiral algebras from CY categories}
@@ -153,7 +153,7 @@
 Let $\cC$ be a CY$_3$ category with a chain-level $S^3$-framing on $\mathrm{HC}^-_3(\cC)$ (the condition of Conjecture~CY-A$_3$). Then the ordered bar complex of the cyclic $A_\infty$ algebra $A_\cC$ carries an $E_1$-chiral structure whose representation category is a braided monoidal refinement of the BPS Yangian of $\cC$.
 \end{conjecture}
 
-The conjecture is conditional on the chain-level framing; the unconditional statement requires the full CY-A$_3$ programme. Every downstream result in \ref{part:examples} and \ref{part:connections} that uses the BPS Yangian inherits this conditionality. The connection to Maulik-Okounkov and Costello-Witten cohomological Hall algebras is traced in Chapter~\ref{ch:cha-yangian}.
+The conjecture is conditional on the chain-level framing; the unconditional statement requires the full CY-A$_3$ programme. Every downstream result in \ref{part:examples} and \ref{part:connections} that uses the BPS Yangian inherits this conditionality. The connection to Maulik-Okounkov and Costello-Witten cohomological Hall algebras is traced in Chapter~\ref{ch:toric-coha}.
 
 \begin{proposition}[$E_2$ enhancement via Drinfeld center]
 \label{prop:e2-enhancement-drinfeld}
@@ -318,7 +318,7 @@
 
 \begin{remark}[How this chapter is used downstream]
 \label{rem:downstream-usage}
-Chapters~\ref{ch:braided-factorization}, \ref{ch:drinfeld-center}, and \ref{ch:quantum-group-reps} use this chapter as the source of the ordered bar coalgebra and the averaging map. Chapter~\ref{ch:cy-chiral-functor} uses Proposition~\ref{prop:e1-sector-d2} as the $d=2$ existence statement for $A_\cC$. Every braided monoidal category that appears later is the Drinfeld center of an underlying ordered one.
+Chapters~\ref{ch:braided-factorization}, \ref{ch:drinfeld-center}, and \ref{ch:quantum-group-reps} use this chapter as the source of the ordered bar coalgebra and the averaging map. Chapter~\ref{ch:cy-to-chiral} uses Proposition~\ref{prop:e1-sector-d2} as the $d=2$ existence statement for $A_\cC$. Every braided monoidal category that appears later is the Drinfeld center of an underlying ordered one.
 \end{remark}
 
 \section{Operadic dictionary for the CY reader}
@@ -1447,7 +1447,7 @@
 cutting the elliptic curve.}
 For the product CY$_3$ manifold $X = K3 \times E$, the factorization
 homology integral $\int_{K3} \cF|_{K3}$ of
-Section~\ref{sec:k3-perturbative-fact-homology} produces a chiral algebra
+Section~\ref{subsec:fact-homology-k3xe} produces a chiral algebra
 $A_E$ on the residual elliptic curve $E$.  The coproduct on $A_E$ arises
 from cutting $E$ into two intervals via excision.  Concretely, choose a
 collar-gluing decomposition $E = I_1 \cup_{S^0 \times \R} I_2$ (cutting
diff --git a/chapters/theory/e2_chiral_algebras.tex b/chapters/theory/e2_chiral_algebras.tex
index 4d9c49d33b9b71c9728719844b5387b9c256ec23..8a25a3037dc9569752a97c0fc75347a4033380af
--- a/chapters/theory/e2_chiral_algebras.tex
+++ b/chapters/theory/e2_chiral_algebras.tex
@@ -194,7 +194,7 @@
 \label{sec:drinfeld-center-bridge}
 
 Volume~II constructs $\Phi_{E_1}$ and proves $E_1$-chiral Koszul
-duality (see \ref{part:e1-core} of \cite{VolII}). The Drinfeld center
+duality (see Part~I of \cite{VolII}). The Drinfeld center
 $Z\colon E_1\text{-}\Cat \xrightarrow{\sim} E_2\text{-}\Cat$
 (under dualizability) is the categorical passage from ordered
 monoidal data to braided monoidal data. On the bar side it matches the
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 30392e44f20b6614f1f54981964db6c0329363e5..69d953d96d354add714abf2eec933a753336234a
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -201,7 +201,7 @@
 \]
 The SDR data $(i, p, s)$ interfaces directly with the homotopy transfer theorem (HTT), transferring the $A_\infty$-structure from \v{C}ech cochains $\check{C}^\bullet(\mathcal{E}nd(\mathcal{E}))$ to its cohomology $\mathrm{Ext}^\bullet(\mathcal{E}, \mathcal{E})$. The transferred operations $\mu_k^{\mathrm{ch}}$ are given by sums over planar trees whose internal edges are decorated by the homotopy~$s$; each application of~$s$ introduces rational functions on the affine intersections, and the resulting chiral operations are well-defined as formal power series.
 
-The scope is perturbative: the \v{C}ech homotopy produces an algebraic $A_\infty$-structure on the Ext algebra, but convergence of the resulting series to holomorphic functions (the non-perturbative statement) requires separate input from the analytic completion programme of Volume~I (MC5, \S\ref{sec:analytic-sewing}). The perturbative statement suffices for the formal CY-to-chiral functor and for all combinatorial applications in this volume. The full construction, including the proof that the SDR conditions hold and the scope qualification, is Theorem~\ref{thm:cech-contracting-homotopy} in Chapter~\ref{ch:cy-to-chiral}.
+The scope is perturbative: the \v{C}ech homotopy produces an algebraic $A_\infty$-structure on the Ext algebra, but convergence of the resulting series to holomorphic functions (the non-perturbative statement) requires separate input from the analytic completion programme of Volume~I (MC5, the analytic sewing section there). The perturbative statement suffices for the formal CY-to-chiral functor and for all combinatorial applications in this volume. The full construction, including the proof that the SDR conditions hold and the scope qualification, is Theorem~\ref{thm:cech-contracting-homotopy} in Chapter~\ref{ch:cy-to-chiral}.
 
 Three independent consistency checks confirm the resulting chiral data for the quintic: the Gepner model matrix factorization (via mirror symmetry, $\mathrm{MF}(x_1^5 + \cdots + x_5^5)$), the large-volume Hodge--Kodaira--Rosenberg limit ($\mathrm{HKR}$ degeneration of $\mathrm{Ext}^\bullet$ to Dolbeault cohomology), and the Gopakumar--Vafa integrality of the resulting genus-$g$ amplitudes. All three produce the same modular characteristic $\chi/2 = -100$ (the MacMahon-normalised form of $\kappa_{\mathrm{cat}}$ at $d=3$).
 
@@ -277,7 +277,7 @@
  \item The moonshine multiplier: $A_n = \kappa_{\mathrm{cat}} \cdot \dim(\rho_n)$ identifies the factor $2$ in $Z_{K3} = 2\,\phi_{0,1}$.
  \item The categorical $\Etwo$-obstruction for CY$_3$ (Proposition~\ref{prop:e1-obstruction-categorical}): Serre duality forces antisymmetry of the Euler form, universally obstructing $\Etwo$-enhancement without torus hypotheses.
  \item Quiver-chart gluing for toric CY$_3$ (Theorem~\ref{thm:toric-chart-gluing}): the global $\Eone$-chiral algebra is assembled as a homotopy colimit of McKay-chart CoHAs, with $E_2$ descent degeneration and Costello--Li comparison.
- \item The K3 double current algebra $\fg_{K3}$ (Definition~\ref{def:k3-double-current-algebra}): the finite-dimensional analogue of the DDCA in which $\bC[u,v]$ is replaced by $H^*(S,\bC)$ with the Mukai pairing.
+ \item The K3 double current algebra $\fg_{K3}$: the finite-dimensional analogue of the DDCA in which $\bC[u,v]$ is replaced by $H^*(S,\bC)$ with the Mukai pairing.
  \item Forty-two CY/BKM compute engines with $5{,}700{+}$ tests across the standard CY landscape.
 \end{itemize}
 
@@ -360,7 +360,7 @@
 \item \emph{Descent theorem.}
  \v{C}ech descent for $E_1$-algebras over the Bridgeland
  stability manifold. Proved for toric CY3
- (Proposition~\ref{prop:e1-descent-unobstructed}); open for
+ (Theorem~\ref{thm:toric-chart-gluing}); open for
  compact CY3 beyond the chart-atlas regime.
 \item \emph{Higher-dimensional CY shadows.}
  The $E_n$ stabilization theorem
@@ -394,12 +394,12 @@
 
 \emph{Quantum group representations} (Chapter~\ref{ch:quantum-group-reps}). The representation-theoretic target. The braided monoidal category $\mathrm{Rep}_q(\mathfrak{g})$ is what the CY programme aims to realize: Conjecture~CY-C predicts that $\mathrm{Rep}_q(\mathfrak{g}) \simeq \mathrm{Rep}^{E_2}(A_\cC)$ for a CY category $\cC(\mathfrak{g}, q)$. The Kazhdan--Lusztig equivalence $\mathrm{Rep}_q(\mathfrak{g}) \simeq \mathrm{KL}_k(\mathfrak{g})$ at roots of unity is the prototype: the Volume~I bar complex $B(V_k(\mathfrak{g}))$ encodes the quantum group $R$-matrix in its degree-$(1,1)$ component, and the DK bridge (Volume~II, MC3 for all simple types) recovers the quantum group categorical structure. The affine Yangian realization (Chapter~\ref{ch:toric-coha}) provides the $E_1$-sector; the Drinfeld center (Chapter~\ref{ch:drinfeld-center}) provides the $E_2$-enhancement.
 
-In addition to the four standard families, the toroidal and elliptic algebras chapter (Chapter~\ref{chap:toroidal-elliptic}) develops the $K3 \times E$ programme in full: the generalized root datum, the BKM superalgebra $\mathfrak{g}_{\Delta_5}$ with its Igusa cusp form denominator identity, the shadow--Siegel gap theorem, thirteen structural results (K3-1 through K3-13), all ten research programmes (A through J), and the DDCA--toroidal bridge identifying the deformed double current algebra as the rational degeneration of the quantum toroidal algebra (Conjecture~\ref{conj:ddca-toroidal-bridge}). The K3 double current algebra $\fg_{K3}$ (Chapter~\ref{ch:k3-times-e}, Definition~\ref{def:k3-double-current-algebra}) provides the K3 analogue of the DDCA, replacing $\bC[u,v]$ with $H^*(S,\bC)$. The toric CY$_3$ CoHA chapter (Chapter~\ref{ch:toric-coha}) develops the affine Yangian and $\mathcal{W}_{1+\infty}$ side: the Jordan quiver gives $Y(\widehat{\mathfrak{gl}}_1) \simeq \mathcal{W}_{1+\infty}$, the toric fan is the Dynkin data, and the shuffle algebra presentation connects to the KZ equations of Volume~I.
+In addition to the four standard families, the toroidal and elliptic algebras chapter (Chapter~\ref{chap:toroidal-elliptic}) develops the $K3 \times E$ programme in full: the generalized root datum, the BKM superalgebra $\mathfrak{g}_{\Delta_5}$ with its Igusa cusp form denominator identity, the shadow--Siegel gap theorem, thirteen structural results (K3-1 through K3-13), all ten research programmes (A through J), and the DDCA--toroidal bridge identifying the deformed double current algebra as the rational degeneration of the quantum toroidal algebra (Conjecture~\ref{conj:ddca-toroidal-bridge}). The K3 double current algebra $\fg_{K3}$, discussed in the DDCA--toroidal bridge of Chapter~\ref{ch:k3-times-e}, provides the K3 analogue of the DDCA, replacing $\bC[u,v]$ with $H^*(S,\bC)$. The toric CY$_3$ CoHA chapter (Chapter~\ref{ch:toric-coha}) develops the affine Yangian and $\mathcal{W}_{1+\infty}$ side: the Jordan quiver gives $Y(\widehat{\mathfrak{gl}}_1) \simeq \mathcal{W}_{1+\infty}$, the toric fan is the Dynkin data, and the shuffle algebra presentation connects to the KZ equations of Volume~I.
 
 \section{Guide for the reader}
 \label{sec:guide}
 
-Part~\ref{part:cy-categories} establishes the categorical foundations: CY categories, cyclic $\Ainf$-structures, the Hochschild calculus, and the $E_1$/$E_2$/$E_n$ chiral hierarchy with the framing obstruction tower. Part~\ref{part:bridge} constructs the bridge functor $\Phi$ from CY categories to quantum chiral algebras and proves Theorems CY-A (for $d = 2$) and CY-D, with the identification of automorphic correction and shadow obstruction tower as the central result. Part~\ref{part:examples} treats quantum groups and their braided factorization structure, including the Drinfeld center as the bulk algebra. Part~\ref{part:connections} works through the standard landscape: the toroidal and elliptic algebras chapter develops the $K3 \times E$ programme (K3-1 through K3-13, programmes A through J), alongside toric CY3 CoHAs, Fukaya categories, derived categories, matrix factorizations (ADE singularities and W-algebras), and quantum group representations (Kazhdan--Lusztig, affine Yangians, critical CoHAs). Part~\ref{part:frontier} connects to the geometric Langlands programme and to Volumes~I and~II via the bar-cobar bridge and the modular Koszul bridge. The working notes (\S\ref{sec:working-notes}) record the research frontier.
+Part~\ref{part:cy-categories} establishes the categorical foundations: CY categories, cyclic $\Ainf$-structures, the Hochschild calculus, and the $E_1$/$E_2$/$E_n$ chiral hierarchy with the framing obstruction tower. Part~\ref{part:bridge} constructs the bridge functor $\Phi$ from CY categories to quantum chiral algebras and proves Theorems CY-A (for $d = 2$) and CY-D, with the identification of automorphic correction and shadow obstruction tower as the central result. Part~\ref{part:examples} treats quantum groups and their braided factorization structure, including the Drinfeld center as the bulk algebra. Part~\ref{part:connections} works through the standard landscape: the toroidal and elliptic algebras chapter develops the $K3 \times E$ programme (K3-1 through K3-13, programmes A through J), alongside toric CY3 CoHAs, Fukaya categories, derived categories, matrix factorizations (ADE singularities and W-algebras), and quantum group representations (Kazhdan--Lusztig, affine Yangians, critical CoHAs). Part~\ref{part:frontier} connects to the geometric Langlands programme and to Volumes~I and~II via the bar-cobar bridge and the modular Koszul bridge. The separate working notes record the research frontier.
 
 \section{Conventions and notation}
 \label{sec:conventions-intro}

file update:
diff --git a/chapters/connections/cy_holographic_datum_master.tex b/chapters/connections/cy_holographic_datum_master.tex
index 2a66e8a0ca86f097e30b0de99c082498014430c6..b0ef34640300f22c24d57ee10a207c331065f31d
--- a/chapters/connections/cy_holographic_datum_master.tex
+++ b/chapters/connections/cy_holographic_datum_master.tex
@@ -943,7 +943,7 @@
 bar-cobar, CoHA / perverse coherent sheaves, classical CY Poisson
 coisson, MO stable envelope, affine super Yangian for toric CY$_3$,
 elliptic Sklyanin for toroidal CY, Gaudin from CY$_3$
-(Theorem~\ref{thm:cy-seven-face-master} above).
+(Conjecture~\ref{conj:cy-seven-face-master} above).
 \end{enumerate}
 The three master theorems are mutually compatible: under the CY-to-chiral
 functor $\Phi$, face~$i$ of Vol~III maps to a specialization of face~$i$
diff --git a/chapters/connections/modular_koszul_bridge.tex b/chapters/connections/modular_koszul_bridge.tex
index 1199c5aaa32e71f085dd3b7131c8f9aeadb1148c..a423d35b2ce162a9f56bb568768ae1bed7bef2f6
--- a/chapters/connections/modular_koszul_bridge.tex
+++ b/chapters/connections/modular_koszul_bridge.tex
@@ -234,7 +234,7 @@
 \end{theorem}
 
 \begin{proof}[Attribution]
-Parts (i), (iii), (iv) are Vol~I/II results (\S\ref{sec:k3e-cross-volume}, items K3-1 through K3-13, proved in the K3 modular-tower chapter of Vol~I and in the Vol~II 3D quantum gravity treatment, \ref{part:3d-qg} there). Part (ii) is the Borcherds lift of Borcherds (1998); its use as a modular characteristic is the observation of AP-CY8, not a theorem of Vol~III. The conditionality on propagates from Theorem~\ref{thm:cy-shadow-cohft}.
+Parts (i), (iii), (iv) are Vol~I/II results (\S\ref{sec:k3e-cross-volume}, items K3-1 through K3-13, proved in the K3 modular-tower chapter of Vol~I and in Part~III of Vol~II's 3D quantum gravity treatment). Part (ii) is the Borcherds lift of Borcherds (1998); its use as a modular characteristic is the observation of AP-CY8, not a theorem of Vol~III. The conditionality on propagates from Theorem~\ref{thm:cy-shadow-cohft}.
 \end{proof}
 
 \begin{remark}[Kappa-spectrum verification for $K3 \times E$]
diff --git a/chapters/examples/quantum_group_reps.tex b/chapters/examples/quantum_group_reps.tex
index e6b19a4c52de09f17af4b5f794d5f7269f4076b4..5213e6bfc9cb828c11c98b50aa32549aa228cfbf
--- a/chapters/examples/quantum_group_reps.tex
+++ b/chapters/examples/quantum_group_reps.tex
@@ -503,7 +503,7 @@
  additional data);
  \item $\kappa_{\mathrm{BKM}}$: the BKM modular weight, a
  number-theoretic invariant arising from the BKM denominator
- formula (Chapter~\ref{ch:toroidal-elliptic}; distinct from
+ formula (Chapter~\ref{chap:toroidal-elliptic}; distinct from
  both $\kappa_{\mathrm{cat}}$ and $\kappa_{\mathrm{ch}}$).
 \end{enumerate}
 For CY$_2$ categories with $\frakg$-symmetry, all three can be
diff --git a/chapters/examples/toric_cy3_coha.tex b/chapters/examples/toric_cy3_coha.tex
index 2b8821c0fd545c77e9d18a4180e8e67d3c4459be..94da66b26dadb3a8dcd2e91287fd7092ea5a944c
--- a/chapters/examples/toric_cy3_coha.tex
+++ b/chapters/examples/toric_cy3_coha.tex
@@ -205,7 +205,7 @@
 \end{theorem}
 
 \begin{proof}
-(i) The compact base $\bP^1 \times \bP^1$ has $\chi(\bP^1 \times \bP^1) = 4$ (each factor contributes $\chi(\bP^1) = 2$), so $\kappa_{\mathrm{ch}} = \chi/2 = 2$ by the general local-surface formula (Remark~\ref{rem:toric-structural-patterns}).
+(i) The compact base $\bP^1 \times \bP^1$ has $\chi(\bP^1 \times \bP^1) = 4$ (each factor contributes $\chi(\bP^1) = 2$), so $\kappa_{\mathrm{ch}} = \chi/2 = 2$ by the general local-surface formula (Remark~\ref{rem:toric-kappa-patterns}).
 
 (ii) The intersection form on $H^2(\bP^1 \times \bP^1)$ in the basis $\{e_1, e_2\}$ is $\langle e_i, e_j \rangle = \delta_{ij}$ (the two rulings are orthogonal with self-intersection $0$ in the total space, but the relevant inner product for the shadow metric is the Euler pairing $\chi(e_i, e_j) = \delta_{ij}$).
 
@@ -654,7 +654,7 @@
 the chart gluing by descent, the shadow tower by the MC equation.
 These components are \emph{a priori} separate structures on the
 same algebra. The Vol~I chiral quantum group equivalence
-(Theorem~\ref{thm:chiral-qg-equiv}) asserts that three of them
+asserts that three of them
 (the vertex $R$-matrix, the chiral $A_\infty$-structure, and the
 chiral coproduct) determine each other on the Koszul locus. The theorem
 below specializes the abstract equivalence to the toric CY3 setting,
@@ -746,8 +746,7 @@
 
 \begin{proof}
 The abstract equivalence (I) $\leftrightarrow$ (II)
-$\leftrightarrow$ (III) is
-Theorem~\ref{thm:chiral-qg-equiv} of Vol~I, proved for any
+$\leftrightarrow$ (III) is the Vol~I chiral quantum group equivalence, proved for any
 $\Eone$-chiral algebra on the Koszul locus. The content of the
 present theorem is the identification of each abstract vertex
 with the independently constructed toric CY3 structure.
@@ -755,7 +754,7 @@
 \textit{Component~\textup{(I)}: $R$-matrix.}
 The $\Eone$-chiral algebra $A_X$ carries a vertex
 $R$-matrix by the general theory
-(Theorem~\ref{thm:chiral-qg-equiv}(I)). For toric CY3, the
+(item~\textup{(I)} of that equivalence). For toric CY3, the
 Maulik--Okounkov stable-envelope construction provides an
 independent $R$-matrix on $Y^+(\widehat{\fg}_{Q_X})$-modules.
 The two coincide because both solve the same Yang--Baxter
diff --git a/chapters/examples/toroidal_elliptic.tex b/chapters/examples/toroidal_elliptic.tex
index 8fcef3a49b8fe0bd45c3ae248676e994ece0ca7e..0a15b2c062f601ea29e50e3e3771b3eb1544db50
--- a/chapters/examples/toroidal_elliptic.tex
+++ b/chapters/examples/toroidal_elliptic.tex
@@ -5940,8 +5940,7 @@
 
 The K3 analogue of this picture replaces $\bC^2$ by a K3
 surface~$S$: the K3 double current algebra $\fg_{K3}$
-(Chapter~\ref{ch:k3-times-e},
-Definition~\ref{def:k3-double-current-algebra}) substitutes
+substitutes
 $H^*(S,\bC)$ for $\bC[u,v]$ and the Mukai pairing for the
 polynomial residue. Its quantization should produce a
 ``K3 Yangian'' standing in the same relation to $\fg_{K3}$ as the
@@ -6018,7 +6017,7 @@
   At $t \to 1$: the second parameter $w$ decouples and
   $\Delta_{z,w}$ reduces to the single-parameter
   Drinfeld coproduct $\Delta_z(T(u)) = T(u) \otimes T(u - z)$
-  of Theorem~\textup{\ref{thm:w-infty-chiral-qg}}.
+  of Proposition~\textup{\ref{prop:universal-coproduct}}.
 \end{enumerate}
 No two-parameter coproduct $\Delta_{z,w}$ currently exists in
 the literature or in this programme's compute infrastructure.
@@ -6034,7 +6033,7 @@
   $(q_1,q_2,q_3)$.
 \item Promote the DDCA shadow to an explicit $\Delta_{z,w}$
   formula aligned with the $R(u,v)$ surface in
-  \S\ref{subsec:quantum-chiral-algebras-6d}.
+  \S\ref{subsec:chiral-qg-wilson}.
 \item Build a compute witness at low modes: $w = 0$ reduces
   to existing $\Delta_z$; rational limit gives the DDCA
   shift; Miki sends $\Delta_{z,w} \to \Delta_{w,z}$.
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index ddbdfe60d9c9df04ba6f3acf48deee73523a64dc..3ce4e679084f2f25672104c7a00684df5e9f3b26
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -320,7 +320,7 @@
 Drinfeld coproduct from spin~$2$ to arbitrary spin, with the
 universal Miura coefficient $(\Psi{-}1)/\Psi$ on the leading
 cross-term $J \otimes W_{s-1}$ at every spin $s \ge 2$
-(Theorem~\ref{thm:miura-cross-universality}).
+(Proposition~\ref{prop:universal-coproduct}).
 
 \bigskip
 
@@ -328,7 +328,7 @@
 Volume~I defines $E_1$-chiral quantum groups abstractly. This
 volume constructs them concretely from CY geometry. The
 $E_1$-chiral bialgebra axioms (formalized in
-\S\ref{sec:e1-chiral-bialgebra}) require: (H1)~an $E_1$-chiral
+\S\ref{sec:e1-chiral-bialgebras}) require: (H1)~an $E_1$-chiral
 algebra $A$ on a curve $X$; (H2)~a spectral coproduct
 $\Delta_z \colon A \to A \otimes A$ (living on the OPEN/$E_1$
 colour); (H3)~an $R$-matrix $R(z)$ satisfying YBE; (H4)~RTT
diff --git a/chapters/theory/cy_categories.tex b/chapters/theory/cy_categories.tex
index f9b51871c44fa18a574c02fce8aaa49a49aa9c61..00d723a1cb5d4f2355a10cb2d9d3f86688259f09
--- a/chapters/theory/cy_categories.tex
+++ b/chapters/theory/cy_categories.tex
@@ -166,7 +166,7 @@
 Every smooth proper CY$_d$ category admits a cyclic $\Ainf$-enhancement, unique up to $\Ainf$-quasi-isomorphism preserving the pairing. The proof is due to Kontsevich--Soibelman in the formal case, Costello~\cite{Costello2005} for the TCFT enhancement, and Seidel~\cite{Seidel2008} for the Fukaya case.
 \end{theorem}
 
-At $d = 2$ the enhancement is explicit enough to compute directly; it drives the $K3$ computations feeding the Borcherds denominator (Vol~III Chapter~\ref{ch:k3}). At $d = 3$ the enhancement was constructed by Sheridan~\cite{Sheridan2015} for the quintic threefold, as part of the HMS proof; the general $d = 3$ construction remains programme-level (conditional on $\bS^3$-framing, see AP-CY6).
+At $d = 2$ the enhancement is explicit enough to compute directly; it drives the $K3$ computations feeding the Borcherds denominator (Vol~III Chapter~\ref{ch:k3-times-e}). At $d = 3$ the enhancement was constructed by Sheridan~\cite{Sheridan2015} for the quintic threefold, as part of the HMS proof; the general $d = 3$ construction remains programme-level (conditional on $\bS^3$-framing, see AP-CY6).
 
 \section{Interface with the CY-to-chiral functor $\Phi$}
 \label{sec:cy-cat-phi-interface}
@@ -194,7 +194,7 @@
 
 \begin{remark}[What $\Phi$ does not see]
 \label{rem:phi-does-not-see}
-Not every invariant of $\cC$ survives the passage through $\Phi$. The functor retains the cyclic $\Ainf$-structure and the Gerstenhaber bracket; it loses the fine structure of the triangulated / $\Ainf$ category (individual objects, t-structures, stability conditions) that is visible only via the fuller categorical CoHA construction of Chapter~\ref{ch:coha}. The kappa-spectrum (Vol~III CLAUDE.md) encodes which invariants survive: $\kappa_\mathrm{cat}$ is always present, $\kappa_\mathrm{ch}$ exists only when $\Phi$ is defined, and $\kappa_\mathrm{BKM}$ records the Borcherds-side lift for $K3 \times E$.
+Not every invariant of $\cC$ survives the passage through $\Phi$. The functor retains the cyclic $\Ainf$-structure and the Gerstenhaber bracket; it loses the fine structure of the triangulated / $\Ainf$ category (individual objects, t-structures, stability conditions) that is visible only via the fuller categorical CoHA construction of Chapter~\ref{ch:toric-coha}. The kappa-spectrum (Vol~III CLAUDE.md) encodes which invariants survive: $\kappa_\mathrm{cat}$ is always present, $\kappa_\mathrm{ch}$ exists only when $\Phi$ is defined, and $\kappa_\mathrm{BKM}$ records the Borcherds-side lift for $K3 \times E$.
 \end{remark}
 
 \begin{remark}[Cross-volume conventions]
diff --git a/chapters/theory/cy_to_chiral.tex b/chapters/theory/cy_to_chiral.tex
index 030fed4a9a2a7009ae05fdb0f3c431c8aed1fc83..14526e0aba63169841056220749304799a57fe10
--- a/chapters/theory/cy_to_chiral.tex
+++ b/chapters/theory/cy_to_chiral.tex
@@ -618,8 +618,8 @@
 homotopy is purely algebraic: it acts by
 $s(f_{i_0 \cdots i_q}) = f_{0 i_0 \cdots i_q}$ on \v{C}ech cochains and
 involves no PDE solving. The SDR data $(i, p, s)$ interfaces directly
-with the homotopy transfer theorem
-\textup{(}HTT, Theorem~\textup{\ref{thm:htt-general}}\textup{)},
+with the standard homotopy transfer theorem
+\textup{(}HTT\textup{)},
 transferring the $\Ainf$-structure from $\check{C}^\bullet(\cE nd(\cE))$
 to its cohomology $\Ext^\bullet(\cE, \cE)$.
 \end{theorem}
@@ -652,7 +652,7 @@
 (whether the formal series in the OPE coefficients converges to
 define honest holomorphic functions) requires separate input from
 the analytic completion programme (MC5,
-\S\ref{sec:analytic-sewing} of Vol~I). Specifically: the HTT
+the analytic sewing section of Vol~I). Specifically: the HTT
 produces transferred operations $\mu_k^{\mathrm{ch}}$ whose
 coefficients involve iterated applications of~$s$; each application
 introduces rational functions on the intersections $U_{i_0} \cap
@@ -1972,7 +1972,7 @@
  \bottomrule
 \end{tabular}
 \end{center}
-{\footnotesize $^*$The K3 entry records $\kappa_{\mathrm{ch}} = \chi(\cO_{\mathrm{K3}}) = 2$ (Proposition~\ref{prop:cy-kappa-d2}; verified via chiral de Rham, Chapter~\ref{ch:k3-times-e}). The distinct quantity $\dim \HH_*(D^b(\mathrm{K3}))/2 = 12$ arises from an alternative algebraization (the Monster orbifold); the full trichotomy ($\kappa_{\mathrm{ch}} \in \{2, 12, 24\}$) is developed in Section~\ref{subsec:k3-three-algebraizations} of Chapter~\ref{ch:k3-times-e}.
+{\footnotesize $^*$The K3 entry records $\kappa_{\mathrm{ch}} = \chi(\cO_{\mathrm{K3}}) = 2$ (Proposition~\ref{prop:cy-kappa-d2}; verified via chiral de Rham, Chapter~\ref{ch:k3-times-e}). The distinct quantity $\dim \HH_*(D^b(\mathrm{K3}))/2 = 12$ arises from an alternative algebraization (the Monster orbifold); the full trichotomy ($\kappa_{\mathrm{ch}} \in \{2, 12, 24\}$) is developed in the K3 discussion of Chapter~\ref{ch:k3-times-e}.
 
 $^\dagger$The $K3 \times E$ entry records $\kappa_{\mathrm{ch}} = 3$ by additivity (Proposition~\ref{prop:categorical-euler}: $\kappa_{\mathrm{ch}}(\mathrm{K3}) + \kappa_{\mathrm{ch}}(E) = 2 + 1$). The Borcherds automorphic weight is $\kappa_{\mathrm{BKM}} = 5 = \mathrm{wt}(\Delta_5)$, a distinct invariant.}
 
diff --git a/chapters/theory/drinfeld_center.tex b/chapters/theory/drinfeld_center.tex
index ac67d4e3a2ed8fab94fcb3fc63933d8650a92ac9..a711d853438f9e6a0e6fdd4e5dac61154b7b3c24
--- a/chapters/theory/drinfeld_center.tex
+++ b/chapters/theory/drinfeld_center.tex
@@ -726,7 +726,7 @@
 produces only symmetric braiding. The distinction is the
 deep reason for the $\Eone$ stabilization theorem
 (Chapter~\ref{ch:cy-to-chiral},
-Theorem~\ref{thm:e1-stabilization}).
+Theorem~\ref{thm:e1-stabilization-cy}).
 
 \begin{proposition}[$E_3$ restriction gives symmetric braiding]
 \label{prop:e3-symmetric-braiding}
diff --git a/chapters/theory/e1_chiral_algebras.tex b/chapters/theory/e1_chiral_algebras.tex
index 75484d2fff759dc21313b5595a8abade7d55d203..b533b2f5640db9eba4046a61106787f2c19a0d53
--- a/chapters/theory/e1_chiral_algebras.tex
+++ b/chapters/theory/e1_chiral_algebras.tex
@@ -63,7 +63,7 @@
 via holomorphic Chern--Simons; conjectural in general).
 The further $E_3$-topological upgrade requires a conformal
 vector at non-critical level
-(Volume~I, Theorem~\textup{\ref*{thm:topologization}}).
+(Volume~I, the topologization theorem).
 \end{definition}
 
 The closed colour carries $E_2$ structure from
@@ -128,7 +128,7 @@
 
 \begin{remark}[Three bars, one functor]
 \label{rem:three-bars-vol3}
-The CY-to-chiral functor $\Phi$ of Chapter~\ref{ch:cy-chiral-functor} has three natural composites. $\Phi_{E_1}$ produces $B^{\mathrm{ord}}(A_C)$; this is the ordered bar sensed by the Yangian. $\mathrm{av} \circ \Phi_{E_1}$ produces $B^{\Sigma}(A_C)$; this is the symmetric bar sensed by the modular characteristic $\kappa_{\mathrm{ch}}$. The full $E_2$ enhancement $\Phi_{E_2}$ produces the Drinfeld-centered bar $B^{E_2}(A_C) = \cZ(B^{\mathrm{ord}}(A_C))$; this is the braided bar sensed by the quantum group. All three factor through $\Phi_{E_1}$. This is the volume's motto: the ordered bar is the primitive.
+The CY-to-chiral functor $\Phi$ of Chapter~\ref{ch:cy-to-chiral} has three natural composites. $\Phi_{E_1}$ produces $B^{\mathrm{ord}}(A_C)$; this is the ordered bar sensed by the Yangian. $\mathrm{av} \circ \Phi_{E_1}$ produces $B^{\Sigma}(A_C)$; this is the symmetric bar sensed by the modular characteristic $\kappa_{\mathrm{ch}}$. The full $E_2$ enhancement $\Phi_{E_2}$ produces the Drinfeld-centered bar $B^{E_2}(A_C) = \cZ(B^{\mathrm{ord}}(A_C))$; this is the braided bar sensed by the quantum group. All three factor through $\Phi_{E_1}$. This is the volume's motto: the ordered bar is the primitive.
 \end{remark}
 
 \section{$E_1$-chiral algebras from CY categories}
@@ -153,7 +153,7 @@
 Let $\cC$ be a CY$_3$ category with a chain-level $S^3$-framing on $\mathrm{HC}^-_3(\cC)$ (the condition of Conjecture~CY-A$_3$). Then the ordered bar complex of the cyclic $A_\infty$ algebra $A_\cC$ carries an $E_1$-chiral structure whose representation category is a braided monoidal refinement of the BPS Yangian of $\cC$.
 \end{conjecture}
 
-The conjecture is conditional on the chain-level framing; the unconditional statement requires the full CY-A$_3$ programme. Every downstream result in \ref{part:examples} and \ref{part:connections} that uses the BPS Yangian inherits this conditionality. The connection to Maulik-Okounkov and Costello-Witten cohomological Hall algebras is traced in Chapter~\ref{ch:cha-yangian}.
+The conjecture is conditional on the chain-level framing; the unconditional statement requires the full CY-A$_3$ programme. Every downstream result in \ref{part:examples} and \ref{part:connections} that uses the BPS Yangian inherits this conditionality. The connection to Maulik-Okounkov and Costello-Witten cohomological Hall algebras is traced in Chapter~\ref{ch:toric-coha}.
 
 \begin{proposition}[$E_2$ enhancement via Drinfeld center]
 \label{prop:e2-enhancement-drinfeld}
@@ -318,7 +318,7 @@
 
 \begin{remark}[How this chapter is used downstream]
 \label{rem:downstream-usage}
-Chapters~\ref{ch:braided-factorization}, \ref{ch:drinfeld-center}, and \ref{ch:quantum-group-reps} use this chapter as the source of the ordered bar coalgebra and the averaging map. Chapter~\ref{ch:cy-chiral-functor} uses Proposition~\ref{prop:e1-sector-d2} as the $d=2$ existence statement for $A_\cC$. Every braided monoidal category that appears later is the Drinfeld center of an underlying ordered one.
+Chapters~\ref{ch:braided-factorization}, \ref{ch:drinfeld-center}, and \ref{ch:quantum-group-reps} use this chapter as the source of the ordered bar coalgebra and the averaging map. Chapter~\ref{ch:cy-to-chiral} uses Proposition~\ref{prop:e1-sector-d2} as the $d=2$ existence statement for $A_\cC$. Every braided monoidal category that appears later is the Drinfeld center of an underlying ordered one.
 \end{remark}
 
 \section{Operadic dictionary for the CY reader}
@@ -1447,7 +1447,7 @@
 cutting the elliptic curve.}
 For the product CY$_3$ manifold $X = K3 \times E$, the factorization
 homology integral $\int_{K3} \cF|_{K3}$ of
-Section~\ref{sec:k3-perturbative-fact-homology} produces a chiral algebra
+Section~\ref{subsec:fact-homology-k3xe} produces a chiral algebra
 $A_E$ on the residual elliptic curve $E$.  The coproduct on $A_E$ arises
 from cutting $E$ into two intervals via excision.  Concretely, choose a
 collar-gluing decomposition $E = I_1 \cup_{S^0 \times \R} I_2$ (cutting
diff --git a/chapters/theory/e2_chiral_algebras.tex b/chapters/theory/e2_chiral_algebras.tex
index 4d9c49d33b9b71c9728719844b5387b9c256ec23..8a25a3037dc9569752a97c0fc75347a4033380af
--- a/chapters/theory/e2_chiral_algebras.tex
+++ b/chapters/theory/e2_chiral_algebras.tex
@@ -194,7 +194,7 @@
 \label{sec:drinfeld-center-bridge}
 
 Volume~II constructs $\Phi_{E_1}$ and proves $E_1$-chiral Koszul
-duality (see \ref{part:e1-core} of \cite{VolII}). The Drinfeld center
+duality (see Part~I of \cite{VolII}). The Drinfeld center
 $Z\colon E_1\text{-}\Cat \xrightarrow{\sim} E_2\text{-}\Cat$
 (under dualizability) is the categorical passage from ordered
 monoidal data to braided monoidal data. On the bar side it matches the
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 30392e44f20b6614f1f54981964db6c0329363e5..69d953d96d354add714abf2eec933a753336234a
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -201,7 +201,7 @@
 \]
 The SDR data $(i, p, s)$ interfaces directly with the homotopy transfer theorem (HTT), transferring the $A_\infty$-structure from \v{C}ech cochains $\check{C}^\bullet(\mathcal{E}nd(\mathcal{E}))$ to its cohomology $\mathrm{Ext}^\bullet(\mathcal{E}, \mathcal{E})$. The transferred operations $\mu_k^{\mathrm{ch}}$ are given by sums over planar trees whose internal edges are decorated by the homotopy~$s$; each application of~$s$ introduces rational functions on the affine intersections, and the resulting chiral operations are well-defined as formal power series.
 
-The scope is perturbative: the \v{C}ech homotopy produces an algebraic $A_\infty$-structure on the Ext algebra, but convergence of the resulting series to holomorphic functions (the non-perturbative statement) requires separate input from the analytic completion programme of Volume~I (MC5, \S\ref{sec:analytic-sewing}). The perturbative statement suffices for the formal CY-to-chiral functor and for all combinatorial applications in this volume. The full construction, including the proof that the SDR conditions hold and the scope qualification, is Theorem~\ref{thm:cech-contracting-homotopy} in Chapter~\ref{ch:cy-to-chiral}.
+The scope is perturbative: the \v{C}ech homotopy produces an algebraic $A_\infty$-structure on the Ext algebra, but convergence of the resulting series to holomorphic functions (the non-perturbative statement) requires separate input from the analytic completion programme of Volume~I (MC5, the analytic sewing section there). The perturbative statement suffices for the formal CY-to-chiral functor and for all combinatorial applications in this volume. The full construction, including the proof that the SDR conditions hold and the scope qualification, is Theorem~\ref{thm:cech-contracting-homotopy} in Chapter~\ref{ch:cy-to-chiral}.
 
 Three independent consistency checks confirm the resulting chiral data for the quintic: the Gepner model matrix factorization (via mirror symmetry, $\mathrm{MF}(x_1^5 + \cdots + x_5^5)$), the large-volume Hodge--Kodaira--Rosenberg limit ($\mathrm{HKR}$ degeneration of $\mathrm{Ext}^\bullet$ to Dolbeault cohomology), and the Gopakumar--Vafa integrality of the resulting genus-$g$ amplitudes. All three produce the same modular characteristic $\chi/2 = -100$ (the MacMahon-normalised form of $\kappa_{\mathrm{cat}}$ at $d=3$).
 
@@ -277,7 +277,7 @@
  \item The moonshine multiplier: $A_n = \kappa_{\mathrm{cat}} \cdot \dim(\rho_n)$ identifies the factor $2$ in $Z_{K3} = 2\,\phi_{0,1}$.
  \item The categorical $\Etwo$-obstruction for CY$_3$ (Proposition~\ref{prop:e1-obstruction-categorical}): Serre duality forces antisymmetry of the Euler form, universally obstructing $\Etwo$-enhancement without torus hypotheses.
  \item Quiver-chart gluing for toric CY$_3$ (Theorem~\ref{thm:toric-chart-gluing}): the global $\Eone$-chiral algebra is assembled as a homotopy colimit of McKay-chart CoHAs, with $E_2$ descent degeneration and Costello--Li comparison.
- \item The K3 double current algebra $\fg_{K3}$ (Definition~\ref{def:k3-double-current-algebra}): the finite-dimensional analogue of the DDCA in which $\bC[u,v]$ is replaced by $H^*(S,\bC)$ with the Mukai pairing.
+ \item The K3 double current algebra $\fg_{K3}$: the finite-dimensional analogue of the DDCA in which $\bC[u,v]$ is replaced by $H^*(S,\bC)$ with the Mukai pairing.
  \item Forty-two CY/BKM compute engines with $5{,}700{+}$ tests across the standard CY landscape.
 \end{itemize}
 
@@ -360,7 +360,7 @@
 \item \emph{Descent theorem.}
  \v{C}ech descent for $E_1$-algebras over the Bridgeland
  stability manifold. Proved for toric CY3
- (Proposition~\ref{prop:e1-descent-unobstructed}); open for
+ (Theorem~\ref{thm:toric-chart-gluing}); open for
  compact CY3 beyond the chart-atlas regime.
 \item \emph{Higher-dimensional CY shadows.}
  The $E_n$ stabilization theorem
@@ -394,12 +394,12 @@
 
 \emph{Quantum group representations} (Chapter~\ref{ch:quantum-group-reps}). The representation-theoretic target. The braided monoidal category $\mathrm{Rep}_q(\mathfrak{g})$ is what the CY programme aims to realize: Conjecture~CY-C predicts that $\mathrm{Rep}_q(\mathfrak{g}) \simeq \mathrm{Rep}^{E_2}(A_\cC)$ for a CY category $\cC(\mathfrak{g}, q)$. The Kazhdan--Lusztig equivalence $\mathrm{Rep}_q(\mathfrak{g}) \simeq \mathrm{KL}_k(\mathfrak{g})$ at roots of unity is the prototype: the Volume~I bar complex $B(V_k(\mathfrak{g}))$ encodes the quantum group $R$-matrix in its degree-$(1,1)$ component, and the DK bridge (Volume~II, MC3 for all simple types) recovers the quantum group categorical structure. The affine Yangian realization (Chapter~\ref{ch:toric-coha}) provides the $E_1$-sector; the Drinfeld center (Chapter~\ref{ch:drinfeld-center}) provides the $E_2$-enhancement.
 
-In addition to the four standard families, the toroidal and elliptic algebras chapter (Chapter~\ref{chap:toroidal-elliptic}) develops the $K3 \times E$ programme in full: the generalized root datum, the BKM superalgebra $\mathfrak{g}_{\Delta_5}$ with its Igusa cusp form denominator identity, the shadow--Siegel gap theorem, thirteen structural results (K3-1 through K3-13), all ten research programmes (A through J), and the DDCA--toroidal bridge identifying the deformed double current algebra as the rational degeneration of the quantum toroidal algebra (Conjecture~\ref{conj:ddca-toroidal-bridge}). The K3 double current algebra $\fg_{K3}$ (Chapter~\ref{ch:k3-times-e}, Definition~\ref{def:k3-double-current-algebra}) provides the K3 analogue of the DDCA, replacing $\bC[u,v]$ with $H^*(S,\bC)$. The toric CY$_3$ CoHA chapter (Chapter~\ref{ch:toric-coha}) develops the affine Yangian and $\mathcal{W}_{1+\infty}$ side: the Jordan quiver gives $Y(\widehat{\mathfrak{gl}}_1) \simeq \mathcal{W}_{1+\infty}$, the toric fan is the Dynkin data, and the shuffle algebra presentation connects to the KZ equations of Volume~I.
+In addition to the four standard families, the toroidal and elliptic algebras chapter (Chapter~\ref{chap:toroidal-elliptic}) develops the $K3 \times E$ programme in full: the generalized root datum, the BKM superalgebra $\mathfrak{g}_{\Delta_5}$ with its Igusa cusp form denominator identity, the shadow--Siegel gap theorem, thirteen structural results (K3-1 through K3-13), all ten research programmes (A through J), and the DDCA--toroidal bridge identifying the deformed double current algebra as the rational degeneration of the quantum toroidal algebra (Conjecture~\ref{conj:ddca-toroidal-bridge}). The K3 double current algebra $\fg_{K3}$, discussed in the DDCA--toroidal bridge of Chapter~\ref{ch:k3-times-e}, provides the K3 analogue of the DDCA, replacing $\bC[u,v]$ with $H^*(S,\bC)$. The toric CY$_3$ CoHA chapter (Chapter~\ref{ch:toric-coha}) develops the affine Yangian and $\mathcal{W}_{1+\infty}$ side: the Jordan quiver gives $Y(\widehat{\mathfrak{gl}}_1) \simeq \mathcal{W}_{1+\infty}$, the toric fan is the Dynkin data, and the shuffle algebra presentation connects to the KZ equations of Volume~I.
 
 \section{Guide for the reader}
 \label{sec:guide}
 
-Part~\ref{part:cy-categories} establishes the categorical foundations: CY categories, cyclic $\Ainf$-structures, the Hochschild calculus, and the $E_1$/$E_2$/$E_n$ chiral hierarchy with the framing obstruction tower. Part~\ref{part:bridge} constructs the bridge functor $\Phi$ from CY categories to quantum chiral algebras and proves Theorems CY-A (for $d = 2$) and CY-D, with the identification of automorphic correction and shadow obstruction tower as the central result. Part~\ref{part:examples} treats quantum groups and their braided factorization structure, including the Drinfeld center as the bulk algebra. Part~\ref{part:connections} works through the standard landscape: the toroidal and elliptic algebras chapter develops the $K3 \times E$ programme (K3-1 through K3-13, programmes A through J), alongside toric CY3 CoHAs, Fukaya categories, derived categories, matrix factorizations (ADE singularities and W-algebras), and quantum group representations (Kazhdan--Lusztig, affine Yangians, critical CoHAs). Part~\ref{part:frontier} connects to the geometric Langlands programme and to Volumes~I and~II via the bar-cobar bridge and the modular Koszul bridge. The working notes (\S\ref{sec:working-notes}) record the research frontier.
+Part~\ref{part:cy-categories} establishes the categorical foundations: CY categories, cyclic $\Ainf$-structures, the Hochschild calculus, and the $E_1$/$E_2$/$E_n$ chiral hierarchy with the framing obstruction tower. Part~\ref{part:bridge} constructs the bridge functor $\Phi$ from CY categories to quantum chiral algebras and proves Theorems CY-A (for $d = 2$) and CY-D, with the identification of automorphic correction and shadow obstruction tower as the central result. Part~\ref{part:examples} treats quantum groups and their braided factorization structure, including the Drinfeld center as the bulk algebra. Part~\ref{part:connections} works through the standard landscape: the toroidal and elliptic algebras chapter develops the $K3 \times E$ programme (K3-1 through K3-13, programmes A through J), alongside toric CY3 CoHAs, Fukaya categories, derived categories, matrix factorizations (ADE singularities and W-algebras), and quantum group representations (Kazhdan--Lusztig, affine Yangians, critical CoHAs). Part~\ref{part:frontier} connects to the geometric Langlands programme and to Volumes~I and~II via the bar-cobar bridge and the modular Koszul bridge. The separate working notes record the research frontier.
 
 \section{Conventions and notation}
 \label{sec:conventions-intro}

 succeeded in 22.73s:
  -- Fast build (up to 4 passes) --
Building main.tex (up to 4 passes)
-- Pass 1 / 4 --
  Pass 1: 0 errors, 0 undef refs, 6 undef cites, 0 rerun warnings
-- Pass 2 / 4 --
  Pass 2: 0 errors, 0 undef refs, 6 undef cites, 0 rerun warnings
-- Pass 3 / 4 --
  Pass 3: 0 errors, 0 undef refs, 6 undef cites, 0 rerun warnings
-- Pass 4 / 4 --
  Pass 4: 0 errors, 0 undef refs, 6 undef cites, 0 rerun warnings
  main.pdf built successfully.
     Logs: .build_logs/tex-build.stdout.log and main.log
file update:
diff --git a/chapters/connections/cy_holographic_datum_master.tex b/chapters/connections/cy_holographic_datum_master.tex
index 2a66e8a0ca86f097e30b0de99c082498014430c6..b0ef34640300f22c24d57ee10a207c331065f31d
--- a/chapters/connections/cy_holographic_datum_master.tex
+++ b/chapters/connections/cy_holographic_datum_master.tex
@@ -943,7 +943,7 @@
 bar-cobar, CoHA / perverse coherent sheaves, classical CY Poisson
 coisson, MO stable envelope, affine super Yangian for toric CY$_3$,
 elliptic Sklyanin for toroidal CY, Gaudin from CY$_3$
-(Theorem~\ref{thm:cy-seven-face-master} above).
+(Conjecture~\ref{conj:cy-seven-face-master} above).
 \end{enumerate}
 The three master theorems are mutually compatible: under the CY-to-chiral
 functor $\Phi$, face~$i$ of Vol~III maps to a specialization of face~$i$
diff --git a/chapters/connections/modular_koszul_bridge.tex b/chapters/connections/modular_koszul_bridge.tex
index 1199c5aaa32e71f085dd3b7131c8f9aeadb1148c..a423d35b2ce162a9f56bb568768ae1bed7bef2f6
--- a/chapters/connections/modular_koszul_bridge.tex
+++ b/chapters/connections/modular_koszul_bridge.tex
@@ -234,7 +234,7 @@
 \end{theorem}
 
 \begin{proof}[Attribution]
-Parts (i), (iii), (iv) are Vol~I/II results (\S\ref{sec:k3e-cross-volume}, items K3-1 through K3-13, proved in the K3 modular-tower chapter of Vol~I and in the Vol~II 3D quantum gravity treatment, \ref{part:3d-qg} there). Part (ii) is the Borcherds lift of Borcherds (1998); its use as a modular characteristic is the observation of AP-CY8, not a theorem of Vol~III. The conditionality on propagates from Theorem~\ref{thm:cy-shadow-cohft}.
+Parts (i), (iii), (iv) are Vol~I/II results (\S\ref{sec:k3e-cross-volume}, items K3-1 through K3-13, proved in the K3 modular-tower chapter of Vol~I and in Part~III of Vol~II's 3D quantum gravity treatment). Part (ii) is the Borcherds lift of Borcherds (1998); its use as a modular characteristic is the observation of AP-CY8, not a theorem of Vol~III. The conditionality on propagates from Theorem~\ref{thm:cy-shadow-cohft}.
 \end{proof}
 
 \begin{remark}[Kappa-spectrum verification for $K3 \times E$]
diff --git a/chapters/examples/quantum_group_reps.tex b/chapters/examples/quantum_group_reps.tex
index e6b19a4c52de09f17af4b5f794d5f7269f4076b4..5213e6bfc9cb828c11c98b50aa32549aa228cfbf
--- a/chapters/examples/quantum_group_reps.tex
+++ b/chapters/examples/quantum_group_reps.tex
@@ -503,7 +503,7 @@
  additional data);
  \item $\kappa_{\mathrm{BKM}}$: the BKM modular weight, a
  number-theoretic invariant arising from the BKM denominator
- formula (Chapter~\ref{ch:toroidal-elliptic}; distinct from
+ formula (Chapter~\ref{chap:toroidal-elliptic}; distinct from
  both $\kappa_{\mathrm{cat}}$ and $\kappa_{\mathrm{ch}}$).
 \end{enumerate}
 For CY$_2$ categories with $\frakg$-symmetry, all three can be
diff --git a/chapters/examples/toric_cy3_coha.tex b/chapters/examples/toric_cy3_coha.tex
index 2b8821c0fd545c77e9d18a4180e8e67d3c4459be..94da66b26dadb3a8dcd2e91287fd7092ea5a944c
--- a/chapters/examples/toric_cy3_coha.tex
+++ b/chapters/examples/toric_cy3_coha.tex
@@ -205,7 +205,7 @@
 \end{theorem}
 
 \begin{proof}
-(i) The compact base $\bP^1 \times \bP^1$ has $\chi(\bP^1 \times \bP^1) = 4$ (each factor contributes $\chi(\bP^1) = 2$), so $\kappa_{\mathrm{ch}} = \chi/2 = 2$ by the general local-surface formula (Remark~\ref{rem:toric-structural-patterns}).
+(i) The compact base $\bP^1 \times \bP^1$ has $\chi(\bP^1 \times \bP^1) = 4$ (each factor contributes $\chi(\bP^1) = 2$), so $\kappa_{\mathrm{ch}} = \chi/2 = 2$ by the general local-surface formula (Remark~\ref{rem:toric-kappa-patterns}).
 
 (ii) The intersection form on $H^2(\bP^1 \times \bP^1)$ in the basis $\{e_1, e_2\}$ is $\langle e_i, e_j \rangle = \delta_{ij}$ (the two rulings are orthogonal with self-intersection $0$ in the total space, but the relevant inner product for the shadow metric is the Euler pairing $\chi(e_i, e_j) = \delta_{ij}$).
 
@@ -654,7 +654,7 @@
 the chart gluing by descent, the shadow tower by the MC equation.
 These components are \emph{a priori} separate structures on the
 same algebra. The Vol~I chiral quantum group equivalence
-(Theorem~\ref{thm:chiral-qg-equiv}) asserts that three of them
+asserts that three of them
 (the vertex $R$-matrix, the chiral $A_\infty$-structure, and the
 chiral coproduct) determine each other on the Koszul locus. The theorem
 below specializes the abstract equivalence to the toric CY3 setting,
@@ -746,8 +746,7 @@
 
 \begin{proof}
 The abstract equivalence (I) $\leftrightarrow$ (II)
-$\leftrightarrow$ (III) is
-Theorem~\ref{thm:chiral-qg-equiv} of Vol~I, proved for any
+$\leftrightarrow$ (III) is the Vol~I chiral quantum group equivalence, proved for any
 $\Eone$-chiral algebra on the Koszul locus. The content of the
 present theorem is the identification of each abstract vertex
 with the independently constructed toric CY3 structure.
@@ -755,7 +754,7 @@
 \textit{Component~\textup{(I)}: $R$-matrix.}
 The $\Eone$-chiral algebra $A_X$ carries a vertex
 $R$-matrix by the general theory
-(Theorem~\ref{thm:chiral-qg-equiv}(I)). For toric CY3, the
+(item~\textup{(I)} of that equivalence). For toric CY3, the
 Maulik--Okounkov stable-envelope construction provides an
 independent $R$-matrix on $Y^+(\widehat{\fg}_{Q_X})$-modules.
 The two coincide because both solve the same Yang--Baxter
diff --git a/chapters/examples/toroidal_elliptic.tex b/chapters/examples/toroidal_elliptic.tex
index 8fcef3a49b8fe0bd45c3ae248676e994ece0ca7e..0a15b2c062f601ea29e50e3e3771b3eb1544db50
--- a/chapters/examples/toroidal_elliptic.tex
+++ b/chapters/examples/toroidal_elliptic.tex
@@ -5940,8 +5940,7 @@
 
 The K3 analogue of this picture replaces $\bC^2$ by a K3
 surface~$S$: the K3 double current algebra $\fg_{K3}$
-(Chapter~\ref{ch:k3-times-e},
-Definition~\ref{def:k3-double-current-algebra}) substitutes
+substitutes
 $H^*(S,\bC)$ for $\bC[u,v]$ and the Mukai pairing for the
 polynomial residue. Its quantization should produce a
 ``K3 Yangian'' standing in the same relation to $\fg_{K3}$ as the
@@ -6018,7 +6017,7 @@
   At $t \to 1$: the second parameter $w$ decouples and
   $\Delta_{z,w}$ reduces to the single-parameter
   Drinfeld coproduct $\Delta_z(T(u)) = T(u) \otimes T(u - z)$
-  of Theorem~\textup{\ref{thm:w-infty-chiral-qg}}.
+  of Proposition~\textup{\ref{prop:universal-coproduct}}.
 \end{enumerate}
 No two-parameter coproduct $\Delta_{z,w}$ currently exists in
 the literature or in this programme's compute infrastructure.
@@ -6034,7 +6033,7 @@
   $(q_1,q_2,q_3)$.
 \item Promote the DDCA shadow to an explicit $\Delta_{z,w}$
   formula aligned with the $R(u,v)$ surface in
-  \S\ref{subsec:quantum-chiral-algebras-6d}.
+  \S\ref{subsec:chiral-qg-wilson}.
 \item Build a compute witness at low modes: $w = 0$ reduces
   to existing $\Delta_z$; rational limit gives the DDCA
   shift; Miki sends $\Delta_{z,w} \to \Delta_{w,z}$.
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index ddbdfe60d9c9df04ba6f3acf48deee73523a64dc..3ce4e679084f2f25672104c7a00684df5e9f3b26
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -320,7 +320,7 @@
 Drinfeld coproduct from spin~$2$ to arbitrary spin, with the
 universal Miura coefficient $(\Psi{-}1)/\Psi$ on the leading
 cross-term $J \otimes W_{s-1}$ at every spin $s \ge 2$
-(Theorem~\ref{thm:miura-cross-universality}).
+(Proposition~\ref{prop:universal-coproduct}).
 
 \bigskip
 
@@ -328,7 +328,7 @@
 Volume~I defines $E_1$-chiral quantum groups abstractly. This
 volume constructs them concretely from CY geometry. The
 $E_1$-chiral bialgebra axioms (formalized in
-\S\ref{sec:e1-chiral-bialgebra}) require: (H1)~an $E_1$-chiral
+\S\ref{sec:e1-chiral-bialgebras}) require: (H1)~an $E_1$-chiral
 algebra $A$ on a curve $X$; (H2)~a spectral coproduct
 $\Delta_z \colon A \to A \otimes A$ (living on the OPEN/$E_1$
 colour); (H3)~an $R$-matrix $R(z)$ satisfying YBE; (H4)~RTT
diff --git a/chapters/theory/cy_categories.tex b/chapters/theory/cy_categories.tex
index f9b51871c44fa18a574c02fce8aaa49a49aa9c61..00d723a1cb5d4f2355a10cb2d9d3f86688259f09
--- a/chapters/theory/cy_categories.tex
+++ b/chapters/theory/cy_categories.tex
@@ -166,7 +166,7 @@
 Every smooth proper CY$_d$ category admits a cyclic $\Ainf$-enhancement, unique up to $\Ainf$-quasi-isomorphism preserving the pairing. The proof is due to Kontsevich--Soibelman in the formal case, Costello~\cite{Costello2005} for the TCFT enhancement, and Seidel~\cite{Seidel2008} for the Fukaya case.
 \end{theorem}
 
-At $d = 2$ the enhancement is explicit enough to compute directly; it drives the $K3$ computations feeding the Borcherds denominator (Vol~III Chapter~\ref{ch:k3}). At $d = 3$ the enhancement was constructed by Sheridan~\cite{Sheridan2015} for the quintic threefold, as part of the HMS proof; the general $d = 3$ construction remains programme-level (conditional on $\bS^3$-framing, see AP-CY6).
+At $d = 2$ the enhancement is explicit enough to compute directly; it drives the $K3$ computations feeding the Borcherds denominator (Vol~III Chapter~\ref{ch:k3-times-e}). At $d = 3$ the enhancement was constructed by Sheridan~\cite{Sheridan2015} for the quintic threefold, as part of the HMS proof; the general $d = 3$ construction remains programme-level (conditional on $\bS^3$-framing, see AP-CY6).
 
 \section{Interface with the CY-to-chiral functor $\Phi$}
 \label{sec:cy-cat-phi-interface}
@@ -194,7 +194,7 @@
 
 \begin{remark}[What $\Phi$ does not see]
 \label{rem:phi-does-not-see}
-Not every invariant of $\cC$ survives the passage through $\Phi$. The functor retains the cyclic $\Ainf$-structure and the Gerstenhaber bracket; it loses the fine structure of the triangulated / $\Ainf$ category (individual objects, t-structures, stability conditions) that is visible only via the fuller categorical CoHA construction of Chapter~\ref{ch:coha}. The kappa-spectrum (Vol~III CLAUDE.md) encodes which invariants survive: $\kappa_\mathrm{cat}$ is always present, $\kappa_\mathrm{ch}$ exists only when $\Phi$ is defined, and $\kappa_\mathrm{BKM}$ records the Borcherds-side lift for $K3 \times E$.
+Not every invariant of $\cC$ survives the passage through $\Phi$. The functor retains the cyclic $\Ainf$-structure and the Gerstenhaber bracket; it loses the fine structure of the triangulated / $\Ainf$ category (individual objects, t-structures, stability conditions) that is visible only via the fuller categorical CoHA construction of Chapter~\ref{ch:toric-coha}. The kappa-spectrum (Vol~III CLAUDE.md) encodes which invariants survive: $\kappa_\mathrm{cat}$ is always present, $\kappa_\mathrm{ch}$ exists only when $\Phi$ is defined, and $\kappa_\mathrm{BKM}$ records the Borcherds-side lift for $K3 \times E$.
 \end{remark}
 
 \begin{remark}[Cross-volume conventions]
diff --git a/chapters/theory/cy_to_chiral.tex b/chapters/theory/cy_to_chiral.tex
index 030fed4a9a2a7009ae05fdb0f3c431c8aed1fc83..14526e0aba63169841056220749304799a57fe10
--- a/chapters/theory/cy_to_chiral.tex
+++ b/chapters/theory/cy_to_chiral.tex
@@ -618,8 +618,8 @@
 homotopy is purely algebraic: it acts by
 $s(f_{i_0 \cdots i_q}) = f_{0 i_0 \cdots i_q}$ on \v{C}ech cochains and
 involves no PDE solving. The SDR data $(i, p, s)$ interfaces directly
-with the homotopy transfer theorem
-\textup{(}HTT, Theorem~\textup{\ref{thm:htt-general}}\textup{)},
+with the standard homotopy transfer theorem
+\textup{(}HTT\textup{)},
 transferring the $\Ainf$-structure from $\check{C}^\bullet(\cE nd(\cE))$
 to its cohomology $\Ext^\bullet(\cE, \cE)$.
 \end{theorem}
@@ -652,7 +652,7 @@
 (whether the formal series in the OPE coefficients converges to
 define honest holomorphic functions) requires separate input from
 the analytic completion programme (MC5,
-\S\ref{sec:analytic-sewing} of Vol~I). Specifically: the HTT
+the analytic sewing section of Vol~I). Specifically: the HTT
 produces transferred operations $\mu_k^{\mathrm{ch}}$ whose
 coefficients involve iterated applications of~$s$; each application
 introduces rational functions on the intersections $U_{i_0} \cap
@@ -1972,7 +1972,7 @@
  \bottomrule
 \end{tabular}
 \end{center}
-{\footnotesize $^*$The K3 entry records $\kappa_{\mathrm{ch}} = \chi(\cO_{\mathrm{K3}}) = 2$ (Proposition~\ref{prop:cy-kappa-d2}; verified via chiral de Rham, Chapter~\ref{ch:k3-times-e}). The distinct quantity $\dim \HH_*(D^b(\mathrm{K3}))/2 = 12$ arises from an alternative algebraization (the Monster orbifold); the full trichotomy ($\kappa_{\mathrm{ch}} \in \{2, 12, 24\}$) is developed in Section~\ref{subsec:k3-three-algebraizations} of Chapter~\ref{ch:k3-times-e}.
+{\footnotesize $^*$The K3 entry records $\kappa_{\mathrm{ch}} = \chi(\cO_{\mathrm{K3}}) = 2$ (Proposition~\ref{prop:cy-kappa-d2}; verified via chiral de Rham, Chapter~\ref{ch:k3-times-e}). The distinct quantity $\dim \HH_*(D^b(\mathrm{K3}))/2 = 12$ arises from an alternative algebraization (the Monster orbifold); the full trichotomy ($\kappa_{\mathrm{ch}} \in \{2, 12, 24\}$) is developed in the K3 discussion of Chapter~\ref{ch:k3-times-e}.
 
 $^\dagger$The $K3 \times E$ entry records $\kappa_{\mathrm{ch}} = 3$ by additivity (Proposition~\ref{prop:categorical-euler}: $\kappa_{\mathrm{ch}}(\mathrm{K3}) + \kappa_{\mathrm{ch}}(E) = 2 + 1$). The Borcherds automorphic weight is $\kappa_{\mathrm{BKM}} = 5 = \mathrm{wt}(\Delta_5)$, a distinct invariant.}
 
diff --git a/chapters/theory/drinfeld_center.tex b/chapters/theory/drinfeld_center.tex
index ac67d4e3a2ed8fab94fcb3fc63933d8650a92ac9..a711d853438f9e6a0e6fdd4e5dac61154b7b3c24
--- a/chapters/theory/drinfeld_center.tex
+++ b/chapters/theory/drinfeld_center.tex
@@ -726,7 +726,7 @@
 produces only symmetric braiding. The distinction is the
 deep reason for the $\Eone$ stabilization theorem
 (Chapter~\ref{ch:cy-to-chiral},
-Theorem~\ref{thm:e1-stabilization}).
+Theorem~\ref{thm:e1-stabilization-cy}).
 
 \begin{proposition}[$E_3$ restriction gives symmetric braiding]
 \label{prop:e3-symmetric-braiding}
diff --git a/chapters/theory/e1_chiral_algebras.tex b/chapters/theory/e1_chiral_algebras.tex
index 75484d2fff759dc21313b5595a8abade7d55d203..b533b2f5640db9eba4046a61106787f2c19a0d53
--- a/chapters/theory/e1_chiral_algebras.tex
+++ b/chapters/theory/e1_chiral_algebras.tex
@@ -63,7 +63,7 @@
 via holomorphic Chern--Simons; conjectural in general).
 The further $E_3$-topological upgrade requires a conformal
 vector at non-critical level
-(Volume~I, Theorem~\textup{\ref*{thm:topologization}}).
+(Volume~I, the topologization theorem).
 \end{definition}
 
 The closed colour carries $E_2$ structure from
@@ -128,7 +128,7 @@
 
 \begin{remark}[Three bars, one functor]
 \label{rem:three-bars-vol3}
-The CY-to-chiral functor $\Phi$ of Chapter~\ref{ch:cy-chiral-functor} has three natural composites. $\Phi_{E_1}$ produces $B^{\mathrm{ord}}(A_C)$; this is the ordered bar sensed by the Yangian. $\mathrm{av} \circ \Phi_{E_1}$ produces $B^{\Sigma}(A_C)$; this is the symmetric bar sensed by the modular characteristic $\kappa_{\mathrm{ch}}$. The full $E_2$ enhancement $\Phi_{E_2}$ produces the Drinfeld-centered bar $B^{E_2}(A_C) = \cZ(B^{\mathrm{ord}}(A_C))$; this is the braided bar sensed by the quantum group. All three factor through $\Phi_{E_1}$. This is the volume's motto: the ordered bar is the primitive.
+The CY-to-chiral functor $\Phi$ of Chapter~\ref{ch:cy-to-chiral} has three natural composites. $\Phi_{E_1}$ produces $B^{\mathrm{ord}}(A_C)$; this is the ordered bar sensed by the Yangian. $\mathrm{av} \circ \Phi_{E_1}$ produces $B^{\Sigma}(A_C)$; this is the symmetric bar sensed by the modular characteristic $\kappa_{\mathrm{ch}}$. The full $E_2$ enhancement $\Phi_{E_2}$ produces the Drinfeld-centered bar $B^{E_2}(A_C) = \cZ(B^{\mathrm{ord}}(A_C))$; this is the braided bar sensed by the quantum group. All three factor through $\Phi_{E_1}$. This is the volume's motto: the ordered bar is the primitive.
 \end{remark}
 
 \section{$E_1$-chiral algebras from CY categories}
@@ -153,7 +153,7 @@
 Let $\cC$ be a CY$_3$ category with a chain-level $S^3$-framing on $\mathrm{HC}^-_3(\cC)$ (the condition of Conjecture~CY-A$_3$). Then the ordered bar complex of the cyclic $A_\infty$ algebra $A_\cC$ carries an $E_1$-chiral structure whose representation category is a braided monoidal refinement of the BPS Yangian of $\cC$.
 \end{conjecture}
 
-The conjecture is conditional on the chain-level framing; the unconditional statement requires the full CY-A$_3$ programme. Every downstream result in \ref{part:examples} and \ref{part:connections} that uses the BPS Yangian inherits this conditionality. The connection to Maulik-Okounkov and Costello-Witten cohomological Hall algebras is traced in Chapter~\ref{ch:cha-yangian}.
+The conjecture is conditional on the chain-level framing; the unconditional statement requires the full CY-A$_3$ programme. Every downstream result in \ref{part:examples} and \ref{part:connections} that uses the BPS Yangian inherits this conditionality. The connection to Maulik-Okounkov and Costello-Witten cohomological Hall algebras is traced in Chapter~\ref{ch:toric-coha}.
 
 \begin{proposition}[$E_2$ enhancement via Drinfeld center]
 \label{prop:e2-enhancement-drinfeld}
@@ -318,7 +318,7 @@
 
 \begin{remark}[How this chapter is used downstream]
 \label{rem:downstream-usage}
-Chapters~\ref{ch:braided-factorization}, \ref{ch:drinfeld-center}, and \ref{ch:quantum-group-reps} use this chapter as the source of the ordered bar coalgebra and the averaging map. Chapter~\ref{ch:cy-chiral-functor} uses Proposition~\ref{prop:e1-sector-d2} as the $d=2$ existence statement for $A_\cC$. Every braided monoidal category that appears later is the Drinfeld center of an underlying ordered one.
+Chapters~\ref{ch:braided-factorization}, \ref{ch:drinfeld-center}, and \ref{ch:quantum-group-reps} use this chapter as the source of the ordered bar coalgebra and the averaging map. Chapter~\ref{ch:cy-to-chiral} uses Proposition~\ref{prop:e1-sector-d2} as the $d=2$ existence statement for $A_\cC$. Every braided monoidal category that appears later is the Drinfeld center of an underlying ordered one.
 \end{remark}
 
 \section{Operadic dictionary for the CY reader}
@@ -1447,7 +1447,7 @@
 cutting the elliptic curve.}
 For the product CY$_3$ manifold $X = K3 \times E$, the factorization
 homology integral $\int_{K3} \cF|_{K3}$ of
-Section~\ref{sec:k3-perturbative-fact-homology} produces a chiral algebra
+Section~\ref{subsec:fact-homology-k3xe} produces a chiral algebra
 $A_E$ on the residual elliptic curve $E$.  The coproduct on $A_E$ arises
 from cutting $E$ into two intervals via excision.  Concretely, choose a
 collar-gluing decomposition $E = I_1 \cup_{S^0 \times \R} I_2$ (cutting
diff --git a/chapters/theory/e2_chiral_algebras.tex b/chapters/theory/e2_chiral_algebras.tex
index 4d9c49d33b9b71c9728719844b5387b9c256ec23..8a25a3037dc9569752a97c0fc75347a4033380af
--- a/chapters/theory/e2_chiral_algebras.tex
+++ b/chapters/theory/e2_chiral_algebras.tex
@@ -194,7 +194,7 @@
 \label{sec:drinfeld-center-bridge}
 
 Volume~II constructs $\Phi_{E_1}$ and proves $E_1$-chiral Koszul
-duality (see \ref{part:e1-core} of \cite{VolII}). The Drinfeld center
+duality (see Part~I of \cite{VolII}). The Drinfeld center
 $Z\colon E_1\text{-}\Cat \xrightarrow{\sim} E_2\text{-}\Cat$
 (under dualizability) is the categorical passage from ordered
 monoidal data to braided monoidal data. On the bar side it matches the
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 30392e44f20b6614f1f54981964db6c0329363e5..69d953d96d354add714abf2eec933a753336234a
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -201,7 +201,7 @@
 \]
 The SDR data $(i, p, s)$ interfaces directly with the homotopy transfer theorem (HTT), transferring the $A_\infty$-structure from \v{C}ech cochains $\check{C}^\bullet(\mathcal{E}nd(\mathcal{E}))$ to its cohomology $\mathrm{Ext}^\bullet(\mathcal{E}, \mathcal{E})$. The transferred operations $\mu_k^{\mathrm{ch}}$ are given by sums over planar trees whose internal edges are decorated by the homotopy~$s$; each application of~$s$ introduces rational functions on the affine intersections, and the resulting chiral operations are well-defined as formal power series.
 
-The scope is perturbative: the \v{C}ech homotopy produces an algebraic $A_\infty$-structure on the Ext algebra, but convergence of the resulting series to holomorphic functions (the non-perturbative statement) requires separate input from the analytic completion programme of Volume~I (MC5, \S\ref{sec:analytic-sewing}). The perturbative statement suffices for the formal CY-to-chiral functor and for all combinatorial applications in this volume. The full construction, including the proof that the SDR conditions hold and the scope qualification, is Theorem~\ref{thm:cech-contracting-homotopy} in Chapter~\ref{ch:cy-to-chiral}.
+The scope is perturbative: the \v{C}ech homotopy produces an algebraic $A_\infty$-structure on the Ext algebra, but convergence of the resulting series to holomorphic functions (the non-perturbative statement) requires separate input from the analytic completion programme of Volume~I (MC5, the analytic sewing section there). The perturbative statement suffices for the formal CY-to-chiral functor and for all combinatorial applications in this volume. The full construction, including the proof that the SDR conditions hold and the scope qualification, is Theorem~\ref{thm:cech-contracting-homotopy} in Chapter~\ref{ch:cy-to-chiral}.
 
 Three independent consistency checks confirm the resulting chiral data for the quintic: the Gepner model matrix factorization (via mirror symmetry, $\mathrm{MF}(x_1^5 + \cdots + x_5^5)$), the large-volume Hodge--Kodaira--Rosenberg limit ($\mathrm{HKR}$ degeneration of $\mathrm{Ext}^\bullet$ to Dolbeault cohomology), and the Gopakumar--Vafa integrality of the resulting genus-$g$ amplitudes. All three produce the same modular characteristic $\chi/2 = -100$ (the MacMahon-normalised form of $\kappa_{\mathrm{cat}}$ at $d=3$).
 
@@ -277,7 +277,7 @@
  \item The moonshine multiplier: $A_n = \kappa_{\mathrm{cat}} \cdot \dim(\rho_n)$ identifies the factor $2$ in $Z_{K3} = 2\,\phi_{0,1}$.
  \item The categorical $\Etwo$-obstruction for CY$_3$ (Proposition~\ref{prop:e1-obstruction-categorical}): Serre duality forces antisymmetry of the Euler form, universally obstructing $\Etwo$-enhancement without torus hypotheses.
  \item Quiver-chart gluing for toric CY$_3$ (Theorem~\ref{thm:toric-chart-gluing}): the global $\Eone$-chiral algebra is assembled as a homotopy colimit of McKay-chart CoHAs, with $E_2$ descent degeneration and Costello--Li comparison.
- \item The K3 double current algebra $\fg_{K3}$ (Definition~\ref{def:k3-double-current-algebra}): the finite-dimensional analogue of the DDCA in which $\bC[u,v]$ is replaced by $H^*(S,\bC)$ with the Mukai pairing.
+ \item The K3 double current algebra $\fg_{K3}$: the finite-dimensional analogue of the DDCA in which $\bC[u,v]$ is replaced by $H^*(S,\bC)$ with the Mukai pairing.
  \item Forty-two CY/BKM compute engines with $5{,}700{+}$ tests across the standard CY landscape.
 \end{itemize}
 
@@ -360,7 +360,7 @@
 \item \emph{Descent theorem.}
  \v{C}ech descent for $E_1$-algebras over the Bridgeland
  stability manifold. Proved for toric CY3
- (Proposition~\ref{prop:e1-descent-unobstructed}); open for
+ (Theorem~\ref{thm:toric-chart-gluing}); open for
  compact CY3 beyond the chart-atlas regime.
 \item \emph{Higher-dimensional CY shadows.}
  The $E_n$ stabilization theorem
@@ -394,12 +394,12 @@
 
 \emph{Quantum group representations} (Chapter~\ref{ch:quantum-group-reps}). The representation-theoretic target. The braided monoidal category $\mathrm{Rep}_q(\mathfrak{g})$ is what the CY programme aims to realize: Conjecture~CY-C predicts that $\mathrm{Rep}_q(\mathfrak{g}) \simeq \mathrm{Rep}^{E_2}(A_\cC)$ for a CY category $\cC(\mathfrak{g}, q)$. The Kazhdan--Lusztig equivalence $\mathrm{Rep}_q(\mathfrak{g}) \simeq \mathrm{KL}_k(\mathfrak{g})$ at roots of unity is the prototype: the Volume~I bar complex $B(V_k(\mathfrak{g}))$ encodes the quantum group $R$-matrix in its degree-$(1,1)$ component, and the DK bridge (Volume~II, MC3 for all simple types) recovers the quantum group categorical structure. The affine Yangian realization (Chapter~\ref{ch:toric-coha}) provides the $E_1$-sector; the Drinfeld center (Chapter~\ref{ch:drinfeld-center}) provides the $E_2$-enhancement.
 
-In addition to the four standard families, the toroidal and elliptic algebras chapter (Chapter~\ref{chap:toroidal-elliptic}) develops the $K3 \times E$ programme in full: the generalized root datum, the BKM superalgebra $\mathfrak{g}_{\Delta_5}$ with its Igusa cusp form denominator identity, the shadow--Siegel gap theorem, thirteen structural results (K3-1 through K3-13), all ten research programmes (A through J), and the DDCA--toroidal bridge identifying the deformed double current algebra as the rational degeneration of the quantum toroidal algebra (Conjecture~\ref{conj:ddca-toroidal-bridge}). The K3 double current algebra $\fg_{K3}$ (Chapter~\ref{ch:k3-times-e}, Definition~\ref{def:k3-double-current-algebra}) provides the K3 analogue of the DDCA, replacing $\bC[u,v]$ with $H^*(S,\bC)$. The toric CY$_3$ CoHA chapter (Chapter~\ref{ch:toric-coha}) develops the affine Yangian and $\mathcal{W}_{1+\infty}$ side: the Jordan quiver gives $Y(\widehat{\mathfrak{gl}}_1) \simeq \mathcal{W}_{1+\infty}$, the toric fan is the Dynkin data, and the shuffle algebra presentation connects to the KZ equations of Volume~I.
+In addition to the four standard families, the toroidal and elliptic algebras chapter (Chapter~\ref{chap:toroidal-elliptic}) develops the $K3 \times E$ programme in full: the generalized root datum, the BKM superalgebra $\mathfrak{g}_{\Delta_5}$ with its Igusa cusp form denominator identity, the shadow--Siegel gap theorem, thirteen structural results (K3-1 through K3-13), all ten research programmes (A through J), and the DDCA--toroidal bridge identifying the deformed double current algebra as the rational degeneration of the quantum toroidal algebra (Conjecture~\ref{conj:ddca-toroidal-bridge}). The K3 double current algebra $\fg_{K3}$, discussed in the DDCA--toroidal bridge of Chapter~\ref{ch:k3-times-e}, provides the K3 analogue of the DDCA, replacing $\bC[u,v]$ with $H^*(S,\bC)$. The toric CY$_3$ CoHA chapter (Chapter~\ref{ch:toric-coha}) develops the affine Yangian and $\mathcal{W}_{1+\infty}$ side: the Jordan quiver gives $Y(\widehat{\mathfrak{gl}}_1) \simeq \mathcal{W}_{1+\infty}$, the toric fan is the Dynkin data, and the shuffle algebra presentation connects to the KZ equations of Volume~I.
 
 \section{Guide for the reader}
 \label{sec:guide}
 
-Part~\ref{part:cy-categories} establishes the categorical foundations: CY categories, cyclic $\Ainf$-structures, the Hochschild calculus, and the $E_1$/$E_2$/$E_n$ chiral hierarchy with the framing obstruction tower. Part~\ref{part:bridge} constructs the bridge functor $\Phi$ from CY categories to quantum chiral algebras and proves Theorems CY-A (for $d = 2$) and CY-D, with the identification of automorphic correction and shadow obstruction tower as the central result. Part~\ref{part:examples} treats quantum groups and their braided factorization structure, including the Drinfeld center as the bulk algebra. Part~\ref{part:connections} works through the standard landscape: the toroidal and elliptic algebras chapter develops the $K3 \times E$ programme (K3-1 through K3-13, programmes A through J), alongside toric CY3 CoHAs, Fukaya categories, derived categories, matrix factorizations (ADE singularities and W-algebras), and quantum group representations (Kazhdan--Lusztig, affine Yangians, critical CoHAs). Part~\ref{part:frontier} connects to the geometric Langlands programme and to Volumes~I and~II via the bar-cobar bridge and the modular Koszul bridge. The working notes (\S\ref{sec:working-notes}) record the research frontier.
+Part~\ref{part:cy-categories} establishes the categorical foundations: CY categories, cyclic $\Ainf$-structures, the Hochschild calculus, and the $E_1$/$E_2$/$E_n$ chiral hierarchy with the framing obstruction tower. Part~\ref{part:bridge} constructs the bridge functor $\Phi$ from CY categories to quantum chiral algebras and proves Theorems CY-A (for $d = 2$) and CY-D, with the identification of automorphic correction and shadow obstruction tower as the central result. Part~\ref{part:examples} treats quantum groups and their braided factorization structure, including the Drinfeld center as the bulk algebra. Part~\ref{part:connections} works through the standard landscape: the toroidal and elliptic algebras chapter develops the $K3 \times E$ programme (K3-1 through K3-13, programmes A through J), alongside toric CY3 CoHAs, Fukaya categories, derived categories, matrix factorizations (ADE singularities and W-algebras), and quantum group representations (Kazhdan--Lusztig, affine Yangians, critical CoHAs). Part~\ref{part:frontier} connects to the geometric Langlands programme and to Volumes~I and~II via the bar-cobar bridge and the modular Koszul bridge. The separate working notes record the research frontier.
 
 \section{Conventions and notation}
 \label{sec:conventions-intro}

codex
The build is clean on references now: `make fast` converged with `0 undef refs` on all four passes. I’m doing the last hygiene check the task asked for by grepping the touched files for the old broken label names, then I’ll close with a per-finding fixed/block status.
exec
/bin/zsh -lc "rg -n 'thm:miura-cross-universality|sec:e1-chiral-bialgebra|sec:analytic-sewing|def:k3-double-current-algebra|prop:e1-descent-unobstructed|sec:working-notes|ch:k3\\}|ch:coha|thm:topologization|ch:cy-chiral-functor|ch:cha-yangian|sec:k3-perturbative-fact-homology|part:e1-core|thm:htt-general|subsec:k3-three-algebraizations|thm:e1-stabilization|thm:w-infty-chiral-qg|subsec:quantum-chiral-algebras-6d|rem:toric-structural-patterns|thm:chiral-qg-equiv|ch:toroidal-elliptic|thm:cy-seven-face-master|part:3d-qg' chapters/frame/preface.tex chapters/theory/introduction.tex chapters/theory/cy_categories.tex chapters/theory/e1_chiral_algebras.tex chapters/theory/e2_chiral_algebras.tex chapters/theory/cy_to_chiral.tex chapters/theory/drinfeld_center.tex chapters/examples/toric_cy3_coha.tex chapters/examples/quantum_group_reps.tex chapters/examples/toroidal_elliptic.tex chapters/connections/cy_holographic_datum_master.tex chapters/connections/modular_koszul_bridge.tex -S" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc 'git diff --stat -- chapters/frame/preface.tex chapters/theory/introduction.tex chapters/theory/cy_categories.tex chapters/theory/e1_chiral_algebras.tex chapters/theory/e2_chiral_algebras.tex chapters/theory/cy_to_chiral.tex chapters/theory/drinfeld_center.tex chapters/examples/toric_cy3_coha.tex chapters/examples/quantum_group_reps.tex chapters/examples/toroidal_elliptic.tex chapters/connections/cy_holographic_datum_master.tex chapters/connections/modular_koszul_bridge.tex' in /Users/raeez/calabi-yau-quantum-groups succeeded in 52ms:
chapters/theory/drinfeld_center.tex:729:Theorem~\ref{thm:e1-stabilization-cy}).
chapters/frame/preface.tex:331:\S\ref{sec:e1-chiral-bialgebras}) require: (H1)~an $E_1$-chiral
chapters/theory/introduction.tex:67:The full proof of the stabilization theorem (Theorem~\ref{thm:e1-stabilization-cy}) is in Chapter~\ref{ch:en-factorization}.
chapters/theory/introduction.tex:367: (Theorem~\ref{thm:e1-stabilization-cy}) gives a Bott-periodic
chapters/theory/e1_chiral_algebras.tex:724:\label{sec:e1-chiral-bialgebras}
chapters/theory/cy_to_chiral.tex:746:For $d \geq 4$, the $\Eone$ stabilization theorem (Theorem~\ref{thm:e1-stabilization-cy}, Chapter~\ref{ch:en-factorization}) shows that the chiral algebra is always $\Eone$, with additional shifted structure classified by $\pi_d(BU)$ (Bott periodicity). The framing obstruction is $\Z$-valued at all even $d$, trivial at $d \equiv 1, 3, 7 \pmod{8}$, and $\Z_2$-valued from the $\Sp$-refinement at $d \equiv 5 \pmod{8}$.
 succeeded in 51ms:
 chapters/connections/cy_holographic_datum_master.tex |  2 +-
 chapters/connections/modular_koszul_bridge.tex       |  2 +-
 chapters/examples/quantum_group_reps.tex             |  2 +-
 chapters/examples/toric_cy3_coha.tex                 |  9 ++++-----
 chapters/examples/toroidal_elliptic.tex              |  7 +++----
 chapters/frame/preface.tex                           |  4 ++--
 chapters/theory/cy_categories.tex                    |  4 ++--
 chapters/theory/cy_to_chiral.tex                     |  8 ++++----
 chapters/theory/drinfeld_center.tex                  |  2 +-
 chapters/theory/e1_chiral_algebras.tex               | 10 +++++-----
 chapters/theory/e2_chiral_algebras.tex               |  2 +-
 chapters/theory/introduction.tex                     | 10 +++++-----
 12 files changed, 30 insertions(+), 32 deletions(-)
file update:
diff --git a/chapters/connections/cy_holographic_datum_master.tex b/chapters/connections/cy_holographic_datum_master.tex
index 2a66e8a0ca86f097e30b0de99c082498014430c6..b0ef34640300f22c24d57ee10a207c331065f31d
--- a/chapters/connections/cy_holographic_datum_master.tex
+++ b/chapters/connections/cy_holographic_datum_master.tex
@@ -943,7 +943,7 @@
 bar-cobar, CoHA / perverse coherent sheaves, classical CY Poisson
 coisson, MO stable envelope, affine super Yangian for toric CY$_3$,
 elliptic Sklyanin for toroidal CY, Gaudin from CY$_3$
-(Theorem~\ref{thm:cy-seven-face-master} above).
+(Conjecture~\ref{conj:cy-seven-face-master} above).
 \end{enumerate}
 The three master theorems are mutually compatible: under the CY-to-chiral
 functor $\Phi$, face~$i$ of Vol~III maps to a specialization of face~$i$
diff --git a/chapters/connections/modular_koszul_bridge.tex b/chapters/connections/modular_koszul_bridge.tex
index 1199c5aaa32e71f085dd3b7131c8f9aeadb1148c..a423d35b2ce162a9f56bb568768ae1bed7bef2f6
--- a/chapters/connections/modular_koszul_bridge.tex
+++ b/chapters/connections/modular_koszul_bridge.tex
@@ -234,7 +234,7 @@
 \end{theorem}
 
 \begin{proof}[Attribution]
-Parts (i), (iii), (iv) are Vol~I/II results (\S\ref{sec:k3e-cross-volume}, items K3-1 through K3-13, proved in the K3 modular-tower chapter of Vol~I and in the Vol~II 3D quantum gravity treatment, \ref{part:3d-qg} there). Part (ii) is the Borcherds lift of Borcherds (1998); its use as a modular characteristic is the observation of AP-CY8, not a theorem of Vol~III. The conditionality on propagates from Theorem~\ref{thm:cy-shadow-cohft}.
+Parts (i), (iii), (iv) are Vol~I/II results (\S\ref{sec:k3e-cross-volume}, items K3-1 through K3-13, proved in the K3 modular-tower chapter of Vol~I and in Part~III of Vol~II's 3D quantum gravity treatment). Part (ii) is the Borcherds lift of Borcherds (1998); its use as a modular characteristic is the observation of AP-CY8, not a theorem of Vol~III. The conditionality on propagates from Theorem~\ref{thm:cy-shadow-cohft}.
 \end{proof}
 
 \begin{remark}[Kappa-spectrum verification for $K3 \times E$]
diff --git a/chapters/examples/quantum_group_reps.tex b/chapters/examples/quantum_group_reps.tex
index e6b19a4c52de09f17af4b5f794d5f7269f4076b4..5213e6bfc9cb828c11c98b50aa32549aa228cfbf
--- a/chapters/examples/quantum_group_reps.tex
+++ b/chapters/examples/quantum_group_reps.tex
@@ -503,7 +503,7 @@
  additional data);
  \item $\kappa_{\mathrm{BKM}}$: the BKM modular weight, a
  number-theoretic invariant arising from the BKM denominator
- formula (Chapter~\ref{ch:toroidal-elliptic}; distinct from
+ formula (Chapter~\ref{chap:toroidal-elliptic}; distinct from
  both $\kappa_{\mathrm{cat}}$ and $\kappa_{\mathrm{ch}}$).
 \end{enumerate}
 For CY$_2$ categories with $\frakg$-symmetry, all three can be
diff --git a/chapters/examples/toric_cy3_coha.tex b/chapters/examples/toric_cy3_coha.tex
index 2b8821c0fd545c77e9d18a4180e8e67d3c4459be..94da66b26dadb3a8dcd2e91287fd7092ea5a944c
--- a/chapters/examples/toric_cy3_coha.tex
+++ b/chapters/examples/toric_cy3_coha.tex
@@ -205,7 +205,7 @@
 \end{theorem}
 
 \begin{proof}
-(i) The compact base $\bP^1 \times \bP^1$ has $\chi(\bP^1 \times \bP^1) = 4$ (each factor contributes $\chi(\bP^1) = 2$), so $\kappa_{\mathrm{ch}} = \chi/2 = 2$ by the general local-surface formula (Remark~\ref{rem:toric-structural-patterns}).
+(i) The compact base $\bP^1 \times \bP^1$ has $\chi(\bP^1 \times \bP^1) = 4$ (each factor contributes $\chi(\bP^1) = 2$), so $\kappa_{\mathrm{ch}} = \chi/2 = 2$ by the general local-surface formula (Remark~\ref{rem:toric-kappa-patterns}).
 
 (ii) The intersection form on $H^2(\bP^1 \times \bP^1)$ in the basis $\{e_1, e_2\}$ is $\langle e_i, e_j \rangle = \delta_{ij}$ (the two rulings are orthogonal with self-intersection $0$ in the total space, but the relevant inner product for the shadow metric is the Euler pairing $\chi(e_i, e_j) = \delta_{ij}$).
 
@@ -654,7 +654,7 @@
 the chart gluing by descent, the shadow tower by the MC equation.
 These components are \emph{a priori} separate structures on the
 same algebra. The Vol~I chiral quantum group equivalence
-(Theorem~\ref{thm:chiral-qg-equiv}) asserts that three of them
+asserts that three of them
 (the vertex $R$-matrix, the chiral $A_\infty$-structure, and the
 chiral coproduct) determine each other on the Koszul locus. The theorem
 below specializes the abstract equivalence to the toric CY3 setting,
@@ -746,8 +746,7 @@
 
 \begin{proof}
 The abstract equivalence (I) $\leftrightarrow$ (II)
-$\leftrightarrow$ (III) is
-Theorem~\ref{thm:chiral-qg-equiv} of Vol~I, proved for any
+$\leftrightarrow$ (III) is the Vol~I chiral quantum group equivalence, proved for any
 $\Eone$-chiral algebra on the Koszul locus. The content of the
 present theorem is the identification of each abstract vertex
 with the independently constructed toric CY3 structure.
@@ -755,7 +754,7 @@
 \textit{Component~\textup{(I)}: $R$-matrix.}
 The $\Eone$-chiral algebra $A_X$ carries a vertex
 $R$-matrix by the general theory
-(Theorem~\ref{thm:chiral-qg-equiv}(I)). For toric CY3, the
+(item~\textup{(I)} of that equivalence). For toric CY3, the
 Maulik--Okounkov stable-envelope construction provides an
 independent $R$-matrix on $Y^+(\widehat{\fg}_{Q_X})$-modules.
 The two coincide because both solve the same Yang--Baxter
diff --git a/chapters/examples/toroidal_elliptic.tex b/chapters/examples/toroidal_elliptic.tex
index 8fcef3a49b8fe0bd45c3ae248676e994ece0ca7e..0a15b2c062f601ea29e50e3e3771b3eb1544db50
--- a/chapters/examples/toroidal_elliptic.tex
+++ b/chapters/examples/toroidal_elliptic.tex
@@ -5940,8 +5940,7 @@
 
 The K3 analogue of this picture replaces $\bC^2$ by a K3
 surface~$S$: the K3 double current algebra $\fg_{K3}$
-(Chapter~\ref{ch:k3-times-e},
-Definition~\ref{def:k3-double-current-algebra}) substitutes
+substitutes
 $H^*(S,\bC)$ for $\bC[u,v]$ and the Mukai pairing for the
 polynomial residue. Its quantization should produce a
 ``K3 Yangian'' standing in the same relation to $\fg_{K3}$ as the
@@ -6018,7 +6017,7 @@
   At $t \to 1$: the second parameter $w$ decouples and
   $\Delta_{z,w}$ reduces to the single-parameter
   Drinfeld coproduct $\Delta_z(T(u)) = T(u) \otimes T(u - z)$
-  of Theorem~\textup{\ref{thm:w-infty-chiral-qg}}.
+  of Proposition~\textup{\ref{prop:universal-coproduct}}.
 \end{enumerate}
 No two-parameter coproduct $\Delta_{z,w}$ currently exists in
 the literature or in this programme's compute infrastructure.
@@ -6034,7 +6033,7 @@
   $(q_1,q_2,q_3)$.
 \item Promote the DDCA shadow to an explicit $\Delta_{z,w}$
   formula aligned with the $R(u,v)$ surface in
-  \S\ref{subsec:quantum-chiral-algebras-6d}.
+  \S\ref{subsec:chiral-qg-wilson}.
 \item Build a compute witness at low modes: $w = 0$ reduces
   to existing $\Delta_z$; rational limit gives the DDCA
   shift; Miki sends $\Delta_{z,w} \to \Delta_{w,z}$.
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index ddbdfe60d9c9df04ba6f3acf48deee73523a64dc..3ce4e679084f2f25672104c7a00684df5e9f3b26
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -320,7 +320,7 @@
 Drinfeld coproduct from spin~$2$ to arbitrary spin, with the
 universal Miura coefficient $(\Psi{-}1)/\Psi$ on the leading
 cross-term $J \otimes W_{s-1}$ at every spin $s \ge 2$
-(Theorem~\ref{thm:miura-cross-universality}).
+(Proposition~\ref{prop:universal-coproduct}).
 
 \bigskip
 
@@ -328,7 +328,7 @@
 Volume~I defines $E_1$-chiral quantum groups abstractly. This
 volume constructs them concretely from CY geometry. The
 $E_1$-chiral bialgebra axioms (formalized in
-\S\ref{sec:e1-chiral-bialgebra}) require: (H1)~an $E_1$-chiral
+\S\ref{sec:e1-chiral-bialgebras}) require: (H1)~an $E_1$-chiral
 algebra $A$ on a curve $X$; (H2)~a spectral coproduct
 $\Delta_z \colon A \to A \otimes A$ (living on the OPEN/$E_1$
 colour); (H3)~an $R$-matrix $R(z)$ satisfying YBE; (H4)~RTT
diff --git a/chapters/theory/cy_categories.tex b/chapters/theory/cy_categories.tex
index f9b51871c44fa18a574c02fce8aaa49a49aa9c61..00d723a1cb5d4f2355a10cb2d9d3f86688259f09
--- a/chapters/theory/cy_categories.tex
+++ b/chapters/theory/cy_categories.tex
@@ -166,7 +166,7 @@
 Every smooth proper CY$_d$ category admits a cyclic $\Ainf$-enhancement, unique up to $\Ainf$-quasi-isomorphism preserving the pairing. The proof is due to Kontsevich--Soibelman in the formal case, Costello~\cite{Costello2005} for the TCFT enhancement, and Seidel~\cite{Seidel2008} for the Fukaya case.
 \end{theorem}
 
-At $d = 2$ the enhancement is explicit enough to compute directly; it drives the $K3$ computations feeding the Borcherds denominator (Vol~III Chapter~\ref{ch:k3}). At $d = 3$ the enhancement was constructed by Sheridan~\cite{Sheridan2015} for the quintic threefold, as part of the HMS proof; the general $d = 3$ construction remains programme-level (conditional on $\bS^3$-framing, see AP-CY6).
+At $d = 2$ the enhancement is explicit enough to compute directly; it drives the $K3$ computations feeding the Borcherds denominator (Vol~III Chapter~\ref{ch:k3-times-e}). At $d = 3$ the enhancement was constructed by Sheridan~\cite{Sheridan2015} for the quintic threefold, as part of the HMS proof; the general $d = 3$ construction remains programme-level (conditional on $\bS^3$-framing, see AP-CY6).
 
 \section{Interface with the CY-to-chiral functor $\Phi$}
 \label{sec:cy-cat-phi-interface}
@@ -194,7 +194,7 @@
 
 \begin{remark}[What $\Phi$ does not see]
 \label{rem:phi-does-not-see}
-Not every invariant of $\cC$ survives the passage through $\Phi$. The functor retains the cyclic $\Ainf$-structure and the Gerstenhaber bracket; it loses the fine structure of the triangulated / $\Ainf$ category (individual objects, t-structures, stability conditions) that is visible only via the fuller categorical CoHA construction of Chapter~\ref{ch:coha}. The kappa-spectrum (Vol~III CLAUDE.md) encodes which invariants survive: $\kappa_\mathrm{cat}$ is always present, $\kappa_\mathrm{ch}$ exists only when $\Phi$ is defined, and $\kappa_\mathrm{BKM}$ records the Borcherds-side lift for $K3 \times E$.
+Not every invariant of $\cC$ survives the passage through $\Phi$. The functor retains the cyclic $\Ainf$-structure and the Gerstenhaber bracket; it loses the fine structure of the triangulated / $\Ainf$ category (individual objects, t-structures, stability conditions) that is visible only via the fuller categorical CoHA construction of Chapter~\ref{ch:toric-coha}. The kappa-spectrum (Vol~III CLAUDE.md) encodes which invariants survive: $\kappa_\mathrm{cat}$ is always present, $\kappa_\mathrm{ch}$ exists only when $\Phi$ is defined, and $\kappa_\mathrm{BKM}$ records the Borcherds-side lift for $K3 \times E$.
 \end{remark}
 
 \begin{remark}[Cross-volume conventions]
diff --git a/chapters/theory/cy_to_chiral.tex b/chapters/theory/cy_to_chiral.tex
index 030fed4a9a2a7009ae05fdb0f3c431c8aed1fc83..14526e0aba63169841056220749304799a57fe10
--- a/chapters/theory/cy_to_chiral.tex
+++ b/chapters/theory/cy_to_chiral.tex
@@ -618,8 +618,8 @@
 homotopy is purely algebraic: it acts by
 $s(f_{i_0 \cdots i_q}) = f_{0 i_0 \cdots i_q}$ on \v{C}ech cochains and
 involves no PDE solving. The SDR data $(i, p, s)$ interfaces directly
-with the homotopy transfer theorem
-\textup{(}HTT, Theorem~\textup{\ref{thm:htt-general}}\textup{)},
+with the standard homotopy transfer theorem
+\textup{(}HTT\textup{)},
 transferring the $\Ainf$-structure from $\check{C}^\bullet(\cE nd(\cE))$
 to its cohomology $\Ext^\bullet(\cE, \cE)$.
 \end{theorem}
@@ -652,7 +652,7 @@
 (whether the formal series in the OPE coefficients converges to
 define honest holomorphic functions) requires separate input from
 the analytic completion programme (MC5,
-\S\ref{sec:analytic-sewing} of Vol~I). Specifically: the HTT
+the analytic sewing section of Vol~I). Specifically: the HTT
 produces transferred operations $\mu_k^{\mathrm{ch}}$ whose
 coefficients involve iterated applications of~$s$; each application
 introduces rational functions on the intersections $U_{i_0} \cap
@@ -1972,7 +1972,7 @@
  \bottomrule
 \end{tabular}
 \end{center}
-{\footnotesize $^*$The K3 entry records $\kappa_{\mathrm{ch}} = \chi(\cO_{\mathrm{K3}}) = 2$ (Proposition~\ref{prop:cy-kappa-d2}; verified via chiral de Rham, Chapter~\ref{ch:k3-times-e}). The distinct quantity $\dim \HH_*(D^b(\mathrm{K3}))/2 = 12$ arises from an alternative algebraization (the Monster orbifold); the full trichotomy ($\kappa_{\mathrm{ch}} \in \{2, 12, 24\}$) is developed in Section~\ref{subsec:k3-three-algebraizations} of Chapter~\ref{ch:k3-times-e}.
+{\footnotesize $^*$The K3 entry records $\kappa_{\mathrm{ch}} = \chi(\cO_{\mathrm{K3}}) = 2$ (Proposition~\ref{prop:cy-kappa-d2}; verified via chiral de Rham, Chapter~\ref{ch:k3-times-e}). The distinct quantity $\dim \HH_*(D^b(\mathrm{K3}))/2 = 12$ arises from an alternative algebraization (the Monster orbifold); the full trichotomy ($\kappa_{\mathrm{ch}} \in \{2, 12, 24\}$) is developed in the K3 discussion of Chapter~\ref{ch:k3-times-e}.
 
 $^\dagger$The $K3 \times E$ entry records $\kappa_{\mathrm{ch}} = 3$ by additivity (Proposition~\ref{prop:categorical-euler}: $\kappa_{\mathrm{ch}}(\mathrm{K3}) + \kappa_{\mathrm{ch}}(E) = 2 + 1$). The Borcherds automorphic weight is $\kappa_{\mathrm{BKM}} = 5 = \mathrm{wt}(\Delta_5)$, a distinct invariant.}
 
diff --git a/chapters/theory/drinfeld_center.tex b/chapters/theory/drinfeld_center.tex
index ac67d4e3a2ed8fab94fcb3fc63933d8650a92ac9..a711d853438f9e6a0e6fdd4e5dac61154b7b3c24
--- a/chapters/theory/drinfeld_center.tex
+++ b/chapters/theory/drinfeld_center.tex
@@ -726,7 +726,7 @@
 produces only symmetric braiding. The distinction is the
 deep reason for the $\Eone$ stabilization theorem
 (Chapter~\ref{ch:cy-to-chiral},
-Theorem~\ref{thm:e1-stabilization}).
+Theorem~\ref{thm:e1-stabilization-cy}).
 
 \begin{proposition}[$E_3$ restriction gives symmetric braiding]
 \label{prop:e3-symmetric-braiding}
diff --git a/chapters/theory/e1_chiral_algebras.tex b/chapters/theory/e1_chiral_algebras.tex
index 75484d2fff759dc21313b5595a8abade7d55d203..b533b2f5640db9eba4046a61106787f2c19a0d53
--- a/chapters/theory/e1_chiral_algebras.tex
+++ b/chapters/theory/e1_chiral_algebras.tex
@@ -63,7 +63,7 @@
 via holomorphic Chern--Simons; conjectural in general).
 The further $E_3$-topological upgrade requires a conformal
 vector at non-critical level
-(Volume~I, Theorem~\textup{\ref*{thm:topologization}}).
+(Volume~I, the topologization theorem).
 \end{definition}
 
 The closed colour carries $E_2$ structure from
@@ -128,7 +128,7 @@
 
 \begin{remark}[Three bars, one functor]
 \label{rem:three-bars-vol3}
-The CY-to-chiral functor $\Phi$ of Chapter~\ref{ch:cy-chiral-functor} has three natural composites. $\Phi_{E_1}$ produces $B^{\mathrm{ord}}(A_C)$; this is the ordered bar sensed by the Yangian. $\mathrm{av} \circ \Phi_{E_1}$ produces $B^{\Sigma}(A_C)$; this is the symmetric bar sensed by the modular characteristic $\kappa_{\mathrm{ch}}$. The full $E_2$ enhancement $\Phi_{E_2}$ produces the Drinfeld-centered bar $B^{E_2}(A_C) = \cZ(B^{\mathrm{ord}}(A_C))$; this is the braided bar sensed by the quantum group. All three factor through $\Phi_{E_1}$. This is the volume's motto: the ordered bar is the primitive.
+The CY-to-chiral functor $\Phi$ of Chapter~\ref{ch:cy-to-chiral} has three natural composites. $\Phi_{E_1}$ produces $B^{\mathrm{ord}}(A_C)$; this is the ordered bar sensed by the Yangian. $\mathrm{av} \circ \Phi_{E_1}$ produces $B^{\Sigma}(A_C)$; this is the symmetric bar sensed by the modular characteristic $\kappa_{\mathrm{ch}}$. The full $E_2$ enhancement $\Phi_{E_2}$ produces the Drinfeld-centered bar $B^{E_2}(A_C) = \cZ(B^{\mathrm{ord}}(A_C))$; this is the braided bar sensed by the quantum group. All three factor through $\Phi_{E_1}$. This is the volume's motto: the ordered bar is the primitive.
 \end{remark}
 
 \section{$E_1$-chiral algebras from CY categories}
@@ -153,7 +153,7 @@
 Let $\cC$ be a CY$_3$ category with a chain-level $S^3$-framing on $\mathrm{HC}^-_3(\cC)$ (the condition of Conjecture~CY-A$_3$). Then the ordered bar complex of the cyclic $A_\infty$ algebra $A_\cC$ carries an $E_1$-chiral structure whose representation category is a braided monoidal refinement of the BPS Yangian of $\cC$.
 \end{conjecture}
 
-The conjecture is conditional on the chain-level framing; the unconditional statement requires the full CY-A$_3$ programme. Every downstream result in \ref{part:examples} and \ref{part:connections} that uses the BPS Yangian inherits this conditionality. The connection to Maulik-Okounkov and Costello-Witten cohomological Hall algebras is traced in Chapter~\ref{ch:cha-yangian}.
+The conjecture is conditional on the chain-level framing; the unconditional statement requires the full CY-A$_3$ programme. Every downstream result in \ref{part:examples} and \ref{part:connections} that uses the BPS Yangian inherits this conditionality. The connection to Maulik-Okounkov and Costello-Witten cohomological Hall algebras is traced in Chapter~\ref{ch:toric-coha}.
 
 \begin{proposition}[$E_2$ enhancement via Drinfeld center]
 \label{prop:e2-enhancement-drinfeld}
@@ -318,7 +318,7 @@
 
 \begin{remark}[How this chapter is used downstream]
 \label{rem:downstream-usage}
-Chapters~\ref{ch:braided-factorization}, \ref{ch:drinfeld-center}, and \ref{ch:quantum-group-reps} use this chapter as the source of the ordered bar coalgebra and the averaging map. Chapter~\ref{ch:cy-chiral-functor} uses Proposition~\ref{prop:e1-sector-d2} as the $d=2$ existence statement for $A_\cC$. Every braided monoidal category that appears later is the Drinfeld center of an underlying ordered one.
+Chapters~\ref{ch:braided-factorization}, \ref{ch:drinfeld-center}, and \ref{ch:quantum-group-reps} use this chapter as the source of the ordered bar coalgebra and the averaging map. Chapter~\ref{ch:cy-to-chiral} uses Proposition~\ref{prop:e1-sector-d2} as the $d=2$ existence statement for $A_\cC$. Every braided monoidal category that appears later is the Drinfeld center of an underlying ordered one.
 \end{remark}
 
 \section{Operadic dictionary for the CY reader}
@@ -1447,7 +1447,7 @@
 cutting the elliptic curve.}
 For the product CY$_3$ manifold $X = K3 \times E$, the factorization
 homology integral $\int_{K3} \cF|_{K3}$ of
-Section~\ref{sec:k3-perturbative-fact-homology} produces a chiral algebra
+Section~\ref{subsec:fact-homology-k3xe} produces a chiral algebra
 $A_E$ on the residual elliptic curve $E$.  The coproduct on $A_E$ arises
 from cutting $E$ into two intervals via excision.  Concretely, choose a
 collar-gluing decomposition $E = I_1 \cup_{S^0 \times \R} I_2$ (cutting
diff --git a/chapters/theory/e2_chiral_algebras.tex b/chapters/theory/e2_chiral_algebras.tex
index 4d9c49d33b9b71c9728719844b5387b9c256ec23..8a25a3037dc9569752a97c0fc75347a4033380af
--- a/chapters/theory/e2_chiral_algebras.tex
+++ b/chapters/theory/e2_chiral_algebras.tex
@@ -194,7 +194,7 @@
 \label{sec:drinfeld-center-bridge}
 
 Volume~II constructs $\Phi_{E_1}$ and proves $E_1$-chiral Koszul
-duality (see \ref{part:e1-core} of \cite{VolII}). The Drinfeld center
+duality (see Part~I of \cite{VolII}). The Drinfeld center
 $Z\colon E_1\text{-}\Cat \xrightarrow{\sim} E_2\text{-}\Cat$
 (under dualizability) is the categorical passage from ordered
 monoidal data to braided monoidal data. On the bar side it matches the
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 30392e44f20b6614f1f54981964db6c0329363e5..69d953d96d354add714abf2eec933a753336234a
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -201,7 +201,7 @@
 \]
 The SDR data $(i, p, s)$ interfaces directly with the homotopy transfer theorem (HTT), transferring the $A_\infty$-structure from \v{C}ech cochains $\check{C}^\bullet(\mathcal{E}nd(\mathcal{E}))$ to its cohomology $\mathrm{Ext}^\bullet(\mathcal{E}, \mathcal{E})$. The transferred operations $\mu_k^{\mathrm{ch}}$ are given by sums over planar trees whose internal edges are decorated by the homotopy~$s$; each application of~$s$ introduces rational functions on the affine intersections, and the resulting chiral operations are well-defined as formal power series.
 
-The scope is perturbative: the \v{C}ech homotopy produces an algebraic $A_\infty$-structure on the Ext algebra, but convergence of the resulting series to holomorphic functions (the non-perturbative statement) requires separate input from the analytic completion programme of Volume~I (MC5, \S\ref{sec:analytic-sewing}). The perturbative statement suffices for the formal CY-to-chiral functor and for all combinatorial applications in this volume. The full construction, including the proof that the SDR conditions hold and the scope qualification, is Theorem~\ref{thm:cech-contracting-homotopy} in Chapter~\ref{ch:cy-to-chiral}.
+The scope is perturbative: the \v{C}ech homotopy produces an algebraic $A_\infty$-structure on the Ext algebra, but convergence of the resulting series to holomorphic functions (the non-perturbative statement) requires separate input from the analytic completion programme of Volume~I (MC5, the analytic sewing section there). The perturbative statement suffices for the formal CY-to-chiral functor and for all combinatorial applications in this volume. The full construction, including the proof that the SDR conditions hold and the scope qualification, is Theorem~\ref{thm:cech-contracting-homotopy} in Chapter~\ref{ch:cy-to-chiral}.
 
 Three independent consistency checks confirm the resulting chiral data for the quintic: the Gepner model matrix factorization (via mirror symmetry, $\mathrm{MF}(x_1^5 + \cdots + x_5^5)$), the large-volume Hodge--Kodaira--Rosenberg limit ($\mathrm{HKR}$ degeneration of $\mathrm{Ext}^\bullet$ to Dolbeault cohomology), and the Gopakumar--Vafa integrality of the resulting genus-$g$ amplitudes. All three produce the same modular characteristic $\chi/2 = -100$ (the MacMahon-normalised form of $\kappa_{\mathrm{cat}}$ at $d=3$).
 
@@ -277,7 +277,7 @@
  \item The moonshine multiplier: $A_n = \kappa_{\mathrm{cat}} \cdot \dim(\rho_n)$ identifies the factor $2$ in $Z_{K3} = 2\,\phi_{0,1}$.
  \item The categorical $\Etwo$-obstruction for CY$_3$ (Proposition~\ref{prop:e1-obstruction-categorical}): Serre duality forces antisymmetry of the Euler form, universally obstructing $\Etwo$-enhancement without torus hypotheses.
  \item Quiver-chart gluing for toric CY$_3$ (Theorem~\ref{thm:toric-chart-gluing}): the global $\Eone$-chiral algebra is assembled as a homotopy colimit of McKay-chart CoHAs, with $E_2$ descent degeneration and Costello--Li comparison.
- \item The K3 double current algebra $\fg_{K3}$ (Definition~\ref{def:k3-double-current-algebra}): the finite-dimensional analogue of the DDCA in which $\bC[u,v]$ is replaced by $H^*(S,\bC)$ with the Mukai pairing.
+ \item The K3 double current algebra $\fg_{K3}$: the finite-dimensional analogue of the DDCA in which $\bC[u,v]$ is replaced by $H^*(S,\bC)$ with the Mukai pairing.
  \item Forty-two CY/BKM compute engines with $5{,}700{+}$ tests across the standard CY landscape.
 \end{itemize}
 
@@ -360,7 +360,7 @@
 \item \emph{Descent theorem.}
  \v{C}ech descent for $E_1$-algebras over the Bridgeland
  stability manifold. Proved for toric CY3
- (Proposition~\ref{prop:e1-descent-unobstructed}); open for
+ (Theorem~\ref{thm:toric-chart-gluing}); open for
  compact CY3 beyond the chart-atlas regime.
 \item \emph{Higher-dimensional CY shadows.}
  The $E_n$ stabilization theorem
@@ -394,12 +394,12 @@
 
 \emph{Quantum group representations} (Chapter~\ref{ch:quantum-group-reps}). The representation-theoretic target. The braided monoidal category $\mathrm{Rep}_q(\mathfrak{g})$ is what the CY programme aims to realize: Conjecture~CY-C predicts that $\mathrm{Rep}_q(\mathfrak{g}) \simeq \mathrm{Rep}^{E_2}(A_\cC)$ for a CY category $\cC(\mathfrak{g}, q)$. The Kazhdan--Lusztig equivalence $\mathrm{Rep}_q(\mathfrak{g}) \simeq \mathrm{KL}_k(\mathfrak{g})$ at roots of unity is the prototype: the Volume~I bar complex $B(V_k(\mathfrak{g}))$ encodes the quantum group $R$-matrix in its degree-$(1,1)$ component, and the DK bridge (Volume~II, MC3 for all simple types) recovers the quantum group categorical structure. The affine Yangian realization (Chapter~\ref{ch:toric-coha}) provides the $E_1$-sector; the Drinfeld center (Chapter~\ref{ch:drinfeld-center}) provides the $E_2$-enhancement.
 
-In addition to the four standard families, the toroidal and elliptic algebras chapter (Chapter~\ref{chap:toroidal-elliptic}) develops the $K3 \times E$ programme in full: the generalized root datum, the BKM superalgebra $\mathfrak{g}_{\Delta_5}$ with its Igusa cusp form denominator identity, the shadow--Siegel gap theorem, thirteen structural results (K3-1 through K3-13), all ten research programmes (A through J), and the DDCA--toroidal bridge identifying the deformed double current algebra as the rational degeneration of the quantum toroidal algebra (Conjecture~\ref{conj:ddca-toroidal-bridge}). The K3 double current algebra $\fg_{K3}$ (Chapter~\ref{ch:k3-times-e}, Definition~\ref{def:k3-double-current-algebra}) provides the K3 analogue of the DDCA, replacing $\bC[u,v]$ with $H^*(S,\bC)$. The toric CY$_3$ CoHA chapter (Chapter~\ref{ch:toric-coha}) develops the affine Yangian and $\mathcal{W}_{1+\infty}$ side: the Jordan quiver gives $Y(\widehat{\mathfrak{gl}}_1) \simeq \mathcal{W}_{1+\infty}$, the toric fan is the Dynkin data, and the shuffle algebra presentation connects to the KZ equations of Volume~I.
+In addition to the four standard families, the toroidal and elliptic algebras chapter (Chapter~\ref{chap:toroidal-elliptic}) develops the $K3 \times E$ programme in full: the generalized root datum, the BKM superalgebra $\mathfrak{g}_{\Delta_5}$ with its Igusa cusp form denominator identity, the shadow--Siegel gap theorem, thirteen structural results (K3-1 through K3-13), all ten research programmes (A through J), and the DDCA--toroidal bridge identifying the deformed double current algebra as the rational degeneration of the quantum toroidal algebra (Conjecture~\ref{conj:ddca-toroidal-bridge}). The K3 double current algebra $\fg_{K3}$, discussed in the DDCA--toroidal bridge of Chapter~\ref{ch:k3-times-e}, provides the K3 analogue of the DDCA, replacing $\bC[u,v]$ with $H^*(S,\bC)$. The toric CY$_3$ CoHA chapter (Chapter~\ref{ch:toric-coha}) develops the affine Yangian and $\mathcal{W}_{1+\infty}$ side: the Jordan quiver gives $Y(\widehat{\mathfrak{gl}}_1) \simeq \mathcal{W}_{1+\infty}$, the toric fan is the Dynkin data, and the shuffle algebra presentation connects to the KZ equations of Volume~I.
 
 \section{Guide for the reader}
 \label{sec:guide}
 
-Part~\ref{part:cy-categories} establishes the categorical foundations: CY categories, cyclic $\Ainf$-structures, the Hochschild calculus, and the $E_1$/$E_2$/$E_n$ chiral hierarchy with the framing obstruction tower. Part~\ref{part:bridge} constructs the bridge functor $\Phi$ from CY categories to quantum chiral algebras and proves Theorems CY-A (for $d = 2$) and CY-D, with the identification of automorphic correction and shadow obstruction tower as the central result. Part~\ref{part:examples} treats quantum groups and their braided factorization structure, including the Drinfeld center as the bulk algebra. Part~\ref{part:connections} works through the standard landscape: the toroidal and elliptic algebras chapter develops the $K3 \times E$ programme (K3-1 through K3-13, programmes A through J), alongside toric CY3 CoHAs, Fukaya categories, derived categories, matrix factorizations (ADE singularities and W-algebras), and quantum group representations (Kazhdan--Lusztig, affine Yangians, critical CoHAs). Part~\ref{part:frontier} connects to the geometric Langlands programme and to Volumes~I and~II via the bar-cobar bridge and the modular Koszul bridge. The working notes (\S\ref{sec:working-notes}) record the research frontier.
+Part~\ref{part:cy-categories} establishes the categorical foundations: CY categories, cyclic $\Ainf$-structures, the Hochschild calculus, and the $E_1$/$E_2$/$E_n$ chiral hierarchy with the framing obstruction tower. Part~\ref{part:bridge} constructs the bridge functor $\Phi$ from CY categories to quantum chiral algebras and proves Theorems CY-A (for $d = 2$) and CY-D, with the identification of automorphic correction and shadow obstruction tower as the central result. Part~\ref{part:examples} treats quantum groups and their braided factorization structure, including the Drinfeld center as the bulk algebra. Part~\ref{part:connections} works through the standard landscape: the toroidal and elliptic algebras chapter develops the $K3 \times E$ programme (K3-1 through K3-13, programmes A through J), alongside toric CY3 CoHAs, Fukaya categories, derived categories, matrix factorizations (ADE singularities and W-algebras), and quantum group representations (Kazhdan--Lusztig, affine Yangians, critical CoHAs). Part~\ref{part:frontier} connects to the geometric Langlands programme and to Volumes~I and~II via the bar-cobar bridge and the modular Koszul bridge. The separate working notes record the research frontier.
 
 \section{Conventions and notation}
 \label{sec:conventions-intro}


thinking
**Refining grep patterns**

I matched certain patterns with `thm:e1-stabilization` and `sec:e1-chiral-bialgebra` because they're substrings in longer labels. I realize I need to refine these with braces or quotes to ensure that unwanted old forms are excluded. Since the user requested a focus on forbidden patterns, I might need to use exact old labels. I’ll consider curly forms like `\\ref\{thm:e1-stabilization\}` and `\\label{sec:e1-chiral-bialgebra}` for better precision. Let's make sure to run this more accurately!
codex
The first grep was too loose: it matched the fixed labels as substrings of the live ones. I’m rerunning it with exact `\ref{...}` patterns so the hygiene check is actually meaningful.
exec
/bin/zsh -lc "rg -n '\\\\(?:eq)?ref\\{(?:thm:miura-cross-universality|sec:e1-chiral-bialgebra|sec:analytic-sewing|def:k3-double-current-algebra|prop:e1-descent-unobstructed|sec:working-notes|ch:k3|ch:coha|thm:topologization|ch:cy-chiral-functor|ch:cha-yangian|sec:k3-perturbative-fact-homology|part:e1-core|thm:htt-general|subsec:k3-three-algebraizations|thm:e1-stabilization|thm:w-infty-chiral-qg|subsec:quantum-chiral-algebras-6d|rem:toric-structural-patterns|thm:chiral-qg-equiv|ch:toroidal-elliptic|thm:cy-seven-face-master|part:3d-qg)\\}' chapters/frame/preface.tex chapters/theory/introduction.tex chapters/theory/cy_categories.tex chapters/theory/e1_chiral_algebras.tex chapters/theory/e2_chiral_algebras.tex chapters/theory/cy_to_chiral.tex chapters/theory/drinfeld_center.tex chapters/examples/toric_cy3_coha.tex chapters/examples/quantum_group_reps.tex chapters/examples/toroidal_elliptic.tex chapters/connections/cy_holographic_datum_master.tex chapters/connections/modular_koszul_bridge.tex -S" in /Users/raeez/calabi-yau-quantum-groups exited 1 in 52ms:

file update:
diff --git a/chapters/connections/cy_holographic_datum_master.tex b/chapters/connections/cy_holographic_datum_master.tex
index 2a66e8a0ca86f097e30b0de99c082498014430c6..b0ef34640300f22c24d57ee10a207c331065f31d
--- a/chapters/connections/cy_holographic_datum_master.tex
+++ b/chapters/connections/cy_holographic_datum_master.tex
@@ -943,7 +943,7 @@
 bar-cobar, CoHA / perverse coherent sheaves, classical CY Poisson
 coisson, MO stable envelope, affine super Yangian for toric CY$_3$,
 elliptic Sklyanin for toroidal CY, Gaudin from CY$_3$
-(Theorem~\ref{thm:cy-seven-face-master} above).
+(Conjecture~\ref{conj:cy-seven-face-master} above).
 \end{enumerate}
 The three master theorems are mutually compatible: under the CY-to-chiral
 functor $\Phi$, face~$i$ of Vol~III maps to a specialization of face~$i$
diff --git a/chapters/connections/modular_koszul_bridge.tex b/chapters/connections/modular_koszul_bridge.tex
index 1199c5aaa32e71f085dd3b7131c8f9aeadb1148c..a423d35b2ce162a9f56bb568768ae1bed7bef2f6
--- a/chapters/connections/modular_koszul_bridge.tex
+++ b/chapters/connections/modular_koszul_bridge.tex
@@ -234,7 +234,7 @@
 \end{theorem}
 
 \begin{proof}[Attribution]
-Parts (i), (iii), (iv) are Vol~I/II results (\S\ref{sec:k3e-cross-volume}, items K3-1 through K3-13, proved in the K3 modular-tower chapter of Vol~I and in the Vol~II 3D quantum gravity treatment, \ref{part:3d-qg} there). Part (ii) is the Borcherds lift of Borcherds (1998); its use as a modular characteristic is the observation of AP-CY8, not a theorem of Vol~III. The conditionality on propagates from Theorem~\ref{thm:cy-shadow-cohft}.
+Parts (i), (iii), (iv) are Vol~I/II results (\S\ref{sec:k3e-cross-volume}, items K3-1 through K3-13, proved in the K3 modular-tower chapter of Vol~I and in Part~III of Vol~II's 3D quantum gravity treatment). Part (ii) is the Borcherds lift of Borcherds (1998); its use as a modular characteristic is the observation of AP-CY8, not a theorem of Vol~III. The conditionality on propagates from Theorem~\ref{thm:cy-shadow-cohft}.
 \end{proof}
 
 \begin{remark}[Kappa-spectrum verification for $K3 \times E$]
diff --git a/chapters/examples/quantum_group_reps.tex b/chapters/examples/quantum_group_reps.tex
index e6b19a4c52de09f17af4b5f794d5f7269f4076b4..5213e6bfc9cb828c11c98b50aa32549aa228cfbf
--- a/chapters/examples/quantum_group_reps.tex
+++ b/chapters/examples/quantum_group_reps.tex
@@ -503,7 +503,7 @@
  additional data);
  \item $\kappa_{\mathrm{BKM}}$: the BKM modular weight, a
  number-theoretic invariant arising from the BKM denominator
- formula (Chapter~\ref{ch:toroidal-elliptic}; distinct from
+ formula (Chapter~\ref{chap:toroidal-elliptic}; distinct from
  both $\kappa_{\mathrm{cat}}$ and $\kappa_{\mathrm{ch}}$).
 \end{enumerate}
 For CY$_2$ categories with $\frakg$-symmetry, all three can be
diff --git a/chapters/examples/toric_cy3_coha.tex b/chapters/examples/toric_cy3_coha.tex
index 2b8821c0fd545c77e9d18a4180e8e67d3c4459be..94da66b26dadb3a8dcd2e91287fd7092ea5a944c
--- a/chapters/examples/toric_cy3_coha.tex
+++ b/chapters/examples/toric_cy3_coha.tex
@@ -205,7 +205,7 @@
 \end{theorem}
 
 \begin{proof}
-(i) The compact base $\bP^1 \times \bP^1$ has $\chi(\bP^1 \times \bP^1) = 4$ (each factor contributes $\chi(\bP^1) = 2$), so $\kappa_{\mathrm{ch}} = \chi/2 = 2$ by the general local-surface formula (Remark~\ref{rem:toric-structural-patterns}).
+(i) The compact base $\bP^1 \times \bP^1$ has $\chi(\bP^1 \times \bP^1) = 4$ (each factor contributes $\chi(\bP^1) = 2$), so $\kappa_{\mathrm{ch}} = \chi/2 = 2$ by the general local-surface formula (Remark~\ref{rem:toric-kappa-patterns}).
 
 (ii) The intersection form on $H^2(\bP^1 \times \bP^1)$ in the basis $\{e_1, e_2\}$ is $\langle e_i, e_j \rangle = \delta_{ij}$ (the two rulings are orthogonal with self-intersection $0$ in the total space, but the relevant inner product for the shadow metric is the Euler pairing $\chi(e_i, e_j) = \delta_{ij}$).
 
@@ -654,7 +654,7 @@
 the chart gluing by descent, the shadow tower by the MC equation.
 These components are \emph{a priori} separate structures on the
 same algebra. The Vol~I chiral quantum group equivalence
-(Theorem~\ref{thm:chiral-qg-equiv}) asserts that three of them
+asserts that three of them
 (the vertex $R$-matrix, the chiral $A_\infty$-structure, and the
 chiral coproduct) determine each other on the Koszul locus. The theorem
 below specializes the abstract equivalence to the toric CY3 setting,
@@ -746,8 +746,7 @@
 
 \begin{proof}
 The abstract equivalence (I) $\leftrightarrow$ (II)
-$\leftrightarrow$ (III) is
-Theorem~\ref{thm:chiral-qg-equiv} of Vol~I, proved for any
+$\leftrightarrow$ (III) is the Vol~I chiral quantum group equivalence, proved for any
 $\Eone$-chiral algebra on the Koszul locus. The content of the
 present theorem is the identification of each abstract vertex
 with the independently constructed toric CY3 structure.
@@ -755,7 +754,7 @@
 \textit{Component~\textup{(I)}: $R$-matrix.}
 The $\Eone$-chiral algebra $A_X$ carries a vertex
 $R$-matrix by the general theory
-(Theorem~\ref{thm:chiral-qg-equiv}(I)). For toric CY3, the
+(item~\textup{(I)} of that equivalence). For toric CY3, the
 Maulik--Okounkov stable-envelope construction provides an
 independent $R$-matrix on $Y^+(\widehat{\fg}_{Q_X})$-modules.
 The two coincide because both solve the same Yang--Baxter
diff --git a/chapters/examples/toroidal_elliptic.tex b/chapters/examples/toroidal_elliptic.tex
index 8fcef3a49b8fe0bd45c3ae248676e994ece0ca7e..0a15b2c062f601ea29e50e3e3771b3eb1544db50
--- a/chapters/examples/toroidal_elliptic.tex
+++ b/chapters/examples/toroidal_elliptic.tex
@@ -5940,8 +5940,7 @@
 
 The K3 analogue of this picture replaces $\bC^2$ by a K3
 surface~$S$: the K3 double current algebra $\fg_{K3}$
-(Chapter~\ref{ch:k3-times-e},
-Definition~\ref{def:k3-double-current-algebra}) substitutes
+substitutes
 $H^*(S,\bC)$ for $\bC[u,v]$ and the Mukai pairing for the
 polynomial residue. Its quantization should produce a
 ``K3 Yangian'' standing in the same relation to $\fg_{K3}$ as the
@@ -6018,7 +6017,7 @@
   At $t \to 1$: the second parameter $w$ decouples and
   $\Delta_{z,w}$ reduces to the single-parameter
   Drinfeld coproduct $\Delta_z(T(u)) = T(u) \otimes T(u - z)$
-  of Theorem~\textup{\ref{thm:w-infty-chiral-qg}}.
+  of Proposition~\textup{\ref{prop:universal-coproduct}}.
 \end{enumerate}
 No two-parameter coproduct $\Delta_{z,w}$ currently exists in
 the literature or in this programme's compute infrastructure.
@@ -6034,7 +6033,7 @@
   $(q_1,q_2,q_3)$.
 \item Promote the DDCA shadow to an explicit $\Delta_{z,w}$
   formula aligned with the $R(u,v)$ surface in
-  \S\ref{subsec:quantum-chiral-algebras-6d}.
+  \S\ref{subsec:chiral-qg-wilson}.
 \item Build a compute witness at low modes: $w = 0$ reduces
   to existing $\Delta_z$; rational limit gives the DDCA
   shift; Miki sends $\Delta_{z,w} \to \Delta_{w,z}$.
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index ddbdfe60d9c9df04ba6f3acf48deee73523a64dc..3ce4e679084f2f25672104c7a00684df5e9f3b26
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -320,7 +320,7 @@
 Drinfeld coproduct from spin~$2$ to arbitrary spin, with the
 universal Miura coefficient $(\Psi{-}1)/\Psi$ on the leading
 cross-term $J \otimes W_{s-1}$ at every spin $s \ge 2$
-(Theorem~\ref{thm:miura-cross-universality}).
+(Proposition~\ref{prop:universal-coproduct}).
 
 \bigskip
 
@@ -328,7 +328,7 @@
 Volume~I defines $E_1$-chiral quantum groups abstractly. This
 volume constructs them concretely from CY geometry. The
 $E_1$-chiral bialgebra axioms (formalized in
-\S\ref{sec:e1-chiral-bialgebra}) require: (H1)~an $E_1$-chiral
+\S\ref{sec:e1-chiral-bialgebras}) require: (H1)~an $E_1$-chiral
 algebra $A$ on a curve $X$; (H2)~a spectral coproduct
 $\Delta_z \colon A \to A \otimes A$ (living on the OPEN/$E_1$
 colour); (H3)~an $R$-matrix $R(z)$ satisfying YBE; (H4)~RTT
diff --git a/chapters/theory/cy_categories.tex b/chapters/theory/cy_categories.tex
index f9b51871c44fa18a574c02fce8aaa49a49aa9c61..00d723a1cb5d4f2355a10cb2d9d3f86688259f09
--- a/chapters/theory/cy_categories.tex
+++ b/chapters/theory/cy_categories.tex
@@ -166,7 +166,7 @@
 Every smooth proper CY$_d$ category admits a cyclic $\Ainf$-enhancement, unique up to $\Ainf$-quasi-isomorphism preserving the pairing. The proof is due to Kontsevich--Soibelman in the formal case, Costello~\cite{Costello2005} for the TCFT enhancement, and Seidel~\cite{Seidel2008} for the Fukaya case.
 \end{theorem}
 
-At $d = 2$ the enhancement is explicit enough to compute directly; it drives the $K3$ computations feeding the Borcherds denominator (Vol~III Chapter~\ref{ch:k3}). At $d = 3$ the enhancement was constructed by Sheridan~\cite{Sheridan2015} for the quintic threefold, as part of the HMS proof; the general $d = 3$ construction remains programme-level (conditional on $\bS^3$-framing, see AP-CY6).
+At $d = 2$ the enhancement is explicit enough to compute directly; it drives the $K3$ computations feeding the Borcherds denominator (Vol~III Chapter~\ref{ch:k3-times-e}). At $d = 3$ the enhancement was constructed by Sheridan~\cite{Sheridan2015} for the quintic threefold, as part of the HMS proof; the general $d = 3$ construction remains programme-level (conditional on $\bS^3$-framing, see AP-CY6).
 
 \section{Interface with the CY-to-chiral functor $\Phi$}
 \label{sec:cy-cat-phi-interface}
@@ -194,7 +194,7 @@
 
 \begin{remark}[What $\Phi$ does not see]
 \label{rem:phi-does-not-see}
-Not every invariant of $\cC$ survives the passage through $\Phi$. The functor retains the cyclic $\Ainf$-structure and the Gerstenhaber bracket; it loses the fine structure of the triangulated / $\Ainf$ category (individual objects, t-structures, stability conditions) that is visible only via the fuller categorical CoHA construction of Chapter~\ref{ch:coha}. The kappa-spectrum (Vol~III CLAUDE.md) encodes which invariants survive: $\kappa_\mathrm{cat}$ is always present, $\kappa_\mathrm{ch}$ exists only when $\Phi$ is defined, and $\kappa_\mathrm{BKM}$ records the Borcherds-side lift for $K3 \times E$.
+Not every invariant of $\cC$ survives the passage through $\Phi$. The functor retains the cyclic $\Ainf$-structure and the Gerstenhaber bracket; it loses the fine structure of the triangulated / $\Ainf$ category (individual objects, t-structures, stability conditions) that is visible only via the fuller categorical CoHA construction of Chapter~\ref{ch:toric-coha}. The kappa-spectrum (Vol~III CLAUDE.md) encodes which invariants survive: $\kappa_\mathrm{cat}$ is always present, $\kappa_\mathrm{ch}$ exists only when $\Phi$ is defined, and $\kappa_\mathrm{BKM}$ records the Borcherds-side lift for $K3 \times E$.
 \end{remark}
 
 \begin{remark}[Cross-volume conventions]
diff --git a/chapters/theory/cy_to_chiral.tex b/chapters/theory/cy_to_chiral.tex
index 030fed4a9a2a7009ae05fdb0f3c431c8aed1fc83..14526e0aba63169841056220749304799a57fe10
--- a/chapters/theory/cy_to_chiral.tex
+++ b/chapters/theory/cy_to_chiral.tex
@@ -618,8 +618,8 @@
 homotopy is purely algebraic: it acts by
 $s(f_{i_0 \cdots i_q}) = f_{0 i_0 \cdots i_q}$ on \v{C}ech cochains and
 involves no PDE solving. The SDR data $(i, p, s)$ interfaces directly
-with the homotopy transfer theorem
-\textup{(}HTT, Theorem~\textup{\ref{thm:htt-general}}\textup{)},
+with the standard homotopy transfer theorem
+\textup{(}HTT\textup{)},
 transferring the $\Ainf$-structure from $\check{C}^\bullet(\cE nd(\cE))$
 to its cohomology $\Ext^\bullet(\cE, \cE)$.
 \end{theorem}
@@ -652,7 +652,7 @@
 (whether the formal series in the OPE coefficients converges to
 define honest holomorphic functions) requires separate input from
 the analytic completion programme (MC5,
-\S\ref{sec:analytic-sewing} of Vol~I). Specifically: the HTT
+the analytic sewing section of Vol~I). Specifically: the HTT
 produces transferred operations $\mu_k^{\mathrm{ch}}$ whose
 coefficients involve iterated applications of~$s$; each application
 introduces rational functions on the intersections $U_{i_0} \cap
@@ -1972,7 +1972,7 @@
  \bottomrule
 \end{tabular}
 \end{center}
-{\footnotesize $^*$The K3 entry records $\kappa_{\mathrm{ch}} = \chi(\cO_{\mathrm{K3}}) = 2$ (Proposition~\ref{prop:cy-kappa-d2}; verified via chiral de Rham, Chapter~\ref{ch:k3-times-e}). The distinct quantity $\dim \HH_*(D^b(\mathrm{K3}))/2 = 12$ arises from an alternative algebraization (the Monster orbifold); the full trichotomy ($\kappa_{\mathrm{ch}} \in \{2, 12, 24\}$) is developed in Section~\ref{subsec:k3-three-algebraizations} of Chapter~\ref{ch:k3-times-e}.
+{\footnotesize $^*$The K3 entry records $\kappa_{\mathrm{ch}} = \chi(\cO_{\mathrm{K3}}) = 2$ (Proposition~\ref{prop:cy-kappa-d2}; verified via chiral de Rham, Chapter~\ref{ch:k3-times-e}). The distinct quantity $\dim \HH_*(D^b(\mathrm{K3}))/2 = 12$ arises from an alternative algebraization (the Monster orbifold); the full trichotomy ($\kappa_{\mathrm{ch}} \in \{2, 12, 24\}$) is developed in the K3 discussion of Chapter~\ref{ch:k3-times-e}.
 
 $^\dagger$The $K3 \times E$ entry records $\kappa_{\mathrm{ch}} = 3$ by additivity (Proposition~\ref{prop:categorical-euler}: $\kappa_{\mathrm{ch}}(\mathrm{K3}) + \kappa_{\mathrm{ch}}(E) = 2 + 1$). The Borcherds automorphic weight is $\kappa_{\mathrm{BKM}} = 5 = \mathrm{wt}(\Delta_5)$, a distinct invariant.}
 
diff --git a/chapters/theory/drinfeld_center.tex b/chapters/theory/drinfeld_center.tex
index ac67d4e3a2ed8fab94fcb3fc63933d8650a92ac9..a711d853438f9e6a0e6fdd4e5dac61154b7b3c24
--- a/chapters/theory/drinfeld_center.tex
+++ b/chapters/theory/drinfeld_center.tex
@@ -726,7 +726,7 @@
 produces only symmetric braiding. The distinction is the
 deep reason for the $\Eone$ stabilization theorem
 (Chapter~\ref{ch:cy-to-chiral},
-Theorem~\ref{thm:e1-stabilization}).
+Theorem~\ref{thm:e1-stabilization-cy}).
 
 \begin{proposition}[$E_3$ restriction gives symmetric braiding]
 \label{prop:e3-symmetric-braiding}
diff --git a/chapters/theory/e1_chiral_algebras.tex b/chapters/theory/e1_chiral_algebras.tex
index 75484d2fff759dc21313b5595a8abade7d55d203..b533b2f5640db9eba4046a61106787f2c19a0d53
--- a/chapters/theory/e1_chiral_algebras.tex
+++ b/chapters/theory/e1_chiral_algebras.tex
@@ -63,7 +63,7 @@
 via holomorphic Chern--Simons; conjectural in general).
 The further $E_3$-topological upgrade requires a conformal
 vector at non-critical level
-(Volume~I, Theorem~\textup{\ref*{thm:topologization}}).
+(Volume~I, the topologization theorem).
 \end{definition}
 
 The closed colour carries $E_2$ structure from
@@ -128,7 +128,7 @@
 
 \begin{remark}[Three bars, one functor]
 \label{rem:three-bars-vol3}
-The CY-to-chiral functor $\Phi$ of Chapter~\ref{ch:cy-chiral-functor} has three natural composites. $\Phi_{E_1}$ produces $B^{\mathrm{ord}}(A_C)$; this is the ordered bar sensed by the Yangian. $\mathrm{av} \circ \Phi_{E_1}$ produces $B^{\Sigma}(A_C)$; this is the symmetric bar sensed by the modular characteristic $\kappa_{\mathrm{ch}}$. The full $E_2$ enhancement $\Phi_{E_2}$ produces the Drinfeld-centered bar $B^{E_2}(A_C) = \cZ(B^{\mathrm{ord}}(A_C))$; this is the braided bar sensed by the quantum group. All three factor through $\Phi_{E_1}$. This is the volume's motto: the ordered bar is the primitive.
+The CY-to-chiral functor $\Phi$ of Chapter~\ref{ch:cy-to-chiral} has three natural composites. $\Phi_{E_1}$ produces $B^{\mathrm{ord}}(A_C)$; this is the ordered bar sensed by the Yangian. $\mathrm{av} \circ \Phi_{E_1}$ produces $B^{\Sigma}(A_C)$; this is the symmetric bar sensed by the modular characteristic $\kappa_{\mathrm{ch}}$. The full $E_2$ enhancement $\Phi_{E_2}$ produces the Drinfeld-centered bar $B^{E_2}(A_C) = \cZ(B^{\mathrm{ord}}(A_C))$; this is the braided bar sensed by the quantum group. All three factor through $\Phi_{E_1}$. This is the volume's motto: the ordered bar is the primitive.
 \end{remark}
 
 \section{$E_1$-chiral algebras from CY categories}
@@ -153,7 +153,7 @@
 Let $\cC$ be a CY$_3$ category with a chain-level $S^3$-framing on $\mathrm{HC}^-_3(\cC)$ (the condition of Conjecture~CY-A$_3$). Then the ordered bar complex of the cyclic $A_\infty$ algebra $A_\cC$ carries an $E_1$-chiral structure whose representation category is a braided monoidal refinement of the BPS Yangian of $\cC$.
 \end{conjecture}
 
-The conjecture is conditional on the chain-level framing; the unconditional statement requires the full CY-A$_3$ programme. Every downstream result in \ref{part:examples} and \ref{part:connections} that uses the BPS Yangian inherits this conditionality. The connection to Maulik-Okounkov and Costello-Witten cohomological Hall algebras is traced in Chapter~\ref{ch:cha-yangian}.
+The conjecture is conditional on the chain-level framing; the unconditional statement requires the full CY-A$_3$ programme. Every downstream result in \ref{part:examples} and \ref{part:connections} that uses the BPS Yangian inherits this conditionality. The connection to Maulik-Okounkov and Costello-Witten cohomological Hall algebras is traced in Chapter~\ref{ch:toric-coha}.
 
 \begin{proposition}[$E_2$ enhancement via Drinfeld center]
 \label{prop:e2-enhancement-drinfeld}
@@ -318,7 +318,7 @@
 
 \begin{remark}[How this chapter is used downstream]
 \label{rem:downstream-usage}
-Chapters~\ref{ch:braided-factorization}, \ref{ch:drinfeld-center}, and \ref{ch:quantum-group-reps} use this chapter as the source of the ordered bar coalgebra and the averaging map. Chapter~\ref{ch:cy-chiral-functor} uses Proposition~\ref{prop:e1-sector-d2} as the $d=2$ existence statement for $A_\cC$. Every braided monoidal category that appears later is the Drinfeld center of an underlying ordered one.
+Chapters~\ref{ch:braided-factorization}, \ref{ch:drinfeld-center}, and \ref{ch:quantum-group-reps} use this chapter as the source of the ordered bar coalgebra and the averaging map. Chapter~\ref{ch:cy-to-chiral} uses Proposition~\ref{prop:e1-sector-d2} as the $d=2$ existence statement for $A_\cC$. Every braided monoidal category that appears later is the Drinfeld center of an underlying ordered one.
 \end{remark}
 
 \section{Operadic dictionary for the CY reader}
@@ -1447,7 +1447,7 @@
 cutting the elliptic curve.}
 For the product CY$_3$ manifold $X = K3 \times E$, the factorization
 homology integral $\int_{K3} \cF|_{K3}$ of
-Section~\ref{sec:k3-perturbative-fact-homology} produces a chiral algebra
+Section~\ref{subsec:fact-homology-k3xe} produces a chiral algebra
 $A_E$ on the residual elliptic curve $E$.  The coproduct on $A_E$ arises
 from cutting $E$ into two intervals via excision.  Concretely, choose a
 collar-gluing decomposition $E = I_1 \cup_{S^0 \times \R} I_2$ (cutting
diff --git a/chapters/theory/e2_chiral_algebras.tex b/chapters/theory/e2_chiral_algebras.tex
index 4d9c49d33b9b71c9728719844b5387b9c256ec23..8a25a3037dc9569752a97c0fc75347a4033380af
--- a/chapters/theory/e2_chiral_algebras.tex
+++ b/chapters/theory/e2_chiral_algebras.tex
@@ -194,7 +194,7 @@
 \label{sec:drinfeld-center-bridge}
 
 Volume~II constructs $\Phi_{E_1}$ and proves $E_1$-chiral Koszul
-duality (see \ref{part:e1-core} of \cite{VolII}). The Drinfeld center
+duality (see Part~I of \cite{VolII}). The Drinfeld center
 $Z\colon E_1\text{-}\Cat \xrightarrow{\sim} E_2\text{-}\Cat$
 (under dualizability) is the categorical passage from ordered
 monoidal data to braided monoidal data. On the bar side it matches the
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 30392e44f20b6614f1f54981964db6c0329363e5..69d953d96d354add714abf2eec933a753336234a
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -201,7 +201,7 @@
 \]
 The SDR data $(i, p, s)$ interfaces directly with the homotopy transfer theorem (HTT), transferring the $A_\infty$-structure from \v{C}ech cochains $\check{C}^\bullet(\mathcal{E}nd(\mathcal{E}))$ to its cohomology $\mathrm{Ext}^\bullet(\mathcal{E}, \mathcal{E})$. The transferred operations $\mu_k^{\mathrm{ch}}$ are given by sums over planar trees whose internal edges are decorated by the homotopy~$s$; each application of~$s$ introduces rational functions on the affine intersections, and the resulting chiral operations are well-defined as formal power series.
 
-The scope is perturbative: the \v{C}ech homotopy produces an algebraic $A_\infty$-structure on the Ext algebra, but convergence of the resulting series to holomorphic functions (the non-perturbative statement) requires separate input from the analytic completion programme of Volume~I (MC5, \S\ref{sec:analytic-sewing}). The perturbative statement suffices for the formal CY-to-chiral functor and for all combinatorial applications in this volume. The full construction, including the proof that the SDR conditions hold and the scope qualification, is Theorem~\ref{thm:cech-contracting-homotopy} in Chapter~\ref{ch:cy-to-chiral}.
+The scope is perturbative: the \v{C}ech homotopy produces an algebraic $A_\infty$-structure on the Ext algebra, but convergence of the resulting series to holomorphic functions (the non-perturbative statement) requires separate input from the analytic completion programme of Volume~I (MC5, the analytic sewing section there). The perturbative statement suffices for the formal CY-to-chiral functor and for all combinatorial applications in this volume. The full construction, including the proof that the SDR conditions hold and the scope qualification, is Theorem~\ref{thm:cech-contracting-homotopy} in Chapter~\ref{ch:cy-to-chiral}.
 
 Three independent consistency checks confirm the resulting chiral data for the quintic: the Gepner model matrix factorization (via mirror symmetry, $\mathrm{MF}(x_1^5 + \cdots + x_5^5)$), the large-volume Hodge--Kodaira--Rosenberg limit ($\mathrm{HKR}$ degeneration of $\mathrm{Ext}^\bullet$ to Dolbeault cohomology), and the Gopakumar--Vafa integrality of the resulting genus-$g$ amplitudes. All three produce the same modular characteristic $\chi/2 = -100$ (the MacMahon-normalised form of $\kappa_{\mathrm{cat}}$ at $d=3$).
 
@@ -277,7 +277,7 @@
  \item The moonshine multiplier: $A_n = \kappa_{\mathrm{cat}} \cdot \dim(\rho_n)$ identifies the factor $2$ in $Z_{K3} = 2\,\phi_{0,1}$.
  \item The categorical $\Etwo$-obstruction for CY$_3$ (Proposition~\ref{prop:e1-obstruction-categorical}): Serre duality forces antisymmetry of the Euler form, universally obstructing $\Etwo$-enhancement without torus hypotheses.
  \item Quiver-chart gluing for toric CY$_3$ (Theorem~\ref{thm:toric-chart-gluing}): the global $\Eone$-chiral algebra is assembled as a homotopy colimit of McKay-chart CoHAs, with $E_2$ descent degeneration and Costello--Li comparison.
- \item The K3 double current algebra $\fg_{K3}$ (Definition~\ref{def:k3-double-current-algebra}): the finite-dimensional analogue of the DDCA in which $\bC[u,v]$ is replaced by $H^*(S,\bC)$ with the Mukai pairing.
+ \item The K3 double current algebra $\fg_{K3}$: the finite-dimensional analogue of the DDCA in which $\bC[u,v]$ is replaced by $H^*(S,\bC)$ with the Mukai pairing.
  \item Forty-two CY/BKM compute engines with $5{,}700{+}$ tests across the standard CY landscape.
 \end{itemize}
 
@@ -360,7 +360,7 @@
 \item \emph{Descent theorem.}
  \v{C}ech descent for $E_1$-algebras over the Bridgeland
  stability manifold. Proved for toric CY3
- (Proposition~\ref{prop:e1-descent-unobstructed}); open for
+ (Theorem~\ref{thm:toric-chart-gluing}); open for
  compact CY3 beyond the chart-atlas regime.
 \item \emph{Higher-dimensional CY shadows.}
  The $E_n$ stabilization theorem
@@ -394,12 +394,12 @@
 
 \emph{Quantum group representations} (Chapter~\ref{ch:quantum-group-reps}). The representation-theoretic target. The braided monoidal category $\mathrm{Rep}_q(\mathfrak{g})$ is what the CY programme aims to realize: Conjecture~CY-C predicts that $\mathrm{Rep}_q(\mathfrak{g}) \simeq \mathrm{Rep}^{E_2}(A_\cC)$ for a CY category $\cC(\mathfrak{g}, q)$. The Kazhdan--Lusztig equivalence $\mathrm{Rep}_q(\mathfrak{g}) \simeq \mathrm{KL}_k(\mathfrak{g})$ at roots of unity is the prototype: the Volume~I bar complex $B(V_k(\mathfrak{g}))$ encodes the quantum group $R$-matrix in its degree-$(1,1)$ component, and the DK bridge (Volume~II, MC3 for all simple types) recovers the quantum group categorical structure. The affine Yangian realization (Chapter~\ref{ch:toric-coha}) provides the $E_1$-sector; the Drinfeld center (Chapter~\ref{ch:drinfeld-center}) provides the $E_2$-enhancement.
 
-In addition to the four standard families, the toroidal and elliptic algebras chapter (Chapter~\ref{chap:toroidal-elliptic}) develops the $K3 \times E$ programme in full: the generalized root datum, the BKM superalgebra $\mathfrak{g}_{\Delta_5}$ with its Igusa cusp form denominator identity, the shadow--Siegel gap theorem, thirteen structural results (K3-1 through K3-13), all ten research programmes (A through J), and the DDCA--toroidal bridge identifying the deformed double current algebra as the rational degeneration of the quantum toroidal algebra (Conjecture~\ref{conj:ddca-toroidal-bridge}). The K3 double current algebra $\fg_{K3}$ (Chapter~\ref{ch:k3-times-e}, Definition~\ref{def:k3-double-current-algebra}) provides the K3 analogue of the DDCA, replacing $\bC[u,v]$ with $H^*(S,\bC)$. The toric CY$_3$ CoHA chapter (Chapter~\ref{ch:toric-coha}) develops the affine Yangian and $\mathcal{W}_{1+\infty}$ side: the Jordan quiver gives $Y(\widehat{\mathfrak{gl}}_1) \simeq \mathcal{W}_{1+\infty}$, the toric fan is the Dynkin data, and the shuffle algebra presentation connects to the KZ equations of Volume~I.
+In addition to the four standard families, the toroidal and elliptic algebras chapter (Chapter~\ref{chap:toroidal-elliptic}) develops the $K3 \times E$ programme in full: the generalized root datum, the BKM superalgebra $\mathfrak{g}_{\Delta_5}$ with its Igusa cusp form denominator identity, the shadow--Siegel gap theorem, thirteen structural results (K3-1 through K3-13), all ten research programmes (A through J), and the DDCA--toroidal bridge identifying the deformed double current algebra as the rational degeneration of the quantum toroidal algebra (Conjecture~\ref{conj:ddca-toroidal-bridge}). The K3 double current algebra $\fg_{K3}$, discussed in the DDCA--toroidal bridge of Chapter~\ref{ch:k3-times-e}, provides the K3 analogue of the DDCA, replacing $\bC[u,v]$ with $H^*(S,\bC)$. The toric CY$_3$ CoHA chapter (Chapter~\ref{ch:toric-coha}) develops the affine Yangian and $\mathcal{W}_{1+\infty}$ side: the Jordan quiver gives $Y(\widehat{\mathfrak{gl}}_1) \simeq \mathcal{W}_{1+\infty}$, the toric fan is the Dynkin data, and the shuffle algebra presentation connects to the KZ equations of Volume~I.
 
 \section{Guide for the reader}
 \label{sec:guide}
 
-Part~\ref{part:cy-categories} establishes the categorical foundations: CY categories, cyclic $\Ainf$-structures, the Hochschild calculus, and the $E_1$/$E_2$/$E_n$ chiral hierarchy with the framing obstruction tower. Part~\ref{part:bridge} constructs the bridge functor $\Phi$ from CY categories to quantum chiral algebras and proves Theorems CY-A (for $d = 2$) and CY-D, with the identification of automorphic correction and shadow obstruction tower as the central result. Part~\ref{part:examples} treats quantum groups and their braided factorization structure, including the Drinfeld center as the bulk algebra. Part~\ref{part:connections} works through the standard landscape: the toroidal and elliptic algebras chapter develops the $K3 \times E$ programme (K3-1 through K3-13, programmes A through J), alongside toric CY3 CoHAs, Fukaya categories, derived categories, matrix factorizations (ADE singularities and W-algebras), and quantum group representations (Kazhdan--Lusztig, affine Yangians, critical CoHAs). Part~\ref{part:frontier} connects to the geometric Langlands programme and to Volumes~I and~II via the bar-cobar bridge and the modular Koszul bridge. The working notes (\S\ref{sec:working-notes}) record the research frontier.
+Part~\ref{part:cy-categories} establishes the categorical foundations: CY categories, cyclic $\Ainf$-structures, the Hochschild calculus, and the $E_1$/$E_2$/$E_n$ chiral hierarchy with the framing obstruction tower. Part~\ref{part:bridge} constructs the bridge functor $\Phi$ from CY categories to quantum chiral algebras and proves Theorems CY-A (for $d = 2$) and CY-D, with the identification of automorphic correction and shadow obstruction tower as the central result. Part~\ref{part:examples} treats quantum groups and their braided factorization structure, including the Drinfeld center as the bulk algebra. Part~\ref{part:connections} works through the standard landscape: the toroidal and elliptic algebras chapter develops the $K3 \times E$ programme (K3-1 through K3-13, programmes A through J), alongside toric CY3 CoHAs, Fukaya categories, derived categories, matrix factorizations (ADE singularities and W-algebras), and quantum group representations (Kazhdan--Lusztig, affine Yangians, critical CoHAs). Part~\ref{part:frontier} connects to the geometric Langlands programme and to Volumes~I and~II via the bar-cobar bridge and the modular Koszul bridge. The separate working notes record the research frontier.
 
 \section{Conventions and notation}
 \label{sec:conventions-intro}




thinking
**Organizing reference findings**

I need to organize my findings about references, specifically mentioning there are 0 unresolved references and 6 undefined citations remaining. It could be that previously there were 26 broken references, but now it’s down to 0. I should compile an exact list of fixed references, showing each one as either FIXED (how) or BLOCKED (why). 

I want to keep the final answer clean, with 20 unique references, and note any duplicates. It’s important to mention that all unresolved references are fixed and that there are none blocked.
thinking
**Summarizing findings and outcomes**

I don’t need to go into huge detail, but it’s important to group some findings, especially since duplicates appeared. For example, I fixed "def:k3-double-current-algebra" by replacing broken references with plain prose since the merged "toroidal_elliptic.tex" no longer has a live definition label. 

I want to mention verification via build and grep, and I should include a short introductory paragraph followed by a bullet list. It might be helpful to reference main files changed, but a complete inventory isn't necessary. I can finalize with sections like "Outcome" and "Findings."
thinking
**Detailing reference findings**

Since the user asked for details per finding, I think a bullet list will work well. I should avoid nested bullets and keep it simple, aiming for maybe 20 unique broken references.

It's important to summarize command outputs that aren’t visible to the user. I’ll mention that running `make fast` yielded 0 undefined references across four passes. Additionally, checking for forbidden patterns with `rg` returned no matches in the modified files. I’ll also note that I used `grep -rn '\\ref{' chapters/ | head -80` as an initial surface scan, which was effective.
codex
All broken Vol III references that were surfacing in `main.log` are fixed. `make fast` now completes 4 passes with `0 undef refs` and `6 undef cites` remaining. I also grepped the edited files for the exact old broken `\ref{...}` patterns; there were no matches.

Per finding:
- `thm:miura-cross-universality` FIXED by retargeting the preface to `prop:universal-coproduct`.
- `sec:e1-chiral-bialgebra` FIXED by correcting the stale singular label to `sec:e1-chiral-bialgebras`.
- `sec:analytic-sewing` FIXED by replacing both impossible cross-volume refs with plain Vol I prose.
- `def:k3-double-current-algebra` FIXED by removing all stale `Definition~\ref{...}` calls after the K3 material was merged; the text now names the object directly.
- `prop:e1-descent-unobstructed` FIXED by retargeting to the live toric descent theorem `thm:toric-chart-gluing`.
- `sec:working-notes` FIXED by removing the dead cross-document section ref and using plain prose.
- `ch:k3` FIXED by retargeting to `ch:k3-times-e`.
- `ch:coha` FIXED by retargeting to `ch:toric-coha`.
- `thm:topologization` FIXED by replacing the dead Vol I label ref with plain theorem prose.
- `ch:cy-chiral-functor` FIXED by retargeting both occurrences to `ch:cy-to-chiral`.
- `ch:cha-yangian` FIXED by retargeting to `ch:toric-coha`.
- `sec:k3-perturbative-fact-homology` FIXED by retargeting to `subsec:fact-homology-k3xe`.
- `part:e1-core` FIXED by replacing the dead part ref with plain `Part I of \cite{VolII}` prose.
- `thm:htt-general` FIXED by replacing the dead theorem ref with plain HTT prose.
- `subsec:k3-three-algebraizations` FIXED by removing the stale merged-chapter subsection ref and using chapter-level prose.
- `thm:e1-stabilization` FIXED by retargeting to `thm:e1-stabilization-cy`.
- `thm:w-infty-chiral-qg` FIXED by retargeting to `prop:universal-coproduct`.
- `subsec:quantum-chiral-algebras-6d` FIXED by retargeting to `subsec:chiral-qg-wilson`.
- `rem:toric-structural-patterns` FIXED by retargeting to `rem:toric-kappa-patterns`.
- `thm:chiral-qg-equiv` FIXED by removing all three dead Vol I label refs and rewriting them as plain cross-volume prose.
- `ch:toroidal-elliptic` FIXED by correcting it to `chap:toroidal-elliptic`.
- `thm:cy-seven-face-master` FIXED by correcting the claim-state mismatch to `conj:cy-seven-face-master`.
- `part:3d-qg` FIXED by replacing the dead part ref with plain `Part III of Vol. II` prose.

Files changed were the 12 directly affected surfaces in `chapters/` and `chapters/frame/`. No blockers.
file update:
diff --git a/chapters/connections/cy_holographic_datum_master.tex b/chapters/connections/cy_holographic_datum_master.tex
index 2a66e8a0ca86f097e30b0de99c082498014430c6..b0ef34640300f22c24d57ee10a207c331065f31d
--- a/chapters/connections/cy_holographic_datum_master.tex
+++ b/chapters/connections/cy_holographic_datum_master.tex
@@ -943,7 +943,7 @@
 bar-cobar, CoHA / perverse coherent sheaves, classical CY Poisson
 coisson, MO stable envelope, affine super Yangian for toric CY$_3$,
 elliptic Sklyanin for toroidal CY, Gaudin from CY$_3$
-(Theorem~\ref{thm:cy-seven-face-master} above).
+(Conjecture~\ref{conj:cy-seven-face-master} above).
 \end{enumerate}
 The three master theorems are mutually compatible: under the CY-to-chiral
 functor $\Phi$, face~$i$ of Vol~III maps to a specialization of face~$i$
diff --git a/chapters/connections/modular_koszul_bridge.tex b/chapters/connections/modular_koszul_bridge.tex
index 1199c5aaa32e71f085dd3b7131c8f9aeadb1148c..a423d35b2ce162a9f56bb568768ae1bed7bef2f6
--- a/chapters/connections/modular_koszul_bridge.tex
+++ b/chapters/connections/modular_koszul_bridge.tex
@@ -234,7 +234,7 @@
 \end{theorem}
 
 \begin{proof}[Attribution]
-Parts (i), (iii), (iv) are Vol~I/II results (\S\ref{sec:k3e-cross-volume}, items K3-1 through K3-13, proved in the K3 modular-tower chapter of Vol~I and in the Vol~II 3D quantum gravity treatment, \ref{part:3d-qg} there). Part (ii) is the Borcherds lift of Borcherds (1998); its use as a modular characteristic is the observation of AP-CY8, not a theorem of Vol~III. The conditionality on propagates from Theorem~\ref{thm:cy-shadow-cohft}.
+Parts (i), (iii), (iv) are Vol~I/II results (\S\ref{sec:k3e-cross-volume}, items K3-1 through K3-13, proved in the K3 modular-tower chapter of Vol~I and in Part~III of Vol~II's 3D quantum gravity treatment). Part (ii) is the Borcherds lift of Borcherds (1998); its use as a modular characteristic is the observation of AP-CY8, not a theorem of Vol~III. The conditionality on propagates from Theorem~\ref{thm:cy-shadow-cohft}.
 \end{proof}
 
 \begin{remark}[Kappa-spectrum verification for $K3 \times E$]
diff --git a/chapters/examples/quantum_group_reps.tex b/chapters/examples/quantum_group_reps.tex
index e6b19a4c52de09f17af4b5f794d5f7269f4076b4..5213e6bfc9cb828c11c98b50aa32549aa228cfbf
--- a/chapters/examples/quantum_group_reps.tex
+++ b/chapters/examples/quantum_group_reps.tex
@@ -503,7 +503,7 @@
  additional data);
  \item $\kappa_{\mathrm{BKM}}$: the BKM modular weight, a
  number-theoretic invariant arising from the BKM denominator
- formula (Chapter~\ref{ch:toroidal-elliptic}; distinct from
+ formula (Chapter~\ref{chap:toroidal-elliptic}; distinct from
  both $\kappa_{\mathrm{cat}}$ and $\kappa_{\mathrm{ch}}$).
 \end{enumerate}
 For CY$_2$ categories with $\frakg$-symmetry, all three can be
diff --git a/chapters/examples/toric_cy3_coha.tex b/chapters/examples/toric_cy3_coha.tex
index 2b8821c0fd545c77e9d18a4180e8e67d3c4459be..94da66b26dadb3a8dcd2e91287fd7092ea5a944c
--- a/chapters/examples/toric_cy3_coha.tex
+++ b/chapters/examples/toric_cy3_coha.tex
@@ -205,7 +205,7 @@
 \end{theorem}
 
 \begin{proof}
-(i) The compact base $\bP^1 \times \bP^1$ has $\chi(\bP^1 \times \bP^1) = 4$ (each factor contributes $\chi(\bP^1) = 2$), so $\kappa_{\mathrm{ch}} = \chi/2 = 2$ by the general local-surface formula (Remark~\ref{rem:toric-structural-patterns}).
+(i) The compact base $\bP^1 \times \bP^1$ has $\chi(\bP^1 \times \bP^1) = 4$ (each factor contributes $\chi(\bP^1) = 2$), so $\kappa_{\mathrm{ch}} = \chi/2 = 2$ by the general local-surface formula (Remark~\ref{rem:toric-kappa-patterns}).
 
 (ii) The intersection form on $H^2(\bP^1 \times \bP^1)$ in the basis $\{e_1, e_2\}$ is $\langle e_i, e_j \rangle = \delta_{ij}$ (the two rulings are orthogonal with self-intersection $0$ in the total space, but the relevant inner product for the shadow metric is the Euler pairing $\chi(e_i, e_j) = \delta_{ij}$).
 
@@ -654,7 +654,7 @@
 the chart gluing by descent, the shadow tower by the MC equation.
 These components are \emph{a priori} separate structures on the
 same algebra. The Vol~I chiral quantum group equivalence
-(Theorem~\ref{thm:chiral-qg-equiv}) asserts that three of them
+asserts that three of them
 (the vertex $R$-matrix, the chiral $A_\infty$-structure, and the
 chiral coproduct) determine each other on the Koszul locus. The theorem
 below specializes the abstract equivalence to the toric CY3 setting,
@@ -746,8 +746,7 @@
 
 \begin{proof}
 The abstract equivalence (I) $\leftrightarrow$ (II)
-$\leftrightarrow$ (III) is
-Theorem~\ref{thm:chiral-qg-equiv} of Vol~I, proved for any
+$\leftrightarrow$ (III) is the Vol~I chiral quantum group equivalence, proved for any
 $\Eone$-chiral algebra on the Koszul locus. The content of the
 present theorem is the identification of each abstract vertex
 with the independently constructed toric CY3 structure.
@@ -755,7 +754,7 @@
 \textit{Component~\textup{(I)}: $R$-matrix.}
 The $\Eone$-chiral algebra $A_X$ carries a vertex
 $R$-matrix by the general theory
-(Theorem~\ref{thm:chiral-qg-equiv}(I)). For toric CY3, the
+(item~\textup{(I)} of that equivalence). For toric CY3, the
 Maulik--Okounkov stable-envelope construction provides an
 independent $R$-matrix on $Y^+(\widehat{\fg}_{Q_X})$-modules.
 The two coincide because both solve the same Yang--Baxter
diff --git a/chapters/examples/toroidal_elliptic.tex b/chapters/examples/toroidal_elliptic.tex
index 8fcef3a49b8fe0bd45c3ae248676e994ece0ca7e..0a15b2c062f601ea29e50e3e3771b3eb1544db50
--- a/chapters/examples/toroidal_elliptic.tex
+++ b/chapters/examples/toroidal_elliptic.tex
@@ -5940,8 +5940,7 @@
 
 The K3 analogue of this picture replaces $\bC^2$ by a K3
 surface~$S$: the K3 double current algebra $\fg_{K3}$
-(Chapter~\ref{ch:k3-times-e},
-Definition~\ref{def:k3-double-current-algebra}) substitutes
+substitutes
 $H^*(S,\bC)$ for $\bC[u,v]$ and the Mukai pairing for the
 polynomial residue. Its quantization should produce a
 ``K3 Yangian'' standing in the same relation to $\fg_{K3}$ as the
@@ -6018,7 +6017,7 @@
   At $t \to 1$: the second parameter $w$ decouples and
   $\Delta_{z,w}$ reduces to the single-parameter
   Drinfeld coproduct $\Delta_z(T(u)) = T(u) \otimes T(u - z)$
-  of Theorem~\textup{\ref{thm:w-infty-chiral-qg}}.
+  of Proposition~\textup{\ref{prop:universal-coproduct}}.
 \end{enumerate}
 No two-parameter coproduct $\Delta_{z,w}$ currently exists in
 the literature or in this programme's compute infrastructure.
@@ -6034,7 +6033,7 @@
   $(q_1,q_2,q_3)$.
 \item Promote the DDCA shadow to an explicit $\Delta_{z,w}$
   formula aligned with the $R(u,v)$ surface in
-  \S\ref{subsec:quantum-chiral-algebras-6d}.
+  \S\ref{subsec:chiral-qg-wilson}.
 \item Build a compute witness at low modes: $w = 0$ reduces
   to existing $\Delta_z$; rational limit gives the DDCA
   shift; Miki sends $\Delta_{z,w} \to \Delta_{w,z}$.
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index ddbdfe60d9c9df04ba6f3acf48deee73523a64dc..3ce4e679084f2f25672104c7a00684df5e9f3b26
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -320,7 +320,7 @@
 Drinfeld coproduct from spin~$2$ to arbitrary spin, with the
 universal Miura coefficient $(\Psi{-}1)/\Psi$ on the leading
 cross-term $J \otimes W_{s-1}$ at every spin $s \ge 2$
-(Theorem~\ref{thm:miura-cross-universality}).
+(Proposition~\ref{prop:universal-coproduct}).
 
 \bigskip
 
@@ -328,7 +328,7 @@
 Volume~I defines $E_1$-chiral quantum groups abstractly. This
 volume constructs them concretely from CY geometry. The
 $E_1$-chiral bialgebra axioms (formalized in
-\S\ref{sec:e1-chiral-bialgebra}) require: (H1)~an $E_1$-chiral
+\S\ref{sec:e1-chiral-bialgebras}) require: (H1)~an $E_1$-chiral
 algebra $A$ on a curve $X$; (H2)~a spectral coproduct
 $\Delta_z \colon A \to A \otimes A$ (living on the OPEN/$E_1$
 colour); (H3)~an $R$-matrix $R(z)$ satisfying YBE; (H4)~RTT
diff --git a/chapters/theory/cy_categories.tex b/chapters/theory/cy_categories.tex
index f9b51871c44fa18a574c02fce8aaa49a49aa9c61..00d723a1cb5d4f2355a10cb2d9d3f86688259f09
--- a/chapters/theory/cy_categories.tex
+++ b/chapters/theory/cy_categories.tex
@@ -166,7 +166,7 @@
 Every smooth proper CY$_d$ category admits a cyclic $\Ainf$-enhancement, unique up to $\Ainf$-quasi-isomorphism preserving the pairing. The proof is due to Kontsevich--Soibelman in the formal case, Costello~\cite{Costello2005} for the TCFT enhancement, and Seidel~\cite{Seidel2008} for the Fukaya case.
 \end{theorem}
 
-At $d = 2$ the enhancement is explicit enough to compute directly; it drives the $K3$ computations feeding the Borcherds denominator (Vol~III Chapter~\ref{ch:k3}). At $d = 3$ the enhancement was constructed by Sheridan~\cite{Sheridan2015} for the quintic threefold, as part of the HMS proof; the general $d = 3$ construction remains programme-level (conditional on $\bS^3$-framing, see AP-CY6).
+At $d = 2$ the enhancement is explicit enough to compute directly; it drives the $K3$ computations feeding the Borcherds denominator (Vol~III Chapter~\ref{ch:k3-times-e}). At $d = 3$ the enhancement was constructed by Sheridan~\cite{Sheridan2015} for the quintic threefold, as part of the HMS proof; the general $d = 3$ construction remains programme-level (conditional on $\bS^3$-framing, see AP-CY6).
 
 \section{Interface with the CY-to-chiral functor $\Phi$}
 \label{sec:cy-cat-phi-interface}
@@ -194,7 +194,7 @@
 
 \begin{remark}[What $\Phi$ does not see]
 \label{rem:phi-does-not-see}
-Not every invariant of $\cC$ survives the passage through $\Phi$. The functor retains the cyclic $\Ainf$-structure and the Gerstenhaber bracket; it loses the fine structure of the triangulated / $\Ainf$ category (individual objects, t-structures, stability conditions) that is visible only via the fuller categorical CoHA construction of Chapter~\ref{ch:coha}. The kappa-spectrum (Vol~III CLAUDE.md) encodes which invariants survive: $\kappa_\mathrm{cat}$ is always present, $\kappa_\mathrm{ch}$ exists only when $\Phi$ is defined, and $\kappa_\mathrm{BKM}$ records the Borcherds-side lift for $K3 \times E$.
+Not every invariant of $\cC$ survives the passage through $\Phi$. The functor retains the cyclic $\Ainf$-structure and the Gerstenhaber bracket; it loses the fine structure of the triangulated / $\Ainf$ category (individual objects, t-structures, stability conditions) that is visible only via the fuller categorical CoHA construction of Chapter~\ref{ch:toric-coha}. The kappa-spectrum (Vol~III CLAUDE.md) encodes which invariants survive: $\kappa_\mathrm{cat}$ is always present, $\kappa_\mathrm{ch}$ exists only when $\Phi$ is defined, and $\kappa_\mathrm{BKM}$ records the Borcherds-side lift for $K3 \times E$.
 \end{remark}
 
 \begin{remark}[Cross-volume conventions]
diff --git a/chapters/theory/cy_to_chiral.tex b/chapters/theory/cy_to_chiral.tex
index 030fed4a9a2a7009ae05fdb0f3c431c8aed1fc83..14526e0aba63169841056220749304799a57fe10
--- a/chapters/theory/cy_to_chiral.tex
+++ b/chapters/theory/cy_to_chiral.tex
@@ -618,8 +618,8 @@
 homotopy is purely algebraic: it acts by
 $s(f_{i_0 \cdots i_q}) = f_{0 i_0 \cdots i_q}$ on \v{C}ech cochains and
 involves no PDE solving. The SDR data $(i, p, s)$ interfaces directly
-with the homotopy transfer theorem
-\textup{(}HTT, Theorem~\textup{\ref{thm:htt-general}}\textup{)},
+with the standard homotopy transfer theorem
+\textup{(}HTT\textup{)},
 transferring the $\Ainf$-structure from $\check{C}^\bullet(\cE nd(\cE))$
 to its cohomology $\Ext^\bullet(\cE, \cE)$.
 \end{theorem}
@@ -652,7 +652,7 @@
 (whether the formal series in the OPE coefficients converges to
 define honest holomorphic functions) requires separate input from
 the analytic completion programme (MC5,
-\S\ref{sec:analytic-sewing} of Vol~I). Specifically: the HTT
+the analytic sewing section of Vol~I). Specifically: the HTT
 produces transferred operations $\mu_k^{\mathrm{ch}}$ whose
 coefficients involve iterated applications of~$s$; each application
 introduces rational functions on the intersections $U_{i_0} \cap
@@ -1972,7 +1972,7 @@
  \bottomrule
 \end{tabular}
 \end{center}
-{\footnotesize $^*$The K3 entry records $\kappa_{\mathrm{ch}} = \chi(\cO_{\mathrm{K3}}) = 2$ (Proposition~\ref{prop:cy-kappa-d2}; verified via chiral de Rham, Chapter~\ref{ch:k3-times-e}). The distinct quantity $\dim \HH_*(D^b(\mathrm{K3}))/2 = 12$ arises from an alternative algebraization (the Monster orbifold); the full trichotomy ($\kappa_{\mathrm{ch}} \in \{2, 12, 24\}$) is developed in Section~\ref{subsec:k3-three-algebraizations} of Chapter~\ref{ch:k3-times-e}.
+{\footnotesize $^*$The K3 entry records $\kappa_{\mathrm{ch}} = \chi(\cO_{\mathrm{K3}}) = 2$ (Proposition~\ref{prop:cy-kappa-d2}; verified via chiral de Rham, Chapter~\ref{ch:k3-times-e}). The distinct quantity $\dim \HH_*(D^b(\mathrm{K3}))/2 = 12$ arises from an alternative algebraization (the Monster orbifold); the full trichotomy ($\kappa_{\mathrm{ch}} \in \{2, 12, 24\}$) is developed in the K3 discussion of Chapter~\ref{ch:k3-times-e}.
 
 $^\dagger$The $K3 \times E$ entry records $\kappa_{\mathrm{ch}} = 3$ by additivity (Proposition~\ref{prop:categorical-euler}: $\kappa_{\mathrm{ch}}(\mathrm{K3}) + \kappa_{\mathrm{ch}}(E) = 2 + 1$). The Borcherds automorphic weight is $\kappa_{\mathrm{BKM}} = 5 = \mathrm{wt}(\Delta_5)$, a distinct invariant.}
 
diff --git a/chapters/theory/drinfeld_center.tex b/chapters/theory/drinfeld_center.tex
index ac67d4e3a2ed8fab94fcb3fc63933d8650a92ac9..a711d853438f9e6a0e6fdd4e5dac61154b7b3c24
--- a/chapters/theory/drinfeld_center.tex
+++ b/chapters/theory/drinfeld_center.tex
@@ -726,7 +726,7 @@
 produces only symmetric braiding. The distinction is the
 deep reason for the $\Eone$ stabilization theorem
 (Chapter~\ref{ch:cy-to-chiral},
-Theorem~\ref{thm:e1-stabilization}).
+Theorem~\ref{thm:e1-stabilization-cy}).
 
 \begin{proposition}[$E_3$ restriction gives symmetric braiding]
 \label{prop:e3-symmetric-braiding}
diff --git a/chapters/theory/e1_chiral_algebras.tex b/chapters/theory/e1_chiral_algebras.tex
index 75484d2fff759dc21313b5595a8abade7d55d203..b533b2f5640db9eba4046a61106787f2c19a0d53
--- a/chapters/theory/e1_chiral_algebras.tex
+++ b/chapters/theory/e1_chiral_algebras.tex
@@ -63,7 +63,7 @@
 via holomorphic Chern--Simons; conjectural in general).
 The further $E_3$-topological upgrade requires a conformal
 vector at non-critical level
-(Volume~I, Theorem~\textup{\ref*{thm:topologization}}).
+(Volume~I, the topologization theorem).
 \end{definition}
 
 The closed colour carries $E_2$ structure from
@@ -128,7 +128,7 @@
 
 \begin{remark}[Three bars, one functor]
 \label{rem:three-bars-vol3}
-The CY-to-chiral functor $\Phi$ of Chapter~\ref{ch:cy-chiral-functor} has three natural composites. $\Phi_{E_1}$ produces $B^{\mathrm{ord}}(A_C)$; this is the ordered bar sensed by the Yangian. $\mathrm{av} \circ \Phi_{E_1}$ produces $B^{\Sigma}(A_C)$; this is the symmetric bar sensed by the modular characteristic $\kappa_{\mathrm{ch}}$. The full $E_2$ enhancement $\Phi_{E_2}$ produces the Drinfeld-centered bar $B^{E_2}(A_C) = \cZ(B^{\mathrm{ord}}(A_C))$; this is the braided bar sensed by the quantum group. All three factor through $\Phi_{E_1}$. This is the volume's motto: the ordered bar is the primitive.
+The CY-to-chiral functor $\Phi$ of Chapter~\ref{ch:cy-to-chiral} has three natural composites. $\Phi_{E_1}$ produces $B^{\mathrm{ord}}(A_C)$; this is the ordered bar sensed by the Yangian. $\mathrm{av} \circ \Phi_{E_1}$ produces $B^{\Sigma}(A_C)$; this is the symmetric bar sensed by the modular characteristic $\kappa_{\mathrm{ch}}$. The full $E_2$ enhancement $\Phi_{E_2}$ produces the Drinfeld-centered bar $B^{E_2}(A_C) = \cZ(B^{\mathrm{ord}}(A_C))$; this is the braided bar sensed by the quantum group. All three factor through $\Phi_{E_1}$. This is the volume's motto: the ordered bar is the primitive.
 \end{remark}
 
 \section{$E_1$-chiral algebras from CY categories}
@@ -153,7 +153,7 @@
 Let $\cC$ be a CY$_3$ category with a chain-level $S^3$-framing on $\mathrm{HC}^-_3(\cC)$ (the condition of Conjecture~CY-A$_3$). Then the ordered bar complex of the cyclic $A_\infty$ algebra $A_\cC$ carries an $E_1$-chiral structure whose representation category is a braided monoidal refinement of the BPS Yangian of $\cC$.
 \end{conjecture}
 
-The conjecture is conditional on the chain-level framing; the unconditional statement requires the full CY-A$_3$ programme. Every downstream result in \ref{part:examples} and \ref{part:connections} that uses the BPS Yangian inherits this conditionality. The connection to Maulik-Okounkov and Costello-Witten cohomological Hall algebras is traced in Chapter~\ref{ch:cha-yangian}.
+The conjecture is conditional on the chain-level framing; the unconditional statement requires the full CY-A$_3$ programme. Every downstream result in \ref{part:examples} and \ref{part:connections} that uses the BPS Yangian inherits this conditionality. The connection to Maulik-Okounkov and Costello-Witten cohomological Hall algebras is traced in Chapter~\ref{ch:toric-coha}.
 
 \begin{proposition}[$E_2$ enhancement via Drinfeld center]
 \label{prop:e2-enhancement-drinfeld}
@@ -318,7 +318,7 @@
 
 \begin{remark}[How this chapter is used downstream]
 \label{rem:downstream-usage}
-Chapters~\ref{ch:braided-factorization}, \ref{ch:drinfeld-center}, and \ref{ch:quantum-group-reps} use this chapter as the source of the ordered bar coalgebra and the averaging map. Chapter~\ref{ch:cy-chiral-functor} uses Proposition~\ref{prop:e1-sector-d2} as the $d=2$ existence statement for $A_\cC$. Every braided monoidal category that appears later is the Drinfeld center of an underlying ordered one.
+Chapters~\ref{ch:braided-factorization}, \ref{ch:drinfeld-center}, and \ref{ch:quantum-group-reps} use this chapter as the source of the ordered bar coalgebra and the averaging map. Chapter~\ref{ch:cy-to-chiral} uses Proposition~\ref{prop:e1-sector-d2} as the $d=2$ existence statement for $A_\cC$. Every braided monoidal category that appears later is the Drinfeld center of an underlying ordered one.
 \end{remark}
 
 \section{Operadic dictionary for the CY reader}
@@ -1447,7 +1447,7 @@
 cutting the elliptic curve.}
 For the product CY$_3$ manifold $X = K3 \times E$, the factorization
 homology integral $\int_{K3} \cF|_{K3}$ of
-Section~\ref{sec:k3-perturbative-fact-homology} produces a chiral algebra
+Section~\ref{subsec:fact-homology-k3xe} produces a chiral algebra
 $A_E$ on the residual elliptic curve $E$.  The coproduct on $A_E$ arises
 from cutting $E$ into two intervals via excision.  Concretely, choose a
 collar-gluing decomposition $E = I_1 \cup_{S^0 \times \R} I_2$ (cutting
diff --git a/chapters/theory/e2_chiral_algebras.tex b/chapters/theory/e2_chiral_algebras.tex
index 4d9c49d33b9b71c9728719844b5387b9c256ec23..8a25a3037dc9569752a97c0fc75347a4033380af
--- a/chapters/theory/e2_chiral_algebras.tex
+++ b/chapters/theory/e2_chiral_algebras.tex
@@ -194,7 +194,7 @@
 \label{sec:drinfeld-center-bridge}
 
 Volume~II constructs $\Phi_{E_1}$ and proves $E_1$-chiral Koszul
-duality (see \ref{part:e1-core} of \cite{VolII}). The Drinfeld center
+duality (see Part~I of \cite{VolII}). The Drinfeld center
 $Z\colon E_1\text{-}\Cat \xrightarrow{\sim} E_2\text{-}\Cat$
 (under dualizability) is the categorical passage from ordered
 monoidal data to braided monoidal data. On the bar side it matches the
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 30392e44f20b6614f1f54981964db6c0329363e5..69d953d96d354add714abf2eec933a753336234a
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -201,7 +201,7 @@
 \]
 The SDR data $(i, p, s)$ interfaces directly with the homotopy transfer theorem (HTT), transferring the $A_\infty$-structure from \v{C}ech cochains $\check{C}^\bullet(\mathcal{E}nd(\mathcal{E}))$ to its cohomology $\mathrm{Ext}^\bullet(\mathcal{E}, \mathcal{E})$. The transferred operations $\mu_k^{\mathrm{ch}}$ are given by sums over planar trees whose internal edges are decorated by the homotopy~$s$; each application of~$s$ introduces rational functions on the affine intersections, and the resulting chiral operations are well-defined as formal power series.
 
-The scope is perturbative: the \v{C}ech homotopy produces an algebraic $A_\infty$-structure on the Ext algebra, but convergence of the resulting series to holomorphic functions (the non-perturbative statement) requires separate input from the analytic completion programme of Volume~I (MC5, \S\ref{sec:analytic-sewing}). The perturbative statement suffices for the formal CY-to-chiral functor and for all combinatorial applications in this volume. The full construction, including the proof that the SDR conditions hold and the scope qualification, is Theorem~\ref{thm:cech-contracting-homotopy} in Chapter~\ref{ch:cy-to-chiral}.
+The scope is perturbative: the \v{C}ech homotopy produces an algebraic $A_\infty$-structure on the Ext algebra, but convergence of the resulting series to holomorphic functions (the non-perturbative statement) requires separate input from the analytic completion programme of Volume~I (MC5, the analytic sewing section there). The perturbative statement suffices for the formal CY-to-chiral functor and for all combinatorial applications in this volume. The full construction, including the proof that the SDR conditions hold and the scope qualification, is Theorem~\ref{thm:cech-contracting-homotopy} in Chapter~\ref{ch:cy-to-chiral}.
 
 Three independent consistency checks confirm the resulting chiral data for the quintic: the Gepner model matrix factorization (via mirror symmetry, $\mathrm{MF}(x_1^5 + \cdots + x_5^5)$), the large-volume Hodge--Kodaira--Rosenberg limit ($\mathrm{HKR}$ degeneration of $\mathrm{Ext}^\bullet$ to Dolbeault cohomology), and the Gopakumar--Vafa integrality of the resulting genus-$g$ amplitudes. All three produce the same modular characteristic $\chi/2 = -100$ (the MacMahon-normalised form of $\kappa_{\mathrm{cat}}$ at $d=3$).
 
@@ -277,7 +277,7 @@
  \item The moonshine multiplier: $A_n = \kappa_{\mathrm{cat}} \cdot \dim(\rho_n)$ identifies the factor $2$ in $Z_{K3} = 2\,\phi_{0,1}$.
  \item The categorical $\Etwo$-obstruction for CY$_3$ (Proposition~\ref{prop:e1-obstruction-categorical}): Serre duality forces antisymmetry of the Euler form, universally obstructing $\Etwo$-enhancement without torus hypotheses.
  \item Quiver-chart gluing for toric CY$_3$ (Theorem~\ref{thm:toric-chart-gluing}): the global $\Eone$-chiral algebra is assembled as a homotopy colimit of McKay-chart CoHAs, with $E_2$ descent degeneration and Costello--Li comparison.
- \item The K3 double current algebra $\fg_{K3}$ (Definition~\ref{def:k3-double-current-algebra}): the finite-dimensional analogue of the DDCA in which $\bC[u,v]$ is replaced by $H^*(S,\bC)$ with the Mukai pairing.
+ \item The K3 double current algebra $\fg_{K3}$: the finite-dimensional analogue of the DDCA in which $\bC[u,v]$ is replaced by $H^*(S,\bC)$ with the Mukai pairing.
  \item Forty-two CY/BKM compute engines with $5{,}700{+}$ tests across the standard CY landscape.
 \end{itemize}
 
@@ -360,7 +360,7 @@
 \item \emph{Descent theorem.}
  \v{C}ech descent for $E_1$-algebras over the Bridgeland
  stability manifold. Proved for toric CY3
- (Proposition~\ref{prop:e1-descent-unobstructed}); open for
+ (Theorem~\ref{thm:toric-chart-gluing}); open for
  compact CY3 beyond the chart-atlas regime.
 \item \emph{Higher-dimensional CY shadows.}
  The $E_n$ stabilization theorem
@@ -394,12 +394,12 @@
 
 \emph{Quantum group representations} (Chapter~\ref{ch:quantum-group-reps}). The representation-theoretic target. The braided monoidal category $\mathrm{Rep}_q(\mathfrak{g})$ is what the CY programme aims to realize: Conjecture~CY-C predicts that $\mathrm{Rep}_q(\mathfrak{g}) \simeq \mathrm{Rep}^{E_2}(A_\cC)$ for a CY category $\cC(\mathfrak{g}, q)$. The Kazhdan--Lusztig equivalence $\mathrm{Rep}_q(\mathfrak{g}) \simeq \mathrm{KL}_k(\mathfrak{g})$ at roots of unity is the prototype: the Volume~I bar complex $B(V_k(\mathfrak{g}))$ encodes the quantum group $R$-matrix in its degree-$(1,1)$ component, and the DK bridge (Volume~II, MC3 for all simple types) recovers the quantum group categorical structure. The affine Yangian realization (Chapter~\ref{ch:toric-coha}) provides the $E_1$-sector; the Drinfeld center (Chapter~\ref{ch:drinfeld-center}) provides the $E_2$-enhancement.
 
-In addition to the four standard families, the toroidal and elliptic algebras chapter (Chapter~\ref{chap:toroidal-elliptic}) develops the $K3 \times E$ programme in full: the generalized root datum, the BKM superalgebra $\mathfrak{g}_{\Delta_5}$ with its Igusa cusp form denominator identity, the shadow--Siegel gap theorem, thirteen structural results (K3-1 through K3-13), all ten research programmes (A through J), and the DDCA--toroidal bridge identifying the deformed double current algebra as the rational degeneration of the quantum toroidal algebra (Conjecture~\ref{conj:ddca-toroidal-bridge}). The K3 double current algebra $\fg_{K3}$ (Chapter~\ref{ch:k3-times-e}, Definition~\ref{def:k3-double-current-algebra}) provides the K3 analogue of the DDCA, replacing $\bC[u,v]$ with $H^*(S,\bC)$. The toric CY$_3$ CoHA chapter (Chapter~\ref{ch:toric-coha}) develops the affine Yangian and $\mathcal{W}_{1+\infty}$ side: the Jordan quiver gives $Y(\widehat{\mathfrak{gl}}_1) \simeq \mathcal{W}_{1+\infty}$, the toric fan is the Dynkin data, and the shuffle algebra presentation connects to the KZ equations of Volume~I.
+In addition to the four standard families, the toroidal and elliptic algebras chapter (Chapter~\ref{chap:toroidal-elliptic}) develops the $K3 \times E$ programme in full: the generalized root datum, the BKM superalgebra $\mathfrak{g}_{\Delta_5}$ with its Igusa cusp form denominator identity, the shadow--Siegel gap theorem, thirteen structural results (K3-1 through K3-13), all ten research programmes (A through J), and the DDCA--toroidal bridge identifying the deformed double current algebra as the rational degeneration of the quantum toroidal algebra (Conjecture~\ref{conj:ddca-toroidal-bridge}). The K3 double current algebra $\fg_{K3}$, discussed in the DDCA--toroidal bridge of Chapter~\ref{ch:k3-times-e}, provides the K3 analogue of the DDCA, replacing $\bC[u,v]$ with $H^*(S,\bC)$. The toric CY$_3$ CoHA chapter (Chapter~\ref{ch:toric-coha}) develops the affine Yangian and $\mathcal{W}_{1+\infty}$ side: the Jordan quiver gives $Y(\widehat{\mathfrak{gl}}_1) \simeq \mathcal{W}_{1+\infty}$, the toric fan is the Dynkin data, and the shuffle algebra presentation connects to the KZ equations of Volume~I.
 
 \section{Guide for the reader}
 \label{sec:guide}
 
-Part~\ref{part:cy-categories} establishes the categorical foundations: CY categories, cyclic $\Ainf$-structures, the Hochschild calculus, and the $E_1$/$E_2$/$E_n$ chiral hierarchy with the framing obstruction tower. Part~\ref{part:bridge} constructs the bridge functor $\Phi$ from CY categories to quantum chiral algebras and proves Theorems CY-A (for $d = 2$) and CY-D, with the identification of automorphic correction and shadow obstruction tower as the central result. Part~\ref{part:examples} treats quantum groups and their braided factorization structure, including the Drinfeld center as the bulk algebra. Part~\ref{part:connections} works through the standard landscape: the toroidal and elliptic algebras chapter develops the $K3 \times E$ programme (K3-1 through K3-13, programmes A through J), alongside toric CY3 CoHAs, Fukaya categories, derived categories, matrix factorizations (ADE singularities and W-algebras), and quantum group representations (Kazhdan--Lusztig, affine Yangians, critical CoHAs). Part~\ref{part:frontier} connects to the geometric Langlands programme and to Volumes~I and~II via the bar-cobar bridge and the modular Koszul bridge. The working notes (\S\ref{sec:working-notes}) record the research frontier.
+Part~\ref{part:cy-categories} establishes the categorical foundations: CY categories, cyclic $\Ainf$-structures, the Hochschild calculus, and the $E_1$/$E_2$/$E_n$ chiral hierarchy with the framing obstruction tower. Part~\ref{part:bridge} constructs the bridge functor $\Phi$ from CY categories to quantum chiral algebras and proves Theorems CY-A (for $d = 2$) and CY-D, with the identification of automorphic correction and shadow obstruction tower as the central result. Part~\ref{part:examples} treats quantum groups and their braided factorization structure, including the Drinfeld center as the bulk algebra. Part~\ref{part:connections} works through the standard landscape: the toroidal and elliptic algebras chapter develops the $K3 \times E$ programme (K3-1 through K3-13, programmes A through J), alongside toric CY3 CoHAs, Fukaya categories, derived categories, matrix factorizations (ADE singularities and W-algebras), and quantum group representations (Kazhdan--Lusztig, affine Yangians, critical CoHAs). Part~\ref{part:frontier} connects to the geometric Langlands programme and to Volumes~I and~II via the bar-cobar bridge and the modular Koszul bridge. The separate working notes record the research frontier.
 
 \section{Conventions and notation}
 \label{sec:conventions-intro}

tokens used
248,272
