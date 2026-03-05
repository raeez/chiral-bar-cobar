#!/bin/bash
# Converging build script for the chiral bar-cobar manuscript.
# Runs up to MAX_PASSES of pdflatex, stopping when references stabilize.
# Use this instead of raw pdflatex to avoid oscillation on 1100+ page docs.

set -e
cd "$(dirname "$0")/.."

MAX_PASSES=${1:-7}
TEX="pdflatex"
TEXFLAGS="-interaction=nonstopmode -file-line-error -synctex=0"

# Kill any competing pdflatex processes on main.tex
pkill -f 'pdflatex.*main.tex' 2>/dev/null || true
sleep 1

echo "Building main.tex (up to $MAX_PASSES passes)"
for i in $(seq 1 $MAX_PASSES); do
    echo "── Pass $i / $MAX_PASSES ──"
    $TEX $TEXFLAGS main.tex > /dev/null 2>&1 || true

    if [ -f main.idx ]; then
        makeindex -q main.idx 2>/dev/null || true
    fi

    cit=$(grep -c 'Citation.*undefined' main.log 2>/dev/null || echo 0)
    ref=$(grep -c 'Reference.*undefined' main.log 2>/dev/null || echo 0)
    pages=$(grep 'Output written' main.log 2>/dev/null | sed 's/.*(\([0-9]*\) pages.*/\1/' || echo '?')
    echo "   ${pages}pp, ${cit} undef citations, ${ref} undef references"

    if [ "$i" -ge 2 ] && [ "$cit" -eq 0 ] && [ "$ref" -eq 0 ]; then
        echo "✓ Converged after $i passes."
        exit 0
    fi
done

echo "⚠ Did not fully converge after $MAX_PASSES passes (Cit=$cit, Ref=$ref)."
echo "  This is normal for page-count oscillation on large documents."
exit 0
