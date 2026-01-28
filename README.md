# kriscent_ml_assessment

## 📌 Project Overview

This project implements an **end-to-end Machine Learning pipeline** for real-world **Credit Card Fraud Detection**.  
It covers the **entire ML lifecycle** — from modular data processing and model debugging to performance optimization and production system design.

Key focus areas:

- Reproducibility & stability
- Handling extreme class imbalance
- Production-ready architecture
- Real-world metric optimization

---

## 🛠️ Folder Structure

```plaintext
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
```

## 🚀 Implementation Details

---

### 🔹 Task 1: Production Pipeline

**Data Cleaning**

```text
- Removed duplicate transactions
- Applied stratified train-test splits to preserve class balance
```

**Feature Engineering**

```text
Implemented Features:
- log_amount     → Handles skewness in transaction amounts
- hour           → Captures temporal fraud patterns
- amt_per_sec    → Measures transaction velocity
- amt_deviation  → Identifies anomalous spending behavior
```

**Reproducibility**

```text
- Global random seeds applied (random_state = 42)
- Ensures consistent results across multiple runs
```

**Modularization**

```text
- Data ingestion, feature engineering, and model training
  decoupled into independent .py modules
```

### 🔹 Task 2: Model Debugging & Stability

**Observed Problem**

- High variance across runs
- Unstable predictions for identical inputs

**Root Cause**

```text
- Random data splitting
- Inconsistent minority class (fraud) sampling during training
```

**Solution**

```text
- Implemented Stratified Splitting
- Fixed random seeds across the pipeline
```

**Metrics**

```text
Score Variance:
Before → 0.1129
After  → 0.0083
```

### 🔹 Task 3: Performance Improvement

**Objective**

```text
- Improve baseline Recall by ≥ 10%
```

**Techniques Applied**

```text
- Cost-Sensitive Learning
- Classification Threshold Tuning (Threshold = 0.1)
```

**Result**

```text
Recall:
Baseline → 0.7474
Improved → 0.8526
Gain     → +14.08%
```

**Justification**

```text
Lowering the threshold prioritizes fraud detection,
which is more critical than minimizing false positives
in financial risk systems.
```

### 🔹 Task 4: ML System Design

**Architecture**

```text
- Real-time inference via REST API
- Kafka for streaming data ingestion
- Prometheus for monitoring
```

**Operational Strategy**

```text
- Automated data drift detection
- Scheduled retraining to mitigate concept drift
```

**Diagrams**

```text
Full system design diagrams and documentation
available in docs/architecture.md
```

---

**Created By Prem Shandilya** UPES  
SAP ID : 590017213
