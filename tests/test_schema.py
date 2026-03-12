from models import ConferenceRecord


def test_schema_fields_exist():
    item = ConferenceRecord(organization="A", source_page="B", conference_title="C")
    d = item.to_dict()
    expected = {
        "organization", "source_page", "conference_title", "conference_url", "event_date_text",
        "start_date", "end_date", "location", "summary", "scraped_at_utc", "run_date", "status"
    }
    assert expected.issubset(d.keys())
