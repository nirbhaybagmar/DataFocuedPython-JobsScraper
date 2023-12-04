import streamlit as st
import pandas as pd
import sqlite3
import os
import re

# Function to connect to your SQLite database
def load_data(query, params=()):
    # Adjust the database path
    db_path = os.path.join(os.path.dirname(__file__), '..', 'Db', 'jobs.db')
    conn = sqlite3.connect(db_path)
    return pd.read_sql_query(query, conn, params=params)

def extract_salary_range(salary_str):
    """ Extracts numeric salary range from the salary string. """
    numbers = re.findall(r'\d+', salary_str.replace(',', ''))
    return list(map(int, numbers))

def main():
    st.title('Job Insights Dashboard')
    tab1, tab2, tab3 = st.tabs(["Main Dashboard", "H1B Job Insights", "Analytics"])

    with tab1:
        from current_jobs_dashboard import main_dashboard
        main_dashboard()

    with tab2:
        from h1b_dashboard import h1b_job_insights
        h1b_job_insights()

    with tab3:
        from analytics_dashboard import analytics_tab
        analytics_tab()
if __name__ == '__main__':
    main()
