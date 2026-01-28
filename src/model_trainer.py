from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn.metrics import classification_report
import joblib

def train_production_model(X_train, y_train):
    # Model Selection: Random Forest (Justification: Handles imbalanced data well) [cite: 9]
    model = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)
    
    # Cross-Validation [cite: 10]
    scores = cross_val_score(model, X_train, y_train, cv=5, scoring='f1')
    print(f"Cross-Validation F1-Score: {scores.mean():.4f}")
    
    # Fit the final model
    model.fit(X_train, y_train)
    
    # Model Persistence: Save the model [cite: 12]
    joblib.dump(model, 'models/fraud_model.pkl')
    return model

def evaluate_model(model, X_test, y_test):
    # Proper Evaluation Metrics [cite: 11]
    predictions = model.predict(X_test)
    print("Final Evaluation Report:")
    print(classification_report(y_test, predictions))