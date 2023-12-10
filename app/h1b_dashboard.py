import streamlit as st
from dashboard import load_data

def h1b_job_insights():
    st.subheader("H1B Job Insights")

    # Using columns to organize filters
    col1, col2 = st.columns(2)  # First row of columns
    col3, col4 = st.columns(2)  # Second row of columns
    col5, col6 = st.columns(2)  # Third row of columns

    with col1:
        employer = st.text_input("Search by Employer")
    with col2:
        job_title = st.text_input("Search by Job Title")
    with col3:
        min_salary = st.number_input("Minimum Salary", value=0, step=10000)
    with col4:
        max_salary = st.number_input("Maximum Salary", value=0, step=10000)
    with col5:
        location = st.text_input("Search by Location")
    with col6:
        year = st.selectbox("Select Year", options=["", "2020", "2021", "2022"], index=0)

    # Query building logic
    query = "SELECT * FROM h1b_jobs WHERE 1=1"
    params = []
    if employer:
        query += " AND EMPLOYER LIKE ?"
        params.append(f'%{employer}%')
    if job_title:
        query += " AND `JOB TITLE` LIKE ?"
        params.append(f'%{job_title}%')
    if min_salary > 0:
        query += " AND `BASE SALARY` >= ?"
        params.append(min_salary)
    if max_salary > 0:
        query += " AND `BASE SALARY` <= ?"
        params.append(max_salary)
    if location:
        query += " AND LOCATION LIKE ?"
        params.append(f'%{location}%')
    if year:
        query += " AND Year = ?"
        params.append(year)

    results = load_data(query, params)

    st.dataframe(results, width=700, height=300)

# h1b_job_insights()
