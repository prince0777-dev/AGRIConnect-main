from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import numpy as np
import pickle
import os

router = APIRouter()

# Load model
model_path = os.path.join(os.path.dirname(__file__), "../models/price_model.pkl")
with open(model_path, "rb") as f:
    model = pickle.load(f)

# Define input schema
class PricePredictionInput(BaseModel):
    crop_type: int  # Example: 0 = Wheat, 1 = Rice
    region: int  # Example: 1 = North, 2 = South
    season: int  # Example: 0 = Winter, 1 = Summer
    quantity: float  # Example: in kg

@router.post("/predict-price/")
def predict_price(input_data: PricePredictionInput):
    try:
        features = np.array([[input_data.crop_type, input_data.region, input_data.season, input_data.quantity]])
        predicted_price = model.predict(features)[0]
        return {"predicted_price": round(float(predicted_price), 2)}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
