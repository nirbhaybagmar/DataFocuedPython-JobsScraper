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

- **scrape/**: Web scraping modules for each job data source.
  - `glassdoor/`: Contains files for scraping Glassdoor.
    - `glassdoor.py`: The script used to scrape job data from Glassdoor.
    - `jobs.csv`: Scraped job listings from Glassdoor.
  - `h1b/`: Contains files for scraping H1B transfer data.
    - `h1b_data.csv`: Scraped H1B job listings.
    - `scrape.py`: General scraping script that can be adapted for various sources.
  - `linkedin/`: Contains files for scraping LinkedIn.
    - `data_processing.py`: Script for processing scraped LinkedIn job data.
    - `linkedin.py`: The script used to scrape job data from LinkedIn.
    - `LinkedinFinalScrapedData.csv`: The final scraped data from LinkedIn.
    - `linkedinjobsfinal.csv`: Processed LinkedIn job listings for the dashboard.

- **templates/**: HTML templates for the Flask app.

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

6. **Create the Database**:
Set up the database by running the `db.py` script inside the `db` directory:
```
python db/db.py
```

7. **Start the Application**:
Launch the dashboard using Streamlit:
```
streamlit run dashboard.py
```


## Usage

[Explanation on how to use the application, access different dashboards, and interpret the data.]

## Contributing

[Guidelines for how to contribute to the project, if applicable.]

## License

[Information about the project license.]
