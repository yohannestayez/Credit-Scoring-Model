from fastapi import FastAPI, HTTPException
import pickle
import pandas as pd
from pydantic import BaseModel

# Initialize FastAPI app
app = FastAPI()

# Load the trained model
with open("C:/Users/Administrator/Documents/kifiya/Week_6/final_model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

# Input schema for prediction 
class PredictionInput(BaseModel):
    Recency: float
    Frequency: float
    Monetary: float
    Seniority: float

# API Endpoints
@app.post("/predict")
def predict(input_data: PredictionInput):
    # Convert input data to DataFrame (model expects a DataFrame)
    input_df = pd.DataFrame([input_data.dict()])

    # Make prediction
    try:
        prediction = model.predict(input_df)
        return {"prediction": int(prediction[0])}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
