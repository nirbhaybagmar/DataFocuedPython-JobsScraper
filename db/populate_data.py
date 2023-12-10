import sqlite3
import pandas as pd
from constants import H1B_SCRAPED, PROCESSED_AGGREGATED_DATA


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
    db_name = 'db/jobs.db'
    h1b_data = pd.read_csv(H1B_SCRAPED)
    current_jobs_data = pd.read_csv(PROCESSED_AGGREGATED_DATA)
    try:
        table = 'h1b_jobs'
        print(f"Populating database: {db_name} with table: {table}")
        populate_database(db_name, table, h1b_data)
        print("Database populated successfully for h1b data")
    except Exception as e:
        print(f"Error populating database: {e}")

    try:
        table = 'current_jobs'
        print(f"Populating database: {db_name} with table: {table}")
        populate_database(db_name, table, current_jobs_data)
        print("Database populated successfully for current jobs data")
    except Exception as e:
        print(f"Error populating database: {e}")
