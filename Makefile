# ============================================================================
#  Makefile — Modular Koszul Duality (Vol I)
# ============================================================================
#
#  Usage:
#    make               Build everything: manuscript + working notes → out/
#    make fast           Single-pass build for quick iteration
#    make release        Full release: annals + archive + working notes + standalone → out/
#    make standalone     Build standalone paper → out/shadow_towers.pdf
#    make annals         Build annals edition (frontier quarantined)
#    make archive        Build archive edition (full content visible)
#    make working-notes  Build working notes only → out/
#    make watch          Continuous rebuild on file changes (requires latexmk)
#    make clean          Remove all LaTeX build artifacts
#    make veryclean      Remove artifacts AND compiled PDFs
#    make count          Line counts and page estimate
#    make check          Dry-run compilation to check for errors
#    make draft          Build with draft mode (faster, no images)
#
# ============================================================================

# --- Configuration -----------------------------------------------------------

MAIN      := main
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

# Output
PDF       := $(MAIN).pdf
OUT_DIR   := out
OUT_PDF   := $(OUT_DIR)/modular_koszul_duality.pdf

# Working notes
WN_DIR    := .
WN_TEX    := $(WN_DIR)/working_notes.tex
WN_PDF    := $(WN_DIR)/working_notes.pdf
OUT_WN    := $(OUT_DIR)/working_notes.pdf

# Stamp file: tracks last successful build. Survives `make clean` so that
# make can skip recompilation when no .tex files have changed.
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

.PHONY: all fast watch clean veryclean count check draft integrity phase0-index metadata verify census test editorial standalone annals archive dist release help working-notes publish icloud

## icloud: Copy latest PDFs to iCloud Drive
icloud: main.pdf
	@mkdir -p "$(ICLOUD_DIR)"
	@cp -v main.pdf "$(ICLOUD_DIR)/vol1_modular_koszul_duality.pdf"
	@for f in standalone/*.pdf; do [ -f "$$f" ] && cp -v "$$f" "$(ICLOUD_DIR)/$$(basename $$f)" || true; done
	@echo "Vol I PDFs copied to iCloud."

## all: Full build — manuscript + working notes → out/
##   Builds the main manuscript (stamp-based, idempotent), the working notes,
##   and copies final PDFs to out/.
all: $(STAMP) working-notes publish

$(STAMP): $(SOURCES) $(BUILD_SCRIPT)
	@echo "══════════════════════════════════════════════════════════"
	@echo "  Building: $(MAIN).tex  →  $(PDF)"
	@echo "  Engine:   quiet $(TEX) wrapper (up to $(PASSES) passes)"
	@echo "══════════════════════════════════════════════════════════"
	@mkdir -p $(LOG_DIR)
	@$(BUILD_SCRIPT) $(PASSES)
	@if [ ! -f $(MAIN).pdf ]; then \
		echo "  ✗  Build failed — no PDF produced."; exit 1; \
	fi
	@touch $(STAMP)
	@echo ""
	@echo "  ✓  $(PDF) built successfully."
	@echo "     Logs: $(LOG_DIR)/tex-build.stdout.log and $(MAIN).log"
	@echo ""

## fast: Bounded quick build for rapid iteration.
##   Runs enough passes to settle references in normal editing flows, while
##   still capping the work below the full build target.
fast:
	@echo "  ── Fast build (up to $(FAST_PASSES) passes) ──"
	@mkdir -p $(LOG_DIR)
	@$(BUILD_SCRIPT) $(FAST_PASSES)
	@echo "     Logs: $(LOG_DIR)/tex-build.stdout.log and $(MAIN).log"

## working-notes: Build the working notes (standalone document).
working-notes: $(OUT_WN)

$(OUT_WN): $(WN_TEX)
	@echo "  ── Building working notes ──"
	@mkdir -p $(OUT_DIR) $(LOG_DIR)
	@cd $(WN_DIR) && \
		$(TEX) $(TEXFLAGS) working_notes.tex >/dev/null 2>&1 || true && \
		$(TEX) $(TEXFLAGS) working_notes.tex >/dev/null 2>&1 || true
	@if [ -f $(WN_PDF) ]; then \
		cp $(WN_PDF) $(OUT_WN); \
		echo "  ✓  $(OUT_WN)"; \
	else \
		echo "  ✗  Working notes build failed."; \
		exit 1; \
	fi

## publish: Copy final PDFs to out/ (does not trigger a rebuild).
publish:
	@mkdir -p $(OUT_DIR)
	@if [ -f $(PDF) ]; then cp $(PDF) $(OUT_PDF); echo "  ✓  $(OUT_PDF)"; \
	else echo "  ⚠  $(PDF) not found — run 'make fast' first."; fi

## release: Full rebuild of everything — annals + archive + working notes + standalone → out/ + root + iCloud
release:
	@rm -f $(STAMP) $(PDF) $(WN_PDF)
	@rm -rf $(OUT_DIR)
	@mkdir -p $(LOG_DIR) $(OUT_DIR)
	@echo ""
	@echo "  ══════════════════════════════════════════"
	@echo "  ── RELEASE BUILD ──"
	@echo "  ══════════════════════════════════════════"
	@echo ""
	@echo "  [1/4] Annals edition (frontier quarantined, claim-status tags suppressed)"
	@$(BUILD_SCRIPT) $(FAST_PASSES)
	@if [ -f $(PDF) ]; then \
		cp $(PDF) $(OUT_DIR)/modular_koszul_duality_annals.pdf; \
		cp $(PDF) Chiral_Bar_Cobar_Duality__Geometric_Realization.pdf; \
		cp $(PDF) modular_koszul_duality_annals.pdf; \
		echo "  ✓  out/modular_koszul_duality_annals.pdf"; \
	else \
		echo "  ✗  Annals build failed."; \
	fi
	@echo ""
	@echo "  [2/4] Archive edition (full content, all frontiers visible)"
	@for i in $$(seq 1 $(FAST_PASSES)); do \
		$(TEX) $(TEXFLAGS) "\def\archivebuild{1}\input{$(MAIN)}" >$(LOG_DIR)/tex-build.stdout.log 2>&1 || true; \
	done
	@if [ -f $(PDF) ]; then \
		cp $(PDF) $(OUT_DIR)/modular_koszul_duality_archive.pdf; \
		cp $(PDF) modular_koszul_duality_archive.pdf; \
		echo "  ✓  out/modular_koszul_duality_archive.pdf"; \
	else \
		echo "  ✗  Archive build failed."; \
	fi
	@echo ""
	@echo "  [3/4] Working notes"
	@$(MAKE) --no-print-directory working-notes
	@if [ -f $(OUT_WN) ]; then cp $(OUT_WN) working_notes.pdf; echo "  ✓  working_notes.pdf (root)"; fi
	@echo ""
	@echo "  [4/4] Standalone papers"
	@$(MAKE) --no-print-directory standalone
	@for pdf in $(OUT_DIR)/*.pdf; do \
		name=$$(basename "$$pdf"); \
		case "$$name" in \
			modular_koszul_duality_annals.pdf|modular_koszul_duality_archive.pdf|working_notes.pdf) ;; \
			*) if [ -f "$$pdf" ]; then cp "$$pdf" "$$name"; echo "  ✓  $$name (root)"; fi ;; \
		esac; \
	done
	@echo ""
	@echo "  ── Copying to iCloud ──"
	@mkdir -p "$(ICLOUD_DIR)"
	@for pdf in $(OUT_DIR)/*.pdf; do \
		name=$$(basename "$$pdf"); \
		if [ -f "$$pdf" ]; then \
			case "$$name" in \
				working_notes.pdf) \
					cp "$$pdf" "$(ICLOUD_DIR)/working_notes_vol1.pdf"; \
					echo "    ✓  working_notes_vol1.pdf" ;; \
				*) \
					cp "$$pdf" "$(ICLOUD_DIR)/$$name"; \
					echo "    ✓  $$name" ;; \
			esac; \
		fi; \
	done
	@if [ -f Chiral_Bar_Cobar_Duality__Geometric_Realization.pdf ]; then \
		cp Chiral_Bar_Cobar_Duality__Geometric_Realization.pdf "$(ICLOUD_DIR)/"; \
		echo "    ✓  Chiral_Bar_Cobar_Duality__Geometric_Realization.pdf"; \
	fi
	@echo ""
	@echo "  ══════════════════════════════════════════"
	@echo "  Release complete. Output in out/:"
	@ls -1 $(OUT_DIR)/*.pdf 2>/dev/null | sed 's/^/    /'
	@echo "  Root copies:"
	@ls -1 *.pdf 2>/dev/null | grep -v main.pdf | sed 's/^/    /'
	@echo "  iCloud copies:"
	@ls -1 "$(ICLOUD_DIR)"/*.pdf 2>/dev/null | sed 's/^/    /'
	@echo "  ══════════════════════════════════════════"

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
##   Idempotent — safe to spam. After `make clean`, `make` is a no-op if
##   no .tex files changed since the last successful build.
clean:
	@echo "  Cleaning build artifacts..."
	@for ext in $(AUX_EXTS); do \
		rm -f $(MAIN).$$ext; \
	done
	@find chapters appendices bibliography -name '*.aux' -delete 2>/dev/null || true
	@rm -rf $(LOG_DIR)
	@rm -f texput.log
	@echo "  ✓  Clean (stamp preserved — make will skip rebuild if sources unchanged)."

## veryclean: Remove EVERYTHING including PDF, out/, and build stamp (forces full rebuild).
veryclean: clean
	@rm -f $(MAIN).pdf $(STAMP) $(WN_PDF)
	@rm -rf $(OUT_DIR)
	@echo "  ✓  Stamp, PDFs, and out/ removed — next make will rebuild."

## count: Manuscript statistics.
count:
	@echo ""
	@echo "  ── Manuscript Statistics ──"
	@echo ""
	@printf "  Source files:   %s .tex files\n" "$$(find . -name '*.tex' -not -path './archive/*' | wc -l | tr -d ' ')"
	@printf "  Total lines:   %s\n" "$$(find . -name '*.tex' -not -path './archive/*' -exec cat {} + | wc -l | tr -d ' ')"
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
	@python3 scripts/generate_metadata.py

## census: Print claim census from generated metadata.
census: metadata
	@python3 -c "import json; d=json.load(open('metadata/census.json')); t=d['totals']; print(f'  PH={t[\"ProvedHere\"]} PE={t[\"ProvedElsewhere\"]} CJ={t[\"Conjectured\"]} H={t[\"Heuristic\"]} O={t[\"Open\"]} total={t[\"total_claims\"]}')"

## audit: Run Beilinson proof-chain integrity audit on theorem dependency DAG.
audit: metadata
	@python3 -c "from compute.lib.beilinson_auditor import BeilinsonAuditor; a = BeilinsonAuditor('.'); r = a.run_audit(); print(a.format_report(r))"

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

## annals: Build the Annals edition (frontier quarantined, claim-status tags suppressed).
annals:
	@echo "  ── Annals edition build ──"
	@mkdir -p $(LOG_DIR)
	@$(BUILD_SCRIPT) $(FAST_PASSES)
	@echo "  ✓  Annals edition built (default: \\annalseditiontrue)."

## archive: Build the full archive edition (everything visible).
archive:
	@echo "  ── Archive edition build (full content) ──"
	@mkdir -p $(LOG_DIR)
	@for i in $$(seq 1 $(FAST_PASSES)); do \
		$(TEX) $(TEXFLAGS) "\def\archivebuild{1}\input{$(MAIN)}" >$(LOG_DIR)/tex-build.stdout.log 2>&1 || true; \
	done
	@echo "  ✓  Archive edition built (\\annalseditionfalse)."

## dist: Create Vol1Archive.zip for distribution.
dist: working-notes publish
	@echo "  ── Creating Vol1Archive.zip ──"
	@rm -f $(OUT_DIR)/Vol1Archive.zip
	@mkdir -p $(OUT_DIR)
	@zip -r $(OUT_DIR)/Vol1Archive.zip \
		main.tex chapters/ appendices/ bibliography/ scripts/ compute/ \
		Makefile README.md CLAUDE.md \
		$(OUT_DIR)/modular_koszul_duality.pdf \
		$(OUT_DIR)/working_notes.pdf \
		-x '.*' -x '**/.*' -x '**/__pycache__/*' -x '**/*.pyc' \
		-x 'compute/.venv/*' -x 'compute/state/*' \
		>$(LOG_DIR)/dist.log 2>&1
	@echo "  ✓  $(OUT_DIR)/Vol1Archive.zip ($$(du -h $(OUT_DIR)/Vol1Archive.zip | cut -f1))"

## standalone: Build ALL standalone papers → out/
standalone:
	@echo "  ── Building standalone papers ──"
	@mkdir -p $(LOG_DIR) $(OUT_DIR)
	@for paper in \
		shadow_towers shadow_towers_v2 \
		seven_faces classification_trichotomy virasoro_r_matrix \
		w3_holographic_datum bp_self_duality three_parameter_hbar \
		gaudin_from_collision genus1_seven_faces \
		introduction_full_survey survey_modular_koszul_duality \
		survey_modular_koszul_duality_v2 \
		survey_track_a_compressed survey_track_b_compressed \
		chiral_chern_weil ordered_chiral_homology \
		N1_koszul_meta N2_mc3_all_types N3_e1_primacy \
		N4_mc4_completion N5_mc5_sewing N6_shadow_formality \
		classification computations garland_lepowsky riccati \
		programme_summary programme_summary_section1 \
		programme_summary_sections2_4 programme_summary_sections5_8 \
		programme_summary_sections9_14; do \
		if [ -f standalone/$$paper.tex ]; then \
			echo "    Building $$paper.tex ..."; \
			cd standalone && for i in 1 2 3; do \
				$(TEX) $(TEXFLAGS) $$paper.tex >../$(LOG_DIR)/standalone-$$paper.log 2>&1 || true; \
			done && cd ..; \
			if [ -f standalone/$$paper.pdf ]; then \
				cp standalone/$$paper.pdf $(OUT_DIR)/$$paper.pdf; \
				echo "    ✓  out/$$paper.pdf"; \
			else \
				echo "    ✗  $$paper build failed. See $(LOG_DIR)/standalone-$$paper.log"; \
			fi; \
		fi; \
	done

## editorial: Build the editorial companion (concordance + editorial constitution).
editorial:
	@echo "  ── Building editorial companion ──"
	@mkdir -p $(LOG_DIR)
	@for i in 1 2 3; do \
		$(TEX) $(TEXFLAGS) -output-directory=standalone standalone/editorial.tex >$(LOG_DIR)/editorial.log 2>&1 || true; \
	done
	@if [ -f standalone/editorial.pdf ]; then \
		echo "  ✓  standalone/editorial.pdf built."; \
	else \
		echo "  ✗  Editorial build failed. See $(LOG_DIR)/editorial.log"; \
		exit 1; \
	fi

## help: Show available targets.
help:
	@echo ""
	@echo "  Chiral Bar-Cobar Duality — Build System"
	@echo "  ────────────────────────────────────────"
	@echo ""
	@echo "  make               Full build: manuscript + working notes → out/"
	@echo "  make fast           Quick converging build (up to $(FAST_PASSES) passes)"
	@echo "  make working-notes  Build working notes → out/working_notes.pdf"
	@echo "  make release        Full release: annals + archive + working notes + standalone → out/"
	@echo "  make standalone      Build standalone paper → out/shadow_towers.pdf"
	@echo "  make dist           Create Vol1Archive.zip in out/"
	@echo "  make watch      Continuous rebuild on save (latexmk)"
	@echo "  make check      Halt-on-error validation"
	@echo "  make integrity  Strict CI-style integrity gate"
	@echo "  make phase0-index  Regenerate theorem dependency index"
	@echo "  make draft      Draft mode (faster, no images)"
	@echo "  make clean      Remove build debris (idempotent, preserves stamp)"
	@echo "  make veryclean  Remove everything including PDF (forces rebuild)"
	@echo "  make count      Manuscript statistics"
	@echo "  make metadata   Regenerate machine-readable metadata"
	@echo "  make census     Print claim census"
	@echo "  make editorial  Build editorial companion (concordance + constitution)"
	@echo "  make verify     Run anti-pattern verification"
	@echo "  make test       Fast tests (excludes slow — for rapid iteration)"
	@echo "  make test-full  Full test suite (including slow — before commits)"
	@echo "  make help       This message"
	@echo ""
