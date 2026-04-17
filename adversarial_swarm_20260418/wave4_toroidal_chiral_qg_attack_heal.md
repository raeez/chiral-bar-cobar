# Wave 4 (2026-04-18): Toroidal chiral QG — attack + heal

Agent session on Vol~I Toroidal-row claim "PROVED formal disk; global
P¹×P¹ conditional on class-M chain-level topologisation", with
companion phantom label and orphan standalone — channeling Etingof,
Polyakov, Kazhdan, Gelfand, Nekrasov, Kapranov, Bezrukavnikov,
Costello, Gaiotto, Witten.

## Attack ledger (linear reads + adversarial grep)

1. **Label `thm:chiral-qg-equiv-toroidal-sf`** — INSCRIBED at
   `standalone/seven_faces.tex:1043` (CLAUDE.md advertised :1020 —
   **AP257 line-number drift**, corrected in this heal). Body is
   `\ClaimStatusProvedElsewhere` with the classical Drinfeld--Miki
   naming; no proof body, no attribution remark.

2. **Label `thm:chiral-qg-equiv-toroidal-formal-disk`** — ZERO
   `\label{}` inscriptions anywhere in Vol~I. The only use sites
   are two `\verb|...|` prose references:
   - `standalone/N3_e1_primacy.tex:1160` (sub-section N3-NIP.e).
   - `CLAUDE.md` (in the now-retired companion-label line).
   **AP255 PHANTOM**. No `\ref{}` consumers means no `[?]` at build,
   but the advertised label was never real.

3. **`\input{standalone/seven_faces}` in `main.tex`** — ABSENT.
   `main.tex` `\input`s `chapters/connections/genus1_seven_faces`
   but not the standalone. **AP255 standalone orphan**, identical
   status to the elliptic companion. Both `-sf` standalone
   theorems (elliptic conjecture + toroidal theorem) are therefore
   not in the compiled manuscript.

4. **Consumer audit** — zero `\ref{thm:chiral-qg-equiv-toroidal-sf}`
   and zero `\ref{thm:chiral-qg-equiv-toroidal-formal-disk}` across
   `chapters/`, `standalone/`, `appendices/`. The sole prose
   references are `\texttt{...}` / `\verb|...|` string citations,
   not ref-resolution. Build is not broken; the inscription is
   simply not in the compiled PDF.

5. **Drinfeld--Miki naming** — the quantum-toroidal literature
   uniformly uses **Ding--Iohara--Miki (DIM)**: Ding--Iohara 1997,
   Miki 2007. "Drinfeld--Ginzburg--Miki" in the original theorem
   body conflates Drinfeld's New Realization of quantum affine
   (distinct construction) with DIM. **AP239 (naming after
   physical source without content)** at the author level —
   corrected in this heal.

6. **Vol~III chapter-level home** — EXISTS. Vol~III
   `chapters/theory/quantum_groups_foundations.tex:199-231`
   inscribes the formal-disk KL toroidal proposition at $\fsl_2$
   via FHHSY shuffle presentation and Miki $S_3$ triality. This is
   the canonical chapter-level home; the Vol~I standalone is a
   secondary presentation, not an independent proof.

7. **Class-M chain-level frontier pointer** — CLAUDE.md previously
   wrote "class-M chain-level topologisation frontier" as bare
   scope, which is ambiguous: CLAUDE.md Topologization row
   documents THREE open directions (I original-complex in
   $\Ch(\Vect)$; II class-L strict chain-level via $\eta_1$
   antighost-contact; III antighost BRST-commutativity at spin
   $\geq 3$). The toroidal global obstruction is direction~I
   specifically (pro/$J$-adic/weight-completed ambients already
   close class-M chain-level per `thm:mc5-class-m-chain-level-pro-ambient`
   and `thm:mc5-class-m-topological-chain-level-j-adic`). Heal
   pins the specific direction.

8. **Schiffmann--Vasserot CoHA citation density** — the theorem
   body names SV CoHA as the witness without citation; AP272
   folklore-citation risk. Vol~III chapter-level home carries
   FHHSY citation explicitly; Vol~I standalone's attribution
   remark now points to Vol~III for the citation-density.

9. **Bialgebra vs quantum group (AP263)** — "chiral quantum group"
   is the advertised label; the vertex-algebraic antipode lift
   is a separately proved NEGATIVE for Yangian, and the same
   obstruction applies to toroidal. Heal inscribes this as a
   scope remark rather than silently allowing the Hopf-naming
   drift.

## Surviving core (Drinfeld-style)

On the formal disk $(\mathrm{Spec}\,\bC[\![z]\!])^{\times 2}$ the
Ding--Iohara--Miki toroidal algebra $U_{q,t}(\ddot{\fsl}_N)$ with
its two spectral parameters $(u,v)$ and Miki $S_3$ triality of the
$\Omega$-background is the chiral bialgebra of an ordered-Koszul
factorization algebra, witnessed by the Schiffmann--Vasserot
cohomological Hall algebra on instanton moduli (canonical Vol~III
chapter-level inscription; Vol~I standalone is a secondary
presentation). The equivalence is bialgebra-level (AP263: the
antipode lift fails vertex-algebraically). Global extension to
$\PP^1 \times \PP^1$ is conditional on the same class-M
chain-level topologization frontier on the original bar complex
in $\Ch(\Vect)$ (direction~I of the topologization-tower open
inventory) that blocks chain-level Virasoro/$\cW_N$ on the raw
complex; closing direction~I closes the toroidal global case as a
downstream corollary.

## Heal record

| # | File | Action | Tag |
|---|------|--------|-----|
| H1 | `standalone/seven_faces.tex:1042-1053` | Theorem body renamed Drinfeld--Miki → Ding--Iohara--Miki; added Miki $S_3$ triality + pinned class-M frontier to direction~I (original complex in $\Ch(\Vect)$) | AP239 naming heal, AP272 citation sharpening |
| H2 | `standalone/seven_faces.tex:1054-` (new remark) | Inscribed `rem:toroidal-sf-attribution` pointing to Vol~III chapter-level home, AP263 bialgebra-scope caveat, and downstream-corollary statement of the global P¹×P¹ obstruction | AP251 attribution floor |
| H3 | `chapters/examples/yangians_foundations.tex:3915-3939` | Healed dangling broken prose `The (Theorem~\ref{...}): it adds an elliptic layer above it.` — reflowed to honest two-layer reading with explicit Vol~III chapter-level citation; retained the "one layer above the main triangle" Drinfeld compression | AP236 blacklist-style orphan paren, AP272 folklore citation |
| H4 | `standalone/N3_e1_primacy.tex:1159-1163` | Retargeted `\verb|thm:chiral-qg-equiv-toroidal-formal-disk|` to the real `\verb|thm:chiral-qg-equiv-toroidal-sf|` with explicit note that the `-formal-disk` suffix was never inscribed | AP255 phantom retarget (AP286 tactical close, but semantic because the content is identical) |
| H5 | `CLAUDE.md` Toroidal row | Rewrote row: line-number 1020→1043, Drinfeld--Miki→Ding--Iohara--Miki, Vol~III chapter-level home named, companion-phantom noted + retired, AP255 orphan status documented, class-M frontier pinned to direction~I, AP263 bialgebra-scope caveat, reference to this note file | AP257 line-number drift, AP255 phantom accounting, AP271 reverse-drift prevention |

## Status after heal

- `thm:chiral-qg-equiv-toroidal-sf`: correctly named Ding--Iohara--Miki;
  attribution remark points to Vol~III chapter-level home; scope
  pinned to formal disk at bialgebra level; global P¹×P¹ scope
  pinned to topologization direction~I.
- `thm:chiral-qg-equiv-toroidal-formal-disk`: acknowledged phantom;
  the only prose reference retargeted to the real `-sf` label.
- Vol~I chapter-level inscription: NOT added, matching the elliptic
  Wave-2 heal pattern — the canonical chapter-level home is Vol~III
  for toroidal (just as the canonical chapter-level home for the
  base ordered triangle is Vol~I `thm:chiral-qg-equiv`); Vol~I
  `chapters/examples/yangians_foundations.tex` carries the
  scope-concordance remark pointing to Vol~III, which is the
  epistemically honest framing.
- CLAUDE.md Toroidal row now matches manuscript scope (no AP271
  reverse-drift) and carries the specific class-M frontier pointer
  rather than the ambiguous bare phrase.

## Commit plan

No commit from this agent session; heal is inscription-only.
Recommended commit message (for user):

```
Vol I Wave-4 toroidal chiral QG attack-heal: AP255 phantom
companion label retired, AP257 line-drift corrected (seven_faces
:1020 → :1043), AP239 naming normalized (Drinfeld-Miki →
Ding-Iohara-Miki), AP263 bialgebra-scope caveat inscribed,
class-M frontier pinned to direction I (original complex in
Ch(Vect)), Vol III chapter-level home (quantum_groups_foundations
:199-231) named as canonical attribution. Files touched:
standalone/seven_faces.tex, standalone/N3_e1_primacy.tex,
chapters/examples/yangians_foundations.tex, CLAUDE.md,
adversarial_swarm_20260418/wave4_toroidal_chiral_qg_attack_heal.md.
No \input of seven_faces into main.tex (AP255 orphan retained,
matching Wave-2 elliptic-case decision).
```

## Open frontier items (not heal targets)

- **OF-T1**: global P¹×P¹ chain-level toroidal chiral bialgebra —
  blocked by topologization-tower direction~I (original-complex
  class-M in $\Ch(\Vect)$). Same open problem as chain-level
  Virasoro/$\cW_N$ on the raw complex.
- **OF-T2**: Vol~I chapter-level inscription of the toroidal
  formal-disk triangle (if desired; currently the programme
  treats Vol~III as canonical and Vol~I standalone as secondary).
- **OF-T3**: antipode lift for the toroidal bialgebra — expected
  to be a negative analogous to the Yangian case, but the explicit
  two-obstruction proof (OPE + Hopf axiom) has not been inscribed
  for toroidal specifically.
