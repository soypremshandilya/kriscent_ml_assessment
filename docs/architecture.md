ML System Design: Production-Grade Fraud Detection

1. Problem Statement
   Design a production-ready ML system to identify fraudulent transactions in real-time. The system must handle extreme class imbalance (0.17% fraud) and prioritize Recall (catching fraud) while maintaining high stability.

2. End-to-End Flow

A. Data Ingestion & Engineering

Ingestion: Raw transaction data is streamed via Kafka for real-time processing.

Validation: Incoming data is validated against a schema to ensure no missing values or incorrect data types enter the pipeline.

Feature Engineering: Features such as amt_deviation and log_amount are calculated in real-time before being passed to the model.

B. Training Pipeline

Modular Code: The pipeline is built using modular Python scripts (data_pipeline.py, model_trainer.py) to ensure maintainability.

Reproducibility: Global random seeds and stratified splitting ensure the training process is stable across different runs.

Model Selection: A Random Forest Classifier was selected for its ability to handle non-linear relationships in tabular data.

C. Inference Flow

Cost-Sensitive Serving: To address class imbalance without increasing memory overhead, the model utilizes Class Weights during training to penalize misclassification of the minority (fraud) class.

Threshold Tuning: The production API uses a Custom Threshold (0.1) rather than the default 0.5. This ensures high sensitivity, allowing the system to catch a higher percentage of fraud attempts.

Latency: The inference logic is optimized for <100ms response times.

D. Monitoring & Maintenance

Drift Detection: The system monitors for Feature Drift (e.g., shifts in average transaction amounts) and Concept Drift (e.g., new fraud patterns).

Retraining Strategy: An automated retraining trigger is initiated if the F1-Score or Recall drops below a predefined baseline, or on a scheduled monthly basis.

3. Deployment Decisions & Trade-offs

Recall vs. Precision: We intentionally chose a lower threshold (0.1) to maximize Recall. While this increases the number of false positives (manual reviews for bank agents), it significantly reduces the financial loss from missed fraud.

Modular vs. Notebook: The logic was moved from research scripts to modular Python packages to support unit testing and CI/CD integration.
