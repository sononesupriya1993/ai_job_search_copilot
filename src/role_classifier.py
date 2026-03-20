def classify_role(job_description: str):
    text = str(job_description).lower()

    # Data Engineer
    if any(keyword in text for keyword in [
        "etl", "spark", "aws", "data pipeline", "workflow automation",
        "large-scale data processing", "cloud platforms"
    ]):
        return "Data Engineer"
    
    # Machine Learning Engineer
    if any(keyword in text for keyword in [
         "tensorflow", "model monitoring", "deploy ml models",
        "deployment", "production", "ml engineer"
    ]):
        return "Machine Learning Engineer"
    
    # Data Scientist
    if any(keyword in text for keyword in [
        "machine learning", "statistics", "scikit-learn",
        "experimentation", "model development", "data scientist"
    ]):
        return "Data Scientist"
    
    # Data Analyst
    if any(keyword in text for keyword in [
        "power bi", "tableau", "dashboards", "excel",
        "business data", "stakeholders", "sql", "reporting"
    ]):
        return "Data Analyst"
    
    # BI / Analytics
    if any(keyword in text for keyword in [
        "business intelligence", "analytics", "insights"
    ]):
        return "BI / Analytics"
    
    return "Other"