from pipeline.normalize import normalize_record


def test_normalize_relative_url_and_date():
    row = {
        "source_page": "https://example.org/events",
        "conference_title": "  Test Event ",
        "conference_url": "/event/1",
        "event_date_text": "12 March 2026",
        "summary": " a " * 5,
    }
    out = normalize_record(row)
    assert out["conference_url"] == "https://example.org/event/1"
    assert out["start_date"] == "2026-03-12"
