import sqlite3

conn = sqlite3.connect("database/database.db")
c = conn.cursor()

print("=== TRANSACTIONS TABLE ===")
c.execute("SELECT id, category, subcategory, amount, category_id FROM Transactions LIMIT 20;")
for row in c.fetchall():
    print(row)

print("\n=== CATEGORIES TABLE ===")
c.execute("SELECT id, name, parent_id FROM categories;")
for row in c.fetchall():
    print(row)

conn.close()