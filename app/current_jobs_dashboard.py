import streamlit as st
import pandas as pd
from dashboard import load_data, extract_salary_range


def main_dashboard():
    st.subheader("Main Dashboard - Current Jobs")

    # Filters for Main Dashboard
    company = st.text_input("Filter by Company")
    job_title = st.text_input("Filter by Job Title")
    job_type = st.text_input("Filter by Job Type")
    location = st.text_input("Filter by Location")
    salary_range = st.text_input("Filter by Salary Range (e.g., '50000-70000')")
    tech_filter = st.text_input("Filter by Technologies (comma-separated, e.g., 'Python, Java')")

    # Query building logic for current jobs
    query = "SELECT * FROM current_jobs WHERE 1=1"
    params = []
    if company:
        query += " AND Company LIKE ?"
        params.append(f'%{company}%')
    if job_title:
        query += " AND `Job-Title` LIKE ?"
        params.append(f'%{job_title}%')
    if job_type:
        query += " AND `Job-Type` LIKE ?"
        params.append(f'%{job_type}%')
    if location:
        query += " AND Location LIKE ?"
        params.append(f'%{location}%')
    if salary_range:
        salary_bounds = extract_salary_range(salary_range)
        if len(salary_bounds) == 2:
            query += " AND (CAST(SUBSTR(Salary, 1, INSTR(Salary, '-') - 1) AS INTEGER) BETWEEN ? AND ?)"
            params.extend(salary_bounds)
    if tech_filter:
        tech_list = [tech.strip() for tech in tech_filter.split(',')]
        tech_query = " OR ".join(["Tech LIKE ?" for _ in tech_list])
        query += f" AND ({tech_query})"
        params.extend([f'%{tech}%' for tech in tech_list])

    results = load_data(query, params)
    st.dataframe(results, width=700, height=300)
