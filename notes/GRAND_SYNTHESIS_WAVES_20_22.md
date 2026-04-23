# Grand Synthesis — Waves 20 through 22

**Compiled**: 2026-04-20. **Author**: Raeez Lorgat.
**Scope**: Structural synthesis of the inscriptions, falsifications, and hidden-structure heals produced across Waves 20, 21, and 22 (≈ 30 agent-rounds).
**Companion documents**: `notes/ADJUDICATION_LEDGER_WAVES_14_TO_19.md` (prior adjudication); `appendices/first_principles_cache.md` (confusion-pattern registry).

---

## The five-theorem identity at the centre

The chiral bar–cobar adjunction $\Omega^{\mathrm{ch}}_X \dashv B^{\mathrm{ch}}_X$ on factorisation $\mathcal D$-modules over $\overline{\mathcal A_2}$ generates Theorems A–H as successive derived evaluations along the tower $\{\pi_0,\ D^{\mathrm{co}}/D^{\mathrm{ctr}},\ \mathrm{tr},\ \int_{\overline{\mathcal M_g}},\ \mathrm{RHom}\}$. The climax theorem (`thm:unified-five-theorem-identity`) in `chapters/theory/chiral_climax_platonic.tex` names this as one statement with five shadows — A (adjunction), B (Positselski), C (centre complementarity), D (genus-ladder obstruction), H ($\{0,1,2,d\}$ concentration).

## Octachotomy closure of bar–cobar

The global scope of strict chain-level bar–cobar inversion now closes at codim 3 across eight ambients:
1. fibrewise generic
2. single-monodromy-refined
3. bi-unipotent Malcev (on wall-of-walls $H_i \cap H_j$)
4. tri-unipotent Malcev (on triple intersections)
5. weight-completed coderived
6. $A_\infty$-corrected
7. $(\infty,1)$-categorical $\mathrm{Perf}(\overline{\mathcal A_2})$
8. chiral-Kontsevich-formal on Koszul locus

**Falsification (W22.2).** Igusa transversality at all admissible Heegner triples is false; the first non-empty admissible triple $(3,4,7)$ is realised by $[E_{\sqrt{-3}} \times E_{\sqrt{-7}}]$ with tri-commuting $\mathfrak{sl}_2^{\oplus 3}$-triples. Heptachotomy → octachotomy.

**Reciprocity (W22.1).** Compatibility data between chain-level and $(\infty,1)$-ambients forms the $\infty$-groupoid
$$\mathrm{Data}(A) \simeq B\mathrm{Aut}^h_{L_\infty}(\mathfrak g^{\infty,1}_A)$$
so the ambient-chain is canonical, not chosen. For $\mathbf H_{\Delta_5}$ this specialises to $\widehat{\mathfrak{grt}}_1 / \mathrm{ob}^{\mathrm{GN}}$.

**Formality (W22.3).** Chiral Kontsevich $L_\infty$-quasi-iso $T^{\mathrm{poly}}_{\mathrm{ch}}(\overline{\mathcal A_2})|_{U^{\mathrm{adm}}} \xrightarrow{\sim} \mathrm{ChirHoch}^\bullet(\mathbf H_{\Delta_5})|_{U^{\mathrm{adm}}}$ unconditional on the Koszul locus $U^{\mathrm{adm}} = \overline{\mathcal A_2}\setminus\bigcup_{n\,\mathrm{adm}} H_n$, obstructed on each admissible $H_n$ exactly by the Malcev-ladder cocycle $\mathrm{gr}_n^{\mathrm{Malcev}}$.

## Hochschild: sharp concentration, explicit cocycle, CY-ladder

$\mathrm{ChirHoch}^\bullet(\mathbf H_{\Delta_5})$ is now **sharp**:
- Vanishing for $k \ge d+1 = 4$ on CY-3 inputs (W21.5 `thm:chirhoch-above-degree-d-vanishes`).
- Degree-3 cocycle $\chi_3 = {:}T\partial T{:} - (1/4)\partial^3 T + \hbar\cdot\mathrm{qt}(J^{(3)})$ paired against $e_3^{\mathrm{K3}\times E}$ gives the explicit Siegel-Eisenstein period (W22.4)
$$\langle[\chi_3], [e_3^{\mathrm{K3}\times E}]\rangle_{\Phi_3} \;=\; 2\,\mathrm{Vol}(E)\cdot(2\pi i)^3 \;=\; \chi(\mathcal O_{\mathrm{K3}})\cdot\mathrm{Res}_{s=1/2}\bigl[E_5^{(2)}(Z,s)\bigr]\big|_{K(1)}.$$

**Four disjoint verification paths** (W21.4, W22.6): CoHA Casimir (Schiffmann–Vasserot), Igusa $\Phi_{10}^{-1}$ (Oberdieck reduced DT), elliptic-volume rigidity (Kontsevich formality degeneration), Kuznetsov relative HPD over $E$ via K3 as Kuznetsov component of cubic fourfold.

**Cross-volume propagation (AP5).** Stale $4\mathrm{Vol}(E)$ in Vol III `hochschild_calculus.tex:590` → $2\mathrm{Vol}(E)$ synced to corrected Vol I value (factor-of-2 Mukai double-count caught in W21.4 audit).

**CY-4 conditional extension (W22.5).** `conj:chirhoch-CY4-conditional` in `hochschild_cohomology.tex`: under existence of $\Phi_4$ (blocked by Kapustin–Rozansky–Saulina 3d/4d dichotomy at framework level), $\mathrm{ChirHoch}^k(\Phi_4(X_4)) = 0$ for $k \ge 5$, $\ne 0$ at $k = 4$ when $\chi(\mathcal O_{X_4}) \ne 0$. K3×K3 test case ($\chi = 4$) triangulated via Cao–Kool–Monavari DT-4 + Nekrasov 8d + elliptic-genus product $\phi_{0,1}^2$.

## Five-archetype landscape

| Archetype | Witness | $c$ / $k$ | $\kappa + \kappa^!$ | $r_{\max}$ |
|-----------|---------|-----------|----------------------|------------|
| **G** | Heisenberg $\mathcal H_k$ | $k$ | $0$ | $2$ |
| **L** | affine Kac–Moody $V_k(\mathfrak g)$ | $\dim(\mathfrak g)(k+h^\vee)/(2h^\vee)$ | $0$ | $3$ |
| **C** | $\beta\gamma$ system | $-1$ | $0$ | $4$ |
| **M** | Virasoro $\mathrm{Vir}_c$ | $c/2$ | $13$ | $\infty$ |
| **B** | BKM crown $\mathbf H_{\Delta_5}$ | — | $8$ | $\infty$ |

BKM crown satisfies $\hbar^2 \cdot K^{\kappa_{\mathrm{ch}}} = -1$ at $(K, \hbar^2) = (8, -1/8)$, $\kappa_{\mathrm{BKM}} = 12$. $\mathsf W$-extensions at $\{250/3, 98/3\}$ sit on the M-row.

## Pentagon coboundary tower

$\phi^{(n)}$ inscribed through $n = 24$ (Waves 20, 21, 22):
- Padovan dimension $d_n = d_{n-2} + d_{n-3}$ with seeds $(d_1, d_2, d_3) = (1, 0, 1)$.
- Brown motivic MZV basis provides the Hodge filtration.
- Hardy–Ramanujan $p_{24}(\lceil n/2\rceil)$ controls the Borcherds leg asymptotic.

**Depth-threshold table**:

| depth $d$ | first entry $n$ | generating MZV |
|-----------|-----------------|----------------|
| $4$ | $12$ | $\zeta(3,3,3,3)$ |
| $5$ | $15$ | $\zeta(3,3,3,3,3)$ |
| $6$ | $18$ | $\zeta(3,3,3,3,3,3)$ |
| $7$ | $21$ | $\zeta(3,3,3,3,3,3,3)$ |
| $8$ | $24$ | depth-8 first primitive |

At $n = 24$: $p_{24}(12) = \chi(\mathrm{Hilb}^{12}(\mathrm{K3})) = 10{,}914{,}317{,}934$, coincidence with Niemeier $A_2^{12}$ umbral moonshine. Scope double-conditional above $n = 20$ (Zagier–Hoffman depth-reduction + Broadhurst–Kreimer empirical depth-distribution).

## Enriques BKM $\mathfrak g_{\Delta_5}^{\mathrm{Enr}}$

- Cartan lattice $E_8(-1) \oplus \mathrm{II}_{1,1}$, signature $(1, 9)$, rank 10.
- Metaplectic Siegel weight $5/2$ on $\widetilde{K(2)} \subset \widetilde{\mathrm{Sp}_4}$.
- Borisov–Libgober halving $\phi^{\mathrm{En}}_{0,1} = (1/2)\phi^{\mathrm{K3}}_{0,1}$ (orbifold twisted sector vanishes because $\iota$ is fixed-point-free).

**$M_{12}$-moonshine reconstructed** (Waves 20, 21, 22):
- Direct identification falsified at $f_{\mathrm{En}}(0,1) = 10$.
- Virtual-character decomposition via Persson–Volpato point-stabiliser inclusion $M_{12} \hookrightarrow M_{24}$ as centraliser of the Enriques involution.
- Explicit 12-class × 10-coefficient twining table at discriminants $D \in \{-1, 0, 3, 4, 7, 8, 11, 12, 15, 16, 19, 20\}$.
- **Mass formula** (W22.8 `thm:bkm-enriques-m12-mass-formula`): three simultaneous identities — trace-sum over $\iota$-commuting classes; sign-alternating positivity at threshold $D_0 = 0$ with Mersenne-locus exception $\{2^k - 1\} \cup \{47, 55, \ldots\}$; Plancherel norm identity.

## Structural falsifications healed

1. **Conway $V^{s\natural}$** (W20.2): NOT a fifth independent $\Psi$-image. Duncan 2007 *Duke Math. J.* 139 constructs $V^{s\natural} = A(\Lambda_{24})^+ \oplus A(\Lambda_{24})^{\mathrm{tw},+}$ as $\mathbb Z/2$-orbifold of the 24-generator fermionic VOA on the Leech lattice. The commutative orbifolding diamond $\{V_{\Lambda_{24}}, V^\natural, V_{\Lambda_{24}}^s, V^{s\natural}\}$ locates $V^{s\natural}$ as the $\mathbb Z/2$-super-twin of $V^\natural$ on the **Monster** row; $(K, \hbar^2) = (2, -1/2)$ inherited, not independent.
2. **Absolute Kuznetsov HPD on K3×E** (W22.6): blocked by Fano obstruction ($\omega_Y \simeq \mathcal O_Y$ trivial; no Lefschetz twist). Replaced by relative HPD over $E$ via K3 as Kuznetsov component of cubic fourfold (Kuznetsov–Markushevich 2009; Addington–Thomas 2014).
3. **$8^{129}$** (W22.9): NOT a Hopf-quotient dimension. Correct interpretations: (a) $\dim \mathfrak b^{\mathrm{re},+}_{\zeta_8}$, the real-root positive-Borel sub-Hopf-algebra dimension; (b) $|\Lambda^{\mathrm{re}}|$, the Kerler–Lyubashenko non-semisimple-MTC projective-index cardinality at $\ell = 8$. Arithmetic gap: $d(N_\star) = 63$ has no integer $N_\star$ in the truncation sequence $(d(1), d(2), d(3)) = (2, 22, 238)$.
4. **$\Psi$-surjectivity** (W20.9): 22 non-Leech Niemeier BKMs (e.g. $24A_1$ at signature $(25,1)$) are genuine counterexamples. Correct scope: $\Psi|_{d \in \{2, 3\}}$ surjects onto CY-$d$-derivable reflective BKMs. Three-path verification of the $24A_1$ counterexample: lattice-rank signature mismatch; Serre-parity / Caldararu obstruction on $\HH_0$; modular weight collision.
5. **Fricke LDP $\sigma_k^2$** (W20.8): density-curvature vs inverse-density conflation. Correct: $\sigma_k^2 = \pi/(2\sin^2\theta_k^*)$ (Bayes formula via Sanov), not $(\pi^2/2)\cos^{-2}\theta_k^*$. Newton–Thorne 2021 makes the effective rate $\delta = 1/4 - \varepsilon$ unconditional for $f_{16}$.
6. **Umbral Niemeier at $N = 6$** (W20.5): $4A_5$ is not a Niemeier root system; $A_5^4 D_4$ is. The $D_4$ absorbs the rank deficit.

## Gerbes and quantisation

- **$\mu_8$-gerbe** (W20, W21): chain-level Čech 2-cocycle $F_{ij} = [\Phi_{10}/\eta^{24}]^{1/8}$-ratio on Igusa fundamental-domain cover of $\overline{\mathcal A_2}\setminus(H_1 \cup H_4)$; $\delta F = 0$.
- **$\mu_{16}$-refinement on $H_4$** (W21): $G_{ij} = [\Delta_5/\eta^{12}]^{1/8}$-ratio on metaplectic cover of $\overline{\mathcal A_2}\setminus H_1$, $G_{ij}|_U^2 = F_{ij}$; Bockstein class order 16 via Bruinier $\mathrm{ord}_{H_4}(\Delta_5) = 2$ + metaplectic doubling.
- **GRT$_1$ transitivity** (W21.5): scope-restricted torsor over $\exp(\widehat{\mathfrak{grt}}_1)$ on $\mathrm{Quant}^{\mathrm{GN}, \mathrm{Koszul}}(\mathfrak g_{\Delta_5}) / (\mathbb Z/2)_{\mathrm{super}}$; obstruction $\mathrm{ob}^{\mathrm{GN}} \in H^2(\mathfrak{grt}_1; \widehat{\mathrm{Imag}})$ vanishes on the Koszul locus via Deligne–Goncharov motivic-vs-Borcherds filtration alignment through weight 12; conditional on Zagier–Hoffman above weight 12.
- **Yetter–Drinfeld $\delta^{(n)}$** (W21.7): Borcherds weight $\lfloor n/2\rfloor + 1$ proved (falsifying $\lceil n/2\rceil$ ansatz); Schauenburg-bracket expansion at $n = 4, 5, 6$ inscribed as $\sum_{\mathsf T} (\text{Catalan-tree coefficient}) \otimes (\text{Brown MZV basis})$; general rule $C_{n-1} \cdot d_n$ (Catalan × Padovan).

## Arithmetic anchors

- **Pseudo-character $S^{\mathrm{ps}}$** (W20.4) -- $\perp$ retracted per canonical preamble: the programme-canonical object is the Chenevier 2014 determinant $D^{\mathrm{Chen}}$ (see Pattern 295 / W25 in `notes/first_principles_cache_comprehensive.md`; Vol I `chapters/theory/derived_langlands.tex` Remark `rem:dl-w25-determinant-not-pseudocharacter`). Rename $S^{\mathrm{ps}}\to D^{\mathrm{Chen}}$; axioms shift from Taylor--Wiles symmetric-polarisation triple to Chenevier 2014 arXiv:1301.0635 \S1.2 polynomial law. The numerical content below is preserved (the polarisations of $D^{\mathrm{Chen}}$ recover the Taylor--Wiles tuple on the reduced ring $\mathbb T^{\mathrm{par}}_1$, Chenevier 2014 Thm.~2.12): 4-dim on paramodular Hecke algebra $\mathbb T^{\mathrm{par}}_1$; $S^{\mathrm{ps}}_1(T_p) = \lambda_p = a_p(f_{16}) + p^8 + p^9$; $S^{\mathrm{ps}}_4(T_p, T_p, T_p, T_p) = p^{32}$; verified on 22 primes $p \le 79$.
- **Hecke $a_p$**: continued through $p = 109$ via $E_4 \cdot \Delta$ convolution.
- **Siegel weight ladder** (W20.5, W21.9): $k_N^{\mathrm{honest}} = N + 3$, $k_N^{\mathrm{spin}} = (N + 3)/2$, continuous through $N \in \{2, 3, 4, 5, 6, 7, 8\}$ with Niemeier labellings $24A_1, 12A_2, 8A_3, 6A_4, A_5^4 D_4, 4A_6, 2A_7 D_5^2$; first genuine failure at $N = 24$ (Conway-moonshine escape to $\Lambda_{24}$).

## Frontier opened by Waves 20–22

Priority items remaining after W22:
- **CY-4 extension**: $\Phi_4$ framework gap; Kapustin–Rozansky–Saulina 3d/4d dichotomy is the structural obstacle.
- **$\phi^{(n \ge 25)}$**: doubly conditional on Zagier–Hoffman depth-reduction and Broadhurst–Kreimer empirical depth-distribution.
- **Fake-Monster $\theta^{\Phi_{12}}$ explicit generators** (rank 26 RTT).
- **$\Psi$-surjectivity closure**: modulo Conway conjecture (W20.2), the five $\Psi$-images saturate CY-$d$ reflective BKMs at $d \in \{2, 3\}$.
- **Monster Lusztig $\ell_{\mathrm{Monster}} = 2$ refined bookkeeping**: ratio $\ell_{\mathrm{K3}}/\ell_{\mathrm{Monster}} = 4 = c_+$-ratio load-bearing.

## Aggregate signature

- **~30 agent-rounds** across Waves 20–22 (10 per wave).
- **~2,500 inscribed lines** across Vol I + Vol III manuscript files.
- **~20 cache entries** appended to `appendices/first_principles_cache.md`.
- **5+ primary falsifications** with hidden-structure heals.
- **3 cross-volume AP5 propagation fixes** (`4\mathrm{Vol}(E) \to 2\mathrm{Vol}(E)$; $N = 6$ umbral re-anchor; $c_3$ Bruinier-reduced convention).
- **Octachotomy closure** at codim 3 for bar–cobar scope.
- **Five-archetype classification** G / L / C / M / **B** locked.
- **One unified climax identity** naming Theorems A–H in a single display.

The post-W22 frontier is structural-categorical (CY-4 framework, $\Phi_4$ existence, Conway row) and arithmetical-analytic (high-weight MZVs, high-prime Hecke, Fake-Monster generators); foundational scope of the programme is stable.

---

*End of Grand Synthesis, Waves 20–22. Compiled 2026-04-20.*
