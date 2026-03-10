#!/bin/bash
# Converging build script for the chiral bar-cobar manuscript.
# Runs up to MAX_PASSES of pdflatex, stopping when references stabilize.
# Use this instead of raw pdflatex to avoid oscillation on large documents.

set -euo pipefail
cd "$(dirname "$0")/.."

MAX_PASSES=${1:-7}
TEX="pdflatex"
TEXFLAGS="-interaction=nonstopmode -file-line-error -synctex=0"
LOG_DIR=".build_logs"
RUN_LOG="$LOG_DIR/tex-build.stdout.log"

mkdir -p "$LOG_DIR"

count_matches() {
    local pattern=$1
    local file=$2
    local count
    count=$(grep -aEc "$pattern" "$file" 2>/dev/null || true)
    count=${count##*$'\n'}
    if [ -z "$count" ]; then
        count=0
    fi
    printf '%s\n' "$count"
}

show_failure_summary() {
    echo "✗ Build failed."
    echo "  Logs: $RUN_LOG and main.log"
    if [ -f main.log ]; then
        grep -aE '^! |Emergency stop|Runaway argument|Fatal error|Undefined control sequence|File ended while scanning|No pages of output' main.log | head -n 20 || true
    elif [ -f "$RUN_LOG" ]; then
        tail -n 40 "$RUN_LOG" || true
    fi
}

# Kill any competing pdflatex processes on main.tex
pkill -f 'pdflatex.*main.tex' 2>/dev/null || true
sleep 1

echo "Building main.tex (up to $MAX_PASSES passes)"
for i in $(seq 1 $MAX_PASSES); do
    echo "── Pass $i / $MAX_PASSES ──"
    find . -name '*.aux' -exec xattr -c {} \; 2>/dev/null || true
    xattr -c main.out 2>/dev/null || true
    : > "$RUN_LOG"
    set +e
    $TEX $TEXFLAGS main.tex >"$RUN_LOG" 2>&1
    tex_rc=$?
    set -e

    if [ -f main.idx ]; then
        makeindex -q main.idx 2>/dev/null || true
    fi

    cit=$(count_matches 'Citation.*undefined' main.log)
    ref=$(count_matches 'Reference.*undefined' main.log)
    rerun=$(count_matches 'Label\(s\) may have changed|Package rerunfilecheck Warning' main.log)
    overfull=$(count_matches 'Overfull \\hbox' main.log)
    underfull=$(count_matches 'Underfull \\hbox|Underfull \\vbox' main.log)
    pages=$(grep 'Output written' main.log 2>/dev/null | sed 's/.*(\([0-9]*\) pages.*/\1/' | tail -n 1 || echo '?')
    echo "   ${pages}pp, ${cit} undef citations, ${ref} undef references, ${rerun} rerun requests, ${overfull} overfull, ${underfull} underfull"

    if [ "$tex_rc" -ne 0 ] && { [ ! -f main.pdf ] || ! grep -aq 'Output written' main.log 2>/dev/null; }; then
        show_failure_summary
        exit "$tex_rc"
    fi

    if [ "$i" -ge 2 ] && [ "$cit" -eq 0 ] && [ "$ref" -eq 0 ] && [ "$rerun" -eq 0 ]; then
        echo "✓ Converged after $i passes."
        exit 0
    fi
done

if [ ! -f main.pdf ] || ! grep -aq 'Output written' main.log 2>/dev/null; then
    show_failure_summary
    exit 1
fi

if [ "$MAX_PASSES" -eq 1 ]; then
    echo "✓ Completed single pass."
    exit 0
fi

echo "⚠ Did not fully converge after $MAX_PASSES passes (Cit=$cit, Ref=$ref, Rerun=$rerun)."
echo "  This is normal for page-count oscillation on large documents."
exit 0
