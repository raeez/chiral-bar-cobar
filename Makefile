# ============================================================================
#  Makefile — Modular Koszul Duality (Vol I)
# ============================================================================
#
#  Usage:
#    make               Build everything: manuscript + working notes → out/
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

# Output — everything goes to out/
OUT_DIR   := out
PDF       := $(OUT_DIR)/main.pdf

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

.PHONY: all fast watch clean veryclean clean-builds count check draft integrity phase0-index metadata verify census test editorial standalone dist release help working-notes icloud verify-independence verify-independence-verbose

## icloud: Copy latest PDFs to iCloud Drive, organised by subject
icloud: $(PDF)
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
		ordered_chiral_homology survey_modular_koszul_duality_v2; do \
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

## all: Full build — manuscript + working notes → out/
all: $(STAMP) working-notes

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
	@echo "  [1/3] Manuscript"
	@$(BUILD_SCRIPT) $(FAST_PASSES)
	@if [ -f $(PDF) ]; then \
		echo "  ✓  $(PDF)"; \
	else \
		echo "  ✗  Build failed."; \
	fi
	@echo ""
	@echo "  [2/3] Working notes"
	@$(MAKE) --no-print-directory working-notes
	@echo ""
	@echo "  [3/3] Standalone papers"
	@$(MAKE) --no-print-directory standalone
	@echo ""
	@echo "  ── Copying to iCloud (subject-organised) ──"
	@$(MAKE) --no-print-directory icloud
	@echo ""
	@echo "  ══════════════════════════════════════════"
	@echo "  Release complete. All output in out/:"
	@ls -1 $(OUT_DIR)/*.pdf 2>/dev/null | sed 's/^/    /'
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

## verify-independence: Audit ProvedHere claims vs independent-verification registry
##                     (tautology / orphan check; coverage metric reported)
verify-independence:
	@python3 compute/scripts/audit_independent_verification.py

## verify-independence-verbose: Same, with full list of uncovered claims
verify-independence-verbose:
	@python3 compute/scripts/audit_independent_verification.py --verbose --show-orphans

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
	@for paper in \
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
			echo "    Building $$paper.tex ..."; \
			cd standalone && for i in 1 2 3; do \
				$(TEX) $(TEXFLAGS) $$paper.tex >../$(LOG_DIR)/standalone-$$paper.log 2>&1 || true; \
			done && cd ..; \
			if [ -f standalone/$$paper.pdf ]; then \
				mv standalone/$$paper.pdf $(OUT_DIR)/$$paper.pdf; \
				rm -f standalone/$$paper.aux standalone/$$paper.log standalone/$$paper.out standalone/$$paper.toc 2>/dev/null; \
				echo "    ✓  out/$$paper.pdf"; \
			else \
				echo "    ✗  $$paper build failed. See $(LOG_DIR)/standalone-$$paper.log"; \
			fi; \
		fi; \
	done

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
