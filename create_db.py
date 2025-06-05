import sqlite3

# Connect (this will create the DB file)
conn = sqlite3.connect("sales_data.db")
cursor = conn.cursor()

# Create table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS sales (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product TEXT,
        quantity INTEGER,
        price REAL
    )
''')

# Sample data
sample_data = [
    ('Laptop', 5, 800),
    ('Mouse', 20, 20),
    ('Keyboard', 10, 30),
    ('Monitor', 3, 200),
    ('Mouse', 15, 20),
    ('Laptop', 2, 800),
    ('Keyboard', 5, 30)
]

# Insert data
cursor.executemany("INSERT INTO sales (product, quantity, price) VALUES (?, ?, ?)", sample_data)

# Commit and close
conn.commit()
conn.close()

print("Database created and data inserted successfully.")
