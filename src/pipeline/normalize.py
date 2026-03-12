"""Normalization and cleaning pipeline."""

import re
from urllib.parse import urljoin

from constants import DROP_TITLES
from utils.date_utils import parse_date_range


def normalize_record(record: dict) -> dict:
    for key in ["conference_title", "event_date_text", "summary", "location"]:
        record[key] = re.sub(r"\s+", " ", (record.get(key) or "")).strip()
    record["conference_url"] = (record.get("conference_url") or "").strip()
    if record.get("conference_url") and record.get("source_page"):
        record["conference_url"] = urljoin(record["source_page"], record["conference_url"])

    start, end = parse_date_range(record.get("event_date_text", ""))
    record["start_date"] = record.get("start_date") or start
    record["end_date"] = record.get("end_date") or end
    if len(record.get("summary", "")) > 500:
        record["summary"] = record["summary"][:500]
    if "online" in record.get("event_date_text", "").lower() and not record.get("location"):
        record["location"] = "Online"

    title = record.get("conference_title", "").lower()
    if not title:
        record["status"] = "error"
    elif title in DROP_TITLES:
        record["status"] = "error"
    elif not record.get("conference_url") or not record.get("start_date"):
        record["status"] = "partial"
    else:
        record["status"] = "ok"
    return record
