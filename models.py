import sqlite3

# Initialize the SQLite database
conn = sqlite3.connect('bug_database.db')
cursor = conn.cursor()

# Create a table for bug reports
cursor.execute('''
    CREATE TABLE IF NOT EXISTS bugs (
        id INTEGER PRIMARY KEY,
        description TEXT
    )
''')
conn.commit()
conn.close()
