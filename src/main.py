"""Main pipeline entrypoint."""

from config import load_sources
from pipeline.archive import write_outputs
from pipeline.extract import extract_from_source
from pipeline.normalize import normalize_record
from pipeline.publish import publish_site_data
from pipeline.summarize import build_summary
from pipeline.validate import is_valid_record
from utils.dedupe import dedupe_records
from utils.date_utils import utc_now_iso, utc_today
from utils.io_utils import ensure_dir, write_json
from utils.logging_utils import setup_logger
from constants import RAW_DIR


def run() -> int:
    logger = setup_logger()
    run_date = utc_today()
    started_at = utc_now_iso()
    sources = [s for s in load_sources() if s.enabled]

    all_records = []
    source_stats = []
    raw_day = RAW_DIR / run_date
    ensure_dir(raw_day)

    for source in sources:
        records, stat = extract_from_source(source)
        source_stats.append(stat)
        for rec in records:
            cleaned = normalize_record(rec)
            if is_valid_record(cleaned):
                all_records.append(cleaned)
        logger.info("%s -> %s records (%s)", source.organization, stat["record_count"], stat["status"])

    deduped = dedupe_records(all_records)
    finished_at = utc_now_iso()
    summary = build_summary(started_at, finished_at, source_stats, len(all_records), len(deduped))
    write_outputs(run_date, all_records, deduped, summary)
    publish_site_data()
    write_json(raw_day / "source_stats.json", source_stats)
    logger.info("Run complete: %s raw, %s deduped", len(all_records), len(deduped))
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
