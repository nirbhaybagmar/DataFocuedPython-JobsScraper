import sqlite3

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

    # Create 'current_jobs' table
    # Note: The original statement for 'current_jobs' table creation is incomplete.
    # Assuming additional fields are required, such as 'location' and 'date_posted'.
    # Adjust these fields as per your requirements.
    cursor.execute('''
        CREATE TABLE current_jobs (
            employer TEXT, 
            job_title TEXT,
            location TEXT,
            date_posted TEXT
        )
    ''')

    # Commit changes and close the connection
    conn.commit()
    conn.close()


db_name = 'jobs.db'
setup_database(db_name)
