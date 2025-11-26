# **Apple-Health Inspired Streamlit App | XGBoost Model | SHAP Explainability | Full ML Pipeline**

A modern, end-to-end machine learning system that predicts Autism Spectrum Disorder (ASD) risk using the AQ-10 screening questionnaire, paired with transparent SHAP explanations, a clinical-style UI, and a clean PDF report generator.

Designed for learning, research demonstration, and portfolio showcasing — not for clinical diagnosis.

## ⭐ 1. Problem Statement

Early detection of Autism is essential for timely interventions, yet millions remain undiagnosed due to:

limited access to clinical screening

low awareness

long hospital wait-times

stigma and fear of assessment

This project builds an interactive ML-powered support tool that makes ASD risk assessment accessible, explainable, and easy to understand using a validated 10-question AQ-10 screening dataset.

## ⭐ 2. Why Autism Detection Matters

ASD affects 1 in 100 individuals globally.

Early detection improves language, learning, and social outcomes.

Digital tools help bridge the gap for low-resource clinical settings.

Machine learning can assist, but should never replace professional evaluation.


This project explores how ML + Explainability can enhance early screening systems.

## ⭐ 3. Dataset Description

Source:

Autism Screening Adults & Children Dataset (UCI / Kaggle Variants)

Contains:

AQ-10 responses (10 binary items)

Demographics: age, gender, ethnicity, country

Jaundice, family relations, “used app before”

Target column: Class/ASD → renamed to class_asd

Size: ~700 rows

Type: Questionnaire-based classification

#### 📌 Note: This dataset is small, simple, and diagnostic by design — which explains the high model performance.

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

<img width="1634" height="920" alt="Screenshot 2025-11-26 at 8 20 56 AM" src="https://github.com/user-attachments/assets/800e538c-3cc8-4fc7-9d24-d9f603f1f5bf" />

<img width="1643" height="919" alt="Screenshot 2025-11-26 at 8 21 40 AM" src="https://github.com/user-attachments/assets/1a3d1442-a1ee-4240-b6f4-f9f10d8154f3" />



### 📝 PDF Report

<img width="701" height="546" alt="Screenshot 2025-11-26 at 8 23 44 AM" src="https://github.com/user-attachments/assets/58bfa026-1a83-4a40-a868-3d22d82df919" />


## 🔍 SHAP Local Explanation (Per-Patient)

This section shows **why the XGBoost model predicted ASD Positive/Negative** for a specific patient input.  
SHAP assigns each feature a positive (pushes toward ASD+) or negative (pushes toward ASD−) contribution.

### 📌 Example Local SHAP Output
| Feature        | SHAP Value |
|----------------|------------|
| a9_score       | -1.2110    |
| a6_score       | -1.0042    |
| a5_score       | -0.8661    |
| a7_score       | -0.8091    |
| a3_score       | -0.7645    |
| a4_score       | -0.7368    |

### 🔎 Interpretation  
- **Negative SHAP values** → Feature pushes prediction toward *ASD Negative*  
- **Positive SHAP values** → Feature pushes prediction toward *ASD Positive*  
- Higher absolute magnitude = **stronger impact**

This improves transparency and trust by showing *why* the model predicted what it did for each patient.


## ⭐ 7. Model Comparison Table


| Model               | Accuracy | F1 Score | Recall | AUC    |
|---------------------|----------|----------|--------|--------|
| Logistic Regression | **1.00** | **1.00** | **1.00** | 0.99 |
| Random Forest       | 0.94     | 0.89     | 0.84   | 0.996  |
| **XGBoost (Chosen)**| **0.986** | **0.974** | **0.974** | **0.9995** |
| Neural Network      | **1.00** | **1.00** | **1.00** | **1.00** |


## ⭐ 8. Model Stack

### Core Model

XGBoost Classifier

Tuned for small structured datasets

Supports Tree SHAP (fast, reliable)

### Explainability

SHAP TreeExplainer

Local + global attribution

Top 6 most influential features shown

## ⭐ 9. SHAP Example Images

### 📌 Sample Local SHAP Bar Plot

<img width="800" height="1100" alt="shap_bar" src="https://github.com/user-attachments/assets/ac6114ae-60d1-4d10-b6c4-d5da2b87094f" />



### 📌 SHAP Beeswarm (global)

<img width="800" height="910" alt="shap_beeswarm" src="https://github.com/user-attachments/assets/26891602-a186-40bf-bb43-1137f8649b3a" />



### 📌 SHAP Waterfall Example

<img width="800" height="650" alt="shap_waterfall_sample_0" src="https://github.com/user-attachments/assets/073525b8-b967-4e00-818d-c55287b47071" />




## ⭐ 10. PDF Report Example

The app generates a clinical-style PDF including:

Prediction

Probability

AQ-10 Score

Risk Level

Recommendation

Top SHAP Features

<img width="1419" height="1092" alt="image" src="https://github.com/user-attachments/assets/7084f0a2-be79-424e-9e7d-dab4c60da130" />


## ⭐ 11. System Design Overview

### Backend

Model inference pipeline

Preprocessing (label encoders + scaler)

Age group derived feature

SHAP explanation engine

### Frontend

Apple HealthInspired UI

Glassmorphism cards

Real-time probability ring

### PDF generation

Storage

/models/ for artifacts

/reports/ for visual outputs

## ⭐ 12. How to Run Locally

1. Clone the repo
   
git clone https://github.com/aparnaworkspace/autism-diagnostic-support-tool
cd autism-diagnostic-support-tool

3. Create virtual environment

python3 -m venv venv
source venv/bin/activate

5. Install dependencies
   
pip install -r requirements.txt

7. Run Streamlit App
   
streamlit run app/streamlit_app.py

## ⭐ 13. Features Screenshot Section

Include images for:

Input form

Prediction card

SHAP charts

Risk level card

DF button

## ⭐ 14. Clinical Disclaimer

⚠️ This tool is NOT a clinical diagnostic system.

It is a portfolio project built for learning, experimentation, and demonstrating ML/SHAP explainability concepts.

Autism assessment requires:

clinical interviews

behavioural observation

developmental history

genetic & neurological assessment

## ⭐ 15. Folder Structure

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

## ⭐ 16. XGBoost Model Card

Model: XGBoostClassifier

Task: Binary classification (ASD / non-ASD)

Training data: AQ-10 questionnaire

Features: 19

Explainability: SHAP TreeExplainer

Intended use: Educational screening insights

Not intended for: Professional diagnosis

#### Strengths:

Highly separable dataset

Fast inference

Strong performance

Built-in explainability

#### Risks:

Overconfidence due to small dataset

Dataset biases may carry forward

## ⭐ 17. Limitations

### Data-related

Dataset is very small (< 800 samples)

Data is questionnaire-based, not multi-modal

AQ-10 questions are diagnostic, causing high separability

Labels may not represent real clinical outcomes

### Model-related

Cannot generalize to real-world populations

### Does not use:

behavioural observation

functional MRI

language patterns

genetics

App-related

Intended for education & research showcase only

## ⭐ 18. What I Learned

End-to-end ML pipeline design

XGBoost tuning

SHAP explainability (TreeExplainer)

Streamlit UI development

PDF report generation

Data engineering + encoding pipelines

ML ethics & model cards

GitHub project structuring

Deployment workflow

## ⭐ Final Notes

This project demonstrates:

✔ Full ML pipeline
✔ Modern, premium UI
✔ Model explainability
✔ Deployment-ready architecture
✔ Excellent GitHub presentation
