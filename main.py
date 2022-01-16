from fastapi import FastAPI
import services as _services

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to the Historical events FastAPI"}

@app.get("/events")
async def all_events():
    return _services.get_all_events()

@app.get("/events/today")
async def todays_events():
    return _services.get_all_today_events()

@app.get("/events/{month}")
async def month_events(month: str):
    return _services.get_all_month_events(month)

@app.get("/events/{month}/{day}")
async def day_events(month: str, day: int):
    return _services.get_all_day_events(month,day)