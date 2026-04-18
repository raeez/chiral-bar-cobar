# Wave-12 AP124 Duplicate-Label Heal: `thm:shadow-tower-sub-subleading-closed-form`

Date: 2026-04-18
Agent: Wave-12 targeted-heal executor
Input: audit by agent `a2807e46` (Wave-12 AP124 scan)

## Problem

Two `\label{thm:shadow-tower-sub-subleading-closed-form}` inscriptions in Vol I:

- `chapters/theory/shadow_tower_higher_coefficients.tex:3215` — inline 6-step proof, attached `cor:kummer-emergence-at-r-8`, `cor:tier-3-characteristic-primes`, `lem:sub-subleading-cubic-identity`, `rem:gamma-not-beta-squared`.
- `chapters/theory/shadow_tower_sub_subleading_platonic.tex:247` — dedicated chapter with canonical proof, dedicated Kummer section, 14 HZ-IV tests.

AP124 (label uniqueness across Vol I / Vol II / Vol III) violated.

## Consumers audited

- `\ref{thm:shadow-tower-sub-subleading-closed-form}`: 6 sites (self-refs x3, all_tier_generating_function_platonic:376, _platonic:78, _platonic:369). All must continue to resolve.
- `\ref{cor:kummer-emergence-at-r-8}`: 3 sites (self-ref :3740, all_tier_generating_function_platonic.tex:503, compute/tests/test_four_tier_kummer_database.py:133 claim string).
- `\ref{cor:tier-3-characteristic-primes}`: 1 site (self-ref :3741).
- `\ref{lem:sub-subleading-cubic-identity}`: 1 site (compute/lib/shadow_tower_higher_vir.py:308 comment).

## Option chosen: B (rename inline + ProvedElsewhere attribution)

Rejected Option A (migrate corollary to `_platonic`): four-item content migration (cor + cor + lem + rem). `_platonic` already has an equivalent but distinct Kummer-691 dissection via `rem:gamma-691-emergence-sporadic` (modular-coincidence polynomial route), orthogonal to the explicit $r = 8$ arithmetic at `cor:kummer-emergence-at-r-8`. Both proofs are reader-useful; the issue is strictly the duplicate `thm:` label.

Rejected Option C (delete theorem + rename corollary): breaks external consumer `test_four_tier_kummer_database.py:133`.

Option B preserves all child labels in-place (they are unique) and only normalises the duplicate `thm:` label.

## Edits applied

Single edit at `chapters/theory/shadow_tower_higher_coefficients.tex:3215-3230`:

1. `\label{thm:shadow-tower-sub-subleading-closed-form}` → `\label{thm:shadow-tower-sub-subleading-closed-form-inline}`.
2. `\ClaimStatusProvedHere` → `\ClaimStatusProvedElsewhere` (AP60 discipline).
3. Inserted `\begin{remark}[Attribution]` immediately after the theorem, citing the canonical `\ref{thm:shadow-tower-sub-subleading-closed-form}` at `_platonic:247`, noting the inline 6-step proof is retained as an alternative (not independent) route, and confirming the Kummer and Tier-3 corollaries remain inscribed at the inline site because their labels are unique.

No deletions. No consumer-site edits required — all 6 `\ref{thm:...closed-form}` consumers auto-resolve to the surviving canonical label (uniqueness restored).

## Post-edit verification (PE-7 gate)

- Vol I `\label{thm:shadow-tower-sub-subleading-closed-form}` count: **1** (was 2). Unique, at `_platonic:247`.
- Vol I `\label{thm:shadow-tower-sub-subleading-closed-form-inline}` count: 1 (new, unique).
- Vol II / Vol III canonical label: 0 hits (only phantomsection `V1-`-prefixed aliases in Vol II; no collision).
- 4 child labels (`cor:kummer-emergence-at-r-8`, `cor:tier-3-characteristic-primes`, `lem:sub-subleading-cubic-identity`, `rem:gamma-not-beta-squared`) retained uniquely at inline site.
- `cor:kummer-emergence-at-r-8` external consumer `test_four_tier_kummer_database.py:133` — label still exists, no change needed.
- `all_tier_generating_function_platonic.tex:503` cite of `cor:kummer-emergence-at-r-8` — still resolves.

## AP discipline satisfied

- AP124 (uniqueness across Vol I/II/III): restored for canonical label.
- AP125 (prefix matches environment): `thm:` prefix retained for theorem env at both sites.
- AP60 (tag only genuinely new content ProvedHere): inline theorem downgraded to ProvedElsewhere with attribution remark.
- AP149 (resolution propagation): zero consumer edits required because consumer refs point at the canonical name which remains valid and unique post-heal. No propagation debt.

## PostToolUse hook note

Hook fired AP24 on line 2295 (pre-existing, out of edit scope). The flagged line `\kappa(W_3) + \kappa(W_3^!) = 250/3` is correctly qualified (W_3 complementarity = 250/3 per C4 census); the hook's AP24 trigger is a false positive on a correctly-qualified non-Virasoro complementarity. No action.

## Commit plan

Single commit, Vol I only:

- Path: `chapters/theory/shadow_tower_higher_coefficients.tex`
- Message (candidate): `Vol I AP124 heal: rename inline thm:shadow-tower-sub-subleading-closed-form duplicate to -inline, retag ProvedElsewhere with attribution remark to canonical _platonic:247; child corollaries preserved in-place (unique labels).`
- No cross-volume propagation required.
- No test-file edits required.

## Residual

None. Heal is atomic and complete per Option B spec.
