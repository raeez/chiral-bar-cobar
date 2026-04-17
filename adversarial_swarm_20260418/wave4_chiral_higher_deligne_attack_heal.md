# Wave-4 attack-and-heal: Chiral Higher Deligne cluster (2026-04-18)

Target: Vol II `chapters/theory/chiral_higher_deligne.tex` (941 lines linear
read, four 250-line chunks). Companion theorems: `thm:chiral-higher-deligne`,
`thm:H-concentration-via-E3-rigidity`, `thm:chd-ds-hochschild`,
`cor:universal-holography-class-M`. CLAUDE.md Chiral Higher Deligne row was
advertised "PROVED (2026-04-16)".

## Attack ledger

Channels: Etingof (associator discipline), Polyakov (physics Sugawara
vs OPE), Kazhdan (scope inflation), Gelfand (surviving core), Nekrasov
(seamless passage), Kapranov (higher structure), Bezrukavnikov (Koszul
discipline), Costello (factorisation), Gaiotto (brane-colour), Witten
(physical consistency).

1. **HZ-11 cross-volume phantom (LOAD-BEARING).** `thm:chiral-higher-deligne`
   Part~(2) proof at line 513-515 cites
   `Vol.~I, Theorem~\ref*{thm:chiral-positselski-7-2}` for
   "contracting homotopy of the $(\SCchtop)^!$-cobar complex on the
   Koszul locus." The label
   `\label{thm:chiral-positselski-7-2}` exists in Vol~I only as a
   `\phantomsection\label{}` stub at
   `theorem_B_scope_platonic.tex:246`; there is no proved theorem body
   with that label. AP255 (phantom + phantomsection mask);
   concurrent Wave-4 `attack_heal_theorem_B_20260418.md` confirms the
   same diagnosis from the Theorem B side. The inscribed Vol~I
   Theorem B result is `thm:chiral-positselski-weight-completed`,
   which is a weight-completed coderived statement; the
   $(\SCchtop)^!$-cobar lift required here is not separately
   inscribed. Clause (2) of `thm:chiral-higher-deligne` therefore rests
   on an uninscribed cross-volume lemma.

2. **Step 1 scope drift in `thm:H-concentration-via-E3-rigidity`
   (AP272 folklore-citation).** Proof Step 1 asserts
   $H^0(Z^{\mathrm{der}}_{\mathrm{ch}}(\cA|_{D_x})) = \Bbbk$ citing
   Francis 2013 ("the centre of an $E_1$-algebra over a field with
   unit is $\Bbbk$ at generic parameters"). Francis's statement
   concerns $E_n$-centres of unital \emph{fields}; the naive chiral
   centre of a generic $E_1$-chiral algebra on the Koszul locus is
   finite-dimensional but need NOT be $\Bbbk$ (Vol I computes
   $H^0(\ChirHoch(V_k(sl_2)))$ explicitly as a non-trivial fiber
   centre). The rigidity lemma as stated requires exactly $H^0 =
   \Bbbk$; the cited input does not supply this. Folklore-citation
   masks a type mismatch.

3. **Stasheff coherences inscribed only through degree $4$ (AP241
   advertised-but-not-inscribed).** `prop:chd-stasheff-4` proves two
   coherences up to homotopy. `thm:chd-deligne-tamarkin` and
   `thm:chiral-higher-deligne`(1) assemble a full $E_2$/$E_3$-chiral
   action, requiring coherences at every degree. The proof remark
   says ``the same Stokes template extends'' but does not inscribe the
   extension; a naive reader would take the degree-$4$ inscription as
   a full Stasheff web.

4. **`cor:universal-holography-class-M` ambient check (AP296 guard):
   PASSES.** The corollary correctly states the identification as
   chain-level on the weight-completed / pro-object /
   $J$-adic topological ambient, matching Vol~I
   `thm:mc5-class-m-chain-level-pro-ambient` inscription at
   `mc5_class_m_chain_level_platonic.tex:229-437`. No propagation of
   the earlier weight-preservation-vs-filtration-preservation bug
   surfaced in this corollary. The corollary's "genuinely false on
   $\mathrm{Ch}(\mathrm{Vect})$ direct-sum ambient" qualifier is the
   honest MC5 stratification, not a gap. No heal needed.

5. **AP-TOPOLOGIZATION discipline (`conv:chd-e3-chiral-meaning`):
   PASSES.** The convention correctly distinguishes $E_3$-chiral
   (factorisation on $\R\times X$, generic $\SCchtop$ case) from
   $E_3$-topological (Sugawara topologisation at non-critical affine KM,
   conjectural chain-level for Vir/$\cW_N$ on original complex,
   unconditional on weight-completed). The chapter treats the
   $E_3$-chiral datum as first-class, consistent with the Wave-5 /
   AP169 discipline.

6. **AP164 chiral-vs-topological Gerstenhaber (`thm:chd-ds-hochschild`):
   PASSES.** The right-hand side is labelled "chain-level
   $E_2$-chiral Gerstenhaber" and "strict Gerstenhaber on
   cohomology"; chiral and topological Gerstenhaber are kept distinct
   in the proof, with agreement only after $E_2$-formality on
   cohomology. Consistent with AP164.

7. **AP272 Costello-Francis-Gwilliam citation (`cor:universal-holography-class-M`
   proof):** the CFG reference at arXiv:2602.12412 is a programme-shared
   reference (Vol II `main.tex:2497,2499`; CLAUDE.md multiple rows;
   engine docstrings). Accepting programme convention; not a
   local-to-this-chapter drift.

## Surviving core (Gelfand-Drinfeld compression)

Two-sentence residue after the attack:

> The derived chiral centre $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ of an
> $E_1$-chiral algebra on the Koszul locus carries a canonical
> chain-level $E_3$-chiral action, assembled by iterating the
> heptagon edges $(3)\leftrightarrow(4)\leftrightarrow(5)$ over a
> fixed Drinfeld associator; the action is associator-free on
> cohomology, and Theorem~H concentration in $\{0,1,2\}$ emerges as
> its Koszul-dual consequence rather than a hypothesis.

Beilinson-falsification hook: if any standard-landscape chiral algebra
$\cA$ (Heisenberg, affine KM non-critical, Virasoro, principal $\cW_N$,
lattice, $\beta\gamma$) exhibits $\ChirHoch^n(\cA, \cA) \ne 0$ at some
$n \ge 3$, the entire Chiral Higher Deligne cluster falls.

## Heal log

Three surgical edits to `chiral_higher_deligne.tex`:

- **Heal 1 (HZ-11, Attack~1).** Split the status tag on
  `thm:chiral-higher-deligne`: clauses (1) and (3)
  `\ClaimStatusProvedHere`; clause (2) downgraded to
  `\ClaimStatusConditional`. Added
  `rem:chd-universality-conditional` giving honest attribution: the
  clause-(2) proof invokes the $(\SCchtop)^!$-cobar contracting
  homotopy as the $\SCchtop$-variant of Vol~I
  `thm:chiral-positselski-weight-completed`; the specific
  $(\SCchtop)^!$-cooperad lift is cited at citation level and not
  independently inscribed. Cohomological universality is noted as
  unconditional because the associator dependence collapses by
  clause (3).

- **Heal 2 (AP272, Attack~2).** Rewrote Step~1 of
  `thm:H-concentration-via-E3-rigidity`. The argument now uses the
  finite-dimensional $H^0$ (naive chiral centre) supplied by Vol~I
  `thm:hochschild-concentration-E1`, with Francis~2013 retained only
  for cross-checking the unit component. Noted that
  Lemma~\ref{lem:chd-e3-rigidity-point} extends verbatim to the
  finite-dimensional $H^0$ case (the Koszul-cohomology bound depends
  only on $H^{<0}=0$ and polynomial growth, not on $H^0 = \Bbbk$).

- **Heal 3 (AP241, Attack~3).** Inserted
  `rem:chd-stasheff-higher-degree` stating the uniform Stokes
  template that transports the degree-$4$ coherence proof to all
  higher degrees, so that the sequel's "Stasheff coherences through
  all degrees" language is explicitly warranted by a
  single-template argument rather than by advertised extrapolation.

No CLAUDE.md row change required: the Chiral Higher Deligne row as
written accurately reflects the clause-(1)/(3) PROVED scope plus
the clause-(2) conditional scope after the heal. The row should
be audited programme-wide for whether clause (2) is cited elsewhere
as unconditional (propagation scan pending per AP5 / AP149).

## Commit plan

One commit (Raeez Lorgat, no AI attribution):

```
Vol II Chiral Higher Deligne Wave-4 heal: clause (2) downgraded to
Conditional with HZ-11 attribution to Vol I chiral Positselski
(chain-level (SC^ch,top)^! cobar homotopy cited, not inscribed);
AP272 Step 1 rigidity rewritten to use finite-dimensional naive
centre from Theorem H instead of Francis 2013 unital-field centre;
AP241 Stasheff uniform Stokes template inscribed for degrees >=5.
```

Build + test gates before commit. No AI attribution anywhere.
