import streamlit as st
import sys
import os

# Get absolute path to src folder
current_dir = os.path.dirname(__file__)
src_path = os.path.abspath(os.path.join(current_dir, "..", "src"))

sys.path.append(src_path)

from skill_extractor import extract_skills
from role_classifier import classify_role
from resume_advisor import generate_resume_advice

st.set_page_config(page_title="AI Job Search Copilot", layout="wide")

st.title("💼 AI Job Search Copilot")
st.write("Paste a job description to extract skills, predict the role, and get resume-tailoring advice.")

job_description = st.text_area(
    "Paste the job description here",
    height=250,
    placeholder="Example: We are looking for a Data Analyst with strong SQL, Excel, and Power BI skills..."
)

if st.button("Analyze Job Description"):
    if not job_description.strip():
        st.warning("Please paste a job description first.")
    else:
        extracted_skills = extract_skills(job_description)
        predicted_role = classify_role(job_description)
        advice_output = generate_resume_advice(predicted_role, extracted_skills)

        st.subheader("📌 Predicted Role")
        st.success(predicted_role)

        st.subheader("🛠 Extracted Skills")
        if extracted_skills:
            st.write(", ".join(extracted_skills))
        else:
            st.write("No matching skills found.")

        st.subheader("⚠ Missing Keywords to Consider")
        missing_keywords = advice_output["missing_keywords"]
        if missing_keywords:
            st.write(", ".join(missing_keywords))
        else:
            st.write("No major missing keywords detected.")

        st.subheader("📝 Resume Advice")
        st.info(advice_output["resume_advice"])