#!/bin/bash
# ==========================================================================
# CONVERGENCE GATE — Stop hook
# ==========================================================================
# Enforces convergence discipline during rectification sessions.
# When a rectification SKILL was explicitly invoked, prevents stopping until:
# 1. The word CONVERGED appears in recent output
# 2. Or the agent explicitly reports being blocked
#
# IMPORTANT: Only activates on SKILL INVOCATIONS (slash commands), not on
# mere mentions of rectification in conversation. This prevents false
# positives when discussing or creating rectification infrastructure.
# ==========================================================================

INPUT=$(cat)

# Check if we're in a rectification session by looking for SKILL invocations
# Skill invocations appear as specific patterns in the transcript:
# - User typing "/rectify", "/audit", "/swarm", "/chriss-ginzburg-rectify"
# - Or the skill expansion markers from Claude Code
TRANSCRIPT=$(echo "$INPUT" | jq -r '.transcript_path // empty')

if [ -n "$TRANSCRIPT" ] && [ -f "$TRANSCRIPT" ]; then
  TAIL=$(tail -c 8000 "$TRANSCRIPT" 2>/dev/null)

  # Detect SKILL INVOCATIONS only — not loose word matches.
  # Skill invocations in Claude Code produce specific patterns:
  # 1. The user prompt starts with a slash command
  # 2. The skill expansion contains <command-name> tags
  # 3. A "Beilinson Rectification Loop" or "Deep Beilinson Audit" header
  #    appears as the FIRST content after skill expansion (not mid-conversation)
  IS_RECTIFICATION=false

  # Pattern 1: Skill invocation markers from Claude Code
  if echo "$TAIL" | grep -q '<command-name>rectify\|<command-name>audit\|<command-name>chriss-ginzburg\|<command-name>rectify-all\|<command-name>beilinson'; then
    IS_RECTIFICATION=true
  fi

  # Pattern 2: The convergence gate MARKER that skills can set explicitly
  # Skills can write "RECTIFICATION_SESSION_ACTIVE" to signal the gate
  if echo "$TAIL" | grep -q 'RECTIFICATION_SESSION_ACTIVE'; then
    IS_RECTIFICATION=true
  fi

  # Pattern 3: User explicitly invoked a rectification slash command
  # (appears as "/rectify " or "/audit " at start of a user message)
  if echo "$TAIL" | grep -q '"content":"/rectify \|"content":"/audit \|"content":"/chriss-ginzburg-rectify\|"content":"/rectify-all\|"content":"/beilinson-rectify'; then
    IS_RECTIFICATION=true
  fi

  if [ "$IS_RECTIFICATION" = true ]; then
    # Check for convergence declaration
    if echo "$TAIL" | grep -q "CONVERGED"; then
      exit 0  # Allow stop
    fi

    # Check for explicit block/stuck declaration
    if echo "$TAIL" | grep -qi "BLOCKED\|STUCK\|cannot proceed\|rate.limited"; then
      exit 0  # Allow stop with reason
    fi

    # Block the stop
    jq -n '{
      "decision": "block",
      "reason": "CONVERGENCE GATE: The rectification loop has not converged. You must either: (1) complete all phases and declare CONVERGED, (2) declare BLOCKED with reason if stuck. Do not stop mid-loop."
    }'
    exit 0
  fi
fi

# For non-rectification sessions: allow stop silently
exit 0
