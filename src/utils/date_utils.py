"""Date parsing helpers."""

import re
from datetime import datetime

try:
    from dateutil import parser as date_parser
except Exception:  # optional in constrained environments
    date_parser = None


def parse_date_range(text: str) -> tuple[str, str]:
    if not text:
        return "", ""
    normalized = re.sub(r"\s+", " ", text).strip()

    if date_parser is not None:
        try:
            dt = date_parser.parse(normalized, fuzzy=True, dayfirst=False)
            return dt.date().isoformat(), dt.date().isoformat()
        except Exception:
            pass

        if "-" in normalized:
            parts = [p.strip() for p in normalized.split("-") if p.strip()]
            if len(parts) == 2:
                try:
                    start = date_parser.parse(parts[0], fuzzy=True)
                    end = date_parser.parse(parts[1], fuzzy=True)
                    return start.date().isoformat(), end.date().isoformat()
                except Exception:
                    return "", ""

    for fmt in ("%d %B %Y", "%d %b %Y", "%Y-%m-%d"):
        try:
            dt = datetime.strptime(normalized, fmt)
            return dt.date().isoformat(), dt.date().isoformat()
        except ValueError:
            continue
    return "", ""


def utc_now_iso() -> str:
    return datetime.utcnow().replace(microsecond=0).isoformat() + "Z"


def utc_today() -> str:
    return datetime.utcnow().date().isoformat()
