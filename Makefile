# Central Asia B2G Research — Makefile
# Orchestrates the harness extension layer

.PHONY: help setup deps run merge audit \
	render obsidian site seo \
	verify-links check-quality test \
	publish clean

help:
	@echo "Targets:"
	@echo "  setup           — bootstrap dependencies + create state dirs"
	@echo "  deps            — install Python deps (pip install -e .[dev])"
	@echo "  run             — run full 7-wave pipeline (~10h, see scripts/run-all.sh)"
	@echo "  merge           — merge per-agent state into knowledge_graph.json"
	@echo "  audit           — quick summary of knowledge graph (audit.py)"
	@echo ""
	@echo "  render          — render all outputs (crm + memo + playbook + obsidian + site)"
	@echo "  obsidian        — render Obsidian vault only"
	@echo "  site            — render public HTML site only"
	@echo "  seo             — build llms.txt, sitemap, robots, feed"
	@echo ""
	@echo "  verify-links    — async HEAD-check every URL in knowledge graph"
	@echo "  check-quality   — 12 content quality gates over outputs/site + outputs/obsidian"
	@echo "  test            — pytest tests/"
	@echo ""
	@echo "  publish         — git commit + push + GitHub Pages deploy"
	@echo "  clean           — remove built outputs (keeps state/)"

setup:
	bash scripts/setup.sh

deps:
	pip install --break-system-packages -e .[dev]

run:
	bash scripts/run-all.sh

merge:
	python3 scripts/merge_state.py

audit:
	python3 scripts/audit.py

render:
	python3 scripts/render.py crm
	python3 scripts/render.py memo
	python3 scripts/render.py playbook
	python3 scripts/render_obsidian.py
	python3 scripts/render_site.py
	python3 scripts/build_seo_assets.py

obsidian:
	python3 scripts/render_obsidian.py

site:
	python3 scripts/render_site.py
	python3 scripts/build_seo_assets.py

seo:
	python3 scripts/build_seo_assets.py

verify-links:
	python3 scripts/verify_links.py

check-quality:
	python3 scripts/check_quality.py

test:
	pytest tests/ -v

publish:
	git add -A
	git status
	@echo "Run: git commit -m '...' && git push"

clean:
	rm -rf outputs/site/_built outputs/site/_drafts
	rm -rf outputs/obsidian/.obsidian-cache
	@echo "Cleaned built outputs (state/ preserved)"
