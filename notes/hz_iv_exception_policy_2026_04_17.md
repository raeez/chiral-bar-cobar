# HZ-IV Exception Policy for Metadata-Hygiene Sweeps

Date: 2026-04-17.  Author: Raeez Lorgat.

## Decision

Option (a): carve an explicit exception for the exact token `HZ-IV`
in hygiene greps.  `HZ-IV` is the canonical NAME of the Independent
Verification Protocol (Vol III CLAUDE.md §HZ3-11), not a HOT ZONE
index such as `HZ-4`.  It is load-bearing, like "BRST" or "KZ".

## Vol II distribution (2026-04-17 sweep)

27 of 28 Vol II in-prose hits are `HZ-IV` references.  Top files:

1. `chapters/theory/bp_chain_level_strict_platonic.tex`  -- 10 hits.
2. `chapters/theory/beta_N_closed_form_all_platonic.tex` --  6 hits.
3. `chapters/connections/y_algebras.tex`                 --  2 hits.

Plus 1 hit each in 6 further `platonic.tex` files (tempered closure,
topologization class M, tempered stratum, logarithmic W(p),
irrational cosets, W_infty endpoint).

## Recommended sweep filter

```bash
grep -rn '\bAP[0-9]\+\b\|\bHZ-[0-9]\+\b\|V[0-9]-AP[0-9]\+\|AP-CY[0-9]\+' ... \
  | grep -v ':[0-9]*:\s*%' | grep -v 'HZ-IV'
```

`HZ-[0-9]+` still catches Arabic indices (`HZ-4`, `HZ-10`); final
`grep -v 'HZ-IV'` preserves the protocol-name exception.

## Recommended CLAUDE.md update

Add under Metadata Hygiene "ALLOWED" (all three volumes):

> The exact token `HZ-IV` is the canonical name of the Independent
> Verification Protocol (Vol III CLAUDE.md §HZ3-11) and is permitted
> in typeset prose.  HOT ZONE indices `HZ-[0-9]+` remain forbidden.
