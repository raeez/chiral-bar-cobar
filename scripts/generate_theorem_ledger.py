#!/usr/bin/env python3
"""Generate a theorem ledger CSV from the Annals-edition .tex files.

For each theorem/proposition/lemma/corollary environment, extract:
  - label
  - environment type (theorem, proposition, lemma, corollary)
  - name (from square brackets)
  - claim status (ProvedHere, ProvedElsewhere, Conjectured, etc.)
  - file path
  - line number

Output: standalone/theorem_ledger.csv
"""

import csv
import os
import re
import sys

# Annals-build files (not quarantined)
ANNALS_FILES = []

# Theory chapters
for f in sorted(os.listdir("chapters/theory")):
    if f.endswith(".tex"):
        ANNALS_FILES.append(f"chapters/theory/{f}")

# Frame
for f in ["chapters/frame/preface.tex", "chapters/frame/heisenberg_frame.tex"]:
    if os.path.exists(f):
        ANNALS_FILES.append(f)

# Example chapters (Annals-kept)
ANNALS_EXAMPLES = [
    "lattice_foundations", "free_fields", "beta_gamma", "kac_moody",
    "w_algebras", "w3_composite_fields", "minimal_model_fusion",
    "minimal_model_examples", "w_algebras_deep",
    "deformation_quantization", "deformation_quantization_examples",
    "yangians_foundations", "yangians_computations", "yangians_drinfeld_kohno",
    "heisenberg_eisenstein",
]
for name in ANNALS_EXAMPLES:
    path = f"chapters/examples/{name}.tex"
    if os.path.exists(path):
        ANNALS_FILES.append(path)

# Connections (Annals-kept)
ANNALS_CONNECTIONS = [
    "poincare_computations", "feynman_diagrams", "feynman_connection", "bv_brst",
]
for name in ANNALS_CONNECTIONS:
    path = f"chapters/connections/{name}.tex"
    if os.path.exists(path):
        ANNALS_FILES.append(path)

# Appendices (Annals-kept + Part I promoted)
ANNALS_APPENDICES = [
    "general_relations", "arnold_relations", "signs_and_shifts",
    "theta_functions", "spectral_sequences", "spectral_higher_genus",
    "koszul_reference", "existence_criteria",
    "ordered_associative_chiral_kd", "notation_index",
    "nonlinear_modular_shadows", "branch_line_reductions",
]
for name in ANNALS_APPENDICES:
    path = f"appendices/{name}.tex"
    if os.path.exists(path):
        ANNALS_FILES.append(path)

# Regex patterns
ENV_PATTERN = re.compile(
    r'\\begin\{(theorem|proposition|lemma|corollary)\}'
    r'\s*\[([^\]]*)\]',
    re.DOTALL,
)
LABEL_PATTERN = re.compile(r'\\label\{([^}]+)\}')
STATUS_PATTERN = re.compile(r'\\ClaimStatus(\w+)')


def extract_theorems(filepath):
    """Extract theorem-like environments from a file."""
    results = []
    try:
        with open(filepath, "r", encoding="utf-8", errors="replace") as f:
            content = f.read()
            lines = content.split("\n")
    except FileNotFoundError:
        return results

    for i, line in enumerate(lines, 1):
        # Check for theorem-like environment start
        for env_type in ["theorem", "proposition", "lemma", "corollary"]:
            if f"\\begin{{{env_type}}}" in line:
                # Extract name from brackets
                name = ""
                status = ""
                label = ""

                # Look at this line and next few for name, label, status
                context = "\n".join(lines[i - 1 : min(i + 5, len(lines))])

                m = re.search(
                    rf"\\begin{{{env_type}}}\s*\[([^\]]*)\]", context
                )
                if m:
                    name = m.group(1).strip()

                m = LABEL_PATTERN.search(context)
                if m:
                    label = m.group(1)

                m = STATUS_PATTERN.search(context)
                if m:
                    status = m.group(1)

                if label:  # Only include labeled theorems
                    results.append(
                        {
                            "label": label,
                            "type": env_type,
                            "name": name,
                            "status": status,
                            "file": filepath,
                            "line": i,
                        }
                    )
                break

    return results


def main():
    all_theorems = []
    for filepath in ANNALS_FILES:
        theorems = extract_theorems(filepath)
        all_theorems.extend(theorems)

    # Sort by file then line
    all_theorems.sort(key=lambda t: (t["file"], t["line"]))

    # Write CSV
    os.makedirs("standalone", exist_ok=True)
    outpath = "standalone/theorem_ledger.csv"
    with open(outpath, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["label", "type", "name", "status", "file", "line"],
        )
        writer.writeheader()
        writer.writerows(all_theorems)

    # Summary
    by_type = {}
    by_status = {}
    for t in all_theorems:
        by_type[t["type"]] = by_type.get(t["type"], 0) + 1
        s = t["status"] or "no-tag"
        by_status[s] = by_status.get(s, 0) + 1

    print(f"Theorem ledger written to {outpath}")
    print(f"Total: {len(all_theorems)} labeled environments")
    print(f"By type: {dict(sorted(by_type.items()))}")
    print(f"By status: {dict(sorted(by_status.items()))}")


if __name__ == "__main__":
    main()
