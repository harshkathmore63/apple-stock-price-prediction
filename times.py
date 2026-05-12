import uvicorn
from fastapi import FastAPI
import pickle
from datetime import datetime

app = FastAPI()
pickle_in = open("tsmodel.pkl", "rb")
model=pickle.load(pickle_in)

@app.get('/')
def index():
    return {'Deployment': 'Apple Stock Price Prediction'}

@app.post('/predict')
def predict(year:int ,month:int ,day:int):
    prediction = model.predict([[year,month,day]])
    
    return {
        'prediction': prediction
    }

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=9000)