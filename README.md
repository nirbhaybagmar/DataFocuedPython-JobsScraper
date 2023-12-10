# Job Data Aggregator and Dashboard

## Introduction

This project is designed to scrape job listings from LinkedIn, Glassdoor, and H1B transfer data, consolidating them into a single platform that provides an intuitive dashboard for job search and analysis. The purpose is to offer a comprehensive view of the job market, aiding job seekers and analysts in their quest for up-to-date job information.

## Folder Structure and File Descriptions

- **app/**: Contains the Flask application files for the dashboard.
  - `analytics_dashboard.py`: Renders the analytics dashboard view with aggregated job data insights.
  - `app.py`: The main Flask application file that initializes the app and registers blueprints.
  - `current_jobs_dashboard.py`: Provides current job listings from various sources in a dashboard view.
  - `dashboard.py`: A module that sets up the general layout and elements of the dashboard.
  - `h1b_dashboard.py`: Displays a dashboard specific to H1B visa-related job data.

- **data_processing/**: Scripts and data files related to data processing.
  - `aggregated_data.csv`: A CSV file containing the combined job data from all sources.
  - `data_aggregation.py`: Script for aggregating job data into a single CSV file.

- **db/**: Database scripts and files.
  - `db_query.py`: Contains functions to query the SQLite database.
  - `db.py`: Script to set up the SQLite database.
  - `jobs.db`: SQLite database file containing job listings.
  - `populate_data.py`: Populate database with job data from CSV file.

- **scrape/**: Web scraping modules for each job data source.
  - `glassdoor/`: Contains files for scraping Glassdoor.
    - `scrape_glassdoor.py`: The script used to scrape job data from Glassdoor.
    - `jobs.csv`: Scraped job listings from Glassdoor.
  - `h1b/`: Contains files for scraping H1B transfer data.
    - `h1b_data.csv`: Scraped H1B job listings.
    - `scrape_h1b.py`: General scraping script that can be adapted for various sources.
  - `linkedin/`: Contains files for scraping LinkedIn.
    - `data_processing.py`: Script for processing scraped LinkedIn job data.
    - `scrape_linkedin.py`: The script used to scrape job data from LinkedIn.
    - `LinkedinFinalScrapedData.csv`: The final scraped data from LinkedIn.
    - `linkedinjobsfinal.csv`: Processed LinkedIn job listings for the dashboard.

- **venv/**: Virtual environment for project dependencies.

- `.gitignore`: Specifies intentionally untracked files to ignore.

- `README.md`: The file you are currently reading.

- `requirements.txt`: A list of Python package dependencies.

## Setup and Installation

To get the Job Data Aggregator and Dashboard up and running on your local machine, follow these steps:

1. **Install virtualenv**:
   If you do not have `virtualenv` installed, you can install it using pip: 
   ```
   pip install virtualenv
   ```

2. **Create a Virtual Environment**:
    To create a new virtual environment named `venv`, run the following command in the root of the project directory:
    ```
    virtualenv venv
    ```


3. **Activate the Virtual Environment**:
Activate the virtual environment by running the following command:
- On macOS and Linux:
  ```
  source venv/bin/activate
  ```
- On Windows:
  ```
  .\venv\Scripts\activate
  ```

4. **Install Requirements**:
    Install the required Python packages specified in `requirements.txt`:
    ```
    pip install -r requirements.txt
    ```

5. **Modify the Chromedriver Path**:
  Update the path to the Chromedriver in the scraping scripts to match the location of Chromedriver on your system.

      Create a new file `.env` in the root directory and add the following line:
      ```
      CHROMEDRIVER_PATH = "path/to/chromedriver"
      ```
      Make sure to replace `"path/to/chromedriver"` with the actual path to the Chromedriver executable on your system.
      Chromedriver can be downloaded from [here](https://sites.google.com/chromium.org/driver/).
      Chromedriver version should match the version of Chrome installed on your system.

      Issues with Chromedriver:
      - If you are using Windows, you may need to add the Chromedriver path to the system PATH variable.
      - If you are using macOS, you may need to grant permission to the Chromedriver executable using the following command:
        ```
        chmod +x /path/to/chromedriver
        ```
        ```
        xattr -d com.apple.quarantine /path/to/chromedriver
        ```

6. Command to run all the process in one command i.e scrape the data, clean the data, create database, populate database, run the application
    ```
    python run_commands.py
    ```

## To individually run the functionality follow the below steps
7. **To Scrape data**: This will sequntially run scraping for all the sources
    ```
    python scrape/scrape.py
    ```

8. **To process and clean data**: This will clean the data and aggregate data from multiple sources
    ```
    python data_processing/process_data.py
    ```

9. **Create the Database**:
    Set up the database by running the `db.py` script inside the `db` directory:
    ```
    python db/db.py
    ```

10. **Populate the Database**:
    Populate the database by running the `db.py` script inside the `db` directory:
    ```
    python db/populate_db.py
    ```

11. **Start the Application**:
    Launch the dashboard using Streamlit:
    ```
    streamlit run dashboard.py
    ```


## Usage

[Instructions on how to use the project or application.]

Dashboard contains 3 tabs:
1. **Current Jobs**: This tab contains the current job listings from various sources.
2. **H1B Data**: This tab contains the H1B visa-related job data.
3. **Analytics**: This tab provides insights and analytics on the aggregated job data.

Current Jobs tab contains the following filters:
- **Location**: Filter job listings by location.
- **Company**: Filter job listings by company.
- **Job Title**: Filter job listings by job title.
- **Experience Level**: Filter job listings by experience level.
- **Salary**: Filter job listings by salary range.
- **Technology**: Filter job listings by technology.

H1B Data tab contains the following filters:
- **Location**: Filter job listings by location.
- **Company**: Filter job listings by company.
- **Job Title**: Filter job listings by job title.
- **Base Salary**: Filter job listings by base salary range.

Analytics tab contains the following insights:
- **Job Count by Location**: A bar chart showing the number of job listings by location.
- **Job Count by Company**: A bar chart showing the number of job listings by company.
- **Job Count by Job Title**: A bar chart showing the number of job listings by job title.
- **Job Count by Experience Level**: A bar chart showing the number of job listings by experience level.
- **Job Count by Salary**: A bar chart showing the number of job listings by salary range.
- **Job Count by Technology**: A bar chart showing the number of job listings by technology.


## Authors
1. `Nirbhay Bagmar` (nbagmar)
2. `Dhruv Rakesh` (drakesh)
3. `Kovidh Pathak` (kpathak)
4. `Leher`
5. `Aishwarya`

