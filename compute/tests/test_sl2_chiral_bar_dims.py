from compute.lib.sl2_chiral_bar_dims import triple_verification


def test_sl2_h2_triple_verification():
    report = triple_verification()

    assert report["values"]["direct_bar"] == 5
    assert report["values"]["ce_comparison"] == 5
    assert report["values"]["compute_engine"] == 5
    assert report["all_five"] is True


def test_sl2_h2_direct_rank_count():
    report = triple_verification()
    critical = report["direct_bar"]["critical_weight"]

    assert critical["chain_dims"] == {"L^1": 3, "L^2": 9, "L^3": 1}
    assert critical["rank_d1"] == 3
    assert critical["rank_d2"] == 1
    assert critical["H2_dim"] == 5
