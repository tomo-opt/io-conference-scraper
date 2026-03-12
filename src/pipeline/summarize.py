"""Run summary computation."""

from models import RunSummary


def build_summary(started_at: str, finished_at: str, source_stats: list[dict], raw_count: int, dedupe_count: int) -> dict:
    summary = RunSummary(
        total_sources=len(source_stats),
        successful_sources=sum(1 for s in source_stats if s["status"] == "ok"),
        partial_sources=sum(1 for s in source_stats if s["status"] == "partial"),
        failed_sources=sum(1 for s in source_stats if s["status"] == "error"),
        total_raw_records=raw_count,
        total_deduped_records=dedupe_count,
        run_started_at_utc=started_at,
        run_finished_at_utc=finished_at,
        per_source_stats=source_stats,
    )
    return summary.to_dict()
