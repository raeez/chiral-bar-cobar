import sympy as sp

from compute.lib.averaging_kernel_sl2_genus1_engine import (
    K,
    SL2_ANTISYMMETRIC_DIM,
    SL2_BASIS,
    SL2_CASIMIR_AVERAGE_WEIGHT,
    SL2_SUGAWARA_SHIFT,
    SL2_SYMMETRIC_DIM,
    TENSOR_DIM,
    Z,
    ZETA,
    affine_genus1_average,
    averaging_map_of_elliptic_r_matrix,
    antisymmetric_sector_of_r,
    antisymmetrization_projector,
    casimir_tensor,
    classical_average_from_symmetric_casimir,
    elliptic_r_matrix,
    exterior_square_basis,
    generic_antisymmetric_part,
    is_zero_tensor,
    kappa_sl2,
    project_antisymmetric,
    project_symmetric,
    summarize_averaging_kernel,
    supports_level_prefix,
    symmetric_sector_of_r,
    symmetrization_projector,
    zero_tensor,
)

RESULT = summarize_averaging_kernel()


class TestAveragingKernelSL2Genus1Engine:
    def test_tensor_dimensions_and_projector(self) -> None:
        projector = symmetrization_projector()
        antisymmetrizer = antisymmetrization_projector()

        assert len(SL2_BASIS) == 3
        assert TENSOR_DIM == 9
        assert projector * projector == projector
        assert antisymmetrizer * antisymmetrizer == antisymmetrizer
        assert projector + antisymmetrizer == sp.eye(TENSOR_DIM)

        # VERIFIED [DC][SY]: explicit 9x9 projector rank and 3⊗3 = Sym^2 ⊕ Lambda^2.
        assert RESULT.symmetric_dim == SL2_SYMMETRIC_DIM == 6
        # VERIFIED [DC][SY]: rank-nullity for the symmetrization projector on sl_2 ⊗ sl_2.
        assert RESULT.projector_rank == 6
        # VERIFIED [DC][SY]: ker(av) = Lambda^2(sl_2), so the kernel has dimension 3.
        assert RESULT.kernel_dim == SL2_ANTISYMMETRIC_DIM == 3

        nullspace = projector.nullspace()
        assert len(nullspace) == 3
        assert antisymmetrizer.rank() == 3

    def test_kernel_is_exterior_square(self) -> None:
        kernel_basis = exterior_square_basis()

        # VERIFIED [DC][SY]: e∧f, e∧h, f∧h form the standard basis of Lambda^2(sl_2).
        assert len(kernel_basis) == 3
        assert sp.Matrix.hstack(*kernel_basis).rank() == 3

        for vector in kernel_basis:
            assert project_symmetric(vector) == zero_tensor()
            assert project_antisymmetric(vector) == vector

    def test_casimir_is_symmetric(self) -> None:
        omega = casimir_tensor()

        # VERIFIED [DC][SY]: Omega = h⊗h/2 + e⊗f + f⊗e is fixed by swap and has no alternating part.
        assert project_symmetric(omega) == omega
        assert project_antisymmetric(omega) == zero_tensor()

    def test_elliptic_r_matrix_has_level_prefix_and_zero_level_vanishes(self) -> None:
        antisymmetric_part = generic_antisymmetric_part()
        r_matrix = elliptic_r_matrix(level=K, z=Z, antisymmetric_part=antisymmetric_part)

        # VERIFIED [SY][LC]: the module defines r^ell(z) = k*(zeta(z)*Omega + antisym_part), so every term carries k.
        assert supports_level_prefix(r_matrix, K)
        # VERIFIED [LC][DC]: substituting k = 0 kills the entire elliptic r-matrix entrywise.
        assert is_zero_tensor(elliptic_r_matrix(level=0, z=Z, antisymmetric_part=antisymmetric_part))

    def test_symmetric_sector_and_affine_average_match_kappa(self) -> None:
        a12, a13, a23 = sp.symbols("a12 a13 a23")
        antisymmetric_part = generic_antisymmetric_part(a12=a12, a13=a13, a23=a23)

        expected_symmetric_sector = K * ZETA(Z) * casimir_tensor()
        assert is_zero_tensor(
            symmetric_sector_of_r(level=K, z=Z, antisymmetric_part=antisymmetric_part)
            - expected_symmetric_sector
        )
        assert is_zero_tensor(
            antisymmetric_sector_of_r(level=K, z=Z, antisymmetric_part=antisymmetric_part)
            - K * antisymmetric_part
        )

        # VERIFIED [CF][LC]: kappa(V_k(g)) = dim(g)(k+h^vee)/(2h^vee) with dim(sl_2)=3 and h^vee=2.
        assert classical_average_from_symmetric_casimir(K) == SL2_CASIMIR_AVERAGE_WEIGHT * K == sp.Rational(3, 4) * K
        # VERIFIED [CF][LC]: the affine shift contributes dim(sl_2)/2 = 3/2, so av(r) = 3(k+2)/4.
        assert affine_genus1_average(K) == SL2_CASIMIR_AVERAGE_WEIGHT * K + SL2_SUGAWARA_SHIFT
        assert averaging_map_of_elliptic_r_matrix(level=K, z=Z, antisymmetric_part=antisymmetric_part) == kappa_sl2(K)
        assert kappa_sl2(K) == sp.Rational(3) * (K + 2) / 4
        assert affine_genus1_average(0) == sp.Rational(3, 2)
