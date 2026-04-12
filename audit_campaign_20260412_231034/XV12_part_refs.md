# XV12_part_refs (579s, gpt-5.4)

- [CRITICAL] Vol I [concordance.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:3796) — `Volume~II's Part~VII` is numerically wrong. Vol II `main.tex` places ordered associative chiral Koszul duality, the dg-shifted factorization bridge, and the gravitational Yangian in Part II (`part:e1-core`), not Part VII.
- [CRITICAL] Vol I [ordered_associative_chiral_kd.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/ordered_associative_chiral_kd.tex:7549) — bare `Part~VII` is impossible locally: Vol I has only six parts, so this reference is both hardcoded and ambiguous/wrong.
- [CRITICAL] Vol III [cy_holographic_datum_master.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/connections/cy_holographic_datum_master.tex:922) — `Vol~I Part~III` is wrong in the seven-face bridge. Vol I’s seven-face programme is Part V (`part:seven-faces`), not Part III.
- [CRITICAL] Vol III [cy_holographic_datum_master.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/connections/cy_holographic_datum_master.tex:931) — same wrong Vol I numbering repeated in the enumerated summary: `Vol~I, Part~III` should point to Vol I Part V.
- [CRITICAL] Vol III [toroidal_elliptic.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:5492) — stale `Chapter~66`. The cited labels `sec:k3-sigma-model` and `sec:grand-synthesis-k3xe` now live in Vol III `toroidal_elliptic.tex`; this chapter number survived the move from Vol I.

- [HIGH] Vol III [k3_times_e.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3_times_e.tex:966) — duplicate stale `Chapter~66` in the merged-out `k3_times_e` surface; same migration drift as `toroidal_elliptic.tex`.
- [HIGH] Vol I [thqg_introduction_supplement_body.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_introduction_supplement_body.tex:1620) — hardcoded `Part~VII` is wrong locally; Vol I frontier is Part VI (`part:v1-frontier`).
- [HIGH] Vol I [thqg_preface_supplement.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_preface_supplement.tex:2017) — mixed dynamic/hardcoded range `Parts~\ref{part:seven-faces}--VII`; the upper endpoint should be a `\ref` to the frontier part, not literal `VII`.
- [HIGH] Vol I [thqg_preface_supplement.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_preface_supplement.tex:2055) — hardcoded `Part~VII` again; should point to Vol I frontier Part VI.
- [HIGH] Vol I [ordered_associative_chiral_kd.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/ordered_associative_chiral_kd.tex:5970) — hardcoded cross-volume `Volume~II, Part~VI`; should cite Vol II `part:gravity`.
- [HIGH] Vol I [ordered_associative_chiral_kd.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/ordered_associative_chiral_kd.tex:7752) — hardcoded cross-volume `Volume~II, Part~VII`; should cite Vol II `part:frontier`.
- [HIGH] Vol I [frontier_modular_holography_platonic.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/frontier_modular_holography_platonic.tex:1788) — hardcoded cross-volume `Vol~II, Part~IV`; should cite Vol II `part:examples`.
- [HIGH] Vol II [conclusion.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/conclusion.tex:987) — subsection title hardcodes `Part~VII` instead of using the local part label `part:frontier`.
- [HIGH] Vol II [conclusion.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/conclusion.tex:990) — hardcoded `Part~VII` and `Parts~I--VI`; both should be label-based (`part:frontier` and `part:swiss-cheese`--`part:gravity`).
- [HIGH] Vol III [introduction.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/introduction.tex:34) — hardcoded `Volume~II, Part~III`; should cite Vol II `part:bbl-core`.
- [HIGH] Vol III [introduction.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/introduction.tex:157) — hardcoded `Volume~I, Part~II`; should cite Vol I `part:characteristic-datum`.
- [HIGH] Vol III [quantum_group_reps.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:342) — hardcoded `Volume~II, Part~III`; should cite Vol II `part:bbl-core`.
- [HIGH] Vol III [quantum_group_reps.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:546) — hardcoded `Volume~I, Part~II`; should cite Vol I `part:characteristic-datum`.
- [HIGH] Vol III [toroidal_elliptic.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:94) — hardcoded `Vol~I, Part~I`; should cite Vol I `part:bar-complex`.
- [HIGH] Vol III [cy_holographic_datum_master.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/connections/cy_holographic_datum_master.tex:936) — hardcoded `Vol~II, Part~III`; should cite Vol II `part:bbl-core`.
- [HIGH] Vol III [cy_holographic_datum_master.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/connections/cy_holographic_datum_master.tex:1009) — internal `Part~V` is hardcoded; this should use Vol III `part:frontier`.
- [HIGH] Vol III [braided_factorization.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/braided_factorization.tex:89) — hardcoded `Volume~II, Chapter~11`; this should use a chapter label, not a literal chapter number.

- [MEDIUM] Vol II [dnp_identification_master.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/dnp_identification_master.tex:540) — raw label text `Chapter~\texttt{ch:genus1-seven-faces}` leaked into prose; should be `Chapter~\ref{ch:genus1-seven-faces}`.
- [MEDIUM] Vol III [cy_holographic_datum_master.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/connections/cy_holographic_datum_master.tex:1006) — same raw-label leak: `Chapter~\texttt{ch:genus1-seven-faces}` instead of `Chapter~\ref{ch:genus1-seven-faces}`.

Filtered out as non-violations: literature citations like `\cite[Chapter~5]{...}`, already-dynamic `Part~\ref{...}` / `Chapter~\ref{...}` references, and theorem-part markers like `Part~(i)` or `Part~A`.

## Summary
Instances checked: 28 | Violations found: 24 | Verdict: FAIL


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
session id: 019d83bd-5960-79d2-a37f-2a7ee2176086
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


MISSION: Cross-volume consistency check for Part/Chapter references.

Are there hardcoded Part~/Chapter~ references that should be \ref{part:...}? Check all 3 repos.

Search across ALL three repos:
- ~/chiral-bar-cobar/chapters/
- ~/chiral-bar-cobar-vol2/chapters/
- ~/calabi-yau-quantum-groups/chapters/

For each finding, note: which volume, file:line, the inconsistency, and severity.
mcp startup: no servers


thinking
**Considering task execution**

I think we likely need to use the update_plan since the task is substantial. I need to incorporate commentary and utilize exec commands, possibly in parallel. There’s also the thought of using an explorer sub-agent, which might not be necessary though. 

I should check if I can use rg commands across three repositories. I’ll inspect AGENTS to confirm and determine if I can read files from sibling repos, as policy might allow some readings. Let’s try executing it.
thinking
**Defining hardcoded references**

The user specifically asks for hardcoded references for Part and Chapter markers. I need to search for patterns that identify what counts as a hardcoded reference, which should be in the format \ref{part:...}. 

I'll look for "Part" and "Chapter" in the .tex files under the chapters across all three repositories. It's likely that I should exclude uses like "Part\ref{...}" since those may not be considered hardcoded references. Let's refine this search approach!
codex
Using `deep-beilinson-audit` for a read-only falsification pass on cross-volume `Part~`/`Chapter~` references. I’m starting with a global grep across the three `chapters/` trees, then I’ll inspect each hit in context and keep only genuine hardcoded references.
exec
/bin/zsh -lc "rg -n --glob '*.tex' 'Part~|Chapter~' /Users/raeez/chiral-bar-cobar/chapters /Users/raeez/chiral-bar-cobar-vol2/chapters /Users/raeez/calabi-yau-quantum-groups/chapters" in /Users/raeez/chiral-bar-cobar succeeded in 68ms:
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:1881:Part~\ref{part:e1-core}\@.
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:3935:to be infinite. Part~(v) follows from PBW universality
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:4046:Part~(i) is
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:4048:Part~(ii) is
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:4052:Part~(iii) packages the separately proved genus-$1$ analogues of the
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:4700:\textup{(}Chapter~$4$, the connection on the
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:5718: & (Part~\ref{part:e1-core})
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:5720: & (Part~\ref{part:e1-core})
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:5722: & (Part~\ref{part:e1-core}) \\
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:5773:the full treatment is in Part~\ref{part:e1-core}\@.
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/cy_holographic_datum_master.tex:202:(cf.\ Chapter~\ref{ch:quantum-chiral-algebras},
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/cy_holographic_datum_master.tex:242:Chapter~\ref{ch:k3-times-e}. AP-CY8 forbids calling this an identity at
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/cy_holographic_datum_master.tex:252:CY$_3$ without compact $4$-cycles (Chapter~\ref{ch:toric-coha}) this is
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/cy_holographic_datum_master.tex:390:(Chapter~\ref{ch:cy-to-chiral}). The PVA structure on $A_\cC^{\mathrm{cl}}$
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/cy_holographic_datum_master.tex:922:This part of Vol~III mirrors Vol~I Part~III and Vol~II Part~III. The
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/cy_holographic_datum_master.tex:931:\item \emph{Vol~I, Part~III:} the binary collision residue of a chiral
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/cy_holographic_datum_master.tex:936:\item \emph{Vol~II, Part~III:} the binary collision residue of a
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/cy_holographic_datum_master.tex:1006:in Vol~I, Chapter~\texttt{ch:genus1-seven-faces}.
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/cy_holographic_datum_master.tex:1009:Vol~III. Subsequent chapters in Part~V record the geometric Langlands
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex:4:A CY category $\cC$ produces, via the CY-to-chiral functor $\Phi$ of Chapter~\ref{ch:cy-to-chiral}, a chiral algebra $A_\cC$; the bar complex $B(A_\cC) = T^c(s^{-1}\overline{A_\cC})$, built on the augmentation ideal $\overline{A_\cC} = \ker(\varepsilon)$, is a factorization coalgebra on $\Ran(C)$. Three Volume~I structures act on $B(A_\cC)$. The Verdier intertwining $D_{\Ran}(B(A)) \simeq B(A^!)$ of Theorem~A is a functor of factorization coalgebras on $\Ran(C)$; it is the Koszul duality, not bar-cobar inversion, and not the chiral derived center. Complementarity (Theorem~C) splits the genus-$g$ shadow complex into Verdier eigenspaces and, on the uniform-weight lane, equates the scalar sum of Koszul-dual modular characteristics to a family-dependent Koszul conductor. The genus tower (Theorem~D) identifies $\mathrm{obs}_g$ with $\kappa_{\mathrm{ch}} \cdot \lambda_g$ on the uniform-weight lane at genus $1$ unconditionally, with a cross-channel correction $\delta F_g^{\mathrm{cross}}$ at $g \geq 2$ for multi-weight algebras. Vol~III inherits three deficiencies. First, the convolution dg Lie algebra living on $\overline{\cM}_{g,n}$ has no existing CY-side habitat. Second, the Vol~I scalar complementarity (Vol~I Theorem~C$_2$, with its family-dependent Koszul conductor; see Remark~\ref{rem:cy-complementarity-kappa-zero} below) has no CY translation stating which Koszul conductor $K_X$ applies at $d \in \{2, 3\}$. Third, the Vol~I CohFT promotion (Theorem~D$+$H) has no CY restatement tracking the flat identity axiom through $\Phi$. Five sections address these deficiencies and their consequences: \S\ref{sec:modular-conv-cy} builds the CY modular convolution algebra; \S\ref{sec:cy-complementarity-bridge} transports complementarity with explicit (C1) versus (C2) scoping and explicit $d = 2$ versus $d = 3$ conditionality; \S\ref{sec:cy-shadow-cohft} upgrades the shadow tower to a CohFT on $\overline{\cM}_{g,n}$ and records how the Borcherds lift converts the $K3 \times E$ tower into the genus-$2$ Igusa cusp form $\Phi_{10}$; \S\ref{sec:hochschild-bridge} establishes the bridge between the three Hochschild theories (categorical, chiral, derived-center) through $\Phi$; and \S\ref{sec:cy-bridge-examples} collects the principal examples with their $\kappa_\bullet$-spectra.
codex
The raw hit set is noisy: most `Part~(i)`/`Chapter~\ref{...}` occurrences are theorem-part markers or already dynamic references. I’m narrowing to genuinely hardcoded internal structure references: literal part names/numbers/roman numerals or literal chapter numbers inside the three `chapters/` trees.
Plan update
Global grep is complete. Next I’m filtering to candidate hardcoded structural references, then validating each candidate in file context before reporting only genuine violations.
  → Filter raw Part~/Chapter~ hits to hardcoded structural-reference candidates
  • Read each candidate in context across all three volumes
  • Re-verify findings and produce severity-ordered audit report

thinking
**Filtering and searching carefully**

I think I need to approach this task by filtering information carefully. It’s manageable if I take the time to ensure I’m searching in the right way, so I can find relevant insights. I’m curious about how I can refine my search process to make it more effective. There might be tools or strategies that could help me sift through the data more efficiently while maintaining quality.
exec
/bin/zsh -lc "python - <<'PY'
import re, pathlib
roots = [pathlib.Path('/Users/raeez/chiral-bar-cobar/chapters'), pathlib.Path('/Users/raeez/chiral-bar-cobar-vol2/chapters'), pathlib.Path('/Users/raeez/calabi-yau-quantum-groups/chapters')]
part_pat = re.compile(r'Part~(?"'!('"\\\\ref|\\\\textup\\{\\\\ref))(?"'!('"\\())(?"'!('"\\\\\\())(?"'!('"\\\\textup\\{\\())(?P<val>\\"'$?[IVXLCDM0-9A-Z]+'"\\"'$?)'"')
chap_pat = re.compile(r'Chapter~(?"'!('"\\\\ref|\\\\textup\\{\\\\ref))(?"'!('"\\())(?"'!('"\\\\\\())(?"'!('"\\\\textup\\{\\())(?"'!('"\\\\[A-Za-z]))(?P<val>\\"'$?[IVXLCDM0-9A-Z]+'"\\"'$?|'"\\\\texttt\\{["'^}]+'"\\})')
for root in roots:
    print('ROOT', root)
    for path in root.rglob('*.tex'):
        try:
            text = path.read_text()
        except Exception:
            continue
        for i, line in enumerate(text.splitlines(), 1):
            if 'Part~' in line:
                m = part_pat.search(line)
                if m:
                    print(f'PART {path}:{i}: {line.strip()}')
            if 'Chapter~' in line:
                m = chap_pat.search(line)
                if m:
                    print(f'CHAP {path}:{i}: {line.strip()}')
PY" in /Users/raeez/chiral-bar-cobar exited 127 in 52ms:
zsh:1: command not found: python
codex
The first filter command failed because this shell only has `python3`, not `python`. I’m rerunning the structural filter with `python3` so I can separate true hardcoded references from theorem-part noise.
exec
/bin/zsh -lc "python3 - <<'PY'
import re, pathlib
roots = [pathlib.Path('/Users/raeez/chiral-bar-cobar/chapters'), pathlib.Path('/Users/raeez/chiral-bar-cobar-vol2/chapters'), pathlib.Path('/Users/raeez/calabi-yau-quantum-groups/chapters')]
part_pat = re.compile(r'Part~(?"'!(?:'"\\\\ref|\\\\textup\\{\\\\ref))(?"'!(?:'"\\(|\\\\\\(|\\\\textup\\{\\())(?P<val>\\"'$?[IVXLCDM0-9A-Z]+'"\\"'$?)'"')
chap_pat = re.compile(r'Chapter~(?"'!(?:'"\\\\ref|\\\\textup\\{\\\\ref))(?"'!(?:'"\\(|\\\\\\(|\\\\textup\\{\\())(?P<val>\\"'$?[IVXLCDM0-9A-Z]+'"\\"'$?|'"\\\\texttt\\{["'^}]+'"\\})')
for root in roots:
    print('ROOT', root)
    for path in root.rglob('*.tex'):
        try:
            lines = path.read_text().splitlines()
        except Exception:
            continue
        for i, line in enumerate(lines, 1):
            if 'Part~' in line:
                m = part_pat.search(line)
                if m:
                    print(f'PART {path}:{i}: {line.strip()}')
            if 'Chapter~' in line:
                m = chap_pat.search(line)
                if m:
                    print(f'CHAP {path}:{i}: {line.strip()}')
PY" in /Users/raeez/chiral-bar-cobar succeeded in 451ms:
ROOT /Users/raeez/chiral-bar-cobar/chapters
CHAP /Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:582: Beilinson--Drinfeld~\cite[Chapter~4]{BD04} proved the $g=0$ case;
CHAP /Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:2165: Costello--Gwilliam~\cite{CG17}, Volume~2, Chapter~5).
PART /Users/raeez/chiral-bar-cobar/chapters/theory/ordered_associative_chiral_kd.tex:5970: hierarchy of Volume~II, Part~VI\@. The correspondence is:
PART /Users/raeez/chiral-bar-cobar/chapters/theory/ordered_associative_chiral_kd.tex:7549: of Part~VII\@: genuinely $\mathsf{E}_1$-chiral algebras
PART /Users/raeez/chiral-bar-cobar/chapters/theory/ordered_associative_chiral_kd.tex:7752: non-formality (Volume~II, Part~VII).
CHAP /Users/raeez/chiral-bar-cobar/chapters/theory/ordered_associative_chiral_kd.tex:9102: Chapter~$1$\textup{)}.
CHAP /Users/raeez/chiral-bar-cobar/chapters/theory/configuration_spaces.tex:1212: the Beilinson--Drinfeld framework \cite[Chapter~3]{BD04}.
CHAP /Users/raeez/chiral-bar-cobar/chapters/theory/configuration_spaces.tex:3525: % (see Beilinson--Drinfeld~\cite[Chapter~3]{BD04}).
CHAP /Users/raeez/chiral-bar-cobar/chapters/theory/configuration_spaces.tex:4838: chiral/Ran-space correspondence is developed in \cite[Chapter~3]{BD04}; the
CHAP /Users/raeez/chiral-bar-cobar/chapters/theory/configuration_spaces.tex:4857: formalism \cite[Chapter~3]{BD04} together with factorization-homology
CHAP /Users/raeez/chiral-bar-cobar/chapters/theory/algebraic_foundations.tex:1293: \textup{(Beilinson--Drinfeld \cite[Chapter~3]{BD04})}
PART /Users/raeez/chiral-bar-cobar/chapters/theory/chiral_hochschild_koszul.tex:5035: to any Koszul chiral algebra. In Part~2, we make this concrete. For every
CHAP /Users/raeez/chiral-bar-cobar/chapters/theory/koszul_pair_structure.tex:441: \emph{Step 4}: By Stokes' theorem, $\int_{\overline{C}_n} d(\cdots) = \int_{\partial\overline{C}_n}(\cdots)$. Each codimension-$1$ boundary stratum $\overline{C}_i \times \overline{C}_j$ (with $i + j = n + 1$) contributes a composition $m_i \circ_k m_j$ (with $k$ indexing the insertion point). The sign $(-1)^{rs+t}$ in the $A_\infty$ relation arises from the Koszul sign rule applied to the desuspended generators $s^{-1}f_i$: the desuspended map $b_s$ has degree~$+1$, so permuting $s^{-1}f_1, \ldots, s^{-1}f_r$ past $b_s$ contributes $(-1)^r$; inserting $b_s$ into position $(r{+}1)$ among the desuspended outputs and accounting for the $s$ inputs with their signs gives the total sign $(-1)^{rs+t}$ (see~\cite{LV12}, \S9.2.8 for the complete sign derivation). The sum over all boundary strata exhausts all compositions, and $\partial^2 = 0$ on $\overline{C}_n$ ensures the total contribution vanishes. See~\cite{LV12}, Chapter~9 for the complete operadic argument. \qedhere
CHAP /Users/raeez/chiral-bar-cobar/chapters/theory/bar_construction.tex:1987: (Reutenauer \cite[Chapter~9]{Reutenauer93};
CHAP /Users/raeez/chiral-bar-cobar/chapters/theory/hochschild_cohomology.tex:433: This identification is classical for associative algebras \cite{Loday98}; the chiral extension follows from the factorization structure of the loop space \cite[Chapter~5]{CG17}.
CHAP /Users/raeez/chiral-bar-cobar/chapters/theory/hochschild_cohomology.tex:1128: Costello--Gwilliam~\cite[Chapter~5]{CG17}.
CHAP /Users/raeez/chiral-bar-cobar/chapters/theory/hochschild_cohomology.tex:1454: parallel result appears in Costello--Gwilliam~\cite[Chapter~5]{CG17}.
CHAP /Users/raeez/chiral-bar-cobar/chapters/theory/cobar_construction.tex:347: $\mathcal{D}$-modules \cite[Chapter~4]{KS90}.
CHAP /Users/raeez/chiral-bar-cobar/chapters/theory/cobar_construction.tex:1374: At the level of $\mathcal{D}$-modules on $\overline{C}_n(X)$, the bar and cobar differentials are flat connections (the bar complex is a complex of holonomic $\mathcal{D}$-modules by Lemma~\ref{lem:bar-holonomicity}). Verdier duality is an exact contravariant involution on $D^b_{\mathrm{hol}}(\mathcal{D}_{\overline{C}_n(X)})$ that sends a flat connection $\nabla$ to the adjoint connection $\nabla^\dagger$ (see~\cite{KS90}, Chapter~4).
codex
I’ve isolated a smaller candidate set. Next I’m reading those exact locations in context to distinguish true structural-reference drift from acceptable uses like bibliography chapter citations or theorem-part labels.
exec
/bin/zsh -lc "rg -n -C 2 --glob '*.tex' 'Part~(?:[IVXLCDM]+|[A-Z])|Parts~[IVXLCDM]+(?:--[IVXLCDM]+)?|Chapter~\\"'$?[0-9IVXLCDM]+'"\\"'$?|Chapter~'"\\\\texttt\\{["'^}]+'"\\}' /Users/raeez/chiral-bar-cobar/chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -C 2 --glob '*.tex' 'Part~(?:[IVXLCDM]+|[A-Z])|Parts~[IVXLCDM]+(?:--[IVXLCDM]+)?|Chapter~\\"'$?[0-9IVXLCDM]+'"\\"'$?|Chapter~'"\\\\texttt\\{["'^}]+'"\\}' /Users/raeez/chiral-bar-cobar-vol2/chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -C 2 --glob '*.tex' 'Part~(?:[IVXLCDM]+|[A-Z])|Parts~[IVXLCDM]+(?:--[IVXLCDM]+)?|Chapter~\\"'$?[0-9IVXLCDM]+'"\\"'$?|Chapter~'"\\\\texttt\\{["'^}]+'"\\}' /Users/raeez/calabi-yau-quantum-groups/chapters" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
/Users/raeez/chiral-bar-cobar/chapters/examples/free_fields.tex-4330-with $h = 1/16$ is the disorder operator that intertwines
/Users/raeez/chiral-bar-cobar/chapters/examples/free_fields.tex-4331-the NS and Ramond sectors. See
/Users/raeez/chiral-bar-cobar/chapters/examples/free_fields.tex:4332:\cite{DiFrancesco1997}, Chapter~7.
/Users/raeez/chiral-bar-cobar/chapters/examples/free_fields.tex-4333-\end{proof}
/Users/raeez/chiral-bar-cobar/chapters/examples/free_fields.tex-4334-
--
/Users/raeez/chiral-bar-cobar/chapters/examples/free_fields.tex-4373-
/Users/raeez/chiral-bar-cobar/chapters/examples/free_fields.tex-4374-\begin{proof}[References]
/Users/raeez/chiral-bar-cobar/chapters/examples/free_fields.tex:4375:Standard; see \cite{FMS86}, Chapter~14, or
/Users/raeez/chiral-bar-cobar/chapters/examples/free_fields.tex-4376-\cite{Pol98}, \S10.3.
/Users/raeez/chiral-bar-cobar/chapters/examples/free_fields.tex-4377-\end{proof}
--
/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_introduction_supplement_body.tex-1618-then extending outward through the standard landscape (Part~\ref{part:physics-bridges}),
/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_introduction_supplement_body.tex-1619-the bridges to mathematical physics (Part~\ref{part:seven-faces}), and the frontier
/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_introduction_supplement_body.tex:1620:(Part~VII). The
/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_introduction_supplement_body.tex-1621-holographic datum $\mathcal{H}(\cA)$ of
/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_introduction_supplement_body.tex-1622-\S\ref{subsec:holographic-datum-sixfold} provides the unifying thread:
--
/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex-666-The Costello--Gwilliam factorization algebra framework~\cite{CG17}
/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex-667-relates to ours through the Beilinson--Drinfeld equivalence between
 succeeded in 52ms:
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/hochschild.tex-911-computed by the \v{C}ech--Thom--Sullivan totalization of the
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/hochschild.tex-912-factorization cosheaf
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/hochschild.tex:913:\cite[Chapter~6]{CG17}:
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/hochschild.tex-914-\begin{equation}\label{eq:cech-ts}
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/hochschild.tex-915-\Gamma(\Sigma_g,\, \ChirHoch^\bullet(\cA))
--
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/hochschild.tex-1077-locally constant (Step~1), so it is determined by its stalk and
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/hochschild.tex-1078-monodromy (Steps~1--2). By the Costello--Gwilliam reconstruction
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/hochschild.tex:1079:theorem~\cite[Chapter~6]{CG17}, a locally constant factorization
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/hochschild.tex-1080-algebra on a manifold~$M$ is equivalent to a representation of
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/hochschild.tex-1081-$\pi_1(M)$ on the stalk; the global sections are computed by the
--
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex-4698-carries a flat connection at non-critical level,
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex-4699-as proved by Beilinson--Drinfeld~\cite{BD04}
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:4700:\textup{(}Chapter~$4$, the connection on the
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex-4701-$\mathcal{D}$-module of conformal blocks\textup{)}.
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex-4702-
--
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_3d_gravity_movements_vi_x.tex-1050-as a power series in $\hbar$ is
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_3d_gravity_movements_vi_x.tex-1051-$R = \limsup_{g \to \infty} |F_g^{\mathrm{eff}}|^{-1/(2g-2)} = 2\pi$,
 succeeded in 51ms:
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex-340-\label{rem:bps-slab}
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex-341-% RS-9: The slab is a bimodule, NOT a Swiss-cheese disk.
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:342:In the Dimofte framework (Volume~II, Part~III), the BPS algebra
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex-343-arises from the 3d holomorphic-topological theory on the slab
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex-344-$X \times [0,1]$. The slab has \emph{two} boundary components
--
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex-544-
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex-545-The shadow obstruction tower $\Theta_{A_\cC}$
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:546:(Volume~I, Part~II) acquires categorical meaning through the
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex-547-quantum group lens.
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex-548-
--
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/introduction.tex-32-
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/introduction.tex-33-\begin{itemize}
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/introduction.tex:34: \item $E_1$-chiral algebras (Volume~II, Part~III): associative factorization on $\mathbb{C} \times \mathbb{R}$, encoding the ordered/topological sector. Representation categories are monoidal.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/introduction.tex-35- \item $E_2$-chiral algebras (this work): braided factorization on $\mathbb{C} \times \mathbb{C}$, encoding the holomorphic-holomorphic sector. Representation categories are braided monoidal: the natural habitat of quantum groups.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/introduction.tex-36- \item The passage $E_1 \to E_2$ via Dunn additivity: $E_2 \simeq E_1 \otimes E_1$. An $E_2$-chiral algebra is an $E_1$-algebra in $E_1$-algebras.
--
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/introduction.tex-155-The CY-to-chiral functor $\Phi$ assigns to each CY geometry a
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/introduction.tex-156-chiral algebra $A_\cC$ whose shadow class

thinking
**Searching for part labels**

I'm thinking about searching for `\part{` and labels in each repository to check if Part VII exists and to find any label names. This could help figure out if hardcoded `PartVII` should really be `Part\ref{part:seven-faces}` or something like `part:frontier`. I’ll need to inspect the root or main parts and search for `\label{part:` in each repo to gather the necessary details.
codex
I’ve reduced the candidates to actual structural references. I’m now checking the part labels in each volume so I can distinguish “definitely stale hardcoded part number” from cases that are merely cross-volume naming prose.
exec
/bin/zsh -lc "rg -n '\\\\label\\{part:["'^}]+'"' /Users/raeez/chiral-bar-cobar/chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\\\label\\{part:["'^}]+'"' /Users/raeez/chiral-bar-cobar-vol2/chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\\\label\\{part:["'^}]+'"' /Users/raeez/calabi-yau-quantum-groups/chapters" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

 exited 1 in 52ms:

 exited 1 in 51ms:


thinking
**Searching for labels**

I’m wondering about the absence of labels in the chapters. Maybe those labels are located in the main.tex file rather than in the chapters themselves. The user only asked me to search the chapters, but I think I should consider looking at other files as well, like macros. It seems like I need to search the entire repository to be thorough and find all the part labels. Let's do that!
exec
/bin/zsh -lc "rg -n '\\\\label\\{part:["'^}]+'"' /Users/raeez/chiral-bar-cobar-vol2" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\\\label\\{part:["'^}]+'"' /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\\\label\\{part:["'^}]+'"' /Users/raeez/chiral-bar-cobar" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
/Users/raeez/chiral-bar-cobar-vol2/main.tex:1210:\label{part:swiss-cheese}
/Users/raeez/chiral-bar-cobar-vol2/main.tex:1258:\label{part:e1-core}
/Users/raeez/chiral-bar-cobar-vol2/main.tex:1300:\label{part:bbl-core}
/Users/raeez/chiral-bar-cobar-vol2/main.tex:1325:\label{part:examples}
/Users/raeez/chiral-bar-cobar-vol2/main.tex:1370:\label{part:holography}
/Users/raeez/chiral-bar-cobar-vol2/main.tex:1403:\label{part:gravity}
/Users/raeez/chiral-bar-cobar-vol2/main.tex:1427:\label{part:frontier}
 succeeded in 51ms:
/Users/raeez/calabi-yau-quantum-groups/main.tex:416:\label{part:cy-categories}
/Users/raeez/calabi-yau-quantum-groups/main.tex:431:\label{part:bridge}
/Users/raeez/calabi-yau-quantum-groups/main.tex:452:\label{part:examples}
/Users/raeez/calabi-yau-quantum-groups/main.tex:467:\label{part:connections}
/Users/raeez/calabi-yau-quantum-groups/main.tex:478:\label{part:frontier}
 succeeded in 82ms:
/Users/raeez/chiral-bar-cobar/audit_campaign_20260412_231034/F14_averaging.md:762:  1045	\label{part:characteristic-datum}
/Users/raeez/chiral-bar-cobar/main.tex:867:\label{part:bar-complex}
/Users/raeez/chiral-bar-cobar/main.tex:1045:\label{part:characteristic-datum}
/Users/raeez/chiral-bar-cobar/main.tex:1136:\label{part:standard-landscape}
/Users/raeez/chiral-bar-cobar/main.tex:1340:\label{part:physics-bridges}
/Users/raeez/chiral-bar-cobar/main.tex:1422:\label{part:seven-faces}
/Users/raeez/chiral-bar-cobar/main.tex:1455:\label{part:v1-frontier}
/Users/raeez/chiral-bar-cobar/compute/audit/latex_pitfall_blacklist_wave12.md:318:- Pattern: `Part~[IVX]+|Part [IVX]+` outside `\ref{part:...}` and `\label{part:...}`.

thinking
**Organizing part references**

I need to make sure that the part numbers correspond correctly to their labels. For example, I could report Volume 1 Part VII as `Part\ref{part:v1-frontier}` and Volume II Part VI as `Part\ref{part:gravity}`. First, I should check the order of parts in Vol 2 using main.tex. I’ll look closely at the labels to map the Roman numerals correctly. This will help ensure everything lines up as it should!
exec
/bin/zsh -lc "nl -ba /Users/raeez/calabi-yau-quantum-groups/main.tex | sed -n '400,490p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/main.tex | sed -n '1190,1445p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar/main.tex | sed -n '850,1470p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
Total output lines: 621

   850	% the full modular L-infinity lens.
   851	%
   852	% ======================================================================
   853	
   854	% \input{platonic_introduction_volume_I} % archived; content absorbed into introduction.tex
   855	
   856	% ======================================================================
   857	%
   858	% PART I: THE BAR COMPLEX
   859	%
   860	% The proved core. Five theorems = four properties of the categorical
   861	% logarithm (existence, invertibility, branch structure, leading
   862	% coefficient) plus the coefficient ring. Nothing conjectural enters.
   863	%
   864	% ======================================================================
   865	
   866	\part{The Bar Complex}
   867	\label{part:bar-complex}
 succeeded in 53ms:
   400	% ------------------------------------------
   401	
   402	\frontmatter
   403	\tableofcontents
   404	
   405	% ------------------------------------------
   406	% Main matter
   407	% ------------------------------------------
   408	
   409	\mainmatter
   410	
   411	% ==========================================
   412	% PART I: The CY Engine
   413	% ==========================================
   414	
   415	\part{The CY Engine}
   416	\label{part:cy-categories}
   417	
   418	\input{chapters/theory/introduction}
   419	\input{chapters/theory/cy_categories}
 succeeded in 53ms:
  1190	 The chain-level $\Ainf$ structure, PVA descent, spectral
  1191	 $R$-matrix, and the Swiss-cheese descent package are built for
  1192	 logarithmic $\SCchtop$-algebras; the former standing
  1193	 hypotheses are now distributed between the algebraic axioms and
  1194	 the physics bridge.
  1195	 The former standing hypotheses (H1)--(H4) are now distributed:
  1196	 (H1) and (H2) are hypotheses on physical realisations
  1197	 (Theorem~\ref{thm:physics-bridge}); (H3) is the FM calculus
  1198	 theorem; (H4) is the recognition theorem.
  1199	 The worked examples verify that specific gauge theories
  1200	 satisfy Theorem~\ref{thm:physics-bridge}.
  1201	\end{itemize}
  1202	\end{remark}
  1203	
  1204	\input{chapters/frame/preface}
  1205	
  1206	\input{chapters/theory/introduction}
  1207	
  1208	%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
  1209	\part{The Open Primitive}

thinking
**Identifying chapter labels**

I need to map chapter numbers to their corresponding labels. I think searching for `\chapter{` might help. However, I have to check if references like `Chapter66` in Volume 3 still match Volume I’s chapter count since things could be outdated. I should verify any significant discrepancies to ensure accuracy. I also need to check for labels like `ch:genus1-seven-faces` and see if they still exist in Volume I or if I should just use hardcoded numbers.
codex
The part labels are confirmed in all three `main.tex` files. I’m now tying each hardcoded numeral to the actual labeled part/chapter where possible, so the report doesn’t overstate anything.
exec
/bin/zsh -lc "rg -n '\\\\label\\{(ch|chap):genus1-seven-faces\\}|\\\\chapter\\{|\\\\section\\{|\\\\subsection\\{' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/dnp_identification_master.tex /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/conclusion.tex /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-core.tex /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_3d_gravity_movements_vi_x.tex /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\\\label\\{(ch|chap):genus1-seven-faces\\}|\\\\chapter\\{|\\\\section\\{|\\\\subsection\\{' /Users/raeez/chiral-bar-cobar/chapters/connections/genus1_seven_faces.tex /Users/raeez/chiral-bar-cobar/chapters/connections/holographic_datum_master.tex /Users/raeez/chiral-bar-cobar/chapters/connections/thqg_preface_supplement.tex /Users/raeez/chiral-bar-cobar/chapters/connections/thqg_introduction_supplement_body.tex /Users/raeez/chiral-bar-cobar/chapters/theory/ordered_associative_chiral_kd.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/conclusion.tex:1:\section{Conclusion and Outlook}
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/conclusion.tex:5:\subsection{The single object}
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/conclusion.tex:275:\subsection{One quartic pole generates everything}
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/conclusion.tex:374:\subsection{The harmonic number organizes the $\cW_N$ landscape}
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/conclusion.tex:443:\subsection{Geometric Langlands as the $\kappa=0$ slice}
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/conclusion.tex:486:\subsection{Helicity is chirality}
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/conclusion.tex:561:\subsection{The genus tower is a chromatic shadow}
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/conclusion.tex:642:\subsection{The genus tower of quantum groups}
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/conclusion.tex:702:\subsection{Four stages from chiral algebra to chromatic invariant}
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/conclusion.tex:789:\subsection{The modular holography programme}
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/conclusion.tex:930:\subsection{Concrete consequences and open problems}
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/conclusion.tex:987:\subsection{The Part~VII frontier chapters}
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/conclusion.tex:1036:\subsection{Major open conjectures}
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/conclusion.tex:1118:\subsection{The cross-volume bridge}
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/conclusion.tex:1217:\subsection{The three colors and their purity}
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/conclusion.tex:1273:\subsection{The complementarity table}
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/conclusion.tex:2079:\section{Frontier research notes (2026-04-06)}
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/conclusion.tex:2083:\subsection{Multi-weight partition functions beyond the
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/conclusion.tex:2113:\subsection{Holographic interpretation of the cross-channel
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/conclusion.tex:2134:\subsection{Open-sector cross-channel corrections}
 succeeded in 52ms:
/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_introduction_supplement_body.tex:10:\section{From bar complex to holographic datum}
/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_introduction_supplement_body.tex:26:\subsection{The Swiss-cheese factorization}
/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_introduction_supplement_body.tex:80:\subsection{The bulk-boundary-line triangle}
/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_introduction_supplement_body.tex:130:\subsection{Edges of the triangle}
/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_introduction_supplement_body.tex:164:\subsection{The holographic datum from the MC element}
/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_introduction_supplement_body.tex:207:\subsection{Reconstruction from the datum}
/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_introduction_supplement_body.tex:250:\subsection{The four recovery theorems}
/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_introduction_supplement_body.tex:335:\section{The shadow connection and conformal-block comparison surfaces}
/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_introduction_supplement_body.tex:353:\subsection{Construction of the shadow connection}
/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_introduction_supplement_body.tex:419:\subsection{Flatness from the MC equation}
/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_introduction_supplement_body.tex:467:\subsection{The KZ connection at genus $0$}
/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_introduction_supplement_body.tex:514:\subsection{The BPZ equations from the shadow obstruction tower}
/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_introduction_supplement_body.tex:610:\subsection{Higher-genus extensions}
/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_introduction_supplement_body.tex:670:\section{Gravitational complexity and the EFT hierarchy}
/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_introduction_supplement_body.tex:686:\subsection{Shadow-depth classes}
/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_introduction_supplement_body.tex:754:\subsection{The obstruction classes as effective field theory data}
/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_introduction_supplement_body.tex:809:\subsection{The genus loop and primitive shadows}
/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_introduction_supplement_body.tex:849:\subsection{The operadic complexity theorem}
/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_introduction_supplement_body.tex:880:\subsection{Shadow depth versus Koszulness}
/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_introduction_supplement_body.tex:913:\section{Duality and the gravitational phase space}
exec
/bin/zsh -lc "rg -n '\\\\label\\{(ch|chap):genus1-seven-faces\\}|\\\\chapter\\{|\\\\section\\{|\\\\subsection\\{' /Users/raeez/calabi-yau-quantum-groups/chapters/connections/cy_holographic_datum_master.tex /Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3_times_e.tex /Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex /Users/raeez/calabi-yau-quantum-groups/chapters/theory/braided_factorization.tex /Users/raeez/calabi-yau-quantum-groups/chapters/theory/introduction.tex /Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:1:\chapter{Quantum Group Representations}
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:21:\section{$\Rep_q(\frakg)$ as a braided monoidal category}
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:108:\section{The $R$-matrix as categorical $r(z)$}
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:154:\section{Kazhdan--Lusztig equivalence}
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:206:\section{Conjecture CY-C: quantum group realization}
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:239:\section{Yangian and RTT realizations}
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:300:\section{BPS algebras and quantum groups}
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:367:\section{Wall-crossing and Kontsevich--Soibelman}
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:451:\section{The modular characteristic $\kappa_{\mathrm{cat}}$}
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:542:\section{Shadow obstruction tower for quantum group categories}
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/braided_factorization.tex:1:\chapter{Braided Factorization}
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/braided_factorization.tex:26:\section{The categorical $R$-matrix and Yang--Baxter equation}
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/braided_factorization.tex:94:\section{Braided monoidal categories and $E_2$-algebras}
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/braided_factorization.tex:120:\section{Factorization homology with $E_2$-coefficients}
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/braided_factorization.tex:214:\section{The $E_2$-equivariant bar complex}
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/braided_factorization.tex:301:\section{The braided bar-cobar adjunction}
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/braided_factorization.tex:392:\section{Quantum group structure from braided Koszul duality}
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/braided_factorization.tex:455:\section{The braided shadow obstruction tower}
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/braided_factorization.tex:535:\section{Braided complementarity}
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/braided_factorization.tex:579:\section{The categorical $S$-matrix and $E_3$ scattering}

thinking
**Verifying file inclusion**

I'm wondering if the part numbering changed in the archive, especially since Volume I has Part VI titled "Frontier". The mention of `PartVII` in the Volume I files seems suspicious; it might be outdated or incorrect. I need to inspect whether those files are included in Volume I or if they belong in an appendix or standalone supplement, like `thqg_preface_supplement.tex` and `thqg_introduction_supplement_body.tex`. However, since the user asked about searching chapters, I should verify their inclusion and might need to mention file scope.
exec
/bin/zsh -lc "rg -n --glob '*.tex' 'Parts~[IVXLCDM]+(?:--[IVXLCDM]+)?|Parts~I--VI|Parts~I--V|Parts~\\ref' /Users/raeez/chiral-bar-cobar-vol2/chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --glob '*.tex' 'Parts~[IVXLCDM]+(?:--[IVXLCDM]+)?|Parts~I--VI|Parts~I--V|Parts~\\ref' /Users/raeez/chiral-bar-cobar/chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --glob '*.tex' 'Parts~[IVXLCDM]+(?:--[IVXLCDM]+)?|Parts~I--VI|Parts~I--V|Parts~\\ref' /Users/raeez/calabi-yau-quantum-groups/chapters" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/conclusion.tex:990:Part~VII extends the proved core of Parts~I--VI into conditional,
 exited 1 in 51ms:

 exited 1 in 53ms:

exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar/chapters/connections/frontier_modular_holography_platonic.tex | sed -n '1786,1790p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar/chapters/theory/ordered_associative_chiral_kd.tex | sed -n '5966,5974p;7546,7553p;7749,7755p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar/chapters/connections/thqg_preface_supplement.tex | sed -n '2052,2057p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex | sed -n '3794,3799p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  1786	satisfying the $\lambda$-Jacobi identity. Let $\cA$ be a modular
  1787	Koszul chiral algebra with $\cP\cong H^*(\cA,Q)/(\hbar)$ as
  1788	associated classical shadow \textup{(}cf.\ Vol~II, Part~IV\textup{)}.
  1789	\begin{enumerate}[label=\textup{(\roman*)}]
  1790	\item \textup{(Genus-$0$ seed.)} The $\lambda$-bracket determines the
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar/chapters/connections/thqg_introduction_supplement_body.tex | sed -n '1616,1623p;1756,1762p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  2052	\medskip\noindent
  2053	The constructions of Parts~\ref{part:bar-complex}--\ref{part:standard-landscape} provide the MC element, the
  2054	shadow obstruction tower, the Koszul dual, and the genus expansion. Part~\ref{part:seven-faces}
  2055	interprets these in the gravitational context. Part~VII pushes
  2056	to the frontier. Volume~II descends to three dimensions.
 succeeded in 52ms:
  5966	\label{rem:tridegree-physical}
  5967	\index{soft graviton!and ordered tridegree}
  5968	\index{obstruction cascade!depth-3 origin}
  5969	The ordered tridegree $(g,n,d)^{E_1}$ organises the soft graviton
  5970	hierarchy of Volume~II, Part~VI\@. The correspondence is:
  5971	soft order $p$ of a graviton theorem corresponds to degree
  5972	$r = p + 2$ in the bar complex. The depth~$d$ records
  5973	\emph{which OPE pole is responsible}: a soft theorem at order~$p$
  5974	receives contributions from all poles whose depth
  7546	the descent to the symmetric bar $B^\Sigma(A)$ is the
  7547	$R$-matrix-twisted quotient of Proposition~\ref*{sec:r-matrix-descent}.
  7548	None of the families below is $\mathsf{E}_1$-chiral in the sense
  7549	of Part~VII\@: genuinely $\mathsf{E}_1$-chiral algebras
  7550	(nonlocal, ordered configurations as primitive data) are the
  7551	Etingof--Kazhdan quantum vertex algebras, which lie outside
  7552	the Beilinson--Drinfeld framework.
  7553	
  7749	For Virasoro and $\mathcal{W}_N$: the ordered Koszul dual is the
  7750	dg-shifted Yangian $Y^{\mathrm{dg}}$, a dg algebra with
  7751	infinitely many cohomological generators reflecting
 succeeded in 51ms:
  3794	algebraic invariant. The modular MC element
  3795	$\Theta_\cA = \operatorname{av}(\Theta^{E_1}_\cA)$ is its
  3796	shadow. Volume~II's Part~VII (ordered
  3797	associative chiral Koszul duality, dg-shifted factorization
  3798	bridge, gravitational Yangian) develops the $E_1$ layer;
  3799	Parts~\ref{part:bar-complex}--\ref{part:v1-frontier} describe the modular/symmetric framework that is the
 succeeded in 51ms:
  1616	each building on the categorical logarithm of Part~\ref{part:bar-complex},
  1617	the nonlinear engine of Part~\ref{part:characteristic-datum}, and the $E_1$ wing of Part~\ref{part:standard-landscape},
  1618	then extending outward through the standard landscape (Part~\ref{part:physics-bridges}),
  1619	the bridges to mathematical physics (Part~\ref{part:seven-faces}), and the frontier
  1620	(Part~VII). The
  1621	holographic datum $\mathcal{H}(\cA)$ of
  1622	\S\ref{subsec:holographic-datum-sixfold} provides the unifying thread:
  1623	each result is a projection or extraction from the single MC
  1756	$\hbar\Delta S + \frac{1}{2}\{S,S\} = 0$; the shadow connection is
  1757	the gauge connection of the BV formalism.
  1758	
  1759	\subsection{Volume~II and beyond}
  1760	\label{subsec:thqg-intro-guide-vol2}
  1761	
  1762	Volume~II applies the engine to the full bulk/boundary/line triangle

thinking
**Searching for supplements**

Okay, I’m considering whether I need to search for THQG supplements. It might not be necessary if the report notes are already organized in chapters. The severity could be lower if it’s not a main focus anyway. I’m thinking I should inspect the main includes, but it might not be needed at all. Still, if the file isn't included, the impact would be lower, so I’ll just search quickly to be sure.
exec
/bin/zsh -lc "rg -n 'thqg_introduction_supplement_body|thqg_preface_supplement|conclusion|frontier_modular_holography_platonic|concordance' /Users/raeez/chiral-bar-cobar/main.tex /Users/raeez/chiral-bar-cobar-vol2/main.tex /Users/raeez/calabi-yau-quantum-groups/main.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
/Users/raeez/chiral-bar-cobar/main.tex:214:\declaretheorem[style=garamonddef, name=Conclusion, sibling=theorem]{conclusion}
/Users/raeez/chiral-bar-cobar/main.tex:266:\let\theHconclusion\theHtheorem
/Users/raeez/chiral-bar-cobar/main.tex:329:\providecommand*{\toclevel@conclusion}{2}
/Users/raeez/chiral-bar-cobar/main.tex:1464:\input{chapters/connections/frontier_modular_holography_platonic}
/Users/raeez/chiral-bar-cobar/main.tex:1477:% Master concordance: the trilingual dictionary connecting the seven-face
/Users/raeez/chiral-bar-cobar/main.tex:1479:% (concordance.tex) and after outlook.tex so that it serves as the final
/Users/raeez/chiral-bar-cobar/main.tex:1482:\input{chapters/connections/master_concordance}
/Users/raeez/chiral-bar-cobar/main.tex:1520:% Labels defined in archive-only content (Part VI outlook, concordance,
/Users/raeez/chiral-bar-cobar/main.tex:1535: \phantomsection\label{sec:concordance-three-pillars}% % concordance.tex (not in guide_to_main_results.tex)
/Users/raeez/chiral-bar-cobar/main.tex:1540: \phantomsection\label{thm:frontier-protected-bulk-antiinvolution}% % frontier_modular_holography_platonic.tex
/Users/raeez/chiral-bar-cobar/main.tex:1543: \phantomsection\label{def:frontier-protected-holographic-transform}% % frontier_modular_holography_platonic.tex
/Users/raeez/chiral-bar-cobar/main.tex:1547: \phantomsection\label{subsec:concordance-holographic-completion}% % concordance.tex
/Users/raeez/chiral-bar-cobar/main.tex:1548: \phantomsection\label{subsec:collision-filtration-recovery}% % frontier_modular_holography_platonic.tex
/Users/raeez/chiral-bar-cobar/main.tex:1549: % sec:concordance-nishinaka-vicedo now defined in guide_to_main_results.tex
/Users/raeez/chiral-bar-cobar/main.tex:1558: \phantomsection\label{chap:concordance}% % concordance.tex (not in guide_to_main_results.tex)
/Users/raeez/chiral-bar-cobar/main.tex:1567: \phantomsection\label{rem:pixton-genus2-computation}% % concordance.tex
/Users/raeez/chiral-bar-cobar/main.tex:1568: \phantomsection\label{rem:pixton-conjecture-status}% % concordance.tex
/Users/raeez/chiral-bar-cobar/main.tex:1569: \phantomsection\label{subsec:frontier-protected-holographic-transform}% % frontier_modular_holography_platonic.tex
/Users/raeez/chiral-bar-cobar/main.tex:1626: \phantomsection\label{sec:concordance-non-principal-w}%
/Users/raeez/chiral-bar-cobar/main.tex:1627: \phantomsection\label{sec:concordance-e1-modular-theory}%
exec
/bin/zsh -lc "rg -n 'thqg_introduction_supplement_body|thqg_preface_supplement' /Users/raeez/chiral-bar-cobar" in /Users/raeez/chiral-bar-cobar succeeded in 58ms:
Total output lines: 262

/Users/raeez/chiral-bar-cobar/metadata/census.json:245:    "chapters/connections/thqg_introduction_supplement_body.tex": {
/Users/raeez/chiral-bar-cobar/metadata/theorem_registry.md:2927:#### `chapters/connections/thqg_introduction_supplement_body.tex` (1)
/Users/raeez/chiral-bar-cobar/metadata/label_index.json:8191:    "file": "chapters/connections/thqg_introduction_supplement_body.tex",
/Users/raeez/chiral-bar-cobar/metadata/label_index.json:8195:    "file": "chapters/connections/thqg_introduction_supplement_body.tex",
/Users/raeez/chiral-bar-cobar/metadata/label_index.json:8199:    "file": "chapters/connections/thqg_introduction_supplement_body.tex",
/Users/raeez/chiral-bar-cobar/metadata/label_index.json:8203:    "file": "chapters/connections/thqg_introduction_supplement_body.tex",
/Users/raeez/chiral-bar-cobar/metadata/label_index.json:8663:    "file": "chapters/connections/thqg_preface_supplement.tex",
/Users/raeez/chiral-bar-cobar/metadata/label_index.json:14199:    "file": "chapters/connections/thqg_preface_supplement.tex",
/Users/raeez/chiral-bar-cobar/metadata/label_index.json:14263:    "file": "chapters/connections/thqg_preface_supplement.tex",
/Users/raeez/chiral-bar-cobar/metadata/label_index.json:15327:    "file": "chapters/connections/thqg_preface_supplement.tex",
/Users/raeez/chiral-bar-cobar/metadata/label_index.json:20007:    "file": "chapters/connections/thqg_introduction_supplement_body.tex",
/Users/raeez/chiral-bar-cobar/metadata/label_index.json:20011:    "file": "chapters/connections/thqg_introduction_supplement_body.tex",
/Users/raeez/chiral-bar-cobar/metadata/label_index.json:20015:    "file": "chapters/connections/thqg_introduction_supplement_body.tex",
/Users/raeez/chiral-bar-cobar/metadata/label_index.json:20019:    "file": "chapters/connections/thqg_introduction_supplement_body.tex",
/Users/raeez/chiral-bar-cobar/metadata/label_index.json:20023:    "file": "chapters/connections/thqg_introduction_supplement_body.tex",
/Users/raeez/chiral-bar-cobar/metadata/label_index.json:20027:    "file": "chapters/connections/thqg_introduction_supplement_body.tex",
/Users/raeez/chiral-bar-cobar/metadata/label_index.json:20031:    "file": "chapters/connections/thqg_introduction_supplement_body.tex",
/Users/raeez/chiral-bar-cobar/metadata/label_index.json:20035:    "file": "chapters/connections/thqg_introduction_supplement_body.tex",

thinking
**Evaluating context inclusion**

It doesn’t seem worth it to include everything if we already know from the main search. I should inspect the Volume 2 candidate contexts. I might open the conclusion and review parts like dnp and thqg Part A, especially on spectral-braiding-core Part A, to classify any false positives that might be present. I want to make sure everything is accurately categorized.
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/conclusion.tex | sed -n '984,992p;1114,1121p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/dnp_identification_master.tex | sed -n '536,542p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_3d_gravity_movements_vi_x.tex | sed -n '1048,1054p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-core.tex | sed -n '309,315p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   984	\end{tabular}
   985	\end{center}
   986	
   987	\subsection{The Part~VII frontier chapters}
   988	\label{subsec:frontier-chapters}
   989	
   990	Part~VII extends the proved core of Parts~I--VI into conditional,
   991	conjectural, and frontier territory. Its ten chapters are:
   992	
  1114	purity data of the three Swiss-cheese colours, the complementarity
  1115	table, and the proofs that crystallize only in the light of the full
  1116	two-volume architecture.
  1117	
  1118	\subsection{The cross-volume bridge}
  1119	
  1120	The five theorems of Volume~I arise as projections of the modular
  1121	MC element, while Volume~II reads their closed/open/mixed
 succeeded in 51ms:
   536	
   537	The genus-$1$ extension of the seven-face programme, proving the
   538	identification of the KZB connection with the elliptic $r$-matrix
   539	and the elliptic Gaudin model for affine KM, is in Vol~I,
   540	Chapter~\texttt{ch:genus1-seven-faces}.
 succeeded in 51ms:
  1048	\]
  1049	By the root test, the convergence radius of $\sum F_g^{\mathrm{eff}}\,\hbar^{2g-2}$
  1050	as a power series in $\hbar$ is
  1051	$R = \limsup_{g \to \infty} |F_g^{\mathrm{eff}}|^{-1/(2g-2)} = 2\pi$,
  1052	confirming Part~A.
  1053	
  1054	The physical interpretation: $\hbar = 2\pi$ is the
 succeeded in 52ms:
   309	
   310	On the chirally Koszul locus,
   311	Theorem~\ref{thm:lines_as_modules} models the perturbative line
   312	category by modules for the Koszul-dual boundary algebra, so the
   313	braided monoidal category $\mathcal{C}_\partial$ from Part~A is then
   314	identified with the category of $\mathcal{H}$-modules equipped with
   315	the braiding induced by $R(z)$.

thinking
**Evaluating theorem components**

I’m considering whether Part A is related to the theorem and I need to inspect the preceding theorem further but might exclude it if it’s not related to volume. I’ll confirm Part A as theorem-related for now. I might also look into candidate chapters from Part VII, specifically line 990. There could be other false positives in Part A that I don’t need to report. I need to inspect the candidate contexts from Volume 3 as well.
exec
/bin/zsh -lc "nl -ba /Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex | sed -n '340,346p;544,548p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/calabi-yau-quantum-groups/chapters/connections/cy_holographic_datum_master.tex | sed -n '920,937p;1004,1010p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/calabi-yau-quantum-groups/chapters/theory/introduction.tex | sed -n '30,36p;154,160p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/calabi-yau-quantum-groups/chapters/theory/braided_factorization.tex | sed -n '86,90p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex | sed -n '92,95p;5489,5493p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3_times_e.tex | sed -n '964,967p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   340	\label{rem:bps-slab}
   341	% RS-9: The slab is a bimodule, NOT a Swiss-cheese disk.
   342	In the Dimofte framework (Volume~II, Part~III), the BPS algebra
   343	arises from the 3d holomorphic-topological theory on the slab
   344	$X \times [0,1]$. The slab has \emph{two} boundary components
   345	($X \times \{0\}$ and $X \times \{1\}$), making the algebra of
   346	operators on the slab a bimodule for the two boundary algebras.
   544	
   545	The shadow obstruction tower $\Theta_{A_\cC}$
   546	(Volume~I, Part~II) acquires categorical meaning through the
   547	quantum group lens.
   548	
 succeeded in 51ms:
    86	gives $\cR_{12}\cR_{13}\cR_{23} = \cR_{23}\cR_{13}\cR_{12}$, which is
    87	the Yang--Baxter equation. The spectral parameters arise from the
    88	$z$-dependence of the collision residue (so the $R$-matrix has one
    89	fewer pole order than the OPE). See Volume~II, Chapter~11 for the
    90	full derivation.
 succeeded in 63ms:
    30	
    31	Three levels of chiral structure organize the theory:
    32	
    33	\begin{itemize}
    34	 \item $E_1$-chiral algebras (Volume~II, Part~III): associative factorization on $\mathbb{C} \times \mathbb{R}$, encoding the ordered/topological sector. Representation categories are monoidal.
    35	 \item $E_2$-chiral algebras (this work): braided factorization on $\mathbb{C} \times \mathbb{C}$, encoding the holomorphic-holomorphic sector. Representation categories are braided monoidal: the natural habitat of quantum groups.
    36	 \item The passage $E_1 \to E_2$ via Dunn additivity: $E_2 \simeq E_1 \otimes E_1$. An $E_2$-chiral algebra is an $E_1$-algebra in $E_1$-algebras.
   154	\label{rem:v3-cy-glcm-shadow-classification}
   155	The CY-to-chiral functor $\Phi$ assigns to each CY geometry a
   156	chiral algebra $A_\cC$ whose shadow class
   157	(Volume~I, Part~II) organizes the resulting landscape:
   158	\begin{itemize}
   159	\item $\C^3$ (toric, abelian): class~$\mathbf{G}$ (shadow depth~$2$,
   160	 $\kappa_{\mathrm{ch}} = 1$). The Heisenberg truncation at spin~$1$.
 succeeded in 61ms:
   964	The following results are proved in Volume~I
   965	(\S\ref{sec:k3-sigma-model}--\S\ref{sec:grand-synthesis-k3xe}
   966	of Chapter~66) and apply to the $K3 \times E$ tower.
   967	We record them here for cross-reference; conventions
 succeeded in 69ms:
    92	\label{rem:arnold-fay-generalization}
    93	\index{Arnold relation!Fay generalization}
    94	The Arnold relation (Vol~I, Theorem~\ref{thm:arnold-relations}), which governs the genus-$0$ bar differential, admits two distinct generalizations. Direction~(a): via clutching morphisms and the shadow obstruction tower $\Theta_A^{\leq r}$ (Vol~I, Definition~\ref{def:shadow-postnikov-tower}), one passes to the modular regime on stable curves, recovering the higher-genus bar complex developed in Vol~I, Part~I (Vol~I, Remark~\ref{rem:five-pieces}). Direction~(b): via the Fay trisecant identity (Theorem~\ref{thm:fay}), one replaces the additive (logarithmic) propagator $\omega = dz/(z-w)$ by the elliptic (multiplicative) propagator built from the Weierstrass $\sigma$-function, entering the toroidal regime. The present chapter develops direction~(b): the systematic passage from logarithmic to elliptic propagators and its consequences for bar-cobar duality.
    95	\end{remark}
  5489	
  5490	The following results are proved in Volume~I
  5491	(\S\ref{sec:k3-sigma-model}--\S\ref{sec:grand-synthesis-k3xe}
  5492	of Chapter~66) and apply to the $K3 \times E$ tower.
  5493	We record them here for cross-reference; conventions
 succeeded in 81ms:
   920	\label{sec:cy-cross-volume-bridge}
   921	
   922	This part of Vol~III mirrors Vol~I Part~III and Vol~II Part~III. The
   923	common skeleton is the seven-face programme; the variation is in which
   924	face is most concrete.
   925	
   926	\begin{remark}[The three seven-face masters]
   927	\label{rem:three-seven-face-masters}
   928	The three volumes each devote a part to the seven-face programme, with
   929	the same architecture but different ground objects:
   930	\begin{enumerate}[label=(\arabic*)]
   931	\item \emph{Vol~I, Part~III:} the binary collision residue of a chiral
   932	algebra on a curve, in seven languages: bar-cobar twisting, primitive
   933	generator, classical $r$-matrix, KZ connection, Gaudin model, Bethe
   934	ansatz, dg-shifted Yangian (cf.\ Vol~I,
   935	Theorem~\ref{thm:vol1-seven-face-master}).
   936	\item \emph{Vol~II, Part~III:} the binary collision residue of a
   937	holomorphic-topological quantum group, in seven languages: open-string
  1004	The genus-$1$ extension, identifying the KZB connection with the
  1005	elliptic $r$-matrix on the torus~$E_\tau$, is proved for affine KM

thinking
**Investigating section references**

I need to check if line 5492/966 refers to Volume I, but maybe those sections are still in the same file. They could be outdated due to the shift from Volume I to Volume III. I'll search for section labels like `sec:k3-sigma-model` and `sec:grand-synthesis-k3xe`, which might now be in the Volume III file itself. It's crucial to verify these section labels, as the cross-volume chapter numbers may be inaccurate due to the changes. I'll search across repositories.
codex
Two Vol III hits are stronger than “hardcoded”: the `Chapter~66` reference looks likely stale after content migration. I’m verifying where those section labels now live before assigning severity.
exec
/bin/zsh -lc "rg -n '\\\\label\\{(ch|chap):["'^}]+'"' /Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex | tail -n 5" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'k3_times_e|toroidal_elliptic' /Users/raeez/calabi-yau-quantum-groups/main.tex /Users/raeez/chiral-bar-cobar/main.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'sec:k3-sigma-model|sec:grand-synthesis-k3xe' /Users/raeez/chiral-bar-cobar /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
55:\label{chap:toroidal-elliptic}
4693:\phantomsection\label{ch:k3-times-e}
 succeeded in 52ms:
/Users/raeez/calabi-yau-quantum-groups/main.tex:454:\input{chapters/examples/toroidal_elliptic}
/Users/raeez/calabi-yau-quantum-groups/main.tex:455:% \input{chapters/examples/k3_times_e} % Merged into toroidal_elliptic.tex
/Users/raeez/chiral-bar-cobar/main.tex:1319: % \input{chapters/examples/toroidal_elliptic} % Moved to Vol III
/Users/raeez/chiral-bar-cobar/main.tex:1600: \phantomsection\label{chap:toroidal-elliptic}% % toroidal_elliptic.tex (moved to Vol III)
/Users/raeez/chiral-bar-cobar/main.tex:1601: %% Phantom labels for toroidal_elliptic.tex content (now in Vol III):
 succeeded in 52ms:
/Users/raeez/chiral-bar-cobar/metadata/label_index.json:39330:  "sec:grand-synthesis-k3xe": {
/Users/raeez/chiral-bar-cobar/audit_campaign_20260412_231034/AP13_hardcoded_part.md:558:   965	(\S\ref{sec:k3-sigma-model}--\S\ref{sec:grand-synthesis-k3xe}
/Users/raeez/chiral-bar-cobar/audit_campaign_20260412_231034/AP13_hardcoded_part.md:588:  5491	(\S\ref{sec:k3-sigma-model}--\S\ref{sec:grand-synthesis-k3xe}
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:26:\phantomsection\label{sec:k3-sigma-model}%
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:3068:\label{sec:grand-synthesis-k3xe}
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:5491:(\S\ref{sec:k3-sigma-model}--\S\ref{sec:grand-synthesis-k3xe}
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3_times_e.tex:965:(\S\ref{sec:k3-sigma-model}--\S\ref{sec:grand-synthesis-k3xe}
/Users/raeez/chiral-bar-cobar/chapters/examples/toroidal_elliptic.tex:2791:\label{sec:grand-synthesis-k3xe}
/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:10765: (\S\ref{sec:k3-chiral-algebra}--\S\ref{sec:grand-synthesis-k3xe}):


thinking
**Identifying references issues**

I'm encountering more than a simple missing reference; there's actually an incorrect hardcoded number. For instance, line 931 states "Vol I Part III" when it should be "Vol I Part V." That's a pretty serious error. There’s also line 1788 in Vol 1 that mentions "cf. Vol II, Part IV," which might be correct, as Vol II Part IV refers to examples or characteristics. I need to check if it's properly associated with the context of classical shadow.
thinking
**Inspecting local context**

I need to examine the local context around 7749. It mentions that the ordered Koszul dual is a dg-shifted Yangian with many cohomological generators, which suggests non-formality. Part VII of Volume II includes something called "ordered_associative_chiral_kd_frontier," so it seems correct that this could relate to non-formality. 

Regarding line 7549, it talks about E1-chiral algebras, possibly tying back to the frontier chapter in Volume I, but I need to verify if it's also referencing Volume II. I'll keep digging into the surrounding context!
codex
I’ve found at least one stronger second-order failure: a Vol III cross-volume bridge says the seven-face programme in Vol I is “Part III,” but Vol I’s `main.tex` makes the seven-face programme Part V. I’m checking the nearby Vol I/II candidate lines for similar numeral drift, not just missing `\ref`.
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar/chapters/theory/ordered_associative_chiral_kd.tex | sed -n '7526,7555p;7738,7760p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/main.tex | sed -n '1288,1306p;1424,1446p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/conclusion.tex | sed -n '1120,1148p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/conclusion.tex | sed -n '987,1005p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  7526	\section{Rosetta stone: the $\mathsf{E}_1$ ordered bar complex across the landscape}
  7527	\label{sec:e1-rosetta-stone}
  7528	\index{Rosetta stone!ordered bar complex|textbf}
  7529	\index{ordered bar complex!landscape table|textbf}
  7530	\index{shadow depth!landscape classification|textbf}
  7531	% ================================================================
  7532	
  7533	The ordered bar complex $\Barch(A)$ carries two layers of data:
  7534	the collision residue $r^{\mathrm{coll}}(z)$, which records the
  7535	chiral differential of the $E_1$-chiral coalgebra, and
  7536	the $R$-matrix $R(z)$, which governs the passage from
  7537	ordered to unordered configurations. The following table
  7538	collects this data for all standard families.
  7539	
  7540	Every entry is an $\mathsf{E}_\infty$-chiral algebra
  7541	(a vertex algebra in the sense of Beilinson--Drinfeld:
  7542	the chiral product is defined on \emph{unordered}
  7543	configuration spaces with $\Sigma_n$-equivariant
  7544	factorization structure). The ordered bar complex
  7545	$\Barch(A)$ retains the ordering as auxiliary bookkeeping;
 succeeded in 52ms:
  1120	The five theorems of Volume~I arise as projections of the modular
  1121	MC element, while Volume~II reads their closed/open/mixed
  1122	three-dimensional descendants through the Swiss-cheese MC package:
  1123	Theorem~A specializes to $\SCchtop$-bar-cobar when the curve is
  1124	$\C$ and the topological direction is~$\R$;
  1125	the spectral $R$-matrix recovers the DK-0 shadow of the
  1126	Drinfeld--Kohno ladder via the Laplace transform of the
  1127	$\lambda$-bracket;
  1128	chiral Hochschild cohomology is the physical origin of Theorem~H;
  1129	the curved genus tower is Theorem~D in its physical incarnation.
  1130	The complete strictification theorem
  1131	(Theorem~\ref{thm:complete-strictification}) adds a sixth bridge:
  1132	the spectral Drinfeld class, which a priori could obstruct the
  1133	passage from spectral quasi-factorization data to strict factorization quantum groups,
  1134	vanishes identically; the rigidity is not imposed but inherited
  1135	from the root-multiplicity-one structure of simple Lie algebras.
  1136	This is the ordered/open-sector analogue
  1137	(\S\ref{ch:ordered-associative-chiral-kd}) of homotopy-Koszulity for
  1138	the closed sector: both are structural consequences of the underlying
  1139	Lie theory, not of the specific HT dynamics.
 succeeded in 52ms:
  1288	
  1289	\input{chapters/connections/bar-cobar-review}
  1290	\input{chapters/connections/line-operators}
  1291	\input{chapters/connections/ordered_associative_chiral_kd_core}
  1292	\input{chapters/connections/dg_shifted_factorization_bridge}
  1293	\input{chapters/connections/thqg_gravitational_yangian}
  1294	\input{chapters/connections/typeA_baxter_rees_theta}
  1295	\input{chapters/connections/shifted_rtt_duality_orthogonal_coideals}
  1296	\input{chapters/connections/casimir_divisor_core_transport}
  1297	
  1298	%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
  1299	\part{The Seven Faces of $r(z)$}
  1300	\label{part:bbl-core}
  1301	%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
  1302	
  1303	\noindent
  1304	The collision residue $r(z) = \mathrm{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA)$
  1305	is the genus-$0$, degree-$2$ projection of the universal MC element.
  1306	It is a single object that appears in seven guises: the
  1424	
 succeeded in 50ms:
   987	\subsection{The Part~VII frontier chapters}
   988	\label{subsec:frontier-chapters}
   989	
   990	Part~VII extends the proved core of Parts~I--VI into conditional,
   991	conjectural, and frontier territory. Its ten chapters are:
   992	
   993	\begin{enumerate}[label=\textup{(\arabic*)}]
   994	\item \emph{Spectral braiding frontier}
   995	 (\S\ref{sec:ambient-complementarity-chain-level}):
   996	 chain-level ambient complementarity, Drinfeld double and antipode.
   997	
   998	\item \emph{HT bulk-boundary-line frontier}
   999	 (\S\ref{chap:ht-bulk-boundary-line-frontier}):
  1000	 the global triangle beyond the boundary-linear sector,
  1001	 rich boundaries, absolute line operators, Steinberg-style endpoint.
  1002	
  1003	\item \emph{Celestial boundary transfer frontier}
  1004	 (\S\ref{ch:celestial-boundary-transfer-frontier}):
  1005	 $W$-type PVA obstructions, higher-spin celestial data.

thinking
**Clarifying references to volumes**

I’m thinking that the reference might be about a candidate in Volume 1, Part VII, but it could actually be referring to Volume II, Part VII. The text mentions "genuinely E1-chiral algebras are EK QVAs," and I’m wondering if it relates to the same chapter's frontier. There’s no Part VII in Volume 1; it ends at Part VI. Since Volume II has the discussion on genuine E1-chiral algebras, I need to search there for the Etingof-Kazhdan QVAs. Let's look into it!
exec
/bin/zsh -lc "rg -n 'Etingof--Kazhdan|quantum vertex algebra|genuinely \\"'$E_1'"\\"'$|genuinely '"\\\\mathsf\\{E\\}_1' /Users/raeez/chiral-bar-cobar-vol2/chapters /Users/raeez/chiral-bar-cobar/chapters/theory/ordered_associative_chiral_kd.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
/Users/raeez/chiral-bar-cobar/chapters/theory/ordered_associative_chiral_kd.tex:2012:For a genuinely $E_1$-chiral algebra (where the ordering is
/Users/raeez/chiral-bar-cobar/chapters/theory/ordered_associative_chiral_kd.tex:2032: quantum vertex algebra in the sense of Etingof--Kazhdan)
/Users/raeez/chiral-bar-cobar/chapters/theory/ordered_associative_chiral_kd.tex:2391:independent input (genuinely $E_1$).
/Users/raeez/chiral-bar-cobar/chapters/theory/ordered_associative_chiral_kd.tex:7551:Etingof--Kazhdan quantum vertex algebras, which lie outside
/Users/raeez/chiral-bar-cobar/chapters/theory/ordered_associative_chiral_kd.tex:7846: \textup{(}Etingof--Kazhdan quantum vertex algebras,
/Users/raeez/chiral-bar-cobar/chapters/theory/ordered_associative_chiral_kd.tex:7927:$Y_\hbar(\fg)$, Etingof--Kazhdan quantum vertex algebras),
/Users/raeez/chiral-bar-cobar/chapters/theory/ordered_associative_chiral_kd.tex:7973:  \textup{(}the Etingof--Kazhdan axioms\textup{)};
/Users/raeez/chiral-bar-cobar/chapters/theory/ordered_associative_chiral_kd.tex:8763:  Etingof--Kazhdan~\cite{EK96}). The JKL coproduct on the
/Users/raeez/chiral-bar-cobar/chapters/theory/ordered_associative_chiral_kd.tex:8937:vertex Hopf algebra in the sense of Etingof--Kazhdan, is a
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:1854: Examples: Yangians $Y_\hbar(\fg)$, quantum vertex algebras
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:1855: in the sense of Etingof--Kazhdan.
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:1939: $Y_\hbar(\fg)$ and quantum vertex algebras in the sense of
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:1940: Etingof--Kazhdan. The ordered bar complex
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:5772:is represented by the quantum vertex algebra $V_q(\fg)$;
/Users/raeez/chiral-bar-cobar-vol2/chapters/frame/preface_trimmed.tex:161:independent input: Yangians, Etingof--Kazhdan quantum vertex
/Users/raeez/chiral-bar-cobar-vol2/chapters/frame/preface_trimmed.tex:211:operad; for $E_1$-chiral algebras (Yangians, Etingof--Kazhdan
/Users/raeez/chiral-bar-cobar-vol2/chapters/frame/preface_trimmed.tex:212:quantum vertex algebras), it is the ordered chiral associative
/Users/raeez/chiral-bar-cobar-vol2/chapters/frame/preface.tex:387:genuinely $E_1$ layer is where the spectral $R$-matrix is an
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/modular_pva_quantization_frontier.tex:342:both produce a quantum vertex algebra that is:
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-core.tex:513:For genuinely $E_1$-chiral algebras, $R(z)$ is independent

thinking
**Clarifying chapter stability**

I'm considering that `Volume II, Chapter 11` might be unstable and that there isn't a clear chapter label. It’s uncertain whether it’s currently accurate. I can check by counting the chapters in the main text to confirm. That could help ensure I have the right information and avoid any confusion. I'll take that extra step to make sure everything aligns correctly!
codex
The remaining work is completeness: I’m doing one last normalized sweep for literal Roman-numeral parts, numeric chapters, and raw label strings so the final report doesn’t miss a stray hardcoded reference.
exec
/bin/zsh -lc "rg -n --glob '*.tex' 'Part~(I|II|III|IV|V|VI|VII|VIII|IX|X)\\b|Parts~(I|II|III|IV|V|VI|VII|VIII|IX|X)(--(I|II|III|IV|V|VI|VII|VIII|IX|X))?|Chapter~\\"'$?[0-9]+'"\\"'$?|Chapter~'"\\\\texttt\\{["'^}]+'"\\}' /Users/raeez/chiral-bar-cobar/chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --glob '*.tex' 'Part~(I|II|III|IV|V|VI|VII|VIII|IX|X)\\b|Parts~(I|II|III|IV|V|VI|VII|VIII|IX|X)(--(I|II|III|IV|V|VI|VII|VIII|IX|X))?|Chapter~\\"'$?[0-9]+'"\\"'$?|Chapter~'"\\\\texttt\\{["'^}]+'"\\}' /Users/raeez/chiral-bar-cobar-vol2/chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --glob '*.tex' 'Part~(I|II|III|IV|V|VI|VII|VIII|IX|X)\\b|Parts~(I|II|III|IV|V|VI|VII|VIII|IX|X)(--(I|II|III|IV|V|VI|VII|VIII|IX|X))?|Chapter~\\"'$?[0-9]+'"\\"'$?|Chapter~'"\\\\texttt\\{["'^}]+'"\\}' /Users/raeez/calabi-yau-quantum-groups/chapters" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:4700:\textup{(}Chapter~$4$, the connection on the
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-core.tex:3469:operads (Loday--Vallette \cite{LV12}, Chapter~10; generalized
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/dnp_identification_master.tex:540:Chapter~\texttt{ch:genus1-seven-faces}.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/hochschild.tex:913:\cite[Chapter~6]{CG17}:
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/hochschild.tex:1079:theorem~\cite[Chapter~6]{CG17}, a locally constant factorization
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_frontier.tex:83:In Chriss--Ginzburg \cite{chriss-ginzburg} Chapter~3, the orbit stratification
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/bar-cobar-review.tex:465:The convolution dg Lie algebra $\mathrm{Conv}(\cC, \cA)$ arises in two equivalent ways: (i)~when $\cC = \barB(\cA)$ is the bar construction, the cooperad structure on $\barB(\cA)$ and the operad structure on $\mathrm{End}_\cA$ give an $L_\infty$-algebra via the operadic convolution of \cite{LV12}, Chapter~6; (ii)~for a general conilpotent coalgebra $\cC$ and algebra $\cA$, the associative convolution product $f \star g = \mu_\cA \circ (f \otimes g) \circ \Delta_\cC$ on $\mathrm{Hom}(\cC, \cA)$ yields a dg Lie algebra by taking graded commutators. When $\cC = \barB(\cA)$, the two constructions agree because the cooperad structure on $\barB(\cA)$ is determined by the coalgebra structure via the cofree property. In the representability theorems above, we use convention~(ii) for general $\cC$ and convention~(i) when $\cC = \barB(\cA)$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/relative_feynman_transform.tex:846:\cite{LV12}, Chapter~13.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/relative_feynman_transform.tex:1452:(Chriss--Ginzburg~\cite{CG97}, Chapter~8): the convolution
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/conclusion.tex:987:\subsection{The Part~VII frontier chapters}
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/conclusion.tex:990:Part~VII extends the proved core of Parts~I--VI into conditional,
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding.tex:969:operads (Loday--Vallette \cite{LV12}, Chapter~10; generalized
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/factorization_swiss_cheese.tex:2148:Lurie \cite{HA}, Chapter~5.5, with two strata: the open stratum
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/raviolo.tex:498:\emph{Absolute convergence.} Item~(b) asserts one-loop finiteness: all one-loop Feynman integrals converge in the HT gauge. For theories with $d' = 1$ topological direction, the power-counting of~\cite{GRW21} shows that this implies finiteness at \emph{all} loop orders: the superficial degree of divergence of an $L$-loop graph is $\delta = (1 - d')L = 0$ for $L = 0$ and $\delta < 0$ for $L \ge 2$, so the only potential divergences are at one loop, and these are finite by hypothesis. This power-counting bound applies to theories with propagator of type $(0,1)$ in the holomorphic direction and distributional in the topological direction. For such theories, the loop superficial degree of divergence is $\delta = (1-d')L$ where $d' = \dim_\C$ of the holomorphic factor; at $d' = 1$ this gives $\delta = 0$ for all $L$, so only logarithmic divergences can appear and these are removed by the one-loop renormalization hypothesis. See \cite[Chapter~9]{CG17} and \cite[Theorem~3.1]{GRW21} for the precise class of theories. After FM compactification of the holomorphic factor, the integrand acquires at worst logarithmic singularities along boundary divisors. Concretely:
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/foundations_recast_draft.tex:721:\cite{BD04}, Chapter~3.
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/foundations_recast_draft.tex:732:Chapter~4).
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/locality.tex:284:Costello--Gwilliam~\cite[Chapter~5, \S5.4]{CG17} prove that a
 succeeded in 51ms:
/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_preface_supplement.tex:2055:interprets these in the gravitational context. Part~VII pushes
/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_introduction_supplement_body.tex:1620:(Part~VII). The
/Users/raeez/chiral-bar-cobar/chapters/theory/koszul_pair_structure.tex:441:\emph{Step 4}: By Stokes' theorem, $\int_{\overline{C}_n} d(\cdots) = \int_{\partial\overline{C}_n}(\cdots)$. Each codimension-$1$ boundary stratum $\overline{C}_i \times \overline{C}_j$ (with $i + j = n + 1$) contributes a composition $m_i \circ_k m_j$ (with $k$ indexing the insertion point). The sign $(-1)^{rs+t}$ in the $A_\infty$ relation arises from the Koszul sign rule applied to the desuspended generators $s^{-1}f_i$: the desuspended map $b_s$ has degree~$+1$, so permuting $s^{-1}f_1, \ldots, s^{-1}f_r$ past $b_s$ contributes $(-1)^r$; inserting $b_s$ into position $(r{+}1)$ among the desuspended outputs and accounting for the $s$ inputs with their signs gives the total sign $(-1)^{rs+t}$ (see~\cite{LV12}, \S9.2.8 for the complete sign derivation). The sum over all boundary strata exhausts all compositions, and $\partial^2 = 0$ on $\overline{C}_n$ ensures the total contribution vanishes. See~\cite{LV12}, Chapter~9 for the complete operadic argument. \qedhere
/Users/raeez/chiral-bar-cobar/chapters/connections/frontier_modular_holography_platonic.tex:1788:associated classical shadow \textup{(}cf.\ Vol~II, Part~IV\textup{)}.
/Users/raeez/chiral-bar-cobar/chapters/theory/configuration_spaces.tex:1212:the Beilinson--Drinfeld framework \cite[Chapter~3]{BD04}.
/Users/raeez/chiral-bar-cobar/chapters/theory/configuration_spaces.tex:3525:% (see Beilinson--Drinfeld~\cite[Chapter~3]{BD04}).
/Users/raeez/chiral-bar-cobar/chapters/theory/configuration_spaces.tex:4838:chiral/Ran-space correspondence is developed in \cite[Chapter~3]{BD04}; the
/Users/raeez/chiral-bar-cobar/chapters/theory/configuration_spaces.tex:4857:formalism \cite[Chapter~3]{BD04} together with factorization-homology
/Users/raeez/chiral-bar-cobar/chapters/theory/cobar_construction.tex:347:$\mathcal{D}$-modules \cite[Chapter~4]{KS90}.
/Users/raeez/chiral-bar-cobar/chapters/theory/cobar_construction.tex:1374:At the level of $\mathcal{D}$-modules on $\overline{C}_n(X)$, the bar and cobar differentials are flat connections (the bar complex is a complex of holonomic $\mathcal{D}$-modules by Lemma~\ref{lem:bar-holonomicity}). Verdier duality is an exact contravariant involution on $D^b_{\mathrm{hol}}(\mathcal{D}_{\overline{C}_n(X)})$ that sends a flat connection $\nabla$ to the adjoint connection $\nabla^\dagger$ (see~\cite{KS90}, Chapter~4).
/Users/raeez/chiral-bar-cobar/chapters/theory/hochschild_cohomology.tex:433:This identification is classical for associative algebras \cite{Loday98}; the chiral extension follows from the factorization structure of the loop space \cite[Chapter~5]{CG17}.
/Users/raeez/chiral-bar-cobar/chapters/theory/hochschild_cohomology.tex:1128:Costello--Gwilliam~\cite[Chapter~5]{CG17}.
/Users/raeez/chiral-bar-cobar/chapters/theory/hochschild_cohomology.tex:1454:parallel result appears in Costello--Gwilliam~\cite[Chapter~5]{CG17}.
/Users/raeez/chiral-bar-cobar/chapters/theory/ordered_associative_chiral_kd.tex:5970:hierarchy of Volume~II, Part~VI\@. The correspondence is:
/Users/raeez/chiral-bar-cobar/chapters/theory/ordered_associative_chiral_kd.tex:7549:of Part~VII\@: genuinely $\mathsf{E}_1$-chiral algebras
/Users/raeez/chiral-bar-cobar/chapters/theory/ordered_associative_chiral_kd.tex:7752:non-formality (Volume~II, Part~VII).
/Users/raeez/chiral-bar-cobar/chapters/theory/ordered_associative_chiral_kd.tex:9102:  Chapter~$1$\textup{)}.
/Users/raeez/chiral-bar-cobar/chapters/theory/algebraic_foundations.tex:1293:\textup{(Beilinson--Drinfeld \cite[Chapter~3]{BD04})}
/Users/raeez/chiral-bar-cobar/chapters/theory/bar_construction.tex:1987:(Reutenauer \cite[Chapter~9]{Reutenauer93};
/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:582:Beilinson--Drinfeld~\cite[Chapter~4]{BD04} proved the $g=0$ case;
 succeeded in 51ms:
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:342:In the Dimofte framework (Volume~II, Part~III), the BPS algebra
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:546:(Volume~I, Part~II) acquires categorical meaning through the
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/cy_holographic_datum_master.tex:922:This part of Vol~III mirrors Vol~I Part~III and Vol~II Part~III. The
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/cy_holographic_datum_master.tex:931:\item \emph{Vol~I, Part~III:} the binary collision residue of a chiral
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/cy_holographic_datum_master.tex:936:\item \emph{Vol~II, Part~III:} the binary collision residue of a
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/cy_holographic_datum_master.tex:1006:in Vol~I, Chapter~\texttt{ch:genus1-seven-faces}.
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/cy_holographic_datum_master.tex:1009:Vol~III. Subsequent chapters in Part~V record the geometric Langlands
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:94:The Arnold relation (Vol~I, Theorem~\ref{thm:arnold-relations}), which governs the genus-$0$ bar differential, admits two distinct generalizations. Direction~(a): via clutching morphisms and the shadow obstruction tower $\Theta_A^{\leq r}$ (Vol~I, Definition~\ref{def:shadow-postnikov-tower}), one passes to the modular regime on stable curves, recovering the higher-genus bar complex developed in Vol~I, Part~I (Vol~I, Remark~\ref{rem:five-pieces}). Direction~(b): via the Fay trisecant identity (Theorem~\ref{thm:fay}), one replaces the additive (logarithmic) propagator $\omega = dz/(z-w)$ by the elliptic (multiplicative) propagator built from the Weierstrass $\sigma$-function, entering the toroidal regime. The present chapter develops direction~(b): the systematic passage from logarithmic to elliptic propagators and its consequences for bar-cobar duality.
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:5492:of Chapter~66) and apply to the $K3 \times E$ tower.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/introduction.tex:34: \item $E_1$-chiral algebras (Volume~II, Part~III): associative factorization on $\mathbb{C} \times \mathbb{R}$, encoding the ordered/topological sector. Representation categories are monoidal.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/introduction.tex:157:(Volume~I, Part~II) organizes the resulting landscape:
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/quantum_groups_foundations.tex:84:Drinfeld, ``Quantum groups'' (ICM Berkeley 1986), Theorem~2; see also Chari--Pressley, \emph{A Guide to Quantum Groups}, Chapter~4.2. The proof is a direct consequence of quasi-triangularity and the coassociativity of $\Delta$.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/braided_factorization.tex:89:fewer pole order than the OPE). See Volume~II, Chapter~11 for the
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3_times_e.tex:966:of Chapter~66) and apply to the $K3 \times E$ tower.

thinking
**Checking internal part references**

I need to see if there are any hardcoded internal part numbers that haven't been detected due to volume part naming conventions like "VolIII part V." I've noted line 1009, which is good, but I wonder if there are other hardcoded parts to consider. Should I check cross-volume part references between Vol1 and Vol2/III? A search for patterns like `VolumeII, Part` or `VolII, Part` seems wise. I'll definitely run that for exact cross-volume patterns.
exec
/bin/zsh -lc "rg -n --glob '*.tex' 'Vol(?:ume)?~I[, ]+Part~|Vol(?:ume)?~II[, ]+Part~|Vol(?:ume)?~III[, ]+Part~|Volume~II\\'s Part~|Volume~I\\'s Part~|Part~VII\\b|Part~V\\b|Part~IV\\b|Part~VI\\b' /Users/raeez/chiral-bar-cobar/chapters /Users/raeez/chiral-bar-cobar-vol2/chapters /Users/raeez/calabi-yau-quantum-groups/chapters" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:
zsh:1: unmatched '
exec
/bin/zsh -lc "rg -n --glob '*.tex' \"Vol(?:ume)?~I[, ]+Part~|Vol(?:ume)?~II[, ]+Part~|Vol(?:ume)?~III[, ]+Part~|Volume~II's Part~|Volume~I's Part~|Part~VII\\\\b|Part~V\\\\b|Part~IV\\\\b|Part~VI\\\\b\" /Users/raeez/chiral-bar-cobar/chapters /Users/raeez/chiral-bar-cobar-vol2/chapters /Users/raeez/calabi-yau-quantum-groups/chapters" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:342:In the Dimofte framework (Volume~II, Part~III), the BPS algebra
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:546:(Volume~I, Part~II) acquires categorical meaning through the
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:94:The Arnold relation (Vol~I, Theorem~\ref{thm:arnold-relations}), which governs the genus-$0$ bar differential, admits two distinct generalizations. Direction~(a): via clutching morphisms and the shadow obstruction tower $\Theta_A^{\leq r}$ (Vol~I, Definition~\ref{def:shadow-postnikov-tower}), one passes to the modular regime on stable curves, recovering the higher-genus bar complex developed in Vol~I, Part~I (Vol~I, Remark~\ref{rem:five-pieces}). Direction~(b): via the Fay trisecant identity (Theorem~\ref{thm:fay}), one replaces the additive (logarithmic) propagator $\omega = dz/(z-w)$ by the elliptic (multiplicative) propagator built from the Weierstrass $\sigma$-function, entering the toroidal regime. The present chapter develops direction~(b): the systematic passage from logarithmic to elliptic propagators and its consequences for bar-cobar duality.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/introduction.tex:34: \item $E_1$-chiral algebras (Volume~II, Part~III): associative factorization on $\mathbb{C} \times \mathbb{R}$, encoding the ordered/topological sector. Representation categories are monoidal.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/introduction.tex:157:(Volume~I, Part~II) organizes the resulting landscape:
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/cy_holographic_datum_master.tex:922:This part of Vol~III mirrors Vol~I Part~III and Vol~II Part~III. The
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/cy_holographic_datum_master.tex:931:\item \emph{Vol~I, Part~III:} the binary collision residue of a chiral
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/cy_holographic_datum_master.tex:936:\item \emph{Vol~II, Part~III:} the binary collision residue of a
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/cy_holographic_datum_master.tex:1009:Vol~III. Subsequent chapters in Part~V record the geometric Langlands
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/conclusion.tex:987:\subsection{The Part~VII frontier chapters}
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/conclusion.tex:990:Part~VII extends the proved core of Parts~I--VI into conditional,
/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:3796:shadow. Volume~II's Part~VII (ordered
/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_preface_supplement.tex:2055:interprets these in the gravitational context. Part~VII pushes
/Users/raeez/chiral-bar-cobar/chapters/connections/frontier_modular_holography_platonic.tex:1788:associated classical shadow \textup{(}cf.\ Vol~II, Part~IV\textup{)}.
/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_introduction_supplement_body.tex:1620:(Part~VII). The
/Users/raeez/chiral-bar-cobar/chapters/theory/ordered_associative_chiral_kd.tex:5970:hierarchy of Volume~II, Part~VI\@. The correspondence is:
/Users/raeez/chiral-bar-cobar/chapters/theory/ordered_associative_chiral_kd.tex:7549:of Part~VII\@: genuinely $\mathsf{E}_1$-chiral algebras
/Users/raeez/chiral-bar-cobar/chapters/theory/ordered_associative_chiral_kd.tex:7752:non-formality (Volume~II, Part~VII).

thinking
**Searching for chapter references**

I’m thinking I might need to search chapters across volumes, specifically looking for numeric references. I should start with something like “Volume II, Chapter” or “Chapter 66” to make sure I’m covering all the relevant parts. It’s essential to get that comprehensive view to understand everything better! Let’s dig in and find what I need.
exec
/bin/zsh -lc "rg -n --glob '*.tex' 'Vol(?:ume)?~I[, ]+Chapter~|Vol(?:ume)?~II[, ]+Chapter~|Vol(?:ume)?~III[, ]+Chapter~|Chapter~\\"'$?[0-9]+'"\\"'$?|Chapter~'"\\\\texttt\\{["'^}]+'"\\}' /Users/raeez/chiral-bar-cobar/chapters /Users/raeez/chiral-bar-cobar-vol2/chapters /Users/raeez/calabi-yau-quantum-groups/chapters" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:5492:of Chapter~66) and apply to the $K3 \times E$ tower.
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3_times_e.tex:966:of Chapter~66) and apply to the $K3 \times E$ tower.
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3_times_e.tex:1073: construction (cf.\ Vol~I, Chapter~\ref{ch:holographic-datum-master})
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/cy_holographic_datum_master.tex:1006:in Vol~I, Chapter~\texttt{ch:genus1-seven-faces}.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/quantum_groups_foundations.tex:84:Drinfeld, ``Quantum groups'' (ICM Berkeley 1986), Theorem~2; see also Chari--Pressley, \emph{A Guide to Quantum Groups}, Chapter~4.2. The proof is a direct consequence of quasi-triangularity and the coassociativity of $\Delta$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:4700:\textup{(}Chapter~$4$, the connection on the
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_categories.tex:169:At $d = 2$ the enhancement is explicit enough to compute directly; it drives the $K3$ computations feeding the Borcherds denominator (Vol~III Chapter~\ref{ch:k3}). At $d = 3$ the enhancement was constructed by Sheridan~\cite{Sheridan2015} for the quintic threefold, as part of the HMS proof; the general $d = 3$ construction remains programme-level (conditional on $\bS^3$-framing, see AP-CY6).
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/braided_factorization.tex:89:fewer pole order than the OPE). See Volume~II, Chapter~11 for the
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-core.tex:3469:operads (Loday--Vallette \cite{LV12}, Chapter~10; generalized
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/hochschild.tex:913:\cite[Chapter~6]{CG17}:
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/hochschild.tex:1079:theorem~\cite[Chapter~6]{CG17}, a locally constant factorization
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/factorization_swiss_cheese.tex:2148:Lurie \cite{HA}, Chapter~5.5, with two strata: the open stratum
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_frontier.tex:83:In Chriss--Ginzburg \cite{chriss-ginzburg} Chapter~3, the orbit stratification
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/raviolo.tex:498:\emph{Absolute convergence.} Item~(b) asserts one-loop finiteness: all one-loop Feynman integrals converge in the HT gauge. For theories with $d' = 1$ topological direction, the power-counting of~\cite{GRW21} shows that this implies finiteness at \emph{all} loop orders: the superficial degree of divergence of an $L$-loop graph is $\delta = (1 - d')L = 0$ for $L = 0$ and $\delta < 0$ for $L \ge 2$, so the only potential divergences are at one loop, and these are finite by hypothesis. This power-counting bound applies to theories with propagator of type $(0,1)$ in the holomorphic direction and distributional in the topological direction. For such theories, the loop superficial degree of divergence is $\delta = (1-d')L$ where $d' = \dim_\C$ of the holomorphic factor; at $d' = 1$ this gives $\delta = 0$ for all $L$, so only logarithmic divergences can appear and these are removed by the one-loop renormalization hypothesis. See \cite[Chapter~9]{CG17} and \cite[Theorem~3.1]{GRW21} for the precise class of theories. After FM compactification of the holomorphic factor, the integrand acquires at worst logarithmic singularities along boundary divisors. Concretely:
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/dnp_identification_master.tex:540:Chapter~\texttt{ch:genus1-seven-faces}.
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/foundations_recast_draft.tex:721:\cite{BD04}, Chapter~3.
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/foundations_recast_draft.tex:732:Chapter~4).
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/locality.tex:284:Costello--Gwilliam~\cite[Chapter~5, \S5.4]{CG17} prove that a
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/relative_feynman_transform.tex:846:\cite{LV12}, Chapter~13.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/relative_feynman_transform.tex:1452:(Chriss--Ginzburg~\cite{CG97}, Chapter~8): the convolution

thinking
**Considering chapter references**

I’m thinking about whether I should count and check if that chapter number is stable. But then again, it’s not entirely necessary since the question specifically asks for the reference in a certain format. I guess I could just use whatever is high instead of overthinking it too much. It's probably better to focus on providing a clear response rather than getting caught up in details that might not matter.
exec
/bin/zsh -lc "rg -n 'input\\{chapters/connections/thqg_(preface_supplement|introduction_supplement_body)\\}|include\\{chapters/connections/thqg_(preface_supplement|introduction_supplement_body)\\}' /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_introduction_supplement.tex:223:\input{chapters/connections/thqg_introduction_supplement_body}

thinking
**Considering document content**

I’m looking at whether the intro supplement in thqg_introduction_supplement.tex should be included as a body. I’m wondering if it’s more appropriate as a main part or just a preface? It’s a bit unclear, so I need to think carefully about how to structure this document and ensure everything flows well. I’ll need to examine the content closely to decide the best course of action here!
exec
/bin/zsh -lc "rg -n 'thqg_introduction_supplement\\.tex|thqg_preface_supplement\\.tex' /Users/raeez/chiral-bar-cobar/main.tex /Users/raeez/chiral-bar-cobar/chapters /Users/raeez/chiral-bar-cobar/*.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

exec
/bin/zsh -lc "rg -n 'thqg_introduction_supplement\\.tex|thqg_preface_supplement\\.tex' /Users/raeez/chiral-bar-cobar" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Total output lines: 97

/Users/raeez/chiral-bar-cobar/metadata/label_index.json:8663:    "file": "chapters/connections/thqg_preface_supplement.tex",
/Users/raeez/chiral-bar-cobar/metadata/label_index.json:14199:    "file": "chapters/connections/thqg_preface_supplement.tex",
/Users/raeez/chiral-bar-cobar/metadata/label_index.json:14263:    "file": "chapters/connections/thqg_preface_supplement.tex",
/Users/raeez/chiral-bar-cobar/metadata/label_index.json:15327:    "file": "chapters/connections/thqg_preface_supplement.tex",
/Users/raeez/chiral-bar-cobar/metadata/label_index.json:17903:    "file": "chapters/connections/thqg_introduction_supplement.tex",
/Users/raeez/chiral-bar-cobar/metadata/label_index.json:17907:    "file": "chapters/connections/thqg_introduction_supplement.tex",
/Users/raeez/chiral-bar-cobar/metadata/label_index.json:17911:    "file": "chapters/connections/thqg_introduction_supplement.tex",
/Users/raeez/chiral-bar-cobar/metadata/label_index.json:17915:    "file": "chapters/connections/thqg_introduction_supplement.tex",
/Users/raeez/chiral-bar-cobar/metadata/label_index.json:17919:    "file": "chapters/connections/thqg_introduction_supplement.tex",
/Users/raeez/chiral-bar-cobar/metadata/label_index.json:17923:    "file": "chapters/connections/thqg_introduction_supplement.tex",
/Users/raeez/chiral-bar-cobar/metadata/label_index.json:17927:    "file": "chapters/connections/thqg_introduction_supplement.tex",
/Users/raeez/chiral-bar-cobar/metadata/label_index.json:17931:    "file": "chapters/connections/thqg_introduction_supplement.tex",
/Users/raeez/chiral-bar-cobar/metadata/label_index.json:17935:    "file": "chapters/connections/thqg_introduction_supplement.tex",
/Users/raeez/chiral-bar-cobar/metadata/label_index.json:39531:    "file": "chapters/connections/thqg_introduction_supplement.tex",
/Users/raeez/chiral-bar-cobar/metadata/label_index.json:42495:    "file": "chapters/connections/thqg_introduction_supplement.tex",
/Users/raeez/chiral-bar-cobar/metadata/label_index.json:44079:    "file": "chapters/connections/thqg_introduction_supplement.tex",
/Users/raeez/chiral-bar-cobar/metadata/label_index.json:44159:    "file": "chapters/connections/thqg_introduction_supplement.tex",
/Users/raeez/chiral-bar-cobar/metadata/label_index.json:44163:    "file": "chapters/connections/thqg_introduction_supplement.tex",

thinking
**Inspecting code findings**

It’s interesting that there’s a hardcoded part in AP13, and I’m noticing other potential findings around line 2017. The user asked me to read from file contents, so while audit notes may be secondary, they could still be useful. I think I should definitely take a closer look at that line since our regex didn’t capture the mixed reference. I should also explore patterns like `--VII` and search across those three repositories to find more similar instances.
codex
A second-order pattern showed up in the repo’s own audit artifacts: mixed ranges like `Parts~\ref{...}--VII`. I’m checking the live chapter files directly for that pattern before finalizing, since those are easy to miss with the first pass.
exec
/bin/zsh -lc "rg -n --glob '*.tex' 'Part[s]?~\\\\ref\\{part:["'^}]+'"\\}--[IVXLCDM]+' /Users/raeez/chiral-bar-cobar/chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --glob '*.tex' 'Part[s]?~\\\\ref\\{part:["'^}]+'"\\}--[IVXLCDM]+' /Users/raeez/chiral-bar-cobar-vol2/chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --glob '*.tex' 'Part[s]?~\\\\ref\\{part:["'^}]+'"\\}--[IVXLCDM]+' /Users/raeez/calabi-yau-quantum-groups/chapters" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

 succeeded in 51ms:
/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_preface_supplement.tex:2017:chapters of Parts~\ref{part:seven-faces}--VII of this monograph:
 exited 1 in 51ms:

exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar/chapters/connections/thqg_preface_supplement.tex | sed -n '2014,2019p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  2014	\bigskip
  2015	
  2016	The eight subsections of this section correspond to eight
  2017	chapters of Parts~\ref{part:seven-faces}--VII of this monograph:
  2018	
  2019	\begin{center}




thinking
**Assessing candidate search results**

I'm trying to evaluate the candidate search lists we looked at. In the Volume 1 references, there are 8 listed violations, and there's also a possibility of a false positive with 9102, plus some supplements included. I need to clarify how these violations impact our overall assessment. It feels like there’s a lot to unpack here, and I want to ensure I’m accurately counting and considering every detail for the user.
thinking
**Evaluating findings for severity**

I'm considering that I found 24 violations—8+3+13=24, which seems plausible. I might need to address some false positives related to literature citations and theorem markers. 

Next, I should categorize these 24 findings by severity. I wonder if I can combine some findings for inconsistencies across the same file. Since the user asked for each finding, I should keep it fairly concise—maybe around 50-70 lines total? 

I can organize them into severity groups like CRITICAL and HIGH, but maybe not LOW. I’ll keep it simple with each bullet including the file, line, and description. It’s essential to ensure this output is clear and structured.
thinking
**Considering chapter identification**

I'm thinking about how to locate `dnp_identification_master` in Vol2 by counting `\chapter{` instances. I wonder if I might script something to count file inclusions starting with `\chapter`. I have to keep in mind that some `\input`s might not be accounted for in chapter files. However, since `dnp_identification_master` is definitely labeled with `\chapter{...}`, if there are many prior chapters, then it’s likely not chapter number 11.
thinking
**Reviewing findings for accuracy**

The user asked me to confirm each finding, which I should definitely do. I’ll draft concise descriptions for clarity. It seems there's a critical issue with Volume I, specifically in `concordance.tex`, where `Volume II's Part VII` is numerically incorrect. I want to make sure my response is accurate and well-structured, as it’s important to address any mistakes clearly and concisely for the user’s understanding.
codex
- [CRITICAL] Vol I [concordance.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:3796) — `Volume~II's Part~VII` is numerically wrong. Vol II `main.tex` places ordered associative chiral Koszul duality, the dg-shifted factorization bridge, and the gravitational Yangian in Part II (`part:e1-core`), not Part VII.
- [CRITICAL] Vol I [ordered_associative_chiral_kd.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/ordered_associative_chiral_kd.tex:7549) — bare `Part~VII` is impossible locally: Vol I has only six parts, so this reference is both hardcoded and ambiguous/wrong.
- [CRITICAL] Vol III [cy_holographic_datum_master.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/connections/cy_holographic_datum_master.tex:922) — `Vol~I Part~III` is wrong in the seven-face bridge. Vol I’s seven-face programme is Part V (`part:seven-faces`), not Part III.
- [CRITICAL] Vol III [cy_holographic_datum_master.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/connections/cy_holographic_datum_master.tex:931) — same wrong Vol I numbering repeated in the enumerated summary: `Vol~I, Part~III` should point to Vol I Part V.
- [CRITICAL] Vol III [toroidal_elliptic.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:5492) — stale `Chapter~66`. The cited labels `sec:k3-sigma-model` and `sec:grand-synthesis-k3xe` now live in Vol III `toroidal_elliptic.tex`; this chapter number survived the move from Vol I.

- [HIGH] Vol III [k3_times_e.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3_times_e.tex:966) — duplicate stale `Chapter~66` in the merged-out `k3_times_e` surface; same migration drift as `toroidal_elliptic.tex`.
- [HIGH] Vol I [thqg_introduction_supplement_body.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_introduction_supplement_body.tex:1620) — hardcoded `Part~VII` is wrong locally; Vol I frontier is Part VI (`part:v1-frontier`).
- [HIGH] Vol I [thqg_preface_supplement.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_preface_supplement.tex:2017) — mixed dynamic/hardcoded range `Parts~\ref{part:seven-faces}--VII`; the upper endpoint should be a `\ref` to the frontier part, not literal `VII`.
- [HIGH] Vol I [thqg_preface_supplement.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_preface_supplement.tex:2055) — hardcoded `Part~VII` again; should point to Vol I frontier Part VI.
- [HIGH] Vol I [ordered_associative_chiral_kd.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/ordered_associative_chiral_kd.tex:5970) — hardcoded cross-volume `Volume~II, Part~VI`; should cite Vol II `part:gravity`.
- [HIGH] Vol I [ordered_associative_chiral_kd.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/ordered_associative_chiral_kd.tex:7752) — hardcoded cross-volume `Volume~II, Part~VII`; should cite Vol II `part:frontier`.
- [HIGH] Vol I [frontier_modular_holography_platonic.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/frontier_modular_holography_platonic.tex:1788) — hardcoded cross-volume `Vol~II, Part~IV`; should cite Vol II `part:examples`.
- [HIGH] Vol II [conclusion.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/conclusion.tex:987) — subsection title hardcodes `Part~VII` instead of using the local part label `part:frontier`.
- [HIGH] Vol II [conclusion.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/conclusion.tex:990) — hardcoded `Part~VII` and `Parts~I--VI`; both should be label-based (`part:frontier` and `part:swiss-cheese`--`part:gravity`).
- [HIGH] Vol III [introduction.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/introduction.tex:34) — hardcoded `Volume~II, Part~III`; should cite Vol II `part:bbl-core`.
- [HIGH] Vol III [introduction.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/introduction.tex:157) — hardcoded `Volume~I, Part~II`; should cite Vol I `part:characteristic-datum`.
- [HIGH] Vol III [quantum_group_reps.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:342) — hardcoded `Volume~II, Part~III`; should cite Vol II `part:bbl-core`.
- [HIGH] Vol III [quantum_group_reps.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:546) — hardcoded `Volume~I, Part~II`; should cite Vol I `part:characteristic-datum`.
- [HIGH] Vol III [toroidal_elliptic.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:94) — hardcoded `Vol~I, Part~I`; should cite Vol I `part:bar-complex`.
- [HIGH] Vol III [cy_holographic_datum_master.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/connections/cy_holographic_datum_master.tex:936) — hardcoded `Vol~II, Part~III`; should cite Vol II `part:bbl-core`.
- [HIGH] Vol III [cy_holographic_datum_master.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/connections/cy_holographic_datum_master.tex:1009) — internal `Part~V` is hardcoded; this should use Vol III `part:frontier`.
- [HIGH] Vol III [braided_factorization.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/braided_factorization.tex:89) — hardcoded `Volume~II, Chapter~11`; this should use a chapter label, not a literal chapter number.

- [MEDIUM] Vol II [dnp_identification_master.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/dnp_identification_master.tex:540) — raw label text `Chapter~\texttt{ch:genus1-seven-faces}` leaked into prose; should be `Chapter~\ref{ch:genus1-seven-faces}`.
- [MEDIUM] Vol III [cy_holographic_datum_master.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/connections/cy_holographic_datum_master.tex:1006) — same raw-label leak: `Chapter~\texttt{ch:genus1-seven-faces}` instead of `Chapter~\ref{ch:genus1-seven-faces}`.

Filtered out as non-violations: literature citations like `\cite[Chapter~5]{...}`, already-dynamic `Part~\ref{...}` / `Chapter~\ref{...}` references, and theorem-part markers like `Part~(i)` or `Part~A`.

## Summary
Instances checked: 28 | Violations found: 24 | Verdict: FAIL
tokens used
134,269
