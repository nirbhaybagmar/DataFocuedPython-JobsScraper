import sqlite3
import pandas as pd


def setup_database(db_name):
    """
    Sets up a SQLite database with specified tables.

    Args:
        db_name (str): Name of the SQLite database file.
    """

    # Connect to SQLite database (it will be created if it doesn't exist)
    conn = sqlite3.connect(db_name)

    # Create a cursor object
    cursor = conn.cursor()

    # Create 'h1b_jobs' table
    cursor.execute('''
        CREATE TABLE h1b_jobs (
            employer TEXT,
            job_title TEXT,
            base_salary INTEGER,
            location TEXT,
            submit_date TEXT,
            start_date TEXT,
            year INTEGER
        )
    ''')

    cursor.execute('''
        CREATE TABLE current_jobs (
            employer TEXT,
            job_title TEXT,
            location TEXT,
            date_posted TEXT,
            job_type TEXT,
            salary TEXT,
            tech TEXT
        )
    ''')
    print("Database initialized and tables created.")

    # Commit changes and close the connection
    conn.commit()
    conn.close()


def populate_database(db_name, table, data):
    """
    Populates the SQLite database with the specified data.

    Args:
        db_name (str): Name of the SQLite database file.
        data (list): List of tuples containing data to be inserted into the database.
    """

    # Connect to SQLite database
    conn = sqlite3.connect(db_name)

    # Create a cursor object
    cursor = conn.cursor()

    # Insert data into 'h1b_jobs' table
    data.to_sql(table, conn, if_exists='replace', index=False)

    # Commit changes and close the connection
    conn.commit()
    conn.close()



if __name__ == '__main__':
    db_name = 'jobs.db'
    try:
        setup_database(db_name)
    except Exception as e:
        print(f"Error setting up database: {e}")

    # Read data from CSV file for H1B data
    print("Reading data from CSV file for H1B data...")
    data = pd.read_csv('scrape/h1b/h1b_data.csv')

    # read current jobs data
    print("Reading data from CSV file for current jobs data...")
    data2 = pd.read_csv('data_processing/aggregated_data.csv')

    # Populate 'h1b_jobs' table
    print("Populating 'h1b_jobs' table...")
    populate_database(db_name, 'h1b_jobs', data)

    # Populate 'current_jobs' table
    print("Populating 'current_jobs' table...")
    populate_database(db_name, 'current_jobs', data2)

