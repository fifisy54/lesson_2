from fastapi import FastAPI
import uvicorn
from model import Model
app = FastAPI()
import numpy as np


@app.get("/")
def root():
    return {"message": "Hello World!"}


@app.get("/api/")
async def read_item():
    return {"api": 23}


@app.get("/api/calculate/")
def read_value(value_1: int, value_2: int):
    return value_1 + value_2


modelNN = model.Model()


@app.get("/api/model/")
def make_prediction():
    model = Model()
    model.preprocess()
    model.fit()
    model.chart()
    number = model.prediction()

    return number


make_prediction()


#uvicorn my_web_server:app --reload


