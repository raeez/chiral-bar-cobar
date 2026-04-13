# F16_undefined_macros_v1 (current rerun)

## Findings

- [CRITICAL] `standalone/introduction_full_survey.tex:280` — PROBLEM: `\dzero` is used for the genus-0 bar differential, but the standalone preamble never defines `\dzero`. FIX: add `\providecommand{\dzero}{d_0}` to the local macro block.

- [CRITICAL] `standalone/introduction_full_survey.tex:422` — PROBLEM: `\Hom` and `\End` are used in the modular convolution formulas at lines `422`, `436`, and `485`, but neither macro is declared in this standalone preamble. FIX: add `\DeclareMathOperator{\Hom}{Hom}` and `\DeclareMathOperator{\End}{End}` to the operator block.

- [CRITICAL] `standalone/introduction_full_survey.tex:483` — PROBLEM: `\Res` is used in the cyclic-trace formula, but no local macro defines it. FIX: add `\DeclareMathOperator{\Res}{Res}` to the operator block.

- [CRITICAL] `standalone/introduction_full_survey.tex:566` — PROBLEM: `\id` is used in `\operatorname{av} \circ s = \id`, but the preamble has no `\id` macro. FIX: add `\providecommand{\id}{\mathrm{id}}`.

- [CRITICAL] `standalone/introduction_full_survey.tex:1217` — PROBLEM: `\R` is used repeatedly for the real line/configuration-space discussion, but only `\bR` is defined locally. FIX: add `\providecommand{\R}{\mathbb{R}}` or replace each occurrence by `\bR`.

- [CRITICAL] `standalone/introduction_full_survey.tex:1106` — PROBLEM: `\llbracket` and `\rrbracket` are used in `\Bbbk\llbracket x \rrbracket`, but this standalone file does not load a package that defines those bracket macros. FIX: add `\usepackage{stmaryrd}` to the preamble.

- [CRITICAL] `standalone/introduction_full_survey.tex:5061` — PROBLEM: `\chirAss`, `\chirtensor`, `\chirLie`, and `\chirCom` are used at lines `5061-5163`, but none of these macros is defined in the standalone preamble. FIX: add local definitions such as `\providecommand{\chirAss}{\mathrm{Ass}^{\mathrm{ch}}}`, `\providecommand{\chirtensor}{\otimes^{\mathrm{ch}}}`, `\providecommand{\chirLie}{\mathrm{Lie}^{\mathrm{ch}}}`, and `\providecommand{\chirCom}{\mathrm{Com}^{\mathrm{ch}}}`.

- [HIGH] `standalone/N2_mc3_all_types.tex:391` — PROBLEM: `\cF` is used in the filtration notation `\cF^{\ge N}`, but the local macro block defines no `\cF`. FIX: add `\newcommand{\cF}{\mathcal{F}}` alongside the other calligraphic macros.

- [HIGH] `standalone/N3_e1_primacy.tex:346` — PROBLEM: `\BarchFG` is used for the Francis--Gaitsgory bar complex, but the file defines only `\Barch`, `\Barord`, `\BarSig`, and `\Cobar`. FIX: add `\newcommand{\BarchFG}{\overline{B}^{\mathrm{ch},\mathrm{FG}}}` to the local macro block.

- [HIGH] `standalone/programme_summary.tex:1047` — PROBLEM: `\ChirHoch` is used in Theorem H, but the standalone preamble never defines it. FIX: add `\newcommand{\ChirHoch}{\mathrm{ChirHoch}}` to the macro section.

- [HIGH] `standalone/survey_modular_koszul_duality_v2.tex:710` — PROBLEM: `\ord` is used in `\Ran^{\ord}(X)` and `\barB^{\ord}`, but the standalone preamble contains no `\ord` macro. FIX: add `\DeclareMathOperator{\ord}{ord}`.

- [HIGH] `standalone/survey_modular_koszul_duality_v2.tex:6676` — PROBLEM: `\Ydg` is used for the line dual in the non-abelian CS datum, but the standalone preamble never defines it. FIX: add a local macro, e.g. `\newcommand{\Ydg}{Y^{\mathrm{dg}}}` or the intended notation.

## Summary

Checked: `standalone/*.tex` by macro-use grep plus local preamble reread on the files with live misses | Findings: 12 | Verdict: FAIL
