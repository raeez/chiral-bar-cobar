"""Tests for the universal chiral algebra invariant machine.

Verifies computed invariants against Master Table ground truth
(examples_summary.tex) and CLAUDE.md verified formulas.
"""

import pytest
from sympy import Rational, Symbol, simplify

from compute.lib.chiral_invariant_machine import (
    ChiralInvariantMachine,
    InvariantPackage,
    compute_all_invariants,
    master_table_verification,
    extract_bracket_relations,
    extract_curvature,
    check_pbw_koszulness,
    compute_kappa_from_registry,
    check_bar_gf_algebraicity,
)
from compute.lib.bar_complex import (
    KNOWN_BAR_DIMS, sl2_algebra, heisenberg_algebra, virasoro_algebra,
)
from compute.lib.cross_algebra import ALGEBRA_REGISTRY
from compute.lib.bar_gf_solver import bar_dims_sl2, bar_dims_virasoro


# ===================================================================
# Basic pipeline tests
# ===================================================================

class TestMachineBasics:
    """Test that the machine runs for all registered algebras."""

    @pytest.mark.parametrize("name", list(ALGEBRA_REGISTRY.keys()))
    def test_machine_runs(self, name):
        machine = ChiralInvariantMachine(name)
        pkg = machine.compute()
        assert isinstance(pkg, InvariantPackage)
        assert pkg.name == name
        assert pkg.n_generators > 0

    @pytest.mark.parametrize("name", list(ALGEBRA_REGISTRY.keys()))
    def test_summary_string(self, name):
        machine = ChiralInvariantMachine(name)
        pkg = machine.compute()
        s = pkg.summary()
        assert name in s
        assert "Generators" in s


# ===================================================================
# Bar cohomology verification
# ===================================================================

class TestBarCohomology:
    """Verify bar cohomology dims match Master Table."""

    def test_heisenberg_bar_dims(self):
        pkg = ChiralInvariantMachine("Heisenberg").compute()
        assert pkg.bar_dims[1] == 1
        assert pkg.bar_dims[2] == 1  # p(0) = 1
        assert pkg.bar_dims[3] == 1  # p(1) = 1
        assert pkg.bar_dims[4] == 2  # p(2) = 2

    def test_sl2_bar_dims_riordan(self):
        """sl₂ bar cohomology = Riordan R(n+3)."""
        pkg = ChiralInvariantMachine("sl2").compute()
        expected = bar_dims_sl2(7)  # [3, 6, 15, 36, 91, 232, 603]
        for i, val in enumerate(expected):
            assert pkg.bar_dims[i + 1] == val, f"H^{i+1} mismatch"

    def test_virasoro_bar_dims_motzkin(self):
        """Virasoro bar cohomology = M(n+1) - M(n)."""
        pkg = ChiralInvariantMachine("Virasoro").compute()
        expected = bar_dims_virasoro(7)  # [1, 2, 5, 12, 30, 76, 196]
        for i, val in enumerate(expected):
            assert pkg.bar_dims[i + 1] == val, f"H^{i+1} mismatch"

    def test_sl3_bar_dims(self):
        pkg = ChiralInvariantMachine("sl3").compute()
        assert pkg.bar_dims[1] == 8
        assert pkg.bar_dims[2] == 36
        assert pkg.bar_dims[3] == 204

    def test_free_fermion_bar_dims(self):
        pkg = ChiralInvariantMachine("free_fermion").compute()
        # p(n-1): p(0)=1, p(1)=1, p(2)=2, p(3)=3
        assert pkg.bar_dims[1] == 1
        assert pkg.bar_dims[2] == 1
        assert pkg.bar_dims[3] == 2

    def test_beta_gamma_bar_dims(self):
        pkg = ChiralInvariantMachine("beta_gamma").compute()
        assert pkg.bar_dims[1] == 2
        assert pkg.bar_dims[2] == 4
        assert pkg.bar_dims[3] == 10
        assert pkg.bar_dims[4] == 26

    def test_bc_bar_dims(self):
        """bc bar dims = 2^n - n + 1."""
        pkg = ChiralInvariantMachine("bc").compute()
        for n in range(1, 8):
            assert pkg.bar_dims[n] == 2**n - n + 1

    def test_w3_bar_dims(self):
        pkg = ChiralInvariantMachine("W3").compute()
        assert pkg.bar_dims[1] == 2
        assert pkg.bar_dims[2] == 5
        assert pkg.bar_dims[3] == 16


# ===================================================================
# Koszulness tests
# ===================================================================

class TestKoszulness:
    """Test PBW Koszulness determination."""

    @pytest.mark.parametrize("name", ["sl2", "sl3", "E8", "B2", "G2"])
    def test_km_koszul(self, name):
        pkg = ChiralInvariantMachine(name).compute()
        assert pkg.pbw_koszul is True
        assert "KM" in pkg.koszul_method or "Priddy" in pkg.koszul_method

    def test_heisenberg_koszul(self):
        pkg = ChiralInvariantMachine("Heisenberg").compute()
        assert pkg.pbw_koszul is True

    def test_virasoro_koszul(self):
        pkg = ChiralInvariantMachine("Virasoro").compute()
        assert pkg.pbw_koszul is True

    @pytest.mark.parametrize("name", ["free_fermion", "beta_gamma", "bc"])
    def test_free_field_koszul(self, name):
        pkg = ChiralInvariantMachine(name).compute()
        assert pkg.pbw_koszul is True

    def test_w3_conjectured(self):
        pkg = ChiralInvariantMachine("W3").compute()
        assert pkg.pbw_koszul is None  # conjectured, not proved

    def test_koszulness_via_ope(self):
        """Test Koszulness from OPE data (not just registry)."""
        alg = sl2_algebra()
        result, method = check_pbw_koszulness(alg)
        assert result is True


# ===================================================================
# Kappa tests
# ===================================================================

class TestKappa:
    """Verify obstruction coefficient κ."""

    def test_heisenberg_kappa(self):
        kap = compute_kappa_from_registry("Heisenberg")
        assert kap == Symbol("kappa")

    def test_sl2_kappa(self):
        """κ(sl₂_k) = 3(k+2)/4."""
        kap = compute_kappa_from_registry("sl2")
        k = Symbol("k")
        assert simplify(kap - 3*(k+2)/4) == 0

    def test_sl3_kappa(self):
        """κ(sl₃_k) = 4(k+3)/3."""
        kap = compute_kappa_from_registry("sl3")
        k = Symbol("k")
        assert simplify(kap - 4*(k+3)/3) == 0

    def test_virasoro_kappa(self):
        """κ(Vir_c) = c/2."""
        kap = compute_kappa_from_registry("Virasoro")
        c = Symbol("c")
        assert simplify(kap - c/2) == 0

    def test_w3_kappa(self):
        """κ(W₃_c) = 5c/6."""
        kap = compute_kappa_from_registry("W3")
        c = Symbol("c")
        assert simplify(kap - 5*c/6) == 0

    def test_g2_kappa(self):
        """κ(G₂_k) = 7(k+4)/4."""
        kap = compute_kappa_from_registry("G2")
        k = Symbol("k")
        assert simplify(kap - 7*(k+4)/4) == 0

    def test_b2_kappa(self):
        """κ(B₂_k) = 5(k+3)/3."""
        kap = compute_kappa_from_registry("B2")
        k = Symbol("k")
        assert simplify(kap - 5*(k+3)/3) == 0


# ===================================================================
# Complementarity tests
# ===================================================================

class TestComplementarity:
    """Verify κ(A) + κ(A!) = 0 for KM (level-independent)."""

    @pytest.mark.parametrize("name", ["sl2", "sl3", "B2", "G2", "E8"])
    def test_km_complementarity_zero(self, name):
        """For KM: κ + κ' = 0 (identically in k)."""
        pkg = ChiralInvariantMachine(name).compute()
        assert pkg.kappa_sum is not None
        assert simplify(pkg.kappa_sum) == 0

    def test_virasoro_complementarity(self):
        """For Virasoro: κ + κ' = 13."""
        pkg = ChiralInvariantMachine("Virasoro").compute()
        assert pkg.kappa_sum == 13

    def test_w3_complementarity(self):
        """For W₃: κ + κ' = 250/3."""
        pkg = ChiralInvariantMachine("W3").compute()
        assert pkg.kappa_sum == Rational(250, 3)


# ===================================================================
# Genus expansion tests
# ===================================================================

class TestGenusExpansion:
    """Verify genus expansion F_g = κ · λ_g^FP."""

    def test_genus1_heisenberg(self):
        """F_1(H_κ) = κ · λ_1 = κ/24 (Bernoulli B_2 = 1/6)."""
        from compute.lib.utils import lambda_fp
        lam1 = lambda_fp(1)
        # λ_1 = (2^1-1)/2^1 * |B_2|/2! = 1/2 * 1/6 / 2 = 1/24
        assert lam1 == Rational(1, 24)

    def test_genus1_sl2(self):
        """F_1(sl₂_k) = 3(k+2)/4 · 1/24 = (k+2)/32."""
        pkg = ChiralInvariantMachine("sl2").compute()
        k = Symbol("k")
        expected = 3*(k+2)/4 * Rational(1, 24)
        assert simplify(pkg.genus_table[1] - expected) == 0

    def test_genus1_virasoro(self):
        """F_1(Vir_c) = c/2 · 1/24 = c/48."""
        pkg = ChiralInvariantMachine("Virasoro").compute()
        c = Symbol("c")
        expected = c / 48
        assert simplify(pkg.genus_table[1] - expected) == 0


# ===================================================================
# Spectral discriminant tests
# ===================================================================

class TestDiscriminant:
    """Verify spectral discriminant Δ_A."""

    def test_shared_discriminant(self):
        """sl₂, Virasoro, βγ share Δ = 1-2x-3x² = (1-3x)(1+x)."""
        for name in ["sl2", "Virasoro", "beta_gamma"]:
            pkg = ChiralInvariantMachine(name).compute()
            assert pkg.discriminant is not None
            assert "1-3x" in pkg.discriminant.replace(" ", "").replace("−", "-")

    def test_heisenberg_trivial_discriminant(self):
        pkg = ChiralInvariantMachine("Heisenberg").compute()
        assert pkg.discriminant is not None
        assert "1" in pkg.discriminant


# ===================================================================
# Curvature tests
# ===================================================================

class TestCurvature:
    """Verify curvature extraction from OPE data."""

    def test_heisenberg_curved(self):
        pkg = ChiralInvariantMachine("Heisenberg").compute()
        assert pkg.is_curved is True

    def test_free_fermion_uncurved(self):
        pkg = ChiralInvariantMachine("free_fermion").compute()
        assert pkg.is_curved is False

    def test_sl2_curved(self):
        pkg = ChiralInvariantMachine("sl2").compute()
        assert pkg.is_curved is True

    @pytest.mark.parametrize("name", ["free_fermion", "beta_gamma", "bc"])
    def test_free_field_uncurved(self, name):
        pkg = ChiralInvariantMachine(name).compute()
        assert pkg.is_curved is False

    def test_curvature_from_ope(self):
        """Extract curvature from OPE algebra object."""
        alg = sl2_algebra(k=Symbol("k"))
        curv = extract_curvature(alg)
        assert curv["has_curvature"] is True
        assert len(curv["curvature_sources"]) > 0


# ===================================================================
# Spectral sequence collapse tests
# ===================================================================

class TestCollapse:
    """Verify spectral sequence collapse pages."""

    @pytest.mark.parametrize("name,page", [
        ("Heisenberg", 1),
        ("sl2", 1), ("sl3", 1), ("E8", 1), ("B2", 1), ("G2", 1),
        ("Virasoro", 2),
        ("free_fermion", 2), ("beta_gamma", 2), ("bc", 2),
    ])
    def test_collapse_page(self, name, page):
        pkg = ChiralInvariantMachine(name).compute()
        assert pkg.collapse_page == page


# ===================================================================
# Bar GF algebraicity tests
# ===================================================================

class TestBarGFAlgebraicity:
    """Test bar generating function algebraicity detection."""

    def test_sl2_algebraic(self):
        """sl₂ bar GF is algebraic of degree 2."""
        dims = {n: d for n, d in KNOWN_BAR_DIMS["sl2"].items() if n <= 7}
        result = check_bar_gf_algebraicity(dims)
        assert result["algebraic"] is True
        assert result["degree"] == 2

    def test_virasoro_algebraic(self):
        """Virasoro bar GF is algebraic of degree 2."""
        dims = {n: d for n, d in KNOWN_BAR_DIMS["Virasoro"].items() if n <= 7}
        result = check_bar_gf_algebraicity(dims)
        assert result["algebraic"] is True
        assert result["degree"] == 2

    def test_beta_gamma_algebraic(self):
        """βγ bar GF = √((1+x)/(1-3x)) is algebraic of degree 2."""
        dims = {n: d for n, d in KNOWN_BAR_DIMS["beta_gamma"].items() if n <= 7}
        result = check_bar_gf_algebraicity(dims)
        assert result["algebraic"] is True
        assert result["degree"] == 2


# ===================================================================
# OPE extraction tests
# ===================================================================

class TestOPEExtraction:
    """Test bracket and curvature extraction from OPE data."""

    def test_sl2_bracket_relations(self):
        """sl₂ has 3 generators, 3 antisymmetric relations."""
        alg = sl2_algebra()
        d, relations = extract_bracket_relations(alg)
        assert d == 3
        assert relations.shape[0] == 3  # C(3,2) = 3 antisymmetric relations

    def test_heisenberg_no_bracket(self):
        """Heisenberg has no simple pole → no bracket relations."""
        alg = heisenberg_algebra()
        d, relations = extract_bracket_relations(alg)
        assert d == 1
        assert relations.shape[0] == 0  # C(1,2) = 0


# ===================================================================
# Master Table integration
# ===================================================================

class TestMasterTableIntegration:
    """Full cross-check against Master Table."""

    def test_master_table_all_pass(self):
        """All Master Table verification checks should pass."""
        results = master_table_verification()
        for name, checks in results.items():
            for check_name, ok in checks.items():
                assert ok, f"{name}: {check_name} FAILED"

    def test_all_algebras_computed(self):
        """All 11 registered algebras produce packages."""
        packages = compute_all_invariants()
        assert len(packages) == 11
        for name in ALGEBRA_REGISTRY:
            assert name in packages


# ===================================================================
# Koszul dual name tests
# ===================================================================

class TestKoszulDualNames:
    """Verify Koszul dual identifications from CLAUDE.md."""

    def test_heisenberg_not_self_dual(self):
        pkg = ChiralInvariantMachine("Heisenberg").compute()
        assert pkg.koszul_dual_name == "Sym^ch(V*)"

    def test_free_fermion_dual_beta_gamma(self):
        pkg = ChiralInvariantMachine("free_fermion").compute()
        assert pkg.koszul_dual_name == "beta_gamma"

    def test_bc_dual_beta_gamma(self):
        pkg = ChiralInvariantMachine("bc").compute()
        assert pkg.koszul_dual_name == "beta_gamma"

    def test_beta_gamma_dual_bc(self):
        pkg = ChiralInvariantMachine("beta_gamma").compute()
        assert pkg.koszul_dual_name == "bc"
