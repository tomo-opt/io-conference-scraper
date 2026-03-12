from utils.dedupe import dedupe_records


def test_dedupe_records():
    rows = [
        {"organization": "A", "conference_title": "X", "conference_url": "u", "start_date": "2025-01-01"},
        {"organization": "A", "conference_title": "X", "conference_url": "u", "start_date": "2025-01-01"},
    ]
    assert len(dedupe_records(rows)) == 1
