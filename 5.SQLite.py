# Practical 5: Python SQL Database Access
import sqlite3

# Connect to SQLite database (creates 'students.db' if it doesn't exist)
conn = sqlite3.connect('students.db')
cursor = conn.cursor()
print("Connected to SQLite database")

# Create Students table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Students (
        ID INTEGER PRIMARY KEY,
        Name TEXT NOT NULL,
        Marks REAL
    )
''')
print("Students table created")

# Insert 5 records
students_data = [
    (1, "Alice", 85.5),
    (2, "Bob", 90.0),
    (3, "Charlie", 78.5),
    (4, "Diana", 92.0),
    (5, "Eve", 88.5)
]

cursor.executemany('INSERT OR REPLACE INTO Students (ID, Name, Marks) VALUES (?, ?, ?)', students_data)
conn.commit()
print("Inserted 5 student records")

# Retrieve and display all records
cursor.execute('SELECT * FROM Students')
records = cursor.fetchall()
print("\nStudent Records:")
for record in records:
    print(f"ID: {record[0]}, Name: {record[1]}, Marks: {record[2]}")

# Close connection
conn.close()
print("\nDatabase connection closed")