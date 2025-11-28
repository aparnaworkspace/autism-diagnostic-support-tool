Model Card: Autism Diagnostic Support Tool (AQ-10 Screening)
1. Model Overview

This model is a binary classification system designed to estimate the likelihood of Autism Spectrum Disorder (ASD) using the AQ-10 screening questionnaire along with demographic features.

⚠️ Important:
This model is for educational and demonstration purposes only.
It is not a medical device and cannot diagnose ASD.

2. Intended Use
Primary

Portfolio demonstration of an end-to-end ML pipeline

Educational use: explainability (SHAP), calibration, metrics

Screening support insights using AQ-10-based inputs

Not Intended For

Clinical diagnosis

Real-world medical decision-making

Replacement for professional evaluation

3. Model Details
Component	Details
Algorithm	XGBoost Classifier
Version	1.0
Training Framework	Python, scikit-learn, XGBoost
Explainability	SHAP TreeExplainer
Preprocessing	Label Encoding + StandardScaler
Feature Count	19
Task	Binary Classification (ASD+ / ASD–)
4. Dataset Summary

The model uses the combined:

Autism Screening Adult Dataset

Autism Screening Children Dataset

After preprocessing, data includes:

Type	Count
Total Samples	~700+ before splitting
Train Samples	~560
Test Samples	~140
Feature Categories

AQ-10 symptoms: a1–a10

Demographics: age, gender, ethnicity

Medical: jaundice status

Metadata: relation, used_app_before, country of residence

Engineered: age_group

5. Evaluation Metrics (Test Set)

Model: XGBoost
Test Samples: 141

Metric	Score
Accuracy	0.9858
F1-Score	0.9737
Recall (Sensitivity)	0.9737
Precision	0.9736
AUC-ROC	0.9995
Classification Report
precision    recall  f1-score   support
0       0.99      0.99      0.99       103
1       0.97      0.97      0.97        38
accuracy                           0.99       141

6. Confusion Matrix

True Positives: 37

False Positives: 1

False Negatives: 1

True Negatives: 102

Saved as: reports/confusion_matrix.png

7. ROC Curve

AUC = 0.9995

Saved as: reports/roc_curve.png

8. Calibration Curve

XGBoost shows overconfident probability outputs (common behavior), producing a non-smooth calibration curve due to small dataset size.

Saved as: reports/calibration_curve.png

9. Explainability (SHAP)

The app provides:

Local explainability (per-sample SHAP values)

Global ranking (top contributing features)

Typical top drivers:

a9_score

a6_score

a7_score

a5_score

a3_score

Saved SHAP object:
models/shap_explainer_and_values.pkl

10. Ethical Considerations
Potential Risks

Incorrect classification may cause unnecessary concern

Bias due to demographic imbalance in dataset

Overfitting due to small dataset

Overconfident probability outputs

Mitigations

Clear disclaimer in UI

Transparent SHAP explanations

Detailed calibration analysis

Avoid using sensitive demographic data for decision-making in real deployments

11. Limitations

Not a clinical diagnostic system

Small dataset → limited generalization

Model trained on AQ-10 self-report screening data

Cultural / demographic diversity limited by dataset

Probability calibration not perfect

12. Recommended Future Improvements

Deploy with Platt scaling or isotonic regression for better calibration

Retrain on larger, clinically validated datasets

Add confidence intervals

Add drift monitoring for deployment

Build a clinician-friendly interface