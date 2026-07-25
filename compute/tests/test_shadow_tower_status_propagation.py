"""Status guards for the higher-shadow propagation surfaces."""

from __future__ import annotations

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[2]

PART_II = ROOT / "chapters/frame/part_ii_platonic_introduction.tex"
OPEN_TOWER = ROOT / "chapters/frame/open_beilinson_tower_platonic.tex"
ALL_TIER = ROOT / "chapters/theory/all_tier_generating_function_platonic.tex"
MOTIVIC = ROOT / "chapters/theory/virasoro_motivic_purity.tex"
KUMMER = ROOT / "chapters/theory/higher_kummer_arithmetic_duality_platonic.tex"


def source(path: Path) -> str:
    return path.read_text()


def labels(path: Path) -> list[str]:
    return re.findall(r"\\label\{([^}]+)\}", source(path))


def window(path: Path, start: str, end: str) -> str:
    text = source(path)
    left = text.index(start)
    right = text.index(end, left)
    return text[left:right]


class TestRetainedSurfaces:
    def test_label_counts_and_uniqueness(self):
        expected = {
            PART_II: 31,
            OPEN_TOWER: 1,
            ALL_TIER: 33,
            MOTIVIC: 24,
            KUMMER: 12,
        }
        for path, count in expected.items():
            found = labels(path)
            assert len(found) == count
            assert len(found) == len(set(found))

    def test_retired_numeric_fingerprints_are_absent(self):
        combined = "\n".join(source(path) for path in (
            PART_II,
            OPEN_TOWER,
            ALL_TIER,
            MOTIVIC,
            KUMMER,
        ))
        for fragment in (
            "45c+193",
            "45c + 193",
            "240c+1031",
            "240c + 1031",
            "4144720",
            "19683",
            "8(-6)^{r-4}",
            r"C_{\Vir}=6",
            r"C_{\Vir} = 6",
            "radius of convergence~$1/6$",
            r"\ref{thm:virasoro-shadow-recurrence}",
            r"\ref{thm:shadow-tower-asymptotic-closed-form}",
            r"\ref{thm:shadow-tower-subleading-closed-form}",
            r"\ref{thm:shadow-tower-tier-4-closed-form}",
        ):
            assert fragment not in combined


class TestFrontMatterPropagation:
    def test_part_ii_uses_open_residue_and_motivic_packages(self):
        text = source(PART_II)
        for fragment in (
            r"\mathsf H_{\mathrm{res}}",
            r"\mathsf H_{\mathrm{mot}}^{\le8}",
            r"\mathsf H_{\mathrm{Tate}}^{\le8}",
            r"\ClaimStatusOpen",
            r"\operatorname{pr}_6(s_{\Vir_c})",
        ):
            assert fragment in text
        motivic = window(
            PART_II,
            r"\section{Motivic residue comparison}",
            r"\section{Chiral moonshine via fingerprint}",
        )
        assert r"\ClaimStatusProvedHere" not in motivic

    def test_open_tower_treats_growth_as_an_analytic_problem(self):
        text = source(OPEN_TOWER)
        assert r"\mathsf H_{\mathrm{res}}+\mathsf H_{\mathrm{asymp}}" in text
        assert r"\mathsf H_{\mathrm{Ricc}\to\mathrm{res}}" in text
        assert r"N_\Lambda(c)=c(5c+22)/10" in text


class TestTheoryPropagation:
    def test_all_tier_surface_is_open_and_typed(self):
        text = source(ALL_TIER)
        assert r"\ClaimStatusProvedHere" not in text
        assert text.count(r"\begin{problem}") == 3
        assert text.count(r"\ClaimStatusOpen") == 4
        for fragment in (
            r"\mathsf H_{\mathrm{res}}",
            r"\mathsf H_{\mathrm{quad}}",
            r"\mathsf H_{\mathrm{asymp}}",
            r"\mathsf H_{\mathrm{arith}}",
            r"\mathsf H_{\mathrm{ODE}}",
        ):
            assert fragment in text

    def test_motivic_surface_requires_chain_map_and_tate_factorization(self):
        text = source(MOTIVIC)
        main = window(
            MOTIVIC,
            r"\begin{theorem}[Tate-factorization criterion",
            r"\section{Denominator and growth obligations}",
        )
        assert r"\ClaimStatusConditional" in main
        assert r"\mathsf H_{\mathrm{res}}" in main
        assert r"\mathsf H_{\mathrm{mot}}" in main
        assert r"\mathsf H_{\mathrm{Tate}}" in main
        assert "reduced positive-weight motivic coaction vanishes" in main
        denominator = window(
            MOTIVIC,
            r"\begin{problem}[Determine the divisor",
            r"\section{Rational transfer as a conditional algebraic statement}",
        )
        assert r"\ClaimStatusOpen" in denominator

    def test_kummer_keeps_bernoulli_theorem_and_opens_residue_comparison(self):
        text = source(KUMMER)
        exact = window(
            KUMMER,
            r"\begin{theorem}[Kummer-irregular primes",
            r"\section{The Virasoro coefficient census}",
        )
        assert r"\ClaimStatusProvedHere" in exact
        shadow = window(
            KUMMER,
            r"\begin{problem}[Compute the Virasoro prime census",
            r"\section{Finite Bernoulli--Virasoro comparison}",
        )
        assert r"\ClaimStatusOpen" in shadow
        assert r"\mathsf H_{\mathrm{Kum}}^{\le13}" in shadow
        assert r"\mathcal P_{\le13}\cap\mathrm{IrrKum}_{\le22}=\varnothing" in shadow
