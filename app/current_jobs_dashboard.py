import streamlit as st
import pandas as pd
from dashboard import load_data

def main_dashboard():
    st.subheader("Current Jobs Dashboard")

    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)
    col5, col6 = st.columns(2)
    col7 = st.columns(1)[0]
    col8 = st.columns(1)[0]

    with col1:
        company = st.text_input("Filter by Company", key='company_filter')
    with col2:
        job_title = st.text_input("Filter by Job Title", key='job_title_filter')
    with col3:
        min_salary = st.number_input("Minimum Salary", min_value=0, step=1000, key='min_salary_filter')
    with col4:
        max_salary = st.number_input("Maximum Salary", min_value=0, step=1000, key='max_salary_filter')
    with col5:
        location = st.text_input("Filter by Location", key='location_filter')
    with col6:
        job_type = st.text_input("Filter by Job Type", key='job_type_filter')
    with col7:
        tech_filter = st.text_input("Filter by Technologies (e.g., 'Python, Java')", key='tech_filter')
    with col8:
        h1b_sponsorship = st.checkbox("Filter by H1B Sponsorship", key='h1b_sponsorship_filter')

    # Query building logic for current jobs
    query = "SELECT * FROM current_jobs WHERE 1=1"
    params = []
    if company:
        query += " AND employer LIKE ?"
        params.append(f'%{company}%')
    if job_title:
        query += " AND `job_title` LIKE ?"
        params.append(f'%{job_title}%')
    if location:
        query += " AND location LIKE ?"
        params.append(f'%{location}%')
    if min_salary > 0:
        query += " AND min_salary >= ?"
        params.append(min_salary)
    if max_salary > 0:
        query += " AND max_salary <= ?"
        params.append(max_salary)
    if job_type:
        query += " AND `job_type` LIKE ?"
        params.append(f'%{job_type}%')
    if tech_filter:
        tech_list = [tech.strip() for tech in tech_filter.split(',')]
        tech_query = " OR ".join(["tech LIKE ?" for _ in tech_list])
        query += f" AND ({tech_query})"
        params.extend([f'%{tech}%' for tech in tech_list])

    results = load_data(query, params)

    def word_based_match(employer_name, company_list):
        """
        Check if any word in employer_name is a substring of any company in company_list.
        """
        if not employer_name:
            return False
        employer_words = employer_name.lower().split()
        for company in company_list:
            company_lower = company.lower()
            # Check if any word in employer_name is a substring of company
            if any(word in company_lower for word in employer_words):
                return True
        return False

    # If H1B sponsorship filter is checked, filter the results
    if h1b_sponsorship:
        h1b_companies = load_data("SELECT DISTINCT EMPLOYER FROM h1b_jobs", [])
        h1b_companies_list = [employer for employer in h1b_companies['EMPLOYER'].tolist() if employer]
        results = results[results['employer'].apply(lambda x: word_based_match(x, h1b_companies_list))]

    rename_dict = {
        'employer': 'Employer',
        'job_title': 'Job Title',
        'location': 'Location',
        'tech': 'Technology',
        'job_type': 'Job Type',
        'min_salary': 'Min Salary',
        'max_salary': 'Max Salary'
    }

    results.rename(columns=rename_dict, inplace=True)
    replace_values = [None, 'None', 'Null', 'NaN', 'Not Applicable']
    results.replace(replace_values, 'N/A', inplace=True)
    st.dataframe(results, width=1200, height=600)
