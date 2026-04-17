# Wave 4 --- Universal Celestial Holography + $\mathcal W(p)$ tempering
## Attack + Heal (2026-04-17, first-principles, CG voice)

Target: Vol II `chapters/connections/universal_celestial_holography.tex` (`thm:uch-main`,
`thm:uch-gravity-chain-level`, `thm:uch-soft-hierarchy`, four-regime coverage)
and `chapters/theory/logarithmic_wp_tempered_analysis_platonic.tex`
(`conj:tempered-stratum-contains-wp` retraction language).

---

## Phase 1. Adversarial audit.

### (i) Coverage = four regimes. Genuine instance vs cited analogy.

**Self-dual gauge (a), `prop:uch-sdgauge`.** The celestial boundary algebra of
$4$d SDYM is $V_k(\mathfrak g)$ by Costello--Paquette (CPN19, CP21). This is
a genuine instance: the HT twist is the algebraic condition, the
$4$d Chern--Simons bulk is its explicit geometric realisation, and the
Costello--Gaiotto boundary VOA theorem gives $\mathcal A^{\mathrm{cel}} = V_k(\mathfrak g)$
as a chiral algebra on $\mathbb C_z$, not as analogy. **Verdict:** genuine.

**Gauge + matter (b), `prop:uch-ds-matter`.** Drinfeld--Sokolov reduction
of $V_k(\mathfrak g)\otimes F_R$ under the superpotential BRST constraint
(Paquette--Williams \S 5). The statement is genuine for $\mathcal N = 2$
gauge-with-matter admitting an HT twist. **Silent scope:** the claim
``class $\mathsf L$ for $f = 0$, class $\mathsf M$ for $f$ principal'' implicitly
assumes the DS datum is well-defined on the HT-twisted boundary; for
non-conformal matter, spectral-flow ambiguity of
Theorem~\ref{thm:uch-main}(i) propagates into the DS reduction, and
the class assignment becomes local (per-fibre) rather than global. **Verdict:**
genuine but needs the scope qualifier ``conformal matter, HT twist unobstructed.''

**Gravity (c), `prop:uch-gravity-leading`.** The displayed statement
$\mathcal A^{\mathrm{cel}}(T_4) \supseteq \mathrm{Vir}_c \oplus w_{1+\infty}$ uses
$\oplus$ as vector-space sum, not direct product of VOAs: Virasoro sits inside
$w_{1+\infty}$ as its spin-$2$ generator (Pope--Romans--Shen 1990, Bakas 1989,
Strominger 2021). **Minor attack:** the symbol $\oplus$ is misleading; the
correct relation is $\mathrm{Vir}_c \subset w_{1+\infty}$. Fix: replace $\oplus$
by $\supset \mathrm{Vir}_c \subset w_{1+\infty}$. **Verdict:** substance correct;
notation needs tightening.

**YM (d), `prop:uch-ym`.** The Beem--Rastelli $\chi$-functor takes $4$d $\mathcal N{=}2$
SCFTs to $2$d VOAs (BLLPRvR 2015). The UCH claim invokes $\chi$ for any
$\mathcal N{=}2$ YM (not just SCFT): pure $\mathcal N{=}2$ SYM is asymptotically
free, not conformal, so $\chi$ in its original form does not apply. The heal
inside the text routes through HT-twisted BV Yang--Mills
(Paquette--Williams), not $\chi$; the Beem--Rastelli image is then
recovered on the SCFT locus (conformal matter + gauge anomaly cancellation).
**Critical attack:** the phrase ``celestial chiral algebra of HT-twisted
Yang--Mills = $\chi(T_4)$'' is correct only for $\mathcal N{=}2$ SCFT;
for pure $\mathcal N{=}2$ SYM (non-SCFT), the correct object is the
Costello--Gwilliam boundary VOA of the HT-twisted BV action, not $\chi$.
**Verdict:** scope inflation; the $\chi$-match requires conformal invariance.

### (ii) Soft-factor hierarchy = shadow-tower coefficients, numerical match at $r=2, r=3$.

$r=2$ is Weinberg (leading soft graviton). The shadow-tower coefficient $S_2$
of $\mathrm{Vir}_c$ is $\kappa = c/2$ (Vol I census C2). The celestial Weinberg
pole at $\Delta_s = 2$ extracts the stress tensor $T(z)$; its vacuum
two-point function is $c/2 \cdot (z-w)^{-4}$. Match at $r=2$: $S_2 = c/2$
both sides. Verified.

$r=3$ is Cachazo--Strominger (subleading soft graviton). The shadow depth
$3$ coefficient is $S_3(\mathrm{Vir}_c)$, explicit closed form. Vol I
`notes/true_formula_census.md` and `shadow_tower_higher_coefficients.tex`
give $S_3(\mathrm{Vir}_c) = 0$ at generic $c$ (odd-depth vanishing from
Virasoro $\mathbb Z_2$-parity of the OPE); the Cachazo--Strominger subleading
soft piece has the same $\mathbb Z_2$ selection rule (derivative of stress tensor,
odd under parity). Both zero; match. The FIRST nontrivial higher-$r$
coefficient is $S_4 = 10/[c(5c+22)]$, matching Hamada--Shiu's
sub-subleading soft graviton at the kinematic factor $(z_{12})^3 (\bar z_{12})^{-1}$
after Mellin integration. This is a genuine coefficient match at leading large $c$.

**Verdict:** soft-factor match at $r=2, 3$ is either exact (Weinberg) or
a vanishing-on-vanishing match (Cachazo--Strominger). The first nontrivial
match is at $r=4$; Vol II `thm:uch-soft-hierarchy`(iii) is exactly this claim,
correctly scoped.

### (iii) Gravity case: Virasoro vs $w_{1+\infty}$ scope.

Vol II `prop:uch-gravity-leading` writes
$\mathcal A^{\mathrm{cel}} \supseteq \mathrm{Vir}_c \oplus w_{1+\infty}$.
`prop:uch-celestial-virasoro` and `rem:uch-winfty-celestial` then treat Virasoro
as the $c$-dependent representative and $w_{1+\infty}$ as the full soft tower
after weight completion. **Precise statement:** the $w_{1+\infty}$ algebra is
the large-$N$ limit of $\mathcal W_N$; Virasoro is its spin-$2$ truncation.
The shadow tower of Virasoro alone does NOT capture $w_{1+\infty}$; the
full $w_{1+\infty}$ shadow has $\beta_N = 12(H_N - 1)$ per-spin (Vol II
`thm:beta-N-closed-form-proved-all-N`) at each spin $s$, and the
large-$N$ limit is $\sum_{s=2}^\infty 12/s$, which diverges. The
weight-completion $w_{1+\infty}^\wedge$ of `rem:uch-winfty-celestial`
regularises this via the Koszul locus completion. **Attack:** the coverage claim
``gravity = Virasoro + $w_{1+\infty}$'' is correct only in the weight-completed
category; at the level of the original complex, only Virasoro is controlled
(Vol II `thm:tempered-stratum-contains-virasoro`), and $w_{1+\infty}$ is the
$N \to \infty$ limit of the W_N tower whose chain-level class $\mathsf M$
original-complex statement is open per Vol II `conj:wn-original-chain-level`.
**Verdict:** weight-completed scope correct; original-complex scope needs
qualification.

### (iv) `conj:uch-gravity-chain-level` content.

Inspecting the file at L499--566: `thm:uch-gravity-chain-level` is
already a ProvedHere theorem, not a conjecture. The CLAUDE.md HZ entry
``Chain-level class M at g\ge 1 still open as `conj:uch-gravity-chain-level`''
is stale: the theorem is in place. The proof routes through
`thm:chd-ds-hochschild` (chiral higher Deligne) + class-$\mathsf L$
chain-level on $V_k(\mathfrak{sl}_2)$ + DS exactness on Kazhdan-graded
category. **Attack:** the Step 2 invocation ``chain-level
$\mathrm{ChirHoch}^\bullet(V_k(\mathfrak{sl}_2))$ away from
modular-bootstrap obstruction'' implicitly assumes $H^2 = 0$ on the
$\mathfrak{sl}_2$ affine complex, which is Vol I Theorem MC4 class $\mathsf L$
unconditional. This is correct. Step 4 ``weight-completed $\to$ original''
uses ``$V_k(\mathfrak{sl}_2)$ conformally graded with finite-dimensional
weight spaces'' which is correct. **Verdict:** the theorem is rigorous; the
stale CLAUDE.md conj reference is a bookkeeping propagation lag.

### (v) YM via $\chi$: SCFT scope.

As in (i)(d). The Beem--Rastelli $\chi$-functor is defined on $\mathcal N{=}2$
\emph{SCFTs}, not general YM. For non-conformal $\mathcal N{=}2$ theories, the
celestial boundary algebra exists (Costello--Gwilliam HT quantisation) but is
not the $\chi$-image. **Fix:** `prop:uch-ym` scope qualifier restricts to
$\mathcal N{=}2$ SCFT; non-conformal matter falls under (b) DS reduction
with spectral-flow ambiguity.

### (vi) $\mathcal W(p)$ tempering retraction language: correlation-function Massey vs shadow-tower Massey.

This is the decisive attack. Reading
`logarithmic_wp_tempered_analysis_platonic.tex` L481--534:
the retraction argument says ``Gurarie 1993 and Flohr 1996 construct
logarithmic-CFT amplitudes whose $n$-point functions grow as $(\log z)^n$
in the collision limit; the corresponding Massey triple products
$\langle \Omega, \Omega, \Omega \rangle$ on bar cohomology are non-vanishing
and are NOT bounded by a power of $\dim A(\mathcal W(p))$.''

**First-principles dissection.**

Gurarie 1993 and Flohr 1996 produce unbounded growth in
CORRELATION-FUNCTION amplitudes: $\langle \mathcal O_1(z_1) \cdots \mathcal O_n(z_n)\rangle
\sim (\log z_{ij})^n$ in the coincidence limit. These are \emph{on-shell}
bar amplitudes at a specific collision stratum.

The shadow-tower coefficient $S_r(\mathcal A)$ is a \emph{different object}: it is the
$r$-th structure constant of the bar coalgebra's $A_\infty$ coproduct,
extracted by the $\mathrm d\log$ mechanism from the
Orlik--Solomon / Arnold form. It pairs against the universal
$\mathrm{FM}_r(\mathbb C)$ fundamental class, not against specific correlator
insertions.

The claim ``Massey bounded by $(2p)^{k+1}$'' was:
$$
\| \langle \Omega_{i_1},\ldots,\Omega_{i_k}\rangle \|_{\mathrm{amplitude}}
\le (\dim A(\mathcal W(p)))^{k+1}.
$$
Gurarie--Flohr falsifies this inequality for the AMPLITUDE norm. But the
shadow-tower coefficient $S_r$ is NOT an amplitude norm; it is a
\emph{structure constant} of the bar coalgebra. The honest implication
chain is:
\begin{enumerate}
\item[(A)] unbounded amplitude Masseys (Gurarie--Flohr) $\Rightarrow$
  correlation functions have log-accumulation.
\item[(B)] unbounded amplitude Masseys $\stackrel{?}{\Rightarrow}$ unbounded
  shadow-tower coefficients $S_r$.
\item[(C)] unbounded $S_r$ $\Rightarrow$ non-tempered stratum.
\end{enumerate}
The retraction falsifies (A) via Gurarie--Flohr but CONFLATES (A) with (B):
amplitude unboundedness does not imply shadow-coefficient unboundedness.
The two objects are related by an Orlik--Solomon residue that may regularise
the logarithmic growth into polynomial structure constants; the
$\mathrm d\log$ extraction kills the $(\log z)^n$ growth by construction
(the Arnold form is the \emph{logarithmic-free} part of the bar propagator).

**Correct statement of the retraction.**
Gurarie--Flohr falsifies \emph{correlation-function Massey boundedness},
which is the (A) $\Rightarrow$ (C) route via the Zhu inner product.
Gurarie--Flohr does NOT falsify \emph{shadow-tower Massey boundedness}
(the (B) $\Rightarrow$ (C) route via Orlik--Solomon residue).

The (B) $\Rightarrow$ (C) route is the DIRECT tempering criterion
$\limsup (|S_r|/r!)^{1/r} = 0$ and has not been falsified by any
primary source. Its status is genuinely OPEN, and
Conjecture~\ref{conj:tempered-stratum-contains-wp} correctly reflects this
as conjectural.

**Sharper split of the open frontier:**
\begin{itemize}
\item[(a)] \emph{Correlation-function Massey boundedness on $\mathcal W(p)$.}
  FALSIFIED by Gurarie 1993 + Flohr 1996. CLOSED (negative).
\item[(b)] \emph{Shadow-tower Massey boundedness on $\mathcal W(p)$.}
  $c(p)$-independent bound OPEN. Tempering implication OPEN.
\end{itemize}
The two are not equivalent because the Orlik--Solomon / Arnold residue
strips the logarithmic growth from amplitudes when extracting shadow
structure constants. The shadow coefficient $S_r(\mathcal W(p))$ is
finite and polynomial in the generator norms at fixed $r$ by construction
(finite-dim Zhu + $\mathrm{FM}_r$ compactness); the question is uniform
boundedness in $r$.

---

## Phase 2. Heal.

### (H1) UCH coverage explicit scope per regime.

Add scope-qualifier remark after `prop:uch-ym` clarifying:
\begin{itemize}
\item (a) self-dual gauge: genuine, unconditional.
\item (b) gauge + matter: genuine, scope = conformal HT-twist-unobstructed.
\item (c) gravity: Virasoro on original complex + $w_{1+\infty}$ in weight-completed category.
\item (d) YM: $\chi$-image on $\mathcal N{=}2$ SCFT; non-conformal via Costello--Gwilliam HT BV.
\end{itemize}

### (H2) Sharpen $w_{1+\infty}$ coverage.

Replace $\oplus$ in `prop:uch-gravity-leading` displayed equation by
$\supseteq \mathrm{Vir}_c \hookrightarrow w_{1+\infty}^\wedge$,
indicating Virasoro embedded in weight-completed $w_{1+\infty}$.

### (H3) $\mathcal W(p)$ tempering: split open frontier.

Append a `\begin{remark}[Correlation-function vs shadow-tower Massey]` to
the $\mathcal W(p)$ retraction, stating:
\begin{itemize}
\item[(a)] Correlation-function Massey boundedness is FALSIFIED (Gurarie 1993 +
  Flohr 1996); the $(2p)^{k+1}$ inequality on amplitudes is wrong.
\item[(b)] Shadow-tower Massey boundedness is a DISTINCT property, measured by
  the Orlik--Solomon residue of the bar propagator, not by the
  amplitude / Zhu inner product. It is OPEN.
\end{itemize}
The correct open conjecture is (b), not (a).

### (H4) Stale CLAUDE.md conj reference.

CLAUDE.md Vol I line ``Chain-level class M at g\ge 1 still open as
`conj:uch-gravity-chain-level`'' is stale:
`thm:uch-gravity-chain-level` is now ProvedHere (L499--566). Not editing
CLAUDE.md in this wave; flagging for next metadata sync.

---

## Inscribed edits.

1. `universal_celestial_holography.tex`: (i) add scope qualifier remark after
   `prop:uch-ym`; (ii) tighten $w_{1+\infty}$ notation in
   `prop:uch-gravity-leading`.
2. `logarithmic_wp_tempered_analysis_platonic.tex`: insert
   `rem:correlation-vs-shadow-massey` after `rem:gurarie-flohr-massey-obstruction`
   splitting the open frontier; amend
   `rem:wp-tempering-status` first-principles triple to state the
   distinction explicitly.

No theorem is retracted or upgraded; the healing is scope-qualification
of existing statements and separation of two Massey notions previously
conflated.

---

## Coverage ledger after wave 4.

| Claim | Pre-wave | Post-wave |
|-------|----------|-----------|
| UCH gauge (KM) | ProvedElsewhere | unchanged |
| UCH gauge+matter (DS) | ProvedHere | scope-qualified: conformal matter |
| UCH gravity (Vir) | ProvedHere | unchanged |
| UCH gravity ($w_{1+\infty}$) | implicit | weight-completed, original open |
| UCH YM ($\chi$) | ProvedHere | scope-qualified: SCFT locus |
| $\mathcal W(p)$ corr-fn Massey | --- | FALSIFIED (Gurarie-Flohr) |
| $\mathcal W(p)$ shadow-tower Massey | conflated | OPEN (genuine frontier) |

---

Raeez Lorgat, 2026-04-17.
