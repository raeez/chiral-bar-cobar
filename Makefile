# ============================================================================
#  Makefile — Chiral Bar-Cobar Duality Monograph
# ============================================================================
#
#  Usage:
#    make            Build the manuscript (default: pdflatex, 3 passes)
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
TEXFLAGS  := -interaction=nonstopmode -file-line-error -synctex=1
LATEXMK   := latexmk
MKFLAGS   := -pdf -pdflatex="$(TEX) $(TEXFLAGS)" -interaction=nonstopmode

# Number of passes for cross-references, TOC, and page numbers to stabilize.
PASSES    := 3

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

.PHONY: all fast watch clean veryclean count check draft integrity phase0-index help

## all: Full build — three pdflatex passes for stable cross-references.
all: $(PDF)

$(PDF): $(SOURCES)
	@echo "══════════════════════════════════════════════════════════"
	@echo "  Building: $(MAIN).tex  →  $(PDF)"
	@echo "  Engine:   $(TEX) ($(PASSES) passes)"
	@echo "══════════════════════════════════════════════════════════"
	@for i in $$(seq 1 $(PASSES)); do \
		echo ""; \
		echo "  ── Pass $$i / $(PASSES) ──────────────────────────────────"; \
		if [ $$i -eq $(PASSES) ]; then \
			$(TEX) $(TEXFLAGS) $(MAIN).tex || exit 1; \
		else \
			$(TEX) $(TEXFLAGS) $(MAIN).tex || true; \
		fi; \
		if [ -f $(MAIN).idx ]; then makeindex -q $(MAIN).idx 2>/dev/null || true; fi; \
	done
	@echo ""
	@echo "  ✓  $(PDF) built successfully."
	@echo ""

## fast: Single-pass build for rapid iteration during writing.
fast:
	@echo "  ── Fast build (single pass) ──"
	$(TEX) $(TEXFLAGS) $(MAIN).tex

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
	@touch $(MAIN).aux
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
	@echo "  make help       This message"
	@echo ""
