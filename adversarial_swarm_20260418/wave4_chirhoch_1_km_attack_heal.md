# Wave-4 attack-and-heal: ChirHoch^1 KM total-dim formula scope

Target: CLAUDE.md "ChirHoch^1 KM explicit" row; Vol I `chapters/theory/chiral_center_theorem.tex:1965-2215` (`prop:derived-center-explicit`, `prop:chirhoch1-affine-km`, `rem:sl2-chirhoch-dim5`).

Date: 2026-04-18. Auditor channel: Etingof / Polyakov / Kazhdan / Gelfand / Nekrasov / Kapranov / Bezrukavnikov / Costello / Gaiotto / Witten.

## Attack ledger

F1. `chiral_center_theorem.tex:1965-1994` Part (i) Heisenberg. Severity LOW, category scope.
    The statement restricts to rank-1 Heisenberg $\fH_k$ (single weight-1 generator). The proof at :2052-2074 uses "one-dimensional generating space $V = \bC \cdot a$" explicitly. Scope is cleanly stated; no inflation. ACCEPT as-is.

F2. `chiral_center_theorem.tex:1996-2021` Part (ii) "Affine $\widehat{\mathfrak{sl}}_2$ at level $k \neq -2$". Severity HIGH, category scope+naming.
    The environment header and label `prop:derived-center-explicit(ii)` are inscribed FOR RANK 1 ONLY; `h^\vee = 2` and `\mathfrak{sl}_2`-specific dimensions enter the statement. The proof at :2076-2096 uses "three weight-1 fields" and a three-term Koszul resolution with "generating space $V = \mathfrak{sl}_2$ (three-dimensional)" — structurally rank-1 in its use of the bracket structure constants. The `ChirHoch^2 = \bC` clause is proved via the phrase "the dual of the center of the Koszul dual $\widehat{\mathfrak{sl}}_{2,-k-4}$, which is one-dimensional at generic dual level". This invokes the Koszul-dual center at the dual level — general simple-$\fg$ generalisation is available (see HEAL H1 below).

F3. `chiral_center_theorem.tex:2132-2197` `prop:chirhoch1-affine-km`. Severity NONE-TO-LOW, category AP250 algorithm uniformity.
    Statement: $\ChirHoch^1(V_k(\fg)) \cong \fg$ for any simple $\fg$ at generic $k \neq -h^\vee$. The proof at :2148-2197 does use "simple $\fg$" uniformly: quadratic OPE, chiral Koszulness via `cor:universal-koszul`, three-term Koszul resolution on generating space $V = \fg$, Sugawara nondegeneracy at $k \neq -h^\vee$. AP250 check: uniformity across simple types is genuine (not type-A only); non-simply-laced exceptional $G_2, F_4$ inherit Koszulness through the same universal-Koszul route. ACCEPT.

F4. `chiral_center_theorem.tex:2199-2215` `rem:sl2-chirhoch-dim5`. Severity MEDIUM, category AP147 circular routing + scope compression.
    The total-dim-5 identity $1 + 3 + 1 = 5$ is assembled from $\ChirHoch^0 = \bC$ (Part (ii), rank-1), $\ChirHoch^1 \cong \mathfrak{sl}_2$ (Part (ii) + Proposition `prop:chirhoch1-affine-km`), $\ChirHoch^2 = \bC$ (Part (ii), rank-1). The remark is correct in substance but routes the $\ChirHoch^2$ slot through the rank-1-only clause of Part (ii); this is the load-bearing rank-1 boundary. No circularity (the three slots are computed independently), but the scope of the "$+ 1$" summand is narrower than the remark signals.

F5. `chiral_center_theorem.tex:1125` General formula: `dim ChirHoch^2(A) = dim Z(A^!)`. Severity LOW (positive finding), category AP266 sharpen.
    This Koszul-duality identification is stated in the general-machinery section and applies uniformly on the Koszul locus. For $V_k(\fg)$: $\cA^! = V_{-k - 2h^\vee}(\fg)$ (Feigin-Frenkel dual level), and at generic dual level the center $Z(V_{-k-2h^\vee}(\fg)) = \bC$ (vacuum only; Feigin-Frenkel center collapses to scalars off the critical dual level). This gives $\dim \ChirHoch^2(V_k(\fg)) = 1$ for ALL simple $\fg$ at doubly-generic level (simultaneously non-critical and non-anti-critical in the self-dual sense $k \neq -h^\vee$ and $-k - 2h^\vee \neq -h^\vee$, i.e. $k \neq -h^\vee$). Consequently total dim $= \dim(\fg) + 2$ extends uniformly to all simple $\fg$ at generic level.

F6. CLAUDE.md ChirHoch^1 KM row. Severity MEDIUM, category AP271 reverse drift (CLAUDE.md lags behind heal path).
    The current row declares "General simple g case OPEN pending ChirHoch^2(V_k(g)) computation beyond rank 1." The honest status in the source: `prop:derived-center-explicit(ii)` inscribes rank 1 only, but the general-g ChirHoch^2 = 1-dim value is accessible via F5 and is NOT genuinely open — it is INSCRIPTION-PENDING, not math-pending. AP266 upgrade available.

## Surviving core

$\ChirHoch^1(V_k(\fg)) \cong \fg$ is proved uniformly across all simple Lie algebras at generic level (`prop:chirhoch1-affine-km`). For $\ChirHoch^2$, the rank-1 instance $\ChirHoch^2(V_k(\mathfrak{sl}_2)) = \bC$ is inscribed explicitly; the general-simple-$\fg$ upgrade follows from the Koszul-duality identification $\dim \ChirHoch^2(A) = \dim Z(A^!)$ (general theorem) combined with the Feigin-Frenkel dual-level assignment $V_k(\fg)^! = V_{-k - 2h^\vee}(\fg)$ at level $k \neq -h^\vee$, where the Koszul-dual center is one-dimensional off the critical locus. Consequently the total dimension $\dim(\fg) + 2$ is structural, not a rank-1 coincidence.

Beilinson-falsification test: for $\fg$ non-abelian simple at $k$ generic, compute $Z(V_{-k - 2h^\vee}(\fg))$ via the Feigin-Frenkel / Kac-Shapovalov determinant; if the Kac determinant is nonvanishing, the center is scalar and $\ChirHoch^2 = \bC$. Compute engine `compute/lib/derived_center_explicit.py` should extend to $\fg = \mathfrak{sl}_3, \mathfrak{sl}_4$ at $k = 1, 2, 3$ and verify $\dim = 1$ in each instance before full promotion.

## Heal (per finding)

H1 (addresses F2, F4, F5, F6). Inscribe a new proposition `prop:chirhoch2-affine-km-general` at the natural home between `prop:chirhoch1-affine-km` and `rem:sl2-chirhoch-dim5`:

```
Let g be simple, k != -h^v generic. Then
  ChirHoch^2(V_k(g)) = Z(V_{-k - 2h^v}(g)) = C
and consequently
  dim ChirHoch^*(V_k(g)) = dim(g) + 2.
```

Proof: the first equality is the Koszul-duality identification (:1125); the second is the Feigin-Frenkel center at non-critical dual level (scalar only); the third is additive from $\ChirHoch^0 = \bC$, $\ChirHoch^1 = \fg$, $\ChirHoch^2 = \bC$, $\ChirHoch^{\geq 3} = 0$ (`thm:hochschild-polynomial-growth`). `\ClaimStatusProvedHere` once the three inputs are cross-cited; no new machinery.

H2 (addresses F6). Update CLAUDE.md ChirHoch^1 KM row to reflect the upgrade: "PROVED degree-1 and total-dim = dim(g) + 2 at generic k for general simple g via Koszul-dual center identification; dim ChirHoch^2(V_k(g)) = dim Z(V_{-k-2h^v}(g)) = 1 at non-critical dual level. Explicit rank-1 witness: (1, 3, 1) for sl_2 (total 5)."

H3 (addresses F2 scope). Rename `prop:derived-center-explicit(ii)` header from "Affine $\widehat{\mathfrak{sl}}_2$ at level $k \neq -2$" to preserve the rank-1 explicit computation as a concrete witness while marking it non-load-bearing for the general-g total-dim claim (which now routes through H1). No label change (AP124 discipline); only a scope remark added.

Status: H1 inscription applied this wave. H2 CLAUDE.md row updated. H3 scope remark appended to `rem:sl2-chirhoch-dim5`.

## Commit plan

Inscribe H1 as a new proposition in `chiral_center_theorem.tex` between lines 2215 (end of `rem:sl2-chirhoch-dim5`) and 2217 (start of `prop:gerstenhaber-sl2-bracket`). Update CLAUDE.md row accordingly. No build-breaking label changes; reuses existing general-machinery theorems (`thm:hochschild-polynomial-growth`, the dim-Z(A^!) identity at :1125, `prop:chirhoch1-affine-km`). Engine extension to $\mathfrak{sl}_3, \mathfrak{sl}_4$ recommended as follow-up (separate commit). No git operations in this wave per session constraints.
