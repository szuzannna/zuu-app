from fastapi import FastAPI
from fastapi import status
from fastapi import Response
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()
app.counter = 0
event={}

class Item(BaseModel):
    date: str
    event: str

class Event():
    def __init__(self, id, date, name, date_added):
        self.id = id
        self.date= date
        self.name = name
        self.date_added = date_added
    def __str__(self):
        return "{'id': " + str(self.id)+",\n'name': " + str(self.name)+ ",\n'date': " +str(self.date) +",\n'date_added': " + str(self.date_added)+"}"


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

@app.put("/events",status_code=200)
async def add_new_event(item: Item):
    current_event = Event(app.counter, item.date, item.event, datetime.today().strftime('%Y-%m-%d'))
    if item.date in event:
        event[item.date].append(current_event)
    else:
        event[item.date] = [current_event]

    app.counter += 1

    return current_event


@app.get("/events/{date}", status_code=200)
async def event_on_date(date: str, response: Response):
    if type(date) != str:
        response.status_code = status.HTTP_400_BAD_REQUEST
    else:
        if date in event:
            return event[date]
        else:
            response.status_code = status.HTTP_404_NOT_FOUND
    return response.status_code

