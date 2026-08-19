import sqlite3
import os
import pandas as pd

# Always point to cricbuzz.db relative to the project root directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_FILE = os.path.join(BASE_DIR, "cricbuzz.db")

def get_connection():
    """Returns a connection object to SQLite database."""
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn

def execute_query(query, params=()):
    """Executes SELECT queries and returns result as a Pandas DataFrame."""
    conn = get_connection()
    try:
        df = pd.read_sql_query(query, conn, params=params)
        return df
    finally:
        conn.close()

def execute_commit(query, params=()):
    """Executes INSERT, UPDATE, DELETE queries."""
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(query, params)
        conn.commit()
        return cursor.lastrowid
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        conn.close()