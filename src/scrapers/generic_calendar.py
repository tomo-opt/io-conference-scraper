"""Generic calendar/table scraper."""

from urllib.parse import urljoin

from scrapers.base import BaseScraper


class GenericCalendarScraper(BaseScraper):
    def scrape(self):
        soup = self.get_soup()
        rows = soup.select("table tr")
        records = []
        for row in rows:
            cells = [c.get_text(" ", strip=True) for c in row.select("th,td")]
            if len(cells) < 2:
                continue
            title = cells[-1]
            date_text = cells[0]
            if len(title) < 4:
                continue
            link = row.find("a", href=True)
            url = urljoin(self.source.url, link["href"]) if link else self.source.url
            records.append(
                self.make_record(
                    conference_title=title,
                    conference_url=url,
                    event_date_text=date_text,
                    summary=" | ".join(cells)[:280],
                    status="partial",
                )
            )
        return records
