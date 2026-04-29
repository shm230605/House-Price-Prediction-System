from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()

model = joblib.load("models/model.pkl")

class HouseInput(BaseModel):
    area: int
    bedrooms: int
    bathrooms: int
    location_score: int
    age: int

@app.get("/")
def home():
    return {"message": "API running"}

@app.post("/predict")
def predict(data: HouseInput):

    try:
        # MUST be 2D array
        input_data = np.array([[
            data.area,
            data.bedrooms,
            data.bathrooms,
            data.location_score,
            data.age
        ]])

        prediction = model.predict(input_data)

        return {
            "predicted_price": float(prediction[0])
        }

    except Exception as e:
        return {
            "error": str(e)
        }