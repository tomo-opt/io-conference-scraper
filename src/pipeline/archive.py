"""Archive writing logic."""

from pathlib import Path

from constants import ARCHIVE_DIR, PROCESSED_DIR
from utils.io_utils import ensure_dir, write_csv, write_json


def write_outputs(run_date: str, records: list[dict], deduped: list[dict], summary: dict) -> None:
    archive_path = ARCHIVE_DIR / run_date
    ensure_dir(archive_path)
    write_csv(archive_path / "conferences.csv", records)
    write_json(archive_path / "conferences.json", records)
    write_csv(archive_path / "conferences_deduped.csv", deduped)
    write_json(archive_path / "run_summary.json", summary)

    ensure_dir(PROCESSED_DIR)
    write_csv(PROCESSED_DIR / "latest_conferences.csv", records)
    write_json(PROCESSED_DIR / "latest_conferences.json", records)
    write_csv(PROCESSED_DIR / "latest_conferences_deduped.csv", deduped)
    write_json(PROCESSED_DIR / "latest_run_summary.json", summary)
