# G3 Attack

## 1. Executive verdict
- PROVED affine KM topologisation is under-evidenced: no explicit homotopy is supplied.
- WEIGHT-COMPLETED class M is not original-complex class M; keep F3 OPEN.
- E_infty tower is conditional unless every `G^(n)` primitive is constructed.
- Heptagon equivalence is INSCRIBED, not verifiable from supplied readings.
- Holography scope is only the named non-log `C_2`-cofinite landscape.

## 2. Question-by-question audit

**Q1.** Attack: the supplied proof does not write the requested homotopy. PIR:1149-1151 says Sugawara Dirichlet topologises and `[L_sug, bar-partial]=0`; that is invariance/centrality, not `[Q,G]=partial` or a homotopy inverse. Current status: PROVED affine KM by PIR:252, but the evidence lacks the explicit `G`.

**Q2.** WEIGHT-COMPLETED class M is weaker than original-complex class M. PIR:252 says `prop:bv-bar-class-m-weight-completed` is proved but original-complex chain-level class M is CONJECTURAL; PIR:715 names F3 OPEN. The files do not decide technical gap versus obstruction; they only give the path: half-BRST plus MC5.

**Q3.** The tower is not evidenced as an unconditional theorem for all `N`. PIR:254 states the implication: higher-spin Casimirs inner with `G^(n)` primitives imply `E_{N+1}`. PVPI:69 calls `W_infty` an operadic horizon. Unless the files construct every `G^(n)`, status should be CONDITIONAL finite-stage, ASPIRATIONAL at `W_infty`.

**Q4.** Cannot list seven faces from supplied readings. PIR:555 gives only “seven equivalent presentations,” naming Drinfeld-centre and derived-AG faces; PVPI:25 says 5 chain plus 2 cohomological. Costello-Gwilliam factorisation and Dimofte/D|T|N slab-bimodule are adjacent evidence (PIR:1012; PVPI:155,188), not an equivalence proof here.

**Q5.** The “standard landscape” is named, not defined intrinsically: affine KM, principal `W_N`, Virasoro, irrational cosets (PIR:557; PVPI:77). No supplied line includes non-principal or subregular `W`-algebras. Therefore inclusion of subregular/non-principal `W` is ASPIRATIONAL unless separately proved.

**Q6.** W(p) retraction is correct. PIR:711 says `thm:tempered-stratum-contains-wp` was downgraded ProvedHere -> Conjectured because Zhu-bounded-Massey fails, citing Gurarie, *Logarithmic Operators in Conformal Field Theory*, and Flohr, *On Fusion Rules in Logarithmic Conformal Field Theories*. Correct route: direct Adamovic-Milas character-amplitude bound; no supplied salvage proof.

## 3. Retraction candidates
- Theorem P11 / topologisation proof (PIR:1149-1151): retract “homotopy-level” until `G` and `[Q,G]=partial` are written.
- `e_infinity_topologization.tex`, handle unknown in supplied readings (PIR:254): downgrade to conditional on `G^(n)` primitives.
- Universal Celestial Holography scope (PIR:557): exclude subregular/non-principal `W` unless proved.
- `thm:tempered-stratum-contains-wp`: keep CONJECTURED (PIR:711).

## 4. Aspirational vs. proved claims table
| Claim | Current status | Evidence | Recommended status |
|---|---|---|---|
| Affine KM topologisation | PROVED | PIR:252; weak P11 evidence | PROVED only with explicit homotopy |
| Class M original complex | CONJECTURED/OPEN | PIR:252,715 | CONJECTURED |
| `W_N/W_infty` tower | INSCRIBED/horizon | PIR:254,557; PVPI:69 | CONDITIONAL; `W_infty` ASPIRATIONAL |
| Heptagon equivalence | INSCRIBED | PIR:555; PVPI:25 | UNVERIFIED from supplied readings |
| Universal landscape | PROVED named scope | PIR:557; PVPI:77 | PROVED only for listed families |

## 5. Recommended follow-up
- Write the affine KM chain homotopy explicitly.
- Separate completed and original class M statements.
- Install finite-`N` `G^(n)` existence checks.
- Put all seven heptagon faces in one theorem.
- Define “standard landscape” extension criteria.
