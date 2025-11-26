<p align="center">
  <img src="banner04.png" width="100%" />
</p>
<!-- EXECUTIVE SUMMARY  -->
<p align="center">
  <div style="
      background: #e8f1ff;
      border-radius: 16px;
      padding: 22px;
      max-width: 780px;
      margin: auto;
      box-shadow: 0 4px 14px rgba(0,0,0,0.06);
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto;
  ">
    <h2 align="center" style="color:#1d4ed8; margin-bottom:10px;">
      ⭐ Executive Summary
    </h2>
    <p align="center" style="color:#1e3a8a; font-size:15px;">
      This project is a full end-to-end <b>Autism Diagnostic Support System</b>, blending 
      <b>Machine Learning</b>, <b>Explainable AI</b>, and a polished Apple-Health-style UI.  
      It predicts ASD likelihood using the validated AQ-10 questionnaire via a tuned 
      <b>XGBoost model</b>, enhanced by <b>SHAP local & global explanations</b>.
      The system includes real-time probability rings, structured risk scoring, 
      and automatic PDF report generation.
      <br><br>
      Built completely from scratch, it demonstrates expertise in 
      <b>data engineering</b>, <b>model development</b>, <b>explainability</b>,
      <b>UI/UX engineering</b>, and <b>deployment-ready architecture</b>.
    </p>
  </div>
</p>

# 🧠 Autism Diagnostic Support System
## XGBoost • SHAP Explainability • Apple-Health Inspired Clinical UI

A modern, end-to-end machine learning system that predicts Autism Spectrum Disorder (ASD) likelihood using the AQ-10 screening questionnaire, paired with transparent SHAP explainability, a clean Apple-Health-style UI, and clinical-style PDF report generation.

This project is built for learning, explainability research, and portfolio showcasing — not clinical diagnosis.

## ⭐ 1. Problem Statement

Early ASD screening is critical, yet millions remain undiagnosed due to:

Limited access to clinical specialists

Long hospital wait-times

Low awareness

Stigma or fear of evaluation

This project builds an interactive ML-powered support tool that makes ASD risk easier to screen using a validated AQ-10 questionnaire, while **ensuring explainability, transparency, and responsible UI design.**

## ⭐ 2. Why Autism Detection Matters

ASD affects 1 in 100 individuals worldwide

Early detection improves social, cognitive, and language outcomes

Digital screening tools support low-resource clinical settings

ML assists clinicians — but does not replace clinical evaluation

This project explores how **ML + Explainable AI (XAI) can enhance early screening systems.**

## ⭐ 3. Dataset Description

### Source:
UCI / Kaggle — Autism Screening Adults & Children Dataset

### Contains:

AQ-10 responses (10 binary items)

Demographics: age, gender, ethnicity, country

Jaundice, family relation

"Used autism app before"

Target: class_asd

### Size: ~700 rows
### Type: Questionnaire-based classification

📌 Note: Dataset is small and diagnostic by design → high model accuracy.

## ⭐ 4. Project Pipeline (ML Workflow)


A[Raw Data] --> B[Data Cleaning]

B --> C[Feature Engineering]

C --> D[Label Encoding]

D --> E[Train-Test Split]

E --> F[XGBoost Training]

F --> G[Model Evaluation]

G --> H[SHAP Explainability]

H --> I[Streamlit App + PDF Report]

I --> J[Deployment]

## ⭐ 5. System Architecture Diagram

UI[Streamlit UI] --> API

API[Prediction Engine] --> Model[XGBoost Model]

API --> Scaler[StandardScaler]

API --> Encoders[Label Encoders]

Model --> SHAP[TreeExplainer]

SHAP --> UI

API --> Report[PDF Generator]

## ⭐ 6. Screenshot Previews

### 📱 Home / Prediction Dashboard


[Home]
<img width="1634" height="920" alt="Screenshot 2025-11-26 at 8 20 56 AM" src="https://github.com/user-attachments/assets/220a8538-6a02-41b0-97e0-60737187011b" />

[Prediction]
<img width="1643" height="919" alt="Screenshot 2025-11-26 at 8 21 40 AM" src="https://github.com/user-attachments/assets/7d08017c-18f1-4842-bda1-a7cdca3373e9" />


### 📝 PDF Report

[PDF]

<img width="710" height="546" alt="Screenshot 2025-11-26 at 7 52 03 AM" src="https://github.com/user-attachments/assets/e447423b-4165-4282-921e-3cfd676ffe0b" />


## ⭐ 7. SHAP Local Explanation (Per-Patient)

This section shows why XGBoost predicted ASD Positive/Negative.

SHAP assigns each feature a positive (toward ASD+) or negative (toward ASD−) contribution.

### 📌 Example Local SHAP Output

| Feature  | SHAP Value |
| -------- | ---------- |
| a9_score | -1.2110    |
| a6_score | -1.0042    |
| a5_score | -0.8661    |
| a7_score | -0.8091    |
| a3_score | -0.7645    |
| a4_score | -0.7368    |


### 🔎 Interpretation

**Negative SHAP** → pushes prediction toward ASD Negative

**Positive SHAP** → pushes prediction toward ASD Positive

**Larger magnitude** → stronger contribution

Explainability improves transparency, trust, and model accountability.

## ⭐ 8. Model Comparison Table

| Model               | Accuracy | F1 Score | Recall | AUC    |
|---------------------|----------|----------|--------|--------|
| Logistic Regression | 1.00     | 1.00     | 1.00   | 0.99   |
| Random Forest       | 0.94     | 0.89     | 0.84   | 0.996  |
| XGBoost (Chosen)    | 0.986    | 0.974    | 0.974  | 0.9995 |
| Neural Network      | 1.00     | 1.00     | 1.00   | 1.00   |


## ⭐ 9. Model Stack

### Core Model

XGBoost Classifier

Optimized for small, structured datasets

Supports TreeSHAP → fast & reliable explainability

### Explainability

SHAP TreeExplainer

Local + Global contributions

Top-6 features shown

## ⭐ 10. SHAP Example Images

### 📌 Local SHAP Bar Plot

[SHAP Bar]

<img width="800" height="1100" alt="shap_bar" src="https://github.com/user-attachments/assets/c3a85107-179f-402f-a47a-1d5676b14189" />


### 📌 SHAP Beeswarm (Global)

[SHAP Beeswarm]

<img width="800" height="910" alt="shap_beeswarm" src="https://github.com/user-attachments/assets/00109a6d-889b-4866-a9a4-d9a827ff1974" />


### 📌 SHAP Waterfall (Per-sample)

[SHAP Waterfall]

<img width="800" height="650" alt="shap_waterfall_sample_0" src="https://github.com/user-attachments/assets/ce7e3ce4-f2d8-4087-9ac0-f11fb8cb4c8b" />


## ⭐ 11. PDF Report Example

The app generates a clinical-style PDF summarizing:

Prediction

Probability

AQ-10 Score

Risk Level

Recommendation

Top SHAP Features

<img width="1624" height="919" alt="Screenshot 2025-11-26 at 8 22 04 AM" src="https://github.com/user-attachments/assets/fc1c0aa2-7e27-4d9b-8bdf-594269ebbdc1" />


## ⭐ 12. System Design Overview

### Backend

XGBoost inference pipeline

Label encoding + scaling

Age-group engineered feature

SHAP explainability

### Frontend

Apple-Health inspired UI

Soft shadows, rounded cards

Real-time probability ring

PDF generation

### Storage

/models/ → ML artifacts

/reports/ → SHAP outputs + visuals

## ⭐ 13. How to Run Locally
git clone https://github.com/aparnaworkspace/autism-diagnostic-support-tool
cd autism-diagnostic-support-tool


Create venv:

python3 -m venv venv
source venv/bin/activate


Install dependencies:

pip install -r requirements.txt


Run the Streamlit app:

streamlit run app/streamlit_app.py

## ⭐ 14. Features (Screenshots Section)

Include images for:

Input Form

Prediction Card

SHAP Charts

Risk Level Card

PDF Button

Final Output

## ⭐ 15. Clinical Disclaimer

⚠️ This is NOT a diagnostic tool.
It is a **portfolio / educational project.**

Autism diagnosis requires:

Behavioural observation

Clinical interviews

Developmental history

Neuropsychological testing

Genetic & neurological evaluation

## ⭐ 16. Folder Structure


autism-diagnostic-support-tool/

│
├── app/

│   └── streamlit_app.py

├── data/

│   ├── raw/

│   └── processed/

├── models/

│   ├── best_model.pkl

│   ├── scaler.pkl

│   ├── label_encoders.pkl

│   └── shap_explainer_and_values.pkl

├── notebooks/

│   ├── 01_EDA.ipynb

│   ├── 02_Feature_Engineering.ipynb

│   └── 03_Model_Training.ipynb

├── reports/

├── src/

│   ├── preprocess.py

│   ├── train_model.py

│   ├── risk_scoring.py

│   └── explainability.py

└── README.md

## ⭐ 17. XGBoost Model Card

**Model:** XGBoostClassifier

**Task:** Binary classification (ASD / non-ASD)

**Features:** 19

**Explainability:** SHAP TreeExplainer

**Intended Use:** Educational demo

### Strengths

Very strong performance

Fast inference

Deep explainability

Works well with structured data

### Risks

Small dataset → risks overfitting

Questionnaire-based data → high separability

May not generalize outside dataset

## ⭐ 18. Limitations

### Dataset

Small (<800 rows)

Highly diagnostic questions → easy classification

No behavioural/video/MRI data

### Model

Cannot replace clinical evaluations

Contains dataset biases

### App

Built for learning, portfolio, and research

## ⭐ 19. What I Learned

Full ML pipeline design

XGBoost tuning

SHAP explainability

Streamlit UI engineering

Apple-Health style UI creation

PDF report generation

ML ethics & model cards

GitHub project structure

End-to-end deployment workflow
