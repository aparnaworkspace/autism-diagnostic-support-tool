<p align="center"> <img src="banner04.png" width="100%" /> </p> <h1 align="center">🧠 Autism Diagnostic Support System</h1> <p align="center"><b>XGBoost · SHAP Explainability · Streamlit Clinical UI</b></p> <p align="center"> <img src="https://img.shields.io/badge/Machine%20Learning-XGBoost-blue?style=for-the-badge" /> <img src="https://img.shields.io/badge/Explainability-SHAP-purple?style=for-the-badge" /> <img src="https://img.shields.io/badge/UI-Streamlit-green?style=for-the-badge" /> <img src="https://img.shields.io/badge/Python-3.10+-yellow?style=for-the-badge" /> </p>
🔍 Executive Summary

A modern, end-to-end Autism Screening Support System built using:

XGBoost (high-performance ML classifier)

SHAP Explainability (clinical-style feature attributions)

Apple-Health inspired UI (clean, minimal, professional)

PDF report generator (summary + SHAP insights)

This project is built for learning, explainability research, and portfolio showcasing — not for clinical diagnosis.

📑 Table of Contents

Problem Statement

Dataset

ML Pipeline

Architecture

Screenshots

Explainability

Model Comparison

How to Run

Model Card

Limitations

What I Learned

⭐ Problem Statement

Millions remain undiagnosed due to:

Limited access to clinical specialists

Long hospital wait-times

Low awareness & stigma

This project builds a transparent, interactive ML tool to assist early ASD screening using the AQ-10 questionnaire.

📊 Dataset

Source: Kaggle / UCI Autism Screening (Adults & Children)
Rows: ~700
Features:

10 AQ-10 binary responses

Age, gender, ethnicity, country

Jaundice, family relation, app-usage

📌 Dataset is diagnostic → high separability → high model accuracy.

🔁 ML Pipeline
flowchart LR
A[Raw Data] --> B[Cleaning]
B --> C[Feature Engineering]
C --> D[Label Encoding]
D --> E[Train-Test Split]
E --> F[XGBoost Model]
F --> G[Evaluation]
G --> H[SHAP Explainability]
H --> I[Streamlit App + PDF Report]

🏗 Architecture
flowchart TD
UI[Streamlit UI] --> API[Prediction Engine]
API --> M[XGBoost Model]
API --> S[Scaler]
API --> LE[Label Encoders]
M --> SHAP[TreeExplainer]
SHAP --> UI
API --> PDF[PDF Generator]

📱 Screenshots
<details> <summary>🖼 Click to expand</summary>
🔹 Home Screen & Prediction Dashboard
<img src="https://github.com/user-attachments/assets/220a8538-6a02-41b0-97e0-60737187011b" width="700" />
🔹 Model Output
<img src="https://github.com/user-attachments/assets/7d08017c-18f1-4842-bda1-a7cdca3373e9" width="700" />
🔹 PDF Report
<img src="https://github.com/user-attachments/assets/e447423b-4165-4282-921e-3cfd676ffe0b" width="500" /> </details>
🔍 Explainability
SHAP Local Explanation Example
Feature	SHAP Value
a9_score	-1.21
a6_score	-1.00
a5_score	-0.86
a7_score	-0.80
a3_score	-0.76
a4_score	-0.73

✔ Negative → pushes towards ASD−
✔ Positive → pushes towards ASD+

<details> <summary>📊 SHAP Visualizations</summary>
🔹 Bar Plot
<img src="https://github.com/user-attachments/assets/c3a85107-179f-402f-a47a-1d5676b14189" width="600" />
🔹 Beeswarm
<img src="https://github.com/user-attachments/assets/00109a6d-889b-4866-a9a4-d9a827ff1974" width="600" />
🔹 Waterfall
<img src="https://github.com/user-attachments/assets/ce7e3ce4-f2d8-4087-9ac0-f11fb8cb4c8b" width="600" /> </details>
📈 Model Comparison
Model	Accuracy	F1	Recall	AUC
Logistic Regression	1.00	1.00	1.00	0.99
Random Forest	0.94	0.89	0.84	0.996
XGBoost (Chosen)	0.986	0.974	0.974	0.9995
Neural Network	1.00	1.00	1.00	1.00
▶️ How to Run
git clone https://github.com/aparnaworkspace/autism-diagnostic-support-tool
cd autism-diagnostic-support-tool

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt
streamlit run app/streamlit_app.py

📄 Model Card

Model: XGBoost
Features: 19
Explainability: SHAP TreeExplainer
Use Case: Educational screening aid

Strengths

Excellent performance

Highly interpretable

Fast inference

Risks

Small dataset

Questionnaire-based → artificially separable

⚠️ Limitations

Dataset < 800 rows

Based only on AQ-10 questionnaire

No behavioral/MRI/audio/video data

Cannot generalize to clinical populations

Not a diagnostic system

🎓 What I Learned

End-to-end ML pipeline design

XGBoost tuning

SHAP explainability

Streamlit UI engineering

PDF report generation

Model cards + ethical AI

GitHub project structuring

Deployment workflow

