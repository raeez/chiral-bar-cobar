#!/usr/bin/env python3
"""Corpus-level quality-control checks for the monograph sources."""

from __future__ import annotations

import argparse
import collections
import pathlib
import re
import sys
from dataclasses import dataclass


ROOT = pathlib.Path(__file__).resolve().parent.parent
SCAN_ROOTS = ("main.tex", "chapters", "appendices", "bibliography")
CONTROL_DOCS = (
    "AGENTS.md",
    "notes/GPT54_CODEX_OPERATING_SYSTEM.md",
    "notes/SESSION_PROMPT_v23.md",
    "notes/autonomous_state.md",
    "notes/VISION.md",
    "notes/PROGRAMMES.md",
    "notes/HORIZON.md",
    "notes/NEW_MACHINERY.md",
    "notes/REWRITE_QUEUE.md",
    "latest_state_scaffold.md",
    "metadata/frontier_and_gaps.md",
    "metadata/reference_theorems.md",
    "CLAUDE.md",
)
FRONTIER_PHRASE_DOCS = (
    "AGENTS.md",
    "notes/GPT54_CODEX_OPERATING_SYSTEM.md",
    "notes/SESSION_PROMPT_v23.md",
    "notes/autonomous_state.md",
    "notes/VISION.md",
    "notes/PROGRAMMES.md",
    "notes/HORIZON.md",
    "notes/NEW_MACHINERY.md",
    "notes/SESSION_PROMPT_v20.md",
    "notes/ADVERSARIAL_AUDIT_SESSION5.md",
    "notes/SESSION_STATE_POST_AUDIT5.md",
    "notes/METAMORPHOSIS_PLAN.md",
    "latest_state_scaffold.md",
    "metadata/frontier_and_gaps.md",
    "metadata/reference_theorems.md",
    "CLAUDE.md",
)
ACTIVE_META_DOCS = (
    "AGENTS.md",
    "CLAUDE.md",
    "notes/GPT54_CODEX_OPERATING_SYSTEM.md",
    "notes/PROGRAMMES.md",
    "notes/SESSION_PROMPT_v23.md",
    "notes/VISION.md",
    "notes/autonomous_state.md",
    "latest_state_scaffold.md",
)
ACTIVE_PROMPT_DOCS = ("notes/SESSION_PROMPT_v23.md",)
ACTIVE_STATE_DOCS = ("notes/autonomous_state.md",)
ARCHIVAL_PROMPT_GLOBS = (
    "notes/SESSION_PROMPT*.md",
    "notes/DEEP_SESSION_PROMPT*.md",
    "notes/GPT54_AUDIT_PROMPT.md",
)
ARCHIVAL_STATE_GLOBS = (
    "notes/*state*.md",
    "notes/SESSION_STATE*.md",
)
LIVE_PROMPT_POINTER_DOCS = (
    "AGENTS.md",
    "CLAUDE.md",
    "notes/autonomous_state.md",
)
THEOREM_ENVS = ("theorem", "lemma", "proposition", "corollary")
STATUS_RE = re.compile(
    r"\\ClaimStatus(?:ProvedHere|ProvedElsewhere|Open|Conjectured|Conditional|Heuristic)"
)
GOQ_RE = re.compile(r"governing question", re.IGNORECASE)
HMS_RE = re.compile(r"semantic levels; convention|conv:hms-levels", re.IGNORECASE)
PRIOR_VERSION_PATTERNS = (
    re.compile(r"previous version", re.IGNORECASE),
    re.compile(r"previous draft", re.IGNORECASE),
    re.compile(r"earlier draft", re.IGNORECASE),
    re.compile(r"legacy", re.IGNORECASE),
    re.compile(r"supersede[s]? earlier preview", re.IGNORECASE),
)
AI_TELL_PATTERNS = (
    re.compile(r"it is worth noting", re.IGNORECASE),
    re.compile(r"it is important to note", re.IGNORECASE),
    re.compile(r"this chapter is organized as follows", re.IGNORECASE),
    re.compile(r"in this chapter[, ]+we", re.IGNORECASE),
    re.compile(r"we now turn to", re.IGNORECASE),
    re.compile(r"needless to say", re.IGNORECASE),
)
AMBIGUOUS_STATUS_PATTERNS = (
    re.compile(r"\bis expected\b", re.IGNORECASE),
    re.compile(r"\bare expected\b", re.IGNORECASE),
    re.compile(r"\bsuggests?\b", re.IGNORECASE),
    re.compile(r"\bby analogy\b", re.IGNORECASE),
    re.compile(r"\bin precise analogy\b", re.IGNORECASE),
)
VIRASORO_DUAL_PATTERNS = (
    re.compile(r"Virasoro[^.\n]{0,140}\bhas a Koszul dual\b", re.IGNORECASE),
    re.compile(r"Virasoro[^.\n]{0,140}\badmits? a Koszul dual\b", re.IGNORECASE),
    re.compile(r"Virasoro[^.\n]{0,140}\brequires completion[^.\n]{0,80}\bKoszul dual\b", re.IGNORECASE),
    re.compile(r"Virasoro[^.\n]{0,140}\bKoszul dual is\b", re.IGNORECASE),
    re.compile(r"Virasoro[^.\n]{0,140}\bdual algebra\b", re.IGNORECASE),
    re.compile(r"Virasoro[^.\n]{0,140}\bdual object\b", re.IGNORECASE),
    re.compile(r"Virasoro[^\n]{0,160}W_\\infty", re.IGNORECASE),
    re.compile(r"Virasoro[^\n]{0,160}W_infty", re.IGNORECASE),
)
VIRASORO_SAFE_PATTERNS = (
    re.compile(r"same-family", re.IGNORECASE),
    re.compile(r"\bshadow\b", re.IGNORECASE),
    re.compile(r"self-dual", re.IGNORECASE),
    re.compile(r"m/s-level", re.IGNORECASE),
    re.compile(r"\bm-level\b", re.IGNORECASE),
    re.compile(r"\bs-level\b", re.IGNORECASE),
    re.compile(r"\bmc4\b", re.IGNORECASE),
    re.compile(r"completion frontier", re.IGNORECASE),
    re.compile(r"realization problem", re.IGNORECASE),
    re.compile(r"infinite-generator", re.IGNORECASE),
    re.compile(r"does not yet", re.IGNORECASE),
    re.compile(r"not yet", re.IGNORECASE),
)
INFINITE_GENERATOR_DUAL_PATTERNS = (
    re.compile(r"W_\\infty[^.\n]{0,140}\bis (?:the )?Koszul dual\b", re.IGNORECASE),
    re.compile(r"W_infty[^.\n]{0,140}\bis (?:the )?Koszul dual\b", re.IGNORECASE),
    re.compile(r"W_\\infty[^.\n]{0,160}\bdual object\b", re.IGNORECASE),
    re.compile(r"W_infty[^.\n]{0,160}\bdual object\b", re.IGNORECASE),
    re.compile(r"Yangian tower[^.\n]{0,160}\bis (?:the )?Koszul dual\b", re.IGNORECASE),
    re.compile(r"Yangian tower[^.\n]{0,160}\bdual object\b", re.IGNORECASE),
    re.compile(r"dg-shifted Yangian[^.\n]{0,160}\bis (?:the )?Koszul dual\b", re.IGNORECASE),
    re.compile(r"dg-shifted Yangian[^.\n]{0,160}\bdual object\b", re.IGNORECASE),
)
INFINITE_GENERATOR_SAFE_PATTERNS = (
    re.compile(r"\bmc4\b", re.IGNORECASE),
    re.compile(r"theorem-ready", re.IGNORECASE),
    re.compile(r"frontier", re.IGNORECASE),
    re.compile(r"inverse-limit", re.IGNORECASE),
    re.compile(r"completed bar", re.IGNORECASE),
    re.compile(r"continuity", re.IGNORECASE),
    re.compile(r"stabilization", re.IGNORECASE),
    re.compile(r"surjectiv", re.IGNORECASE),
    re.compile(r"mittag", re.IGNORECASE),
    re.compile(r"not yet", re.IGNORECASE),
    re.compile(r"does not yet", re.IGNORECASE),
    re.compile(r"realization problem", re.IGNORECASE),
)
DK_SCOPE_PATTERNS = (
    re.compile(r"The derived Drinfeld--Kohno theorem", re.IGNORECASE),
    re.compile(r"Towards a derived Drinfeld--Kohno theorem", re.IGNORECASE),
    re.compile(r"\[Derived Drinfeld--Kohno", re.IGNORECASE),
    re.compile(r"Derived Drinfeld--Kohno is proved", re.IGNORECASE),
)
DK_SCOPE_SAFE_PATTERNS = (
    re.compile(r"chain-level", re.IGNORECASE),
    re.compile(r"evaluation locus", re.IGNORECASE),
    re.compile(r"evaluation-locus", re.IGNORECASE),
    re.compile(r"full derived Drinfeld--Kohno", re.IGNORECASE),
    re.compile(r"full factorization", re.IGNORECASE),
    re.compile(r"conjectur", re.IGNORECASE),
)
PERIODICITY_PROFILE_PATTERNS = (
    re.compile(r"periodicity triple", re.IGNORECASE),
)
KL_SCOPE_PATTERNS = (
    re.compile(r"Kazhdan--Lusztig equivalence from bar-cobar", re.IGNORECASE),
    re.compile(r"full Kazhdan--Lusztig equivalence", re.IGNORECASE),
    re.compile(r"Rep\^\{\\mathrm\{fd\}\}\(U_q", re.IGNORECASE),
    re.compile(r"equivalence of abelian categories", re.IGNORECASE),
)
KL_SCOPE_SAFE_PATTERNS = (
    re.compile(r"semisimplified tilting quotient", re.IGNORECASE),
    re.compile(r"\\mathcal\{C\}\(U_q", re.IGNORECASE),
    re.compile(r"non-semisimple", re.IGNORECASE),
    re.compile(r"before semisimplification", re.IGNORECASE),
    re.compile(r"abelian lift", re.IGNORECASE),
    re.compile(r"BGG reciprocity", re.IGNORECASE),
    re.compile(r"chain-level adjunction", re.IGNORECASE),
    re.compile(r"recovery problem", re.IGNORECASE),
    re.compile(r"programme", re.IGNORECASE),
    re.compile(r"conjectur", re.IGNORECASE),
    re.compile(r"small quantum group", re.IGNORECASE),
)
PERIODICITY_OVERCLAIM_PATTERNS = (
    re.compile(r"proved for minimal models and WZW", re.IGNORECASE),
    re.compile(r"Proved for min\.\ models/WZW", re.IGNORECASE),
    re.compile(r"proved minimal model and WZW cases", re.IGNORECASE),
    re.compile(r"all three periodicity sources are controlled", re.IGNORECASE),
)
PACKAGE_SCOPE_PATTERNS = (
    re.compile(r"full scalar modular characteristic package", re.IGNORECASE),
    re.compile(r"modular characteristic package is trivial", re.IGNORECASE),
    re.compile(r"preserves the modular characteristic package", re.IGNORECASE),
    re.compile(r"consequences of the modular characteristic package", re.IGNORECASE),
    re.compile(r"\(\\Theta_\{\\cA\}, H_\{\\cA\}, \\Delta_\{\\cA\}\)"),
    re.compile(r"`\(\\Theta_A,\s*H_A,\s*\\Delta_A\)`"),
    re.compile(r"universal `Theta_A` package", re.IGNORECASE),
    re.compile(r"N-complex periodicity of Theta_A", re.IGNORECASE),
    re.compile(r"modular package is functorial", re.IGNORECASE),
    re.compile(r"characteristic package \$\(\\Delta_\{\\cA\}, \\Pi_\{\\cA\}, \\Theta_\{\\cA\}\)\$"),
    re.compile(r"characteristic package \$\(\\kappa\(\\cA\), \\Delta_\{\\cA\}\)\$"),
)
MC2_FRONTIER_PATTERNS = (
    re.compile(r"MC2 is the foundational next target", re.IGNORECASE),
    re.compile(r"Foundational next target[^.\n]{0,160}MC2", re.IGNORECASE),
    re.compile(r"immediate foundational target is now MC2", re.IGNORECASE),
    re.compile(r"Advance MC2 first", re.IGNORECASE),
    re.compile(r"build MC2 infrastructure for the cyclic deformation algebra", re.IGNORECASE),
    re.compile(r"MC2 \(cyclic deformation / universal `Theta_A`\) first", re.IGNORECASE),
)
MC2_FRONTIER_SAFE_PATTERNS = (
    re.compile(r"reduction principle", re.IGNORECASE),
    re.compile(r"three exact packages", re.IGNORECASE),
    re.compile(r"three-package frontier", re.IGNORECASE),
    re.compile(r"intrinsic cyclic", re.IGNORECASE),
    re.compile(r"completed tensor", re.IGNORECASE),
    re.compile(r"clutching", re.IGNORECASE),
    re.compile(r"one-channel", re.IGNORECASE),
    re.compile(r"genus-by-genus normalization", re.IGNORECASE),
)
MC2_VERDIER_DRIFT_PATTERNS = (
    re.compile(r"one-channel[^.\n]{0,160}Verdier/Koszul", re.IGNORECASE),
    re.compile(r"Verdier/Koszul[^.\n]{0,160}one-channel", re.IGNORECASE),
    re.compile(r"Verdier/Koszul[^.\n]{0,160}compatibilit", re.IGNORECASE),
)
MC2_VERDIER_SAFE_PATTERNS = (
    re.compile(r"one-channel Verdier/Koszul criterion", re.IGNORECASE),
    re.compile(r"one-channel-verdier-criterion"),
    re.compile(r"\\sigma-stable"),
    re.compile(r"sigma-stable", re.IGNORECASE),
    re.compile(r"Lagrangian", re.IGNORECASE),
    re.compile(r"Verdier-nondegenerate", re.IGNORECASE),
    re.compile(r"two-plane", re.IGNORECASE),
    re.compile(r"opposite one-channel line", re.IGNORECASE),
)
MC2_PTVV_LIFT_PATTERNS = (
    re.compile(r"\bH-level lift\b", re.IGNORECASE),
)
MC2_PTVV_LIFT_SAFE_PATTERNS = (
    re.compile(r"PTVV", re.IGNORECASE),
    re.compile(r"anti-involution", re.IGNORECASE),
    re.compile(r"anti-involution criterion", re.IGNORECASE),
    re.compile(r"one-channel-ptvv-criterion"),
    re.compile(r"projector", re.IGNORECASE),
    re.compile(r"quasi-isomorphism", re.IGNORECASE),
    re.compile(r"Defcyc", re.IGNORECASE),
    re.compile(r"chain-model", re.IGNORECASE),
)
MC2_CHAIN_MODEL_PATTERNS = (
    re.compile(r"one-channel chain models?", re.IGNORECASE),
    re.compile(r"explicit chain-model construction", re.IGNORECASE),
)
MC2_CHAIN_MODEL_SAFE_PATTERNS = (
    re.compile(r"Defcyc", re.IGNORECASE),
    re.compile(r"coderivation", re.IGNORECASE),
    re.compile(r"one-channel-chain-model-criterion"),
    re.compile(r"chain-model criterion", re.IGNORECASE),
    re.compile(r"projector-compatible", re.IGNORECASE),
)
MC2_SEED_PATTERNS = (
    re.compile(r"low-bar-length", re.IGNORECASE),
    re.compile(r"bar-coderivation seeds?", re.IGNORECASE),
    re.compile(r"seed construction inside", re.IGNORECASE),
)
MC2_SEED_SAFE_PATTERNS = (
    re.compile(r"CoDer", re.IGNORECASE),
    re.compile(r"one-channel-seed-criterion"),
    re.compile(r"seed criterion", re.IGNORECASE),
    re.compile(r"coderivation", re.IGNORECASE),
    re.compile(r"bar length", re.IGNORECASE),
    re.compile(r"seed-pairing", re.IGNORECASE),
)
MC2_SEED_PACKET_PATTERNS = (
    re.compile(r"one-cocycle-plus-corrections", re.IGNORECASE),
    re.compile(r"correction packets?", re.IGNORECASE),
    re.compile(r"finite pairing matrix", re.IGNORECASE),
)
MC2_SEED_PACKET_SAFE_PATTERNS = (
    re.compile(r"one-channel-minimal-seed-packet-criterion"),
    re.compile(r"minimal seed-packet criterion", re.IGNORECASE),
    re.compile(r"degree-`?2`? cocycle", re.IGNORECASE),
    re.compile(r"degree-[^\s]{0,12}2", re.IGNORECASE),
    re.compile(r"bar length", re.IGNORECASE),
    re.compile(r"bar-length", re.IGNORECASE),
    re.compile(r"CoDer", re.IGNORECASE),
)
MC2_VISIBLE_LOWARITY_PATTERNS = (
    re.compile(r"simple-pole bracket sector", re.IGNORECASE),
    re.compile(r"double-pole pairing matrix", re.IGNORECASE),
    re.compile(r"Killing[- ]?\$?l_3", re.IGNORECASE),
    re.compile(r"visible low-arity", re.IGNORECASE),
)
MC2_VISIBLE_LOWARITY_SAFE_PATTERNS = (
    re.compile(r"one-channel-visible-lowarity-packet-criterion"),
    re.compile(r"visible low-arity seed-packet criterion", re.IGNORECASE),
    re.compile(r"simple-pole", re.IGNORECASE),
    re.compile(r"double-pole", re.IGNORECASE),
    re.compile(r"Killing", re.IGNORECASE),
    re.compile(r"packet", re.IGNORECASE),
    re.compile(r"eta", re.IGNORECASE),
)
MC2_TRANSFER_PACKAGE_PATTERNS = (
    re.compile(r"canonical transfer package", re.IGNORECASE),
    re.compile(r"generator-seed lift", re.IGNORECASE),
    re.compile(r"functorial normalization", re.IGNORECASE),
)
MC2_TRANSFER_PACKAGE_SAFE_PATTERNS = (
    re.compile(r"one-channel-canonical-transfer-criterion"),
    re.compile(r"one-channel-transfer-law-criterion"),
    re.compile(r"one-channel-visible-lowarity-packet-criterion"),
    re.compile(r"canonical transfer-package criterion", re.IGNORECASE),
    re.compile(r"root-string transfer law", re.IGNORECASE),
    re.compile(r"universal seed formula", re.IGNORECASE),
    re.compile(r"one-channel seed spaces", re.IGNORECASE),
    re.compile(r"cyclic seed", re.IGNORECASE),
    re.compile(r"simple-pole", re.IGNORECASE),
    re.compile(r"Killing", re.IGNORECASE),
    re.compile(r"cocycle line", re.IGNORECASE),
    re.compile(r"visible low-arity packet", re.IGNORECASE),
)
MC2_TRANSFER_LAW_PATTERNS = (
    re.compile(r"root-string transfer law", re.IGNORECASE),
    re.compile(r"universal seed formula", re.IGNORECASE),
    re.compile(r"obstruction-side recovery", re.IGNORECASE),
    re.compile(r"round-trip exact", re.IGNORECASE),
)
MC2_TRANSFER_LAW_SAFE_PATTERNS = (
    re.compile(r"one-channel-transfer-law-criterion"),
    re.compile(r"root-string transfer-law criterion", re.IGNORECASE),
    re.compile(r"canonical transfer package", re.IGNORECASE),
    re.compile(r"root-string", re.IGNORECASE),
    re.compile(r"O_2"),
    re.compile(r"O_3"),
    re.compile(r"obstruction", re.IGNORECASE),
)
MC2_CHART_PATTERNS = (
    re.compile(r"root-string chart", re.IGNORECASE),
    re.compile(r"chart[- ]existence", re.IGNORECASE),
    re.compile(r"chart[- ]uniqueness", re.IGNORECASE),
    re.compile(r"chart is forced", re.IGNORECASE),
    re.compile(r"forced .*seed-line rescaling", re.IGNORECASE),
)
MC2_CHART_SAFE_PATTERNS = (
    re.compile(r"one-channel-root-string-chart-criterion"),
    re.compile(r"root-string chart criterion", re.IGNORECASE),
    re.compile(r"chart-existence/uniqueness", re.IGNORECASE),
    re.compile(r"root-string chart differs by rescaling", re.IGNORECASE),
    re.compile(r"shifted root-string chart", re.IGNORECASE),
    re.compile(r"root-string chart at channel level", re.IGNORECASE),
    re.compile(r"support graph", re.IGNORECASE),
    re.compile(r"seed-line rescaling", re.IGNORECASE),
    re.compile(r"root-string transfer law", re.IGNORECASE),
    re.compile(r"one-channel seed spaces", re.IGNORECASE),
)
MC2_LINE_DETECTION_PATTERNS = (
    re.compile(r"intrinsic line-detection", re.IGNORECASE),
    re.compile(r"canonically picked out", re.IGNORECASE),
    re.compile(r"detected intrinsically", re.IGNORECASE),
    re.compile(r"intrinsic one-channel data", re.IGNORECASE),
)
MC2_LINE_DETECTION_SAFE_PATTERNS = (
    re.compile(r"one-channel-intrinsic-line-detection-criterion"),
    re.compile(r"intrinsic line-detection criterion", re.IGNORECASE),
    re.compile(r"intrinsic line-detection statement", re.IGNORECASE),
    re.compile(r"root-string chart", re.IGNORECASE),
    re.compile(r"one-channel support lines", re.IGNORECASE),
    re.compile(r"l_\{2,\\mathrm\{sp\}\}"),
    re.compile(r"beta", re.IGNORECASE),
    re.compile(r"obstruction", re.IGNORECASE),
)
MC2_AUTOMORPHISM_RIGIDITY_PATTERNS = (
    re.compile(r"automorphism-rigidity", re.IGNORECASE),
    re.compile(r"support automorphism group", re.IGNORECASE),
    re.compile(r"unique invariant lines", re.IGNORECASE),
)
MC2_AUTOMORPHISM_RIGIDITY_SAFE_PATTERNS = (
    re.compile(r"one-channel-automorphism-rigidity-criterion"),
    re.compile(r"automorphism-rigidity criterion", re.IGNORECASE),
    re.compile(r"one-channel support automorphism group", re.IGNORECASE),
    re.compile(r"one-channel support graph", re.IGNORECASE),
    re.compile(r"one-channel support lines", re.IGNORECASE),
    re.compile(r"root-string", re.IGNORECASE),
    re.compile(r"bracket", re.IGNORECASE),
    re.compile(r"pairing", re.IGNORECASE),
)
MC2_STABILIZER_PATTERNS = (
    re.compile(r"support-graph stabilizer", re.IGNORECASE),
    re.compile(r"stabilizer computation", re.IGNORECASE),
    re.compile(r"fixed vertices", re.IGNORECASE),
)
MC2_STABILIZER_SAFE_PATTERNS = (
    re.compile(r"one-channel-support-graph-stabilizer-criterion"),
    re.compile(r"support-graph stabilizer criterion", re.IGNORECASE),
    re.compile(r"one-channel support graph", re.IGNORECASE),
    re.compile(r"one-channel support automorphism group", re.IGNORECASE),
    re.compile(r"one-channel\s+support-graph stabilizer", re.IGNORECASE),
    re.compile(r"fixed vertices of .*Stab", re.IGNORECASE),
    re.compile(r"only fixed vertices inside it", re.IGNORECASE),
    re.compile(r"simple-pole", re.IGNORECASE),
    re.compile(r"root-string", re.IGNORECASE),
)
MC2_INCIDENCE_ORBIT_PATTERNS = (
    re.compile(r"incidence-matrix", re.IGNORECASE),
    re.compile(r"orbit-count", re.IGNORECASE),
    re.compile(r"singleton orbits", re.IGNORECASE),
    re.compile(r"visible permutation group", re.IGNORECASE),
    re.compile(r"small-group computation", re.IGNORECASE),
)
MC2_INCIDENCE_ORBIT_SAFE_PATTERNS = (
    re.compile(r"one-channel-incidence-orbit-criterion"),
    re.compile(r"incidence-matrix / orbit-count criterion", re.IGNORECASE),
    re.compile(r"support-graph stabilizer", re.IGNORECASE),
    re.compile(r"one-channel support graph", re.IGNORECASE),
    re.compile(r"normalization-zero subgraph", re.IGNORECASE),
    re.compile(r"root-string", re.IGNORECASE),
    re.compile(r"bracket", re.IGNORECASE),
    re.compile(r"pairing", re.IGNORECASE),
    re.compile(r"support indicators", re.IGNORECASE),
)
MC2_ORBIT_TABLE_PATTERNS = (
    re.compile(r"orbit table", re.IGNORECASE),
    re.compile(r"three-case", re.IGNORECASE),
    re.compile(r"m=1,2,3"),
    re.compile(r"small-group computation", re.IGNORECASE),
)
MC2_ORBIT_TABLE_SAFE_PATTERNS = (
    re.compile(r"one-channel-visible-orbit-table-criterion"),
    re.compile(r"visible root-string orbit-table criterion", re.IGNORECASE),
    re.compile(r"incidence-matrix / orbit-count", re.IGNORECASE),
    re.compile(r"singleton orbits", re.IGNORECASE),
    re.compile(r"invariant-signature", re.IGNORECASE),
    re.compile(r"invariant signature", re.IGNORECASE),
    re.compile(r"mathfrak\{sl\}_3"),
    re.compile(r"mathfrak\{sp\}_4"),
    re.compile(r"mathfrak\{g\}_2"),
    re.compile(r"sl_3", re.IGNORECASE),
    re.compile(r"sp_4", re.IGNORECASE),
    re.compile(r"g_2", re.IGNORECASE),
    re.compile(r"root-string", re.IGNORECASE),
)
MC2_UNIVERSAL_TABLE_PATTERNS = (
    re.compile(r"canonical universal orbit table", re.IGNORECASE),
    re.compile(r"canonical universal table", re.IGNORECASE),
    re.compile(r"direct lookup", re.IGNORECASE),
    re.compile(r"lookup/identification", re.IGNORECASE),
    re.compile(r"fixed labeled orbit table", re.IGNORECASE),
)
MC2_UNIVERSAL_TABLE_SAFE_PATTERNS = (
    re.compile(r"one-channel-canonical-universal-orbit-table-criterion"),
    re.compile(r"canonical universal orbit-table criterion", re.IGNORECASE),
    re.compile(r"visible orbit-table", re.IGNORECASE),
    re.compile(r"invariant-signature", re.IGNORECASE),
    re.compile(r"invariant signature", re.IGNORECASE),
    re.compile(r"root-string", re.IGNORECASE),
    re.compile(r"m=1,2,3"),
    re.compile(r"sl_3", re.IGNORECASE),
    re.compile(r"sp_4", re.IGNORECASE),
    re.compile(r"g_2", re.IGNORECASE),
)
MC2_INVARIANT_SIGNATURE_PATTERNS = (
    re.compile(r"invariant signature", re.IGNORECASE),
    re.compile(r"minimal invariant signature packet", re.IGNORECASE),
    re.compile(r"forces that table", re.IGNORECASE),
    re.compile(r"forced by one invariant signature", re.IGNORECASE),
)
MC2_INVARIANT_SIGNATURE_SAFE_PATTERNS = (
    re.compile(r"one-channel-universal-invariant-signature-criterion"),
    re.compile(r"universal invariant-signature criterion", re.IGNORECASE),
    re.compile(r"universal invariant signature packet", re.IGNORECASE),
    re.compile(r"minimal invariant signature packet", re.IGNORECASE),
    re.compile(r"invariant signature packet", re.IGNORECASE),
    re.compile(r"canonical universal orbit table", re.IGNORECASE),
    re.compile(r"root-string", re.IGNORECASE),
    re.compile(r"visible", re.IGNORECASE),
    re.compile(r"lookup/identification", re.IGNORECASE),
    re.compile(r"forces that table", re.IGNORECASE),
    re.compile(r"forces the visible one-channel table", re.IGNORECASE),
)
MC2_SEED_CHARACTER_PATTERNS = (
    re.compile(r"signed seed-character", re.IGNORECASE),
    re.compile(r"seed character", re.IGNORECASE),
    re.compile(r"recovering that packet", re.IGNORECASE),
    re.compile(r"root-string character", re.IGNORECASE),
)
MC2_SEED_CHARACTER_SAFE_PATTERNS = (
    re.compile(r"one-channel-signed-seed-character-criterion"),
    re.compile(r"signed seed-character criterion", re.IGNORECASE),
    re.compile(r"universal signed seed-character law", re.IGNORECASE),
    re.compile(r"universal signed seed-character", re.IGNORECASE),
    re.compile(r"signed seed-character", re.IGNORECASE),
    re.compile(r"root-string", re.IGNORECASE),
    re.compile(r"visible", re.IGNORECASE),
    re.compile(r"invariant signature", re.IGNORECASE),
)
MC2_TWOSIGN_SCALAR_PATTERNS = (
    re.compile(r"two-sign plus normalization-scalar", re.IGNORECASE),
    re.compile(r"two signs and one normalization scalar", re.IGNORECASE),
    re.compile(r"reduced root-string datum", re.IGNORECASE),
    re.compile(r"normalization scalar", re.IGNORECASE),
)
MC2_TWOSIGN_SCALAR_SAFE_PATTERNS = (
    re.compile(r"one-channel-two-sign-plus-normalization-scalar-criterion"),
    re.compile(r"two-sign plus normalization-scalar criterion", re.IGNORECASE),
    re.compile(r"universal two-sign plus normalization-scalar law", re.IGNORECASE),
    re.compile(r"reduced root-string datum", re.IGNORECASE),
    re.compile(r"one-channel-parity-sign-plus-normalization-scalar-criterion"),
    re.compile(r"parity-sign plus normalization-scalar datum", re.IGNORECASE),
    re.compile(r"root-string", re.IGNORECASE),
    re.compile(r"signed seed-character", re.IGNORECASE),
)
MC2_PARITY_SCALAR_PATTERNS = (
    re.compile(r"parity sign plus normalization scalar", re.IGNORECASE),
    re.compile(r"root-string parity sign", re.IGNORECASE),
    re.compile(r"one normalization scalar", re.IGNORECASE),
    re.compile(r"parity-sign", re.IGNORECASE),
)
MC2_PARITY_SCALAR_SAFE_PATTERNS = (
    re.compile(r"one-channel-parity-sign-plus-normalization-scalar-criterion"),
    re.compile(r"parity-sign plus normalization-scalar criterion", re.IGNORECASE),
    re.compile(r"root-string parity sign plus normalization scalar", re.IGNORECASE),
    re.compile(r"parity sign plus normalization scalar", re.IGNORECASE),
    re.compile(r"two root-string signs and one normalization scalar", re.IGNORECASE),
    re.compile(r"recovering that reduced datum", re.IGNORECASE),
    re.compile(r"two-sign plus normalization-scalar", re.IGNORECASE),
    re.compile(r"reduced root-string datum", re.IGNORECASE),
    re.compile(r"transfer law", re.IGNORECASE),
)
MC2_PARITY_FORCING_PATTERNS = (
    re.compile(r"chart-normalized seed scalar", re.IGNORECASE),
    re.compile(r"parity-forcing", re.IGNORECASE),
    re.compile(r"forces the parity sign", re.IGNORECASE),
    re.compile(r"ordered root-string chart", re.IGNORECASE),
)
MC2_PARITY_FORCING_SAFE_PATTERNS = (
    re.compile(r"one-channel-parity-forcing-criterion"),
    re.compile(r"parity-forcing criterion", re.IGNORECASE),
    re.compile(r"chart-normalized seed scalar", re.IGNORECASE),
    re.compile(r"normalization convention", re.IGNORECASE),
    re.compile(r"root-string", re.IGNORECASE),
    re.compile(r"parity sign", re.IGNORECASE),
)
NONPRINCIPAL_PACKET_PATTERNS = (
    re.compile(r"representation-theoretic frontier", re.IGNORECASE),
    re.compile(r"orbit-duality frontier", re.IGNORECASE),
    re.compile(r"non-principal orbit duality", re.IGNORECASE),
    re.compile(r"DS reduction for arbitrary f", re.IGNORECASE),
    re.compile(r"BV duality theory", re.IGNORECASE),
    re.compile(r"level-shift formula k' = k'\(k, f\)", re.IGNORECASE),
    re.compile(
        r"generalizing the principal case to arbitrary nilpotent",
        re.IGNORECASE,
    ),
    re.compile(
        r"for general nilpotent orbits and Langlands dual groups",
        re.IGNORECASE,
    ),
)
NONPRINCIPAL_PACKET_SAFE_PATTERNS = (
    re.compile(r"three exact packets", re.IGNORECASE),
    re.compile(r"exact remaining packets", re.IGNORECASE),
    re.compile(r"dual-orbit input", re.IGNORECASE),
    re.compile(r"orbit-indexed level shift", re.IGNORECASE),
    re.compile(r"paired DS seed transport", re.IGNORECASE),
    re.compile(r"transport/globalization", re.IGNORECASE),
    re.compile(r"without the packet split", re.IGNORECASE),
    re.compile(r"Exact packet A", re.IGNORECASE),
    re.compile(r"Packet 11\.A", re.IGNORECASE),
)
EN_AXIS_PATTERNS = (
    re.compile(r"curves \(n = 1\)", re.IGNORECASE),
    re.compile(r"\bn ?= ?1 recovery\b", re.IGNORECASE),
    re.compile(r"\bn ?= ?1 case proved\b", re.IGNORECASE),
    re.compile(r"specialization to n=1", re.IGNORECASE),
    re.compile(r"E_1 vs E_inf dictionary", re.IGNORECASE),
    re.compile(r"curve inside (?:a )?real surface", re.IGNORECASE),
)
EN_AXIS_SAFE_PATTERNS = (
    re.compile(r"n ?= ?2", re.IGNORECASE),
    re.compile(r"real oriented surface", re.IGNORECASE),
    re.compile(r"topological shadow", re.IGNORECASE),
    re.compile(r"not[^.\n]{0,80}manifold dimension", re.IGNORECASE),
    re.compile(r"little-disks", re.IGNORECASE),
    re.compile(r"internal [^.\n]{0,80} chiral hierarchy", re.IGNORECASE),
    re.compile(r"historical alias", re.IGNORECASE),
)
FRONTIER_STALE_PHRASE_PATTERNS = (
    re.compile(r"four remaining master conjectures", re.IGNORECASE),
    re.compile(r"remaining master conjectures", re.IGNORECASE),
    re.compile(r"completed infinite-generator bar theory", re.IGNORECASE),
    re.compile(r"completed infinite-generator bar", re.IGNORECASE),
    re.compile(r"Completed bar ∞-gen", re.IGNORECASE),
)
PROMPT_POINTER_DRIFT_PATTERNS = (
    re.compile(r"Session prompt:\s*notes/SESSION_PROMPT_v(?:2[4-9]|[3-9]\d)\.md"),
    re.compile(
        r"current execution prompt[^.\n]{0,160}SESSION_PROMPT_v(?:2[4-9]|[3-9]\d)\.md",
        re.IGNORECASE,
    ),
    re.compile(
        r"live control prompt[^.\n]{0,160}SESSION_PROMPT_v(?:2[4-9]|[3-9]\d)\.md",
        re.IGNORECASE,
    ),
)
MC3_WORDING_DRIFT_PATTERNS = (
    re.compile(r"\beval-gen core\b", re.IGNORECASE),
    re.compile(r"\bbeyond generated core\b", re.IGNORECASE),
)
MC3_WORDING_SAFE_PATTERNS = (
    re.compile(r"evaluation-generated core", re.IGNORECASE),
    re.compile(r"D\^b\(\\mathcal O_\{\\mathrm\{poly\}\}\)"),
    re.compile(r"ordinary-derived", re.IGNORECASE),
    re.compile(r"completed/coderived", re.IGNORECASE),
)
MC4_WORDING_DRIFT_PATTERNS = (
    re.compile(r"H-level coefficients open", re.IGNORECASE),
    re.compile(r"H-level MC4 comparison", re.IGNORECASE),
)
MC4_TARGET_SAFE_PATTERNS = (
    re.compile(r"\\mathcal W\^\{\\mathrm\{ht\}\}|\\mathcal W\^\{ht\}|W\^\{ht\}"),
    re.compile(r"\\Ydg_\{\\cA\}|Ydg_\{\\cA\}|Ydg_A|dg-shifted Yangian", re.IGNORECASE),
    re.compile(r"filtered H-level targets", re.IGNORECASE),
)
MC4_PACKET_SAFE_PATTERNS = (
    re.compile(r"\\mathcal I_N|mathcal\{I\}_N|\bI_N\b"),
    re.compile(r"\\Delta_\{a,0\}\(N\)|Delta_\{a,0\}\(N\)"),
    re.compile(r"K\^\{line\}|K\\\^line|C\^\{res\}|C\\\^\{res\}"),
    re.compile(r"finite quotients", re.IGNORECASE),
)
PHYSICS_DICTIONARY_DRIFT_PATTERNS = (
    re.compile(r"is governed by genus-graded Koszul duality", re.IGNORECASE),
    re.compile(r"realizes open-closed string duality", re.IGNORECASE),
    re.compile(r"maps boundary operators to bulk fields", re.IGNORECASE),
    re.compile(r"reconstructs boundary correlators from bulk data", re.IGNORECASE),
    re.compile(r"Koszul duality = holographic duality", re.IGNORECASE),
    re.compile(
        r"The AdS\$_3\$/CFT\$_2\$ correspondence exchanges:",
        re.IGNORECASE,
    ),
    re.compile(
        r"The AdS\$_3\$/CFT\$_2\$ correspondence identifies the bulk Chern--Simons theory",
        re.IGNORECASE,
    ),
    re.compile(
        r"The dictionary identifies the boundary WZW model",
        re.IGNORECASE,
    ),
    re.compile(
        r"The quantization of the boundary theory controls the bulk theory",
        re.IGNORECASE,
    ),
    re.compile(
        r"The conjecture identifies the holographic bulk-boundary correspondence with Koszul duality",
        re.IGNORECASE,
    ),
    re.compile(
        r"The conjecture formulates the AdS\$_3\$/CFT\$_2\$ holographic correspondence as an instance of chiral Koszul duality exchanging",
        re.IGNORECASE,
    ),
    re.compile(
        r"The conjecture identifies the bar-cobar adjunction with the holographic boundary-bulk correspondence",
        re.IGNORECASE,
    ),
    re.compile(
        r"Every AdS gravity theory yields a quantum group via Koszul duality",
        re.IGNORECASE,
    ),
    re.compile(
        r"Three-point functions in AdS/CFT are computed by the Koszul pairing",
        re.IGNORECASE,
    ),
    re.compile(
        r"Given a boundary chiral algebra \$\\mathcal\{A\}_\{\\text\{CFT\}\}\$, the bulk theory is reconstructed as:",
        re.IGNORECASE,
    ),
    re.compile(
        r"The conjecture identifies bar-cobar duality with the AdS\$_3\$/CFT\$_2\$ correspondence",
        re.IGNORECASE,
    ),
    re.compile(
        r"The Gaberdiel--Gopakumar duality .* identifies",
        re.IGNORECASE,
    ),
    re.compile(
        r"\\cA\^!_\{g_s\} then describes the bulk theory with",
        re.IGNORECASE,
    ),
    re.compile(
        r"The conjecture identifies bar complex cohomology with string scattering amplitudes at all genera",
        re.IGNORECASE,
    ),
    re.compile(
        r"The conjecture identifies the bar complex Fredholm determinant with the worldsheet path integral",
        re.IGNORECASE,
    ),
    re.compile(
        r"Under this correspondence, the bar differential is identified with the BRST operator of string theory",
        re.IGNORECASE,
    ),
    re.compile(
        r"The conjecture identifies each step of the dimensional reduction tower",
        re.IGNORECASE,
    ),
    re.compile(
        r"The conjecture identifies the chiral algebra of local operators on the Hitchin moduli space",
        re.IGNORECASE,
    ),
    re.compile(
        r"The conjecture identifies bar complex elements with off-shell correlation functions",
        re.IGNORECASE,
    ),
    re.compile(
        r"The conjecture identifies cobar complex elements with on-shell propagators",
        re.IGNORECASE,
    ),
    re.compile(
        r"The conjecture identifies the \$A_\\\\infty\$ operations \$m_k\$ with loop-level corrections",
        re.IGNORECASE,
    ),
    re.compile(
        r"The conjecture identifies bar complex elements with worldline Feynman amplitude integrands",
        re.IGNORECASE,
    ),
    re.compile(
        r"The conjecture identifies W-algebra Koszul duality with S-duality",
        re.IGNORECASE,
    ),
    re.compile(
        r"The conjecture identifies Yangian--quantum affine Koszul duality",
        re.IGNORECASE,
    ),
    re.compile(
        r"The conjecture identifies topological \$\\\\Eone\$-Koszul duality",
        re.IGNORECASE,
    ),
    re.compile(
        r"The conjecture identifies D-brane vertex algebras as \$\\\\Eone\$-chiral algebras",
        re.IGNORECASE,
    ),
    re.compile(
        r"The conjecture identifies conformal blocks of the quantum W-algebra",
        re.IGNORECASE,
    ),
    re.compile(
        r"The conjecture identifies the bar complex of \$\\\\widehat\{\\\\fg\}_k\$",
        re.IGNORECASE,
    ),
    re.compile(
        r"The conjecture identifies the coderived category of the periodic bar complex",
        re.IGNORECASE,
    ),
    re.compile(
        r"realizing symplectic duality at the \$\\\\Eone\$-chiral level",
        re.IGNORECASE,
    ),
    re.compile(
        r"provides a chain-level realization of the Drinfeld--Kohno",
        re.IGNORECASE,
    ),
    re.compile(
        r"is identified with the quantum group factorization structure",
        re.IGNORECASE,
    ),
    re.compile(
        r"already realized factorization category",
        re.IGNORECASE,
    ),
    re.compile(
        r"the bar complex computes the Feynman diagram expansion",
        re.IGNORECASE,
    ),
    re.compile(
        r"Feynman integrals <-> bar complex operations",
        re.IGNORECASE,
    ),
    re.compile(
        r"A_infinity relations are equivalent to cancellation of Feynman diagram anomalies",
        re.IGNORECASE,
    ),
)


@dataclass(frozen=True)
class Finding:
    path: pathlib.Path
    line: int
    detail: str


@dataclass(frozen=True)
class Paragraph:
    path: pathlib.Path
    line: int
    text: str
    normalized: str


def iter_tex_files() -> list[pathlib.Path]:
    files: list[pathlib.Path] = []
    for entry in SCAN_ROOTS:
        path = ROOT / entry
        if path.is_file():
            files.append(path)
            continue
        files.extend(sorted(path.rglob("*.tex")))
    return [
        path
        for path in sorted(files)
        if "archive/legacy" not in str(path) and "_legacy_" not in path.name
    ]


def iter_drift_files() -> list[pathlib.Path]:
    files = iter_tex_files()
    for entry in dict.fromkeys((*CONTROL_DOCS, *FRONTIER_PHRASE_DOCS)):
        path = ROOT / entry
        if path.exists():
            files.append(path)
    return sorted(dict.fromkeys(files))


def iter_globbed_docs(patterns: tuple[str, ...]) -> list[pathlib.Path]:
    files: list[pathlib.Path] = []
    for pattern in patterns:
        files.extend(sorted(ROOT.glob(pattern)))
    return sorted(dict.fromkeys(files))


def active_include_graph() -> set[pathlib.Path]:
    main_path = ROOT / "main.tex"
    lines = clean_lines(main_path)
    text = "\n".join(lines)
    active = {pathlib.Path("main.tex")}
    for match in re.finditer(r"\\(?:include|input)\{([^}]+)\}", text):
        include = pathlib.Path(match.group(1))
        if include.suffix != ".tex":
            include = include.with_suffix(".tex")
        active.add(include)
    return active


def strip_comments(line: str) -> str:
    escaped = False
    chars: list[str] = []
    for ch in line:
        if ch == "%" and not escaped:
            break
        chars.append(ch)
        escaped = ch == "\\"
        if ch != "\\":
            escaped = False
    return "".join(chars)


def clean_lines(path: pathlib.Path) -> list[str]:
    return [strip_comments(line.rstrip("\n")) for line in path.read_text(encoding="utf-8", errors="ignore").splitlines()]


def paragraph_iter(path: pathlib.Path, lines: list[str]) -> list[Paragraph]:
    paragraphs: list[Paragraph] = []
    start = 0
    while start < len(lines):
        while start < len(lines) and not lines[start].strip():
            start += 1
        if start >= len(lines):
            break
        end = start
        block: list[str] = []
        while end < len(lines) and lines[end].strip():
            block.append(lines[end].strip())
            end += 1
        text = " ".join(block)
        if len(text) >= 180 and not text.startswith("\\begin") and not text.startswith("\\end"):
            normalized = normalize_paragraph(text)
            paragraphs.append(Paragraph(path=path, line=start + 1, text=text, normalized=normalized))
        start = end
    return paragraphs


def normalize_paragraph(text: str) -> str:
    norm = re.sub(r"\\label\{[^}]+\}", "", text)
    norm = re.sub(r"\\index\{[^}]+\}", "", norm)
    norm = re.sub(r"\\cite\{[^}]+\}", "CITE", norm)
    norm = re.sub(r"\\(?:eq)?ref\{[^}]+\}", "REF", norm)
    norm = re.sub(r"\s+", " ", norm).strip()
    return norm


def is_chapter_like(path: pathlib.Path) -> bool:
    return path.parts[0] in {"chapters", "appendices"}


def scan() -> dict[str, object]:
    files = iter_tex_files()
    drift_files = iter_drift_files()
    active_files = active_include_graph()
    frontier_phrase_docs = {pathlib.Path(entry) for entry in FRONTIER_PHRASE_DOCS}
    total_lines = 0
    missing_goq: list[pathlib.Path] = []
    missing_hms: list[pathlib.Path] = []
    untagged: list[Finding] = []
    prior_version: list[Finding] = []
    ai_tells: list[Finding] = []
    ambiguous_status: list[Finding] = []
    virasoro_shadow_drift: list[Finding] = []
    infinite_generator_drift: list[Finding] = []
    dk_scope_drift: list[Finding] = []
    periodicity_profile_drift: list[Finding] = []
    kl_scope_drift: list[Finding] = []
    periodicity_overclaim_drift: list[Finding] = []
    package_scope_drift: list[Finding] = []
    mc2_frontier_drift: list[Finding] = []
    mc2_verdier_drift: list[Finding] = []
    mc2_ptvv_lift_drift: list[Finding] = []
    mc2_chain_model_drift: list[Finding] = []
    mc2_seed_drift: list[Finding] = []
    mc2_seed_packet_drift: list[Finding] = []
    mc2_visible_lowarity_drift: list[Finding] = []
    mc2_transfer_package_drift: list[Finding] = []
    mc2_transfer_law_drift: list[Finding] = []
    mc2_chart_drift: list[Finding] = []
    mc2_line_detection_drift: list[Finding] = []
    mc2_automorphism_rigidity_drift: list[Finding] = []
    mc2_stabilizer_drift: list[Finding] = []
    mc2_incidence_orbit_drift: list[Finding] = []
    mc2_orbit_table_drift: list[Finding] = []
    mc2_universal_table_drift: list[Finding] = []
    mc2_invariant_signature_drift: list[Finding] = []
    mc2_seed_character_drift: list[Finding] = []
    mc2_twosign_scalar_drift: list[Finding] = []
    mc2_parity_scalar_drift: list[Finding] = []
    mc2_parity_forcing_drift: list[Finding] = []
    nonprincipal_packet_drift: list[Finding] = []
    en_axis_drift: list[Finding] = []
    frontier_stale_phrase_drift: list[Finding] = []
    physics_dictionary_drift: list[Finding] = []
    active_prompt_banner_drift: list[Finding] = []
    archival_prompt_banner_drift: list[Finding] = []
    active_state_banner_drift: list[Finding] = []
    archival_state_banner_drift: list[Finding] = []
    prompt_pointer_drift: list[Finding] = []
    mc3_wording_drift: list[Finding] = []
    mc4_wording_drift: list[Finding] = []
    long_paragraphs: list[Paragraph] = []
    duplicate_map: dict[str, list[Paragraph]] = collections.defaultdict(list)

    head_re = re.compile(r"\\begin\{(" + "|".join(THEOREM_ENVS) + r")\}")
    active_meta_docs = {
        pathlib.Path(entry)
        for entry in ACTIVE_META_DOCS
        if (ROOT / entry).exists()
    }
    active_prompt_docs = {
        pathlib.Path(entry)
        for entry in ACTIVE_PROMPT_DOCS
        if (ROOT / entry).exists()
    }
    active_state_docs = {
        pathlib.Path(entry)
        for entry in ACTIVE_STATE_DOCS
        if (ROOT / entry).exists()
    }
    archival_prompt_docs = {
        path.relative_to(ROOT)
        for path in iter_globbed_docs(ARCHIVAL_PROMPT_GLOBS)
    } - active_prompt_docs
    archival_state_docs = {
        path.relative_to(ROOT)
        for path in iter_globbed_docs(ARCHIVAL_STATE_GLOBS)
    } - active_state_docs

    for rel in sorted(active_prompt_docs):
        lines = clean_lines(ROOT / rel)
        window = "\n".join(lines[:8])
        if "Active doctrine note" not in window:
            active_prompt_banner_drift.append(
                Finding(rel, 1, "missing `Active doctrine note` banner near top of file")
            )
    for rel in sorted(archival_prompt_docs):
        lines = clean_lines(ROOT / rel)
        window = "\n".join(lines[:8])
        if "Historical prompt note" not in window:
            archival_prompt_banner_drift.append(
                Finding(rel, 1, "missing `Historical prompt note` banner near top of file")
            )
    for rel in sorted(active_state_docs):
        lines = clean_lines(ROOT / rel)
        window = "\n".join(lines[:8])
        if "Live state note" not in window:
            active_state_banner_drift.append(
                Finding(rel, 1, "missing `Live state note` banner near top of file")
            )
    for rel in sorted(archival_state_docs):
        lines = clean_lines(ROOT / rel)
        window = "\n".join(lines[:8])
        if "Historical state note" not in window:
            archival_state_banner_drift.append(
                Finding(rel, 1, "missing `Historical state note` banner near top of file")
            )
    for rel in sorted(
        pathlib.Path(entry)
        for entry in LIVE_PROMPT_POINTER_DOCS
        if (ROOT / entry).exists()
    ):
        lines = clean_lines(ROOT / rel)
        for idx, line in enumerate(lines, start=1):
            if any(pattern.search(line) for pattern in PROMPT_POINTER_DRIFT_PATTERNS):
                prompt_pointer_drift.append(Finding(rel, idx, line.strip()))
    for rel in sorted(active_meta_docs):
        lines = clean_lines(ROOT / rel)
        for idx, line in enumerate(lines, start=1):
            if any(pattern.search(line) for pattern in MC3_WORDING_DRIFT_PATTERNS):
                window = "\n".join(lines[max(0, idx - 3) : min(len(lines), idx + 3)])
                if not any(pattern.search(window) for pattern in MC3_WORDING_SAFE_PATTERNS):
                    mc3_wording_drift.append(Finding(rel, idx, line.strip()))
            if any(pattern.search(line) for pattern in MC4_WORDING_DRIFT_PATTERNS):
                window = "\n".join(lines[max(0, idx - 3) : min(len(lines), idx + 3)])
                if not any(pattern.search(window) for pattern in MC4_TARGET_SAFE_PATTERNS) or not any(
                    pattern.search(window) for pattern in MC4_PACKET_SAFE_PATTERNS
                ):
                    mc4_wording_drift.append(Finding(rel, idx, line.strip()))

    for path in files:
        rel = path.relative_to(ROOT)
        lines = clean_lines(path)
        total_lines += len(lines)
        text = "\n".join(lines)

        is_active = rel in active_files

        if is_active and is_chapter_like(rel):
            if not GOQ_RE.search(text):
                missing_goq.append(rel)
            if not HMS_RE.search(text):
                missing_hms.append(rel)

        for idx, line in enumerate(lines, start=1):
            if is_active:
                for pattern in PRIOR_VERSION_PATTERNS:
                    if pattern.search(line):
                        prior_version.append(Finding(rel, idx, line.strip()))
                        break
                if is_chapter_like(rel):
                    lower = line.lower()
                    # Allow explicit conjectural/open framing.
                    if (
                        "conjectur" not in lower
                        and "\\claimstatusconjectured" not in lower
                        and "\\claimstatusheuristic" not in lower
                    ):
                        for pattern in AMBIGUOUS_STATUS_PATTERNS:
                            if pattern.search(line):
                                ambiguous_status.append(Finding(rel, idx, line.strip()))
                                break
            for pattern in AI_TELL_PATTERNS:
                if pattern.search(line):
                    ai_tells.append(Finding(rel, idx, line.strip()))
                    break
            if is_active and head_re.search(line):
                window = "\n".join(lines[idx - 1 : idx + 7])
                if not STATUS_RE.search(window):
                    untagged.append(Finding(rel, idx, line.strip()))

        if is_active:
            for idx, line in enumerate(lines, start=1):
                if not any(pattern.search(line) for pattern in VIRASORO_DUAL_PATTERNS):
                    continue
                window = "\n".join(lines[max(0, idx - 3) : min(len(lines), idx + 3)])
                if not any(pattern.search(window) for pattern in VIRASORO_SAFE_PATTERNS):
                    virasoro_shadow_drift.append(Finding(rel, idx, line.strip()))
            for idx, line in enumerate(lines, start=1):
                if not any(pattern.search(line) for pattern in INFINITE_GENERATOR_DUAL_PATTERNS):
                    continue
                window = "\n".join(lines[max(0, idx - 3) : min(len(lines), idx + 3)])
                if not any(pattern.search(window) for pattern in INFINITE_GENERATOR_SAFE_PATTERNS):
                    infinite_generator_drift.append(Finding(rel, idx, line.strip()))
            for idx, line in enumerate(lines, start=1):
                if not any(pattern.search(line) for pattern in DK_SCOPE_PATTERNS):
                    continue
                window = "\n".join(lines[max(0, idx - 3) : min(len(lines), idx + 3)])
                if not any(pattern.search(window) for pattern in DK_SCOPE_SAFE_PATTERNS):
                    dk_scope_drift.append(Finding(rel, idx, line.strip()))
            for idx, line in enumerate(lines, start=1):
                if not any(pattern.search(line) for pattern in PERIODICITY_PROFILE_PATTERNS):
                    continue
                periodicity_profile_drift.append(Finding(rel, idx, line.strip()))
            for idx, line in enumerate(lines, start=1):
                if not any(pattern.search(line) for pattern in KL_SCOPE_PATTERNS):
                    continue
                window = "\n".join(lines[max(0, idx - 3) : min(len(lines), idx + 3)])
                lower_window = window.lower()
                if "kazhdan--lusztig" not in lower_window and "u_q" not in lower_window:
                    continue
                if not any(pattern.search(window) for pattern in KL_SCOPE_SAFE_PATTERNS):
                    kl_scope_drift.append(Finding(rel, idx, line.strip()))
            for idx, line in enumerate(lines, start=1):
                if not any(pattern.search(line) for pattern in PERIODICITY_OVERCLAIM_PATTERNS):
                    continue
                periodicity_overclaim_drift.append(Finding(rel, idx, line.strip()))
            for idx, line in enumerate(lines, start=1):
                if not any(pattern.search(line) for pattern in PACKAGE_SCOPE_PATTERNS):
                    continue
                package_scope_drift.append(Finding(rel, idx, line.strip()))
            for idx, line in enumerate(lines, start=1):
                if not any(pattern.search(line) for pattern in MC2_FRONTIER_PATTERNS):
                    continue
                window = "\n".join(lines[max(0, idx - 3) : min(len(lines), idx + 3)])
                if not any(pattern.search(window) for pattern in MC2_FRONTIER_SAFE_PATTERNS):
                    mc2_frontier_drift.append(Finding(rel, idx, line.strip()))
            for idx, line in enumerate(lines, start=1):
                if not any(pattern.search(line) for pattern in MC2_VERDIER_DRIFT_PATTERNS):
                    continue
                window = "\n".join(lines[max(0, idx - 3) : min(len(lines), idx + 3)])
                if not any(pattern.search(window) for pattern in MC2_VERDIER_SAFE_PATTERNS):
                    mc2_verdier_drift.append(Finding(rel, idx, line.strip()))
            for idx, line in enumerate(lines, start=1):
                if not any(pattern.search(line) for pattern in MC2_PTVV_LIFT_PATTERNS):
                    continue
                window = "\n".join(lines[max(0, idx - 3) : min(len(lines), idx + 3)])
                if not any(pattern.search(window) for pattern in MC2_PTVV_LIFT_SAFE_PATTERNS):
                    mc2_ptvv_lift_drift.append(Finding(rel, idx, line.strip()))
            for idx, line in enumerate(lines, start=1):
                if not any(pattern.search(line) for pattern in MC2_CHAIN_MODEL_PATTERNS):
                    continue
                window = "\n".join(lines[max(0, idx - 3) : min(len(lines), idx + 3)])
                if not any(pattern.search(window) for pattern in MC2_CHAIN_MODEL_SAFE_PATTERNS):
                    mc2_chain_model_drift.append(Finding(rel, idx, line.strip()))
            for idx, line in enumerate(lines, start=1):
                if not any(pattern.search(line) for pattern in MC2_SEED_PATTERNS):
                    continue
                window = "\n".join(lines[max(0, idx - 3) : min(len(lines), idx + 3)])
                if not any(pattern.search(window) for pattern in MC2_SEED_SAFE_PATTERNS):
                    mc2_seed_drift.append(Finding(rel, idx, line.strip()))
            for idx, line in enumerate(lines, start=1):
                if not any(pattern.search(line) for pattern in MC2_SEED_PACKET_PATTERNS):
                    continue
                window = "\n".join(lines[max(0, idx - 7) : min(len(lines), idx + 7)])
                if not any(pattern.search(window) for pattern in MC2_SEED_PACKET_SAFE_PATTERNS):
                    mc2_seed_packet_drift.append(Finding(rel, idx, line.strip()))
            for idx, line in enumerate(lines, start=1):
                if not any(pattern.search(line) for pattern in MC2_VISIBLE_LOWARITY_PATTERNS):
                    continue
                window = "\n".join(lines[max(0, idx - 5) : min(len(lines), idx + 5)])
                if not any(pattern.search(window) for pattern in MC2_VISIBLE_LOWARITY_SAFE_PATTERNS):
                    mc2_visible_lowarity_drift.append(Finding(rel, idx, line.strip()))
            for idx, line in enumerate(lines, start=1):
                if not any(pattern.search(line) for pattern in MC2_TRANSFER_PACKAGE_PATTERNS):
                    continue
                window = "\n".join(lines[max(0, idx - 5) : min(len(lines), idx + 5)])
                if not any(pattern.search(window) for pattern in MC2_TRANSFER_PACKAGE_SAFE_PATTERNS):
                    mc2_transfer_package_drift.append(Finding(rel, idx, line.strip()))
            for idx, line in enumerate(lines, start=1):
                if not any(pattern.search(line) for pattern in MC2_TRANSFER_LAW_PATTERNS):
                    continue
                window = "\n".join(lines[max(0, idx - 5) : min(len(lines), idx + 5)])
                if not any(pattern.search(window) for pattern in MC2_TRANSFER_LAW_SAFE_PATTERNS):
                    mc2_transfer_law_drift.append(Finding(rel, idx, line.strip()))
            for idx, line in enumerate(lines, start=1):
                if not any(pattern.search(line) for pattern in MC2_CHART_PATTERNS):
                    continue
                window = "\n".join(lines[max(0, idx - 5) : min(len(lines), idx + 5)])
                if not any(pattern.search(window) for pattern in MC2_CHART_SAFE_PATTERNS):
                    mc2_chart_drift.append(Finding(rel, idx, line.strip()))
            for idx, line in enumerate(lines, start=1):
                if not any(pattern.search(line) for pattern in MC2_LINE_DETECTION_PATTERNS):
                    continue
                window = "\n".join(lines[max(0, idx - 5) : min(len(lines), idx + 5)])
                if not any(pattern.search(window) for pattern in MC2_LINE_DETECTION_SAFE_PATTERNS):
                    mc2_line_detection_drift.append(Finding(rel, idx, line.strip()))
            for idx, line in enumerate(lines, start=1):
                if not any(pattern.search(line) for pattern in MC2_AUTOMORPHISM_RIGIDITY_PATTERNS):
                    continue
                window = "\n".join(lines[max(0, idx - 5) : min(len(lines), idx + 5)])
                if not any(pattern.search(window) for pattern in MC2_AUTOMORPHISM_RIGIDITY_SAFE_PATTERNS):
                    mc2_automorphism_rigidity_drift.append(Finding(rel, idx, line.strip()))
            for idx, line in enumerate(lines, start=1):
                if not any(pattern.search(line) for pattern in MC2_STABILIZER_PATTERNS):
                    continue
                window = "\n".join(lines[max(0, idx - 5) : min(len(lines), idx + 5)])
                if not any(pattern.search(window) for pattern in MC2_STABILIZER_SAFE_PATTERNS):
                    mc2_stabilizer_drift.append(Finding(rel, idx, line.strip()))
            for idx, line in enumerate(lines, start=1):
                if not any(pattern.search(line) for pattern in MC2_INCIDENCE_ORBIT_PATTERNS):
                    continue
                window = "\n".join(lines[max(0, idx - 5) : min(len(lines), idx + 5)])
                if not any(pattern.search(window) for pattern in MC2_INCIDENCE_ORBIT_SAFE_PATTERNS):
                    mc2_incidence_orbit_drift.append(Finding(rel, idx, line.strip()))
            for idx, line in enumerate(lines, start=1):
                if not any(pattern.search(line) for pattern in MC2_ORBIT_TABLE_PATTERNS):
                    continue
                window = "\n".join(lines[max(0, idx - 5) : min(len(lines), idx + 5)])
                if not any(pattern.search(window) for pattern in MC2_ORBIT_TABLE_SAFE_PATTERNS):
                    mc2_orbit_table_drift.append(Finding(rel, idx, line.strip()))
            for idx, line in enumerate(lines, start=1):
                if not any(pattern.search(line) for pattern in MC2_UNIVERSAL_TABLE_PATTERNS):
                    continue
                window = "\n".join(lines[max(0, idx - 5) : min(len(lines), idx + 5)])
                if not any(pattern.search(window) for pattern in MC2_UNIVERSAL_TABLE_SAFE_PATTERNS):
                    mc2_universal_table_drift.append(Finding(rel, idx, line.strip()))
            for idx, line in enumerate(lines, start=1):
                if not any(pattern.search(line) for pattern in MC2_INVARIANT_SIGNATURE_PATTERNS):
                    continue
                window = "\n".join(lines[max(0, idx - 5) : min(len(lines), idx + 5)])
                if not any(pattern.search(window) for pattern in MC2_INVARIANT_SIGNATURE_SAFE_PATTERNS):
                    mc2_invariant_signature_drift.append(Finding(rel, idx, line.strip()))
            for idx, line in enumerate(lines, start=1):
                if not any(pattern.search(line) for pattern in MC2_SEED_CHARACTER_PATTERNS):
                    continue
                window = "\n".join(lines[max(0, idx - 5) : min(len(lines), idx + 5)])
                if not any(pattern.search(window) for pattern in MC2_SEED_CHARACTER_SAFE_PATTERNS):
                    mc2_seed_character_drift.append(Finding(rel, idx, line.strip()))
            for idx, line in enumerate(lines, start=1):
                if not any(pattern.search(line) for pattern in MC2_TWOSIGN_SCALAR_PATTERNS):
                    continue
                window = "\n".join(lines[max(0, idx - 5) : min(len(lines), idx + 5)])
                if not any(pattern.search(window) for pattern in MC2_TWOSIGN_SCALAR_SAFE_PATTERNS):
                    mc2_twosign_scalar_drift.append(Finding(rel, idx, line.strip()))
            for idx, line in enumerate(lines, start=1):
                if not any(pattern.search(line) for pattern in MC2_PARITY_SCALAR_PATTERNS):
                    continue
                window = "\n".join(lines[max(0, idx - 5) : min(len(lines), idx + 5)])
                if not any(pattern.search(window) for pattern in MC2_PARITY_SCALAR_SAFE_PATTERNS):
                    mc2_parity_scalar_drift.append(Finding(rel, idx, line.strip()))
            for idx, line in enumerate(lines, start=1):
                if not any(pattern.search(line) for pattern in MC2_PARITY_FORCING_PATTERNS):
                    continue
                window = "\n".join(lines[max(0, idx - 5) : min(len(lines), idx + 5)])
                if not any(pattern.search(window) for pattern in MC2_PARITY_FORCING_SAFE_PATTERNS):
                    mc2_parity_forcing_drift.append(Finding(rel, idx, line.strip()))
            for idx, line in enumerate(lines, start=1):
                if not any(pattern.search(line) for pattern in NONPRINCIPAL_PACKET_PATTERNS):
                    continue
                window = "\n".join(lines[max(0, idx - 5) : min(len(lines), idx + 5)])
                if not any(pattern.search(window) for pattern in NONPRINCIPAL_PACKET_SAFE_PATTERNS):
                    nonprincipal_packet_drift.append(Finding(rel, idx, line.strip()))
            for idx, line in enumerate(lines, start=1):
                if not any(pattern.search(line) for pattern in EN_AXIS_PATTERNS):
                    continue
                window = "\n".join(lines[max(0, idx - 5) : min(len(lines), idx + 5)])
                if not any(pattern.search(window) for pattern in EN_AXIS_SAFE_PATTERNS):
                    en_axis_drift.append(Finding(rel, idx, line.strip()))
            if rel in frontier_phrase_docs:
                for idx, line in enumerate(lines, start=1):
                    if any(pattern.search(line) for pattern in FRONTIER_STALE_PHRASE_PATTERNS):
                        frontier_stale_phrase_drift.append(Finding(rel, idx, line.strip()))
            for idx, line in enumerate(lines, start=1):
                if any(pattern.search(line) for pattern in PHYSICS_DICTIONARY_DRIFT_PATTERNS):
                    physics_dictionary_drift.append(Finding(rel, idx, line.strip()))

        for para in paragraph_iter(rel, lines):
            if len(para.text) > 1200:
                long_paragraphs.append(para)
            duplicate_map[para.normalized].append(para)

    for path in drift_files:
        rel = path.relative_to(ROOT)
        if rel in active_files:
            continue
        lines = clean_lines(path)
        for idx, line in enumerate(lines, start=1):
            if any(pattern.search(line) for pattern in DK_SCOPE_PATTERNS):
                window = "\n".join(lines[max(0, idx - 3): min(len(lines), idx + 3)])
                if not any(pattern.search(window) for pattern in DK_SCOPE_SAFE_PATTERNS):
                    dk_scope_drift.append(Finding(rel, idx, line.strip()))
            if any(pattern.search(line) for pattern in PERIODICITY_PROFILE_PATTERNS):
                periodicity_profile_drift.append(Finding(rel, idx, line.strip()))
            if any(pattern.search(line) for pattern in KL_SCOPE_PATTERNS):
                window = "\n".join(lines[max(0, idx - 3): min(len(lines), idx + 3)])
                lower_window = window.lower()
                if "kazhdan--lusztig" not in lower_window and "u_q" not in lower_window:
                    continue
                if not any(pattern.search(window) for pattern in KL_SCOPE_SAFE_PATTERNS):
                    kl_scope_drift.append(Finding(rel, idx, line.strip()))
            if any(pattern.search(line) for pattern in PERIODICITY_OVERCLAIM_PATTERNS):
                periodicity_overclaim_drift.append(Finding(rel, idx, line.strip()))
            if any(pattern.search(line) for pattern in PACKAGE_SCOPE_PATTERNS):
                package_scope_drift.append(Finding(rel, idx, line.strip()))
            if any(pattern.search(line) for pattern in MC2_FRONTIER_PATTERNS):
                window = "\n".join(lines[max(0, idx - 3): min(len(lines), idx + 3)])
                if not any(pattern.search(window) for pattern in MC2_FRONTIER_SAFE_PATTERNS):
                    mc2_frontier_drift.append(Finding(rel, idx, line.strip()))
            if any(pattern.search(line) for pattern in MC2_VERDIER_DRIFT_PATTERNS):
                window = "\n".join(lines[max(0, idx - 3): min(len(lines), idx + 3)])
                if not any(pattern.search(window) for pattern in MC2_VERDIER_SAFE_PATTERNS):
                    mc2_verdier_drift.append(Finding(rel, idx, line.strip()))
            if any(pattern.search(line) for pattern in MC2_PTVV_LIFT_PATTERNS):
                window = "\n".join(lines[max(0, idx - 3): min(len(lines), idx + 3)])
                if not any(pattern.search(window) for pattern in MC2_PTVV_LIFT_SAFE_PATTERNS):
                    mc2_ptvv_lift_drift.append(Finding(rel, idx, line.strip()))
            if any(pattern.search(line) for pattern in MC2_CHAIN_MODEL_PATTERNS):
                window = "\n".join(lines[max(0, idx - 3): min(len(lines), idx + 3)])
                if not any(pattern.search(window) for pattern in MC2_CHAIN_MODEL_SAFE_PATTERNS):
                    mc2_chain_model_drift.append(Finding(rel, idx, line.strip()))
            if any(pattern.search(line) for pattern in MC2_SEED_PATTERNS):
                window = "\n".join(lines[max(0, idx - 3): min(len(lines), idx + 3)])
                if not any(pattern.search(window) for pattern in MC2_SEED_SAFE_PATTERNS):
                    mc2_seed_drift.append(Finding(rel, idx, line.strip()))
            if any(pattern.search(line) for pattern in MC2_SEED_PACKET_PATTERNS):
                window = "\n".join(lines[max(0, idx - 7): min(len(lines), idx + 7)])
                if not any(pattern.search(window) for pattern in MC2_SEED_PACKET_SAFE_PATTERNS):
                    mc2_seed_packet_drift.append(Finding(rel, idx, line.strip()))
            if any(pattern.search(line) for pattern in MC2_VISIBLE_LOWARITY_PATTERNS):
                window = "\n".join(lines[max(0, idx - 5): min(len(lines), idx + 5)])
                if not any(pattern.search(window) for pattern in MC2_VISIBLE_LOWARITY_SAFE_PATTERNS):
                    mc2_visible_lowarity_drift.append(Finding(rel, idx, line.strip()))
            if any(pattern.search(line) for pattern in MC2_TRANSFER_PACKAGE_PATTERNS):
                window = "\n".join(lines[max(0, idx - 5): min(len(lines), idx + 5)])
                if not any(pattern.search(window) for pattern in MC2_TRANSFER_PACKAGE_SAFE_PATTERNS):
                    mc2_transfer_package_drift.append(Finding(rel, idx, line.strip()))
            if any(pattern.search(line) for pattern in MC2_TRANSFER_LAW_PATTERNS):
                window = "\n".join(lines[max(0, idx - 5): min(len(lines), idx + 5)])
                if not any(pattern.search(window) for pattern in MC2_TRANSFER_LAW_SAFE_PATTERNS):
                    mc2_transfer_law_drift.append(Finding(rel, idx, line.strip()))
            if any(pattern.search(line) for pattern in MC2_CHART_PATTERNS):
                window = "\n".join(lines[max(0, idx - 5): min(len(lines), idx + 5)])
                if not any(pattern.search(window) for pattern in MC2_CHART_SAFE_PATTERNS):
                    mc2_chart_drift.append(Finding(rel, idx, line.strip()))
            if any(pattern.search(line) for pattern in MC2_LINE_DETECTION_PATTERNS):
                window = "\n".join(lines[max(0, idx - 5): min(len(lines), idx + 5)])
                if not any(pattern.search(window) for pattern in MC2_LINE_DETECTION_SAFE_PATTERNS):
                    mc2_line_detection_drift.append(Finding(rel, idx, line.strip()))
            if any(pattern.search(line) for pattern in MC2_AUTOMORPHISM_RIGIDITY_PATTERNS):
                window = "\n".join(lines[max(0, idx - 5): min(len(lines), idx + 5)])
                if not any(pattern.search(window) for pattern in MC2_AUTOMORPHISM_RIGIDITY_SAFE_PATTERNS):
                    mc2_automorphism_rigidity_drift.append(Finding(rel, idx, line.strip()))
            if any(pattern.search(line) for pattern in MC2_STABILIZER_PATTERNS):
                window = "\n".join(lines[max(0, idx - 5): min(len(lines), idx + 5)])
                if not any(pattern.search(window) for pattern in MC2_STABILIZER_SAFE_PATTERNS):
                    mc2_stabilizer_drift.append(Finding(rel, idx, line.strip()))
            if any(pattern.search(line) for pattern in MC2_INCIDENCE_ORBIT_PATTERNS):
                window = "\n".join(lines[max(0, idx - 5): min(len(lines), idx + 5)])
                if not any(pattern.search(window) for pattern in MC2_INCIDENCE_ORBIT_SAFE_PATTERNS):
                    mc2_incidence_orbit_drift.append(Finding(rel, idx, line.strip()))
            if any(pattern.search(line) for pattern in MC2_ORBIT_TABLE_PATTERNS):
                window = "\n".join(lines[max(0, idx - 5): min(len(lines), idx + 5)])
                if not any(pattern.search(window) for pattern in MC2_ORBIT_TABLE_SAFE_PATTERNS):
                    mc2_orbit_table_drift.append(Finding(rel, idx, line.strip()))
            if any(pattern.search(line) for pattern in MC2_UNIVERSAL_TABLE_PATTERNS):
                window = "\n".join(lines[max(0, idx - 5): min(len(lines), idx + 5)])
                if not any(pattern.search(window) for pattern in MC2_UNIVERSAL_TABLE_SAFE_PATTERNS):
                    mc2_universal_table_drift.append(Finding(rel, idx, line.strip()))
            if any(pattern.search(line) for pattern in MC2_INVARIANT_SIGNATURE_PATTERNS):
                window = "\n".join(lines[max(0, idx - 5): min(len(lines), idx + 5)])
                if not any(pattern.search(window) for pattern in MC2_INVARIANT_SIGNATURE_SAFE_PATTERNS):
                    mc2_invariant_signature_drift.append(Finding(rel, idx, line.strip()))
            if any(pattern.search(line) for pattern in MC2_SEED_CHARACTER_PATTERNS):
                window = "\n".join(lines[max(0, idx - 5): min(len(lines), idx + 5)])
                if not any(pattern.search(window) for pattern in MC2_SEED_CHARACTER_SAFE_PATTERNS):
                    mc2_seed_character_drift.append(Finding(rel, idx, line.strip()))
            if any(pattern.search(line) for pattern in MC2_TWOSIGN_SCALAR_PATTERNS):
                window = "\n".join(lines[max(0, idx - 5): min(len(lines), idx + 5)])
                if not any(pattern.search(window) for pattern in MC2_TWOSIGN_SCALAR_SAFE_PATTERNS):
                    mc2_twosign_scalar_drift.append(Finding(rel, idx, line.strip()))
            if any(pattern.search(line) for pattern in MC2_PARITY_SCALAR_PATTERNS):
                window = "\n".join(lines[max(0, idx - 5): min(len(lines), idx + 5)])
                if not any(pattern.search(window) for pattern in MC2_PARITY_SCALAR_SAFE_PATTERNS):
                    mc2_parity_scalar_drift.append(Finding(rel, idx, line.strip()))
            if any(pattern.search(line) for pattern in MC2_PARITY_FORCING_PATTERNS):
                window = "\n".join(lines[max(0, idx - 5): min(len(lines), idx + 5)])
                if not any(pattern.search(window) for pattern in MC2_PARITY_FORCING_SAFE_PATTERNS):
                    mc2_parity_forcing_drift.append(Finding(rel, idx, line.strip()))
            if any(pattern.search(line) for pattern in NONPRINCIPAL_PACKET_PATTERNS):
                window = "\n".join(lines[max(0, idx - 5): min(len(lines), idx + 5)])
                if not any(pattern.search(window) for pattern in NONPRINCIPAL_PACKET_SAFE_PATTERNS):
                    nonprincipal_packet_drift.append(Finding(rel, idx, line.strip()))
            if any(pattern.search(line) for pattern in EN_AXIS_PATTERNS):
                window = "\n".join(lines[max(0, idx - 5): min(len(lines), idx + 5)])
                if not any(pattern.search(window) for pattern in EN_AXIS_SAFE_PATTERNS):
                    en_axis_drift.append(Finding(rel, idx, line.strip()))
            if rel in frontier_phrase_docs and any(
                pattern.search(line) for pattern in FRONTIER_STALE_PHRASE_PATTERNS
            ):
                frontier_stale_phrase_drift.append(Finding(rel, idx, line.strip()))
            if any(pattern.search(line) for pattern in PHYSICS_DICTIONARY_DRIFT_PATTERNS):
                physics_dictionary_drift.append(Finding(rel, idx, line.strip()))

    duplicates = []
    for norm, paras in duplicate_map.items():
        unique_paths = {para.path for para in paras}
        if len(paras) > 1 and len(unique_paths) > 1:
            duplicates.append((norm, paras))
    duplicates.sort(key=lambda item: (-len(item[1]), item[1][0].path.as_posix(), item[1][0].line))
    long_paragraphs.sort(key=lambda para: (-len(para.text), para.path.as_posix(), para.line))

    return {
        "files": files,
        "active_files": active_files,
        "total_lines": total_lines,
        "missing_goq": missing_goq,
        "missing_hms": missing_hms,
        "untagged": untagged,
        "prior_version": prior_version,
        "ai_tells": ai_tells,
        "ambiguous_status": ambiguous_status,
        "virasoro_shadow_drift": virasoro_shadow_drift,
        "infinite_generator_drift": infinite_generator_drift,
        "dk_scope_drift": dk_scope_drift,
        "periodicity_profile_drift": periodicity_profile_drift,
        "kl_scope_drift": kl_scope_drift,
        "periodicity_overclaim_drift": periodicity_overclaim_drift,
        "package_scope_drift": package_scope_drift,
        "mc2_frontier_drift": mc2_frontier_drift,
        "mc2_verdier_drift": mc2_verdier_drift,
        "mc2_ptvv_lift_drift": mc2_ptvv_lift_drift,
        "mc2_chain_model_drift": mc2_chain_model_drift,
        "mc2_seed_drift": mc2_seed_drift,
        "mc2_seed_packet_drift": mc2_seed_packet_drift,
        "mc2_visible_lowarity_drift": mc2_visible_lowarity_drift,
        "mc2_transfer_package_drift": mc2_transfer_package_drift,
        "mc2_transfer_law_drift": mc2_transfer_law_drift,
        "mc2_chart_drift": mc2_chart_drift,
        "mc2_line_detection_drift": mc2_line_detection_drift,
        "mc2_automorphism_rigidity_drift": mc2_automorphism_rigidity_drift,
        "mc2_stabilizer_drift": mc2_stabilizer_drift,
        "mc2_incidence_orbit_drift": mc2_incidence_orbit_drift,
        "mc2_orbit_table_drift": mc2_orbit_table_drift,
        "mc2_universal_table_drift": mc2_universal_table_drift,
        "mc2_invariant_signature_drift": mc2_invariant_signature_drift,
        "mc2_seed_character_drift": mc2_seed_character_drift,
        "mc2_twosign_scalar_drift": mc2_twosign_scalar_drift,
        "mc2_parity_scalar_drift": mc2_parity_scalar_drift,
        "mc2_parity_forcing_drift": mc2_parity_forcing_drift,
        "nonprincipal_packet_drift": nonprincipal_packet_drift,
        "en_axis_drift": en_axis_drift,
        "frontier_stale_phrase_drift": frontier_stale_phrase_drift,
        "physics_dictionary_drift": physics_dictionary_drift,
        "active_prompt_banner_drift": active_prompt_banner_drift,
        "archival_prompt_banner_drift": archival_prompt_banner_drift,
        "active_state_banner_drift": active_state_banner_drift,
        "archival_state_banner_drift": archival_state_banner_drift,
        "prompt_pointer_drift": prompt_pointer_drift,
        "mc3_wording_drift": mc3_wording_drift,
        "mc4_wording_drift": mc4_wording_drift,
        "long_paragraphs": long_paragraphs,
        "duplicates": duplicates,
    }


def print_section(title: str) -> None:
    print(f"## {title}")


def print_findings(findings: list[Finding], limit: int) -> None:
    for finding in findings[:limit]:
        print(f"- `{finding.path}:{finding.line}` {finding.detail}")
    if len(findings) > limit:
        print(f"- ... {len(findings) - limit} more")


def print_paragraphs(paragraphs: list[Paragraph], limit: int) -> None:
    for para in paragraphs[:limit]:
        snippet = para.text[:180].strip()
        print(f"- `{para.path}:{para.line}` {len(para.text)} chars: {snippet}")
    if len(paragraphs) > limit:
        print(f"- ... {len(paragraphs) - limit} more")


def report(data: dict[str, object], limit: int) -> None:
    files = data["files"]
    print("# Manuscript QC Report")
    print()
    print(f"- Files scanned: `{len(files)}`")
    print(f"- Active files: `{len(data['active_files'])}`")
    print(f"- Lines scanned: `{data['total_lines']}`")
    print(f"- Missing governing-question markers: `{len(data['missing_goq'])}`")
    print(f"- Missing H/M/S markers: `{len(data['missing_hms'])}`")
    print(f"- Untagged theorem heads: `{len(data['untagged'])}`")
    print(f"- Prior-version leaks: `{len(data['prior_version'])}`")
    print(f"- Ambiguous status language: `{len(data['ambiguous_status'])}`")
    print(f"- Virasoro shadow-doctrine drift: `{len(data['virasoro_shadow_drift'])}`")
    print(f"- Infinite-generator frontier drift: `{len(data['infinite_generator_drift'])}`")
    print(f"- DK scope drift: `{len(data['dk_scope_drift'])}`")
    print(f"- Periodicity-profile drift: `{len(data['periodicity_profile_drift'])}`")
    print(f"- KL scope drift: `{len(data['kl_scope_drift'])}`")
    print(f"- Periodicity overclaim drift: `{len(data['periodicity_overclaim_drift'])}`")
    print(f"- Package-scope drift: `{len(data['package_scope_drift'])}`")
    print(f"- MC2 frontier drift: `{len(data['mc2_frontier_drift'])}`")
    print(f"- MC2 Verdier-plane drift: `{len(data['mc2_verdier_drift'])}`")
    print(f"- MC2 PTVV-lift drift: `{len(data['mc2_ptvv_lift_drift'])}`")
    print(f"- MC2 chain-model drift: `{len(data['mc2_chain_model_drift'])}`")
    print(f"- MC2 seed drift: `{len(data['mc2_seed_drift'])}`")
    print(f"- MC2 seed-packet drift: `{len(data['mc2_seed_packet_drift'])}`")
    print(f"- MC2 visible-lowarity drift: `{len(data['mc2_visible_lowarity_drift'])}`")
    print(f"- MC2 transfer-package drift: `{len(data['mc2_transfer_package_drift'])}`")
    print(f"- MC2 transfer-law drift: `{len(data['mc2_transfer_law_drift'])}`")
    print(f"- MC2 chart drift: `{len(data['mc2_chart_drift'])}`")
    print(f"- MC2 line-detection drift: `{len(data['mc2_line_detection_drift'])}`")
    print(f"- MC2 automorphism-rigidity drift: `{len(data['mc2_automorphism_rigidity_drift'])}`")
    print(f"- MC2 stabilizer drift: `{len(data['mc2_stabilizer_drift'])}`")
    print(f"- MC2 incidence-orbit drift: `{len(data['mc2_incidence_orbit_drift'])}`")
    print(f"- MC2 orbit-table drift: `{len(data['mc2_orbit_table_drift'])}`")
    print(f"- MC2 universal-table drift: `{len(data['mc2_universal_table_drift'])}`")
    print(f"- MC2 invariant-signature drift: `{len(data['mc2_invariant_signature_drift'])}`")
    print(f"- MC2 seed-character drift: `{len(data['mc2_seed_character_drift'])}`")
    print(f"- MC2 two-sign-scalar drift: `{len(data['mc2_twosign_scalar_drift'])}`")
    print(f"- MC2 parity-scalar drift: `{len(data['mc2_parity_scalar_drift'])}`")
    print(f"- MC2 parity-forcing drift: `{len(data['mc2_parity_forcing_drift'])}`")
    print(f"- Non-principal packet drift: `{len(data['nonprincipal_packet_drift'])}`")
    print(f"- E_n axis drift: `{len(data['en_axis_drift'])}`")
    print(f"- Stale frontier-phrase drift: `{len(data['frontier_stale_phrase_drift'])}`")
    print(f"- Physics-dictionary drift: `{len(data['physics_dictionary_drift'])}`")
    print(f"- Active prompt banner drift: `{len(data['active_prompt_banner_drift'])}`")
    print(f"- Archival prompt banner drift: `{len(data['archival_prompt_banner_drift'])}`")
    print(f"- Active state banner drift: `{len(data['active_state_banner_drift'])}`")
    print(f"- Archival state banner drift: `{len(data['archival_state_banner_drift'])}`")
    print(f"- Prompt-pointer drift: `{len(data['prompt_pointer_drift'])}`")
    print(f"- MC3 wording drift: `{len(data['mc3_wording_drift'])}`")
    print(f"- MC4 wording drift: `{len(data['mc4_wording_drift'])}`")
    print(f"- AI-tell candidates: `{len(data['ai_tells'])}`")
    print(f"- Cross-file duplicate paragraphs: `{len(data['duplicates'])}`")
    print(f"- Long paragraphs (>1200 chars): `{len(data['long_paragraphs'])}`")
    print()

    print_section("Structural Findings")
    if data["missing_goq"]:
        for path in data["missing_goq"][:limit]:
            print(f"- missing governing question: `{path}`")
    if data["missing_hms"]:
        for path in data["missing_hms"][:limit]:
            print(f"- missing semantic-level marker: `{path}`")
    if data["untagged"]:
        print_findings(data["untagged"], limit)
    if not data["missing_goq"] and not data["missing_hms"] and not data["untagged"]:
        print("- none")
    print()

    print_section("Prior-Version Leaks")
    if data["prior_version"]:
        print_findings(data["prior_version"], limit)
    else:
        print("- none")
    print()

    print_section("Ambiguous Status Language")
    if data["ambiguous_status"]:
        print_findings(data["ambiguous_status"], limit)
    else:
        print("- none")
    print()

    print_section("Virasoro Shadow-Doctrine Drift")
    if data["virasoro_shadow_drift"]:
        print_findings(data["virasoro_shadow_drift"], limit)
    else:
        print("- none")
    print()

    print_section("Infinite-Generator Frontier Drift")
    if data["infinite_generator_drift"]:
        print_findings(data["infinite_generator_drift"], limit)
    else:
        print("- none")
    print()

    print_section("DK Scope Drift")
    if data["dk_scope_drift"]:
        print_findings(data["dk_scope_drift"], limit)
    else:
        print("- none")
    print()

    print_section("Periodicity-Profile Drift")
    if data["periodicity_profile_drift"]:
        print_findings(data["periodicity_profile_drift"], limit)
    else:
        print("- none")
    print()

    print_section("KL Scope Drift")
    if data["kl_scope_drift"]:
        print_findings(data["kl_scope_drift"], limit)
    else:
        print("- none")
    print()

    print_section("Periodicity Overclaim Drift")
    if data["periodicity_overclaim_drift"]:
        print_findings(data["periodicity_overclaim_drift"], limit)
    else:
        print("- none")
    print()

    print_section("Package-Scope Drift")
    if data["package_scope_drift"]:
        print_findings(data["package_scope_drift"], limit)
    else:
        print("- none")
    print()

    print_section("MC2 Frontier Drift")
    if data["mc2_frontier_drift"]:
        print_findings(data["mc2_frontier_drift"], limit)
    else:
        print("- none")
    print()

    print_section("MC2 Verdier-Plane Drift")
    if data["mc2_verdier_drift"]:
        print_findings(data["mc2_verdier_drift"], limit)
    else:
        print("- none")
    print()

    print_section("MC2 PTVV-Lift Drift")
    if data["mc2_ptvv_lift_drift"]:
        print_findings(data["mc2_ptvv_lift_drift"], limit)
    else:
        print("- none")
    print()

    print_section("MC2 Chain-Model Drift")
    if data["mc2_chain_model_drift"]:
        print_findings(data["mc2_chain_model_drift"], limit)
    else:
        print("- none")
    print()

    print_section("MC2 Seed Drift")
    if data["mc2_seed_drift"]:
        print_findings(data["mc2_seed_drift"], limit)
    else:
        print("- none")
    print()

    print_section("MC2 Seed-Packet Drift")
    if data["mc2_seed_packet_drift"]:
        print_findings(data["mc2_seed_packet_drift"], limit)
    else:
        print("- none")
    print()

    print_section("MC2 Visible-Lowarity Drift")
    if data["mc2_visible_lowarity_drift"]:
        print_findings(data["mc2_visible_lowarity_drift"], limit)
    else:
        print("- none")
    print()

    print_section("MC2 Transfer-Package Drift")
    if data["mc2_transfer_package_drift"]:
        print_findings(data["mc2_transfer_package_drift"], limit)
    else:
        print("- none")
    print()

    print_section("MC2 Transfer-Law Drift")
    if data["mc2_transfer_law_drift"]:
        print_findings(data["mc2_transfer_law_drift"], limit)
    else:
        print("- none")
    print()

    print_section("MC2 Chart Drift")
    if data["mc2_chart_drift"]:
        print_findings(data["mc2_chart_drift"], limit)
    else:
        print("- none")
    print()

    print_section("MC2 Line-Detection Drift")
    if data["mc2_line_detection_drift"]:
        print_findings(data["mc2_line_detection_drift"], limit)
    else:
        print("- none")
    print()

    print_section("MC2 Automorphism-Rigidity Drift")
    if data["mc2_automorphism_rigidity_drift"]:
        print_findings(data["mc2_automorphism_rigidity_drift"], limit)
    else:
        print("- none")
    print()

    print_section("MC2 Stabilizer Drift")
    if data["mc2_stabilizer_drift"]:
        print_findings(data["mc2_stabilizer_drift"], limit)
    else:
        print("- none")
    print()

    print_section("MC2 Incidence-Orbit Drift")
    if data["mc2_incidence_orbit_drift"]:
        print_findings(data["mc2_incidence_orbit_drift"], limit)
    else:
        print("- none")
    print()

    print_section("MC2 Orbit-Table Drift")
    if data["mc2_orbit_table_drift"]:
        print_findings(data["mc2_orbit_table_drift"], limit)
    else:
        print("- none")
    print()

    print_section("MC2 Universal-Table Drift")
    if data["mc2_universal_table_drift"]:
        print_findings(data["mc2_universal_table_drift"], limit)
    else:
        print("- none")
    print()

    print_section("MC2 Invariant-Signature Drift")
    if data["mc2_invariant_signature_drift"]:
        print_findings(data["mc2_invariant_signature_drift"], limit)
    else:
        print("- none")
    print()

    print_section("MC2 Seed-Character Drift")
    if data["mc2_seed_character_drift"]:
        print_findings(data["mc2_seed_character_drift"], limit)
    else:
        print("- none")
    print()

    print_section("MC2 Two-Sign-Scalar Drift")
    if data["mc2_twosign_scalar_drift"]:
        print_findings(data["mc2_twosign_scalar_drift"], limit)
    else:
        print("- none")
    print()

    print_section("MC2 Parity-Scalar Drift")
    if data["mc2_parity_scalar_drift"]:
        print_findings(data["mc2_parity_scalar_drift"], limit)
    else:
        print("- none")
    print()

    print_section("MC2 Parity-Forcing Drift")
    if data["mc2_parity_forcing_drift"]:
        print_findings(data["mc2_parity_forcing_drift"], limit)
    else:
        print("- none")
    print()

    print_section("Non-Principal Packet Drift")
    if data["nonprincipal_packet_drift"]:
        print_findings(data["nonprincipal_packet_drift"], limit)
    else:
        print("- none")
    print()

    print_section("E_n Axis Drift")
    if data["en_axis_drift"]:
        print_findings(data["en_axis_drift"], limit)
    else:
        print("- none")
    print()

    print_section("Stale Frontier-Phrase Drift")
    if data["frontier_stale_phrase_drift"]:
        print_findings(data["frontier_stale_phrase_drift"], limit)
    else:
        print("- none")
    print()

    print_section("Physics-Dictionary Drift")
    if data["physics_dictionary_drift"]:
        print_findings(data["physics_dictionary_drift"], limit)
    else:
        print("- none")
    print()

    print_section("Prompt/State Banner Drift")
    if data["active_prompt_banner_drift"]:
        print_findings(data["active_prompt_banner_drift"], limit)
    if data["archival_prompt_banner_drift"]:
        print_findings(data["archival_prompt_banner_drift"], limit)
    if data["active_state_banner_drift"]:
        print_findings(data["active_state_banner_drift"], limit)
    if data["archival_state_banner_drift"]:
        print_findings(data["archival_state_banner_drift"], limit)
    if (
        not data["active_prompt_banner_drift"]
        and not data["archival_prompt_banner_drift"]
        and not data["active_state_banner_drift"]
        and not data["archival_state_banner_drift"]
    ):
        print("- none")
    print()

    print_section("Prompt-Pointer Drift")
    if data["prompt_pointer_drift"]:
        print_findings(data["prompt_pointer_drift"], limit)
    else:
        print("- none")
    print()

    print_section("MC3/MC4 Wording Drift")
    if data["mc3_wording_drift"]:
        print_findings(data["mc3_wording_drift"], limit)
    if data["mc4_wording_drift"]:
        print_findings(data["mc4_wording_drift"], limit)
    if not data["mc3_wording_drift"] and not data["mc4_wording_drift"]:
        print("- none")
    print()

    print_section("Duplicate Paragraphs")
    if data["duplicates"]:
        for _, paras in data["duplicates"][:limit]:
            print(f"- duplicate x{len(paras)}")
            for para in paras[:4]:
                snippet = para.text[:140].strip()
                print(f"  - `{para.path}:{para.line}` {snippet}")
    else:
        print("- none")
    print()

    print_section("Long Paragraphs")
    if data["long_paragraphs"]:
        print_paragraphs(data["long_paragraphs"], limit)
    else:
        print("- none")
    print()

    print_section("AI-Tell Candidates")
    if data["ai_tells"]:
        print_findings(data["ai_tells"], limit)
    else:
        print("- none")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=12, help="Maximum findings per section.")
    parser.add_argument(
        "--strict",
        action="store_true",
        help=(
            "Exit nonzero on doctrinal regressions, theorem-status drift, "
            "or prior-version leakage; chapter-opening GOQ/HMS backlog "
            "remains report-only until the repo-wide entry-point pass lands."
        ),
    )
    args = parser.parse_args()

    data = scan()
    report(data, args.limit)

    if args.strict and (
        data["untagged"]
        or data["prior_version"]
        or data["ambiguous_status"]
        or data["virasoro_shadow_drift"]
        or data["infinite_generator_drift"]
        or data["dk_scope_drift"]
        or data["periodicity_profile_drift"]
        or data["kl_scope_drift"]
        or data["periodicity_overclaim_drift"]
        or data["package_scope_drift"]
        or data["mc2_frontier_drift"]
        or data["mc2_verdier_drift"]
        or data["mc2_ptvv_lift_drift"]
        or data["mc2_chain_model_drift"]
        or data["mc2_seed_drift"]
        or data["mc2_seed_packet_drift"]
        or data["mc2_visible_lowarity_drift"]
        or data["mc2_transfer_package_drift"]
        or data["mc2_transfer_law_drift"]
        or data["mc2_chart_drift"]
        or data["mc2_line_detection_drift"]
        or data["mc2_automorphism_rigidity_drift"]
        or data["mc2_stabilizer_drift"]
        or data["mc2_incidence_orbit_drift"]
        or data["mc2_orbit_table_drift"]
        or data["mc2_universal_table_drift"]
        or data["mc2_invariant_signature_drift"]
        or data["mc2_seed_character_drift"]
        or data["mc2_twosign_scalar_drift"]
        or data["mc2_parity_scalar_drift"]
        or data["mc2_parity_forcing_drift"]
        or data["nonprincipal_packet_drift"]
        or data["en_axis_drift"]
        or data["frontier_stale_phrase_drift"]
        or data["physics_dictionary_drift"]
        or data["active_prompt_banner_drift"]
        or data["archival_prompt_banner_drift"]
        or data["active_state_banner_drift"]
        or data["archival_state_banner_drift"]
        or data["prompt_pointer_drift"]
        or data["mc3_wording_drift"]
        or data["mc4_wording_drift"]
    ):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
