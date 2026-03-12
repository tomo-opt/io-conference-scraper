"""Deduplication helpers."""

import re


def _norm(text: str) -> str:
    return re.sub(r"\s+", " ", (text or "").strip().lower())


def fingerprint(record: dict) -> str:
    return "|".join(
        [
            _norm(record.get("organization", "")),
            _norm(record.get("conference_title", "")),
            _norm(record.get("conference_url", "")),
            _norm(record.get("start_date", "") or record.get("event_date_text", "")),
        ]
    )


def dedupe_records(records: list[dict]) -> list[dict]:
    seen: set[str] = set()
    out: list[dict] = []
    for row in records:
        fp = fingerprint(row)
        if fp in seen:
            continue
        seen.add(fp)
        out.append(row)
    return out
