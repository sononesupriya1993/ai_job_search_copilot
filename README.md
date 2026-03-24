# 💼 AI Job Search Copilot

## 📌 Project Overview

AI Job Search Copilot is an NLP-powered application that helps users analyze job descriptions and tailor their resumes more effectively.

The system extracts key skills, predicts the job role, identifies missing keywords, and provides actionable resume advice — enabling smarter and more strategic job applications.

The project is deployed as an interactive **Streamlit application** for real-time analysis.

---

## 🎯 Business Problem

Job descriptions are often long and complex, making it difficult for candidates to:

- Identify the most important skills
- Understand the exact role requirements
- Tailor their resumes effectively
- Recognize missing keywords

This leads to:
- Poor resume-job alignment
- Lower chances of getting shortlisted

This project solves that by acting as an **AI-powered job analysis assistant**.

---

## ⚙️ Methodology

### 1️⃣ Skill Extraction
- Extracts relevant skills from job descriptions
- Uses keyword-based NLP approach

### 2️⃣ Role Classification
- Classifies job into categories:
  - Data Analyst
  - Data Scientist
  - Data Engineer
  - Machine Learning Engineer
  - BI / Analytics
- Based on rule-based NLP logic

### 3️⃣ Resume Advisor
- Identifies:
  - matched skills
  - missing keywords
- Generates role-specific resume guidance

### 4️⃣ End-to-End Pipeline
Job Description → Skill Extraction → Role Prediction → Resume Advice

---

## 📊 Key Features

- 🔍 Automatic skill extraction
- 🎯 Job role prediction
- ⚠ Identification of missing keywords
- 📝 Resume-tailoring recommendations
- ⚡ Real-time analysis using Streamlit

---

📊 Experimentation (A/B Testing Approach)

To evaluate the effectiveness of AI-generated job applications, an A/B testing framework was designed:

- Group A: AI-generated applications
- Group B: Manual applications
- Metrics: Response rate, recruiter engagement, interview conversion rate

Considered statistical significance and sample size requirements for reliable comparison
This framework demonstrates how the system can be evaluated in a real-world scenario using data-driven experimentation.

---

## 📈 Example Output

Input:
> Job description for Data Scientist role

Output:
- Predicted Role: **Data Scientist**
- Extracted Skills: Python, Machine Learning, Statistics
- Missing Keywords: Experimentation, Data Analysis
- Resume Advice: Highlight ML projects, Python, statistics, and model development

---

## 🧰 Tools & Technologies

- Python
- Pandas
- NLP (text processing, keyword matching)
- Streamlit (UI application)
- Jupyter Notebook

---

## 📂 Repository Structure

ai_job_search_copilot/
│
├── app/
│ └── streamlit_app.py
│
├── src/
│ ├── skill_extractor.py
│ ├── role_classifier.py
│ ├── resume_advisor.py
│
├── notebooks/
│ ├── 1_skill_extraction.ipynb
│ └── 2_role_and_resume_logic.ipynb
│
├── data/
│ └── sample_inputs/
│ └── sample_job_descriptions.csv
│
├── outputs/
│ └── examples/
│
├── requirements.txt
└── README.md


---

## 🚀 How to Run the Project

### 1. Install dependencies

pip install -r requirements.txt

### 2. Run Streamlit App

streamlit run app/streamlit_app.py

# 💡 Use Case

This tool helps:

- job seekers tailor resumes
- identify missing skills
- understand job expectations quickly
- improve application quality

---

# 🚀 Future Improvements

- Add ML-based role classification
- Integrate LLM (OpenAI / Gemini) for smarter advice
- Add resume upload and comparison
- Add job match score
- Deploy online (Streamlit Cloud)

---

# 👩‍💻 Author

**Supriya Sonone** 
Data Scientist | AI & Analytics Enthusiast  
Oslo, Norway
