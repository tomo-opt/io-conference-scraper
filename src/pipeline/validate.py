"""Validation helpers."""

from constants import DROP_TITLES


def is_valid_record(record: dict) -> bool:
    title = (record.get("conference_title") or "").strip().lower()
    if not title or title in DROP_TITLES:
        return False
    if len(title) < 3:
        return False
    return True
