"""Copy processed files to docs/data for site publishing."""

import shutil

from constants import DOCS_DATA_DIR, PROCESSED_DIR
from utils.io_utils import ensure_dir


def publish_site_data() -> None:
    ensure_dir(DOCS_DATA_DIR)
    shutil.copy2(PROCESSED_DIR / "latest_conferences.json", DOCS_DATA_DIR / "latest_conferences.json")
    shutil.copy2(PROCESSED_DIR / "latest_run_summary.json", DOCS_DATA_DIR / "latest_run_summary.json")
