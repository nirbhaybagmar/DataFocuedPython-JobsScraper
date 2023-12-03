import streamlit as st
import pandas as pd
import sqlite3

# Function to connect to your SQLite database
def load_data(query, params=()):
    conn = sqlite3.connect('h1b_data.db')
    return pd.read_sql_query(query, conn, params=params)

def main():
    st.title('H1B Job Insights')

    st.sidebar.subheader("Search and Filter Options")
    search_query = st.sidebar.text_input("Search by Job Title, Employer")
    search_location = st.sidebar.text_input("Search by Location")
    min_salary = st.sidebar.number_input("Minimum Salary", value=0, step=1000)
    max_salary = st.sidebar.number_input("Maximum Salary", value=0, step=1000)
    year = st.sidebar.selectbox("Select Year", options=["", "2020", "2021", "2022"], index=0)

    # Search and filter logic
    query = "SELECT * FROM h1b_jobs WHERE 1=1"
    params = []
    if search_query:
        query += " AND (`JOB TITLE` LIKE ? OR EMPLOYER LIKE ?)"
        params.extend([f'%{search_query}%', f'%{search_query}%'])
    if search_location:
        query += " AND LOCATION LIKE ?"
        params.append(f'%{search_location}%')
    if min_salary > 0:
        query += " AND `BASE SALARY` >= ?"
        params.append(min_salary)
    if max_salary > 0:
        query += " AND `BASE SALARY` <= ?"
        params.append(max_salary)
    if year:
        query += " AND YEAR = ?"
        params.append(year)

    results = load_data(query, params)
    st.subheader('Search Results')
    st.write(results)

    # Salary Insights
    st.subheader('Salary Insights')
    if st.button("Show Salary Insights"):
        salary_data = load_data("SELECT `JOB TITLE`, AVG(`BASE SALARY`) as AvgSalary FROM h1b_jobs GROUP BY `JOB TITLE`")
        st.write(salary_data)

    # Footer
    st.write('H1B Job Insights Web Application')

if __name__ == '__main__':
    main()
