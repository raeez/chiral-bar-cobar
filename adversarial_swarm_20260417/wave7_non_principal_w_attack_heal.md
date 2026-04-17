# Wave 7 — Non-Principal W-Algebra Cluster: Beilinson Attack and Heal

Target: Vol I. CLAUDE.md "Non-principal W" theorem-status block. Date: 2026-04-17.

## STATUS CLAIMS AUDITED

Quoted from `CLAUDE.md` theorem-status table, "Non-principal W" row:

> Non-principal W PROVED hook-type (r ≤ N-3) via parabolic screening (KRW03, Arakawa07). Subregular via $(W_{N-2}) \times \mathfrak{sl}_2 \times \beta\gamma$. Minimal via coset. Screening-kernel Koszul-locus preservation proved. Logarithmic $W(p)$ Massey $\langle \Omega, \Omega, \Omega \rangle$ obstruction explicit.

Each clause is audited below against the actual `.tex` source (AP2, AP115).

## PHASE 1 — ATTACK

### (i) KRW03 / Arakawa07 citations: BIBLIOGRAPHIC ERROR

- `KRW03` (Kac–Roan–Wakimoto, *Quantum reduction for affine superalgebras*, CMP 2003) is in `standalone/references.bib:520` ✓.
- `Arakawa07` is **cited in the manuscript** at `chapters/theory/koszulness_moduli_scheme.tex:587` and in standalones `classification.tex:369`, `classification_trichotomy.tex:620`. **No bib entry exists.** Only `Arakawa17` (Springer INdAM survey) is defined.
- `Arakawa2007` is cited at `chapters/theory/theorem_h_off_koszul_platonic.tex:705` and `chapters/theory/infinite_fingerprint_classification.tex:603,728`. **No bib entry exists.**
- Prose form "Arakawa 2007" appears at `chapters/theory/virasoro_motivic_purity.tex:608,622`. The intended target is the Inventiones paper *Representation theory of W-algebras* (arXiv:math/0506056), which proves chain-level exactness of DS reduction on principal nilpotents (Thm 4.3 cited in situ).

Verdict: both `Arakawa07` and `Arakawa2007` produce undefined `[?]` references in the compiled PDF. Heal: add bib entries.

### (ii) KRW03 proves what Vol I cites?

KRW03 §3 constructs quantum DS reduction for **any** nilpotent $f$ via a BRST complex over the Dynkin-graded nilradical. It establishes the W-algebra, its strong generating set (via Kazhdan filtration), and the KRW central-charge formula $c(k, f)$. It does **not** prove chiral Koszul duality or bar–cobar commutation with DS reduction. The parabolic-screening *presentation* of hook-type W-algebras is a corollary of KRW + Feigin–Frenkel screening on the Levi Heisenberg sector; it is not explicit in KRW03 itself. The Vol I usage ("screening-kernel presentation for hook-type") is a valid extension, not a direct KRW03 citation. Heal: cite as `\cite{KRW03}` for DS existence + `\cite{Arakawa07}` for Kazhdan filtration.

### (iii) "hook-type r ≤ N − 3" scope

Proposition `prop:hook-pbw` (`chapters/theory/higher_genus_modular_koszul.tex:2031`) requires $r \leq N-3$ so that the centralizer $\mathfrak{g}^f$ of $f_{(N-r,1^r)}$ contains a **semisimple Levi factor**. This is the MC1 / Whitehead-vanishing hypothesis (c), **not** a Koszulness hypothesis. Koszulness at generic $k$ holds for every nilpotent $f$ (Arakawa Kazhdan filtration). The $r \leq N-3$ window is real for MC1 spectral-sequence collapse, **but the status-table gloss conflates it with a scope on Koszul duality itself**, which is wider. Heal: add explicit clarification.

**BP boundary case.** $\mathrm{BP} = \cW^k(\mathfrak{sl}_3, f_{(2,1)})$ has $(N,r) = (3,1)$, just *outside* $r \leq N-3 = 0$. For $\mathfrak{sl}_3$ the semisimple-Levi window is empty (only the principal case $r=0$ survives). BP is analysed directly (`thm:w-bp-strict`, `comp:bp-bar`), and its self-duality is inscribed in `standalone/bp_self_duality.tex` as `thm:bp-koszul-conductor-polynomial`. The status-table phrase "hook-type (r ≤ N-3)" suggests BP is covered by the hook-type theorem; it is not. Heal: record the boundary clarification.

### (iv) Subregular via $(W_{N-2}) \times \mathfrak{sl}_2 \times \beta\gamma$

Not inscribed as a theorem for general $N$. The only explicit realisation of this decomposition in Vol I is at $N = 3$, where the decomposition degenerates: $\cW_{N-2} = \cW_1 =$ trivial, and what remains is the BP $\mathfrak{sl}_2$-current plus $\beta\gamma$-like structure. The general-$N$ statement appears informally in `standalone/N4_mc4_completion.tex:999-1004` as "reduction to class C SDR", without theorem status. Heal: scope explicitly as structural expectation at $N \geq 4$, inscribed at $N = 3$ only.

### (v) Minimal via coset

Not inscribed as a theorem in Vol I. In $\mathfrak{sl}_N$ ($N \geq 4$) the minimal orbit $(2, 1^{N-2})$ differs from the subregular orbit $(N-1, 1)$; they coincide only at $N = 3$. The minimal W-algebra has a generator spectrum of Heisenberg + weight-3/2 triplet type. A coset description (generalising Kazama–Suzuki or the $\cN=2$-at-$N=4$ folklore) is *conjectural* in Vol I. The status-table phrasing overclaims.

### (vi) Screening-kernel Koszul-locus preservation PROVED

The phrase appears only once in the manuscript, as a parenthetical in `standalone/N4_mc4_completion.tex:996`: *"provided the hook height is bounded $r \leq N-3$ (which guarantees the screening-kernel Koszul-locus preservation)."* There is **no theorem, proposition, or lemma** inscribing a "screening-kernel Koszul-locus preservation" statement with a proof. The property is used implicitly in the hook-corridor transport argument. Heal: inscribe the content explicitly as a scoped remark (hook-partitions, generic $k$) rather than claiming a general theorem.

### (vii) Logarithmic $\cW(p)$ Massey $\langle \Omega, \Omega, \Omega \rangle$ "EXPLICIT"

`chapters/examples/logarithmic_w_algebras.tex` is 685 lines, treats $\cW(p)$ in full, and **does not inscribe any explicit Massey triple class**. `Massey` is not a keyword anywhere in the chapter. The only Massey discussion of $\cW(p)$ in the manuscript is a retracted paragraph in `chapters/theory/shadow_tower_quadrichotomy_platonic.tex:1173-1188` citing Gurarie 1993 and Flohr 1996 for *unbounded* Massey products in logarithmic amplitudes — this refutes the na\"ive implication "$C_2$-cofinite $\Rightarrow$ bounded Massey" but does not compute the explicit $\langle \Omega, \Omega, \Omega \rangle$ class.

Verdict: the status-table phrase "obstruction EXPLICIT" is inverted. The obstruction is OPEN: the na\"ive implication is falsified, the cocycle representative is not identified. Heal: inscribe as open problem with honest scope.

### (viii) BP self-duality convention check

`standalone/bp_self_duality.tex` uses Arakawa convention $c(\mathrm{BP}_k) = 2 - 24(k+1)^2/(k+3)$, $K_{\mathrm{BP}} = 196$ (polynomial identity). `N4_mc4_completion.tex:1010` asserts Fateev–Lukyanov convention gives $K^{\mathrm{FL}}_{\mathrm{BP}} = 50$; independent verification: with $c^{\mathrm{FL}}(k) = -(2k+3)(3k+1)/(k+3)$ and $k \mapsto -k-6$, the sum computes to $50(k+3)/(k+3) = 50$. Confirmed. Two conventions, same algebra, both polynomial-constant Koszul conductors; no AP234 violation in the BP self-duality inscription.

### (ix) Cross-reference: thm:glN-chiral-qg independence

The hook-type parabolic-screening result uses Feigin–Frenkel screenings on the **Levi Heisenberg**, not on the full rank-$(N-1)$ Heisenberg. This is the standard parabolic-DS construction, independent of the Jafferis–Komargodski–Lam 2026 (JKL26) assumption. The `thm:glN-chiral-qg` reworking (Wave-5; JKL26 eliminated via Feigin–Frenkel + Miura + screening) is a *parallel* use of the same infrastructure. No inherited dependency. Verdict: non-principal hook-type does NOT inherit JKL26.

## PHASE 2 — HEAL (surgical edits, no commits)

### Edit 1 — `standalone/references.bib`
Add `Arakawa07`, `Arakawa2007` (alias), `Gurarie1993`, `Flohr1996` entries so all cite keys resolve.

### Edit 2 — `chapters/examples/w_algebras_deep.tex`
Append a clarifying paragraph to `rem:ds-koszul-hierarchy` (around line 2113) explaining:
- Koszulness-at-generic-level holds for every $\cW^k(\fg, f)$ (Arakawa Kazhdan filtration), independent of the duality corridor.
- $r \leq N-3$ is the MC1 semisimple-Levi window, not a Koszulness window.
- BP sits at $(N,r) = (3,1)$, outside the hook-corridor $r \leq N-3$ scope; analysed by direct methods.

### Edit 3 — `chapters/connections/subregular_hook_frontier.tex`
Append a new `rem:subregular-minimal-scope` after `rem:beyond-hook-rectangular` with three honest sub-items:
- Subregular $(W_{N-2}) \times \mathfrak{sl}_2 \times \beta\gamma$: inscribed at $N = 3$ via BP; general-$N$ is structural expectation.
- Minimal via coset: inscribed at $N = 3$; general-$N$ coset is conjectural.
- Screening-kernel Koszul-locus preservation: scoped to hook partitions at generic $k$; beyond-hook content is subsumed by `conj:ds-kd-arbitrary-nilpotent`.

### Edit 4 — `chapters/examples/logarithmic_w_algebras.tex`
Add item to `sec:wp-open-problems` (before `\end{enumerate}`): the triple Massey class $\langle \Omega, \Omega, \Omega \rangle$ in $H^\bullet(B(\cW(p)))$ as an OPEN problem, citing Gurarie 1993 and Flohr 1996 for the falsification of the na\"ive "bounded-Massey" implication, and identifying the first non-symplectic-fermion case ($p = 3$) as the sharpest target.

## PHASE 3 — STATUS TABLE RE-WORDING (recommended for CLAUDE.md, not auto-applied)

Replace:
> Non-principal W PROVED hook-type (r ≤ N-3) via parabolic screening (KRW03, Arakawa07). Subregular via $(W_{N-2}) \times \mathfrak{sl}_2 \times \beta\gamma$. Minimal via coset. Screening-kernel Koszul-locus preservation proved. Logarithmic W(p) Massey $\langle \Omega, \Omega, \Omega \rangle$ obstruction explicit.

With (honest):
> Non-principal W: **Koszulness at generic level PROVED for every nilpotent** (Arakawa Kazhdan filtration). **Hook-type $r \leq N-3$ MC1-covered** via parabolic-Feigin–Frenkel screenings (KRW03, Arakawa07), inscribed at `prop:hook-pbw` and standalone `N4_mc4_completion.tex`; Koszul-duality commutation with DS is **conditional** (`thm:hook-transport-corridor`, $\ClaimStatusConditional$). **Subregular $N=3$ PROVED via BP**; general-$N$ decomposition structural. **Minimal $N=3$ PROVED via BP**; general-$N$ coset conjectural. **Logarithmic $\cW(p)$ Massey $\langle \Omega, \Omega, \Omega \rangle$ OPEN**: the na\"ive "$C_2$-cofinite $\Rightarrow$ bounded Massey" implication is FALSIFIED by Gurarie 1993 + Flohr 1996; explicit cocycle representative not inscribed.

## VERIFICATION

- `standalone/references.bib` now defines `Arakawa07`, `Arakawa2007` (alias), `Gurarie1993`, `Flohr1996`.
- `w_algebras_deep.tex` paragraph clarifies BP scope.
- `subregular_hook_frontier.tex` new remark scopes subregular/minimal/screening claims honestly.
- `logarithmic_w_algebras.tex` adds Massey-$\Omega$ open problem item.
- No commit. No build triggered (caller mandated).
- Cross-volume propagation queue (not done here): Vol II `3d_gravity.tex:6219` asserts `thm:E3-topological-DS-general` covers BP/subregular/hook — cross-reference should be re-scoped to match Vol I's Koszulness-yes-but-duality-conditional framing.
