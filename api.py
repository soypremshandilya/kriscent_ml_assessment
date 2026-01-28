from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
import os
from src.features import engineer_features

# 1. Initialize FastAPI
app = FastAPI(title="Fraud Detection API")

# 2. Load the model
model_path = 'models/improved_fraud_model.pkl'
model = joblib.load(model_path)

# 3. Define the input data structure
class Transaction(BaseModel):
    Time: float
    V1: float; V2: float; V3: float; V4: float; V5: float
    V6: float; V7: float; V8: float; V9: float; V10: float
    V11: float; V12: float; V13: float; V14: float; V15: float
    V16: float; V17: float; V18: float; V19: float; V20: float
    V21: float; V22: float; V23: float; V24: float; V25: float
    V26: float; V27: float; V28: float
    Amount: float

@app.get("/")
def home():
    return {"message": "Fraud Detection API is Live!"}

@app.post("/predict")
def predict(data: Transaction):
    # Convert input to DataFrame
    input_df = pd.DataFrame([data.dict()])
    
    # Apply your custom feature engineering
    processed_df = engineer_features(input_df)
    
    # Get probability and use your 0.1 threshold
    prob = model.predict_proba(processed_df)[:, 1][0]
    is_fraud = int(prob >= 0.1)
    
    return {
        "is_fraud": is_fraud,
        "fraud_probability": round(float(prob), 4),
        "status": "Fraud Detected" if is_fraud else "Legitimate"
    }