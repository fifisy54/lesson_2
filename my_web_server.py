from fastapi import FastAPI
import uvicorn
app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World!"}


# @app.get("/api/")
# async def read_item():
#     return {"api": 23}


@app.get("/api/calculate/")
def read_value(value_1: int, value_2: int):
    return value_1 + value_2


@app.get("/api/calculate/")
def read_value(value_1: int, value_2: int):
    return value_1 + value_2

# uvicorn my_web_server:app --reload

