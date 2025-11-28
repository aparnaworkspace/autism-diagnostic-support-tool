1. High-level summary

This project is an end-to-end ML demo that ingests AQ-10 screening + demographic data, performs preprocessing and feature engineering, trains an XGBoost model, exposes predictions and SHAP explanations via a Streamlit app, and stores artifacts in models/ and reports/. The system is intended for demonstration and educational purposes only (not clinical use).

2. Logical components
+------------------+      +----------------------+      +-----------------------+
|  User (Browser)  | <--> |  Streamlit Web App   | <--> |  Model artifacts      |
|  (Desktop/Mobile)|      |  (app/streamlit_app) |      |  (models/*.pkl)       |
+------------------+      +----------------------+      +-----------------------+
         |                         |                             ^
         |                         |                             |
         v                         v                             |
  (Input Form)              (Prediction + SHAP)                 |
                                                  +--------------+-------------+
                                                  |  Data (raw & processed)    |
                                                  |  data/raw/   data/processed|
                                                  +--------------+-------------+


Components:

Notebooks (notebooks/01_EDA.ipynb, 02_Feature_Engineering.ipynb, 03_Model_Training.ipynb) — exploration, FE, model training.

Preprocessing module (src/preprocess.py) — deterministic cleaning & encodings.

Feature engineering (src/preprocess.py / notebooks) — creates total_symptom_score, age_group, encoders.

Training module (src/train_model.py) — trains models, saves best_model.pkl, scaler.pkl, label_encoders.pkl, shap_explainer_and_values.pkl.

Explainability (src/explainability.py) — SHAP helpers (beeswarm, waterfall).

Risk scoring (src/risk_scoring.py) — deterministic rule-based score for PDF & UI.

App (app/streamlit_app.py) — UI, loads artifacts, encodes input, scales, predicts, generates PDF.

Reports (reports/) — generated plots, SHAP images, PDFs.

Model artifacts (models/) — trained model, scaler, encoders, SHAP object.

3. Data flow (detailed)

Raw ingestion: data/raw/*.csv → notebook / src/preprocess.py.

Cleaning & FE:

Normalize column names

Convert types, fix age outliers

Create total_symptom_score, age_group, high_risk_flag

Encode categorical columns (deterministic label maps saved as label_encoders.pkl)

Split & scale:

Stratified train_test_split on target class_asd

Fit StandardScaler on numeric features → save scaler.pkl

Train:

Train XGBoost + baseline models

Evaluate and select best model (here: XGBoost)

Save best_model.pkl (XGBoost), optionally save the best model architecture/params

Explainability:

Generate SHAP explainer and sample SHAP outputs and save object for quick loading

App:

Streamlit loads raw_df for encoder choices, loads encoders & scaler & model, computes age_group on-the-fly, encodes input, scales, predicts, computes local SHAP, shows risk-scoring and downloads PDF.

4. File / folder map (important)
autism-diagnostic-support-tool/
├── app/
│   └── streamlit_app.py
├── data/
│   ├── raw/
│   └── processed/
├── docs/
│   └── SYSTEM_ARCHITECTURE.md   <-- you are placing this file here
├── models/
│   ├── best_model.pkl
│   ├── scaler.pkl
│   ├── label_encoders.pkl
│   └── shap_explainer_and_values.pkl
├── notebooks/
├── reports/
├── src/
│   ├── preprocess.py
│   ├── train_model.py
│   └── risk_scoring.py
├── requirements.txt
└── README.md

5. Deployment options (step-by-step highlights)
Option A — Streamlit Community Cloud (fastest, easiest for portfolio)

In GitHub repo settings, point Streamlit to branch & main file app/streamlit_app.py.

Add requirements.txt with exact versions.

Set secrets/env vars (if any) in Streamlit Cloud UI (none required for demo).

Click deploy.
Pros: free demo, simple.
Cons: limited compute, not for production.

Option B — Docker (recommended for reproducible self-host)

Dockerfile (example) — put at repo root:

FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENV PYTHONUNBUFFERED=1
EXPOSE 8501
CMD ["streamlit", "run", "app/streamlit_app.py", "--server.port=8501", "--server.runOnSave=false"]


Build & run:

docker build -t autism-app:latest .
docker run -p 8501:8501 --rm autism-app:latest

Option C — Heroku / Render / VPS

Use Docker or direct Python environment on server.

Ensure secrets and model artifacts are present (push models/ or load from cloud storage).

6. CI/CD (GitHub Actions) — example

.github/workflows/ci.yml (basic):

name: CI

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      - name: Install deps
        run: pip install -r requirements.txt
      - name: Lint
        run: pip install flake8 && flake8 src app
      - name: Run smoke tests
        run: pytest -q


For deployment, add a second workflow to push to DockerHub/Render/Streamlit Cloud.

7. Versioning & artifact management

Code: Git + branches (feature / develop / main).

Data & models: Use DVC or store versioned models as models/best_model_v1.pkl. For medium projects consider MLflow.

Reproducibility: Freeze requirements.txt. Commit training seeds and numpy / sklearn / xgboost versions.

8. Security & privacy considerations

PII / PHI: avoid storing personally identifiable info; current datasets are public. Add a privacy checklist prior to any real-world deployment.

Secrets: do not commit API keys or credentials. Use environment variables or secret stores.

Model safety: show clear disclaimers, do not present as diagnosis.

Dependencies: pin versions to avoid supply-chain issues.

9. Monitoring & observability

Logging: add request logging in Streamlit (simple file logs or structured logs).

Model drift: collect anonymized (consented) inputs & predictions to monitor drift.

Metrics: track request rate, average latency, top errors.

Crash reporting: Sentry or similar for production.

10. Testing

Unit tests for:

src/preprocess.py (type conversion, outlier handling)

src/risk_scoring.py (boundary cases)

src/train_model.py (small smoke training)

Integration tests:

Load model & run predict on small sample

Streamlit smoke test (headless run)

Example pytest command:

pytest tests/ -q

11. Scalability & cost

For a demo, Streamlit Cloud is fine.

For higher traffic:

Containerize and run behind a load balancer (Kubernetes / ECS).

Use autoscaling and a model-serving stack (TorchServe or Seldon for model infra) if moving to production.

Offload explainability heavy-lifting (SHAP) to background worker if latency is important.


