# STRIKE LISTS — CATALOGUE ITEMS TO MANUSCRIPT FILES

Each catalogue item maps to specific files that need rewriting.
Intensity: H = heavy rewrite, M = moderate integration, L = light touch.

---

## CLUSTER A: THE OPEN-SECTOR REORIENTATION
Items: RL-1, RL-2, RL-3, RL-4, RL-5, RL-6, RL-7, RL-10, RL-11, RL-17

This is the single most pervasive change. It touches every file that
discusses "the chiral algebra A" as a primitive, because after the rewrite
A is a presentation of C_op, not the primitive itself.

| File | Vol | Intensity | What changes |
|------|-----|-----------|-------------|
| chapters/frame/preface.tex | I | H | New subsection: "The open sector" after Heisenberg atom. Bar coalgebra coproduct IS the open color. Center theorem explains bulk. |
| chapters/theory/introduction.tex | I | H | Reframe entire intro: Arnold -> bar -> open sector -> center -> modularity. Currently missing center theorem. |
| chapters/theory/chiral_hochschild_koszul.tex | I | H | Currently closed-sector only. Add brace algebra, center theorem, open-sector perspective. New subsection on Deligne-Tamarkin. |
| chapters/theory/higher_genus_modular_koszul.tex | I | M | Add subsection: modular completion via open-sector traces. Connect shadow obstruction tower to categorical trace. |
| chapters/theory/e1_modular_koszul.tex | I | M | Connect E_1 modular to ribbon/'t Hooft bridge and open-sector cyclic traces. |
| chapters/connections/holomorphic_topological.tex | I | M | Ground "why 2d+1" in center theorem, not bar ordering. |
| chapters/connections/concordance.tex | I | M | Add section on open-sector architecture, center theorem, Morita invariance. |
| introduction.tex | II | H | Rewrite around open-sector-primary perspective. |
| preface.tex | II | H | Open sector is primitive; bulk is center; modularity is trace+clutching. |
| foundations.tex | II | M | Connect correspondence geometry to center theorem. |
| ht_bulk_boundary_line_core.tex | II | H | Promote from "HT-specific" to universal center theorem. |
| hochschild.tex | II | M | Connect to chiral Deligne-Tamarkin explicitly. |
| brace.tex | II | M | State and prove brace theorem as standalone result. |

**Total: 13 files. 5 heavy, 6 moderate, 2 light.**

---

## CLUSTER B: A_INFTY-CHIRAL ALGEBRA DEFINITION
Items: RL-6, V2-1, V2-2, V2-3

| File | Vol | Intensity | What changes |
|------|-----|-----------|-------------|
| chapters/theory/algebraic_foundations.tex | I | M | Add forward reference to A_infty-chiral definition. Currently only classical quadratic. |
| chapters/theory/introduction.tex | I | M | State A_infty-chiral definition early. |
| axioms.tex | II | L | Already correct; ensure Vol I convention consistency. |
| equivalence.tex | II | L | Already correct. |

**Total: 4 files. 0 heavy, 2 moderate, 2 light.**

---

## CLUSTER C: MIXED CONFIG SPACES + LOG-FM ON BORDERED CURVES
Items: RL-2, RL-3, RL-4, V1-29, V1-33

| File | Vol | Intensity | What changes |
|------|-----|-----------|-------------|
| chapters/theory/configuration_spaces.tex | I | H | Add tangential log curves, real-oriented blowup, mixed config spaces, bordered FM compactification. Currently only classical FM on smooth curves. |
| chapters/theory/higher_genus_foundations.tex | I | M | Connect log-FM geometry to modular cooperad on bordered curves. Add depth filtration. |
| appendices/combinatorial_frontier.tex | I | M | Extend stable graph enumeration to bordered case. |
| fm_calculus.tex | II | M | Connect FM calculus to bordered/mixed case. |

**Total: 4 files. 1 heavy, 3 moderate.**

---

## CLUSTER D: BAR VS CENTER DISTINCTION
Items: RL-14, V1-32

| File | Vol | Intensity | What changes |
|------|-----|-----------|-------------|
| chapters/theory/bar_construction.tex | I | L | Add remark: bar represents twisting morphisms, not bulk. |
| chapters/theory/chiral_hochschild_koszul.tex | I | M | (Already in Cluster A.) Sharpen: cochains IS bulk; bar IS coupling space. |
| chapters/connections/bv_brst.tex | I | L | Qualify: BV = bar at genus 0; BV != center at higher genus. |
| bar-cobar-review.tex | II | M | Add clean separation. |

**Total: 4 files. 0 heavy, 2 moderate, 2 light.**

---

## CLUSTER E: MODULAR COMPLETION VIA TRACES
Items: RL-15, RL-16, RL-17, RL-18, RL-19, V2-24

| File | Vol | Intensity | What changes |
|------|-----|-----------|-------------|
| chapters/theory/higher_genus_modular_koszul.tex | I | M | New subsection: cyclic trace -> annulus = HH -> modular MC with clutching. |
| chapters/theory/e1_modular_koszul.tex | I | M | Connect ribbon modular operad to cyclic open-sector traces. |
| appendices/nonlinear_modular_shadows.tex | I | L | Cross-reference trace perspective. |
| chapters/connections/concordance.tex | I | L | Add modular-completion-from-traces to constitution. |
| modular_pva_quantization_core.tex | II | M | Connect PVA quantization to trace/clutching framework. |

**Total: 5 files. 0 heavy, 3 moderate, 2 light.**

---

## CLUSTER F: THE STAIRCASE OF EXAMPLES
Items: RL-23, RL-24, RL-26, RL-27, RL-28

| File | Vol | Intensity | What changes |
|------|-----|-----------|-------------|
| chapters/examples/free_fields.tex | I | M | Add: center = free polyvectors. |
| chapters/examples/heisenberg_eisenstein.tex | I | M | Add: Laplace kernel, abelian CS, complementarity. |
| chapters/examples/beta_gamma.tex | I | M | Add: first m_3, degree counting, contact archetype. |
| chapters/examples/kac_moody.tex | I | M | Add: nonabelian 3d action, exact complementarity. |
| chapters/examples/w_algebras.tex | I | M | Add: composite nonlinearity, RL-27. |
| chapters/examples/w3_composite_fields.tex | I | L | Cross-reference brace/center perspective. |
| Vol II examples (6 new chapters) | II | H | NEW: explicit center computations, 3d actions, Jacobi coalgebras. |

**Total: 13 files. 6 heavy (new), 5 moderate, 2 light.**

---

## CLUSTER G: EDITORIAL + STATUS HYGIENE
Items: V1-1 through V1-5, V1-19

| File | Vol | Intensity | What changes |
|------|-----|-----------|-------------|
| chapters/frame/preface.tex | I | M | (Cluster A.) Finalize editorial pass. |
| chapters/theory/introduction.tex | I | M | (Cluster A.) Propagate scope narrowings. |
| chapters/connections/concordance.tex | I | M | (Clusters A, E.) Meta-theorem count alignment. |
| All 98 modified files | I | L | Punctuation standardization; verify propagation. |
| metadata/theorem_registry.md | I | L | Regenerate after rewrites. |
| metadata/claims.jsonl | I | L | Regenerate. |
| metadata/label_index.json | I | L | Regenerate. |

**Total: ~100 files, mostly light.**

---

## AGGREGATE STATISTICS

| Cluster | Files | Heavy | Moderate | Light |
|---------|-------|-------|----------|-------|
| A (open sector) | 13 | 5 | 6 | 2 |
| B (A_infty defn) | 4 | 0 | 2 | 2 |
| C (mixed config) | 4 | 1 | 3 | 0 |
| D (bar vs center) | 4 | 0 | 2 | 2 |
| E (modular traces) | 5 | 0 | 3 | 2 |
| F (staircase) | 13 | 6 | 5 | 2 |
| G (editorial) | ~100 | 0 | 3 | ~97 |
| **TOTAL (unique)** | **~120** | **~10** | **~18** | **~92** |

Unique files requiring heavy rewrite: ~10
Unique files requiring moderate edit: ~18
Unique files requiring only light touch: ~92
New files to create: ~8 (Vol I open sector chapter + staircase chapter;
  Vol II tangential log curves + Jacobi coalgebra + modular traces + 6 examples)
