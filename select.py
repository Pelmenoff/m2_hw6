import sys
import sqlite3
import os

# Check for the presence of a command-line argument
if len(sys.argv) != 2:
    print("Usage: python select.py <query_number>")
    sys.exit(1)

# Read the query number from the command-line argument
query_number = int(sys.argv[1])

# Form the path to the SQL query file
query_file_path = os.path.join('select', f'query_{query_number}.sql')

try:
    # Open the SQL query file
    with open(query_file_path, 'r') as file:
        sql_query = file.read()

    # Connect to the database
    conn = sqlite3.connect('m2_hw6.db')
    cursor = conn.cursor()

    # Execute the SQL query
    cursor.execute(sql_query)

    # Display the query results
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close the database connection
    conn.close()

except FileNotFoundError:
    print(f"Query file '{query_file_path}' not found.")
    sys.exit(1)
except sqlite3.Error as e:
    print("SQLite error:", e)
    sys.exit(1)
