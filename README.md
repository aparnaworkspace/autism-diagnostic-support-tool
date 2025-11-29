<p align="center">
  <img src="banner04.png" width="100%" />
</p>

<h1 align="center">🧠 Autism Diagnostic Support System</h1>
<p align="center"><b>XGBoost · SHAP Explainability · Apple-Health Inspired UI</b></p>

<p align="center">
  <img src="https://img.shields.io/badge/Machine%20Learning-XGBoost-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Explainability-SHAP-purple?style=for-the-badge" />
  <img src="https://img.shields.io/badge/UI-Streamlit-green?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Python-3.10+-yellow?style=for-the-badge" />
</p>

<p align="center">
  <a href="https://autism-diagnostic-support-tool-2rngfswshayeyl7tghwwpt.streamlit.app/">
    <img src="https://img.shields.io/badge/Live%20Demo-Streamlit%20App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" />
  </a>
</p>

## 📑 Table of Contents

1. [Executive Summary](#executive-summary)
2. [Problem Statement](#problem-statement)
3. [Why Autism Detection Matters](#why-autism-detection-matters)
4. [Dataset Description](#dataset-description)
5. [Project Pipeline (ML Workflow)](#project-pipeline-ml-workflow)
6. [System Architecture](#system-architecture)
7. [Model Performance & Comparison](#model-performance--comparison)
8. [Explainability (SHAP)](#explainability-shap)
9. [Streamlit App UI Preview](#streamlit-app-ui-preview)
10. [Project Features](#project-features)
11. [How to Run Locally](#how-to-run-locally)
12. [Folder Structure](#folder-structure)
13. [Clinical Disclaimer](#clinical-disclaimer)
14. [Limitations](#limitations)


## Executive Summary

This project delivers a complete end-to-end **Autism Diagnostic Support System** powered by an 
optimized **XGBoost model**, **SHAP explainability**, and a premium **Apple-Health-inspired UI**.  
It transforms the AQ-10 screening questionnaire into an interactive risk-estimation tool with:

- 🧠 Real-time ASD probability prediction  
- 🎯 Transparent SHAP feature attributions  
- 🩺 Clean clinical-style interface  
- 📄 Auto-generated PDF reports  
- ⚡ A fully reproducible ML pipeline + documentation  

It is designed for **learning**, **research demonstration**, and **portfolio value** — not for clinical diagnosis.  

## Problem Statement

Millions of individuals remain undiagnosed or diagnosed late for Autism Spectrum Disorder (ASD) due to:

- Limited access to clinical specialists  
- Long waiting periods for assessments  
- Lack of awareness or hesitation to seek help  
- Resource constraints in low-income regions  

The challenge:  
**How can we build a fast, transparent, accessible tool to support early ASD screening — without replacing clinical evaluation?**

This project answers that by building a responsible, explainable ML-based support system using the AQ-10 screening questionnaire.

## Why Autism Detection Matters

- ASD affects approximately **1 in 100 people** globally  
- Early identification improves communication, social, and learning outcomes  
- Screening gaps exist in rural and low-resource healthcare systems  
- Digital tools can help triage cases early  
- Machine learning can support clinicians — not replace them  

This project demonstrates how **XAI + ML** can enhance early screening accessibility.

## Dataset Description

**Source:**  
UCI / Kaggle — Autism Screening Adults & Children Dataset

**Dataset Type:**  
Questionnaire-based binary classification (ASD vs Non-ASD)

**Contents:**
- **AQ-10** questionnaire (10 binary questions)
- **Demographics:**  
  age, gender, ethnicity, country of residence  
- **Medical factors:** jaundice at birth  
- **Social factors:** relation (parent/self), used autism app before  
- **Target:** `class_asd`

**Size:** ~700 samples  
**Features:** 19  
**Label distribution:** Balanced enough for supervised learning

📌 **Note:**  
The dataset is **small and highly separable** because AQ-10 questions are directly diagnostic.  
This explains the unusually high performance of ML models.


## Project Pipeline (ML Workflow)


    subgraph PREP[Data Preparation]
        A1[Raw Data]
        A2[Cleaning]
        A3[Feature Engineering]
        A4[Encoding]
        A5[Train-Test Split]
        A1 --> A2 --> A3 --> A4 --> A5
    end

    subgraph MODEL[Modeling]
        B1[XGBoost Training]
        B2[Evaluation]
        B3[SHAP Explainability]
        B1 --> B2 --> B3
    end

    subgraph APP[Application Layer]
        C1[Streamlit App]
        C2[PDF Report Generator]
    end

    A5 --> B1
    B3 --> C1
    C1 --> C2

    
## System Architecture Diagram

```mermaid
flowchart LR
    subgraph UI[Streamlit Frontend]
        A1[Input Form]
        A2[Prediction Dashboard]
        A3[PDF Report Button]
    end

    subgraph API[Backend Inference Layer]
        B1[Preprocessing Pipeline]
        B2[Label Encoders]
        B3[StandardScaler]
        B4[XGBoost Model]
        B5[SHAP TreeExplainer]
    end

    subgraph Storage[Artifacts & Reports]
        C1[models/]
        C2[reports/]
        C3[data/processed/]
    end

    %% Connections
    A1 --> B1
    B1 --> B2
    B1 --> B3
    B3 --> B4
    B4 --> B5
    B4 --> A2
    B5 --> A2
    A3 --> C2
    B4 --> C1
    B2 --> C1
    B3 --> C1
```

## Model Performance & Comparison

| Model                 | Accuracy | F1 Score | Recall | AUC      |
|----------------------|----------|----------|--------|----------|
| Logistic Regression   | 1.00     | 1.00     | 1.00   | 0.99     |
| Random Forest         | 0.94     | 0.89     | 0.84   | 0.996    |
| XGBoost (Chosen)      | **0.986**| **0.974**| **0.974** | **0.9995** |
| Neural Network (MLP)  | 1.00     | 1.00     | 1.00   | 1.00     |

### 🏆 Why XGBoost Was Chosen
- Best trade-off between **accuracy**, **stability**, and **interpretability**
- Works extremely well on **small structured datasets**
- Fully compatible with **TreeSHAP** for transparent explainability
- Fast, robust, and highly generalizable

## Explainability (SHAP)

This project uses **SHAP (SHapley Additive Explanations)** to provide
transparent, interpretable insights into *why* the model predicts
ASD Positive or Negative.

### 🔍 Local SHAP (Per-Patient Explanation)
Shows how each feature contributed to an individual prediction.

Example:

| Feature    | SHAP Value |
|----------- |----------- |
| a9_score   | -1.2110    |
| a6_score   | -1.0042    |
| a5_score   | -0.8661    |
| a7_score   | -0.8091    |
| a3_score   | -0.7645    |
| a4_score   | -0.7368    |

- **Negative SHAP** → pushes toward *ASD Negative*  
- **Positive SHAP** → pushes toward *ASD Positive*  
- **Larger magnitude** → stronger influence

### 🌍 Global Explainability
SHAP also generates global-level insights:

- Which features influence predictions the most?
- How strongly do AQ-10 symptoms contribute?
- How does age or relation reporting affect outcomes?

## Streamlit App — UI Gallery
<details> <summary><strong>📸 Click to expand full UI + SHAP gallery</strong></summary> <br>
  
🏠 Home Dashboard
<p align="center"> <img src="assets/home.png" width="85%"> </p>

🔍 Prediction View (Model Output)
<p align="center"> <img src="assets/prediction.png" width="85%"> </p>

📝 Generated PDF Report
<p align="center"> <img src="assets/pdf_report.png" width="85%"> </p>

🧠 SHAP Explainability

📌 Local Feature Impact (Bar Plot)
<p align="center"> <img src="assets/shap_bar.png" width="85%"> </p>

📌 Global Beeswarm Plot
<p align="center"> <img src="assets/shap_beeswarm.png" width="85%"> </p>

📌 Waterfall (Single Sample)
<p align="center"> <img src="assets/shap_waterfall_sample_0.png" width="85%"> </p>

📈 Evaluation Metrics

✔️ Confusion Matrix
<p align="center"> <img src="assets/confusion_matrix.png" width="80%"> </p>

✔️ ROC Curve
<p align="center"> <img src="assets/roc_curve.png" width="80%"> </p>

✔️ Calibration Curve
<p align="center"> <img src="assets/calibration_curve.png" width="80%"> </p>

</details>

## Project Features
<details> <summary><strong>✨ Click to expand Feature Highlights</strong></summary> <br>
  
### 💡 Core Features

ASD Risk Prediction using an optimized XGBoost classifier

Apple-Health Inspired UI with clean, clinical-style cards

Real-time Probability Ring that visualizes ASD+ likelihood

AQ-10 Questionnaire Input (10 binary symptom questions)

Demographic Inputs with encoded categorical features

Dynamic Risk Scoring based on total AQ-10 + age

SHAP Explainability (local + global)

### 🧠 Explainability Features

Local SHAP force explanation (per patient)

Global beeswarm + bar importance plots

Waterfall plot for individual predictions

Top 6 contributing features displayed in-dashboard

### 📄 PDF Report Generator

Exports a clinical-style report containing:

Prediction

Probability

AQ-10 score

Risk level

Recommendation

Top SHAP contributions

Great for portfolio + recruiters.

### 📚 Machine Learning Pipeline

Preprocessing: encoding + feature engineering

Train/test split

XGBoost model training

ROC, AUC, confusion matrix, calibration

Serialized model artifacts saved in /models/

### 🧪 Evaluation & Model Monitoring

Confusion Matrix

ROC Curve

Calibration Curve

Model Comparison Table

SHAP-based auditing

### 🏗️ Software Architecture Highlights

Clear separation of concerns (src/, app/, models/, notebooks/)

Production-like artifact loading in Streamlit

Modular risk scoring function

Explainability integrated into UI

### 🚀 Deployment-Ready

Fully packaged Streamlit app

GitHub-friendly structure

Works locally or on cloud platforms (Streamlit Cloud)

</details>

