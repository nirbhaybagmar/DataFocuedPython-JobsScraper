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
            tech TEXT,
            job_type TEXT,
            min_salary TEXT,
            max_salary TEXT
        )
    ''')
    print("Database initialized and tables created.")

    # Commit changes and close the connection
    conn.commit()
    conn.close()



if __name__ == '__main__':
    db_name = 'db/jobs.db'
    try:
        print(f"Setting up database: {db_name}")
        setup_database(db_name)
        print("Database setup complete.")
    except Exception as e:
        print(f"Error setting up database: {e}")


