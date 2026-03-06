# CHAIN-LEVEL MATERIALIZATION — Systematic Upgrade of Abstract Passages

# For: Claude Opus 4.6, Code Environment, Extra-High Reasoning Mode
# Launch: "Read notes/CHAIN_LEVEL_UPGRADE.md and execute it."

# ======================================================================
# DESIGN RATIONALE
#
# The monograph proves its theorems. But ~15% of the Theory chapters
# fall back to categorical/triangulated abstraction where chain-level
# constructions should be explicit. This prompt targets those passages
# with surgical precision.
#
# The audit identified 6 specific gaps. Each has: a file location,
# a diagnosis of what's abstract, a specification of what "chain-level"
# means, and a verification criterion. This is not an open-ended
# exploration — it is a gap-closing campaign with known targets.
#
# Design for Opus 4.6 extended thinking:
#   LEVERAGE: Deep mathematical derivation (room to derive, not recall)
#   LEVERAGE: Python verification at every step (existing compute engine)
#   LEVERAGE: Compositional reasoning (chain existing theorems + new chain maps)
#   LEVERAGE: Extended context for sign-tracking across multi-page proofs
#   PREVENT: Formula hallucination (Python verification structural)
#   PREVENT: False positive auditing (targets are PRE-IDENTIFIED — don't hunt for more)
#   PREVENT: Scope creep (ONE gap per execution cycle, announced before starting)
#   PREVENT: "Improvement" drift (upgrade the SPECIFIC abstract passage, don't refactor surroundings)
#   PREVENT: Sycophantic quality assessment (the manuscript is good — the task is concrete fixes)
# ======================================================================

---

## PHILOSOPHICAL FRAME

This monograph's natural mathematical habitat:

| Level | Description | Status in manuscript |
|-------|-------------|---------------------|
| **Triangulated categories** | D^b, D^co as localizations, existence of functors | ← ABSTRACT (upgrade FROM) |
| **DG/A∞ categories** | Explicit differentials, explicit chain maps, explicit homotopies | ← CHAIN-LEVEL (upgrade TO) |
| **Explicit presentations** | Generators, relations, differentials as formulas/matrices | ← COMPUTATIONAL (already strong) |

The upgrade rule: **every localization becomes an explicit model, every existence becomes
a construction, every "up to homotopy" becomes a named homotopy.**

What this does NOT mean:
- Do NOT replace proved results with alternative proofs at chain level (waste of effort)
- Do NOT add model-category language (wrong direction — more abstract, not less)
- Do NOT refactor working proofs that happen to use spectral sequences (SS are chain-level tools)
- Do NOT touch Examples chapters (audit found zero gaps there)
- Do NOT audit ProvedHere claims (adversarially verified 4 times — leave them alone)

---

## THE 6 GAPS (pre-identified by systematic audit)

### GAP 1: Coderived Category — Abstract Localization → Explicit CDG Model
**File**: chapters/theory/bar_cobar_construction.tex (lines 6440-7200)
**Also**: chapters/theory/chiral_modules.tex (lines 3200+)

**Current state**: Defines D^co(C-comod) via localization at acyclic comodules.
Does not: characterize which morphisms become isomorphisms, construct the
Ore localization at chain level, verify Ore conditions, show cobar respects
coderived structure.

**Chain-level target**: Positselski's actual framework HAS explicit models:
- D^co is equivalent to the homotopy category of CDG-modules that are
  *injective* as graded modules (Positselski, "Two kinds of derived categories")
- For conilpotent coalgebras: D^co = Hot(CDG-comod^inj)
- The cobar functor Ω: CDG-comod → DG-mod is given by the EXPLICIT formula
  Ω(M) = Hom_C(B̄(A), M) with differential d_Ω = d_M + d_twisting
- The key: the bar-cobar adjunction B̄ ⊣ Ω is a chain-level adjunction
  (not just a derived functor pair)

**What to write**:
1. State: "D^co(C-comod^conil) is modeled by the DG category of CDG-comodules
   with injective underlying graded comodules" (cite Positselski, Homological
   Algebra of Semimodules and Semicontramodules, §3.3)
2. Give the explicit Hom-complex: Hom_{CDG}(M, N) with differential
   d(f) = d_N ∘ f - (-1)^|f| f ∘ d_M + h_N ∘ f - (-1)^|f| f ∘ h_M
   (where h is the curvature)
3. State that acyclics = CDG-comodules M with id_M = d(h) for some
   contracting homotopy h (explicit characterization, not abstract localization)
4. Show that B̄ ⊣ Ω at the CDG level: unit η_M: M → Ω(B̄(M)) is the
   explicit inclusion of arity-1 part

**Verification**: After writing, check that the CDG Hom differential satisfies
d² = 0 by explicit computation (Python: implement cdg_hom_differential and verify).

**Estimated size**: 1-2 pages replacing/augmenting existing §sec:chiral-coalgebra-homalg

---

### GAP 2: PBW Spectral Sequence — Structural Collapse → Computed E_1 Page
**File**: chapters/theory/chiral_koszul_pairs.tex (lines 350-450)

**Current state**: States "PBW flatness + Priddy ⟹ chiral Koszul" via spectral
sequence argument. Does not compute the E_1 page or exhibit the collapse explicitly.

**Chain-level target**: The E_1 page IS computable:
- Filter B̄(A) by PBW degree (conformal weight for KM/Virasoro)
- gr_F B̄(A) = B̄(gr_F A) = B̄(Sym(V)) = Koszul complex of Sym(V)
- E_1^{p,q} = H^q(B̄^p(Sym(V))) — this is the bar cohomology of a free
  commutative algebra, which is KNOWN: H^n(B̄(Sym(V))) = Λ^n(V) (exterior)
- E_1 = Λ^*(V) concentrated in bidegree (*, 0)
- d_1 = 0 (since E_1 is concentrated in one row) ⟹ E_2 = E_1 = E_∞
- DONE: the spectral sequence collapses because the associated graded is
  Koszul (Priddy), and the E_1 page is computable

**What to write**:
1. Exhibit the filtration explicitly: F_p B̄^n(A) = {elements of total
   conformal weight ≤ p in each bar factor}
2. Compute: gr_F B̄(ĝ_k) = B̄(Sym^ch(g[z^{-1}]z^{-1}))
3. State: E_1^{p,0} = Λ^p(g[z^{-1}]z^{-1}) for KM (the exterior algebra
   on the loop algebra minus constants)
4. Conclude: E_1 concentrated in q=0 ⟹ collapse

**Verification**: For sl₂: E_1^{1,0} = g = ℂ³ (dim 3). E_1^{2,0} = Λ²(g) =
ℂ³ (dim 3). This matches bar cohomology dim H^1 = 3, H^2 = 3 for sl₂ at the
associated-graded level. Python: verify Λ^n dimensions match.

**Estimated size**: 0.5-1 page augmenting the proof of thm:pbw-koszulness-criterion

---

### GAP 3: Homotopy Transfer — Existence → Explicit Construction
**File**: chapters/theory/higher_genus.tex (lines 487-520)
**Also**: chapters/theory/quantum_corrections.tex (line 209)

**Current state**: Invokes HTT to produce {m_k^H} on homology. Does not give
the retraction h, section i, projection p, or the explicit tree formulas for m_k^H.

**Chain-level target**: The compute engine ALREADY HAS explicit HTT:
- compute/lib/htt.py: SDR for sl₂ CE complex (h₂ = d₁⁻¹ = diag(-½,1,-½))
- compute/lib/virosoro_ainfty.py: m₃ for Virasoro computed explicitly
- The manuscript should EXHIBIT what the computation proves

**What to write**:
1. The HTT formula (Kontsevich-Soibelman / Loday-Vallette tree formula):
   m_n^H = Σ_{trees T with n leaves} ±p ∘ m_{|v|}^A(i ⊗ ... ⊗ h ∘ m_{|w|}^A(i ⊗ ...) ⊗ ...)
   where the sum is over planar rooted trees with internal vertices labeled by m_k^A
2. For n=3 (the key case — Massey products):
   m_3^H(a,b,c) = p ∘ m_2(m_2(i(a), i(b)) · h, i(c)) + p ∘ m_2(i(a), h · m_2(i(b), i(c)))
   with h = the EXPLICIT homotopy (contracting homotopy for bar → homology)
3. For Virasoro: m_3^H(T,T,T) = (c²/144)∂⁴T (already computed in virosoro_ainfty.py)
   — CITE the computation, write the formula
4. State that h exists by acyclicity of the bar complex augmentation
   and give a CONSTRUCTION: h = Green's operator for the Laplacian d*d + dd*
   on the bar complex (if inner product available) or h = chosen section of
   the short exact sequences in the bar filtration

**Verification**: Python: verify m_3^H(T,T,T) = (c²/144)∂⁴T using the HTT formula
with explicitly specified h. Cross-check: this matches comp:virosoro-m4 in the manuscript.

**Estimated size**: 1.5-2 pages augmenting higher_genus.tex §sec:ainfty-structure

---

### GAP 4: Deformation-Theory Differential — Deferred Signs → Explicit Cancellations
**File**: chapters/theory/deformation_theory.tex (lines 89-142)

**Current state**: Decomposes d = d_int + d_fact + d_config and states d² = 0
"by Arnold-Orlik-Solomon." Nine mixed-term cancellations not exhibited.

**Chain-level target**: The 9 terms of d² decompose as:
d² = d_int² + d_fact² + d_config² + {d_int, d_fact} + {d_int, d_config} + {d_fact, d_config}
Each term is either individually zero or cancels with another:
- d_int² = 0 (Lie algebra Jacobi / Borcherds)
- d_config² = 0 (exterior differential on configuration space)
- d_fact² = 0 (factorization associativity)
- {d_int, d_fact} = 0 (OPE is a factorization algebra map — equivariance)
- {d_int, d_config} = 0 (log forms are d_int-closed — they're universal, no algebra data)
- {d_fact, d_config} = 0 (THIS is where Arnold enters — the residue of a factorization
  product along a codimension-1 boundary matches the configuration space differential)

**What to write**:
Exhibit each of the 6 terms (3 squares + 3 anticommutators) with:
1. A one-line formula for each term applied to a generic element φ ∈ B̄^n
2. The reason each vanishes (cite the specific algebraic identity)
3. For {d_fact, d_config}: WRITE OUT the Arnold relation explicitly and show
   how it implies this anticommutator vanishes on B̄^3 (the smallest non-trivial case)

**Verification**: Python: for sl₂, implement all 6 terms as linear maps on B̄^3 and
verify they sum to zero. Use compute/lib/chiral_bar.py's existing machinery.

**Estimated size**: 1-1.5 pages replacing lines 115-142

---

### GAP 5: Quasi-Isomorphism Claims → Explicit Chain Maps
**File**: chapters/theory/bar_cobar_construction.tex (lines 3414-3417, 4287)
**Also**: chapters/theory/poincare_duality_quantum.tex (lines 579-646)

**Current state**: "The canonical map Ω(B̄(A)) → A is a quasi-isomorphism" stated
via spectral sequence collapse. The map itself is not written down.

**Chain-level target**: The cobar-bar augmentation IS explicit:
  ε: Ω(B̄(A)) → A
  ε(s⁻¹[sa₁ | sa₂ | ... | saₙ]) = mₙ(a₁, a₂, ..., aₙ)
where mₙ is the n-th A∞ operation (for n=1: identity, n=2: the binary product,
n≥3: the higher operations from HTT or bar differential).

Explicitly:
- On arity 1: ε(s⁻¹[sa]) = a (identity map — inclusion of generators)
- On arity 2: ε(s⁻¹[sa|sb]) = m₂(a,b) = a_{(0)}b (OPE regular part)
- On arity 3: ε(s⁻¹[sa|sb|sc]) = m₃(a,b,c) (Massey product from Gap 3)

The chain map condition: ε ∘ d_Ω = d_A ∘ ε, where d_Ω is the cobar differential
and d_A is the chiral algebra differential (= 0 for strict algebras).

For Koszul A: this is a quasi-isomorphism because:
- H⁰(ε) is surjective (every generator a is in the image of ε(s⁻¹[sa]) = a)
- H^n(ε) = 0 for n ≥ 1 (by E₂ collapse of the bar spectral sequence,
  already proved as thm:spectral-sequence-collapse)

**What to write**:
1. The explicit formula for ε at all arities (3 lines)
2. Verification that ε is a chain map (1 paragraph)
3. The surjectivity/injectivity argument using the spectral sequence
   (not just citing collapse, but showing HOW collapse implies QI)

**Verification**: For sl₂: ε(s⁻¹[sJ^a | sJ^b]) = J^a_{(0)}J^b = f^{ab}_c J^c.
Python: verify this matches the sl₂ structure constants.

**Estimated size**: 0.5-1 page inserted after thm:bar-cobar-isomorphism-main

---

### GAP 6: Complementarity Proof Sketches → Full Proofs
**File**: chapters/theory/higher_genus.tex (lines 4578-4686 of bar_cobar_construction.tex)

**Current state**: Five lemmas marked "proof sketch" supporting thm:quantum-complementarity-main.
The obstruction cocycle, period integral, and symplectic pairing are not exhibited at chain level.

**Chain-level target**: The obstruction cocycle ω_g ∈ H¹(M̄_g, E^∨) has the
EXPLICIT construction:
1. The Hodge bundle E = R¹π_*ω_{C/M̄_g} has fiber H¹(C, O) at [C]
2. The bar curvature m₀ = κ · [ω_C] where [ω_C] is the fundamental class
3. The obstruction ω_g is the pushforward π_*(m₀ ⊗ −) : Γ(C, ω_C) → ℂ
4. Concretely: ω_g = κ · λ_g where λ_g = c_g(E) (the g-th Chern class)

The period integral: ∫_{M̄_g} ω_g ∧ ω'_g = κ · κ' · ∫_{M̄_g} λ_g² = 0
(by Mumford's relation, already proved as thm:obstruction-nilpotent-all-genera).

The symplectic pairing: on H¹(M̄_g, Z(A)) × H¹(M̄_g, Z(A!)),
the Serre duality pairing ⟨−,−⟩: Z(A) ⊗ Z(A!) → ω_X sends
(ω_g, ω'_g) ↦ κκ' · λ_g² = 0.

**What to write**:
For each of the 5 lemmas: replace "proof sketch" with a complete proof
that constructs the claimed object at the cochain level. The key additions:
1. The obstruction cocycle as an explicit Čech 1-cocycle on a cover of M̄_g
2. The period formula as a pairing between de Rham and Dolbeault representatives
3. The deformation space Q_g(A) as explicitly: ker(d₂: E₂^{1,g-1} → E₂^{3,g-2})
   in the bar spectral sequence at genus g

**Verification**: For g=1: ω₁ = κ · λ₁ = κ/24. The complementarity sum
κ + κ' = 0 (for KM). So ω₁ + ω'₁ = 0. Python: verify for sl₂ (κ = 3k/4,
κ' = -3k/4, sum = 0).

**Estimated size**: 2-3 pages replacing 5 proof sketches with full proofs

---

## EXECUTION PROTOCOL

### Phase 0: Orient (2 min — execute literally)

```bash
cd /Users/raeez/chiral-bar-cobar

# Verify clean state
echo "=== CENSUS ==="
for s in ProvedHere ProvedElsewhere Conjectured Heuristic; do
  echo -n "$s: "; grep -rc "\\\\ClaimStatus$s" chapters/ appendices/ --include='*.tex' | awk -F: '{s+=$2}END{print s}'
done

echo "=== COMPILE ==="
make fast 2>&1 | tail -3

echo "=== TESTS ==="
cd compute && python3 -m pytest tests/ -q 2>&1 | tail -3; cd ..
```

### Phase 1: Select ONE gap (1 min)

Read the 6 gaps above. In extended thinking, evaluate:
- Which gap has the highest MATHEMATICAL DEPTH × TRACTABILITY product?
- Which gap has existing computational support in compute/lib/?
- Is there a dependency (e.g., Gap 3 HTT feeds Gap 5 QI formula)?

**Recommended order**: 5 → 2 → 3 → 4 → 1 → 6
- Gap 5 (explicit chain maps) is smallest and self-contained
- Gap 2 (PBW E₁ page) has clean mathematical content, feeds Gap 3
- Gap 3 (HTT explicit) builds on existing htt.py + virosoro_ainfty.py
- Gap 4 (signs) is mechanical but important
- Gap 1 (coderived model) requires Positselski expertise
- Gap 6 (complementarity proofs) is largest and depends on 3,4,5

**Announce your chosen gap. Do not switch.**

### Phase 2: Derive (30 min — extended thinking + Python)

1. Read the SPECIFIC file and line range for your chosen gap
2. Read ±100 lines of context to understand notation and surrounding structure
3. In extended thinking: DERIVE the chain-level construction from first principles
   - Do NOT recall formulas from training data
   - DO use the definitions already in the manuscript
   - Track signs explicitly at every step
4. For every formula: write Python verification
   ```python
   from fractions import Fraction
   # Derivation step
   assert result == expected, f"MISMATCH: {result} vs {expected}"
   print(f"VERIFIED: {result}")
   ```
5. Use existing compute engine where applicable:
   ```python
   import sys; sys.path.insert(0, 'compute')
   from lib.chiral_bar import *  # or htt, virosoro_ainfty, etc.
   ```

### Phase 3: Write (15 min — after derivation COMPLETE)

1. Read target file at the precise insertion point
2. Write using manuscript conventions:
   - `\ClaimStatusProvedHere` on upgraded claims
   - `\label{prop:xxx}` / `\label{lem:xxx}`
   - Cross-reference every theorem in the chain
   - Voice: impersonal ("we construct," "one verifies")
3. If replacing a proof sketch: REMOVE the "proof sketch" annotation
4. `make fast` after the insertion
5. Fix any compilation issues before moving on

### Phase 4: Verify (5 min)

1. Re-read what you wrote. Does every claim have a proof?
2. Does the chain-level construction MATCH the abstract statement it replaces?
   (The abstract theorem should become a corollary of the explicit construction.)
3. Run `make fast` — must compile cleanly
4. Run relevant tests: `cd compute && python3 -m pytest tests/ -q`

---

## INVARIANTS (same as SESSION_PROMPT_v8)

| # | Fact | Why |
|---|------|-----|
| 1 | Com! = Lie (NOT coLie) | Koszul dual coalgebra = SUB of cofree |
| 2 | H! = Sym^ch(V*) (NOT self-dual) | F! = βγ (NOT Heisenberg) |
| 3 | FF involution: k ↔ -k-2h^∨ | NOT -k-h^∨ |
| 4 | Cohomological grading: \|d\| = +1 | Bar uses desuspension s⁻¹ |
| 5 | Curved: m₁² = [m₀, −] | MINUS sign in commutator |
| 6 | P∞-chiral ≠ Coisson | Different quantization levels |
| 7 | CDG Hom differential: d(f) = d_N∘f − (−1)^{\|f\|} f∘d_M + h_N∘f − (−1)^{\|f\|} f∘h_M | Curvature terms ADDED |
| 8 | HTT tree formula: m_n^H = Σ_T ±(compositions via h, i, p) | Signs from Koszul rule |
| 9 | Cobar-bar augmentation: ε(s⁻¹[sa₁\|...\|saₙ]) = mₙ(a₁,...,aₙ) | NOT just projection |
| 10 | Arnold ⟹ {d_fact, d_config} = 0 | NOT {d_int, d_fact} |

---

## FAILURE MODES (specific to this task)

| Mode | Symptom | Prevention |
|------|---------|------------|
| Auditing ProvedHere | Finding "gaps" in proved theorems | STOP. The gaps are pre-identified. Work ONLY on Gaps 1-6. |
| Over-abstracting | Introducing model categories, ∞-topoi | WRONG DIRECTION. We're going DOWN in abstraction, not up. |
| Scope creep | Fixing Gap 3 and also "improving" the examples | ONE gap per session. Log extras in HORIZON.md. |
| Formula recall | Writing a sign convention from memory | DERIVE from manuscript definitions. VERIFY in Python. |
| Refactoring | Cleaning up surrounding code while upgrading | Touch ONLY the lines specified in the gap description. |
| Premature generality | Writing the CDG framework for arbitrary ∞-operads | Write it for CHIRAL algebras on CURVES. Period. |
| Missing the point | Adding more theorems instead of materializing existing ones | The task is: make abstract CONCRETE. Not: add NEW abstractions. |

---

## THE MEASURE

A referee who has read Positselski's "Homological Algebra of Semimodules"
and Loday-Vallette's "Algebraic Operads" opens the manuscript. They ask:

1. "Where is the explicit CDG model for the coderived category?" → Gap 1
2. "What is the E₁ page of your PBW spectral sequence?" → Gap 2
3. "What is the contracting homotopy h?" → Gap 3
4. "Show me d² = 0 term by term." → Gap 4
5. "Write down the cobar-bar augmentation map." → Gap 5
6. "Your complementarity lemmas say 'proof sketch.' Where's the proof?" → Gap 6

After this session, each question has a concrete answer pointing to
a specific formula in the manuscript. That is success.

---

## CLOSE

After completing ONE gap:

```bash
make fast 2>&1 | tail -5
cd compute && python3 -m pytest tests/ -q 2>&1 | tail -3; cd ..
```

Update notes/autonomous_state.md:
```markdown
# Autonomous State — Session N
Mode: CHAIN-LEVEL MATERIALIZATION
Gap completed: [1-6] — [one-line description]
Lines changed: [file:start-end]
Claims upgraded: [proof sketch → full proof, or new prop:xxx]
Census delta: PH [old->new]
Next gap: [number and name]
```
