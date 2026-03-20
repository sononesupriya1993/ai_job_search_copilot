# src/resume_advisor.py

ROLE_KEYWORDS = {
    "Data Analyst": [
        "sql", "excel", "power bi", "tableau", "dashboards",
        "reporting", "business insights", "stakeholder communication"
    ],
    "Data Scientist": [
        "python", "machine learning", "statistics", "model development",
        "experimentation", "scikit-learn", "data analysis"
    ],
    "Data Engineer": [
        "etl", "spark", "aws", "cloud", "data pipelines",
        "workflow automation", "large-scale data processing"
    ],
    "Machine Learning Engineer": [
        "python", "tensorflow", "deployment", "model monitoring",
        "production", "cloud infrastructure", "machine learning"
    ],
    "BI / Analytics": [
        "business intelligence", "analytics", "dashboards",
        "reporting", "insights"
    ]
}


def generate_resume_advice(predicted_role, extracted_skills):
    extracted_skills = [skill.lower() for skill in extracted_skills]

    role_keywords = ROLE_KEYWORDS.get(predicted_role, [])
    missing_keywords = [kw for kw in role_keywords if kw not in extracted_skills]

    if predicted_role == "Data Analyst":
        advice = "Highlight dashboard building, SQL analysis, reporting, and business communication projects."
    elif predicted_role == "Data Scientist":
        advice = "Highlight machine learning projects, Python, statistics, experimentation, and model-building experience."
    elif predicted_role == "Data Engineer":
        advice = "Highlight ETL pipelines, cloud platforms, workflow automation, and scalable data processing projects."
    elif predicted_role == "Machine Learning Engineer":
        advice = "Highlight ML deployment, Python, TensorFlow, production workflows, and model monitoring experience."
    elif predicted_role == "BI / Analytics":
        advice = "Highlight analytics reporting, business intelligence tools, and decision-support dashboards."
    else:
        advice = "Highlight the most relevant technical and business skills from the job description."

    return {
        "predicted_role": predicted_role,
        "matched_skills": extracted_skills,
        "missing_keywords": missing_keywords,
        "resume_advice": advice
    }