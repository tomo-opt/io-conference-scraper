"""Scraper registry and selection logic."""

from config import SourceConfig
from scrapers.base import BaseScraper
from scrapers.fao import FAOScraper
from scrapers.generic_calendar import GenericCalendarScraper
from scrapers.generic_events import GenericEventsScraper
from scrapers.generic_links import GenericLinksScraper
from scrapers.iaea import IAEAScraper
from scrapers.ilo import ILOScraper
from scrapers.itu import ITUScraper
from scrapers.oecd import OECDScraper
from scrapers.un_calendar import UNCalendarScraper
from scrapers.unesco import UNESCOScraper
from scrapers.who import WHOScraper
from scrapers.world_bank import WorldBankScraper
from scrapers.wto import WTOScraper


def get_scraper(source: SourceConfig) -> BaseScraper:
    org = source.organization.lower()
    url = source.url.lower()
    if "calendar/en" in url and "un.org" in url:
        return UNCalendarScraper(source)
    if "who" in org:
        return WHOScraper(source)
    if "unesco" in org:
        return UNESCOScraper(source)
    if "ilo" in org:
        return ILOScraper(source)
    if "fao" in org:
        return FAOScraper(source)
    if "itu" in org:
        return ITUScraper(source)
    if "world bank" in org or "worldbank" in url:
        return WorldBankScraper(source)
    if "wto" in org:
        return WTOScraper(source)
    if "oecd" in org:
        return OECDScraper(source)
    if "iaea" in org:
        return IAEAScraper(source)
    if any(k in url for k in ["calendar", "meetings", "events-list"]):
        return GenericCalendarScraper(source)
    if "events" in url or "conference" in url:
        return GenericEventsScraper(source)
    return GenericLinksScraper(source)
