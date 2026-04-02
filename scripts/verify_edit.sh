#!/usr/bin/env bash
# verify_edit.sh — Post-edit verification for the chiral bar-cobar monograph.
#
# Checks recently modified .tex files for known false patterns (anti-patterns)
# that have recurred historically in this repository.
#
# Usage:
#   ./scripts/verify_edit.sh                    # check files modified in last 10 min
#   ./scripts/verify_edit.sh file1.tex file2.tex  # check specific files
#   ./scripts/verify_edit.sh --staged           # check git-staged files
#   ./scripts/verify_edit.sh --all              # check all .tex files
#
# Exit code: 0 if clean, 1 if anti-patterns found.

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

# ── Determine which files to check ──────────────────────────────────────

files=()

if [[ "${1:-}" == "--staged" ]]; then
    while IFS= read -r f; do
        [[ "$f" == *.tex ]] && files+=("$f")
    done < <(git diff --cached --name-only 2>/dev/null || true)
elif [[ "${1:-}" == "--all" ]]; then
    while IFS= read -r f; do
        files+=("$f")
    done < <(find chapters appendices -name '*.tex' 2>/dev/null)
elif [[ $# -gt 0 ]]; then
    files=("$@")
else
    # Default: files modified in the last 10 minutes
    while IFS= read -r f; do
        files+=("$f")
    done < <(find chapters appendices -name '*.tex' -mmin -10 2>/dev/null)
fi

if [[ ${#files[@]} -eq 0 ]]; then
    echo "verify_edit: no files to check."
    exit 0
fi

echo "verify_edit: checking ${#files[@]} file(s)..."

# ── Anti-pattern definitions ────────────────────────────────────────────
# Each pattern: GREP_PATTERN|DESCRIPTION|CORRECT
# These are the 16 historically-recurring false claims.

declare -a PATTERNS=(
    # Koszul duality errors
    'Com.\{?\\?!\}? *= *coLie\|Com\^! *= *coLie\|\\mathrm{Com}\^! *= *\\mathrm{coLie}|Com^! = coLie (WRONG: Com^! = Lie)|Com^! = Lie'
    'H_\{?-\\?kappa\}?\|H\^! *= *H\|self-dual.*Heisenberg\|Heisenberg.*self-dual|H^! = H_{-kappa} (self-dual) WRONG|H^! = Sym^ch(V*)'
    'F\^! *= *.*[Hh]eisenberg\|fermion.*dual.*Heisenberg|F^! = Heisenberg WRONG|F^! = beta-gamma'
    '[Bb]osonization *= *[Kk]oszul\|[Bb]osonization.*is.*[Kk]oszul duality|Bosonization = Koszul duality WRONG|Different operations'
    'quotient of cofree\|quotient.*cofree.*coalgebra|Koszul dual = quotient of cofree WRONG|Sub-coalgebra of cofree'

    # Level/charge errors
    '-k-h.*dual[^}]*[^2]\|-k - h|FF involution -k-h^dual WRONG (should be -k-2h^dual)|k -> -k-2h^dual'
    # Note: we can't easily grep for "c diverges at critical" without false positives

    # Quantization level confusion
    '[Cc]oisson *= *P.*infty\|P.*infty *= *[Cc]oisson\|[Cc]oisson.*chiral algebra|Coisson = P_infty-chiral WRONG|Different quantization levels'

    # Module-level errors
    'D\^b(A-mod).*D\^b(A!-mod)\|D\^b.*\\simeq.*D\^b.*mod|D^b(A-mod) ~ D^b(A!-mod) WRONG|Need Positselski D^co/D^ctr'

    # Geometry errors
    'X\^n.*\\setminus.*Delta\|complement of.*diagonal.*FM|FM = complement of diagonals WRONG|FM = blowup along diagonals'
    'K\^\{?+?1/2\}?\|K\^\{1/2\}.*prime form|Prime form in K^{+1/2} WRONG|K^{-1/2}'
)

# ── Run checks ──────────────────────────────────────────────────────────

found=0

for entry in "${PATTERNS[@]}"; do
    IFS='|' read -r pattern desc correct <<< "$entry"
    for f in "${files[@]}"; do
        if [[ ! -f "$f" ]]; then continue; fi
        matches=$(grep -in "$pattern" "$f" 2>/dev/null || true)
        if [[ -n "$matches" ]]; then
            echo ""
            echo "  ANTI-PATTERN DETECTED in $f"
            echo "  Issue: $desc"
            echo "  Correct: $correct"
            echo "  Matches:"
            echo "$matches" | sed 's/^/    /'
            found=$((found + 1))
        fi
    done
done

echo ""
if [[ $found -gt 0 ]]; then
    echo "verify_edit: $found anti-pattern(s) found. Review before committing."
    exit 1
else
    echo "verify_edit: all checks passed."
    exit 0
fi
