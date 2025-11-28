1. Dataset Overview

The Autism Diagnostic Support dataset used in this project combines:

Autism Screening Adult Dataset

Autism Screening Children Dataset

Both publicly available research datasets used for early ASD screening via the AQ-10 questionnaire.

The combined dataset is processed into a unified structure for model training and explainability.

2. Dataset Sources
Dataset Name	Source	License
Autism Screening Adult	Public dataset from UCI / Kaggle	Open, research use
Autism Screening Child	Public dataset from UCI / Kaggle	Open, research use

Note: No private, confidential, or medical records are used.

3. Intended Use

The dataset is intended for:

Educational ML demonstrations

Research experimentation

Model explainability studies

Risk scoring based on AQ-10

Portfolio / project showcase

Not intended for real medical diagnosis.

4. Data Fields
4.1 AQ-10 Screening Items (Binary, 0 or 1)

10 features representing symptoms:

a1_score  
a2_score  
a3_score  
a4_score  
a5_score  
a6_score  
a7_score  
a8_score  
a9_score  
a10_score

4.2 Demographic Features
Feature	Description
age	Age of person being assessed
gender	“m”, “f”, or other categories
ethnicity	Categorical ethnicity label
contry_of_res	Country of residence
used_app_before	Whether the person has used an autism app
jundice	Whether they had jaundice at birth
relation	Who filled the form (self, parent, guardian, etc.)
age_desc	“18 and more”, “4-11 years”, etc.
age_group	Engineered numeric bucket (0–4)
4.3 Target Variable
class_asd (0 = non-ASD, 1 = ASD)

5. Dataset Statistics
Total Samples:

After cleaning and merging: ≈ 700–800 (varies by source)

Class Balance (approx.):

Non-ASD: ~70%

ASD: ~30%

Feature Types:
Type	Count
Binary symptom features	10
Categorical demographic	7
Numerical	1 (age)
Engineered	1 (age_group)
Target	1
6. Preprocessing Steps

Column name standardization

Removal of invalid or missing AQ-10 items

Label encoding of categorical features

Age group feature creation (0–4 bins)

Min-max or standard scaling for numeric features

Train-test splitting (80/20)

Saving processed datasets (X_train, X_test, y_train, y_test)

7. Ethical Considerations
7.1 Potential Risks

Overreliance on ML predictions for sensitive diagnoses

Misinterpretation of AQ-10 scores

Dataset may not fully represent all populations

Bias from imbalanced class distribution

Cultural differences in symptom reporting

7.2 Mitigation

Clearly mark app as non-clinical

Use only for education & research

Provide SHAP explainability

Include risk scoring + recommendation section

Encourage professional follow-up for real assessments

8. Limitations

Self-reported questionnaire data

Limited demographic diversity

Not medically validated for diagnosis

No longitudinal medical history

Small dataset (<1K rows)

May contain noise or reporting bias

9. Who Should Use This Dataset?

✔ Students
✔ Researchers
✔ ML enthusiasts
✔ Portfolio project builders
✔ Educators
✔ Explainable-AI demonstrations

❌ Not for clinical decision-making
❌ Not for production healthcare systems

10. Dataset Versioning
Component	Version
Raw Dataset	v1.0
Cleaned Combined Dataset	v1.0
Feature Engineering Pipeline	v1.0
Model Training Dataset	v1.0
11. Maintainer

Aparna Sajeevan
GitHub: https://github.com/aparnaworkspace

Project: Autism Diagnostic Support Tool

12. Contact

For any dataset questions or improvement suggestions:
raise issues via GitHub Issues.