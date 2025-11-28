This document summarizes how different machine-learning algorithms performed on the autism screening dataset (AQ-10 based).
All models were trained using the same processed dataset, same feature set, and identical train-test split.

1. Models Compared
Model	Framework
Logistic Regression	sklearn
Random Forest Classifier	sklearn
XGBoost Classifier	xgboost
Neural Network (MLPClassifier)	sklearn
2. Evaluation Metrics

We compared all models using:

Accuracy

F1 Score

Recall (important for ASD-positive detection)

Precision

ROC-AUC

Confusion Matrix

Calibration Curve

3. Summary Table of Performance
XGBoost emerged as the strongest model overall.
Model	Accuracy	F1	Recall	ROC-AUC	Notes
Logistic Regression	1.00	1.00	1.00	~1.00	Great baseline; slightly overfits
Random Forest	0.94	0.89	0.84	0.996	Good; slight drop in recall
XGBoost	0.986	0.974	0.974	0.9995	⭐ Best model (balanced, stable, high recall)
Neural Network (MLP)	1.00	1.00	1.00	~1.00	Overfits; unstable on retrain
4. Detailed Comparison
4.1 Logistic Regression

Perfect scores on this test split

But extremely sensitive to feature encoding

Not ideal for mixed categorical data

Limited modeling capacity

📌 Good baseline, but not robust for real-world variability

4.2 Random Forest

Strong model but slightly lower recall

Tends to underperform on small datasets

Feature importance alignment inconsistent

📌 Acceptable, but not top choice

4.3 XGBoost (Chosen Model)

Highest real, stable performance

Handles class imbalance well

Produces reliable SHAP explanations

Works well with categorical encodings

Excellent recall (~97.4%)

📌 Selected as final model because it balances performance + interpretability + stability.

4.4 Neural Network (MLP)

Perfect metrics due to overfitting

Very sensitive to random weight initialization

Harder to explain

Not ideal for small datasets

📌 Good experiment, not reliable enough for final deployment

5. Confusion Matrix

Stored in:

reports/confusion_matrix.png


Interpretation for XGBoost:

Very low false negatives

Very low false positives

Excellent for a screening tool

6. ROC Curve

Stored in:

reports/roc_curve.png


XGBoost ROC-AUC ≈ 0.9995, indicating nearly perfect separability.

7. Calibration Curve

Stored in:

reports/calibration_plot.png


XGBoost shows excellent probability calibration — predicted probabilities correspond well to real likelihood.

8. Final Model Selection
Chosen Model:
🏆 XGBoost Classifier (best_model.pkl)

Because it provides:

Highest recall

Best overall metrics

Great generalization

Best compatibility with SHAP

More stable than NN

Better calibrated than Logistic Regression

9. Recommendation

To improve credibility further:

Add more pediatric + adult samples

Train with stratified K-Fold cross-validation

Add uncertainty estimates

Deploy with version control and MLflow or DVC