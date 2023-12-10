import sqlite3

def query_db(query, args=(), one=False):
    """Query the database and return a list of dictionaries."""
    conn = sqlite3.connect('jobs.db')
    cursor = conn.cursor()
    cursor.execute(query, args)
    rv = cursor.fetchall()
    conn.close()
    return (rv[0] if rv else None) if one else rv

def query_h1b_jobs(job_title):
    """Query the database for jobs with the specified job title."""
    return query_db("SELECT * FROM h1b_jobs WHERE `JOB TITLE` LIKE ? LIMIT 50", ('%' + job_title + '%',))

def query_current_jobs(job_title):
    """Query the database for jobs with the specified job title."""
    return query_db("SELECT * FROM current_jobs WHERE `Job-Title` LIKE ? LIMIT 500", ('%' + job_title + '%',))

conn = sqlite3.connect('db/jobs.db')
cursor = conn.cursor()

# cursor.execute("SELECT COUNT(*) from current_jobs;")
# rv = cursor.fetchall()
# print(rv)

# print(query_h1b_jobs('Software'))
# print(query_current_jobs('Software'))

# print the  schema of the table
cursor.execute("PRAGMA table_info(h1b_jobs)")
print(cursor.fetchall())

# print the  schema of the table
cursor.execute("PRAGMA table_info(current_jobs)")
print(cursor.fetchall())
