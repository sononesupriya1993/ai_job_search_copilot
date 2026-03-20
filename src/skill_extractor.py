# src/skill_extractor.py

SKILL_KEYWORDS = [
    "python",
    "sql",
    "excel",
    "power bi",
    "tableau",
    "machine learning",
    "statistics",
    "scikit-learn",
    "etl",
    "spark",
    "aws",
    "azure",
    "tensorflow",
    "cloud",
    "dashboards",
    "data analysis",
    "model development",
    "workflow automation"
]


def extract_skills(job_description: str):
    text = str(job_description).lower()
    found_skills = []

    for skill in SKILL_KEYWORDS:
        if skill in text:
            found_skills.append(skill)

    return sorted(list(set(found_skills)))