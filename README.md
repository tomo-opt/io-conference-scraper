# IO Conference Scraper

Daily scraper + publisher for conferences, meetings, and events across the UN system and major intergovernmental organizations.

## Why this project exists
Public event data is scattered across many official portals, each with different structures. This project standardizes those listings into one searchable dataset and GitHub Pages site.

## Supported source categories
- UN principal entry points and organs
- UN funds/programmes and secretariat entities
- UN regional commissions
- UN specialized agencies
- UN-related research/training institutes
- Other major intergovernmental organizations

Seed registry: `data/seeds/organizations.csv`.

## Architecture overview
- `src/config.py`: seed-driven source configs
- `src/scrapers/`: base + generic + specialized adapters
- `src/pipeline/`: extract, normalize, validate, dedupe, archive, publish
- `src/main.py`: end-to-end run orchestrator
- `docs/`: GitHub Pages UI

## Data flow
1. Load seed CSV
2. Choose scraper via registry
3. Extract event candidates
4. Normalize and validate records
5. Deduplicate records
6. Write archive + latest processed files
7. Copy site JSON files into `docs/data`

## Output files
- Raw: `data/raw/YYYY-MM-DD/`
- Archive: `data/archive/YYYY-MM-DD/`
- Latest processed: `data/processed/latest_*`
- Site publish data: `docs/data/latest_*`

## Scheduling
GitHub Actions schedule runs daily at Beijing 10:07 (UTC+8), cron `07 02 * * *`.

## Run locally
```bash
python -m pip install -r requirements.txt
python src/main.py
pytest
```

## Add a new source
1. Add a row to `data/seeds/organizations.csv`.
2. Optionally set scraper behavior in `scrapers/registry.py`.
3. Run pipeline and tests.

## Add a new custom scraper
1. Create class in `src/scrapers/<name>.py` extending `BaseScraper`.
2. Implement `scrape()` returning `ConferenceRecord` list.
3. Wire URL/org matching in `registry.py`.

## GitHub Pages usage
Site lives in `docs/` and reads:
- `docs/data/latest_conferences.json`
- `docs/data/latest_run_summary.json`

Enable Pages in repo settings with `docs/` folder source.

## Limitations
- Some sites are JS-heavy or blocked; output may be partial.
- Date granularity varies by source.
- One source failure should not break the whole run.

## Ethics / robots / public-site respect
- Scrape public listing pages only.
- Use conservative request settings and user-agent headers.
- Respect site terms, robots guidance, and avoid abusive traffic.
