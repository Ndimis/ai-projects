## What is Data Drift?

**Data drift** happens when the data used by a machine learning model **changes over time**.  
As a result, the model was trained on an "old world" but must make predictions in a "new world" → its performance decreases.

---

## Simple Example

Imagine a model that predicts whether an email is spam:

- In 2023: many spam emails contain “crypto”, “bitcoin”  
- The model learns this → it works well  

But in 2025:
- Spam emails now talk about “AI”, “quick investment”  
- The vocabulary changed → **data drift**  
- The model becomes less accurate  

---

## The 3 Main Types of Drift

### 1. Covariate Drift (input distribution changes)
The **input data changes**, but not necessarily the relationship to the target.

Example:
- Before: mostly adult customers  
- Now: many young users  
- The model sees different profiles than during training  

---

### 2. Concept Drift (relationship changes)
The **relationship between input and output changes**.

Example:
- Before: frequent buyers = loyal customers  
- Now: frequent buyers = discount hunters  
- The underlying logic changed → more dangerous  

---

### 3. Label Drift (class proportion changes)
The proportion of classes changes.

Example:
- Before: 5% fraud  
- Now: 20% fraud  

---

## How to Detect Data Drift

We usually monitor:

- 📉 Model performance (accuracy, error, etc.)  
- 📊 Data distribution (statistics, histograms)  
- 🧪 Statistical tests (KS test, PSI, etc.)  

---

## How to Fix Data Drift

1. **Retrain regularly** with fresh data  
2. Set up **monitoring in production**  
3. Use **automatic retraining pipelines**  
4. Train with more diverse data from the start  
5. Detect drift early before performance drops too much  

---

## One-Sentence Summary

> **Data drift** happens when real-world data changes, but the model stays stuck in the past.

---
## How to Measure Data Drift

In production, companies continuously measure data drift using statistical and monitoring techniques.

### 1. Population Stability Index (PSI)

PSI measures how much a feature distribution has shifted between **training data** and **production data**.

**Rule of thumb:**
- PSI < 0.1 → No drift
- 0.1 ≤ PSI < 0.25 → Moderate drift
- PSI ≥ 0.25 → Significant drift (action needed)

Used mainly for tabular data and risk / finance models.

---

### 2. Kolmogorov–Smirnov Test (KS Test)

The KS test compares two distributions and detects whether they are statistically different.

Used for:
- Numerical feature drift
- Detecting subtle distribution changes

If the **p-value is very small**, drift is likely present.

---

### 3. KL Divergence (Kullback–Leibler)

Measures how one probability distribution diverges from another.

- KL = 0 → identical distributions
- Higher KL → stronger drift

Common in:
- Deep learning
- NLP / probabilistic systems

---

### 4. Model Performance Monitoring

Sometimes drift is detected indirectly by tracking:

- Accuracy
- F1 score
- AUC
- Prediction error
- Calibration

If performance drops → drift may be occurring.

---

### 5. Data Quality Monitoring

Companies also track:

- Missing values
- Outliers
- Feature mean / variance
- Category frequency changes

Tools often used:
- Evidently AI
- WhyLabs
- Arize AI
- Fiddler AI

---

## How Companies Handle Data Drift in Production

Large companies treat drift as a **normal production problem**, not an exception.

### 1. Continuous Data Monitoring

They monitor in real-time:

- Feature distributions
- Data quality
- Prediction distribution
- Model confidence

Alerts are triggered when drift exceeds thresholds.

---

### 2. Shadow / Champion-Challenger Models

Companies often run:

- **Champion model** → current production model
- **Challenger model** → new retrained model

If challenger performs better → automatic replacement.

---

### 3. Automated Retraining Pipelines

Modern ML systems retrain automatically when:

- Enough new data arrives
- Drift is detected
- Performance drops

Common stack:
- Airflow / Kubeflow / Prefect
- Feature Store (Feast, Tecton)
- CI/CD for ML (MLOps)

---

### 4. Data Versioning and Reproducibility

Companies track:

- Dataset versions
- Model versions
- Training conditions

Tools:
- DVC
- MLflow
- Weights & Biases

This allows rollback if drift causes failure.

---

### 5. Human-in-the-Loop (Critical Systems)

For high-risk systems (fraud, medical, finance):

- Humans review uncertain predictions
- Labels are fed back into training data
- Model improves continuously

---

### 6. Drift-Aware Model Design

Advanced companies design models robust to drift:

- Online learning models
- Incremental training
- Domain adaptation
- Ensemble models
- Regularization against distribution shift

---

## Real-World Examples

**Netflix / YouTube**
- User behavior changes constantly → models retrained daily

**Banks / Fraud Detection**
- Fraud patterns evolve → drift monitored hourly

**E-commerce (Amazon, Shopify)**
- Seasonal drift (Black Friday, holidays) handled via adaptive retraining

**Autonomous systems**
- Sensor / environment drift monitored continuously

---

## Simple Production Rule

> If you don’t monitor drift, your model will silently fail.
