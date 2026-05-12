from fastapi import FastAPI
import pickle
from datetime import datetime
from pydantic import BaseModel
import pandas as pd

app = FastAPI()

# Load model
with open("tsmodel.pkl", "rb") as f:
    model = pickle.load(f)

class InputData(BaseModel):
    year: int
    month: int
    day: int

@app.get("/")
def home():
    return {"message": "Apple Stock Prediction API is running"}

@app.post("/predict")
def predict(data: InputData):
    dt = datetime(data.year, data.month, data.day)
    
    # Adjust based on your model requirement
    dt = datetime(data.year, data.month, data.day)
    prediction = model.predict(start=dt, end=dt)

    return {
        "date": dt.strftime("%Y-%m-%d"),
        "prediction": float(prediction[0])
    }