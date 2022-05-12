from fastapi import FastAPI

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