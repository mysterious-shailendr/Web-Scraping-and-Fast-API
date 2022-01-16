# Web Scraping Project with Fast API
## A Web scraping project to scrape the data from the websites which doesn't require login.<br/>
Beautiful Soup library is used for extracting my response data. It creates a parse tree from page source code that can be used to extract data in a hierarchical and more readable manner, basically a Python library for pulling data out of HTML and XML files.<br/><br/>
I have done scraping on this website: "https://www.onthisday.com"<br/>
" On This Day " is the world's largest, most accurate and popular site for on this day in history, it gives all the historical events happened in a day wise frame.<br/>
I have scrap the whole bunch of data of all days, filtered it in month wise frame and stored it in json file.<br/>
Using Fast API, have assigned endpoints for displaying historical events of today's date, month wise events, a particular day and month event and more...<br/>
It's a basic demo, just for understanding purpose.<br/>
You can use this code to scrap any website data which doesn't requires login.<br/><br/>
### Do these installs before running the project,<br/>
> pip install beautifulsoup4

If anyone got any module error, then install that module like<br/>
> pip install module_name

### For accessing Fast API, run collect_events.py file first ( for creating events.json file ):
> python collect_events.py<br/>
> uvicorn main:app --reload

Then go to the respective url( Ex: http://127.0.0.1:8000/ ), for a better view just add "docs" or "redoc" to your url. ( Ex: http://127.0.0.1:8000/docs or http://127.0.0.1:8000/redoc ) and explore it.

### Reference <br/>

1). https://beautiful-soup-4.readthedocs.io/ <br/>
2). https://www.onthisday.com/<br/>
3). https://fastapi.tiangolo.com/

#### For any doubts, raise your issues, willingly waiting to help you and clear your doubts...
