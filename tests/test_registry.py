from config import SourceConfig
from scrapers.registry import get_scraper
from scrapers.un_calendar import UNCalendarScraper
from scrapers.who import WHOScraper


def test_registry_selects_un_calendar():
    src = SourceConfig("United Nations – Calendar of Conferences and Meetings", "https://www.un.org/calendar/en")
    assert isinstance(get_scraper(src), UNCalendarScraper)


def test_registry_selects_who():
    src = SourceConfig("WHO Events", "https://www.who.int/news-room/events")
    assert isinstance(get_scraper(src), WHOScraper)
