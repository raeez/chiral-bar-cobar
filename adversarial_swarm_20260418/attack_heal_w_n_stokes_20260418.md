# Wave W_N-Stokes attack-and-heal (2026-04-18)

Target: Vol I CLAUDE.md Theorem Status row 611 — "W_N Stokes count: DISCOVERED. Stokes rays for W_N KZ = 4N-4 (linear in N). W_2: 4. W_3: 8. Poincaré rank = 2N-2."

Verdict: **COMPUTATION CORRECT; EPISTEMIC LABEL OVERCLAIMED.** Downgraded "DISCOVERED" to "COMPUTED via standard irregular-sing theory (ProvedElsewhere)" with per-step primary-source attribution. One new anti-pattern AP1301 inscribed.

---

## Section 1. Location and prior-art check

### Manuscript locations

| File | Line | Role |
|---|---|---|
| `chapters/theory/ordered_associative_chiral_kd.tex` | 9985-9993 | Primary inscription `rem:stokes-wN-monograph` (with Boalch/JMU convention pointer) |
| `standalone/survey_modular_koszul_duality_v2.tex` | 4865-4873 | Cross-reference under "Stokes geometry" |
| `standalone/ordered_chiral_homology.tex` | 5372 | N=2 specialisation (4 Stokes rays at $\pi/2$-multiples) |
| `main.tex` | 866 | One-line abstract mention (Virasoro, 4 rays) |
| `FRONTIER.md` | F32, lines 823-827 | Programme ledger |
| `CLAUDE.md` | 611 | Status-table row (target of this heal) |

### Engine

`compute/lib/irregular_kz_stokes_virasoro_engine.py` computes the $N=2$ case from first principles: Poincaré rank 2, 4 Stokes rays at $\theta = \pi/4, 3\pi/4, 5\pi/4, 7\pi/4$, 4 anti-Stokes rays at $\theta = 0, \pi/2, \pi, 3\pi/2$. Companion `compute/tests/test_irregular_kz_stokes_virasoro_engine.py` asserts $2 \cdot r_{\text{Poincaré}} = 4$ numerically.

### Prior audit

`adversarial_swarm_20260417/wave7_wN_stokes_g2_decomp_attack_heal.md` (2026-04-17) verified the Stokes-count claim from first principles step by step and concluded "ACCEPT with optional one-line convention pointer inserted into the remark." The convention pointer was inserted at `rem:stokes-wN-monograph`. Prose of the inscribed remark is thus honest at the manuscript level.

---

## Section 2. First-principles verification chain

The derivation is a four-step classical chain. Each step is ProvedElsewhere in standard primary literature.

### Step (a). $W_N W_N$ OPE pole order = $2N$

$W_N$ has conformal weight $N$. The OPE of two primaries of weight $h$ contains the identity channel with highest singularity $\langle \phi(z) \phi(w) \rangle \sim B (z-w)^{-2h}$. Hence $\langle W_N(z) W_N(w) \rangle \sim B_N (z-w)^{-2N}$.

Primary sources:
- Belavin, Polyakov, Zamolodchikov, "Infinite conformal symmetry in two-dimensional quantum field theory", Nucl. Phys. B 241 (1984) — two-point function of primaries.
- Zamolodchikov, "Infinite additional symmetries in two-dimensional conformal quantum field theory", Teor. Mat. Fiz. 65 (1985) — explicit $W_3 W_3$ OPE with pole $(z-w)^{-6}$.

Verification: $N=2$ (Virasoro): $T T$ OPE pole $(z-w)^{-4}$ matches $c/2$-coefficient (quartic pole in $TT$ canonical). $N=3$ (W_3): $W_3 W_3$ OPE pole $(z-w)^{-6}$ from Zamolodchikov 1985 Table. $N=4$ (W_4): pole $(z-w)^{-8}$.

### Step (b). d-log absorption gives connection-form pole $2N-1$

The KZ-type connection one-form on the configuration space $\text{Conf}_n(\bC)$ is $\omega = \sum_{i<j} r_{ij}(z_i - z_j) \, d \log(z_i - z_j)$ or equivalently $r(z) \, dz$ after absorbing one pole. Starting from $\langle W_N W_N \rangle \sim B_N (z-w)^{-2N}$, the $d$-log form carries pole order $2N - 1$.

Primary source: Arnold, "The cohomology ring of the coloured braid group", Mat. Zametki 5 (1969) — d-log basis on configuration spaces.

### Step (c). Poincaré rank $r = (\text{pole order}) - 1 = 2N - 2$

Standard definition: for a meromorphic connection $dY = A(z) Y \, dz$ with $A$ having a pole of order $p \geq 1$ at $z_0$, the Poincaré rank is $r = p - 1$.

Primary sources:
- Wasow, *Asymptotic Expansions for Ordinary Differential Equations* (1965), Chapter III.
- Sibuya, *Global Theory of a Second Order Linear Ordinary Differential Equation with a Polynomial Coefficient* (1975).

At $N = 2$: $r = 2$. At $N = 3$: $r = 4$. At $N = 4$: $r = 6$.

### Step (d). Stokes ray count $= 2r$ (generic)

For a Poincaré-rank-$r$ irregular singular point with leading eigenvalues $\lambda_i(z) \propto z^{-r}$, the anti-Stokes directions are the zeros of $\text{Re}(\lambda_i - \lambda_j)(\theta)$ in $[0, 2\pi)$. Generically there are $2r$ such directions. Under the dominant convention ("anti-Stokes rays" or equivalently "Stokes sectors"), the Stokes ray count is $2r$.

Primary sources:
- Boalch, "Symplectic manifolds and isomonodromic deformations", Adv. Math. 163 (2001), Lemma 2.1 — canonical $2r$ count.
- Jimbo, Miwa, Ueno, "Monodromy preserving deformation of linear ordinary differential equations with rational coefficients I", Physica D 2 (1981).
- Hertling, Sabbah, various monographs on isomonodromic deformations.

Convention caveat: "Stokes rays" admits three inequivalent usages in the literature — (i) anti-Stokes rays (where a formal multiplier acts non-trivially; $2r$ generic); (ii) Stokes sectors (connected components of the complement; $2r$); (iii) active rays (those carrying a non-trivial Stokes multiplier; could be fewer than $2r$ in non-generic settings). The $4N - 4$ count matches (i)/(ii) under genericity, which is the convention inscribed at `rem:stokes-wN-monograph`.

### Numerical verification

| $N$ | Pole | Rank $r$ | Stokes rays $2r$ |
|---|---|---|---|
| 2 (Vir) | 4 | 2 | 4 |
| 3 (W_3) | 6 | 4 | 8 |
| 4 (W_4) | 8 | 6 | 12 |
| 5 (W_5) | 10 | 8 | 16 |

Linear in $N$: $4N - 4 = 4(N - 1)$. At $N = 2$ (Virasoro), Poincaré rank 2 matches the direct Fuchs / Jimbo-Miwa-Ueno analysis; the engine `irregular_kz_stokes_virasoro_engine.py` confirms the 4 Stokes rays at $\pi/4$-multiples via explicit $\exp(-c/(4z^2))$ asymptotic analysis.

---

## Section 3. Epistemic audit: "DISCOVERED" vs "COMPUTED"

### Is $4N - 4$ a programme discovery?

**No.** Once the four classical steps (a)-(d) are named, the formula $4N - 4$ follows in one line:

$$\text{Stokes rays} = 2 \cdot \text{Poincaré rank} = 2(2N - 2) = 4N - 4.$$

The derivation uses (a) BPZ two-point function, (b) Arnold d-log, (c) Wasow/Sibuya Poincaré rank definition, (d) Boalch/Jimbo-Miwa-Ueno Stokes theory. None of these steps is programme-novel.

### What IS programme-novel?

The IDENTIFICATION of Poincaré rank $2N - 2$ with the $\cW_N$ chiral algebra at degree 2 is programme-adjacent: the chain connects the $W$-algebra's OPE pole to the irregular-singular structure of the degree-2 KZ connection. This identification is honest programme content — but it is a one-line corollary of the pole-order step (a).

### Comparison with AP280 sibling

AP280 catches three-step epistemic inflation (remark → standalone → headline). The present case is a sibling where the inflation is shorter — the manuscript inscription at `rem:stokes-wN-monograph` is HONEST (it names Boalch and JMU, lists the four steps, acknowledges the convention caveat), and the standalone inscription at `survey_modular_koszul_duality_v2.tex` is also honest. Only the CLAUDE.md status-table banner "DISCOVERED" was inflated. This is a new anti-pattern: **AP1301 (Classical-chain computation masquerading as "DISCOVERED")**.

### Correct epistemic label

`\ClaimStatusProvedElsewhere` at the level of the manuscript inscription, with per-step attribution to BPZ 1984 / Zamolodchikov 1985 / Arnold 1969 / Wasow 1965 / Boalch 2002 / JMU 1981. The CLAUDE.md status-table label should read "COMPUTED via standard irregular-sing theory (ProvedElsewhere)".

---

## Section 4. Connection to shadow tower $C_A = s(s+1)$ extrapolation (AP276)

User's fifth question: is the linear-in-$N$ pattern $4N - 4$ related to the AP276 two-point extrapolation $C_{\cW^{(s)}} = s(s+1)$?

**Structurally distinct.** The two patterns come from different sectors of the same algebra family:

- Stokes count $4N - 4 = 4(N - 1)$ is LINEAR in $N$ and comes from the Poincaré rank $2N - 2 = 2(N - 1)$, which is governed by the PARENT algebra's maximum spin $N$ (the spin-$N$ generator's OPE pole).
- Shadow-tower $C_{\cW^{(s)}} = s(s+1)$ (conjectural, AP276) is QUADRATIC in $s$ and indexed by the SPIN-$s$ primary inside principal $\cW_N$, reflecting the Riccati ratio $12 - 30/(n+1)$ at each spin lane.

The two patterns are orthogonal: Stokes count is a property of the full connection (all spins summed), while $C_{\cW^{(s)}}$ is per-spin-lane. No new anti-pattern on this axis; the AP276 falsification test (compute $W_4$ W_4-line coefficient, check against $s(s+1)$, $6(s-1)$, $4s^2 - 4s + 6$, $4s$) is independent of the Stokes count.

---

## Section 5. Heals applied (minimal)

### Heal 1. CLAUDE.md row 611 downgrade

"W_N Stokes count: DISCOVERED" → "W_N Stokes count: COMPUTED via standard irregular-sing theory (ProvedElsewhere)".

Row body expanded with per-step primary-source attribution (BPZ 1984, Zamolodchikov 1985, Arnold 1969, Wasow 1965, Sibuya 1975, Boalch 2002, JMU 1981, Hertling-Sabbah 2005) and the Wave-7 audit cross-reference.

### Heal 2. AP1301 inscription

New anti-pattern at CLAUDE.md tail, Wave W_N-Stokes section. Short form: CLAUDE.md status-table banner "DISCOVERED" (or "IDENTIFIED", "NEW INVARIANT") masking a 3-5 step classical chain derivation. Distinct from AP280 (three-step inflation at manuscript level) and AP272 (unstated cross-lemma via folklore citation). Counter: verify derivation is not a classical chain; if it is, downgrade to "COMPUTED (ProvedElsewhere)" with per-step primary-source attribution.

### Heals NOT required

- The inscribed remark `rem:stokes-wN-monograph` at `ordered_associative_chiral_kd.tex:9985-9993` is already honest (convention pointer inserted via Wave-7 2026-04-17 heal). No change.
- The engine `compute/lib/irregular_kz_stokes_virasoro_engine.py` correctly attributes the computation and links to primary-source conventions. No change.
- FRONTIER.md F32 is descriptive ("Stokes rays = 4N-4 for the W_N KZ connection at degree 2") without the "DISCOVERED" banner. No change.
- The standalone `survey_modular_koszul_duality_v2.tex:4866-4870` inscribes the result with explicit per-step derivation. No change.

---

## Section 6. Cross-volume propagation check (AP5)

### Vol II

`~/chiral-bar-cobar-vol2`: no inscription of the W_N Stokes count claim in the manuscript (the result is Vol-I-specific content at degree 2 of the ordered bar). Vol II has `thm:irregular-singular-kzb-regularity` at `chapters/theory/curved_dunn_higher_genus.tex` (JMU-irregular-singular KZB on $\overline{\cM}_{g,n}$), which is a separate result at the higher-genus KZB layer. No propagation required.

### Vol III

`~/calabi-yau-quantum-groups`: no W_N Stokes count inscription. No propagation required.

---

## Section 7. Summary verdict

- Computation $4N - 4 = 4(N - 1)$ is CORRECT.
- Manuscript inscription at `rem:stokes-wN-monograph` is HONEST (all four classical steps + convention pointer + primary-source attributions in the Wave-7 audit note).
- CLAUDE.md status-table banner "DISCOVERED" was OVERCLAIMED; the derivation is a standard four-step classical chain.
- Heal: CLAUDE.md row 611 downgraded to "COMPUTED via standard irregular-sing theory (ProvedElsewhere)" with per-step primary-source attribution.
- New anti-pattern AP1301 inscribed.
- No manuscript / engine / standalone changes required.

Author: Raeez Lorgat. No AI attribution. Audit completed 2026-04-18.
