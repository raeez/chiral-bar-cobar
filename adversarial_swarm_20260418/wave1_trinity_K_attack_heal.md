# Wave-1 Adversarial Audit: Trinity K Theorem

**Date.** 2026-04-18.
**Target.** Vol I `chapters/theory/universal_conductor_K_platonic.tex` (1289 lines, read linearly, 4 chunks 1-250 / 250-500 / 500-750 / 750-1000 / 1000-1289). Companion: `chapters/theory/kappa_conductor.tex:60-268`, `chapters/theory/higher_genus_complementarity.tex:3000-3145`.
**Flag.** AP272 (unstated cross-lemma via folklore citation), AP238 (statement/proof internal contradiction), AP234 (two Koszul-conductors-same-letter), AP281 (bibkey naming drift), AP264 (forward-/phantom-ref), AP270 (multi-object status-row conflation).

---

## 1. Attack ledger

### F1. Heisenberg three-way numerical contradiction (SEVERITY: FATAL — AP238).

Three inscribed values for Heisenberg `K` cannot be simultaneously correct:

| Site | Inscribed $K(\mathcal{H}_k)$ | Route |
|------|----------|-------|
| `universal_conductor_K_platonic.tex:481` (Cor statement) | $-k$ | "$\kappa = K/2$ for the abelian case, with sign correction" |
| `universal_conductor_K_platonic.tex:494-498` (same Cor proof) | $-2$ | FMS spin-1 bosonic, independent of $k$ |
| `universal_conductor_K_platonic.tex:484` (same Cor, symmetric form) | $+2$ (from $K^c=c+c^!=1+1$) | central-charge sum |
| `kappa_conductor.tex:192` (Cor Heisenberg) | $-2$ | spin-1 bosonic |
| `higher_genus_complementarity.tex:3096` (complementarity table) | $\kappa+\kappa^!=0$ (so $K^c$ n/a) | Heisenberg is free-field with $\kappa+\kappa^!=0$ |
| CLAUDE.md HZ-4 and AP234 | $K=-2$ for Heisenberg (spin-1 bosonic FMS); $\kappa+\kappa^!=0$ | AP234 canonical |

The Trinity Theorem (`thm:uc-trinity`, :376) asserts $K_E=K_c=K_g$ UNCONDITIONALLY on $\KSDual(X)\cap\BRSTGauged$; if the three numerical values differ for the first family in the chapter's own corollary, the headline equality is broken at entry.

Root cause. The proof of `cor:uc-K-heisenberg` applies the FMS ghost formula to a single spin-1 **bosonic** generator and gets $-2$, but then invokes "the convention $\kappa=K/2$ for the abelian case, with sign correction for the matter-vs-ghost grading" to reassign the corollary headline to $-k$. This is not a derivation — it is a convention-substitution that changes the invariant mid-proof. The AP234 HZ-4 κ-route $K_c = 2k$ is the CENTRAL-CHARGE sum in the κ+κ^! family (AP234 ϱ-route with ϱ_Heis = 0), which equals $k-k = 0$, NOT $2k$; CLAUDE.md §AP234 attributes $2k$ to "Heisenberg" but that is the $c(\mathcal{H}_k)+c(\mathcal{H}_{-k})$ sum using $c=1+k$ (non-standard: the Heisenberg central charge is $c=1$ independent of level; the level rescales $J\mapsto J/\sqrt{k}$). So the CLAUDE.md "AP234 κ-route gives 2k for Heisenberg" line itself is convention-dependent.

### F2. Trinity proof silent branch by family (SEVERITY: LOAD-BEARING — AP272).

The $K_c=K_g$ arrow (:404-437) CORRECTLY admits (this was already honest prose in the current manuscript):

> "The matter-reflection $c_{\text{matter}}(\cA) = -c_{\text{matter}}(\cA^!)$ is not a single universal theorem but the union of per-family involutions: the Feigin–Fuks $c\mapsto 26-c$ symmetry for Virasoro; the Sugawara denominator reflection $k\mapsto -k-2h^\vee$ for affine Kac–Moody; the Bershadsky–Polyakov $k\mapsto -k-6$ self-duality for $W_3^{(2)}$; the Feigin–Frenkel screening symmetry on principal $W_N$; and lattice $\ZZ_N$ self-duality for rational lattice vertex algebras. Each family's reflection is cited separately; the $K_c=K_g$ arrow closes on the union over the Koszul-self-dual locus."

This is an AP272 honest-self-flag. The Trinity Theorem's proof is NOT a uniform derivation of a single identity; it is a case-by-case verification that five family-indexed involutions each satisfy $c_{\text{matter}}(\cA)=-c_{\text{matter}}(\cA^!)$. On families outside this list (logarithmic $W(p)$, $N=2$ SCA, non-principal $W$ with non-matching DS-dual, roots-of-unity small quantum groups, non-rational indefinite lattice VOAs) the identity is UNVERIFIED. But the theorem environment is `\ClaimStatusProvedHere` with no scope clause in the statement.

The "verified family-by-family in Wave 13 Appendix A" (:437) is phantom: no Wave-13 Appendix A is inscribed; the label refers to a narrative wave, not a typeset appendix (AP254 + AP280 closure-by-repackaging pattern).

### F3. Phantom bibkeys (SEVERITY: HIGH — AP281).

Bibliography audit against `standalone/references.bib` (127 entries): the following `\cite{...}` keys used in `universal_conductor_K_platonic.tex` DO NOT resolve:
- `polyakov1981` (used :166, :517) — "Polyakov critical dimension of bosonic string theory"
- `fms1986` (used :165, :314, :762) — Friedan–Martinec–Shenker
- `wakimoto1986` (used :136, :208, :551) — Wakimoto resolution
- `feigin_frenkel_ds` (used :138, :208, :551, :603, :681) — Feigin–Frenkel DS
- `beilinson_drinfeld_chiral` (used :106, :324) — BD chiral algebras book
- `hinich_homological` (used :307) — Hinich homological algebra
- `kac_roan_wakimoto2003` (used :608, :681, :693) — KRW03
- `faltings1992` (used :338, :401, :906) — Faltings GRR
- `borcherds1998` (used :1085)
- `felder1989` (used :140)
- `deboer_tjin1993` (used :604)
- `goddard_kent_olive1986` (used :985)
- `frenkel_kac_lepowsky` (used :733)

Bibkeys that DO resolve: `feiginfuks1983`, `kacpeterson1984`, `polyakov1990`, `bershadsky1991`, `arakawa2005`, `feiginfrenkel1992`, `arakawa2017`, `kac1998`. So the Trinity proof's load-bearing per-family reflections cite correctly, but the background infrastructure (FMS formula itself, Wakimoto resolution, DS reduction, Hinich cofibrant model structure, Faltings GRR) resolve to `[?]` at PDF build. This is the AP281 pattern: alias drift + systemic phantom-cite rate.

### F4. ϱ_A = H_N−1 back-fitted, not derived (SEVERITY: MEDIUM — open frontier, acknowledged).

Remark :634-653 ("The harmonic anomaly density of $W_N$") writes
$\rho(W_N) := \sum_{j=2}^N 1/j = H_N - 1$
and claims "$K^\kappa(W_N) = \kappa(W_N)+\kappa(W_N^!) = K(W_N)\cdot\rho(W_N)$". This is arithmetic-consistent (since $\kappa(W_N) = (H_N-1)c$ from C4 and $c+c^! = K_N$), but the STRUCTURAL origin of $\rho = H_N - 1$ as "anomaly density" is asserted by analogy with "Frenkel–Wakimoto anomaly density" (bibkey not provided) and not derived from a DS-Lagrangian Hessian or coset-ratio computation. CLAUDE.md §F1.b (Wave-1 audit) registers this as an OPEN FRONTIER. The remark does not cross into AP269 (SDR fabrication with proved-negative witness) because the arithmetic consistency survives; it is, however, AP244-adjacent (redundant foundational notion: $\rho$ and $\varrho$ are the same object up to convention and both appear in the programme).

### F5. Resolution-independence (P1) non-sequitur (SEVERITY: MEDIUM).

The proof of (P1) (:300-315) asserts that the total Virasoro central charge $c_{\text{tot}} := c_{\text{matter}} + c_{\text{ghost}}$ is invariant under quasi-isomorphism, hence $c_{\text{ghost}}$ is determined up to a shift absorbed by the matter sector. But TWO different quasi-free resolutions of the same $\cA$ need not have the same $c_{\text{matter}}$ split: they can have compensating shifts between the matter and ghost sectors. The FKS example at :144 of `kappa_conductor.tex` explicitly admits this: $\widehat{\mathfrak{g}}_1$ has two quasi-free resolutions (Wakimoto: $K = 2\dim(\fg)$ fermionic $bc(1)$-ghosts; FKS: $K = r$ bosonic free-boson matter), with DIFFERENT $K$ values. The manuscript flags this honestly as "resolution-dependent; P1 holds up to the choice of matter-vs-ghost convention", which is an AP238-adjacent admission that breaks P1 as stated. The theorem statement must carry this scope.

### F6. Cross-volume consumer consistency (SEVERITY: MEDIUM — AP287 attribution discipline).

`thm:uc-universal-trace-identity` is `\ClaimStatusProvedElsewhere` at :1077, attributing to Vol III `prop:bkm-weight-universal`. The cross-volume pointer is explicit and the attribution is honest. BUT: 20 files across Vols I/II/III cite the Trinity Theorem or the trace identity; of these, at least 11 are in Vol II/III. Each consumer needs per-site verification that the inherited scope qualifier (K3-fibered Class A, $N \in \{1,2,3,4,6\}$, "on the Koszul-self-dual locus") propagates. Spot check at `calabi-yau-quantum-groups/chapters/theory/phi_universal_trace_platonic.tex` and `calabi-yau-quantum-groups/chapters/examples/cy_d_kappa_stratification.tex` required; deferred to Wave 2.

### F7. Multi-object status-row conflation in CLAUDE.md (SEVERITY: LOW — AP270).

CLAUDE.md B93 (HZ-4) inscribes the identity $\kappa + \kappa^! = \varrho_A \cdot K$ with canonical values $\{0, 13, 250/3, 98/3\}$ and attributes $K$ to Trinity $K = c + c^! = -c_{\text{ghost}}(\text{BRST})$ with values $\{-k, 2\dim(\fg), 26, 100, 196\}$. The Heisenberg row has "$-k$" here but the inscribed proof gives $-2$ and the $c+c^!$ sum gives $+2$. The CLAUDE.md row is a compressed three-object narrative (AP270) mixing $K_c$, $K_g$, and the AP234 ϱ-route.

---

## 2. Surviving core

After adversarial compression, the Trinity K theorem survives as:

> **Trinity K (per-family pattern, rectified).** Let $\cA \in \KSDual(X)\cap\BRSTGauged$ belong to one of the nine inscribed families {Heisenberg, free fermion, $bc(\lambda)$, $\beta\gamma(\lambda)$, affine Kac–Moody $V_k(\fg)$ at non-critical level, Virasoro $\Vir_c$, principal $W_N$, Bershadsky–Polyakov, lattice VOA $V_L$}. Then $K_g(\cA)$ (negative ghost charge of a fixed quasi-free BRST resolution) coincides with $K_c(\cA)$ (central-charge sum via the family's own matter-reflection: Feigin–Fuks for Virasoro/$W_N$, Sugawara/Feigin–Frenkel for $V_k(\fg)$, Bershadsky self-duality for BP, unimodular self-duality for lattice). The coincidence is verified per-family, not by a uniform theorem. Per-family $K$-values: $K(\mathcal{H}_k) = -2$ (single spin-1 bosonic generator, level-independent; the AP234 ϱ-route $K_c = 0$ for Heisenberg is a DIFFERENT invariant, the κ-complementarity sum with ϱ_Heis=0); $K(V_k(\fg)) = 2\dim(\fg)$; $K(\Vir) = 26$; $K(W_N) = 4N^3-2N-2$; $K(\BP) = 196$.

Trinity $K_E = K_c$ on the Koszul-self-dual locus remains a genuine bar-Euler theorem (uses the Koszul-Euler identity, no family branching). Trinity $K_c = K_g$ is the per-family case-by-case content. $K$ at the working definition $K := K_g$ is canonical via (P1) resolution-independence WITHIN A FIXED MATTER-VS-GHOST SPLIT, not across splits.

---

## 3. Per-finding heals

### H1. Heisenberg rectification (fixes F1).

Rewrite `cor:uc-K-heisenberg` (statement + proof + summary row) so that ONE value is inscribed: $K(\mathcal{H}_k) = -2$, spin-1 bosonic, level-independent. The "$-k$" value in the summary table is the AP234 κ-complementarity-adjacent object $\kappa(\mathcal{H}_k) = k$ with dual $\kappa(\mathcal{H}_k^!) = -k$ summing to $0$; it does not belong in the $K$-column. Add a scope-distinguishing remark: "The working-conductor $K = K_g$ is convention-bosonic-spin-1 for Heisenberg; the κ-complementarity sum $\kappa + \kappa^! = 0$ is a DIFFERENT invariant (HZ-7 κ-route, ϱ_Heis = 0), not reconcilable with $K_g$ by sign flip." Match `kappa_conductor.tex:192`.

Status tag unchanged: `\ClaimStatusProvedHere` for $K(\mathcal{H}_k) = -2$ (spin-1 bosonic FMS is a chain-level invariant).

### H2. Trinity Theorem scope (fixes F2 + F7).

Rewrite theorem statement of `thm:uc-trinity` (:375-385) to carry explicit family scope:

> **Trinity Theorem (per-family).** On each of the nine standard-landscape families $\cA \in \{\mathcal{H}_k, \psi, bc(\lambda), \beta\gamma(\lambda), V_k(\fg), \Vir_c, W_N, \BP, V_L\}$ separately, the three conductors coincide: $K_E(\cA) = K_c(\cA) = K_g(\cA)$. The arrow $K_E = K_c$ is uniform (bar-Euler theorem on the Koszul-self-dual locus). The arrow $K_c = K_g$ is verified per-family via the family's own matter-reflection: Feigin–Fuks $c \mapsto 26 - c$ (Virasoro; $W_N$ by Feigin–Frenkel screening extension), Sugawara reflection $k \mapsto -k - 2h^\vee$ (affine Kac–Moody), Bershadsky–Polyakov self-duality $k \mapsto -k - 6$ (BP, $W_3^{(2)}$), lattice unimodular self-duality (lattice VOA). Families outside this list (logarithmic $W(p)$, $N=2$ SCA, non-principal $W$ with non-matching DS-dual, roots-of-unity small quantum groups, non-rational indefinite lattice VOAs) are OPEN.

Status tag: downgrade from `\ClaimStatusProvedHere` to `\ClaimStatusProvedHere` with a scope remark — the theorem as proved IS the per-family union; honest scope cures AP272 without structural loss. Add a companion `\begin{conjecture}[Uniform Trinity]` that a single universal matter-reflection theorem $c_{\text{matter}}(\cA) = -c_{\text{matter}}(\cA^!)$ holds on all of $\KSDual(X) \cap \BRSTGauged$; inscribed as conjecture, not theorem.

Retire the "verified family-by-family in Wave 13 Appendix A" (:437, :631) clause: no appendix is inscribed, the narrative wave label is AP254/AP280.

### H3. Bibkey resolution (fixes F3).

Add to `standalone/references.bib` the 13 missing entries: `polyakov1981` (Polyakov 1981 Phys Lett B), `fms1986` (Friedan-Martinec-Shenker 1986 Nucl Phys B271), `wakimoto1986` (Wakimoto 1986 CMP), `feigin_frenkel_ds` (Feigin-Frenkel 1992 IJMP), `beilinson_drinfeld_chiral` (BD 2004 AMS CPAM vol 51), `hinich_homological` (Hinich 1997 CAlg), `kac_roan_wakimoto2003` (KRW CMP), `faltings1992` (Faltings JAG 1992), `borcherds1998` (Borcherds Invent 1998), `felder1989` (Felder 1989 NPB), `deboer_tjin1993` (de Boer-Tjin CMP 1993), `goddard_kent_olive1986` (GKO PLB 1986), `frenkel_kac_lepowsky` (FLM book Academic Press 1988). Deferred to Wave-2 bibkey heal pass (systemic — AP281 is Vol-I-wide).

### H4. ϱ_A structural origin (fixes F4 — open frontier, acknowledged).

Inscribe remark `rem:varrho-open-frontier` after `rem:uc-harmonic-density-WN`: "The identification $\varrho_{W_N} = H_N - 1$ is arithmetic-consistent but structurally UNEXPLAINED. Candidate structural origins (Hessian determinant of the DS Lagrangian, coset central-charge ratio, Berezinian shift of DS Jacobson–Morozov gradings) remain OPEN. We inscribe $\varrho_{W_N} = H_N - 1$ as computational datum, not as derived invariant." Matches CLAUDE.md Wave-1 audit §F1.b.

### H5. P1 resolution-independence scope (fixes F5).

Rewrite (P1) to: "$K_g(\cA)$ depends only on the quasi-isomorphism class of $\cA$ WITHIN A FIXED MATTER-VS-GHOST SPLIT: two quasi-free BRST resolutions $(C_\bullet, Q)$ and $(C'_\bullet, Q')$ presenting $\cA$ with the SAME matter sector produce the same $-c_{\text{ghost}}$. Across convention changes (matter-to-ghost absorption, e.g.\ the FKS collapse $\widehat{\fg}_1 \simeq V_{\Lambda_\fg}$), $K_g$ is NOT invariant; the drop from $2\dim(\fg)$ to $\operatorname{rank}(\fg)$ is the invariant bookkeeping of the matter-vs-ghost convention." Downstream: add a scope remark to the summary table noting that lattice-VOA $K = \operatorname{rank}(L)$ is convention-matter, not convention-ghost.

### H6. Cross-volume consumer audit (fixes F6 — deferred).

Defer 20-file propagation audit to Wave 2. Inscribe in FRONTIER.md a Wave-2 target: "Trinity K cross-volume scope propagation (20 files across I/II/III)".

---

## 4. Inscription plan (no commits this session per brief)

**Edit A.** `chapters/theory/universal_conductor_K_platonic.tex`:
1. `cor:uc-K-heisenberg` (:478-508): rewrite statement to $K(\mathcal{H}_k) = -2$ and remove the "$\kappa=K/2$ sign correction" substitution; add scope remark distinguishing $K_g$ from the κ-complementarity.
2. Summary table row (:820-821): change "$-k$" to "$-2$"; update closing summary (:1248).
3. `thm:uc-trinity` (:375-449): rewrite statement with explicit per-family scope; add `\begin{conjecture}[Uniform matter-reflection]` companion.
4. (P1) proof (:304-315): add matter-vs-ghost-split scope qualifier.
5. Delete "Wave 13 Appendix A" forward-references at :437 and :631.
6. `rem:varrho-open-frontier` inserted after :653.

**Edit B.** `chapters/theory/kappa_conductor.tex`:
1. `thm:conductor-trinity` (:71-80): add per-family scope mirroring Edit A.3.
2. `thm:platonic-conductor` (P1) and (P3) (:131-145): add matter-vs-ghost-split qualifier.

**Edit C.** `chapters/theory/higher_genus_complementarity.tex`:
1. Table `tab:complementarity-landscape` (:3073-3140): verify Heisenberg row — it already has $\kappa + \kappa^! = 0$ and $K^c =$ n/a, which is correct under the heal. No edit needed; this table is the honest source of truth.

**Edit D.** CLAUDE.md Trinity K / AP234 rows:
1. HZ-4: remove "$\kappa$ for Heis: `\kappa(H_k)=k`" from the list of Trinity-K values and clarify that Heisenberg κ-route gives $\kappa+\kappa^!=0$ (free-field class G), which is a DIFFERENT invariant from $K_g = -2$.
2. AP234 entry: explicit note that Heisenberg $K_c = 2k$ in CLAUDE.md §AP234 was convention-dependent on a non-standard Heisenberg central charge; canonical $c(\mathcal{H}_k) = 1$ gives $K_c = 2$, matching `kappa_conductor.tex:192`.

**No commits this session.** Defer all Edits A–D + Wave-2 bibkey heal + cross-volume consumer audit to next session with explicit user approval. This note is the attack ledger only.

---

## 5. Status-tag proposals

| Site | Current | After heal |
|------|---------|------------|
| `thm:uc-trinity` | `ProvedHere` (no scope) | `ProvedHere` + per-family scope remark |
| `cor:uc-K-heisenberg` | `ProvedHere` with $K = -k$ | `ProvedHere` with $K = -2$, matching `cor:K-heisenberg` |
| (new) `conj:uc-trinity-uniform` | — | `\ClaimStatusConjectured` (uniform matter-reflection) |
| (new) `rem:varrho-open-frontier` | — | remark, cites CLAUDE.md Wave-1 audit §F1.b |
| `thm:uc-universal-conductor` (P1) | `ProvedHere` universal | `ProvedHere` with matter-vs-ghost-split scope |

---

## 6. Beilinson verdict

"Every claim is false until independently verified from primary source. Prefer a smaller true theorem to a larger false one."

The Trinity K theorem's LARGER form — three invariants coincide uniformly on the Koszul-self-dual BRST-gauged subcategory — is false-as-stated (F2). The SMALLER true form — three invariants coincide PER-FAMILY on the nine inscribed families, with each family's $K_c = K_g$ arrow using its own matter-reflection — is the surviving core. The healings above inscribe the smaller theorem at its honest scope and register the uniform theorem as a conjecture with open families (logarithmic $W(p)$, $N=2$ SCA, non-principal $W$, roots of unity, non-rational indefinite lattice VOAs).

Heisenberg is the worst-exposed case: three inscribed values for $K$ differing by convention ($-k$, $-2$, $+2$) demonstrate that "Trinity $K$ is one number" is false at the entry family. The heal standardises on $K = K_g = -2$ (spin-1 bosonic FMS) and keeps the κ-complementarity ($\kappa + \kappa^! = 0$) as a distinct invariant.

Sharpened obstruction (AP266 positive register): the gap between Trinity-uniform and Trinity-per-family is PRECISELY the class of chiral algebras on which $c_{\text{matter}}(\cA) = -c_{\text{matter}}(\cA^!)$ fails to be a uniform theorem. On the standard landscape this is a union of five involutions (Feigin–Fuks, Sugawara, Bershadsky, Feigin–Frenkel, lattice); off the standard landscape (logarithmic, $N=2$ SCA, non-principal $W$, roots of unity, indefinite) the obstruction lives as an OPEN FRONTIER class in the chiral Picard group of $\KSDual(X) \cap \BRSTGauged$. Conjecture (Wave-1 sharpening): the uniform-Trinity obstruction vanishes on the category of C$_2$-cofinite non-logarithmic chiral algebras admitting a principal DS reduction from a simple affine Kac–Moody algebra.

—End of Wave-1 attack ledger. Deferred to Wave 2: cross-volume consumer audit (F6), bibkey heal (F3), $\varrho$ structural origin (F4 frontier).
