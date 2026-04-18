# Meta-pattern inscription: Symbol-overloading across mathematical contexts

**Session**: 2026-04-18. Meta-inscription only; no mathematical heal.

**Author**: Raeez Lorgat.

## Summary

This session surfaced a systemic notational failure mode in which one symbol (letter plus subscript convention) denotes multiple distinct mathematical objects across independently-developed contexts, and the programme conflates them at context-interfaces. The pattern has six catalogued sub-instances this session; the inscription consolidates them under a single meta-AP (AP2121) with counter-discipline plus a cache entry with regex trigger plus first-principles counter-derivation protocol.

## Canonical sub-instances

1. **AP234**: two $K$'s: $\kappa + \kappa^{!}$ scalar complementarity (per-family: 0 / 13 / 250/3 / 98/3) versus Trinity $K = c + c^{!}$ ghost-charge conductor ($-k$ / $2\dim(\fg)$ / 26 / 100 / 196). Related by $\kappa + \kappa^{!} = \varrho_A \cdot K$ with family-dependent $\varrho_A$.

2. **AP311**: two $\varrho$'s: $\varrho_{\mathrm{lin}}$ (leading coefficient of $\kappa$ linear in $c$) versus $\varrho_{\mathrm{gen}}$ (signed harmonic sum over strong generators, Kac--Roan--Wakimoto orbit invariant). Agree on principal $\cW_N$; diverge on Bershadsky--Polyakov ($1/2$ versus $1/6$).

3. **AP1982**: "Drinfeld center dim 1" ambiguous across $Z(U_{\cH_k}\text{-mod})$ (braided-monoidal centre), $Z(\cH_k)$ (naive commutant), $H^0 \cZ^{\mathrm{der}}_{\mathrm{ch}}(\cH_k)$ (cohomological zeroth slice). All three happen to equal $\bC$ for Heisenberg by coincidence; derived chiral centre is genuinely 3-dimensional ($P(t) = 1 + t + t^2$).

4. **AP2001**: $\kappa_{\mathrm{ch}}^{\mathrm{Heis}}$ (Heisenberg-level additive in rank) versus $\kappa_{\mathrm{ch}}$ (Hodge-supertrace multiplicative via K\"unneth). Reconciling the two at K3 $\times$ E is the structural content of AP289; the symbol-overloading is upstream.

5. **AP2041-2043**: $H^1(\fsl_2)$ four-way collision: full symmetric bar at generic level (dim 3), degree-2 ordered $V \otimes V$ (rank 4 with 8 on the unitary lift), genus-1 KZB Frobenius-rank 4, full symmetric bar at critical level $k = -h^{\vee}$ (infinite-dimensional $\Omega^{\bullet}(\mathrm{Op})$). Bare "$H^1(\fsl_2) = N$" with $N$ numeric is ambiguous without (algebra, grading, genus, level) signature.

6. **AP290**: HZ-7 $\kappa$ type-swap: Vol III proposition `prop:kappa-cat-quantum-groups` used Sugawara-shift formula $\dim(\fg)(k + h^{\vee}) / (2 h^{\vee})$ (a $\kappa_{\mathrm{ch}}$ formula) under the subscript $\kappa_{\mathrm{cat}}$. Subscript present, but wrong subscript for the formula.

## Common structural cause

Each instance arises at the interface of two or more independently-developed contexts:

- AP234: $\kappa$-complementarity context (shadow tower, Feigin--Frenkel involution, $c \leftrightarrow K - c$) meets Trinity-$K$ context (central-charge + ghost-charge, BRST, $c_{\mathrm{matter}} + c_{\mathrm{ghost}} = 0$ at $c_{\mathrm{tot}} = 26$). Both notions are programme-level, both use the letter $K$, the interface ($\varrho_A \cdot K$) was absent from the preface.

- AP311: shadow-tower $\varrho$ ($\kappa$-linearity) meets Kac--Roan--Wakimoto $\varrho$ (generator-profile harmonic). Agree on principal $\cW_N$ where both contexts pin the value; diverge on BP where the contexts are at arm's length.

- AP1982: monoidal-category centre (algebra-module category input) meets chiral-algebra centre (chiral algebra input) meets derived-factorisation centre ($E_3$ output). Four distinct constructions, three distinct source categories, one output symbol "$Z$".

- AP2001: compact CY$_2$ Hodge-supertrace context meets Heisenberg-lattice-rank context. K3 $\times$ E lives at the interface: $\kappa_{\mathrm{ch}}$ by lattice-rank is additive (rank 2 plus rank 1); by Hodge supertrace is multiplicative (2 times 0). The two routes give different values and only one is the genuine invariant (Hodge multiplicative wins, AP289).

- AP2041-2043: the symbol $H^1$ is used for four bar-complex cohomologies that come from four distinct bar constructions (full symmetric, ordered at a fixed degree, genus-1 KZB, critical-level Feigin--Frenkel). Each is well-defined in its own context; cross-context comparison is not a cohomology-level operation.

- AP290: the subscript discipline $\{\kappa_{\mathrm{ch}}, \kappa_{\mathrm{cat}}, \kappa_{\mathrm{BKM}}, \kappa_{\mathrm{fiber}}\}$ is HZ-7-mandatory, but the subscript is applied without verifying that the formula body matches the subscript's definitional meaning. Subscript discipline without formula-substance verification degrades into type-swap.

The unifying failure mode is **notational overload at the interface of independently-developed contexts**, not arithmetic error within any single context. Each context is internally consistent; the overload becomes load-bearing only when contexts collide.

## Counter-discipline

Before deploying any programme-level symbol ($\kappa$, $\varrho$, $Z$, $H^1$, $K$, $\chi$, $c$ when ambiguous, $S_r$ across conventions) in any chapter or standalone:

1. Inscribe a canonical-symbol-table at the opening of the chapter (or in a programme-wide conventions remark) listing every subscript variant used, with its definitional context and one boundary-value check.

2. Every use-site asserts which subscript applies, either explicitly in-line (`$\kappa_{\mathrm{ch}}$`) or by a local convention remark within 10 lines of the first use.

3. Prohibit the bare symbol at any context-interface, meaning any paragraph that names two or more of the contexts in the symbol-table. At such an interface the symbol MUST carry its subscript; the prohibition is enforced by grep gate (Pattern 230).

4. At context-interfaces, if the interface invariant (e.g. $\varrho_A \cdot K$, K\"unneth-multiplicative $\kappa_{\mathrm{ch}}$, Koszul-duality involution on $c$) has a known closed form, inscribe it as a named proposition or remark rather than deriving it inline at each context-interface.

## HOT ZONE candidacy

This session identified six canonical sub-instances. HOT ZONE threshold per CLAUDE.md preamble is "5+ waves / 50+ instances". Sub-instance count (6) exceeds the "5 waves" half of the threshold; programme-wide instance count is higher (AP234 alone propagates across preface, working notes, four surveys, and Vol II prose; AP290 recurs across Vol III $\kappa$-discipline audits; AP1982 recurs at every derived-centre versus naive-centre disambiguation). Recommendation: upgrade to HOT ZONE position HZ-12 in next CLAUDE.md consolidation wave; this inscription does not perform the HOT ZONE edit per AP314 inscription-rate throttling.

## Deliverables

- CLAUDE.md: new Wave section "Wave Symbol-overloading-meta (2026-04-18 meta-pattern consolidation, AP2121)" with meta-AP body.
- `notes/first_principles_cache_comprehensive.md`: new Pattern 230 entry with regex trigger, counter-derivation protocol, canonical violation list, and related-AP cross-references.
- This report file, for session archive.

## Scope and exclusions

- No manuscript edits.
- No heal of any individual sub-instance; those are pre-existing at AP234, AP290, AP311, AP1982, AP2001, AP2041-2043 and are each tracked separately.
- AP2122-AP2140 reserved per mission directive; not inscribed this wave.

## Attribution

No AI attribution. All work attributed to Raeez Lorgat.
