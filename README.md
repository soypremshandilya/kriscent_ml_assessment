# kriscent_ml_assessment

## 📌 Project Overview

This project implements an end-to-end Machine Learning pipeline for real-world Credit Card Fraud Detection.
It covers the entire ML lifecycle — from modular data processing and model debugging to performance optimization
and production system design.

Key focus areas:
- Reproducibility & stability
- Handling extreme class imbalance
- Production-ready architecture
- Real-world metric optimization

------------------------------------------------------------

## 🛠️ Folder Structure

    ├── data/               # Dataset (creditcard.csv)
    ├── docs/               # Task 4: System Design & Diagrams
    ├── models/             # Task 1: Model Persistence (.pkl files)
    ├── src/                # Task 1: Modular Codebase
    │   ├── data_pipeline.py
    │   ├── features.py
    │   ├── model_trainer.py
    │   └── inference.py
    ├── main.py             # Entry point for Production Pipeline
    ├── research_task.py    # Task 2 & 3: Debugging & Improvement
    ├── requirements.txt    # Reproducibility
    └── README.md           # Decisions & Trade-offs

------------------------------------------------------------

## 🚀 Implementation Details

### 🔹 Task 1: Production Pipeline

Data Cleaning:
    - Removed duplicate transactions
    - Applied stratified train-test splits to preserve class balance

Feature Engineering:
    Implemented Features:
    - log_amount     → Handles skewness in transaction amounts
    - hour           → Captures temporal fraud patterns
    - amt_per_sec    → Measures transaction velocity
    - amt_deviation  → Identifies anomalous spending behavior

Reproducibility:
    - Global random seeds applied (random_state = 42)
    - Ensures consistent results across multiple runs

Modularization:
    - Data ingestion, feature engineering, and model training
      decoupled into independent .py modules

------------------------------------------------------------

### 🔹 Task 2: Model Debugging & Stability

Observed Problem:
    - High variance across runs
    - Unstable predictions for identical inputs

Root Cause:
    - Random data splitting
    - Inconsistent minority class (fraud) sampling during training

Solution:
    - Implemented Stratified Splitting
    - Fixed random seeds across the pipeline

Metrics:
    Score Variance:
    - Before → 0.1129
    - After  → 0.0083

------------------------------------------------------------

### 🔹 Task 3: Performance Improvement

Objective:
    - Improve baseline Recall by ≥ 10%

Techniques Applied:
    - Cost-Sensitive Learning
    - Classification Threshold Tuning (Threshold = 0.1)

Result:
    Recall:
    - Baseline → 0.7474
    - Improved → 0.8526
    - Gain     → +14.08%

Justification:
    Lowering the threshold prioritizes fraud detection, which is more
    critical than minimizing false positives in financial risk systems.

------------------------------------------------------------

### 🔹 Task 4: ML System Design

Architecture:
    - Real-time inference via REST API
    - Kafka for streaming data ingestion
    - Prometheus for monitoring

Operational Strategy:
    - Automated data drift detection
    - Scheduled retraining to mitigate concept drift

Diagrams:
    Full system design diagrams and documentation
    available in docs/architecture.md

------------------------------------------------------------

## ⚙️ How to Run Locally

1. Clone the Repository

    git clone https://github.com/soypremshandilya/kriscent_ml_assessment.git
    cd kriscent_ml_assessment

2. Set Up Environment (Recommended: Virtual Environment)

    python -m venv venv
    source venv/bin/scripts/activate   # Windows: venv\Scripts\activate
    pip install -r requirements.txt

3. Run Production Pipeline (Task 1)

    python main.py

4. Run Research & Improvement (Tasks 2 & 3)

    python research_task.py

5. Start the API (Task 4)

    uvicorn api:app --reload

    Open:
    http://127.0.0.1:8000/docs

------------------------------------------------------------

## 👤 Author

Prem Shandilya  
UPES  
SAP ID: 590017213
