import sqlite3

conn = sqlite3.connect("database.db")
table_name = 'categories'


c = conn.cursor()

c.execute("SELECT * FROM pragma_table_info(?)", (table_name,))

columns = c.fetchall()

print(columns)

conn.close()