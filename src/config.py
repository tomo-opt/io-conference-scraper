"""Configuration and seed loading."""

import csv
from dataclasses import dataclass

from constants import DEFAULT_TIMEOUT, MAX_RETRIES, SEED_CSV


@dataclass
class SourceConfig:
    organization: str
    url: str
    enabled: bool = True
    preferred_scraper: str = "auto"
    timeout: int = DEFAULT_TIMEOUT
    max_retries: int = MAX_RETRIES
    allow_playwright_fallback: bool = False


def load_sources() -> list[SourceConfig]:
    with SEED_CSV.open("r", encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    return [SourceConfig(organization=row["organization"], url=row["url"]) for row in rows]
