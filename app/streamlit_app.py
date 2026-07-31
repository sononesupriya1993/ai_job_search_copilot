import streamlit as st
import sys
import os

current_dir = os.path.dirname(__file__)
src_path = os.path.abspath(os.path.join(current_dir, "..", "src"))
sys.path.append(src_path)

from skill_extractor import extract_skills
from role_classifier import classify_role
from resume_advisor import generate_resume_advice
from application_tracker import init_db, log_application  # ← ADD THIS

st.set_page_config(page_title="AI Job Search Copilot", layout="wide")

init_db()  # ← ADD THIS — sets up database when app starts

st.title("💼 AI Job Search Copilot")
st.write("Paste a job description to extract skills, predict the role, and get resume-tailoring advice.")

# ── NEW: user inputs for logging ──────────────────────────────
col1, col2, col3 = st.columns(3)
with col1:
    company_name = st.text_input("Company Name", placeholder="e.g. Microsoft")
with col2:
    role_title = st.text_input("Role Title", placeholder="e.g. Data Scientist")
with col3:
    app_type = st.selectbox("Application Type", ["AI-assisted", "Manual"])
# ─────────────────────────────────────────────────────────────

job_description = st.text_area(
    "Paste the job description here",
    height=250,
    placeholder="Example: We are looking for a Data Analyst with strong SQL..."
)

if st.button("Analyze & Save Application"):  # ← RENAMED BUTTON
    if not job_description.strip():
        st.warning("Please paste a job description first.")
    else:
        extracted_skills = extract_skills(job_description)
        predicted_role = classify_role(job_description)
        advice_output = generate_resume_advice(predicted_role, extracted_skills)
        missing_keywords = advice_output["missing_keywords"]

        # ── NEW: save to database ─────────────────────────────
        if company_name and role_title:
            log_application(
                company=company_name,
                role=role_title,
                job_description=job_description,
                predicted_role=predicted_role,
                match_score=len(extracted_skills),
                missing_keywords=missing_keywords,
                application_type=app_type
            )
            st.toast("✅ Application logged successfully!")
        # ─────────────────────────────────────────────────────

        st.subheader("📌 Predicted Role")
        st.success(predicted_role)

        st.subheader("🛠 Extracted Skills")
        if extracted_skills:
            st.write(", ".join(extracted_skills))
        else:
            st.write("No matching skills found.")

        st.subheader("⚠ Missing Keywords to Consider")
        if missing_keywords:
            st.write(", ".join(missing_keywords))
        else:
            st.write("No major missing keywords detected.")

        st.subheader("📝 Resume Advice")
        st.info(advice_output["resume_advice"])