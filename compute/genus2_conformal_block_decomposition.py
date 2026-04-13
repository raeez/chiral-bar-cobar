#!/usr/bin/env python3
"""Genus-2 degree-2 ordered chiral homology for sl_2 with V = C^2.

This script computes two related but different objects.

1. Generic level: the Euler-characteristic split of the KZB local system on
   Sigma_2 minus one point with fiber V^{tensor 2}, where V = C^2.
2. Integer level k >= 1: the genus-2 Verlinde dimensions and the degree-2
   conformal block count obtained from the fusion decomposition of
   V_{1/2} tensor V_{1/2}.

Conventions:
  - sl_2 integrable labels are j = 0, 1, ..., k, with spin = j/2
  - S_{a,b} = sqrt(2/(k+2)) * sin(pi*(a+1)*(b+1)/(k+2))
  - genus-2 vacuum blocks: Z_2(k) = sum_j S_{0,j}^{-2}
  - genus-2 one-point block in channel j:
        CB_{2,1}(j) = sum_m S_{j,m} / S_{0,m}^3
  - degree-2 insertion from V = C^2 uses the level-k fusion coefficients
        N_{1,1}^j
    so the degree-2 conformal block dimension is
        sum_j N_{1,1}^j * CB_{2,1}(j)
"""

from __future__ import annotations

import math
from fractions import Fraction


GENUS = 2
MARKED_POINTS = 1
TOPOLOGICAL_EULER = 2 - 2 * GENUS - MARKED_POINTS
LEVELS = range(1, 6)


def nearest_integer(value: float, tol: float = 1e-8) -> int:
    """Round a float that should be integral."""
    candidate = round(value)
    if abs(value - candidate) > tol:
        raise ValueError(f"expected an integer, got {value}")
    return int(candidate)


def spin_string(label: int) -> str:
    """Display the spin j/2 attached to Dynkin label j."""
    spin = Fraction(label, 2)
    if spin.denominator == 1:
        return str(spin.numerator)
    return f"{spin.numerator}/{spin.denominator}"


def format_table(headers: list[str], rows: list[list[object]]) -> str:
    """Render a plain-text table."""
    string_rows = [[str(item) for item in row] for row in rows]
    widths = [len(header) for header in headers]
    for row in string_rows:
        for idx, item in enumerate(row):
            widths[idx] = max(widths[idx], len(item))

    def render(row: list[str]) -> str:
        return " | ".join(item.ljust(widths[idx]) for idx, item in enumerate(row))

    separator = "-+-".join("-" * width for width in widths)
    lines = [render(headers), separator]
    lines.extend(render(row) for row in string_rows)
    return "\n".join(lines)


def s_matrix_entry(level: int, a: int, b: int) -> float:
    """Modular S-matrix entry for sl_2 at level k."""
    denominator = level + 2
    prefactor = math.sqrt(2.0 / denominator)
    angle = math.pi * (a + 1) * (b + 1) / denominator
    return prefactor * math.sin(angle)


def genus_two_vacuum_blocks(level: int) -> int:
    """Z_2(k) = sum_j S_{0,j}^{-2}."""
    total = 0.0
    for j in range(level + 1):
        total += s_matrix_entry(level, 0, j) ** (-2)
    return nearest_integer(total)


def genus_two_vacuum_blocks_closed(level: int) -> int:
    """Closed form for Z_2(k)."""
    return math.comb(level + 3, 3)


def fusion_coefficient(level: int, a: int, b: int, c: int) -> int:
    """Verlinde fusion coefficient N_{a,b}^c."""
    total = 0.0
    for m in range(level + 1):
        s0m = s_matrix_entry(level, 0, m)
        total += (
            s_matrix_entry(level, a, m)
            * s_matrix_entry(level, b, m)
            * s_matrix_entry(level, c, m)
            / s0m
        )
    return nearest_integer(total)


def genus_two_one_point_blocks(level: int, label: int) -> int:
    """Genus-2 one-point conformal block dimension in channel j."""
    total = 0.0
    for m in range(level + 1):
        total += s_matrix_entry(level, label, m) / (s_matrix_entry(level, 0, m) ** 3)
    return nearest_integer(total)


def triplet_channel_closed(level: int) -> int:
    """Closed form for the j=2 channel at genus 2."""
    if level < 2:
        return 0
    return (level - 1) * (level + 1) * (level + 2) // 2


def degree_two_total_closed(level: int) -> int:
    """Closed form for the degree-2 insertion V tensor V."""
    return 2 * level * (level + 1) * (level + 2) // 3


def generic_kzb_channel_rows() -> list[list[object]]:
    """Triplet and singlet decomposition at generic level."""
    rows = []
    for channel, rank in [
        ("V_1 = spin-1 triplet = Sym^2(C^2)", 3),
        ("V_0 = spin-0 singlet = wedge^2(C^2)", 1),
    ]:
        chi = rank * TOPOLOGICAL_EULER
        h1 = -chi
        rows.append([channel, rank, chi, 0, h1, 0])
    return rows


def integrable_one_point_rows(level: int) -> list[list[object]]:
    """All genus-2 one-point dimensions at level k."""
    rows = []
    for label in range(level + 1):
        rows.append([
            label,
            spin_string(label),
            label + 1,
            genus_two_one_point_blocks(level, label),
        ])
    return rows


def degree_two_channel_name(label: int) -> str:
    """Human-readable name for the degree-2 fusion channels."""
    if label == 0:
        return "V_0 = spin-0 singlet"
    if label == 2:
        return "V_1 = spin-1 triplet"
    return f"spin-{spin_string(label)} channel"


def degree_two_rows(level: int) -> tuple[list[list[object]], int]:
    """Fusion-channel decomposition of V tensor V at level k."""
    rows = []
    total = 0
    for label in range(level + 1):
        multiplicity = fusion_coefficient(level, 1, 1, label)
        if multiplicity == 0:
            continue
        block_dim = genus_two_one_point_blocks(level, label)
        contribution = multiplicity * block_dim
        total += contribution
        rows.append([
            label,
            spin_string(label),
            degree_two_channel_name(label),
            multiplicity,
            block_dim,
            contribution,
        ])
    return rows, total


def verify_level_data(level: int) -> None:
    """Direct and closed-form checks for the printed tables."""
    z2_direct = genus_two_vacuum_blocks(level)
    z2_closed = genus_two_vacuum_blocks_closed(level)
    if z2_direct != z2_closed:
        raise ValueError(f"Z_2 mismatch at k={level}: {z2_direct} vs {z2_closed}")

    channel_zero = genus_two_one_point_blocks(level, 0)
    if channel_zero != z2_direct:
        raise ValueError(f"vacuum channel mismatch at k={level}: {channel_zero} vs {z2_direct}")

    channel_two = genus_two_one_point_blocks(level, 2) if level >= 2 else 0
    if channel_two != triplet_channel_closed(level):
        raise ValueError(
            f"triplet channel mismatch at k={level}: {channel_two} vs {triplet_channel_closed(level)}"
        )

    degree_two_rows_data, degree_two_total = degree_two_rows(level)
    _ = degree_two_rows_data
    if degree_two_total != degree_two_total_closed(level):
        raise ValueError(
            f"degree-2 total mismatch at k={level}: {degree_two_total} vs {degree_two_total_closed(level)}"
        )


def print_generic_section() -> None:
    """Print the generic-level Euler-characteristic computation."""
    print("Generic level: KZB local system on Sigma_2 \\ {p}")
    print(f"topological Euler characteristic: chi_top = {TOPOLOGICAL_EULER}")
    print("fiber decomposition: C^2 tensor C^2 = Sym^2(C^2) + wedge^2(C^2)")
    print("channel naming: V_1 is the spin-1 triplet and uses affine label j = 2; V_0 uses j = 0")
    print()

    rows = generic_kzb_channel_rows()
    print(format_table(
        ["channel", "rank", "chi", "dim H^0", "dim H^1", "dim H^2"],
        rows,
    ))
    print()

    total_rank = sum(row[1] for row in rows)
    total_chi = sum(row[2] for row in rows)
    total_h1 = sum(row[4] for row in rows)
    print(f"total rank = {total_rank}")
    print(f"total chi = {total_chi}")
    print(f"generic dim H^1 = {total_h1}")
    print()


def print_level_summary() -> None:
    """Print genus-2 vacuum blocks and degree-2 totals."""
    summary_rows = []
    for level in LEVELS:
        verify_level_data(level)
        degree_two_data, degree_two_total = degree_two_rows(level)
        channel_two = 0
        for row in degree_two_data:
            if row[0] == 2:
                channel_two = row[4]
                break
        summary_rows.append([
            level,
            genus_two_vacuum_blocks(level),
            channel_two,
            degree_two_total,
        ])

    print("Finite integrable levels: genus-2 vacuum and degree-2 conformal blocks")
    print(format_table(
        ["k", "Z_2(k) = CB_{2,1}(j=0)", "CB_{2,1}(j=2)", "degree-2 total"],
        summary_rows,
    ))
    print()


def print_level_details(level: int) -> None:
    """Print the integrable one-point table and the degree-2 fusion table."""
    print(f"Level k = {level}")
    print("all integrable genus-2 one-point conformal blocks")
    print(format_table(
        ["j", "spin j/2", "classical dim", "CB_{2,1}(j)"],
        integrable_one_point_rows(level),
    ))
    print()

    rows, total = degree_two_rows(level)
    print("degree-2 decomposition from V tensor V with V = C^2")
    print("fusion input: N_{1,1}^j")
    print(format_table(
        ["j", "spin j/2", "channel", "N_{1,1}^j", "CB_{2,1}(j)", "contribution"],
        rows,
    ))
    print(f"degree-2 conformal block dimension = {total}")
    print(f"closed-form check = {degree_two_total_closed(level)}")
    print()


def print_relationship_note() -> None:
    """Explain how the generic H^1 count and the finite-level Verlinde counts differ."""
    print("Relationship between Z_2 and the generic dim H^1 = 12")
    print("  Z_2(k) is the genus-2 vacuum conformal block count in the integrable theory.")
    print("  The generic number 12 is dim H^1 of a rank-4 KZB local system on the punctured surface.")
    print("  They are different invariants: one is an Euler-characteristic computation on Sigma_2 \\ {p},")
    print("  the other is a Verlinde count of global conformal blocks after integrable truncation.")
    print("  The degree-2 conformal block count is")
    print("      sum_j N_{1,1}^j * CB_{2,1}(j).")
    print("  At k = 1 the triplet channel j = 2 is truncated, so degree-2 total = Z_2(1) = 4.")
    print("  For k >= 2 both singlet and triplet channels contribute.")


def main() -> None:
    print("Genus-2 degree-2 ordered chiral homology for sl_2 with V = C^2")
    print()
    print_generic_section()
    print_level_summary()
    for level in LEVELS:
        print_level_details(level)
    print_relationship_note()


if __name__ == "__main__":
    main()
