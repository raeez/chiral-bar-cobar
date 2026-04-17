# Attack + Heal: N=2 SCA silent non-coverage under the five-family MC3 mechanism

**Date:** 2026-04-18
**Author:** Raeez Lorgat
**AP block consumed:** AP501-AP520 (N=2-SCA-swarm)
**Protocol:** CLAUDE.md CONSTITUTIONAL TRUST WARNING + AP240 (closure-by-repackaging) + AP244 (overcounted foundational terms) + AP266 (sharpened-obstruction healing template) + HZ-8 (AP4 proof after conjecture discipline).

## Phase 1. First-principles attack on the silent hole

### F1. What the five-family mechanism proves

`thm:mc3-evaluation-core-five-family` (Vol I `chapters/theory/mc3_five_family_platonic.tex:102`) proves MC3 on the evaluation-generated core $\mathrm{DK}^{\mathrm{ev}}_\mathfrak{g}$ for:

| Family | Mechanism | Scope |
|--------|-----------|-------|
| (1) Type A | Asymptotic prefundamentals | $Y_\hbar(\mathrm{sl}_N)$ |
| (2) Type B/C/D | Reflection-equation Shapovalov | twisted affine KM |
| (3) Classical + simply-laced exceptional | Chari-Moura multiplicity-free $\ell$-weights | $E_{6,7,8}$ |
| (4) Non-simply-laced exceptional ($G_2$, $F_4$) | Per-case fundamental $q$-characters | Hernandez 2006 / 2010 |
| (5) Elliptic | Theta-divisor complement | $E_{\rho,\eta}(\mathrm{sl}_N)$ |
| (6) Super-Yangian | Parity-balance | $Y_\hbar(\mathfrak{gl}_{m|n})$ |

The scope excludes: logarithmic $W(p)$, $\mathcal{N}=2$ SCA, cosets beyond GKO/KRW, indefinite non-rational lattice VOAs, roots-of-unity admissible-level quantum groups (`cor:five-family-union-coverage`:649-655).

### F2. Why the $\mathcal{N}=2$ SCA is a genuine hole

The $\mathcal{N}=2$ SCA is a vertex operator superalgebra with four strong generators $\{T, J, G^+, G^-\}$ at conformal weights $\{2, 1, 3/2, 3/2\}$ and central charge $c = 3k/(k{+}2)$. First-principles obstruction to reduction to any of the six families above:

- (1) Type A Yangian: $\mathcal{N}=2$ SCA is not a Yangian; its strong generators are a mixed bosonic/fermionic quadruple, not an $R$-matrix presentation over $\mathrm{sl}_N$.
- (2) Type B/C/D: no reflection equation; the $\mathrm{U}(1)$ current $J$ is central in its Cartan sector, not a reflection generator.
- (3) Chari-Moura: requires an evaluation homomorphism onto a simple Lie algebra, which the $\mathcal{N}=2$ SCA lacks (the $G^\pm$ are fermionic, not in any $\mathfrak{g}$-orbit).
- (4) Non-simply-laced exceptional: irrelevant; no $G_2$ or $F_4$ structure.
- (5) Elliptic: no elliptic modulus in the $\mathcal{N}=2$ SCA unless elliptically deformed (separate object).
- (6) Super-Yangian parity-balance: the $\mathcal{N}=2$ SCA is related to affine $\mathfrak{sl}(2|1)$ via Kac-Todorov (1985), but the parity-balance mechanism of `prop:mc3-super-parity-balance-platonic` applies to $Y_\hbar(\mathfrak{gl}_{m|n})$, not to its DS reduction. The super-Yangian Shapovalov pairing is $\mathfrak{gl}_{m|n}$-specific; post-DS reduction the pairing is quotiented and the parity-balance identity is not preserved verbatim.

Hence the $\mathcal{N}=2$ SCA is NOT a specialization of any five-family proof. It is a genuine silent hole.

### F3. What Vol I inscribes about $\mathcal{N}=2$ SCA Koszulness

`prop:n2-koszulness` at `chapters/examples/n2_superconformal.tex:301` inscribes chiral Koszulness of $\mathrm{SCA}_c$ at generic $c$ via PBW spectral sequence collapse at $E_2$ (Adamovic 1999 free strong generation + `prop:pbw-universality`). The proof is sound but DOES NOT address MC3: Koszulness (bar cohomology concentrated in degree 1) is STRUCTURALLY DIFFERENT from MC3 (thick generation of the Drinfeld-Kohno factorization category $\mathrm{DK}_\mathfrak{g}$ by evaluation-type modules). Koszul = $H^\bullet(B(A))$ degree concentration; MC3 = $\mathrm{thick}(\mathrm{ev\text{-}type}) = \mathrm{DK}$. The two assertions share no proof input.

Hence `prop:n2-koszulness` does not heal the MC3 silent hole. The $\mathcal{N}=2$ SCA needs either (a) its own MC3 mechanism or (b) an explicit statement that MC3 is conjectural for $\mathrm{SCA}_c$.

### F4. Kazama-Suzuki coset as candidate sixth family

The Kazama-Suzuki coset (1989)

$$\mathrm{SCA}_c \simeq \operatorname{Com}\bigl(\mathrm{U}(1),\; \widehat{\mathfrak{sl}}_{2,k} \otimes \psi\bar\psi\bigr)$$

(inscribed at `rem:n2-kazama-suzuki`:183) realizes $\mathrm{SCA}_c$ as the coset of a diagonal $\mathrm{U}(1)$ inside $\widehat{\mathfrak{sl}}_{2,k} \otimes \psi\bar\psi$. Both coset constituents lie in Type A (affine $\mathrm{sl}_2$) + class G (free fermion pair), hence MC3 holds for each constituent via Family (1) + Family (6) (super-Yangian parity-balance at $\mathfrak{gl}(1|1) = $ free fermion). BUT: MC3 does NOT automatically descend to the coset. The obstruction: the branching
$$V_k(\mathfrak{sl}_2) \otimes V(\psi\bar\psi) \;\longrightarrow\; \bigoplus_\lambda \mathrm{SCA}_c \cdot v_\lambda$$
requires that every evaluation-type module of $\mathrm{SCA}_c$ lifts to an evaluation-type module of the ambient tensor product, and conversely that branching preserves the thick-generation status. Neither direction is proved in the literature; Kazama-Suzuki 1989 + Feigin-Semikhatov 2004 establish CHARACTER decomposition but not factorization-category thick generation.

### F5. Adamović coset alternative

Adamović 1999 (arXiv:math/9906048) provides a different coset:
$$\mathrm{SCA}_c \simeq \operatorname{Com}(\widehat{\mathfrak{sl}}_{1|2,k'},\; V_L)$$
for specific lattice VOAs $V_L$ at $k' = -\frac{3}{2} + c/6$. This routes through affine $\mathfrak{sl}(1|2)$ (rank-2 super Lie algebra) and a Feigin-Frenkel style screening presentation. MC3 on this route is likewise OPEN: neither Adamović nor Feigin-Semikhatov 2004 establish the thick-generation condition.

### F6. DS reduction from osp(2|2)

Feigin-Semikhatov 2004 (arXiv:hep-th/0401164) presents $\mathcal{N}=2$ SCA as a DS reduction of affine $\mathfrak{osp}(2|2)$ at a principal odd nilpotent. This routes through the super-Yangian family BUT at DS-quotient: the super-Yangian Shapovalov pairing descends to a DS-quotient Shapovalov pairing whose thick-generation status is not established in print.

### F7. Summary of first-principles scope

$\mathcal{N}=2$ SCA MC3 status is CONJECTURAL. Three candidate mechanisms (Kazama-Suzuki coset branching, Adamović lattice coset, $\mathfrak{osp}(2|2)$ DS reduction) reduce the question to a thick-generation preservation theorem that is not proved. Vol I inscribes Koszulness only. MC3 for $\mathcal{N}=2$ SCA must be stated conditionally.

## Phase 2. Attack: inscribed-but-missing items

The following items are inscribed-but-missing or missing-but-needed.

**A1. Missing:** an inscribed theorem naming the $\mathcal{N}=2$ SCA MC3 status. Current `thm:mc3-full-DK-conjectural` at `mc3_five_family_platonic.tex:571-603` enumerates type-A, non-type-A simple, and sectorwise extension; it does NOT enumerate the silent-non-coverage families (logarithmic $W(p)$, $\mathcal{N}=2$ SCA, cosets, non-rational lattice, roots-of-unity). These appear ONLY in the narrative `cor:five-family-union-coverage` non-coverage clause.

**A2. Missing:** an $\mathcal{N}=2$-specific MC3 conjecture inscribing the Kazama-Suzuki coset route as the intended reduction path with an explicit falsification test.

**A3. Missing:** a Vol I anti-pattern registering the pattern "silent-non-coverage family has Koszulness but not MC3" to prevent conflation.

**A4. Manuscript gap:** `prop:n2-koszulness`:301 is `\ClaimStatusProvedHere` but cites `prop:pbw-universality` by slug. Verification: `grep -rn '\\label{prop:pbw-universality}'` in Vol I — inscribed at `chapters/theory/pbw_koszulness_platonic.tex` (verified present, not phantom).

## Phase 3. Heal (AP266 sharpened-obstruction template)

**Strategy:** Option (b) from mission brief — state `conj:mc3-n2-sca-generic-k-conditional` with explicit reduction to Kazama-Suzuki coset thick-generation, and extend `thm:mc3-full-DK-conjectural` with a silent-non-coverage enumeration clause. Do NOT extend the "five-family" headline to "six-family": the Kazama-Suzuki coset route is not proved; advertising it as a sixth proof mechanism would be AP256 (aspirational-heal status drift).

**Heal inscriptions (Phase 4 manuscript edits):**

1. **New proposition** `prop:n2-sca-koszulness-generic-k` — re-scope the existing `prop:n2-koszulness` banner with explicit citation to Adamović 1999 for generic-$c$ free strong generation. Add `\ClaimStatusProvedElsewhere` attribution for the Adamović input; keep `\ClaimStatusProvedHere` for the PBW collapse step. (This is a clarification, not a new inscription; keep current label.)

2. **New conjecture** `conj:mc3-n2-sca-kazama-suzuki` in `chapters/examples/n2_superconformal.tex`, inscribed as `\begin{conjecture}` with explicit statement: MC3 holds on $\mathrm{DK}^{\mathrm{ev}}_{\mathcal{N}=2}$ conditional on the Kazama-Suzuki coset thick-generation lemma. Provide a falsification test (check thick generation on a concrete weight-by-weight level at $c = 1$, the first generic rational point).

3. **Extend `thm:mc3-full-DK-conjectural`** at `mc3_five_family_platonic.tex:571` with a fourth clause enumerating the five silent-non-coverage families (logarithmic $W(p)$, $\mathcal{N}=2$ SCA, cosets beyond GKO/KRW, indefinite non-rational lattice VOAs, roots-of-unity admissible). Each carries an explicit conditional statement naming the candidate mechanism.

4. **Register AP501** in CLAUDE.md "Koszulness without MC3": silent-non-coverage family where Vol I inscribes chiral Koszulness via PBW + free strong generation (Adamović input) but MC3 is open. Not a failure mode but a scope-discipline pattern: never infer MC3 from Koszulness, nor vice versa.

5. **Register AP502** in CLAUDE.md "Coset MC3 non-inheritance": MC3 on a coset is NOT a corollary of MC3 on the ambient tensor product. Thick generation does not descend automatically under branching; the coset-preservation lemma is a separate theorem.

6. **Update `cor:five-family-union-coverage` proof body** at `mc3_five_family_platonic.tex:657-675` with an explicit sentence naming the Kazama-Suzuki coset route as the candidate reduction path for $\mathcal{N}=2$ SCA, labeled conjectural.

7. **Update CLAUDE.md MC1-4 row** silent-non-coverage enumeration to reference the new `conj:mc3-n2-sca-kazama-suzuki` by name (not just "N=2 SCA").

## Phase 4. Propagation (HZ-11 + AP5 + AP149)

Grep scope:
- Vol I: `grep -rn 'N=2 SCA\|Kazama-Suzuki\|mathcal{N}=2' chapters/ standalone/`
- Vol II: same under `~/chiral-bar-cobar-vol2`
- Vol III: same under `~/calabi-yau-quantum-groups`

Propagation sites (Vol I):
- `chapters/frame/part_ii_platonic_introduction.tex` — prose mention of `N=2 SCA`.
- `chapters/examples/n2_superconformal.tex` — primary home.
- `chapters/theory/mc3_five_family_platonic.tex:650, 669, 689` — silent-non-coverage enumeration.
- `chapters/examples/shadow_tower_extended_families.tex` — check for N=2 SCA mention.

No cross-volume consumer refs to `thm:mc3-full-DK-conjectural` from Vol II/III expected; the theorem is Vol I internal MC3 scope statement.

## Phase 5. Independent verification

Existing compute coverage:
- `compute/lib/n2_superconformal_shadow.py` — 60+ tests on shadow tower, $\kappa$, complementarity, multi-channel structure.
- `compute/tests/test_n2_superconformal_shadow.py` — verified PBW collapse through conformal weight 6.
- `compute/lib/n2_kappa_resolution.py` — Kazama-Suzuki $\kappa$ decomposition.

These verify Koszulness witness (PBW collapse) and $\kappa$ complementarity. They do NOT address MC3 (thick generation). No independent-verification decorator for MC3 on $\mathcal{N}=2$ SCA exists or is required at this time, since MC3 itself is CONJECTURAL.

## Status after heal

- `conj:mc3-n2-sca-kazama-suzuki`: NEW conjecture, inscribed.
- `thm:mc3-full-DK-conjectural`: extended with silent-non-coverage enumeration clause.
- `cor:five-family-union-coverage`: proof body annotated with coset-route reference.
- `prop:n2-koszulness`: unchanged status; Adamović attribution clarified.
- CLAUDE.md AP501, AP502: registered.

The $\mathcal{N}=2$ SCA silent hole is now explicitly scoped, not silent. MC3 status is honestly CONJECTURAL with a named falsification test.

## Appendix. AP block consumed

AP501: Koszulness without MC3.
AP502: Coset MC3 non-inheritance.

AP503-AP520 reserved for future N=2-SCA-swarm extensions (e.g. N=4 small SCA, N=1 super-Virasoro, BP as N=2 degeneration).
