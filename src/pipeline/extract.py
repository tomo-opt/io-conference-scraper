"""Extraction orchestrator."""

from models import SourceStat
from scrapers.registry import get_scraper


def extract_from_source(source):
    scraper = get_scraper(source)
    try:
        records = [r.to_dict() for r in scraper.scrape()]
        status = "ok" if records else "partial"
        return records, SourceStat(source.organization, source.url, status, len(records)).__dict__
    except Exception as exc:
        return [], SourceStat(source.organization, source.url, "error", 0, str(exc)).__dict__
