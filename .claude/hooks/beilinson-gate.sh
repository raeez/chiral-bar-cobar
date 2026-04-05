#!/bin/bash
# ==========================================================================
# BEILINSON GATE — PostToolUse hook for Edit|Write on .tex and .py files
# ==========================================================================
# Comprehensive anti-pattern enforcement + build discipline + cross-volume
# propagation awareness. This is the automated enforcement layer of the
# Beilinson Principle: every edit is suspect until verified.
#
# Replaces the former ap-check.sh and build-gate.sh with a unified gate.
# ==========================================================================

INPUT=$(cat)
FILE_PATH=$(echo "$INPUT" | jq -r '.tool_input.file_path // empty')
TOOL_NAME=$(echo "$INPUT" | jq -r '.tool_name // empty')

# Only fire for .tex and .py files
case "$FILE_PATH" in
  *.tex|*.py) ;;
  *) exit 0 ;;
esac

ISSUES=""
WARNINGS=""

# ---------------------------------------------------------------------------
# SECTION 1: ANTI-PATTERN SCAN (targeted, for .tex files)
# ---------------------------------------------------------------------------
if [[ "$FILE_PATH" == *.tex ]]; then

  # --- AP24: Unqualified κ+κ'=0 ---
  if grep -q 'kappa.*+.*kappa.*=.*0' "$FILE_PATH" 2>/dev/null; then
    MATCHES=$(grep -n 'kappa.*+.*kappa.*=.*0' "$FILE_PATH" | grep -v 'Kac--Moody\|Kac-Moody\|free.field\|self-contragredient\|type~I\|type I\|lattice\|principal' | head -3)
    if [ -n "$MATCHES" ]; then
      ISSUES="${ISSUES}AP24: Possibly unqualified kappa+kappa'=0. For Virasoro: kappa+kappa'=13, NOT 0. Lines: ${MATCHES}\n"
    fi
  fi

  # --- AP8: "self-dual" Virasoro/Vir without c=13 ---
  if grep -qi 'self.dual.*virasoro\|virasoro.*self.dual\|self.dual.*Vir\|Vir.*self.dual' "$FILE_PATH" 2>/dev/null; then
    MATCHES=$(grep -n -i 'self.dual.*virasoro\|virasoro.*self.dual\|self.dual.*Vir[^a-z]\|Vir[^a-z].*self.dual' "$FILE_PATH" | grep -v 'c=13\|c = 13\|c\*=13\|c\* = 13' | head -3)
    if [ -n "$MATCHES" ]; then
      ISSUES="${ISSUES}AP8: Self-dual Virasoro without specifying c=13. Lines: ${MATCHES}\n"
    fi
  fi

  # --- AP25/AP34: Bar-cobar conflation ---
  if grep -qi 'bar.cobar.*produces.*bulk\|bar.cobar.*open.to.closed\|Omega.*B(A).*bulk\|cobar.*Koszul dual' "$FILE_PATH" 2>/dev/null; then
    MATCHES=$(grep -n -i 'bar.cobar.*produces.*bulk\|bar.cobar.*open.to.closed\|Omega.*B(A).*bulk\|cobar.*Koszul dual' "$FILE_PATH" | head -3)
    if [ -n "$MATCHES" ]; then
      ISSUES="${ISSUES}AP25/AP34: Possible bar-cobar conflation. Omega(B(A))=A (inversion), NOT bulk. D_Ran(B(A))=B(A!) (Verdier). Lines: ${MATCHES}\n"
    fi
  fi

  # --- AP33: H_k^! = H_{-k} conflation ---
  if grep -Eq 'H[_^].*!\s*(=|\\simeq|\\cong)\s*H_\{?-k|H_k\^!\s*=\s*H_\{-k\}' "$FILE_PATH" 2>/dev/null; then
    MATCHES=$(grep -En 'H[_^].*!\s*(=|\\simeq|\\cong)\s*H_\{?-k|H_k\^!\s*=\s*H_\{-k\}' "$FILE_PATH" | head -3)
    if [ -n "$MATCHES" ]; then
      ISSUES="${ISSUES}AP33: H_k^! = H_{-k} is FALSE. H_k^! = Sym^ch(V*), a different algebra. Lines: ${MATCHES}\n"
    fi
  fi

  # --- AP14: Koszulness = formality conflation ---
  if grep -qi 'not Koszul\|non-Koszul\|breaks Koszulness\|destroys Koszulness' "$FILE_PATH" 2>/dev/null; then
    MATCHES=$(grep -n -i 'not Koszul\|non-Koszul\|breaks Koszulness\|destroys Koszulness' "$FILE_PATH" | head -3)
    if [ -n "$MATCHES" ]; then
      WARNINGS="${WARNINGS}AP14: Check Koszulness claim. ALL standard families are chirally Koszul. Shadow depth != Koszulness. Lines: ${MATCHES}\n"
    fi
  fi

  # --- AP7/AP32: Scope inflation ("for all" without qualification) ---
  if grep -qi 'for all modular Koszul\|for every chiral\|all genera\|universally\|for all algebras' "$FILE_PATH" 2>/dev/null; then
    MATCHES=$(grep -n -i 'for all modular Koszul\|all genera\|universally\|for all algebras' "$FILE_PATH" | grep -v 'uniform.weight\|genus.1\|single.generator\|on the.*lane\|evaluation.generated' | head -3)
    if [ -n "$MATCHES" ]; then
      WARNINGS="${WARNINGS}AP7/AP32: Possible scope inflation. Check: does the proof cover ALL cases? Lines: ${MATCHES}\n"
    fi
  fi

  # --- AP40: Environment/tag mismatch ---
  # Check for ClaimStatusConjectured inside theorem/proposition/lemma/corollary
  if grep -q 'ClaimStatusConjectured' "$FILE_PATH" 2>/dev/null; then
    CONJ_LINES=$(grep -n 'ClaimStatusConjectured' "$FILE_PATH" | cut -d: -f1)
    for LINE in $CONJ_LINES; do
      START=$((LINE - 10))
      [ $START -lt 1 ] && START=1
      CONTEXT=$(sed -n "${START},${LINE}p" "$FILE_PATH")
      # Use printf to avoid echo mangling \b in \begin (CRITICAL: echo interprets \b as backspace)
      if printf '%s\n' "$CONTEXT" | grep -q 'begin{theorem}\|begin{proposition}\|begin{lemma}\|begin{corollary}'; then
        ISSUES="${ISSUES}AP40: ClaimStatusConjectured inside proof-bearing environment near line ${LINE}. Use conjecture environment.\n"
        break
      fi
    done
  fi

  # --- AP19: r-matrix pole check (warn if OPE poles written as r-matrix) ---
  if grep -qi 'r-matrix.*z\^{-4}\|r-matrix.*z\^{-2}.*z\^{-1}' "$FILE_PATH" 2>/dev/null; then
    MATCHES=$(grep -n -i 'r-matrix.*z\^{-4}\|r-matrix.*z\^{-2}.*z\^{-1}' "$FILE_PATH" | head -2)
    if [ -n "$MATCHES" ]; then
      WARNINGS="${WARNINGS}AP19: r-matrix poles should be ONE LESS than OPE poles (d log absorption). Lines: ${MATCHES}\n"
    fi
  fi

  # --- AP27: Weight-h Hodge bundle ---
  # Inner grep uses \\mathcal which grep sees as literal \mathcal (matching .tex content)
  if grep -q '\\mathcal{E}_h\|\\mathcal{E}_{h}' "$FILE_PATH" 2>/dev/null; then
    MATCHES=$(grep -n '\\mathcal{E}_h\|\\mathcal{E}_{h}' "$FILE_PATH" | grep -v 'E_1\|E_2\|E_4\|E_6\|E_8' | head -3)
    if [ -n "$MATCHES" ]; then
      WARNINGS="${WARNINGS}AP27: Check Hodge bundle weight. Bar propagator is ALWAYS weight 1. All edges use E_1. Lines: ${MATCHES}\n"
    fi
  fi

  # --- AP44: lambda-bracket coefficient (divided power) ---
  if grep -qi 'lambda.*bracket.*c/2\|\\{T.*lambda.*T\\}.*c/2' "$FILE_PATH" 2>/dev/null; then
    MATCHES=$(grep -n -i 'lambda.*bracket.*c/2\|{T.*lambda.*T}.*c/2' "$FILE_PATH" | head -2)
    if [ -n "$MATCHES" ]; then
      WARNINGS="${WARNINGS}AP44: Check lambda-bracket coefficient. {T_lambda T} at order lambda^3 is c/12, NOT c/2 (divided power 1/3!). Lines: ${MATCHES}\n"
    fi
  fi

  # --- PROSE: AI slop words ---
  for WORD in notably crucially remarkably interestingly importantly furthermore moreover additionally delve leverage utilize underscore facilitate pivotal nuanced intricate streamline tapestry multifaceted cornerstone; do
    if grep -qi "\\b${WORD}\\b" "$FILE_PATH" 2>/dev/null; then
      LINE=$(grep -n -i "\\b${WORD}\\b" "$FILE_PATH" | head -1)
      ISSUES="${ISSUES}PROSE: AI slop word '${WORD}' detected. Remove it. Line: ${LINE}\n"
    fi
  done

  # --- PROSE: Signpost phrases ---
  for PHRASE in "it is worth noting" "having established" "we now turn to" "in this section we" "as we shall see" "let us now" "we proceed to" "the key insight is" "it turns out that" "this brings us to" "with this in hand"; do
    if grep -qi "$PHRASE" "$FILE_PATH" 2>/dev/null; then
      LINE=$(grep -n -i "$PHRASE" "$FILE_PATH" | head -1)
      ISSUES="${ISSUES}PROSE: Signpost phrase detected: '${PHRASE}'. Replace with mathematics. Line: ${LINE}\n"
    fi
  done

fi

# ---------------------------------------------------------------------------
# SECTION 2: COMPUTE LAYER CHECKS (for .py files)
# ---------------------------------------------------------------------------
if [[ "$FILE_PATH" == *.py ]]; then

  # --- AP10: Hardcoded expected values without cross-check ---
  if grep -q 'assert.*==' "$FILE_PATH" 2>/dev/null; then
    HARDCODED=$(grep -c 'assert.*==.*[0-9]' "$FILE_PATH" 2>/dev/null)
    CROSSCHECK=$(grep -c 'assert.*approx\|assert.*close\|verify_.*path\|cross_check\|independent' "$FILE_PATH" 2>/dev/null)
    if [ "$HARDCODED" -gt 5 ] && [ "$CROSSCHECK" -lt 2 ]; then
      WARNINGS="${WARNINGS}AP10: ${HARDCODED} hardcoded assertions but only ${CROSSCHECK} cross-checks. Add multi-path verification.\n"
    fi
  fi

fi

# ---------------------------------------------------------------------------
# SECTION 3: BUILD DISCIPLINE (edit counter)
# ---------------------------------------------------------------------------
COUNTER_FILE="/tmp/claude_beilinson_edit_count"
COUNT=$(cat "$COUNTER_FILE" 2>/dev/null || echo 0)
COUNT=$((COUNT + 1))
echo "$COUNT" > "$COUNTER_FILE"

BUILD_REMINDER=""
if (( COUNT % 5 == 0 )); then
  BUILD_REMINDER="BUILD CHECK: ${COUNT} edits since last build. Run: pkill -9 -f pdflatex; sleep 2; make fast"
fi

# ---------------------------------------------------------------------------
# SECTION 4: CROSS-VOLUME PROPAGATION AWARENESS
# ---------------------------------------------------------------------------
PROPAGATION=""
if [[ "$FILE_PATH" == *.tex ]]; then
  # Detect if a formula was likely edited — handle both Edit (new_string) and Write (content) tools
  NEW_CONTENT=$(echo "$INPUT" | jq -r '(.tool_input.new_string // .tool_input.content) // empty' 2>/dev/null)
  if echo "$NEW_CONTENT" | grep -q '\\kappa\|\\Theta\|\\lambda_g\|F_g\|Q\^{contact}\|\\delta_\\kappa' 2>/dev/null; then
    PROPAGATION="AP5: Formula edit detected. After this edit, grep ALL THREE volumes for variant forms: ~/chiral-bar-cobar, ~/chiral-bar-cobar-vol2, ~/calabi-yau-quantum-groups"
  fi
fi

# ---------------------------------------------------------------------------
# OUTPUT
# ---------------------------------------------------------------------------
CONTEXT=""
[ -n "$ISSUES" ] && CONTEXT="${CONTEXT}VIOLATIONS:\n${ISSUES}\n"
[ -n "$WARNINGS" ] && CONTEXT="${CONTEXT}WARNINGS:\n${WARNINGS}\n"
[ -n "$BUILD_REMINDER" ] && CONTEXT="${CONTEXT}${BUILD_REMINDER}\n"
[ -n "$PROPAGATION" ] && CONTEXT="${CONTEXT}${PROPAGATION}\n"

if [ -n "$CONTEXT" ]; then
  jq -n --arg ctx "$CONTEXT" '{
    "hookSpecificOutput": {
      "hookEventName": "PostToolUse",
      "additionalContext": $ctx
    }
  }'
fi

exit 0
