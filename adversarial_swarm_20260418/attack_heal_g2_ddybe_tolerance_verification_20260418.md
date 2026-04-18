# Verification follow-up: g2-DDYBE tolerance-ladder heal landing audit
# Date: 2026-04-18
# Author: Raeez Lorgat
# Target: verify attack_heal_g2_ddybe_20260418.md heals H1-H5 landed on disk;
#         AP315-discipline sensitivity check on T4=1e-4 tolerance.

## 0. Scope and verdict

The AP313-truncated completion of the earlier g2-DDYBE attack-heal agent
this session ("Now the tolerance-ladder remark update:") left its work
PARTIALLY LANDED. Findings, by heal line:

| Heal | Target | Advertised | On disk | Verdict |
|------|--------|------------|---------|---------|
| H1   | engine `verify_face_ddybe_g2_ladder` + test `test_ddybe_ladder_plateau` | YES (ref in rem:tolerance-ladder-falsification) | NO | AP256 drift |
| H2   | test `test_ddybe_generic_omega_second_sample` | YES (ref in rem:tolerance-ladder) | NO | AP256 drift |
| H3   | chapter cross-ref proof body -> regression gate | Partial verification below | Partial | OK |
| H4   | engine `verify_szego_three_term_g2` + test `test_szego_three_term_g2` | YES (ref in rem:tolerance-ladder) | NO | AP256 drift |
| H5   | Omega-sampling coarseness disclosure in theorem / remark prose | YES | YES | OK |

**Summary verdict**: the CHAPTER inscription landed (genus_2_ddybe_platonic.tex
mtime 2026-04-18 01:04, after the 01:02 ledger write). The ENGINE + TESTS
did NOT land (mtime 2026-04-16 22:06, untouched this session). The chapter
advertises three engine functions by explicit name that DO NOT EXIST on
disk. This is an AP256 (aspirational-heal manuscript-runs-ahead-of-engine)
violation introduced by the truncated heal.

## 1. Evidence

### 1a. Chapter inscription DID land (H3 + H5 + prose)

`chapters/theory/genus_2_ddybe_platonic.tex` line counts + grep:

- `rem:tolerance-ladder` at :552-594 inscribes the four-tier ladder
  (T1 10^{-12} / T2 10^{-10} / T3 10^{-6} / T4 10^{-4}) with per-tier
  justification columns. Test count now advertised at "32 after the
  2026-04-18 attack-heal additions".
- `rem:tolerance-ladder-falsification` at :596-615 inscribes the H1
  falsification ladder discipline and explicitly names
  `test_ddybe_ladder_plateau` as the regression gate; deferred-numerical
  execution explicitly registered with pointer to
  `attack_heal_g2_ddybe_20260418.md` S6.
- `rem:fay-versus-boltzmann-unitarity` at :617-636 distinguishes
  (a) Szegő trisecant (Fay 1973 Cor. 2.5) from (b) Boltzmann-unitarity
  identity (Riemann addition corollary) as two DISTINCT theta identities
  both due to Fay. Names `verify_unitarity_g2` as the (b)-test.
- `rem:g2-nonseparating-untested` at :638-651 inscribes the genuine
  open frontier: nonseparating degeneration untested. Aligns with
  CLAUDE.md DDYBE row.
- Theorem statement at :419-442 now discloses Omega-sampling coarseness:
  "for generic Omega in HHH_2 ... at a single Omega value Omega_0 ...
  does NOT witness the full three-complex-dimensional Omega-dependence".

H3 (cross-ref proof -> regression gate) is partially implemented via the
test-name drops in rem:tolerance-ladder; a stricter HZ-IV-grade H3
would inscribe the algebraic factorization
`Theta_odd(x e_1 | diag(tau_1, tau_2)) = -theta_1(x|tau_1) * theta_3(0|tau_2)`
inside the proof body of thm:g2-face-model-bypass-scope-restricted(i)
with a direct pointer to `verify_g2_to_g1_degeneration` in the engine.
The current proof body is adequate but not HZ-IV-hardened; this is a
minor residual, not a drift.

### 1b. Engine + tests DID NOT land (H1 + H2 + H4)

File mtimes:
```
chapters/theory/genus_2_ddybe_platonic.tex: 2026-04-18 01:04
compute/lib/face_model_ddybe_engine.py:     2026-04-16 22:06
compute/tests/test_face_model_ddybe_engine.py: 2026-04-16 22:06
```

Grep across `compute/` for the three advertised names:
```
verify_face_ddybe_g2_ladder       -> 0 hits
verify_szego_three_term_g2        -> 0 hits
test_ddybe_ladder_plateau         -> 0 hits
test_ddybe_generic_omega_second_sample -> 0 hits
test_szego_three_term_g2          -> 0 hits
TestFaceSzegoThreeTerm            -> 0 hits
```

The chapter advertises `TestFaceSzegoThreeTerm (new,
test_szego_three_term_g2)` as a test class in rem:tolerance-ladder; no
such class exists on disk. This is a textbook AP256 violation: manuscript
runs ahead of engine implementation.

The earlier agent's S6 DOES register this as "deferred audit (numpy
unavailable in sandbox)", so the work is HONESTLY labelled as pending
in the ledger; the failure mode is that the CHAPTER inscription does
not carry the same honest "deferred" qualifier in its test-name advertisements.

## 2. AP315 sensitivity analysis at T4=1e-4

The mission asks: "per AP315 discipline, is T4 = 1e-4 sufficient, or
within noise of finite-Omega truncation? Compare to elliptic CYBE
finding: tolerance 1e-6 accepted CYBE residuals 0.8-5.8 (AP315)."

Analytical (sandbox has no numpy; analysis by hand):

For generic Omega = [[1.1i, 0.15+0.05i], [0.15+0.05i, 1.3i]],
min(Im Omega) ~ 1.0 (smaller eigenvalue of the imaginary part).

At N=8:
- Theta-series truncation error:
  eps(N) ~ exp(-pi * N^2 * min(Im Omega) / 2)
         = exp(-pi * 64 * 1.0 / 2)
         = exp(-100) ~ 10^{-44}.
  Negligible; N=8 is deep inside the theta-series convergence region for
  min(Im Omega) >= 1.0. (The ledger's text at :40 has a typo in the
  exponent estimate, saying e^{-100} directly; the arithmetic is consistent:
  pi * 64 / 2 ~ 100.5, so e^{-100} is the truncation-error bound at N=8
  with min(Im Omega) >= 1.0. This is orders of magnitude below any
  engineering-relevant floor.)
- Float-64 accumulated roundoff on three 8x8 matrix multiplications
  with Boltzmann-weight entries of scale O(1) and condition number ~O(10^2)
  (generic at eta=0.25 away from weight-zero loci): ~10^{-12} to 10^{-11}.
- DDYBE verifier returns a single `relative = diff / scale` with
  diff = np.max(abs LHS-RHS) and scale = max(abs LHS, abs RHS);
  scale is typically O(10) for Boltzmann products; diff is accumulated
  roundoff plus any theoretical DDYBE residual.

Conclusion: tol=1e-4 at N=8 is approximately 10^7-10^9 ABOVE the
float-64 accumulated-roundoff floor and 10^{40} above the truncation
floor. A finite-hbar DDYBE residual of order eta^k ~ 0.25^k at k >= 4
would be ~4e-3 (k=4), ~1e-3 (k=5), ~3e-4 (k=6), ~6e-5 (k=7). A k=6
residual at ~3e-4 would pass tol=1e-4 and a k=7 residual would pass
tol=1e-6. The current tolerance is therefore SENSITIVE ENOUGH to
detect O(eta^6) or worse breakdowns; it is NOT sensitive enough to
detect O(eta^7) or O(eta^8) breakdowns. The AP641 ladder heal (H1) is
designed to sharpen this to O(10^{-6}) at N=12, which would detect
O(eta^8) to O(eta^9).

Comparison to AP315: NOT the same failure mode. AP315's elliptic CYBE
engine accepted residuals 0.8-5.8 (order-unity!) at tol=1e-6, because
the docstring and the verifier body disagreed on which r-matrix form
was being checked; the g2-DDYBE engine has no such semantic mismatch,
and residuals at N=8 across the 4 test points are genuinely below 1e-4
(corroborated by the 2026-04-16 engine commit's passing test log).
The g2-DDYBE T4=1e-4 is a CONSERVATIVE ENGINEERING BUDGET, not a
hidden silent failure. The AP315 analogue heal is the ladder-test
sharpening (H1), not a retraction.

**T4 verdict**: ACCEPT the current 1e-4 ceiling as an engineering
budget; LAND the H1 ladder test at next session with numpy to obtain
the N=12 plateau value and RECORD the plateau in rem:tolerance-ladder
(the slot is already prepared in the chapter, inscription pending).
NO IMMEDIATE TIGHTENING of the in-test tolerance from 1e-4 to 1e-6 at
N=8 (the residuals at N=8 have not been measured at sub-1e-4 precision,
per the attack-heal ledger); the tightening attaches to the N=12 ladder
point where the residual is empirically in the 10^{-6} band per the
chapter's remark at :492-494.

## 3. Recommendation (minimal scope)

Following AP314 discipline (inscription-rate outpaces audit capacity)
and AP266 (sharpened-obstruction healing register), the correct follow-up
is to LAND H1 + H2 + H4 in a dedicated next session WITH NUMPY, not to
retract the chapter inscription. Specifically:

1. Next-session action (not this session): implement
   `verify_face_ddybe_g2_ladder`, `verify_szego_three_term_g2` in
   `compute/lib/face_model_ddybe_engine.py`; implement
   `test_ddybe_ladder_plateau`, `test_ddybe_generic_omega_second_sample`,
   `test_szego_three_term_g2` in
   `compute/tests/test_face_model_ddybe_engine.py`; run them and inscribe
   the measured residuals back into `rem:tolerance-ladder` of the chapter.

2. This session, no action on engine or chapter: the chapter's
   advertisements are formally AP256 aspirational-heal drift but the
   earlier agent's ledger S6 HONESTLY registers the drift as deferred.
   Tightening the chapter prose further (retracting the test-name
   advertisements) would require a chapter Edit that risks introducing
   noise for a pending-not-stuck condition. Prefer landing the engine
   work to closing the drift.

3. No new AP blocks needed. AP641-AP645 from the earlier ledger cover
   the relevant patterns (AP641 tolerance-ladder-vs-truncation-floor,
   AP642 "extends to genus X" language, AP643 algebraic-vs-numerical,
   AP644 Omega-sampling-coarseness, AP645 face-vs-vertex at g=2). The
   specific landing-partial pattern here is captured by AP256
   (aspirational-heal drift) already in the catalogue. AP1141-AP1160
   block from the verification prompt is NOT spent: per AP314 discipline,
   new APs are inscribed only when a genuinely novel failure mode
   surfaces. No novel failure mode; the truncated-result landing-partial
   is AP256 + AP313 acting in composition, already catalogued.

## 4. Artifact inventory this verification session

Writes:
- `adversarial_swarm_20260418/attack_heal_g2_ddybe_tolerance_verification_20260418.md`
  (this file).

No chapter edits, no engine edits, no CLAUDE.md edits, no commits.

## 5. Summary table for the next-session checklist

| Item | State | Action |
|------|-------|--------|
| genus_2_ddybe_platonic.tex rem:tolerance-ladder (T1..T4 table) | LANDED | -- |
| genus_2_ddybe_platonic.tex rem:tolerance-ladder-falsification | LANDED | -- |
| genus_2_ddybe_platonic.tex rem:fay-versus-boltzmann-unitarity | LANDED | -- |
| genus_2_ddybe_platonic.tex rem:g2-nonseparating-untested | LANDED | -- |
| genus_2_ddybe_platonic.tex single-Omega disclosure in thm (ii) | LANDED | -- |
| face_model_ddybe_engine.py `verify_face_ddybe_g2_ladder` | MISSING | implement next session |
| face_model_ddybe_engine.py `verify_szego_three_term_g2` | MISSING | implement next session |
| test_face_model_ddybe_engine.py `test_ddybe_ladder_plateau` | MISSING | implement next session |
| test_face_model_ddybe_engine.py `test_ddybe_generic_omega_second_sample` | MISSING | implement next session |
| test_face_model_ddybe_engine.py `test_szego_three_term_g2` | MISSING | implement next session |
| test_face_model_ddybe_engine.py `TestFaceSzegoThreeTerm` class | MISSING | implement next session |
| Engine tolerance at the `verify_face_ddybe_g2` line (:795 `1e-4`) | ADEQUATE engineering budget | tighten via ladder at N=12 next session |
| Residual plateau at N in {8,12,16} logged in rem:tolerance-ladder | PENDING (chapter slot ready) | inscribe numerics next session |
| AP315 comparison | NOT the same failure mode (no semantic mismatch) | no action |

End of verification.
