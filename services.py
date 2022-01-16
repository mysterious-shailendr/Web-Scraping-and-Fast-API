from typing import Dict
import json as _json
import datetime as _dt

def get_all_events() -> Dict:
    with open("events.json") as events_file:
        data = _json.load(events_file, encoding='utf8')
        
    return data

def get_all_month_events(month: str) -> Dict:
    events = get_all_events()
    month = month.lower()
    try:
        month_events = events[month]
        return month_events
    except KeyError:
        return "This is not a month name"

def get_all_day_events(month: str, day: int) -> Dict:
    events = get_all_events()
    month = month.lower()
    try:
        day_events = events[month][str(day)] # Here, I passed day as a string becasue in our json, days are written in string format
        return day_events
    except KeyError:
        return "This is not a valid input"

def get_all_today_events():
    today = _dt.date.today()
    month = today.strftime("%B")
    return get_all_day_events(month, today.day)
