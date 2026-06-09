from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def test_w_algebras_agt_shadow_decomposition_types_scalar_source():
    text = (ROOT / "chapters/examples/w_algebras.tex").read_text()
    squashed = " ".join(text.split())

    required_forms = (
        "\\kappa(\\mathcal{W}_N) = c \\cdot (H_N - 1)",
        "K^\\kappa=\\kappa(A)+\\kappa(A^!)",
        "\\kappa(\\mathcal W_3^k)=c/2+c/3=5c/6",
        (
            "\\kappa(\\mathcal W_3^k)+\\kappa((\\mathcal W_3^k)^!)"
            "=250/3"
        ),
        (
            "\\kappa(\\mathcal W_3^k)+\\kappa((\\mathcal W_3^k)^!) "
            "= 5c/6 + 5(100-c)/6 = 250/3"
        ),
        "\\kappa(\\mathcal W_3^k)=\\kappa((\\mathcal W_3^k)^!)=125/3",
        "F_g^{\\mathrm{Nek}}(\\vec a,q) =F_g^{\\mathrm{sc}}(\\mathcal W_N)",
        "+\\delta F_g^{\\mathrm{cross}}(\\mathcal W_N)",
        "+F_g^{\\mathrm{rep}}(\\vec a,q)",
        "F_g^{\\mathrm{sc}}(\\mathcal W_N) =\\kappa(\\mathcal W_N)\\lambda_g^{\\mathrm{FP}}",
        "\\kappa(\\mathcal{W}_N^k) = c \\cdot (H_N - 1)",
        (
            "\\mathrm{obs}_1(\\mathcal W_N^k) "
            "=\\kappa(\\mathcal W_N^k)\\lambda_1"
        ),
        (
            "\\mathrm{obs}_g(\\mathrm{Vir}_c) "
            "=\\kappa(\\mathrm{Vir}_c)\\lambda_g"
        ),
        (
            "\\mathrm{obs}_g(\\mathrm{Vir}_c)=\\kappa(\\mathrm{Vir}_c)"
            "\\lambda_g"
        ),
        "The first summand is the scalar shadow amplitude",
        (
            "the scalar part of the Nekrasov genus expansion reduces "
            "to the constant-map contribution"
        ),
        "\\kappa(\\mathcal W_N)\\lambda_g^{\\mathrm{FP}}",
    )
    for required in required_forms:
        assert required in squashed

    stale_forms = (
        "F_g = \\kappa \\cdot \\lambda_g^{\\mathrm{FP}}",
        "\\kappa \\cdot \\lambda_g^{\\mathrm{FP}}",
        "\\bigl(\\mathrm{ALL\\mbox{-}WEIGHT} + \\delta F_g^{\\mathrm{cross}}\\bigr)",
        "The leading \\textup{(}universal\\textup{)} term",
        "is the shadow amplitude $F_g(\\mathcal{W}_N)$",
        "\\mathrm{obs}_g = \\kappa \\cdot \\lambda_g",
        "$\\mathrm{obs}_g = \\kappa \\cdot \\lambda_g$",
        "\\mathrm{obs}_1 = \\kappa \\cdot \\lambda_1",
        "\\mathrm{obs}_1=\\kappa\\lambda_1",
        "\\kappa + \\kappa' = 250/3",
        "\\kappa + \\kappa' = 13",
        "\\kappa + \\kappa' = 0",
        "\\kappa + \\kappa' = 13 \\cdot 246/12",
        "\\kappa + \\kappa' = 77 \\cdot 488/60",
    )
    for stale in stale_forms:
        assert stale not in squashed
