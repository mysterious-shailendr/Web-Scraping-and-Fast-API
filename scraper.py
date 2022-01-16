from typing import List
import requests as _requests
import bs4 as _bs4

def _generate_url(month: str, day: int) -> str:
    url = f"https://www.onthisday.com/day/{month}/{day}"
    return url

def _get_page(url: str) -> _bs4.BeautifulSoup:
    page = _requests.get(url)
    soup = _bs4.BeautifulSoup(page.content, "html.parser")
    return soup

def _events_of_the_day(month: str, day: int) -> List[str]:
    """
    To return events of a given particular day
    """
    url = _generate_url(month, day)
    page = _get_page(url)
    raw_events = page.find_all(class_="event")
    events = [event.text for event in raw_events]
    return events

#_events_of_the_day("january", 1)