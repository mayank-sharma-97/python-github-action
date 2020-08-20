import src.calculation as cal

from typing import List
from fastapi import FastAPI
from pydantic import BaseModel

class RequestJson(BaseModel):
    num1:int = 1
    num2:int = 1


app = FastAPI()

@app.post("/add")
def addition(request:RequestJson):
    response = {"result":cal.add(request.num1,request.num2)}
    return response

@app.post("/sub")
def subtract(request:RequestJson):
    response = {"result":cal.sub(request.num1,request.num2)}
    return response
