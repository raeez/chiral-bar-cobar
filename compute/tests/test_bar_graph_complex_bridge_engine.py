from compute.lib.bar_graph_complex_bridge_engine import (
    edge_removal_sign,
    prism_graph,
    sign_bridge_theorem,
    tetrahedron_graph,
    verify_d_squared_zero_oriented,
    verify_tetrahedron_cocycle,
)


def test_basic_graph_invariants():
    tetrahedron = tetrahedron_graph()
    prism = prism_graph()

    assert (tetrahedron.n_vertices, tetrahedron.n_edges, tetrahedron.loop_order) == (4, 6, 3)
    assert tetrahedron.gc2_degree == -2
    assert (prism.n_vertices, prism.n_edges, prism.loop_order) == (6, 9, 4)


def test_orientation_sign_convention_alternates():
    assert edge_removal_sign((), 0) == 1
    assert edge_removal_sign((), 1) == -1
    assert edge_removal_sign((), 2) == 1


def test_d_squared_zero_on_prism():
    assert verify_d_squared_zero_oriented(prism_graph())["d2_is_zero"] is True


def test_tetrahedron_cocycle_and_sign_bridge_reports():
    tetra = verify_tetrahedron_cocycle()
    bridge = sign_bridge_theorem()

    assert tetra["d_is_zero"] is True
    assert tetra["n_invalid_contractions"] == 6
    assert bridge["loop3_verification"]["all_signs_agree"] is True
    assert bridge["loop4_verification"]["all_d2_zero"] is True
