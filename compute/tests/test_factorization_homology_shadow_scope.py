"""B3 scope guards for the explicit factorization-homology shadow table."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
ENGINE = ROOT / "compute" / "lib" / "factorization_homology_explicit_engine.py"
TESTS = ROOT / "compute" / "tests" / "test_factorization_homology_explicit_engine.py"
LEDGER = ROOT / "notes" / "audit_repairs_ledger_20260610.md"
MATRIX = ROOT / "notes" / "external_review_harvest_matrix_20260617.md"


def _flat(path: Path) -> str:
    return " ".join(path.read_text().split())


def test_factorization_homology_engine_declares_topological_shadow_scope():
    engine = _flat(ENGINE)
    tests = _flat(TESTS)

    for required in [
        "Finite topological-shadow tables",
        "not a chain-level computation of raw chiral factorization homology",
        "does not identify critical centers, chiral derived centers, Drinfeld centers, or bar cohomology",
        "Topologized MTC/WRT shadow only",
        "not raw chiral factorization homology on T^2 x I",
        "not the chiral derived center",
        "requires Swiss-cheese/OCA comparison datum",
        "No identification of the Drinfeld center with raw chiral",
    ]:
        assert required in f"{engine} {tests}"

    for forbidden in [
        "ACTUAL NUMBERS",
        "int_{T^2 x I} A: Drinfeld center",
        "Cylinder factorization homology = Drinfeld center",
        "T^2 x I cylinder factorization homology = Drinfeld center",
        "equivalently Z^der_ch(A)-module",
        "module over the chiral derived center Z^der_ch(A)",
        "factorization homology computes dim Z(C)",
    ]:
        assert forbidden not in f"{engine} {tests}"


def test_factorization_homology_scope_repair_is_recorded():
    ledger = _flat(LEDGER)
    matrix = _flat(MATRIX)

    assert "Pass 550: Topological shadow scope for explicit factorization homology" in ledger
    assert "Pass 550 fences the factorization-homology explicit engine" in matrix
