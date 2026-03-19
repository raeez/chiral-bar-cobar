# ============================================================================
#  Makefile — Chiral Bar-Cobar Duality Monograph
# ============================================================================
#
#  Usage:
#    make            Build the manuscript (default: pdflatex, 5 passes)
#    make fast       Single-pass build for quick iteration
#    make watch      Continuous rebuild on file changes (requires latexmk)
#    make clean      Remove all LaTeX build artifacts
#    make veryclean  Remove artifacts AND compiled PDFs
#    make count      Line counts and page estimate
#    make check      Dry-run compilation to check for errors
#    make draft      Build with draft mode (faster, no images)
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

.PHONY: all fast watch clean veryclean count check draft integrity phase0-index metadata verify census test editorial help

## all: Full build — up to PASSES pdflatex passes, stopping when converged.
##   Idempotent: no-op if no .tex files changed since last successful build.
##   `make clean` removes debris but preserves the stamp, so `make` after
##   `make clean` is still a no-op when sources are unchanged.
all: $(STAMP)

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

## veryclean: Remove EVERYTHING including PDF and build stamp (forces full rebuild).
veryclean: clean
	@rm -f $(MAIN).pdf $(STAMP)
	@echo "  ✓  Stamp and PDF removed — next make will rebuild."

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
	@echo "  make            Full build ($(PASSES) passes, stable cross-refs)"
	@echo "  make fast       Quick converging build (up to $(FAST_PASSES) passes)"
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
