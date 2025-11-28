ETHICS_CARD — Autism Diagnostic Support Tool

Project: Autism Diagnostic Support Tool (AQ-10 screening demo)
Author / Maintainer: Aparna Sajeevan — https://github.com/aparnaworkspace
Date: 2025-11-25
Status: Educational demo (NOT for clinical diagnosis)

1. Purpose & Scope

This Ethics Card documents ethical considerations, possible harms, and mitigation steps for the Autism Diagnostic Support Tool — a demonstration app that predicts ASD screening outcomes from AQ-10 questionnaire + simple demographics and provides risk-scoring and explainability (SHAP).

Important: The app and model are educational demos only and not intended for clinical use, diagnosis, or treatment decisions.

2. Summary of risks

Misuse for clinical diagnosis: Non-clinical models can be mistaken for authoritative diagnostics.

False negatives/positives: Missed cases (false negatives) can delay care; false positives can cause anxiety and unnecessary follow-ups.

Data bias: Under- or over-representation of certain demographic groups may degrade fairness and generalization.

Privacy / re-identification: Demographic or free-text inputs could risk re-identifying individuals if logged or shared carelessly.

Overtrust & automation bias: Users may over-rely on model outputs without clinical context.

Cultural sensitivity: Question interpretation and reporting vary across cultures and ages.

3. Data provenance & consent

Source: Public autism screening datasets (adult + child sets) from open sources (Kaggle / public research).

License: Public / research use. No proprietary or private medical records included.

Consent: Original datasets are assumed to have been collected under research/consent terms appropriate to their source. This project does not collect new user data for model training.

Recommendation: If you plan to collect or log user inputs in deployment, obtain explicit informed consent and store only the minimum required data, with clear opt-out.

4. Fairness & bias analysis

Observed imbalance: Class imbalance exists (approx ~70% NO / ~30% YES). Demographic skew may exist (country/ethnicity/gender).

Potential bias vectors:

Socio-cultural differences in symptom reporting.

Language and literacy barriers for questionnaires.

Age-group distribution differences between child/adult datasets.

Mitigations implemented:

Stratified train/test split to preserve label distribution.

Label encoder mappings saved deterministically.

Feature importance analysis (SHAP) to examine drivers of prediction results.

Recommended next steps:

Evaluate per-group metrics (precision, recall, FPR, FNR by gender, age_group, geography).

Add balanced samples or perform re-sampling / class-weighting only after careful validation.

Use fairness-aware metrics and, if required, fairness correction (e.g., threshold adjustment per group) with clinical oversight.

5. Privacy & security controls

No PII required: App asks only non-identifying demographic fields; avoid collecting names, emails, or IDs.

Storage: If you log inputs or results, store encrypted at rest and limit retention. Consider anonymization and aggregation for analytics.

Access control: Model artifacts and logs should be stored in restricted repositories or storage buckets (use environment-based secrets for credentials).

Recommendations:

Do not commit user data or logs to Git or public repos.

Use HTTPS for deployed apps, and environment secrets for keys.

Provide a privacy policy if publicly deployed.

6. Explainability & transparency

Explainability: SHAP is provided to surface contributing features per-prediction.

Limitations of SHAP: For non-tree models or poorly calibrated models, SHAP outputs may be misleading; we fall back to a message when SHAP is not applicable.

Recommendations:

Always show SHAP alongside a clear plain-language explanation.

Provide a short interpretation guide in the app explaining what a positive SHAP value means and that these are model-level statistical influences, not clinical evidence.

7. Human-in-the-loop & deployment safeguards

Never automated decision making: The system should be used to inform conversation only, not as autonomous diagnosis.

UI guardrails to implement:

Prominent disclaimer: “For educational purposes only — not a diagnosis.”

Strong visual cues when model confidence is low (e.g., probability close to 0.5).

Suggested next steps (e.g., clinician referral) instead of prescriptive commands.

Escalation & resources: Show local clinician / support contact lists or helplines if available.

8. Handling adverse outcomes

False negative mitigation: Highlight uncertainty; recommend follow-up if symptoms persist despite a negative screen.

False positive mitigation: Provide calming language, explain screening nature, and encourage seeking professional confirmation.

Audit trail: Record model version and artifact checksum in each report to facilitate incident investigation.

9. Model governance & lifecycle

Versioning: Save and release models as best_model_vX.pkl with metadata and code version.

Evaluation cadence: Re-run fairness & calibration checks every time you retrain or add new data.

Responsible deprecation: If a model is found unsafe for a group, deprecate promptly and notify stakeholders.

Responsible owners: Assign who reviews model updates and approves deployment.

10. Metrics to monitor in production

Performance: Accuracy, recall, precision, AUC, F1.

Calibration: Brier score, calibration curves.

Fairness: Per-group recall / FPR / FNR for protected attributes.

Drift: Input distribution drift (population statistics) and performance drift (periodic test on labeled set).

Privacy logs: Number of records stored, retention time, access logs.

11. User-facing wording & disclaimers (recommended)

Primary disclaimer (top of UI):
“This tool is an educational screening demo based on AQ-10. It is not a medical diagnosis. If you are concerned, please contact a qualified health professional.”

Result wording (example):

“Model output: ASD Screening Positive (probability: 0.72). This indicates a higher risk based on this screening tool. This is not a diagnosis. Consider professional assessment.”

12. Ethical checklist before public deployment

 Remove or minimize logging of raw user inputs (or obtain explicit consent).

 Add clear UI disclaimer and guidance to seek clinical care.

 Run subgroup performance tests (gender, age_group, ethnicity, country).

 Ensure model and artifacts have pinned versions & checksums.

 Implement secure storage and secrets management.

 Define owner & incident response procedure.

 Add a clear privacy policy and contact method.

13. Sample consent wording (short)

I understand this is an educational tool. I consent to my anonymized input being used for debugging or aggregate analytics, and I understand that any output is not medical advice.

14. Responsible contacts / reporting

Maintainer: Aparna Sajeevan — GitHub: https://github.com/aparnaworkspace

Issue reporting: Use the repository Issues to report bugs, bias concerns, or privacy issues.

15. Limitations & closing note

This Ethics Card is a living document. It is intentionally conservative: the dataset and model are small and not clinically validated. If you take this project toward any real-world screening use, consult clinical experts, privacy counsel, and run rigorous prospective studies.