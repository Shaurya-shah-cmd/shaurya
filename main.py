import sqlite3
conn = sqlite3.connect("db1.db")
conn.execute("""
create table usersi(
usid INTEGER PRIMARY KEY AUTOINCREMENT,
user VARCHAR(100),
pass VARCHAR(20),
mobile VARCHAR(200),
email VARCHAR(2) 
)""")

