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
TEXFLAGS  := -interaction=nonstopmode -file-line-error -synctex=0 -cnf-line='buf_size=1000000'
LATEXMK   := latexmk
MKFLAGS   := -pdf -pdflatex="$(TEX) $(TEXFLAGS)" -interaction=nonstopmode

# Number of passes for cross-references, TOC, and page numbers to stabilize.
PASSES    := 6

# Source files: every .tex file that main.tex transitively \input's or \include's.
SOURCES   := $(wildcard *.tex) \
             $(wildcard chapters/theory/*.tex) \
             $(wildcard chapters/examples/*.tex) \
             $(wildcard chapters/connections/*.tex) \
             $(wildcard appendices/*.tex) \
             $(wildcard bibliography/*.tex)

# Output
PDF       := $(MAIN).pdf

# LaTeX intermediate extensions
AUX_EXTS  := aux log out toc synctex.gz fdb_latexmk fls bbl blg \
             nav snm vrb idx ilg ind lof lot

# ============================================================================
#  Targets
# ============================================================================

.PHONY: all fast watch clean veryclean count check draft integrity phase0-index metadata verify census test help

## all: Full build — up to PASSES pdflatex passes, stopping when converged.
all: $(PDF)

$(PDF): $(SOURCES)
	@echo "══════════════════════════════════════════════════════════"
	@echo "  Building: $(MAIN).tex  →  $(PDF)"
	@echo "  Engine:   $(TEX) (up to $(PASSES) passes)"
	@echo "══════════════════════════════════════════════════════════"
	@for i in $$(seq 1 $(PASSES)); do \
		echo ""; \
		echo "  ── Pass $$i / $(PASSES) ──────────────────────────────────"; \
		find . -name '*.aux' -exec xattr -c {} \; 2>/dev/null; \
		xattr -c $(MAIN).out 2>/dev/null; \
		$(TEX) $(TEXFLAGS) $(MAIN).tex || true; \
		if [ -f $(MAIN).idx ]; then makeindex -q $(MAIN).idx 2>/dev/null || true; fi; \
		if [ $$i -ge 2 ] && ! grep -q 'Rerun to get' $(MAIN).log 2>/dev/null \
		   && [ $$(grep -c 'Citation.*undefined' $(MAIN).log) -eq 0 ] \
		   && [ $$(grep -c 'Reference.*undefined' $(MAIN).log) -eq 0 ]; then \
			echo "  ✓  Converged after $$i passes."; \
			break; \
		fi; \
	done
	@if [ ! -f $(MAIN).pdf ]; then \
		echo "  ✗  Build failed — no PDF produced."; exit 1; \
	fi
	@echo ""
	@echo "  ✓  $(PDF) built successfully."
	@echo ""

## fast: Single-pass build for rapid iteration during writing.
##   Tolerates font-shape warnings (newtx exit code 1) if PDF is produced.
fast:
	@echo "  ── Fast build (single pass) ──"
	@find . -name '*.aux' -exec xattr -c {} \; 2>/dev/null
	@xattr -c $(MAIN).out 2>/dev/null || true
	@$(TEX) $(TEXFLAGS) $(MAIN).tex; rc=$$?; \
	if [ -f $(MAIN).pdf ] && grep -q "Output written" $(MAIN).log; then \
		exit 0; \
	else \
		exit $$rc; \
	fi

## watch: Continuous rebuild on save (requires latexmk).
watch:
	@command -v $(LATEXMK) >/dev/null 2>&1 || \
		{ echo "Error: latexmk not found. Install via: brew install --cask mactex"; exit 1; }
	$(LATEXMK) $(MKFLAGS) -pvc $(MAIN).tex

## check: Halt on first error — use for CI or pre-commit validation.
check:
	@echo "  ── Error check (halt-on-error) ──"
	$(TEX) -interaction=nonstopmode -halt-on-error -file-line-error $(MAIN).tex
	@echo "  ✓  No fatal errors."

## integrity: Strict manuscript integrity gate (clean rebuild + diagnostics + claim-tag coverage).
integrity:
	@./scripts/integrity_gate.sh

## phase0-index: Regenerate active-theory theorem dependency index.
phase0-index:
	@./scripts/generate_theorem_dependency_index.py

## draft: Build with draft class option (skips image rendering, faster).
draft:
	@echo "  ── Draft build ──"
	$(TEX) $(TEXFLAGS) "\PassOptionsToClass{draft}{memoir}\input{$(MAIN)}"

## clean: Remove all build artifacts and compiled PDF.
clean:
	@echo "  Cleaning build artifacts..."
	@for ext in $(AUX_EXTS); do \
		rm -f $(MAIN).$$ext; \
	done
	@find chapters appendices bibliography -name '*.aux' -delete 2>/dev/null || true
	@rm -f texput.log
	@rm -f $(MAIN).pdf
	@echo "  ✓  Clean."

## veryclean: Alias for clean (kept for backward compatibility).
veryclean: clean

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

## metadata: Regenerate all machine-readable metadata from .tex sources.
metadata:
	@echo "  ── Generating metadata ──"
	@python3 scripts/generate_metadata.py

## census: Print claim census from generated metadata.
census: metadata
	@python3 -c "import json; d=json.load(open('metadata/census.json')); t=d['totals']; print(f'  PH={t[\"ProvedHere\"]} PE={t[\"ProvedElsewhere\"]} CJ={t[\"Conjectured\"]} H={t[\"Heuristic\"]} O={t[\"Open\"]} total={t[\"total_claims\"]}')"

## verify: Run anti-pattern verification on all .tex files.
verify:
	@./scripts/verify_edit.sh --all

## test: Run computational kernel test suite (if it exists).
test:
	@if [ -d compute/tests ] && ls compute/tests/test_*.py 1>/dev/null 2>&1; then \
		echo "  ── Running compute test suite ──"; \
		if [ -f compute/.venv/bin/python ]; then \
			compute/.venv/bin/python -m pytest compute/tests/ -v; \
		elif [ -f .venv/bin/python ]; then \
			.venv/bin/python -m pytest compute/tests/ -v; \
		else \
			python3 -m pytest compute/tests/ -v; \
		fi; \
	else \
		echo "  (no compute tests found — skipping)"; \
	fi

## help: Show available targets.
help:
	@echo ""
	@echo "  Chiral Bar-Cobar Duality — Build System"
	@echo "  ────────────────────────────────────────"
	@echo ""
	@echo "  make            Full build ($(PASSES) passes, stable cross-refs)"
	@echo "  make fast       Single pass for quick iteration"
	@echo "  make watch      Continuous rebuild on save (latexmk)"
	@echo "  make check      Halt-on-error validation"
	@echo "  make integrity  Strict CI-style integrity gate"
	@echo "  make phase0-index  Regenerate theorem dependency index"
	@echo "  make draft      Draft mode (faster, no images)"
	@echo "  make clean      Remove build artifacts and compiled PDF"
	@echo "  make veryclean  Alias for clean"
	@echo "  make count      Manuscript statistics"
	@echo "  make metadata   Regenerate machine-readable metadata"
	@echo "  make census     Print claim census"
	@echo "  make verify     Run anti-pattern verification"
	@echo "  make test       Run computational kernel tests"
	@echo "  make help       This message"
	@echo ""
