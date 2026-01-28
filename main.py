from src.data_pipeline import load_and_clean_data
from src.features import engineer_features
from src.model_trainer import train_production_model, evaluate_model
import os

def run_assessment():
    # 1. Ensure folders exist
    if not os.path.exists('models'): os.makedirs('models')
    
    # 2. Data Loading
    # NOTE: You need to download 'creditcard.csv' from Kaggle and put it in /data
    data_path = 'data/creditcard.csv'
    X_train, X_test, y_train, y_test = load_and_clean_data(data_path)
    
    # 3. Feature Engineering 
    X_train = engineer_features(X_train)
    X_test = engineer_features(X_test)
    
    # 4. Training and Evaluation [cite: 3, 5]
    print("Starting Task 1: Production Pipeline...")
    model = train_production_model(X_train, y_train)
    evaluate_model(model, X_test, y_test)
    print("Task 1 Completed Successfully.")

if __name__ == "__main__":
    run_assessment()