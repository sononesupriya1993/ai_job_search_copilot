import sqlite3
import uuid
from datetime import datetime

def init_db():
    """Create the applications database if it doesn't exist"""
    conn = sqlite3.connect('data/applications.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS applications (
            application_id   TEXT PRIMARY KEY,
            date_applied     TEXT,
            company          TEXT,
            role             TEXT,
            job_description  TEXT,
            predicted_role   TEXT,
            match_score      REAL,
            missing_keywords TEXT,
            application_type TEXT,
            status           TEXT DEFAULT 'applied',
            response_date    TEXT,
            notes            TEXT
        )
    ''')
    conn.commit()
    conn.close()

def log_application(company, role, job_description, 
                    predicted_role, match_score, 
                    missing_keywords, application_type):
    """Save a new application to the database"""
    conn = sqlite3.connect('data/applications.db')
    c = conn.cursor()
    c.execute('''
        INSERT INTO applications VALUES (?,?,?,?,?,?,?,?,?,?,?,?)
    ''', (
        str(uuid.uuid4()),
        datetime.today().strftime('%Y-%m-%d'),
        company,
        role,
        job_description,
        predicted_role,
        match_score,
        ', '.join(missing_keywords),
        application_type,
        'applied',
        None,
        ''
    ))
    conn.commit()
    conn.close()

def update_status(application_id, status, response_date=None):
    """Update application status when you get a response"""
    conn = sqlite3.connect('data/applications.db')
    c = conn.cursor()
    c.execute('''
        UPDATE applications 
        SET status = ?, response_date = ?
        WHERE application_id = ?
    ''', (status, response_date, application_id))
    conn.commit()
    conn.close()

def get_all_applications():
    """Retrieve all applications as a dataframe"""
    import pandas as pd
    conn = sqlite3.connect('data/applications.db')
    df = pd.read_sql_query("SELECT * FROM applications", conn)
    conn.close()
    return df