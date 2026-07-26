# ============================================================================
#  Makefile — Modular Koszul Duality (Vol I)
# ============================================================================
#
#  Usage:
#    make volume         Build the NORMATIVE volume → out/reconstruction.pdf
#                        This is the mathematically current root.
#    make geometry       Build the 408-page revision → out/geometry.pdf
#                        Refuses while any of its 53 sources is absent;
#                        see reconstruction/MISSING_SOURCES.md.
#    make skeleton       Build the earlier 8-chapter spine (superseded).
#    make legacy-manuscript
#                        Build the retracted-architecture manuscript.
#                        Reference only — see PORT_LEDGER.md.
#    make               Build everything: normative volume + manuscript + notes
#    make fast           Quick build for rapid iteration → out/main.pdf
#    make release        Full release: manuscript + working notes + standalone → out/
#    make standalone     Build standalone papers → out/
#    make working-notes  Build working notes → out/working_notes.pdf
#    make watch          Continuous rebuild on file changes (requires latexmk)
#    make clean          Remove all LaTeX build artifacts
#    make veryclean      Remove artifacts AND out/ (forces full rebuild)
#    make clean-builds   Remove all /tmp/mkd-* isolated build directories
#    make count          Line counts and page estimate
#    make check          Dry-run compilation to check for errors
#    make draft          Build with draft mode (faster, no images)
#
#  Build isolation (parallel agents):
#    Each build runs in its own /tmp directory.  Set MKD_BUILD_NS to reuse
#    the same directory across invocations (warm .aux files = faster builds):
#
#      export MKD_BUILD_NS="agent-$$"   # set once per agent session
#      make fast                         # cold first time, warm thereafter
#      # ... edit .tex ...
#      make fast                         # warm — converges in fewer passes
#
#  All compiled output goes to out/.
#
# ============================================================================

# --- Configuration -----------------------------------------------------------

MAIN      := main
NEWVOL    := main_ordered_chiral
RECON     := reconstruction
RECON_DIR := reconstruction
TEX       := pdflatex
TEXFLAGS  := -interaction=nonstopmode -file-line-error -synctex=0 -cnf-line='buf_size=1000000' -cnf-line='stack_size=20000'
LATEXMK   := latexmk
MKFLAGS   := -pdf -pdflatex="$(TEX) $(TEXFLAGS)" -interaction=nonstopmode
BUILD_SCRIPT := ./scripts/build.sh
LOG_DIR   := .build_logs
PYTEST_FAST_TIMEOUT ?= 120
PYTEST_FULL_TIMEOUT ?= 300
PYTEST_FULL_HEARTBEAT ?= 60
PYTEST_FULL_NODEIDS_PER_SHARD ?= 10
PYTEST_FULL_TARGET_SHARD_SECONDS ?= 60
PYTEST_FULL_STATE_DIR ?= .pytest-full-state
PYTHON_BIN ?= $(shell if [ -x compute/.venv/bin/python ]; then echo compute/.venv/bin/python; elif [ -x .venv/bin/python ]; then echo .venv/bin/python; else echo python3; fi)

# iCloud destination for release PDFs
ICLOUD_DIR := /Users/raeez/Library/Mobile Documents/com~apple~CloudDocs/research

# Number of passes for cross-references, TOC, and page numbers to stabilize.
PASSES    := 6
FAST_PASSES := 4

# Source files: every .tex file that main.tex transitively \input's or \include's.
SOURCES   := $(wildcard *.tex) \
             $(wildcard chapters/theory/*.tex) \
             $(wildcard chapters/examples/*.tex) \
             $(wildcard chapters/connections/*.tex) \
             $(wildcard appendices/*.tex) \
             $(wildcard bibliography/*.tex)

# Output — everything goes to out/
OUT_DIR   := out
PDF       := $(OUT_DIR)/main.pdf
ICLOUD_MAIN_PREREQ := $(if $(wildcard $(PDF)),,$(PDF))

# Mathematics publish dir — release binary copied here under canonical name
MATHEMATICS_DIR := $(HOME)/mathematics
PUBLISHED_PDF   := Chiral_Bar_Cobar_Duality__Geometric_Realization.pdf
VOLUME_KEY      := vol1
PYTHON_BIN      ?= $(shell if [ -x compute/.venv/bin/python ]; then echo compute/.venv/bin/python; elif [ -x .venv/bin/python ]; then echo .venv/bin/python; else echo python3; fi)

# Working notes
WN_TEX    := working_notes.tex

# Stamp file: tracks last successful build.
STAMP     := .build_stamp

# If PDF was externally deleted but stamp remains, force a rebuild.
ifeq (,$(wildcard $(PDF)))
  $(shell rm -f $(STAMP))
endif

# LaTeX intermediate extensions
AUX_EXTS  := aux log out toc synctex.gz fdb_latexmk fls bbl blg \
             nav snm vrb idx ilg ind lof lot

# ============================================================================
#  Targets
# ============================================================================

.DEFAULT_GOAL := all

.PHONY: all volume geometry skeleton legacy-manuscript modular-koszul-core fast watch clean veryclean clean-builds count check draft integrity phase0-index metadata verify census test editorial standalone dist release help working-notes icloud verify-independence verify-independence-verbose mathematics-publish root-publish architecture unified-architecture

## icloud: Copy latest PDFs to iCloud Drive, organised by subject
icloud: $(ICLOUD_MAIN_PREREQ) standalone
	@echo "  ── Copying to iCloud (subject-organised) ──"
	@# --- Volumes ---
	@mkdir -p "$(ICLOUD_DIR)/volumes"
	@[ -f $(PDF) ] && cp $(PDF) "$(ICLOUD_DIR)/volumes/vol1_modular_koszul_duality.pdf" && echo "    ✓ volumes/vol1" || true
	@# --- Vol I: Foundational algebraic-geometric theory ---
	@mkdir -p "$(ICLOUD_DIR)/vol1_foundations"
	@for p in five_theorems_modular_koszul shadow_towers_v3 e1_primacy_ordered_bar \
		koszulness_fourteen_characterizations en_chiral_operadic_circle \
		sc_chtop_pva_descent drinfeld_kohno_bridge seven_faces genus1_seven_faces \
		arithmetic_shadows multi_weight_cross_channel analytic_sewing \
		ordered_chiral_homology survey_modular_koszul_duality_v2 \
		determinant_of_an_operator; do \
		[ -f $(OUT_DIR)/$$p.pdf ] && cp $(OUT_DIR)/$$p.pdf "$(ICLOUD_DIR)/vol1_foundations/$$p.pdf" \
			&& echo "    ✓ vol1_foundations/$$p" || true; \
	done
	@# --- Vol II: 3d HT gauge theories (generalising real 3d Chern-Simons) ---
	@mkdir -p "$(ICLOUD_DIR)/vol2_3d_ht_physics"
	@for p in three_dimensional_quantum_gravity holographic_datum; do \
		[ -f $(OUT_DIR)/$$p.pdf ] && cp $(OUT_DIR)/$$p.pdf "$(ICLOUD_DIR)/vol2_3d_ht_physics/$$p.pdf" \
			&& echo "    ✓ vol2_3d_ht_physics/$$p" || true; \
	done
	@# --- Vol III: 6d hCS and higher-dimensional sources ---
	@mkdir -p "$(ICLOUD_DIR)/vol3_6d_hcs_cy"
	@for p in cy_to_chiral_functor cy_quantum_groups_6d_hcs; do \
		[ -f $(OUT_DIR)/$$p.pdf ] && cp $(OUT_DIR)/$$p.pdf "$(ICLOUD_DIR)/vol3_6d_hcs_cy/$$p.pdf" \
			&& echo "    ✓ vol3_6d_hcs_cy/$$p" || true; \
	done
	@# --- Programme overview ---
	@mkdir -p "$(ICLOUD_DIR)/programme"
	@for p in programme_summary introduction_full_survey; do \
		[ -f $(OUT_DIR)/$$p.pdf ] && cp $(OUT_DIR)/$$p.pdf "$(ICLOUD_DIR)/programme/$$p.pdf" \
			&& echo "    ✓ programme/$$p" || true; \
	done
	@# --- Legacy / notes ---
	@mkdir -p "$(ICLOUD_DIR)/notes"
	@for p in shadow_towers shadow_towers_v2 classification classification_trichotomy \
		computations riccati w3_holographic_datum bp_self_duality three_parameter_hbar \
		virasoro_r_matrix gaudin_from_collision chiral_chern_weil garland_lepowsky \
		N1_koszul_meta N2_mc3_all_types N3_e1_primacy N4_mc4_completion \
		N5_mc5_sewing N6_shadow_formality; do \
		[ -f $(OUT_DIR)/$$p.pdf ] && cp $(OUT_DIR)/$$p.pdf "$(ICLOUD_DIR)/notes/$$p.pdf" \
			&& echo "    ✓ notes/$$p" || true; \
	done
	@echo "  Vol I PDFs copied to iCloud (5 folders)."

## volume: Build the normative volume → out/reconstruction.pdf
##   THE mathematically current root: reconstruction/reconstruction.tex.
##   Merges the four PDF witnesses plus the repository corpus, in EB Garamond.
##   `make skeleton` builds the earlier 8-chapter spine (superseded);
##   `make legacy-manuscript` builds the retracted architecture.
##   See PORT_LEDGER.md.
volume:
	@echo "  ── Building the normative volume (reconstruction) ──"
	@mkdir -p $(OUT_DIR) $(LOG_DIR)
	@cd $(RECON_DIR) && \
	  TEXINPUTS=".:..:$$TEXINPUTS" BIBINPUTS=".:..:$$BIBINPUTS" \
	  $(TEX) $(TEXFLAGS) $(RECON).tex >../$(LOG_DIR)/$(RECON).log 2>&1 || true; \
	  TEXINPUTS=".:..:$$TEXINPUTS" BIBINPUTS=".:..:$$BIBINPUTS" \
	  bibtex $(RECON) >>../$(LOG_DIR)/$(RECON).log 2>&1 || true; \
	  for i in 1 2 3; do \
	    TEXINPUTS=".:..:$$TEXINPUTS" BIBINPUTS=".:..:$$BIBINPUTS" \
	    $(TEX) $(TEXFLAGS) $(RECON).tex >../$(LOG_DIR)/$(RECON).log 2>&1 || true; \
	  done
	@if [ -f $(RECON_DIR)/$(RECON).pdf ]; then \
		cp $(RECON_DIR)/$(RECON).pdf $(OUT_DIR)/$(RECON).pdf; \
		echo "    ✓ out/$(RECON).pdf ($$(pdfinfo $(RECON_DIR)/$(RECON).pdf 2>/dev/null | awk '/^Pages/{print $$2}') pages)"; \
	else \
		echo "    ✗ build failed — see $(LOG_DIR)/$(RECON).log"; exit 1; \
	fi
	@if grep -aqE '^! ' $(LOG_DIR)/$(RECON).log; then \
		echo "    ⚠  LaTeX errors present:"; grep -aE '^! ' $(LOG_DIR)/$(RECON).log | head -5; exit 1; \
	fi
	@if grep -aqE 'Reference .* undefined|Citation .* undefined' $(LOG_DIR)/$(RECON).log; then \
		echo "    ⚠  undefined references or citations:"; \
		grep -aE 'Reference .* undefined|Citation .* undefined' $(LOG_DIR)/$(RECON).log | head -5; exit 1; \
	fi
	@echo "    0 errors, 0 undefined references, 0 undefined citations."

## geometry: Build the 408-page revision → out/geometry.pdf
##   Refuses unless every \input target resolves.  46 of its 53 sources are
##   not present; see reconstruction/MISSING_SOURCES.md.
geometry:
	@echo "  ── Building the 408-page revision (geometry) ──"
	@mkdir -p $(OUT_DIR) $(LOG_DIR)
	@missing=0; \
	for f in $$(grep -oE '\\(input|inputaschapter)\{[^}]+\}' $(RECON_DIR)/geometry.tex \
	           | sed 's/.*{\(.*\)}/\1/' | sort -u); do \
	  if [ ! -f "$(RECON_DIR)/$$f.tex" ]; then \
	    if [ $$missing -eq 0 ]; then echo "    missing sources:"; fi; \
	    echo "      $$f.tex"; missing=$$((missing+1)); \
	  fi; \
	done; \
	if [ $$missing -gt 0 ]; then \
	  echo "    ✗ $$missing source file(s) absent — not building a partial document."; \
	  echo "      See $(RECON_DIR)/MISSING_SOURCES.md.  Use \`make volume\` (104pp) meanwhile."; \
	  exit 1; \
	fi
	@cd $(RECON_DIR) && \
	  TEXINPUTS=".:..:$$TEXINPUTS" BIBINPUTS=".:..:$$BIBINPUTS" \
	  $(TEX) $(TEXFLAGS) geometry.tex >../$(LOG_DIR)/geometry.log 2>&1 || true; \
	  for i in 1 2 3; do \
	    TEXINPUTS=".:..:$$TEXINPUTS" BIBINPUTS=".:..:$$BIBINPUTS" \
	    $(TEX) $(TEXFLAGS) geometry.tex >../$(LOG_DIR)/geometry.log 2>&1 || true; \
	  done
	@if [ -f $(RECON_DIR)/geometry.pdf ]; then \
		cp $(RECON_DIR)/geometry.pdf $(OUT_DIR)/geometry.pdf; \
		echo "    ✓ out/geometry.pdf ($$(pdfinfo $(RECON_DIR)/geometry.pdf 2>/dev/null | awk '/^Pages/{print $$2}') pages)"; \
	else \
		echo "    ✗ build failed — see $(LOG_DIR)/geometry.log"; exit 1; \
	fi

## skeleton: Build the earlier 8-chapter normative spine → out/
##   Superseded by `make volume`; its unique results are merged there.
##   Retained because it is a self-contained, independently compiling account.
skeleton:
	@echo "  ── Building the 8-chapter spine ($(NEWVOL)) ──"
	@mkdir -p $(OUT_DIR) $(LOG_DIR)
	@for i in 1 2 3; do \
		$(TEX) $(TEXFLAGS) $(NEWVOL).tex >$(LOG_DIR)/$(NEWVOL).log 2>&1 || true; \
	done
	@if [ -f $(NEWVOL).pdf ]; then \
		cp $(NEWVOL).pdf $(OUT_DIR)/$(NEWVOL).pdf; \
		echo "    ✓ out/$(NEWVOL).pdf ($$(pdfinfo $(NEWVOL).pdf 2>/dev/null | awk '/^Pages/{print $$2}') pages)"; \
	else \
		echo "    ✗ build failed — see $(LOG_DIR)/$(NEWVOL).log"; exit 1; \
	fi
	@if grep -aqE '^! ' $(LOG_DIR)/$(NEWVOL).log; then \
		echo "    ⚠  LaTeX errors present:"; grep -aE '^! ' $(LOG_DIR)/$(NEWVOL).log | head -5; exit 1; \
	fi
	@echo "    0 errors."

## legacy-manuscript: Build the retracted-architecture manuscript → out/
##   Retained for reference and citation archaeology only. Its architecture
##   (Open Beilinson tower, Theorems A/B/C/D/H, the 5x5 kappa matrix) is
##   retracted by volume/no_go.tex. Do not build on it.
legacy-manuscript: $(STAMP)

## all: Full build — normative volume + manuscript + working notes → out/
all: volume skeleton $(STAMP) working-notes modular-koszul-core

## modular-koszul-core: Build the core standalone paper → out/
modular-koszul-core:
	@mkdir -p $(LOG_DIR) $(OUT_DIR)
	@if [ -f $(OUT_DIR)/modular_koszul_core.pdf ] && [ $(OUT_DIR)/modular_koszul_core.pdf -nt standalone/modular_koszul_core.tex ]; then \
		echo "  ✓  out/modular_koszul_core.pdf (up to date)"; \
	else \
		echo "  ── Building modular_koszul_core.tex ──"; \
		cd standalone && TEXINPUTS=".:..:$$TEXINPUTS" $(TEX) $(TEXFLAGS) modular_koszul_core.tex >../$(LOG_DIR)/standalone-modular_koszul_core.log 2>&1 && \
		TEXINPUTS=".:..:$$TEXINPUTS" $(TEX) $(TEXFLAGS) modular_koszul_core.tex >>../$(LOG_DIR)/standalone-modular_koszul_core.log 2>&1 && \
		cd .. && cp standalone/modular_koszul_core.pdf $(OUT_DIR)/ && \
		echo "  ✓  out/modular_koszul_core.pdf"; \
	fi

$(STAMP): $(SOURCES) $(BUILD_SCRIPT)
	@echo "══════════════════════════════════════════════════════════"
	@echo "  Building: $(MAIN).tex  →  $(PDF)"
	@echo "══════════════════════════════════════════════════════════"
	@$(BUILD_SCRIPT) $(PASSES)
	@if [ ! -f $(PDF) ]; then \
		echo "  ✗  Build failed — no PDF produced."; exit 1; \
	fi
	@touch $(STAMP)
	@echo ""
	@echo "  ✓  $(PDF) built successfully."
	@echo ""

$(PDF): $(STAMP)
	@true

## fast: Bounded quick build for rapid iteration → out/main.pdf
fast:
	@echo "  ── Fast build (up to $(FAST_PASSES) passes) ──"
	@$(BUILD_SCRIPT) $(FAST_PASSES)

## working-notes: Build the working notes → out/working_notes.pdf
working-notes:
	@echo "  ── Building working notes ──"
	@mkdir -p $(OUT_DIR) $(LOG_DIR)
	@$(TEX) $(TEXFLAGS) $(WN_TEX) >/dev/null 2>&1 || true
	@$(TEX) $(TEXFLAGS) $(WN_TEX) >/dev/null 2>&1 || true
	@if [ -f working_notes.pdf ]; then \
		mv working_notes.pdf $(OUT_DIR)/working_notes.pdf; \
		rm -f working_notes.aux working_notes.log working_notes.out working_notes.toc 2>/dev/null; \
		echo "  ✓  $(OUT_DIR)/working_notes.pdf"; \
	else \
		echo "  ✗  Working notes build failed."; \
		exit 1; \
	fi

## release: Full rebuild — manuscript + working notes + standalone → out/ + iCloud
release:
	@rm -f $(STAMP)
	@rm -rf $(OUT_DIR)
	@mkdir -p $(LOG_DIR) $(OUT_DIR)
	@echo ""
	@echo "  ══════════════════════════════════════════"
	@echo "  ── RELEASE BUILD ──"
	@echo "  ══════════════════════════════════════════"
	@echo ""
	@echo "  [1/6] Manuscript"
	@$(BUILD_SCRIPT) $(FAST_PASSES)
	@if [ ! -f $(PDF) ]; then echo "  ✗  Manuscript build failed: $(PDF) not produced."; exit 1; fi
	@echo "  ✓  $(PDF)"
	@echo ""
	@echo "  [2/6] Working notes"
	@$(MAKE) --no-print-directory working-notes
	@echo ""
	@echo "  [3/6] Publish to repo root (canonical PDF name)"
	@$(MAKE) --no-print-directory root-publish
	@echo ""
	@echo "  [4/6] Publish to ~/mathematics + per-volume architecture"
	@$(MAKE) --no-print-directory mathematics-publish
	@$(MAKE) --no-print-directory architecture
	@echo ""
	@echo "  [5/6] Cross-volume architecture aggregation"
	@$(MAKE) --no-print-directory unified-architecture
	@echo ""
	@echo "  [6/6] Standalone papers and iCloud (non-fatal)"
	@$(MAKE) --no-print-directory icloud || echo "  ⚠  some standalones / iCloud copies failed — manuscript + architecture artifacts already current"
	@echo ""
	@echo "  ══════════════════════════════════════════"
	@echo "  Release complete. All output in out/:"
	@ls -1 $(OUT_DIR)/*.pdf 2>/dev/null | sed 's/^/    /'
	@echo "  ══════════════════════════════════════════"

## root-publish: Copy the release binary to repo root under its canonical name
root-publish:
	@if [ -f "$(PDF)" ]; then \
		cp "$(PDF)" "$(PUBLISHED_PDF)"; \
		echo "    ✓  $(PUBLISHED_PDF) (in repo root)"; \
	else \
		echo "    ✗  $(PDF) missing — skipping root publish"; \
	fi

## mathematics-publish: Copy the release binary to ~/mathematics under its canonical name
mathematics-publish:
	@mkdir -p "$(MATHEMATICS_DIR)"
	@if [ -f "$(PDF)" ]; then \
		cp "$(PDF)" "$(MATHEMATICS_DIR)/$(PUBLISHED_PDF)"; \
		echo "    ✓  $(MATHEMATICS_DIR)/$(PUBLISHED_PDF)"; \
	else \
		echo "    ✗  $(PDF) missing — skipping ~/mathematics publish"; \
	fi

## architecture: Build interactive HTML + JSON of the manuscript architecture
architecture:
	@$(PYTHON_BIN) scripts/build_architecture.py --root . --volume $(VOLUME_KEY) --out $(OUT_DIR) --quiet
	@mkdir -p "$(MATHEMATICS_DIR)/architecture"
	@cp "$(OUT_DIR)/architecture.json" "$(MATHEMATICS_DIR)/architecture/$(VOLUME_KEY).json"
	@echo "    ✓  $(OUT_DIR)/architecture.html + .json"
	@echo "    ✓  $(MATHEMATICS_DIR)/architecture/$(VOLUME_KEY).json"

## unified-architecture: Aggregate all per-volume architecture.json into the cross-volume HTML+JSON
unified-architecture:
	@$(PYTHON_BIN) scripts/build_unified_architecture.py --mathematics-dir "$(MATHEMATICS_DIR)" --quiet
	@echo "    ✓  $(MATHEMATICS_DIR)/architecture.html + .json"

## watch: Continuous rebuild on save (requires latexmk).
watch:
	@command -v $(LATEXMK) >/dev/null 2>&1 || \
		{ echo "Error: latexmk not found. Install via: brew install --cask mactex"; exit 1; }
	$(LATEXMK) $(MKFLAGS) -pvc $(MAIN).tex

## check: Halt on first error — use for CI or pre-commit validation.
check:
	@echo "  ── Error check (halt-on-error) ──"
	@mkdir -p $(LOG_DIR)
	@$(TEX) -interaction=nonstopmode -halt-on-error -file-line-error $(MAIN).tex >$(LOG_DIR)/check.log 2>&1 || { \
		echo "  ✗  Check failed. See $(LOG_DIR)/check.log"; \
		grep -aE '^! |Emergency stop|Runaway argument|Fatal error|Undefined control sequence|File ended while scanning|No pages of output' $(LOG_DIR)/check.log | head -n 20 || tail -n 40 $(LOG_DIR)/check.log; \
		exit 1; \
	}
	@echo "  ✓  No fatal errors."
	@echo "     Log: $(LOG_DIR)/check.log"

## integrity: Strict manuscript integrity gate (clean rebuild + diagnostics + claim-tag coverage).
integrity:
	@./scripts/integrity_gate.sh

## phase0-index: Regenerate active-theory theorem dependency index.
phase0-index:
	@./scripts/generate_theorem_dependency_index.py

## draft: Build with draft class option (skips image rendering, faster).
draft:
	@echo "  ── Draft build ──"
	@mkdir -p $(LOG_DIR)
	@$(TEX) $(TEXFLAGS) "\PassOptionsToClass{draft}{memoir}\input{$(MAIN)}" >$(LOG_DIR)/draft.log 2>&1 || { \
		echo "  ✗  Draft build failed. See $(LOG_DIR)/draft.log"; \
		grep -aE '^! |Emergency stop|Runaway argument|Fatal error|Undefined control sequence|File ended while scanning|No pages of output' $(LOG_DIR)/draft.log | head -n 20 || tail -n 40 $(LOG_DIR)/draft.log; \
		exit 1; \
	}
	@echo "  ✓  Draft build complete."
	@echo "     Log: $(LOG_DIR)/draft.log"

## clean: Remove build debris (aux, log, etc.) but preserve the build stamp.
clean:
	@echo "  Cleaning build artifacts..."
	@for ext in $(AUX_EXTS); do \
		rm -f $(MAIN).$$ext; \
	done
	@find chapters appendices bibliography -name '*.aux' -delete 2>/dev/null || true
	@rm -rf $(LOG_DIR)
	@rm -f texput.log
	@echo "  ✓  Clean (stamp preserved — make will skip rebuild if sources unchanged)."

## veryclean: Remove EVERYTHING including out/ and build stamp (forces full rebuild).
veryclean: clean
	@rm -f $(STAMP)
	@rm -rf $(OUT_DIR)
	@echo "  ✓  Stamp and out/ removed — next make will rebuild."

## clean-builds: Remove ALL /tmp/mkd-* isolated build directories (all volumes).
clean-builds:
	@echo "  Cleaning isolated build directories..."
	@rm -rf /tmp/mkd-chiral-bar-cobar-* /tmp/mkd-chiral-bar-cobar-vol2-* /tmp/mkd-calabi-yau-quantum-groups-*
	@echo "  ✓  All /tmp/mkd-* build directories removed."

## count: Manuscript statistics.
count:
	@echo ""
	@echo "  ── Manuscript Statistics ──"
	@echo ""
	@printf "  Source files:   %s .tex files\n" "$$(find . -name '*.tex' -not -path './archive/*' -not -path './out/*' | wc -l | tr -d ' ')"
	@printf "  Total lines:   %s\n" "$$(find . -name '*.tex' -not -path './archive/*' -not -path './out/*' -exec cat {} + | wc -l | tr -d ' ')"
	@if [ -f $(PDF) ]; then \
		PAGES=$$(strings $(PDF) | grep -c '/Type /Page' 2>/dev/null || echo '?'); \
		printf "  PDF pages:     %s\n" "$$PAGES"; \
		printf "  PDF size:      %s\n" "$$(du -h $(PDF) | cut -f1)"; \
	else \
		echo "  PDF:           (not yet built — run 'make')"; \
	fi
	@echo ""

## metadata: Regenerate metadata artefacts and the proved-claim registry from .tex sources.
metadata:
	@echo "  ── Generating metadata ──"
	@$(PYTHON_BIN) scripts/generate_metadata.py

## census: Print claim census from generated metadata.
census: metadata
	@$(PYTHON_BIN) -c "import json; d=json.load(open('metadata/census.json')); t=d['totals']; print(f'  PH={t[\"ProvedHere\"]} PE={t[\"ProvedElsewhere\"]} CJ={t[\"Conjectured\"]} H={t[\"Heuristic\"]} O={t[\"Open\"]} total={t[\"total_claims\"]}')"

## audit: Run Beilinson proof-chain integrity audit on theorem dependency DAG.
audit: metadata
	@$(PYTHON_BIN) -c "from compute.lib.beilinson_auditor import BeilinsonAuditor; a = BeilinsonAuditor('.'); r = a.run_audit(); print(a.format_report(r))"

## verify: Run anti-pattern verification on all .tex files.
verify:
	@./scripts/verify_edit.sh --all

## test: Run fast test suite (excludes @pytest.mark.slow).  Use for rapid iteration.
test:
	@if [ -d compute/tests ] && ls compute/tests/test_*.py 1>/dev/null 2>&1; then \
		echo "  ── Running compute test suite (fast: excludes slow) ──"; \
		mkdir -p $(LOG_DIR); \
		if [ -f compute/.venv/bin/python ]; then \
			PYTHON_BIN=compute/.venv/bin/python; \
		elif [ -f .venv/bin/python ]; then \
			PYTHON_BIN=.venv/bin/python; \
		else \
			PYTHON_BIN=python3; \
		fi; \
		LOG_FILE=$(LOG_DIR)/pytest.log; \
		$$PYTHON_BIN -m pytest compute/tests/ -q -ra -m "not slow" \
			-o faulthandler_timeout=$(PYTEST_FAST_TIMEOUT) \
			-o faulthandler_exit_on_timeout=true \
			--durations=10 --durations-min=1.0 >$$LOG_FILE 2>&1; rc=$$?; \
		if [ $$rc -eq 0 ]; then \
			tail -n 5 $$LOG_FILE; \
			echo "     Log: $$LOG_FILE"; \
		else \
			echo "  ✗  Test run failed. See $$LOG_FILE"; \
			tail -n 120 $$LOG_FILE; \
			exit $$rc; \
		fi; \
	else \
		echo "  (no compute tests found — skipping)"; \
	fi

## verify-independence: Audit ProvedHere claims vs independent-verification registry
##                     (tautology / orphan check; coverage metric reported)
verify-independence:
	@$(PYTHON_BIN) compute/scripts/audit_independent_verification.py

## verify-independence-verbose: Same, with full list of uncovered claims
verify-independence-verbose:
	@$(PYTHON_BIN) compute/scripts/audit_independent_verification.py --verbose --show-orphans

## test-full: Run the complete test suite including slow tests.  Use before commits.
test-full:
	@if [ -d compute/tests ] && ls compute/tests/test_*.py 1>/dev/null 2>&1; then \
		echo "  ── Running FULL compute test suite (including slow) ──"; \
		mkdir -p $(LOG_DIR); \
		if [ -f compute/.venv/bin/python ]; then \
			PYTHON_BIN=compute/.venv/bin/python; \
		elif [ -f .venv/bin/python ]; then \
			PYTHON_BIN=.venv/bin/python; \
		else \
			PYTHON_BIN=python3; \
		fi; \
		LOG_FILE=$(LOG_DIR)/pytest-full.log; \
		$$PYTHON_BIN compute/scripts/run_full_pytest.py \
			--python-bin $$PYTHON_BIN \
			--log-dir $(LOG_DIR) \
			--state-dir $(PYTEST_FULL_STATE_DIR) \
			--faulthandler-timeout $(PYTEST_FULL_TIMEOUT) \
			--heartbeat-seconds $(PYTEST_FULL_HEARTBEAT) \
			--max-nodeids-per-shard $(PYTEST_FULL_NODEIDS_PER_SHARD) \
			--target-seconds-per-shard $(PYTEST_FULL_TARGET_SHARD_SECONDS) \
			compute/tests/; rc=$$?; \
		if [ $$rc -eq 0 ]; then \
			tail -n 5 $$LOG_FILE; \
			echo "     Log: $$LOG_FILE"; \
		else \
			echo "  ✗  Test run failed. See $$LOG_FILE"; \
			tail -n 120 $$LOG_FILE; \
			exit $$rc; \
		fi; \
	else \
		echo "  (no compute tests found — skipping)"; \
	fi

## dist: Create Vol1Archive.zip for distribution.
dist: working-notes
	@echo "  ── Creating Vol1Archive.zip ──"
	@rm -f $(OUT_DIR)/Vol1Archive.zip
	@mkdir -p $(OUT_DIR)
	@zip -r $(OUT_DIR)/Vol1Archive.zip \
		main.tex chapters/ appendices/ bibliography/ scripts/ compute/ \
		Makefile README.md CLAUDE.md \
		$(PDF) \
		$(OUT_DIR)/working_notes.pdf \
		-x '.*' -x '**/.*' -x '**/__pycache__/*' -x '**/*.pyc' \
		-x 'compute/.venv/*' -x 'compute/state/*' \
		>$(LOG_DIR)/dist.log 2>&1
	@echo "  ✓  $(OUT_DIR)/Vol1Archive.zip ($$(du -h $(OUT_DIR)/Vol1Archive.zip | cut -f1))"

## standalone: Build ALL standalone papers → out/
standalone:
	@echo "  ── Building standalone papers ──"
	@mkdir -p $(LOG_DIR) $(OUT_DIR)
	@failures=0; \
	for paper in \
		modular_koszul_core \
		shadow_towers shadow_towers_v2 shadow_towers_v3 \
		seven_faces classification_trichotomy virasoro_r_matrix \
		w3_holographic_datum bp_self_duality three_parameter_hbar \
		gaudin_from_collision genus1_seven_faces \
		introduction_full_survey survey_modular_koszul_duality \
		survey_modular_koszul_duality_v2 \
		survey_track_a_compressed survey_track_b_compressed \
		chiral_chern_weil ordered_chiral_homology \
		five_theorems_modular_koszul e1_primacy_ordered_bar \
		en_chiral_operadic_circle koszulness_fourteen_characterizations \
		determinant_of_an_operator \
		drinfeld_kohno_bridge sc_chtop_pva_descent \
		three_dimensional_quantum_gravity \
		arithmetic_shadows multi_weight_cross_channel \
		holographic_datum analytic_sewing \
		cy_to_chiral_functor cy_quantum_groups_6d_hcs \
		N1_koszul_meta N2_mc3_all_types N3_e1_primacy \
		N4_mc4_completion N5_mc5_sewing N6_shadow_formality \
		classification computations garland_lepowsky riccati \
		programme_summary programme_summary_section1 \
		programme_summary_sections2_4 programme_summary_sections5_8 \
		programme_summary_sections9_14; do \
	if [ -f standalone/$$paper.tex ]; then \
		if [ -f $(OUT_DIR)/$$paper.pdf ] && [ $(OUT_DIR)/$$paper.pdf -nt standalone/$$paper.tex ] && [ $(OUT_DIR)/$$paper.pdf -nt raeez-math-template.sty ]; then \
			echo "    ✓  out/$$paper.pdf (up to date)"; \
			continue; \
		fi; \
		echo "    Building $$paper.tex ..."; \
		rm -f standalone/$$paper.pdf; \
		build_failed=0; \
		cd standalone && TEXINPUTS=".:..:$$TEXINPUTS"; export TEXINPUTS; for i in 1 2 3; do \
			if ! $(TEX) $(TEXFLAGS) $$paper.tex >../$(LOG_DIR)/standalone-$$paper.log 2>&1; then \
				if grep -aE '(^! |Undefined control sequence|LaTeX Error|Package .* Error|Emergency stop|Fatal error|Runaway argument|File ended while scanning|No pages of output|Double subscript|Double superscript|Missing \{|Missing \})' ../$(LOG_DIR)/standalone-$$paper.log >/dev/null 2>&1; then \
					build_failed=1; \
					break; \
				fi; \
			fi; \
		done; cd ..; \
		if [ $$build_failed -eq 0 ] && [ -f standalone/$$paper.pdf ]; then \
			mv standalone/$$paper.pdf $(OUT_DIR)/$$paper.pdf; \
			rm -f standalone/$$paper.aux standalone/$$paper.log standalone/$$paper.out standalone/$$paper.toc 2>/dev/null; \
			echo "    ✓  out/$$paper.pdf"; \
		else \
			echo "    ✗  $$paper build failed. See $(LOG_DIR)/standalone-$$paper.log"; \
			failures=$$((failures + 1)); \
		fi; \
	fi; \
	done; \
	if [ $$failures -ne 0 ]; then \
		echo "  ✗  $$failures standalone paper(s) failed."; \
		exit 1; \
	fi

## editorial: Build the editorial companion → out/editorial.pdf
editorial:
	@echo "  ── Building editorial companion ──"
	@mkdir -p $(LOG_DIR) $(OUT_DIR)
	@for i in 1 2 3; do \
		$(TEX) $(TEXFLAGS) -output-directory=standalone standalone/editorial.tex >$(LOG_DIR)/editorial.log 2>&1 || true; \
	done
	@if [ -f standalone/editorial.pdf ]; then \
		mv standalone/editorial.pdf $(OUT_DIR)/editorial.pdf; \
		rm -f standalone/editorial.aux standalone/editorial.log standalone/editorial.out 2>/dev/null; \
		echo "  ✓  $(OUT_DIR)/editorial.pdf"; \
	else \
		echo "  ✗  Editorial build failed. See $(LOG_DIR)/editorial.log"; \
		exit 1; \
	fi

## help: Show available targets.
help:
	@echo ""
	@echo "  Chiral Bar-Cobar Duality — Build System"
	@echo "  ────────────────────────────────────────"
	@echo "  All compiled output goes to out/"
	@echo ""
	@echo "  make               Full build: manuscript + working notes → out/"
	@echo "  make fast           Quick converging build (up to $(FAST_PASSES) passes) → out/"
	@echo "  make working-notes  Build working notes → out/working_notes.pdf"
	@echo "  make release        Full release: manuscript + working notes + standalone → out/"
	@echo "  make standalone     Build standalone papers → out/"
	@echo "  make dist           Create Vol1Archive.zip in out/"
	@echo "  make watch          Continuous rebuild on save (latexmk)"
	@echo "  make check          Halt-on-error validation"
	@echo "  make integrity      Strict CI-style integrity gate"
	@echo "  make phase0-index   Regenerate theorem dependency index"
	@echo "  make draft          Draft mode (faster, no images)"
	@echo "  make clean          Remove build debris (preserves stamp)"
	@echo "  make veryclean      Remove everything including out/ (forces rebuild)"
	@echo "  make clean-builds   Remove /tmp/mkd-* isolated build directories"
	@echo "  make count          Manuscript statistics"
	@echo "  make metadata       Regenerate machine-readable metadata"
	@echo "  make census         Print claim census"
	@echo "  make editorial      Build editorial companion → out/"
	@echo "  make verify         Run anti-pattern verification"
	@echo "  make test           Fast tests (excludes slow — for rapid iteration)"
	@echo "  make test-full      Full test suite (including slow — before commits)"
	@echo "  make help           This message"
	@echo ""
