# Attack-and-heal note: Cherednik monodromy + EK flatness (Yangian Theorem-A instance)

Session 2026-04-18. Adversarial audit of the CLAUDE.md Theorem-A row phrase
"E_1-ordered variant `thm:theorem-A-E1` PROVED via pure braid Orlik-Solomon
Koszulity (Shelton-Yuzvinsky); Yangian instance concrete (Cherednik monodromy
+ EK flatness)."

## Phase 1 — Grep audit

Search for "Cherednik" across Vol I `.tex`:

- `chapters/theory/theorem_A_infinity_2.tex:740` — LaTeX comment (not
  typeset): "Yangian instance concrete via Cherednik monodromy +
  Etingof-Kazhdan flatness." Above the theorem header; reader-invisible.
- `chapters/theory/theorem_A_infinity_2.tex:1242` — proof of
  `lem:R-twisted-descent` Step 1, typeset prose: "standard monodromy of
  the Cherednik-type connection." Used to NAME the connection type
  whose monodromy produces the $PB_n$ representation on
  $\cA^{\otimes n}$. No construction, no qi claim.
- `standalone/drinfeld_kohno_bridge.tex:372` — `thm:dk-os-koszul`
  clause (iii): "the Cherednik monodromy representation of the pure
  braid group factors through $H^\bullet(B^{\ord}(V^k(\fg)))$."
  Typeset, but standalone is ORPHAN: no `\input{...drinfeld_kohno_bridge}`
  anywhere under `main.tex` or the chapters tree (AP255 orphan).
- `chapters/examples/yangians_foundations.tex` — **zero** hits for
  "Cherednik".
- `chapters/examples/yangians_drinfeld_kohno.tex` — **zero** hits for
  "Cherednik".

Search for "EK flatness" / "Etingof-Kazhdan" across Vol I:

- `chapters/examples/yangians_foundations.tex` — **zero** hits for
  "Etingof", "Kazhdan", "EK flatness". ("Kazhdan" appears only in
  "Kazhdan-Lusztig" at :36 and :589, a distinct theorem.)
- `chapters/examples/yangians_drinfeld_kohno.tex` — hits for
  "Felder-Etingof-Varchenko" (:3827) and "Calaque-Enriquez-Etingof"
  (:3906); NO hit for Etingof-Kazhdan flatness or EK quantisation
  acyclicity as a load-bearing step for the Yangian Theorem-A instance.
- `chapters/theory/theorem_A_infinity_2.tex` — one hit: the LaTeX
  comment at :740 naming the pair "Cherednik + EK flatness" as
  scaffolding prose. No typeset theorem body cites an EK flatness lemma.

## Phase 2 — What is actually inscribed for the Yangian Theorem-A instance

The concrete Yangian instance of Theorem A is inscribed at
`chapters/examples/yangians_foundations.tex:828-852`:

```
\begin{corollary}[Yangian bar-cobar recovery; \ClaimStatusProvedHere]
\label{cor:yangian-bar-cobar}
For any simple g, the bar-cobar adjunction yields a quasi-isomorphism
  Omega^ch(B^ch(Y(g)^ch)) --> Y(g)^ch.
```

The proof cites:

- `prop:yangian-koszul` (Molev PBW for RTT Yangian + Polishchuk-Positselski
  PBW-implies-Koszul criterion);
- `thm:e1-chiral-koszul-duality` (bar-cobar qi for augmented pro-nilpotent
  $\Eone$-chiral algebras via PBW local finiteness);
- augmentation ideal pro-nilpotence of $Y_\hbar(\fg)$ in the RTT
  presentation.

The proof mechanism is PBW + Polishchuk-Positselski, NOT Cherednik
monodromy + EK flatness. The two are genuinely different machines:

- PBW + PP: classical quadratic-Koszul criterion; acyclicity of
  $K(\Sym V)$ transported to $K(Y(\fg))$ by flatness of the PBW
  deformation.
- Cherednik monodromy + EK flatness: a KZ-connection analytical
  package (Cherednik 1991, Etingof-Kazhdan 1996-2000) where the
  Yangian is RECOVERED from the monodromy of the rational KZ
  connection (equivalently from EK quantisation of $U(\fg[[t]])$),
  and the bar-complex qi on the ordered side is read off the
  flatness (integrability) of the EK construction.

A chain-level comparison proposition between the two — "the Molev-PBW
Koszulity and the Cherednik-EK flatness presentation of $Y(\fg)$ both
present the same bar-cobar qi" — is NOT inscribed anywhere in Vol I.

## Phase 3 — Diagnosis

This is the AP269 pattern (SDR-formula fabrication with a
proved-contradictory witness) in its weaker "mechanism-mention
fabrication" variant: the CLAUDE.md status-row advertises a
mechanism — "Cherednik monodromy + EK flatness" — whose keywords do
not appear in the typeset inscribed proof, while a DIFFERENT
mechanism (PBW + Polishchuk-Positselski) is in fact what delivers the
qi. The two inscriptions that use the words "Cherednik" or
"Etingof-Kazhdan" in typeset form are (a) a prose name for the
connection whose monodromy produces the $PB_n$ representation — not
a proof step of the Yangian Theorem-A instance — and (b) an orphan
standalone clause in `drinfeld_kohno_bridge.tex` that does not
compile as part of the monograph.

Consequence: a reader who follows the CLAUDE.md row expecting a
Cherednik-monodromy + EK-flatness proof of the Yangian bar-cobar qi
will find no such proof. The qi IS proved — by a different route —
so this is NOT an AP241 advertised-but-not-inscribed over the qi
itself; it is mechanism-level misadvertisement.

AP1521 (new, see below) registers this as a distinct pattern:
**load-bearing mechanism attribution at the status-row layer that
does not match the mechanism in the inscribed proof, even though the
conclusion of the status-row is correctly inscribed by a different
mechanism.** This is adjacent to AP256 (aspirational-heal drift) and
AP269 (fabrication-with-contradicting-witness) but distinct: the
proved conclusion exists, so the downgrade path cannot be
"theorem-level retraction"; the heal is either rename the mechanism
at the status-row layer, or inscribe the alternative mechanism as a
second-proof lemma.

The orphan `drinfeld_kohno_bridge.tex:360-378` does sketch the
Cherednik-monodromy-and-OS-Koszulity route as a SECOND presentation
(DK-0 through DK-3 stage ladder at :317-338, with `thm:dk-os-koszul`
at :360); this is the CLAUDE.md row's intended mechanism. But the
standalone is orphan (zero `\input`), so its theorems do not compile
into the monograph and cannot be cited by a live `\ref{}` consumer
in `theorem_A_infinity_2.tex` or `yangians_foundations.tex`.

Additional finding (AP264 variant): `theorem_A_infinity_2.tex:1292`
writes

```
For nontrivial R(z) (e.g., Yangian; Example~\ref{ex:yangian-bar-cobar}),
```

Grep for `\label{ex:yangian-bar-cobar}` across all three volumes
returns **zero** hits. The label is a phantom. Two near-neighbours
exist: (a) `cor:yangian-bar-cobar` at
`yangians_foundations.tex:829`, (b) `ex:yangian-sl2-modules` at
`yangians_foundations.tex:997`. The cite site reads as an Example
but the intended target is a Corollary; AP264 (phantom `\ref{ex:}`
to a label that does not exist).

## Phase 4 — Heal options (presented, not executed)

Three honest heals, in order of ambition:

**Option A (minimal, status-row rename).** Rewrite the CLAUDE.md
Theorem-A row phrase from

> Yangian instance concrete (Cherednik monodromy + EK flatness).

to

> Yangian instance concrete via `cor:yangian-bar-cobar`
> (`yangians_foundations.tex:828-852`): Molev PBW for RTT Yangian +
> Polishchuk-Positselski PBW-implies-Koszul + augmentation
> pro-nilpotence, routing through `thm:e1-chiral-koszul-duality`
> (bar-cobar qi for augmented pro-nilpotent $E_1$-chiral algebras).
> The Cherednik-monodromy + EK-flatness presentation is sketched in
> the orphan `standalone/drinfeld_kohno_bridge.tex` (DK-0 through
> DK-3 stage ladder, `thm:dk-os-koszul`); inscribing it as a live
> second-proof theorem in Vol I is an open target.

This is the Option-B-style retargeting in the AP149 cross-reference
discipline and costs a single row edit to CLAUDE.md. It preserves
the mathematical content (the qi IS proved) while fixing the
mechanism attribution.

**Option B (moderate, fix phantom `\ref{ex:yangian-bar-cobar}`).**
At `theorem_A_infinity_2.tex:1292`, change

```
For nontrivial R(z) (e.g., Yangian; Example~\ref{ex:yangian-bar-cobar})
```

to

```
For nontrivial R(z) (e.g., Yangian; Corollary~\ref{cor:yangian-bar-cobar})
```

This healing is independent of Option A and addresses the AP264
phantom-ref. The label `cor:yangian-bar-cobar` is inscribed in
`yangians_foundations.tex` which IS `\input`-ed at `main.tex:1613`,
so the retarget resolves at build time.

**Option C (ambitious, inscribe the Cherednik-EK route as a second
proof).** Inscribe a new proposition
`prop:yangian-theorem-A-via-cherednik-ek` in `yangians_foundations.tex`
(or `yangians_drinfeld_kohno.tex`) giving the KZ-connection +
Cherednik-monodromy + EK-flatness presentation of the Yangian
bar-cobar qi, with primary sources Cherednik 1991 (`arXiv:math/...`
primary: "Monodromy representations for generalized Knizhnik-Zamolodchikov
equations") and Etingof-Kazhdan 1996-2000 (the six-paper
"Quantization of Lie bialgebras" series, primarily parts I and VI
for the $U(\fg[[t]]) \to Y_\hbar(\fg)$ quantisation). The
proposition would carry `\ClaimStatusProvedElsewhere` attributing
the integrability (EK flatness) and monodromy (Cherednik)
constructions to their primary sources, and inscribe the bridge:
the quantisation + monodromy data determines the augmented
pro-nilpotent $E_1$-chiral algebra structure on $Y_\hbar(\fg)^{\ch}$
whose bar-cobar qi is the same qi as `cor:yangian-bar-cobar`. This
is a genuine independent verification path (HZ-IV would benefit)
but requires a careful chain-level comparison of the PBW basis to
the KZ-monodromy spectral parameter. That comparison is classical
(Drinfeld 1989 universal $R$-matrix from KZ monodromy is the
standard fact) but needs inscription as a lemma.

## Recommendation

Execute Options A + B immediately (low cost, high clarity). Defer
Option C to a dedicated Cherednik-EK inscription session.

Option B draft edit — single change at
`chapters/theory/theorem_A_infinity_2.tex:1292`:

    OLD: For nontrivial $R(z)$ (e.g., Yangian; Example~\ref{ex:yangian-bar-cobar}),
    NEW: For nontrivial $R(z)$ (e.g., Yangian; Corollary~\ref{cor:yangian-bar-cobar}),

Option A draft edit — single change at CLAUDE.md line 585 (Theorem A
row, final sentence of the E_1-ordered-variant clause): replace

    Yangian instance concrete (Cherednik monodromy + EK flatness).

with the paragraph in Option A above.

## New anti-patterns registered

**AP1521 (Mechanism misadvertisement at status-row layer while
conclusion is correctly inscribed by a different mechanism).**
A CLAUDE.md theorem-status row advertises a mechanism ("Cherednik
monodromy + EK flatness", "Feigin-Frenkel screening", "Wakimoto SDR")
whose keywords do not appear in the typeset inscribed proof body;
the conclusion of the status-row IS correctly inscribed, by a
different mechanism. Distinct from AP269 (conclusion-level
fabrication with a contradicting witness): conclusion is genuine,
mechanism attribution is wrong. Distinct from AP256 (aspirational
heal advertising advance): the advance exists, just by a different
route. Distinct from AP280 (three-step epistemic inflation): the
advertised theorem IS inscribed, at full strength; the drift is at
the mechanism layer only. Heal: (a) retarget the status-row
mechanism phrase to match the inscribed proof body, OR (b) inscribe
the advertised mechanism as a second-proof lemma with
`\ClaimStatusProvedElsewhere` attribution to primary sources, OR
(c) both. Detection: for every CLAUDE.md status-row that names a
specific mechanism (keyword pair, construction name, acyclicity
theorem, homotopy formula, SDR package), grep the cited `.tex` home
for the mechanism keywords; zero hits in typeset content with the
conclusion correctly inscribed by a different mechanism is AP1521.
Canonical violation: "Yangian instance concrete (Cherednik
monodromy + EK flatness)" advertised in CLAUDE.md Theorem A row
while the inscribed `cor:yangian-bar-cobar` at
`yangians_foundations.tex:828-852` proves the qi via Molev PBW +
Polishchuk-Positselski. Related: AP272 (unstated cross-lemma via
folklore citation — stronger, catches the case where neither the
mechanism nor the conclusion is genuinely inscribed); AP285 (alias
section-number drift — mechanism-layer drift specialised to
section-number transcription errors).

**AP1522 (Orphan standalone hosts mechanism cited at status-row
layer as if live).** CLAUDE.md status-row names a mechanism
(Cherednik monodromy + EK flatness, DK-0..DK-3 stage ladder,
Felder-KZB, etc.) whose only typeset inscription is in a standalone
`.tex` that is not `\input`-ed into `main.tex`. Build-level: the
standalone's theorems do not compile into the monograph and
`\ref{...}` consumers from live chapters resolve as `[?]` or not at
all. Canonical violation: `standalone/drinfeld_kohno_bridge.tex:360`
`thm:dk-os-koszul` clause (iii) inscribes the Cherednik monodromy
factorisation through $H^\bullet(B^{\ord}(V^k(\fg)))$; the standalone
is orphan (zero `\input`). Heal: (a) adopt the standalone as a
chapter (inscribe `\input{standalone/drinfeld_kohno_bridge}` at the
appropriate location in `main.tex`), OR (b) move the relevant
theorem(s) into a live chapter, OR (c) retarget the status-row
mechanism phrase to the live inscribed mechanism. Distinct from
AP255 (phantom file + phantomsection mask — file exists but labels
do not resolve): AP1522 is the case where the file exists AND the
labels are inscribed with proof bodies, but the file never compiles
into the monograph. Detection: `grep -n "\\\\input{.*drinfeld_kohno_bridge}" main.tex`;
zero hits with live status-row citation is AP1522.

## Residual frontier (not healed this session)

- Option C: inscribe `prop:yangian-theorem-A-via-cherednik-ek` as a
  second proof in Vol I with primary-source attribution to
  Cherednik 1991 + Etingof-Kazhdan 1996-2000. Load-bearing
  intermediate is the Drinfeld 1989 identification of the universal
  $R$-matrix with the KZ-connection monodromy. Open inscription
  target; HZ-IV decorator for `cor:yangian-bar-cobar` would become
  genuinely disjoint once inscribed (PBW vs KZ-monodromy paths).
- Adopt `standalone/drinfeld_kohno_bridge.tex` into `main.tex` via
  `\input{standalone/drinfeld_kohno_bridge}` in Part I or Part III
  (Yangian examples), OR migrate its DK-0..DK-3 ladder and
  `thm:dk-os-koszul` into `chapters/examples/yangians_drinfeld_kohno.tex`
  as a new section.
- Programme-wide AP1521 sweep: scan every CLAUDE.md status-row for
  mechanism phrases in parentheticals; grep each cited `.tex` home
  for the mechanism keywords; flag zero-hit mismatches for
  retargeting or second-proof inscription.

## Report meta

- No edits committed this session (per AP316 delivery discipline,
  patches recorded as Option-A and Option-B drafts in the
  Recommendation section; main-thread retains authority to apply).
- No AI attribution. Authored by Raeez Lorgat.
- No em-dashes in this note.
- AP numbering 1521-1522 used (reserved block AP1521-AP1540, used
  2 of 20 per AP306 minimal-use discipline).
