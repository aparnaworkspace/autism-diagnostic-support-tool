# ============================================================
# Autism Diagnostic Support Tool — UI V4 (Apple Health PRO)
# White rounded cards, soft shadows, minimal inline SVG icons
# Preserves model/scaler/encoders/SHAP logic (no ML changes)
# ============================================================

import streamlit as st
import pandas as pd
import numpy as np
import joblib
import shap
import matplotlib.pyplot as plt
from pathlib import Path
from fpdf import FPDF
import sys
import base64
from io import BytesIO

# ----------------- Project root -----------------
ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT))
from src.risk_scoring import compute_risk_score

# ----------------- Artifact paths -----------------
RAW_PATH    = ROOT / "data" / "raw" / "autism_screening.csv"
MODEL_PATH  = ROOT / "models" / "best_model.pkl"
SCALER_PATH = ROOT / "models" / "scaler.pkl"
ENC_PATH    = ROOT / "models" / "label_encoders.pkl"
SHAP_PATH   = ROOT / "models" / "shap_explainer_and_values.pkl"
REPORT_DIR  = ROOT / "reports"
REPORT_DIR.mkdir(parents=True, exist_ok=True)

# ----------------- Header logo (uploaded) -----------------
# Use the uploaded file path you provided earlier. If it isn't available, app continues.
LOGO_LOCAL_PATH = "/mnt/data/de5ec9d2-8e35-4a98-be7a-eb997c21bb33.png"

# ----------------- Feature order (must match training) -----------------
FEATURE_ORDER = [
    "a1_score","a2_score","a3_score","a4_score","a5_score",
    "a6_score","a7_score","a8_score","a9_score","a10_score",
    "age","gender","ethnicity","jundice","contry_of_res",
    "used_app_before","age_desc","relation","age_group"
]
SYMPTOM_COLS = [f"a{i}_score" for i in range(1, 11)]

# ----------------- Streamlit config -----------------
st.set_page_config(page_title="Autism Diagnostic Support", layout="wide")

# ----------------- Apple Health PRO styling -----------------
st.markdown(
    """
    <style>
    :root {
        --bg: #fbfdfd;
        --card: #ffffff;
        --muted: #6b7280;
        --accent: #4bc0b9;  /* gentle mint */
        --accent-2: #e7faf9;
    }
    /* page */
    .app-root { background: var(--bg); padding: 10px 18px; }
    /* header */
    .header-wrap {
        display:flex; align-items:center; gap:18px;
        padding:12px; border-radius:16px;
        background: linear-gradient(180deg, rgba(255,255,255,0.98), rgba(255,255,255,0.96));
        box-shadow: 0 12px 30px rgba(10,20,20,0.06);
        margin-bottom: 18px;
    }
    .title-main { font-size:22px; font-weight:800; color:#083535; }
    .title-sub  { font-size:13px; color:var(--muted); margin-top:4px; }
    /* glass card */
    .card {
        background: var(--card);
        border-radius: 20px;
        padding: 18px;
        box-shadow: 0 10px 30px rgba(12,20,20,0.06);
    }
    .card-compact { padding:12px; border-radius:16px; }
    .muted { color: var(--muted); font-size:13px; }
    .metric-lg { font-size:28px; font-weight:800; color:#062e2e; }
    .pill {
        display:inline-block; padding:6px 12px; border-radius:999px;
        background: var(--accent-2); color: var(--accent); font-weight:700;
    }
    /* circle progress */
    .circle-wrap { display:inline-block; width:86px; height:86px; border-radius:999px; background: linear-gradient(180deg,#fff,#fbfffd); display:flex; align-items:center; justify-content:center; box-shadow: 0 8px 24px rgba(12,20,20,0.06); }
    .small-muted { color:var(--muted); font-size:13px; }
    /* table adjustments */
    .stTable thead th { background: transparent; color:#083535; font-weight:700; }
    /* tiny icon */
    .icon { width:18px; height:18px; vertical-align:middle; margin-right:8px; opacity:0.95; }
    </style>
    """,
    unsafe_allow_html=True,
)

# ----------------- Load data & artifacts -----------------
@st.cache_data
def load_raw():
    df = pd.read_csv(RAW_PATH)
    df.columns = df.columns.str.strip().str.lower().str.replace("-", "_").str.replace(" ", "_").str.replace("/", "_")
    return df

@st.cache_resource
def load_artifacts():
    model = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)
    enc = joblib.load(ENC_PATH)
    shap_obj = None
    if SHAP_PATH.exists():
        try:
            shap_obj = joblib.load(SHAP_PATH)
        except Exception:
            shap_obj = None
    return model, scaler, enc, shap_obj

raw_df = load_raw()
model, scaler, enc_maps, saved_shap = load_artifacts()

# ----------------- helpers -----------------
def compute_age_group(age):
    a = float(age)
    if a <= 12: return 0
    if a <= 18: return 1
    if a <= 35: return 2
    if a <= 60: return 3
    return 4

def encode_row(row_dict, enc_maps):
    r = row_dict.copy()
    for col, mapping in enc_maps.items():
        if col in r:
            r[col] = mapping.get(str(r[col]), mapping.get("nan", 0))
    return r

def unique_sorted(col):
    if col in raw_df.columns:
        return sorted(raw_df[col].astype(str).unique().tolist())
    return []

def svg_icon(name="user", size=18):
    # small set of simple line SVG icons for a premium look
    icons = {
        "user": '<svg class="icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M12 12c2.761 0 5-2.239 5-5s-2.239-5-5-5-5 2.239-5 5 2.239 5 5 5zM3 20.5c0-3.038 4.03-5.5 9-5.5s9 2.462 9 5.5" stroke="#073535" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"/></svg>',
        "age": '<svg class="icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M12 2v6l4 2" stroke="#073535" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"/><circle cx="12" cy="12" r="9" stroke="#073535" stroke-width="1.2"/></svg>',
        "shield": '<svg class="icon" viewBox="0 0 24 24" fill="none"><path d="M12 2l7 3v6c0 7-7 11-7 11s-7-4-7-11V5l7-3z" stroke="#073535" stroke-width="1.0" stroke-linecap="round" stroke-linejoin="round"/></svg>'
    }
    return icons.get(name, icons["user"])

# ----------------- Header -----------------
# ----------------- Header (Centered) -----------------
st.markdown(
    f"""
    <div style="
        display:flex;
        justify-content:center;
        align-items:center;
        margin-top:10px;
        margin-bottom:20px;
    ">
        <div class="header-wrap" style="max-width: 900px; width:100%; text-align:center;">
            <div style="width:100%; text-align:center;">
                <div class="title-main" style="text-align:center;">Autism Diagnostic Support</div>
                <div class="title-sub" style="text-align:center;">
                    Apple Health style — educational demo (not clinical)
                </div>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)


# ----------------- Sidebar inputs -----------------
st.sidebar.markdown("<div style='font-weight:700;margin-bottom:6px;color:#073535'>Patient Input</div>", unsafe_allow_html=True)
with st.sidebar.form("input_form"):
    age = st.number_input("Age", 1, 120, 25)
    gender = st.selectbox("Gender", unique_sorted("gender"))
    relation = st.selectbox("Relation reporting", unique_sorted("relation"))
    used_app = st.selectbox("Used app before?", unique_sorted("used_app_before"))
    with st.expander("Advanced (optional)"):
        ethnicity = st.selectbox("Ethnicity", unique_sorted("ethnicity"))
        country = st.selectbox("Country of residence", unique_sorted("contry_of_res"))
        jundice = st.selectbox("Jaundice at birth?", unique_sorted("jundice"))
        age_desc = st.selectbox("Age descriptor", unique_sorted("age_desc"))
    st.markdown("**AQ-10 (0 = No, 1 = Yes)**")
    cols = st.columns(2)
    inputs = {}
    for i, c in enumerate(SYMPTOM_COLS):
        with cols[i % 2]:
            inputs[c] = st.selectbox(c.upper(), [0,1], index=0, key=f"in_{c}")
    submitted = st.form_submit_button("Save")
    if submitted:
        st.session_state["user_input"] = {
            **inputs,
            "age": age,
            "gender": gender,
            "relation": relation,
            "used_app_before": used_app,
            "ethnicity": ethnicity if 'ethnicity' in locals() else "?",
            "contry_of_res": country if 'country' in locals() else "?",
            "jundice": jundice if 'jundice' in locals() else "no",
            "age_desc": age_desc if 'age_desc' in locals() else "18 and more"
        }
        st.sidebar.success("Saved ✅ — view prediction on the right")

# ----------------- Main dashboard -----------------
if "user_input" not in st.session_state:
    st.info("Please fill the Patient Input (sidebar) and click Save.")
    st.stop()

user = st.session_state["user_input"]

# prepare model input (match FEATURE_ORDER)
row = user.copy()
row["age_group"] = compute_age_group(row["age"])
enc_row = encode_row(row, enc_maps)
X_user = pd.DataFrame([{k: enc_row.get(k, 0) for k in FEATURE_ORDER}]).astype(float)

# scale & predict
X_scaled = X_user.copy()
# apply transform in FEATURE_ORDER order to guarantee matching feature names
X_scaled[FEATURE_ORDER] = scaler.transform(X_user[FEATURE_ORDER])

proba = float(model.predict_proba(X_scaled)[0,1])
pred = int(model.predict(X_scaled)[0])
label_text = "ASD Positive" if pred == 1 else "ASD Negative"
pill = "🟥" if pred == 1 else "🟩"

# Top row layout
c1, c2, c3 = st.columns([2,1,1], gap="large")

# Prediction card
with c1:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown(f"<div class='muted'>{svg_icon('user')} Patient</div>", unsafe_allow_html=True)
    st.markdown(f"<div style='font-weight:700'>{user.get('relation','Self')} • {user.get('age')} yrs • {user.get('gender')}</div>", unsafe_allow_html=True)
    st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)

    # circle probability
    percent = int(round(proba * 100))
    # simple circular SVG indicator
    circle_svg = f'''
    <div style="display:flex;align-items:center;gap:14px">
      <div class="circle-wrap">
        <svg width="64" height="64" viewBox="0 0 36 36" xmlns="http://www.w3.org/2000/svg">
          <path d="M18 2.0845
            a 15.9155 15.9155 0 0 1 0 31.831
            a 15.9155 15.9155 0 0 1 0 -31.831" fill="none" stroke="#eee" stroke-width="3.5"></path>
          <path d="M18 2.0845
            a 15.9155 15.9155 0 0 1 0 31.831" fill="none" stroke="#4bc0b9" stroke-width="3.5" stroke-dasharray="{percent} {100-percent}" stroke-linecap="round"></path>
          <text x="18" y="20" font-size="8" text-anchor="middle" fill="#083535" font-weight="700">{percent}%</text>
        </svg>
      </div>
      <div>
        <div style="font-weight:800;font-size:20px">{label_text}</div>
        <div class="muted">Probability (ASD+)</div>
      </div>
    </div>
    '''
    st.markdown(circle_svg, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# AQ-10 card
with c2:
    st.markdown("<div class='card card-compact'>", unsafe_allow_html=True)
    score = sum(int(user[c]) for c in SYMPTOM_COLS)
    st.markdown("<div class='muted'>AQ-10 Score</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='metric-lg'>{score} / 10</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# Risk card
with c3:
    st.markdown("<div class='card card-compact'>", unsafe_allow_html=True)
    risk_series = pd.Series({c: user[c] for c in SYMPTOM_COLS})
    risk_series["age"] = user["age"]
    total_score, risk_level, rec = compute_risk_score(risk_series)
    symbol = "🟢" if risk_level == "Low Risk" else ("🟡" if risk_level == "Medium Risk" else "🔴")
    st.markdown("<div class='muted'>Risk Level</div>", unsafe_allow_html=True)
    st.markdown(f"<div style='font-weight:700'>{symbol} {risk_level}</div>", unsafe_allow_html=True)
    st.markdown("<div class='muted' style='margin-top:8px'>Recommendation</div>", unsafe_allow_html=True)
    st.write(rec)
    st.markdown("</div>", unsafe_allow_html=True)

# SHAP explanation (local)
st.markdown("<div class='card' style='margin-top:16px'>", unsafe_allow_html=True)
st.markdown("<div style='display:flex;justify-content:space-between;align-items:center'><div style='font-weight:700'>Local explainability</div><div class='muted'>Top feature impacts</div></div>", unsafe_allow_html=True)

df_imp = pd.DataFrame({"feature": [], "shap": []})
try:
    expl = saved_shap["explainer"] if isinstance(saved_shap, dict) and "explainer" in saved_shap else shap.TreeExplainer(model)
    shap_vals = expl(X_user)
    vals = shap_vals.values[0] if hasattr(shap_vals, "values") else shap_vals[0]
    df_imp = (pd.DataFrame({"feature": FEATURE_ORDER, "shap": vals})
              .assign(abs_val=lambda d: d.shap.abs())
              .sort_values("abs_val", ascending=False)
              .head(6))
    st.table(df_imp[["feature","shap"]].set_index("feature"))

    fig, ax = plt.subplots(figsize=(8,3))
    ax.barh(df_imp["feature"], df_imp["shap"], color="#4bc0b9")
    ax.set_xlabel("SHAP value (impact)")
    plt.tight_layout()
    st.pyplot(fig)
except Exception as e:
    st.info("SHAP explanation unavailable: " + str(e))

st.markdown("</div>", unsafe_allow_html=True)

# Generate PDF
st.markdown("<div style='margin-top:12px' class='card'>", unsafe_allow_html=True)
if st.button("Generate PDF report"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "Autism Diagnostic Report (AQ-10)", ln=True)
    pdf.ln(6)
    pdf.set_font("Arial", "", 12)
    pdf.cell(0, 8, f"Prediction: {label_text}", ln=True)
    pdf.cell(0, 8, f"Probability: {proba:.3f}", ln=True)
    pdf.cell(0, 8, f"AQ-10 Score: {score}/10", ln=True)
    pdf.cell(0, 8, f"Risk Level: {risk_level}", ln=True)
    pdf.multi_cell(0, 7, f"Recommendation: {rec}")
    pdf.ln(6)
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 8, "Top SHAP features:", ln=True)
    pdf.set_font("Arial", "", 11)
    for item in df_imp.to_dict(orient="records"):
        pdf.cell(0, 7, f"{item['feature']}: {item['shap']:.4f}", ln=True)

    out = REPORT_DIR / f"report_{int(pd.Timestamp.now().timestamp())}.pdf"
    pdf.output(str(out))
    with open(out, "rb") as f:
        st.download_button("Download PDF", f, file_name=out.name)
    st.success(f"Saved to {out}")

st.markdown("</div>", unsafe_allow_html=True)

st.caption("Apple Health PRO UI — educational demo only. Not a medical diagnostic tool.")
