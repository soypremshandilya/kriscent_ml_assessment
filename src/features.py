import numpy as np

def engineer_features(df):
    df = df.copy()
    # Feature 1: Log transform of Amount (to handle skewness)
    df['log_amount'] = np.log1p(df['Amount'])
    
    # Feature 2: Hour of day from 'Time' column
    df['hour'] = (df['Time'] // 3600) % 24
    
    # Feature 3: Transaction speed (Amount per second)
    df['amt_per_sec'] = df['Amount'] / (df['Time'] + 1)
    
    # Feature 4: Deviation from mean (Z-score style)
    df['amt_deviation'] = (df['Amount'] - df['Amount'].mean()) / df['Amount'].std()
    
    return df