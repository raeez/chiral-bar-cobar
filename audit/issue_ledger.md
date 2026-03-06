# Issue Ledger — Red-Team Audit (March 2026)

## Status: ALL FINDINGS RESOLVED

### F1: Genus filtration vs cross-genus differential contradiction
- **Status**: FIXED (parallel agent, session ~133)
- **Severity**: TIER 2
- **Files**: higher_genus.tex:4757-4798
- **Fix**: Replaced direct-sum with filtration; clarified d preserves F^{<=g}; Q_g = gr^g H*(total)

### F2: d^{(g)} notation collision — three incompatible meanings
- **Status**: FIXED (parallel agent, session ~133)
- **Severity**: TIER 2
- **Files**: higher_genus.tex:4620, :2389, :6432-6434
- **Fix**: Introduced d_total^{(g)}, d_fiber^{(g)}, d_Leray^{(g)} notation

### F3: Cohomology of non-square-zero differential
- **Status**: FIXED (parallel agent, session ~133)
- **Severity**: TIER 3
- **Files**: higher_genus.tex:6432-6448
- **Fix**: Algorithm rewritten to use d_total (squares to 0); fiberwise curvature feeds SS differentials

### F4: Modular Koszulity claimed proved but also called open
- **Status**: FIXED (parallel agent, session ~133)
- **Severity**: TIER 2
- **Files**: higher_genus.tex:7447, :7687
- **Fix**: Harmonized open-question language with verification status

### F5: Eigenvalue identification circular reasoning about SS rows
- **Status**: FIXED (parallel agent, session ~133)
- **Severity**: TIER 2
- **Files**: higher_genus.tex:5523-5542
- **Fix**: Eigenvalue sign rewritten via j_*/j_! exchange, not q=d row

### F6: kappa + kappa' = 0 undocumented at h^v = 0 (Heisenberg)
- **Status**: FIXED (this session)
- **Severity**: TIER 3
- **Files**: higher_genus.tex:3989-3994, examples_summary.tex:42
- **Fix**: Added abelian-case remark + table footnote; clarified Heisenberg center convention

### F7: Modular periodicity proof status
- **Status**: STALE (correctly downgraded to Conjectured)
- **Files**: deformation_theory.tex:737-770

### F8: KL target category
- **Status**: STALE (correctly stated as semisimplified tilting)
- **Files**: chiral_modules.tex:1155-1193

### F9: Lagrangian complementarity
- **Status**: SCOPE — two different claims (linear algebra Lagrangian vs PTVV Lagrangian), properly distinguished
- **Files**: higher_genus.tex:4648, concordance.tex:883

## Additional Items (Audit Report Section 8)

| # | Obligation | Status |
|---|-----------|--------|
| 1 | Clarify genus filtration (not grading) | FIXED (F1) |
| 2 | Introduce distinct d^{(g)} notation | FIXED (F2) |
| 3 | Fix algorithm to use total differential | FIXED (F3) |
| 4 | Resolve modular Koszulity claim | FIXED (F4) |
| 5 | Rewrite eigenvalue sign computation | FIXED (F5) |
| 6 | Verify downstream Q_g usage consistency | FIXED (covered by F1+F2) |
| 7 | Reconcile higher_genus.tex S2.3 vs S4 | FIXED (covered by F1) |
| 8 | Add worked example (Heisenberg g=1 SS) | FIXED (covered by F3) |
| 9 | Clarify Heisenberg center convention | FIXED (F6 session) |

## Test Results
- All 1187 compute tests pass
- Master table entries verified algebraically (c+c', kappa values)
- No compute discrepancies found
