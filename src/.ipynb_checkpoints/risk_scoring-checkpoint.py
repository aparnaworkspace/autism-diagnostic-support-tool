# src/risk_scoring.py

"""
Risk Scoring Module for Autism Diagnostic Support Tool

This module computes:
- Total Autism Symptom Score (AQ-10 style)
- Risk Level (Low / Medium / High)
- Clinical Recommendation Text

Used by:
- Model training validation
- Streamlit app
- PDF report generator
"""

def compute_risk_score(row):
    """
    Compute total symptom score and risk level based on AQ-10 thresholds.
    
    Parameters:
        row (pd.Series): A single row of feature inputs.
    
    Returns:
        total_score (int)
        risk_level (str)
        recommendation (str)
    """

    symptom_cols = [
        'a1_score', 'a2_score', 'a3_score', 'a4_score', 'a5_score',
        'a6_score', 'a7_score', 'a8_score', 'a9_score', 'a10_score'
    ]

    # Calculate total score
    total_score = int(row[symptom_cols].sum())

    # Decide risk level
    if total_score <= 6:
        risk_level = "Low Risk"
        recommendation = (
            "Current symptom pattern does not strongly indicate ASD. "
            "No immediate clinical action is necessary. "
            "Monitor if new symptoms appear."
        )

    elif 7 <= total_score <= 8:
        risk_level = "Medium Risk"
        recommendation = (
            "Some ASD-related traits are present. "
            "A formal screening by a qualified clinician is recommended."
        )

    else:  # total_score 9-10
        risk_level = "High Risk"
        recommendation = (
            "Strong indicators of ASD traits. "
            "A detailed clinical assessment is highly recommended."
        )

    return total_score, risk_level, recommendation
