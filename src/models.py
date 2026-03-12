"""Data models for scraper records and run summaries."""

from dataclasses import asdict, dataclass, field
from typing import Any


@dataclass
class ConferenceRecord:
    organization: str
    source_page: str
    conference_title: str
    conference_url: str = ""
    event_date_text: str = ""
    start_date: str = ""
    end_date: str = ""
    location: str = ""
    summary: str = ""
    scraped_at_utc: str = ""
    run_date: str = ""
    status: str = "partial"

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class SourceStat:
    organization: str
    source_page: str
    status: str
    record_count: int
    error: str = ""


@dataclass
class RunSummary:
    total_sources: int = 0
    successful_sources: int = 0
    partial_sources: int = 0
    failed_sources: int = 0
    total_raw_records: int = 0
    total_deduped_records: int = 0
    run_started_at_utc: str = ""
    run_finished_at_utc: str = ""
    per_source_stats: list[dict[str, Any]] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)
