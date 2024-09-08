import sqlite3 

conn = sqlite3.connect("portfoliodata.db")

print("Opened database successfully")

conn.execute("CREATE TABLE IF NOT EXISTS student (name TEXT, email TEXT, subject TEXT ,message  TEXT)")

print("Table has been created")

conn.close()
