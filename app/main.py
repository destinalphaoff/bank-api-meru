from fastapi import FastAPI
from . import models, database

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to Meru Bank API"}
