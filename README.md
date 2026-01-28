# kriscent_ml_assessment

## 📌 Project Overview

This project implements an **end-to-end, production-grade Machine Learning pipeline** for real-world  
**Credit Card Fraud Detection**.

It covers the **entire ML lifecycle** — from modular data processing and model debugging  
to performance optimization and **live cloud deployment**.

Key focus areas:

- Reproducibility & stability
- Handling extreme class imbalance
- Production-ready architecture
- Real-world metric optimization

---

## 🚀 Live Production API

Swagger UI (Interactive Docs):  
https://kriscent-fraud-api.onrender.com/docs

Note:

- Hosted on a free tier
- Initial request may take 30–60 seconds to wake the server

---

## 🛠️ Folder Structure

```plaintext
├── data/               # Dataset (creditcard.csv)
├── docs/               # System Design & Architecture
├── models/             # Task 1: Model Persistence (.pkl files)
├── src/                # Task 1: Modular Codebase
│   ├── data_pipeline.py
│   ├── features.py
│   ├── model_trainer.py
│   └── inference.py
├── api.py              # Task 4: FastAPI Entry Point
├── main.py             # Entry point for Production Pipeline
├── research_task.py    # Task 2 & 3: Debugging & Improvement
├── test_api.py         # Manual API Verification Script
├── requirements.txt    # Reproducibility & Dependencies
└── README.md           # Documentation
```

---

## 🚀 Implementation Details

---

### 🔹 Task 1: Production Pipeline

Data Cleaning

```text
- Removed duplicate transactions
- Applied stratified train-test split to preserve class balance
```

Feature Engineering

```text
Implemented Features:
- log_amount     → Handles skewness in transaction amounts
- hour           → Captures temporal fraud patterns
- amt_per_sec    → Measures transaction velocity
- amt_deviation  → Identifies anomalous spending behavior
```

Reproducibility

```text
- Global random seeds applied (random_state = 42)
- Ensures consistent and repeatable results
```

Modularization

```text
- Data ingestion, feature engineering, model training,
  and inference decoupled into independent modules
```

---

### 🔹 Task 2: Model Debugging & Stability

Observed Problem

```text
- High variance across runs
- Unstable predictions for identical inputs
```

Root Cause

```text
- Random data splitting
- Inconsistent minority class (fraud) sampling
```

Solution

```text
- Implemented Stratified Splitting
- Fixed random seeds across the pipeline
```

Metrics

```text
Score Variance:
Before → 0.1129
After  → 0.0083
Variance Reduction → ~92%
```

---

### 🔹 Task 3: Performance Improvement

Objective

```text
- Improve baseline Recall by ≥ 10%
```

Techniques Applied

```text
- Cost-Sensitive Learning (class_weight='balanced')
- Classification Threshold Tuning (threshold = 0.1)
```

Result

```text
Recall:
Baseline → 0.7474
Improved → 0.8526
Gain     → +14.08%
```

Justification

```text
Lowering the threshold prioritizes fraud detection,
which is more critical than minimizing false positives
in financial risk systems.
```

---

### 🔹 Task 4: ML System Design & Deployment

Architecture

```text
- Real-time inference via FastAPI
- REST-based prediction service
- Model persistence using joblib
- Deployed on Render Cloud Platform
```

Operational Strategy

```text
- Live API-based fraud prediction
- Modular pipeline enables future retraining
- Swagger UI for easy validation and testing
```

Documentation

```text
- Interactive API docs via Swagger UI
- System design notes available in docs/
```

---

## 🧪 Testing the System

Interactive Testing

```text
- Open /docs endpoint
- Use POST /predict
- Click "Try it out"
```

Manual Testing

```text
pip install requests
python test_api.py
```

Sample Fraudulent Payload

```json
{
  "Time": 406.0,
  "V1": -2.3122,
  "V2": 1.9519,
  "V3": -1.6098,
  "V4": 3.9979,
  "V5": -0.5221,
  "V6": -1.4265,
  "V7": -2.5373,
  "V8": 1.3916,
  "V9": -2.77,
  "V10": -2.7722,
  "V11": 3.202,
  "V12": -2.8999,
  "V13": -0.5952,
  "V14": -4.2892,
  "V15": 0.3897,
  "V16": -1.1407,
  "V17": -2.83,
  "V18": -0.0168,
  "V19": 0.4169,
  "V20": 0.1269,
  "V21": 0.5172,
  "V22": -0.035,
  "V23": -0.4652,
  "V24": 0.3201,
  "V25": 0.0445,
  "V26": 0.1778,
  "V27": 0.2611,
  "V28": -0.1432,
  "Amount": 1.0
}
```

---

Created By Prem Shandilya  
Final Year MCA Student | AI & ML  
UPES  
SAP ID: 590017213
