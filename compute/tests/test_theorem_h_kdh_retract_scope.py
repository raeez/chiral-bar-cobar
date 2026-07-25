"""Guards for the finite-window KDH deformation-retract surface."""

from __future__ import annotations

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[2]
THEOREM_H = ROOT / "chapters/theory/theorem_h_off_koszul_platonic.tex"


def visible(path: Path) -> str:
    return "\n".join(
        line
        for line in path.read_text().splitlines()
        if not line.lstrip().startswith("%")
    )


def normalized(text: str) -> str:
    return re.sub(r"\s+", " ", text)


def environment_block(text: str, label: str, environment: str) -> str:
    anchor = rf"\label{{{label}}}"
    label_pos = text.index(anchor)
    start = text.rfind(rf"\begin{{{environment}}}", 0, label_pos)
    end = text.index(rf"\end{{{environment}}}", label_pos)
    return text[start : end + len(rf"\end{{{environment}}}")]


def test_finite_window_kdh_retract_states_every_comparison_map():
    text = visible(THEOREM_H)
    proposition = normalized(
        environment_block(
            text,
            "prop:theorem-h-finite-window-kdh-retracts",
            "proposition",
        )
    )

    required = (
        "Compatible finite-window retracts of the positive-depth complex",
        r"\ClaimStatusProvedHere",
        "finite positive-depth windows, compatible deformation retracts, a finite support set~$S$, and surjective weight transitions",
        r"K_N^\bullet :=\mathrm{KD}_{\mathrm H}^{\bullet}(\cA)/ F_{>N}^{\mathrm{wt}}\mathrm{KD}_{\mathrm H}^{\bullet}(\cA)",
        r"\mathrm{KD}_{\mathrm H}^{\bullet}(\cA) \;\cong\; \varprojlim_N K_N^\bullet",
        r"\pi_{N+1,N}\colon K_{N+1}^\bullet\twoheadrightarrow K_N^\bullet",
        r"i_N\colon L_N^\bullet\longrightarrow K_N^\bullet",
        r"p_N\colon K_N^\bullet\longrightarrow L_N^\bullet",
        r"h_N\colon K_N^\bullet\to K_N^{\bullet-1}",
        r"p_Ni_N=\mathrm{id}_{L_N}",
        r"d_Nh_N+h_Nd_N=\mathrm{id}_{K_N}-i_Np_N",
        r"\pi_{N+1,N}i_{N+1}=i_N\rho_{N+1,N}",
        r"\rho_{N+1,N}p_{N+1}=p_N\pi_{N+1,N}",
        r"\pi_{N+1,N}h_{N+1}=h_N\pi_{N+1,N}",
        r"H^n\!\bigl(\mathrm{KD}_{\mathrm H}^{\bullet}(\cA)\bigr)=0 \qquad(n\notin S)",
        "These data construct the positive-depth component of a family support model",
        r"complete the package $H_H(\cA;S)$",
    )
    for fragment in required:
        assert normalized(fragment) in proposition, fragment



def test_retract_proof_closes_finite_windows_and_the_inverse_limit():
    text = visible(THEOREM_H)
    label = r"\label{prop:theorem-h-finite-window-kdh-retracts}"
    label_pos = text.index(label)
    proposition_end = text.index(r"\end{proposition}", label_pos)
    proof_start = text.index(r"\begin{proof}", proposition_end)
    proof_end = text.index(r"\end{proof}", proof_start)
    proof = normalized(text[proof_start:proof_end])

    required = (
        r"x=(d_Nh_N+h_Nd_N)x=d_Nh_Nx",
        r"H^n(K_N^\bullet)=0",
        r"L^\bullet:=\varprojlim_N L_N^\bullet",
        r"K^\bullet:=\varprojlim_N K_N^\bullet",
        r"dh+hd=\mathrm{id}_{K}-ip",
        "the inverse system is strict Mittag--Leffler",
        "Milnor exact sequence",
        r"H^{n-1}(K_M^\bullet)",
        "stabilizes inside the finite-dimensional vector space",
    )
    for fragment in required:
        assert normalized(fragment) in proof, fragment


def test_theorem_h_boundary_names_family_realization_and_low_columns():
    text = normalized(visible(THEOREM_H))
    required = (
        r"Proposition~\ref{prop:theorem-h-finite-window-kdh-retracts}",
        "transition maps, and triples $(i_N,p_N,h_N)$",
        r"$H_H(\cA;S)$",
        "bounded-to-chart quasi-isomorphism",
        r"\ClaimStatusConditional",
    )
    for fragment in required:
        assert normalized(fragment) in text, fragment
