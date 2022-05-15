from fastapi import FastAPI
from fastapi import status
from fastapi import Response
from fastapi import BaseModel
from datetime import datetime

app = FastAPI()
app.counter = 0
event={}

class Item(BaseModel):
    date: str
    event_name: str

class Event():
    def __init__(self, id, date, event_name, date_added):
        self.id = id
        self.date= date
        self.event_name = event_name
        self.date_added = date_added



@app.get("/",status_code=200)
def root():
    return {"start": "1970-01-01"}

@app.get("/method",status_code=200)
def root():
    return {"method": "GET"}

@app.put("/method",status_code=200)
def root():
    return {"method": "PUT"}

@app.options("/method",status_code=200)
def root():
    return {"method": "OPTIONS"}

@app.delete("/method",status_code=200)
def root():
    return {"method": "DELETE"}

@app.post("/method",status_code=201)
def root():
    return {"method": "POST"}

@app.get("/day", status_code=200)
def read_item(name: str, number: int, response: Response):
    day_dictionary= {"monday" : 1,
                     "tuesday" : 2,
                     "wednesday" : 3,
                     "thursday" :4,
                     "friday" : 5,
                     "saturday" :6,
                     "sunday" :7}
    if name.lower() not in day_dictionary:
        response.status_code = status.HTTP_400_BAD_REQUEST
    elif day_dictionary[name.lower()] != number:
        response.status_code = status.HTTP_400_BAD_REQUEST
    return response.status_code

@app.put("/event/{date}",status_code=200)
async def add_new_event(item: Item):
    event[item.date] = Event(app.counter, item.date, item.event_name, datetime.today().strftime('%Y-%m-%d'))

    app.counter += 1

    return {'id': app.counter,
            'event': item.event_name,
            'date': item.date,
            'date_added': datetime.today().strftime('%Y-%m-%d')}


@app.get("/events/{date}",status_code=200)
async def event_on_date(date: str, response: Response):
    if type(date) != str:
        response.status_code = status.HTTP_400_BAD_REQUEST
    else:
        if date in event['date']:
            return event
        else:
            response.status_code = status.HTTP_404_NOT_FOUND
    return response.status_code