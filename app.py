from symtable import Class

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

import pickle
import numpy as np
import sklearn

with open('C:/Users/mikga/PycharmProjects/JupyterProject2/model_iris_v1.pkl', 'rb') as f:
        model = pickle.load(f)
@app.get("/")
async def root():
    return {"message": "Hello World"}

class Item(BaseModel):
    sl: float
    sw: float
    pl: float
    pw: float
@app.post("/predict")
async def predict(item : Item):
    predict=model.predict([[item.sl,item.sw,item.pl,item.pw]])
    prediction = int(predict[0])
    return {"predict": prediction}