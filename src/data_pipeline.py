import pandas as pd
from sklearn.model_selection import train_test_split

def load_and_clean_data(filepath):
    # For this assessment, we assume the Kaggle Credit Card dataset
    df = pd.read_csv(filepath)
    
    # Data Cleaning: Remove duplicates 
    df = df.drop_duplicates()
    
    # Split into Features (X) and Target (y)
    X = df.drop('Class', axis=1)
    y = df['Class']
    
    # Reproducibility: Using random_state=42 [cite: 13]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    
    return X_train, X_test, y_train, y_test