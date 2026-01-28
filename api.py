from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
import os
import sys

# Ensure the root directory is in the python path so 'src' can be found
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.features import engineer_features

# 1. Initialize FastAPI
app = FastAPI(title="Fraud Detection API")

# 2. Robust Model Loading
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, 'models', 'improved_fraud_model.pkl')

if os.path.exists(model_path):
    model = joblib.load(model_path)
else:
    # This will show up in your Render Logs to help us debug
    print(f"CRITICAL ERROR: Model file not found at {model_path}")
    model = None

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
    if model is None:
        return {"error": "Model not loaded on server"}
        
    # Convert input to DataFrame
    input_df = pd.DataFrame([data.model_dump()]) # dict() is deprecated in newer Pydantic
    
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