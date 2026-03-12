"""Generic event link extraction scraper."""

from urllib.parse import urljoin

from constants import KEYWORDS
from scrapers.base import BaseScraper


class GenericLinksScraper(BaseScraper):
    def scrape(self):
        soup = self.get_soup()
        records = []
        links = soup.find_all("a", href=True)
        for a in links:
            title = a.get_text(" ", strip=True)
            href = a.get("href", "")
            if not title or len(title) < 4:
                continue
            low = f"{title} {href}".lower()
            if not any(k in low for k in KEYWORDS):
                continue
            url = urljoin(self.source.url, href)
            parent_text = self._parent_text(a)
            records.append(
                self.make_record(
                    conference_title=title,
                    conference_url=url,
                    event_date_text=parent_text,
                    summary=parent_text[:280],
                    status="partial",
                )
            )
        return records

    @staticmethod
    def _parent_text(node) -> str:
        parent = node.parent
        if not parent:
            return ""
        return parent.get_text(" ", strip=True)[:280]
