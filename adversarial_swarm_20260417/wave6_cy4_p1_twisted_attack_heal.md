# Wave 6 — CY_4 p_1-twisted Yangian cluster: adversarial attack and heal

Target: Vol III CY_4 p_1-twisted double current algebra cluster.
Primary files: `chapters/theory/en_factorization.tex` §CY_4 (lines ~260-395),
`chapters/theory/cy_to_chiral.tex` §Φ_4 (lines 4502-4701),
`chapters/frame/preface.tex` (lines 570-611), `README.md` L67.

## Phase 1 — falsification

### Finding A (CRITICAL): README L67 scope inflation vs body-conjecture status.

README says: `CY_4 p_1-twisted family | Proved (double current algebra with c(x,y) = ⟨x ∪ y ∪ p_1(T_X),[X]⟩/24; K3 × K3 unobstructed E_4)`.

Body status (en_factorization.tex):
- `conj:cy4-twisted-center` L289: `\ClaimStatusConjectured` (conditional on CY-A_4).
- `prop:e3-max-cy4` L325: `\ClaimStatusConditional{}\ (conditional on CY-A_4)` — the cascade terminates at E_3, NOT E_4.
- `conj:cy4-en-stabilisation` L347: `\ClaimStatusConjectured`.

Both the "Proved" status and the "E_4" level are wrong. The correct summary is Conjectural,
cascade terminates at E_3, and the p_1-twist is the OBSTRUCTION (per AP-CY46, AP185) to E_4,
not evidence of E_4 structure. Scope inflation confirmed.

### Finding B (CRITICAL): Numerical inconsistency between preface (1/24) and body/engine (1/12).

Preface L605-607:
```
c(x, y) = (1/24) ⟨x ∪ y ∪ p_1(T_X), [X]⟩
```

Body `cy_to_chiral.tex:4651`: `Pontryagin shift ∫p_1 / 12 = -15` at sextic (∫p_1 = -180).
Engine `compute/lib/cy4_p1_family_phi_4.py` L232-237:
```python
"""The p_1/12 Pontryagin shift to the central charge.
From Hirzebruch normalisation A-hat_2 = p_1/12 ...
For the sextic: int p_1 = -180, shift = -180/12 = -15."""
```

Arithmetic check at sextic:
- 1/24 × (-180) = -7.5 (non-integer, inconsistent with integer central-charge shift).
- 1/12 × (-180) = -15 (integer, matches engine test `c_eff = 2591`).

The preface normalisation coefficient disagrees with the body, the compute engine,
and the `c_eff = 2606 - 15 = 2591` value that is tested. The docstring cites
"A-hat_2 = p_1/12" — this is a **MISSTATEMENT**: the Hirzebruch A-hat series is
A-hat = 1 - p_1/24 + (7p_1^2 - 4p_2)/5760 - ..., so the A-hat degree-4 coefficient is
-p_1/24. The factor of 2 between 1/24 (A-hat) and 1/12 (central-charge shift)
is the standard doubling from "2 real scalars per complex direction" (two transverse
polarisations in the chiral OPE). The physical normalisation is
`shift = p_1/12 = 2 · (A-hat_1 coefficient)`; the preface formula using 1/24 is
the A-hat coefficient, not the OPE shift. Either fix or consistent narrative required.

Heal: change the preface formula to use the physical 1/12 normalisation, align all
three sites.

### Finding C (CRITICAL): "N(X) = 0, unobstructed E_4" for K3 × K3 topologically false.

Preface L609-611:
```
for X = K3 × K3, N(X) = 0 and the E_4 structure is unobstructed
by the Hopf decomposition S^4 = S^2 × S^2.
```

Three problems:
1. `N(X)` is never defined anywhere in Vol III (grep confirms). Undefined symbol
   in a load-bearing preface sentence.
2. Body table `en_factorization.tex:309`:
   `K3 × K3 | c_2 = 48 | p_1 = -96 | Z-twisted`.
   So K3 × K3 is `Z-TWISTED` per the body and per the Pontryagin arithmetic
   (p_1(K3) = c_1^2 - 2c_2 = 0 - 48 = -48; Whitney sum p_1(K3 × K3) = -48 + -48 = -96
   in homology under the diagonal). Nonzero twist.
3. `S^4 ≠ S^2 × S^2` as manifolds: H^2(S^4) = 0 vs. H^2(S^2 × S^2) = Z^2, Euler char
   4 vs. 2. The "Hopf decomposition" is the Pontryagin-Thom splitting of the Euler
   class at the rational-homotopy level, not a diffeomorphism. It does NOT imply
   E_4 structure is unobstructed on K3 × K3.
4. Even the product framing argument is misapplied: K3 is E_2-chiral native
   (h-twisted K-theory / Mukai vector bundle); the product K3 × K3 inherits
   at best E_2 × E_2 → E_2 (Dunn in the non-p_1-twisted sector). The nonzero
   p_1(K3 × K3) = -96 is the twisting obstruction, not the trivialisation.

Heal: delete the "N(X) = 0, unobstructed E_4" sentence. Replace with a correct
summary noting p_1(K3 × K3) = -96 (nonzero) gives the Z-twist, matching the
en_factorization body.

### Finding D: "Double current algebra" phrase collides with AP-CY46.

AP-CY46 (CLAUDE.md L583) says: "never write E_4 Yangian or CY_4 Yangian. Use
p_1-twisted double current algebra." The body is consistent. The README L67
parenthetical "K3 × K3 unobstructed E_4" VIOLATES AP-CY46 twice — it writes
"E_4" where "p_1-twisted double current algebra (E_1 with E_2-braided Drinfeld
center)" is required.

### Finding E: Cocycle degree and bilinearity.

For a CY_4 with [X] ∈ H_8(X, Z), the pairing ⟨x ∪ y ∪ p_1, [X]⟩ requires
deg(x) + deg(y) + 4 = 8, hence x, y ∈ H^2(X, Z). The cocycle is
c : H^2(X) ⊗ H^2(X) → Q (or Z if the normalisation factor is absorbed).
Preface does not specify the domain; the reader must infer. Minor hygiene.

### Finding F: 7d hCS realization.

Grep for "7d hCS" returns nothing in the Vol III manuscript. The claim in the
user prompt ("7d hCS realization") is not inscribed in Vol III. Either this is
aspirational and should be stated as a conjecture, or it belongs to a future wave
(Costello-Yamazaki 6d hCS + Omega_eps on 1d real = 7d is the likely target; not
yet written). Fact of absence: no manuscript claim to attack.

### Finding G: AP185 framing discipline.

Introduction L1083-1084 correctly writes: "No native CY_4 Yangian: the p_1 ∈
π_4(BU) = Z twist breaks the spectral parameter shift symmetry." This honours
AP185 (obstruction GROUP, not structure). The en_factorization body likewise
honours AP185. **The preface L602-611 and README L67 are the only sites that
violate AP185.** Heal is localised.

### Finding H: κ_ch at K3 × K3 cross-check.

CLAUDE.md says CY_4 stratification: "CY_4 sextic(2), CY_5 generic(0)". K3 × K3
is CY_4 but non-sextic. By Hodge supertrace Xi(K3 × K3) = χ(O_{K3 × K3}) =
χ(O_K3)^2 = (1 - 0 + 1)^2 by Kunneth? Actually χ(O_K3) = 1 - 0 + 1 = 2, so
χ(O_{K3 × K3}) = 4. Then κ_ch(K3 × K3) = χ(O)/2 = 2 per thm:kappa-hodge-supertrace.
This is independent of the p_1-twist (the twist is a cocycle deformation, not a
κ_ch change). Consistent; no edit needed.

## Phase 2 — heal

Three surgical edits in Vol III:

1. **README L67**: change "**Proved**" to "**Conjectural**", remove the
   "K3 × K3 unobstructed E_4" clause, replace with the E_1 + E_2-Drinfeld-center
   Z-twist description matching en_factorization body.

2. **preface.tex L599-611**: (a) replace the 1/24 cocycle coefficient with the
   physical 1/12 Pontryagin-OPE shift matching the body and engine;
   (b) delete the "N(X) = 0 ... unobstructed E_4" sentence. Replace with a
   concise statement matching the en_factorization table (Z-twisted for
   K3 × K3, trivial for T^8).

3. **No change** to en_factorization.tex body — it already honours AP185,
   AP-CY46, and conjectural status.

No commit.
