"""Beilinson Auditor: automated upstream-first proof-chain integrity engine.

Implements the Beilinson Principle computationally:
  "What limits forward progress is not the lack of genius
   but the inability to dismiss false ideas."

Operates at three levels of the epistemic hierarchy:
  Level 2 — .tex source: parses proof blocks to extract ACTUAL dependencies
  Level 3 — Build metadata: uses label_index, claims.jsonl, verified_formulas
  Level 4 — Literature: audits external citation dependencies

Builds DUAL dependency DAGs:
  Statement DAG — refs within theorem/lemma/proposition environments
  Proof DAG    — refs within \\begin{proof}...\\end{proof} blocks

Detects anti-patterns:
  AP4  — Status inflation (ProvedHere depending on Conjectured)
  AP5  — Cross-file propagation risk (high fan-out labels)
  AP6  — Missing scope qualifiers (genus/arity/level on key claims)
  AP11 — Single external dependency (proved via one preprint)
  AP13 — Genuine circular dependencies (proof-level, not forward refs)

Usage:
    auditor = BeilinsonAuditor('/path/to/repo')
    report = auditor.run_audit()
    print(auditor.format_report(report))
"""

import json
import re
from collections import defaultdict, deque
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Set, Tuple

# Status strength ordering (higher = stronger epistemic claim)
STATUS_STRENGTH = {
    'Open': 0,
    'Heuristic': 1,
    'Conjectured': 2,
    'Conditional': 3,
    'ProvedElsewhere': 4,
    'ProvedHere': 5,
}

STATUS_NAME = {v: k for k, v in STATUS_STRENGTH.items()}

SEVERITY_ORDER = {'CRITICAL': 0, 'SERIOUS': 1, 'WARNING': 2, 'INFO': 3}

# Environments that contain mathematical claims
CLAIM_ENVS = {
    'theorem', 'lemma', 'proposition', 'corollary', 'conjecture',
    'computation', 'calculation', 'maintheorem', 'verification', 'remark',
}

# Regex for extracting \ref-family commands
REF_RE = re.compile(r'\\(?:ref|eqref|Cref|cref)\{([^}]+)\}')

# Editorial markers preceding a \ref indicate non-logical citation
# These refs are contextual, not proof dependencies
EDITORIAL_RE = re.compile(
    r'(?:cf\.?|compare|see\s+also|alternative|recall\s+from|recall\s+that|'
    r'verified\s+(?:explicitly|in|for)|verifies|is\s+consistent\s+with|'
    r'is\s+compatible\s+with|creating\s+a\s+cross.reference|'
    r'independently\s+summarized|summarized\s+in|as\s+in|analogous\s+to|'
    r'converse\s+of|similar\s+to|motivation\s+is|physics.dictionary|'
    r'see\s+§|see\s+\\S|but\s+the\s+mathematical|not\s+a\s+circular)'
    r'.{0,30}?'
    r'(?:Theorem|Proposition|Lemma|Corollary|Conjecture|Remark|'
    r'condition|clause|\\Cref|\\ref|\\eqref)',
    re.IGNORECASE | re.DOTALL
)

# Key terms that require scope qualification (AP6)
# Only flag property claims ("X is Koszul"), not operation names
# ("Koszul dual of X", "under Koszul duality")
SCOPE_TERMS = [
    (r'[Dd]\^2\s*=\s*0|\\partial\^2\s*=\s*0|d-squared.zero', 'D^2=0'),
    (r'(?<![Kk]oszul\s)\\kappa(?!\s*duality)|curvature.invariant', 'kappa'),
    # Only match "Koszul" as a property claim, not as an operation name
    (r'(?:is|are)\s+(?:chiral\s+)?[Kk]oszul|[Kk]oszulness\b|[Kk]oszulity\b', 'Koszulness'),
    (r'\\Theta_?\{?A\}?|shadow.tower|shadow.Postnikov', 'Theta_A'),
]

# Scope qualifiers that should appear near key terms
SCOPE_QUALIFIERS = re.compile(
    r'genus|arity|level|convolution|ambient|cobar|'
    r'g\s*[=≥>]\s*\d|g\s*\\geq|all\s+genera|'
    r'type\s+[A-G]|all\s+types|simple\s+Lie'
)


@dataclass
class Claim:
    """A tagged mathematical claim in the manuscript."""
    label: str
    env_type: str
    status: str
    file: str
    line: int
    title: str = ''
    refs_in_block: list = field(default_factory=list)
    cites_in_block: list = field(default_factory=list)
    labels_in_block: list = field(default_factory=list)

    @property
    def strength(self) -> int:
        return STATUS_STRENGTH.get(self.status, -1)


@dataclass
class Finding:
    """A single audit finding."""
    severity: str       # CRITICAL, SERIOUS, WARNING, INFO
    anti_pattern: str   # AP4, AP5, AP6, AP11, AP13, BOTTLENECK, TRANSITIVE
    claim_label: str
    message: str
    file: str = ''
    line: int = 0
    upstream_label: str = ''


@dataclass
class AuditReport:
    """Complete audit output."""
    total_claims: int
    statement_edges: int
    proof_edges: int
    proof_claims_found: int
    root_count: int
    layer_count: int
    findings: List[Finding]
    layers: Dict[int, List[str]]
    bottlenecks: List[Tuple[str, int]]
    genuine_cycles: List[List[str]]
    forward_ref_cycles: List[List[str]]
    test_coverage: Dict[str, List[str]]
    uncovered_proved: List[str]
    status_by_layer: Dict[int, Dict[str, int]]
    effective_strength: Dict[str, int]
    weakest_links: Dict[str, str]


class BeilinsonAuditor:
    """Automated upstream-first proof-chain integrity engine.

    Operates on the full epistemic hierarchy: parses .tex source for
    proof-level dependencies, builds dual DAGs, classifies reference
    cycles, and detects anti-patterns AP4/AP5/AP6/AP11/AP13.
    """

    def __init__(self, repo_root: str):
        self.repo_root = Path(repo_root)
        self.claims: Dict[str, Claim] = {}

        # Statement-level DAG (from claims.jsonl refs_in_block)
        self.stmt_adj: Dict[str, Set[str]] = defaultdict(set)
        self.stmt_rev: Dict[str, Set[str]] = defaultdict(set)

        # Proof-level DAG (from .tex proof block parsing)
        self.proof_adj: Dict[str, Set[str]] = defaultdict(set)
        self.proof_rev: Dict[str, Set[str]] = defaultdict(set)
        self.proof_deps: Dict[str, Set[str]] = {}
        self.editorial_refs: Dict[str, Set[str]] = {}  # refs preceded by editorial markers

        # Combined DAG (union)
        self.adjacency: Dict[str, Set[str]] = defaultdict(set)
        self.reverse_adj: Dict[str, Set[str]] = defaultdict(set)

        self.secondary_to_primary: Dict[str, str] = {}
        self.layers: Dict[int, List[str]] = {}
        self.claim_to_layer: Dict[str, int] = {}

        # Label cross-file data (for AP5)
        self.label_files: Dict[str, Set[str]] = defaultdict(set)

    # ==================================================================
    # PHASE 1: Data Collection (Epistemic Levels 2-4)
    # ==================================================================

    def load_claims(self) -> int:
        """Load claims from metadata/claims.jsonl. Returns count loaded."""
        claims_path = self.repo_root / 'metadata' / 'claims.jsonl'
        if not claims_path.exists():
            raise FileNotFoundError(
                f"claims.jsonl not found at {claims_path}. "
                "Run 'python3 scripts/generate_metadata.py' first."
            )

        count = 0
        with open(claims_path) as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                data = json.loads(line)
                label = data.get('label', '')
                if not label:
                    continue

                claim = Claim(
                    label=label,
                    env_type=data.get('env_type', ''),
                    status=data.get('status', ''),
                    file=data.get('file', ''),
                    line=data.get('line', 0),
                    title=data.get('title', ''),
                    refs_in_block=data.get('refs_in_block', []),
                    cites_in_block=data.get('cites_in_block', []),
                    labels_in_block=data.get('labels_in_block', []),
                )
                self.claims[label] = claim
                count += 1

                for sec in claim.labels_in_block:
                    if sec != label:
                        # Exclude equation labels (eq:*) from secondary mapping.
                        # Equations are definitional notation — referencing
                        # \eqref{eq:foo} inside a conjecture is using the
                        # formula, not asserting the conjecture.
                        if not sec.startswith('eq:'):
                            self.secondary_to_primary[sec] = label

        return count

    def build_statement_dag(self):
        """Build statement-level DAG from refs_in_block."""
        self.stmt_adj.clear()
        self.stmt_rev.clear()

        for label, claim in self.claims.items():
            for ref in claim.refs_in_block:
                target = self.secondary_to_primary.get(ref, ref)
                if target in self.claims and target != label:
                    self.stmt_adj[label].add(target)
                    self.stmt_rev[target].add(label)

    def extract_proof_deps(self) -> int:
        """Parse .tex files to extract refs from proof blocks. Returns count found.

        For each claim, locates the proof environment that follows it and
        extracts all \\ref{} citations. These are the ACTUAL logical
        dependencies — what the proof uses, not what the statement mentions.
        """
        self.proof_deps.clear()
        self.proof_adj.clear()
        self.proof_rev.clear()

        # Group claims by file for efficient I/O
        claims_by_file: Dict[str, List[Claim]] = defaultdict(list)
        for claim in self.claims.values():
            if claim.file:
                claims_by_file[claim.file].append(claim)

        found_count = 0

        for filepath, file_claims in claims_by_file.items():
            full_path = self.repo_root / filepath
            if not full_path.exists():
                continue

            try:
                lines = full_path.read_text(errors='replace').split('\n')
            except Exception:
                continue

            # Sort claims by line number (ascending)
            file_claims.sort(key=lambda c: c.line)

            for claim in file_claims:
                proof_refs = self._find_proof_refs(
                    lines, claim.line - 1, claim.env_type, claim.label
                )
                if proof_refs is not None:
                    self.proof_deps[claim.label] = proof_refs
                    found_count += 1

                    for target in proof_refs:
                        self.proof_adj[claim.label].add(target)
                        self.proof_rev[target].add(claim.label)

        return found_count

    def _find_proof_refs(
        self, lines: List[str], start_idx: int, env_type: str, claim_label: str
    ) -> Set[str]:
        """Find refs in the proof block following a claim environment.

        Returns set of resolved claim labels, or None if no proof found.
        """
        n = len(lines)

        # Find end of the claim environment
        end_tag = f'\\end{{{env_type}}}'
        env_end = None
        for i in range(start_idx, min(start_idx + 300, n)):
            if end_tag in lines[i]:
                env_end = i
                break

        if env_end is None:
            return None

        # Scan forward for \begin{proof} (allow up to 20 lines gap)
        proof_start = None
        for i in range(env_end + 1, min(env_end + 20, n)):
            line = lines[i]
            if '\\begin{proof}' in line:
                proof_start = i
                break
            # Stop if we hit another claim environment before finding a proof
            if any(f'\\begin{{{et}}}' in line for et in CLAIM_ENVS):
                break

        if proof_start is None:
            return None

        # Find \end{proof} (handles single-line and nested proofs)
        proof_end = None
        depth = 0
        for i in range(proof_start, min(proof_start + 1000, n)):
            line = lines[i]
            if '\\begin{proof}' in line:
                depth += 1
            if '\\end{proof}' in line:
                depth -= 1
                if depth == 0:
                    proof_end = i
                    break

        if proof_end is None:
            return None

        # Extract refs from proof text, classifying as logical vs editorial
        proof_text = '\n'.join(lines[proof_start:proof_end + 1])

        # --- Phase A: Detect editorial ref positions via marker patterns ---
        editorial_positions = set()
        for em in EDITORIAL_RE.finditer(proof_text):
            search_start = em.end() - 30
            for rm in REF_RE.finditer(proof_text[max(0, search_start):em.end() + 80]):
                editorial_positions.add(
                    search_start + rm.start() if search_start >= 0 else rm.start()
                )

        # --- Phase B: Detect "alternative/supplementary" paragraphs ---
        # Refs in paragraphs marked "Alternative route/proof" are supplementary,
        # not part of the main deductive chain.
        alt_para_re = re.compile(
            r'\\emph\{(?:Alternative|Second|Supplementary)\s+'
            r'(?:route|proof|argument|approach)'
            r'|\\emph\{Verification\b',
            re.IGNORECASE
        )
        # Also detect "assuming Conjecture/Theorem" — explicit conditional steps
        assuming_re = re.compile(
            r'(?:assuming|conditional\s+on)\s+.{0,30}?'
            r'\\(?:ref|Cref)\{([^}]+)\}',
            re.IGNORECASE
        )

        # Find refs in alternative paragraphs
        alt_editorial_targets = set()
        paragraphs = proof_text.split('\n\n')
        for para in paragraphs:
            if alt_para_re.search(para):
                for rm in REF_RE.finditer(para):
                    ref = rm.group(1).strip()
                    target = self.secondary_to_primary.get(ref, ref)
                    if target in self.claims and target != claim_label:
                        alt_editorial_targets.add(target)

        # Find refs preceded by "assuming" — these are conditional, not logical
        for am in assuming_re.finditer(proof_text):
            ref = am.group(1).strip()
            target = self.secondary_to_primary.get(ref, ref)
            if target in self.claims and target != claim_label:
                alt_editorial_targets.add(target)

        # --- Phase C: Classify all refs ---
        refs = set()
        editorial = set()
        for match in REF_RE.finditer(proof_text):
            ref = match.group(1).strip()
            target = self.secondary_to_primary.get(ref, ref)
            if target in self.claims and target != claim_label:
                is_editorial = (
                    target in alt_editorial_targets or
                    any(abs(match.start() - ep) < 80 for ep in editorial_positions)
                )
                if is_editorial:
                    editorial.add(target)
                else:
                    refs.add(target)

        if editorial:
            self.editorial_refs[claim_label] = editorial

        return refs

    def build_combined_dag(self):
        """Build the combined DAG (union of statement + proof deps)."""
        self.adjacency.clear()
        self.reverse_adj.clear()

        for label in self.claims:
            combined = (
                self.stmt_adj.get(label, set()) |
                self.proof_adj.get(label, set())
            )
            if combined:
                self.adjacency[label] = combined
                for target in combined:
                    self.reverse_adj[target].add(label)

    def load_label_index(self):
        """Load label_index.json for cross-file analysis (AP5)."""
        idx_path = self.repo_root / 'metadata' / 'label_index.json'
        if not idx_path.exists():
            return

        try:
            with open(idx_path) as f:
                label_data = json.load(f)
        except Exception:
            return

        # For each label, track which file defines it
        for label, info in label_data.items():
            if isinstance(info, dict) and 'file' in info:
                self.label_files[label].add(info['file'])

        # Also track which files REFERENCE each claim label
        claims_by_file: Dict[str, List[Claim]] = defaultdict(list)
        for claim in self.claims.values():
            if claim.file:
                for ref in claim.refs_in_block:
                    target = self.secondary_to_primary.get(ref, ref)
                    self.label_files[target].add(claim.file)

    # ==================================================================
    # PHASE 2: Structural Analysis
    # ==================================================================

    def topological_sort(self) -> Tuple[List[str], List[List[str]]]:
        """Kahn's algorithm on combined DAG. Returns (sorted, cycles)."""
        self.layers.clear()
        self.claim_to_layer.clear()

        in_degree = {}
        for label in self.claims:
            in_degree[label] = len(self.adjacency.get(label, set()))

        queue = deque()
        for label, deg in in_degree.items():
            if deg == 0:
                queue.append(label)

        sorted_nodes = []
        layer_idx = 0

        while queue:
            layer_size = len(queue)
            layer_nodes = []
            for _ in range(layer_size):
                node = queue.popleft()
                layer_nodes.append(node)
                self.claim_to_layer[node] = layer_idx
                sorted_nodes.append(node)

            self.layers[layer_idx] = layer_nodes

            next_queue = []
            for node in layer_nodes:
                for downstream in self.reverse_adj.get(node, set()):
                    in_degree[downstream] -= 1
                    if in_degree[downstream] == 0:
                        next_queue.append(downstream)

            for n in next_queue:
                queue.append(n)
            layer_idx += 1

        remaining = set(self.claims.keys()) - set(sorted_nodes)
        cycles = self._extract_cycles(remaining) if remaining else []

        if remaining:
            cycle_layer = layer_idx
            cycle_nodes = sorted(remaining)
            self.layers[cycle_layer] = cycle_nodes
            for label in cycle_nodes:
                self.claim_to_layer[label] = cycle_layer
                sorted_nodes.append(label)

        return sorted_nodes, cycles

    def _extract_cycles(self, nodes: Set[str]) -> List[List[str]]:
        """Extract cycle representatives from nodes not in topological order."""
        visited = set()
        cycles = []

        for start in sorted(nodes):
            if start in visited:
                continue

            path = [start]
            path_set = {start}
            current = start

            while True:
                next_nodes = self.adjacency.get(current, set()) & nodes
                back_targets = next_nodes & path_set
                if back_targets:
                    target = next(iter(back_targets))
                    idx = path.index(target)
                    cycles.append(path[idx:])
                    break

                candidates = next_nodes - path_set - visited
                if not candidates:
                    break

                nxt = next(iter(candidates))
                path.append(nxt)
                path_set.add(nxt)
                current = nxt

            visited.update(path_set)

        return cycles

    def classify_cycles(
        self, cycles: List[List[str]]
    ) -> Tuple[List[List[str]], List[List[str]]]:
        """Classify cycles as genuine (proof-level) or forward-ref/editorial.

        A cycle is GENUINE if BOTH directions have logical proof-level deps.
        A cycle is EDITORIAL if at least one direction is only an editorial
        ref (cf., see also, etc.) or exists only in the statement DAG.
        """
        genuine = []
        forward_ref = []

        for cycle in cycles:
            # Count how many edges have logical (non-editorial) proof deps
            logical_edge_count = 0
            for i in range(len(cycle)):
                a = cycle[i]
                b = cycle[(i + 1) % len(cycle)]
                # a->b: does proof of a logically depend on b?
                if b in self.proof_adj.get(a, set()):
                    # Check it's not editorial
                    if b not in self.editorial_refs.get(a, set()):
                        logical_edge_count += 1

            # A cycle is genuine only if ALL edges are logical proof deps
            # (both directions for 2-cycles, all edges for n-cycles)
            if logical_edge_count >= len(cycle):
                genuine.append(cycle)
            else:
                forward_ref.append(cycle)

        return genuine, forward_ref

    def _compute_strength_on_dag(
        self, sorted_nodes: List[str], adj: Dict[str, Set[str]]
    ) -> Tuple[Dict[str, int], Dict[str, str]]:
        """Compute effective strength via DP on a given DAG.

        effective_strength(C) = min(C.strength, min(eff(U) for U in adj[C]))
        Conditional claims floor at Conditional level.
        Returns (eff_map, weakest_link_map).
        """
        eff = {}
        weakest = {}

        for label in sorted_nodes:
            claim = self.claims[label]
            own_strength = claim.strength
            min_strength = own_strength
            min_source = ''

            for upstream_label in adj.get(label, set()):
                if upstream_label not in eff:
                    continue

                up_eff = eff[upstream_label]
                up_claim = self.claims.get(upstream_label)

                if up_claim and up_claim.status == 'Conditional':
                    effective_up = max(up_eff, STATUS_STRENGTH['Conditional'])
                else:
                    effective_up = up_eff

                if effective_up < min_strength:
                    min_strength = effective_up
                    if effective_up < self.claims[upstream_label].strength:
                        min_source = weakest.get(upstream_label, upstream_label)
                    else:
                        min_source = upstream_label

            eff[label] = min_strength
            if min_strength < own_strength:
                weakest[label] = min_source

        return eff, weakest

    def compute_effective_strength(
        self, sorted_nodes: List[str]
    ) -> Tuple[Dict[str, int], Dict[str, str]]:
        """Compute effective strength on the combined DAG."""
        return self._compute_strength_on_dag(sorted_nodes, self.adjacency)

    def compute_proof_effective_strength(
        self, sorted_nodes: List[str]
    ) -> Tuple[Dict[str, int], Dict[str, str]]:
        """Compute effective strength on the proof-only DAG.

        Used for severity classification: degradation through statement-only
        refs is INFO, not SERIOUS.
        """
        return self._compute_strength_on_dag(sorted_nodes, self.proof_adj)

    # ==================================================================
    # PHASE 3: Anti-Pattern Detection
    # ==================================================================

    def check_ap4_proof_level(self) -> List[Finding]:
        """AP4: Status inflation using PROOF-LEVEL dependencies.

        This is the real check: what does the proof actually use?
        A ProvedHere theorem whose proof cites a Conjectured claim
        is the ground-truth AP4 violation.
        """
        findings = []

        for label, proof_refs in self.proof_deps.items():
            claim = self.claims.get(label)
            if not claim:
                continue

            for upstream_label in proof_refs:
                upstream = self.claims.get(upstream_label)
                if not upstream:
                    continue

                if upstream.strength < claim.strength:
                    if (claim.status == 'ProvedHere' and
                            upstream.status in ('Conjectured', 'Heuristic', 'Open')):
                        severity = 'CRITICAL'
                    elif claim.status == 'ProvedHere' and upstream.status == 'Conditional':
                        severity = 'WARNING'
                    else:
                        severity = 'INFO'

                    findings.append(Finding(
                        severity=severity,
                        anti_pattern='AP4',
                        claim_label=label,
                        message=(
                            f'{claim.status} [{claim.env_type}] proof cites '
                            f'{upstream.status} upstream {upstream_label}'
                        ),
                        file=claim.file,
                        line=claim.line,
                        upstream_label=upstream_label,
                    ))

        return findings

    def check_ap4_statement_level(self) -> List[Finding]:
        """AP4 on statement DAG (weaker signal — includes forward refs)."""
        findings = []

        for label, claim in self.claims.items():
            # Only check statement refs NOT already in proof deps
            stmt_only = self.stmt_adj.get(label, set()) - self.proof_deps.get(label, set())

            for upstream_label in stmt_only:
                upstream = self.claims.get(upstream_label)
                if not upstream:
                    continue

                if upstream.strength < claim.strength:
                    if (claim.status == 'ProvedHere' and
                            upstream.status in ('Conjectured', 'Heuristic', 'Open')):
                        severity = 'WARNING'  # Downgraded: might be forward ref
                    else:
                        severity = 'INFO'

                    findings.append(Finding(
                        severity=severity,
                        anti_pattern='AP4-STMT',
                        claim_label=label,
                        message=(
                            f'{claim.status} [{claim.env_type}] statement refs '
                            f'{upstream.status} {upstream_label} (may be forward ref)'
                        ),
                        file=claim.file,
                        line=claim.line,
                        upstream_label=upstream_label,
                    ))

        return findings

    def check_ap5_propagation_risk(self, threshold: int = 8) -> List[Finding]:
        """AP5: Cross-file propagation risk.

        Identifies claims referenced from many files — changing these
        requires checking all referencing files (the #1 systematic failure
        mode, historically requiring 3-4 commits per correction).
        """
        findings = []

        for label in self.claims:
            files = self.label_files.get(label, set())
            if len(files) >= threshold:
                claim = self.claims[label]
                findings.append(Finding(
                    severity='WARNING',
                    anti_pattern='AP5',
                    claim_label=label,
                    message=(
                        f'Referenced from {len(files)} files — '
                        f'any correction requires checking all'
                    ),
                    file=claim.file,
                    line=claim.line,
                ))

        return findings

    def check_ap6_scope_qualifiers(self) -> List[Finding]:
        """AP6: Missing boundary qualifications on key claims.

        Checks whether claims about D^2=0, kappa, Koszulness, Theta_A,
        complementarity specify genus, arity, and/or level.
        """
        findings = []

        for label, claim in self.claims.items():
            if claim.status not in ('ProvedHere', 'ProvedElsewhere'):
                continue

            title = claim.title or ''
            if not title:
                continue

            for pattern, term in SCOPE_TERMS:
                if re.search(pattern, title, re.IGNORECASE):
                    # Check if any scope qualifier appears in the title
                    if not SCOPE_QUALIFIERS.search(title):
                        findings.append(Finding(
                            severity='INFO',
                            anti_pattern='AP6',
                            claim_label=label,
                            message=(
                                f'Claim about {term} without explicit scope '
                                f'qualifier (genus/arity/level/type): "{title}"'
                            ),
                            file=claim.file,
                            line=claim.line,
                        ))
                    break  # Only flag once per claim

        return findings

    def check_ap11_external_deps(self) -> List[Finding]:
        """AP11: Single external dependency.

        Flags ProvedHere claims whose proof cites exactly one external paper
        and has few internal theorem dependencies — the proof rests on
        a single external source.
        """
        findings = []

        for label, claim in self.claims.items():
            if claim.status != 'ProvedHere':
                continue

            cites = claim.cites_in_block
            if not cites or len(cites) != 1:
                continue

            # Check if this claim has few internal deps relative to the single cite
            internal_deps = len(
                self.proof_deps.get(label, set()) |
                self.stmt_adj.get(label, set())
            )
            if internal_deps <= 2:
                cite_key = cites[0]
                findings.append(Finding(
                    severity='WARNING',
                    anti_pattern='AP11',
                    claim_label=label,
                    message=(
                        f'ProvedHere with single external citation [{cite_key}] '
                        f'and only {internal_deps} internal deps'
                    ),
                    file=claim.file,
                    line=claim.line,
                ))

        return findings

    def check_transitive_degradation(
        self,
        eff_strength: Dict[str, int],
        weakest_links: Dict[str, str],
        proof_eff_strength: Dict[str, int] = None,
    ) -> List[Finding]:
        """TRANSITIVE: Claims whose full upstream chain degrades their status.

        Uses proof-only effective strength for severity: if degradation
        flows only through statement refs (not proof deps), it's INFO.
        """
        findings = []

        for label, eff in eff_strength.items():
            claim = self.claims[label]
            if eff >= claim.strength or label not in weakest_links:
                continue

            weak_label = weakest_links[label]
            weak_claim = self.claims.get(weak_label)
            weak_status = weak_claim.status if weak_claim else '?'
            eff_name = STATUS_NAME.get(eff, '?')

            # Determine severity using proof-only strength:
            # SERIOUS only if the degradation path goes through PROOF deps.
            # Statement-only degradation = INFO (editorial/forward refs).
            if claim.status in ('ProvedHere', 'ProvedElsewhere') and eff <= 2:
                weak_is_remark = (
                    weak_claim and weak_claim.env_type == 'remark'
                )
                # Check proof-only strength: is the claim degraded at proof level?
                proof_eff = (proof_eff_strength or {}).get(label, claim.strength)
                degraded_at_proof_level = (proof_eff <= 2)

                if weak_is_remark or not degraded_at_proof_level:
                    severity = 'INFO'
                else:
                    severity = 'SERIOUS'
            else:
                severity = 'INFO'

            findings.append(Finding(
                severity=severity,
                anti_pattern='TRANSITIVE',
                claim_label=label,
                message=(
                    f'{claim.status} has effective strength {eff_name} '
                    f'(weakest link: {weak_label} [{weak_status}])'
                ),
                file=claim.file,
                line=claim.line,
                upstream_label=weak_label,
            ))

        return findings

    def find_bottlenecks(self, threshold: int = 5) -> List[Tuple[str, int]]:
        """Identify nodes with >= threshold downstream dependents."""
        bottlenecks = []
        for label in self.claims:
            count = len(self.reverse_adj.get(label, set()))
            if count >= threshold:
                bottlenecks.append((label, count))
        bottlenecks.sort(key=lambda x: -x[1])
        return bottlenecks

    def scan_test_coverage(self) -> Dict[str, List[str]]:
        """Map claim labels to compute/tests files that reference them."""
        coverage: Dict[str, List[str]] = defaultdict(list)
        test_dir = self.repo_root / 'compute' / 'tests'
        if not test_dir.exists():
            return dict(coverage)

        claim_labels = set(self.claims.keys())
        label_re = re.compile(
            r'(?:thm|prop|lem|cor|def|conj|rem|comp|calc|eq|sec)'
            r':[\w][\w\-:]*'
        )

        for test_file in sorted(test_dir.glob('test_*.py')):
            try:
                content = test_file.read_text(errors='replace')
            except Exception:
                continue

            found = set(label_re.findall(content))
            for match in found:
                if match in claim_labels:
                    coverage[match].append(test_file.name)

        return dict(coverage)

    def status_by_layer(self) -> Dict[int, Dict[str, int]]:
        """Compute status distribution for each DAG layer."""
        result = {}
        for layer_idx, nodes in self.layers.items():
            dist: Dict[str, int] = defaultdict(int)
            for label in nodes:
                claim = self.claims.get(label)
                if claim:
                    dist[claim.status] += 1
            result[layer_idx] = dict(dist)
        return result

    # ==================================================================
    # PHASE 4: Full Audit Pipeline
    # ==================================================================

    def run_audit(self) -> AuditReport:
        """Execute the complete Beilinson audit."""
        # --- Data collection ---
        self.load_claims()
        self.build_statement_dag()
        proof_count = self.extract_proof_deps()
        self.build_combined_dag()
        self.load_label_index()

        # --- Structural analysis ---
        sorted_nodes, raw_cycles = self.topological_sort()
        genuine_cycles, forward_ref_cycles = self.classify_cycles(raw_cycles)
        eff_strength, weakest_links = self.compute_effective_strength(sorted_nodes)
        proof_eff, _ = self.compute_proof_effective_strength(sorted_nodes)

        # --- Anti-pattern detection ---
        findings: List[Finding] = []

        # AP4 proof-level (the REAL check)
        findings.extend(self.check_ap4_proof_level())

        # AP4 statement-level (weaker signal, may include forward refs)
        findings.extend(self.check_ap4_statement_level())

        # AP13 genuine cycles (proof-level confirmed)
        for cycle in genuine_cycles:
            cycle_str = ' -> '.join(cycle) + ' -> ' + cycle[0]
            findings.append(Finding(
                severity='CRITICAL',
                anti_pattern='AP13',
                claim_label=cycle[0],
                message=f'Genuine proof-level cycle: {cycle_str}',
                file=self.claims[cycle[0]].file if cycle[0] in self.claims else '',
            ))

        # AP13 forward-ref cycles (downgraded to INFO)
        for cycle in forward_ref_cycles:
            cycle_str = ' -> '.join(cycle) + ' -> ' + cycle[0]
            findings.append(Finding(
                severity='INFO',
                anti_pattern='AP13-FWD',
                claim_label=cycle[0],
                message=f'Forward-reference cycle (not logical): {cycle_str}',
                file=self.claims[cycle[0]].file if cycle[0] in self.claims else '',
            ))

        # AP5 propagation risk
        findings.extend(self.check_ap5_propagation_risk())

        # AP6 scope qualifiers
        findings.extend(self.check_ap6_scope_qualifiers())

        # AP11 external deps
        findings.extend(self.check_ap11_external_deps())

        # Transitive degradation (proof-only strength for severity)
        findings.extend(self.check_transitive_degradation(
            eff_strength, weakest_links, proof_eff
        ))

        # Test coverage
        test_coverage = self.scan_test_coverage()

        # Bottlenecks
        bottlenecks = self.find_bottlenecks()

        # Uncovered bottlenecks
        for label, count in bottlenecks:
            if label not in test_coverage:
                findings.append(Finding(
                    severity='SERIOUS',
                    anti_pattern='BOTTLENECK',
                    claim_label=label,
                    message=f'Bottleneck ({count} downstream deps) with no compute test',
                    file=self.claims[label].file,
                    line=self.claims[label].line,
                ))

        # Uncovered ProvedHere
        uncovered_proved = sorted([
            label for label, claim in self.claims.items()
            if claim.status == 'ProvedHere' and label not in test_coverage
        ])

        sbl = self.status_by_layer()
        stmt_edges = sum(len(deps) for deps in self.stmt_adj.values())
        proof_edges = sum(len(deps) for deps in self.proof_adj.values())

        findings.sort(key=lambda f: SEVERITY_ORDER.get(f.severity, 99))

        return AuditReport(
            total_claims=len(self.claims),
            statement_edges=stmt_edges,
            proof_edges=proof_edges,
            proof_claims_found=proof_count,
            root_count=len(self.layers.get(0, [])),
            layer_count=len(self.layers),
            findings=findings,
            layers=self.layers,
            bottlenecks=bottlenecks,
            genuine_cycles=genuine_cycles,
            forward_ref_cycles=forward_ref_cycles,
            test_coverage=test_coverage,
            uncovered_proved=uncovered_proved,
            status_by_layer=sbl,
            effective_strength=eff_strength,
            weakest_links=weakest_links,
        )

    # ==================================================================
    # PHASE 5: Report Formatting
    # ==================================================================

    def format_report(self, report: AuditReport) -> str:
        """Format audit report."""
        lines = []
        sep = '=' * 72

        lines.append(sep)
        lines.append('BEILINSON AUDIT — Proof-Chain Integrity Report')
        lines.append(sep)
        lines.append('')

        # Dual DAG summary
        editorial_count = sum(len(s) for s in self.editorial_refs.values())
        lines.append('## Dual DAG Summary')
        lines.append(f'  Claims:              {report.total_claims}')
        lines.append(f'  Statement edges:     {report.statement_edges}')
        lines.append(f'  Proof edges:         {report.proof_edges}')
        lines.append(f'  Editorial refs:      {editorial_count} (detected, excluded from proof DAG)')
        lines.append(f'  Proofs extracted:    {report.proof_claims_found}')
        lines.append(f'  Root nodes:          {report.root_count}')
        lines.append(f'  DAG layers:          {report.layer_count}')
        lines.append(f'  Genuine cycles:      {len(report.genuine_cycles)}')
        lines.append(f'  Forward-ref cycles:  {len(report.forward_ref_cycles)}')
        lines.append('')

        # Test coverage
        covered = len(report.test_coverage)
        proved_count = sum(
            1 for c in self.claims.values() if c.status == 'ProvedHere'
        )
        lines.append('## Test Coverage')
        lines.append(f'  Claims with compute tests:   {covered}')
        lines.append(f'  ProvedHere total:            {proved_count}')
        lines.append(f'  ProvedHere without tests:    {len(report.uncovered_proved)}')
        pct = covered / max(report.total_claims, 1) * 100
        lines.append(f'  Overall coverage:            {pct:.1f}%')
        lines.append('')

        # Transitive strength
        degraded = sum(
            1 for label, eff in report.effective_strength.items()
            if eff < self.claims[label].strength
        )
        lines.append('## Transitive Strength (proof-aware)')
        lines.append(f'  Full upstream support:       '
                      f'{len(report.effective_strength) - degraded}')
        lines.append(f'  Degraded eff. strength:      {degraded}')
        lines.append('')

        # Findings summary
        by_sev: Dict[str, List[Finding]] = defaultdict(list)
        by_ap: Dict[str, List[Finding]] = defaultdict(list)
        for f in report.findings:
            by_sev[f.severity].append(f)
            by_ap[f.anti_pattern].append(f)

        lines.append('## Findings Summary')
        for sev in ['CRITICAL', 'SERIOUS', 'WARNING', 'INFO']:
            lines.append(f'  {sev:8s}: {len(by_sev[sev])}')
        lines.append('')

        lines.append('  By anti-pattern:')
        for ap in sorted(by_ap.keys()):
            lines.append(f'    {ap:12s}: {len(by_ap[ap])}')
        lines.append('')

        # Detail: CRITICAL and SERIOUS
        for sev in ['CRITICAL', 'SERIOUS']:
            items = by_sev[sev]
            if not items:
                continue
            lines.append(f'### {sev}')
            for f in items:
                loc = f'{f.file}:{f.line}' if f.file else ''
                lines.append(f'  [{f.anti_pattern}] {f.claim_label}')
                lines.append(f'    {f.message}')
                if loc:
                    lines.append(f'    at {loc}')
                lines.append('')

        # WARNING summary (compact)
        warnings = by_sev['WARNING']
        if warnings:
            lines.append(f'### WARNING ({len(warnings)} items)')
            ap_counts: Dict[str, int] = defaultdict(int)
            for f in warnings:
                ap_counts[f.anti_pattern] += 1
            for ap, count in sorted(ap_counts.items()):
                lines.append(f'  {ap}: {count}')
            # Show first 10 AP4-STMT warnings
            ap4_stmt = [f for f in warnings if f.anti_pattern == 'AP4-STMT']
            if ap4_stmt:
                lines.append('')
                lines.append('  AP4-STMT details (first 10):')
                for f in ap4_stmt[:10]:
                    lines.append(f'    {f.claim_label}: {f.message}')
            lines.append('')

        # Bottlenecks (top 20)
        if report.bottlenecks:
            lines.append('## Bottleneck Nodes (top 20)')
            for label, count in report.bottlenecks[:20]:
                claim = self.claims.get(label)
                status = claim.status if claim else '?'
                tested = 'tested' if label in report.test_coverage else 'UNTESTED'
                eff = report.effective_strength.get(label, -1)
                eff_name = STATUS_NAME.get(eff, '?')
                flag = ''
                if claim and eff < claim.strength:
                    flag = f' (eff: {eff_name})'
                lines.append(
                    f'  {count:3d} deps  [{status:16s}]  {tested:8s}  '
                    f'{label}{flag}'
                )
            lines.append('')

        # Status by layer (first 20)
        lines.append('## Status by DAG Layer')
        for layer_idx in sorted(report.status_by_layer.keys())[:20]:
            dist = report.status_by_layer[layer_idx]
            total = sum(dist.values())
            parts = ', '.join(
                f'{s}:{c}' for s, c in
                sorted(dist.items(), key=lambda x: -STATUS_STRENGTH.get(x[0], -1))
            )
            lines.append(f'  Layer {layer_idx:2d} ({total:4d}): {parts}')
        remaining_layers = len(report.status_by_layer) - 20
        if remaining_layers > 0:
            lines.append(f'  ... ({remaining_layers} more layers)')
        lines.append('')

        lines.append(sep)
        return '\n'.join(lines)


# ==================================================================
# CLI entry point
# ==================================================================

def main():
    """Run Beilinson audit from command line."""
    import sys
    repo_root = sys.argv[1] if len(sys.argv) > 1 else '.'
    auditor = BeilinsonAuditor(repo_root)
    report = auditor.run_audit()
    print(auditor.format_report(report))

    critical = [f for f in report.findings if f.severity == 'CRITICAL']
    sys.exit(1 if critical else 0)


if __name__ == '__main__':
    main()
