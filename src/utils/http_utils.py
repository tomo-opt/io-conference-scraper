"""HTTP helper utilities."""

from constants import USER_AGENT


def fetch_url(url: str, timeout: int = 20):
    import requests

    headers = {"User-Agent": USER_AGENT}
    response = requests.get(url, headers=headers, timeout=timeout, allow_redirects=True)
    response.raise_for_status()
    return response
