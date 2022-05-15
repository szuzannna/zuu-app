from fastapi import FastAPI
from fastapi import status
from fastapi import Response
import asyncio

app = FastAPI()

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