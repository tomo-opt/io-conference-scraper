"""Base scraper class."""

from abc import ABC, abstractmethod

from config import SourceConfig
from models import ConferenceRecord
from utils.date_utils import utc_now_iso, utc_today
from utils.http_utils import fetch_url


class BaseScraper(ABC):
    def __init__(self, source: SourceConfig):
        self.source = source

    def get_soup(self):
        from bs4 import BeautifulSoup

        response = fetch_url(self.source.url, timeout=self.source.timeout)
        return BeautifulSoup(response.text, "lxml")

    def make_record(self, **kwargs) -> ConferenceRecord:
        return ConferenceRecord(
            organization=self.source.organization,
            source_page=self.source.url,
            scraped_at_utc=utc_now_iso(),
            run_date=utc_today(),
            **kwargs,
        )

    @abstractmethod
    def scrape(self) -> list[ConferenceRecord]:
        raise NotImplementedError
