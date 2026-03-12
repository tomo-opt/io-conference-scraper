"""Project-wide constants."""

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"
SEED_CSV = DATA_DIR / "seeds" / "organizations.csv"
RAW_DIR = DATA_DIR / "raw"
ARCHIVE_DIR = DATA_DIR / "archive"
PROCESSED_DIR = DATA_DIR / "processed"
DOCS_DATA_DIR = PROJECT_ROOT / "docs" / "data"

DEFAULT_TIMEOUT = 20
MAX_RETRIES = 2
USER_AGENT = (
    "Mozilla/5.0 (compatible; IOConferenceScraper/0.1; +https://github.com/tomo-opt/io-conference-scraper)"
)
KEYWORDS = [
    "event",
    "meeting",
    "conference",
    "assembly",
    "session",
    "summit",
    "forum",
    "congress",
    "governing council",
    "ministerial",
]
DROP_TITLES = {"read more", "learn more", "view all", "more", "details"}
