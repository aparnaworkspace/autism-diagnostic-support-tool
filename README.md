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
10. [PDF Report Example](#pdf-report-example)
11. [System Design Overview](#system-design-overview)
12. [How to Run Locally](#how-to-run-locally)
13. [Project Features](#project-features)
14. [Clinical Disclaimer](#clinical-disclaimer)
15. [Folder Structure](#folder-structure)
16. [Model Card (XGBoost)](#xgboost-model-card)
17. [Limitations](#limitations)
18. [What I Learned](#what-i-learned)
19. [About the Author](#about-the-author)

## ⭐1. Executive Summary

This project delivers a complete end-to-end **Autism Diagnostic Support System** powered by an 
optimized **XGBoost model**, **SHAP explainability**, and a premium **Apple-Health-inspired UI**.  
It transforms the AQ-10 screening questionnaire into an interactive risk-estimation tool with:

- 🧠 Real-time ASD probability prediction  
- 🎯 Transparent SHAP feature attributions  
- 🩺 Clean clinical-style interface  
- 📄 Auto-generated PDF reports  
- ⚡ A fully reproducible ML pipeline + documentation  

It is designed for **learning**, **research demonstration**, and **portfolio value** — not for clinical diagnosis.  

## ⭐2. Problem Statement

Millions of individuals remain undiagnosed or diagnosed late for Autism Spectrum Disorder (ASD) due to:

- Limited access to clinical specialists  
- Long waiting periods for assessments  
- Lack of awareness or hesitation to seek help  
- Resource constraints in low-income regions  

The challenge:  
**How can we build a fast, transparent, accessible tool to support early ASD screening — without replacing clinical evaluation?**

This project answers that by building a responsible, explainable ML-based support system using the AQ-10 screening questionnaire.

## ⭐3. Why Autism Detection Matters

- ASD affects approximately **1 in 100 people** globally  
- Early identification improves communication, social, and learning outcomes  
- Screening gaps exist in rural and low-resource healthcare systems  
- Digital tools can help triage cases early  
- Machine learning can support clinicians — not replace them  

This project demonstrates how **XAI + ML** can enhance early screening accessibility.

## ⭐4. Dataset Description

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


## ⭐5. Project Pipeline (ML Workflow)


    A[Raw Data (UCI/Kaggle AQ-10)] --> B[Data Cleaning]
    B --> C[Feature Engineering (age_group, encoding)]
    C --> D[Label Encoding]
    D --> E[Train-Test Split]
    E --> F[Model Training (XGBoost)]
    F --> G[Evaluation (Accuracy, F1, AUC)]
    G --> H[SHAP Explainability (Local + Global)]
    H --> I[Streamlit App (Apple Health UI)]
    I --> J[PDF Report Generator]
    
## ⭐6. System Architecture Diagram

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



