import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from dashboard import load_data

def analytics_tab():
    st.subheader("Data Analytics")

    # Fetch data from both tables
    h1b_data = load_data("SELECT * FROM h1b_jobs")
    current_jobs_data = load_data("SELECT * FROM current_jobs")

    # H1B Data Analysis
    if not h1b_data.empty:
        st.subheader("H1B Jobs Salary Distribution")
        plt.figure(figsize=(10, 6))
        sns.histplot(h1b_data['BASE SALARY'], kde=True)
        plt.xlabel("Base Salary")
        plt.ylabel("Frequency")
        st.pyplot(plt)

        # 2. Top Employers in H1B Jobs
        st.subheader("Top Employers in H1B Jobs")
        top_employers = h1b_data['EMPLOYER'].value_counts().head(10)
        plt.figure(figsize=(10, 6))
        sns.barplot(x=top_employers.values, y=top_employers.index)
        plt.xlabel("Number of Jobs")
        plt.ylabel("Employers")
        st.pyplot(plt)
    
        # 3. Job Distribution by Year
        st.subheader("Job Distribution by Year (H1B Jobs)")
        jobs_by_year = h1b_data['Year'].value_counts().sort_index()
        plt.figure(figsize=(10, 6))
        sns.lineplot(x=jobs_by_year.index, y=jobs_by_year.values)
        plt.xlabel("Year")
        plt.ylabel("Number of Jobs")
        st.pyplot(plt)

        # 4. Job Titles Pie Chart
        st.subheader("Job Titles Distribution (H1B Jobs)")
        top_titles = h1b_data['JOB TITLE'].value_counts().head(5)
        plt.figure(figsize=(8, 8))
        plt.pie(top_titles, labels=top_titles.index, autopct='%1.1f%%')
        plt.title("Top 5 Job Titles")
        st.pyplot(plt)

        # # 5. Average Salary by Location
        # st.subheader("Average Salary by Location (H1B Jobs)")
        # avg_salary_by_location = h1b_data.groupby('LOCATION')['BASE SALARY'].mean().sort_values(ascending=False).head(10)
        # plt.figure(figsize=(10, 6))
        # sns.barplot(x=avg_salary_by_location.values, y=avg_salary_by_location.index)
        # plt.xlabel("Average Salary")
        # plt.ylabel("Location")
        # st.pyplot(plt)

    # Current Jobs Data Analysis
    if not current_jobs_data.empty:
        # 6. Number of Jobs by Job Type
        st.subheader("Number of Jobs by Job Type (Current Jobs)")
        job_type_count = current_jobs_data['Job-Type'].value_counts()
        plt.figure(figsize=(10, 6))
        sns.barplot(x=job_type_count.values, y=job_type_count.index)
        plt.xlabel("Number of Jobs")
        plt.ylabel("Job Types")
        st.pyplot(plt)

        # 7. Technology Frequency
        # Assuming 'Tech' field contains comma-separated values
        tech_series = current_jobs_data['Tech'].dropna().str.split(',').explode()
        tech_count = tech_series.value_counts().head(10)
        st.subheader("Technology Frequency (Current Jobs)")
        plt.figure(figsize=(10, 6))
        sns.barplot(x=tech_count.values, y=tech_count.index)
        plt.xlabel("Frequency")
        plt.ylabel("Technology")
        st.pyplot(plt)

        # 8. Salary Range Distribution
        # # Assuming 'Salary' contains ranges like '50000-70000'
        # # This is a simplistic approach and might need adjustment based on actual data format
        # salary_ranges = current_jobs_data['Salary'].dropna().str.split('-', expand=True).astype(float)
        # salary_ranges.columns = ['Min Salary', 'Max Salary']
        # st.subheader("Salary Range Distribution (Current Jobs)")
        # plt.figure(figsize=(10, 6))
        # sns.histplot(salary_ranges['Min Salary'], kde=True, color='blue', label='Min Salary')
        # sns.histplot(salary_ranges['Max Salary'], kde=True, color='orange', label='Max Salary')
        # plt.xlabel("Salary")
        # plt.ylabel("Frequency")
        # plt.legend()
        # st.pyplot(plt)

        # 9. Company-wise Job Distribution
        st.subheader("Company-wise Job Distribution (Current Jobs)")
        company_job_dist = current_jobs_data['Company'].value_counts().head(10)
        plt.figure(figsize=(10, 6))
        sns.barplot(x=company_job_dist.values, y=company_job_dist.index)
        plt.xlabel("Number of Jobs")
        plt.ylabel("Company")
        st.pyplot(plt)

        # 10. Location-based Job Distribution
        st.subheader("Location-based Job Distribution (Current Jobs)")
        location_job_dist = current_jobs_data['Location'].value_counts().head(10)
        plt.figure(figsize=(10, 6))
        sns.barplot(x=location_job_dist.values, y=location_job_dist.index)
        plt.xlabel("Number of Jobs")
        plt.ylabel("Location")
        st.pyplot(plt)
