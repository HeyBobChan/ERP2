import pyodbc
import os

def get_db_connection():
    conn = pyodbc.connect(
        f'DRIVER={{ODBC Driver 17 for SQL Server}};'
        f'SERVER={os.getenv("PRIORITY_DB_HOST")};'
        f'DATABASE={os.getenv("PRIORITY_DB_NAME")};'
        f'UID={os.getenv("PRIORITY_DB_USERNAME")};'
        f'PWD={os.getenv("PRIORITY_DB_PASSWORD")}'
    )
    return conn

"""
db_connection.py
----------------
Establishes a connection to the Priority ERP database.

Functions:
- get_db_connection(): Connects to the Priority ERP database using connection details from environment variables.
"""
