import json
from db_connection import get_db_connection

def extract_schema():
    conn = get_db_connection()
    cursor = conn.cursor()

    schema = {}
    cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_type = 'BASE TABLE'")
    tables = cursor.fetchall()

    for table in tables:
        table_name = table[0]
        cursor.execute(f"SELECT column_name, data_type FROM information_schema.columns WHERE table_name = '{table_name}'")
        columns = cursor.fetchall()
        schema[table_name] = {column[0]: column[1] for column in columns}

    conn.close()

    with open('schema.json', 'w', encoding='utf-8') as f:
        json.dump(schema, f, ensure_ascii=False, indent=4)

    return schema

"""
schema_extractor.py
-------------------
Extracts the schema of the Priority ERP database and saves it to a JSON file.

Functions:
- extract_schema(): Extracts table and column information from the database and writes it to 'schema.json'.
"""
