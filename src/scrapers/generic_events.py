"""Generic events scraper using cards/lists."""

from urllib.parse import urljoin

from constants import KEYWORDS
from scrapers.base import BaseScraper


class GenericEventsScraper(BaseScraper):
    SELECTORS = ["article", ".event", ".events-item", "li", ".card"]

    def scrape(self):
        soup = self.get_soup()
        records = []
        seen = set()
        for selector in self.SELECTORS:
            for node in soup.select(selector):
                text = node.get_text(" ", strip=True)
                if not text or len(text) < 6:
                    continue
                if not any(k in text.lower() for k in KEYWORDS):
                    continue
                link = node.find("a", href=True)
                title = (link.get_text(" ", strip=True) if link else text[:150]).strip()
                if title.lower() in seen:
                    continue
                seen.add(title.lower())
                href = urljoin(self.source.url, link["href"]) if link else self.source.url
                records.append(
                    self.make_record(
                        conference_title=title,
                        conference_url=href,
                        event_date_text=text,
                        summary=text[:280],
                        status="partial",
                    )
                )
        return records
