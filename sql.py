import sqlite3

# Connect to a database (or create a new one if it doesn't exist)
conn = sqlite3.connect('example.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create a table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        email TEXT NOT NULL
    )
''')

# Insert data into the table
cursor.execute("INSERT INTO users (username, email) VALUES (?, ?)", ('brad_jones', 'bjones@gmail.com'))
cursor.execute("INSERT INTO users (username, email) VALUES (?, ?)", ('cynthia_james', 'cjames1@yahoo.com'))
cursor.execute("INSERT INTO users (username, email) VALUES (?, ?)", ('lindsy_boykins', 'lindboykins@gmail.com'))
cursor.execute("INSERT INTO users (username, email) VALUES (?, ?)", ('ryan_clark', 'ryanc@outlook.com'))

# Commit the changes
conn.commit()

# Retrieve and print data from the table
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

print("Users:")
for row in rows:
    print(f"ID: {row[0]}, Username: {row[1]}, Email: {row[2]}")

# Close the connection
conn.close()
