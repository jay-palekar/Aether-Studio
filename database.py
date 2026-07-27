import sqlite3

connection = sqlite3.connect("aether.db")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS messages(
               
id INTEGER PRIMARY KEY AUTOINCREMENT,
               
name TEXT,
               
email TEXT,
               
message TEXT

)
""")

connection.commit()

connection.close()