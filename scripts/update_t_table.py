import sqlite3

conn = sqlite3.connect("database.db")

c = conn.cursor()

c.execute("""UPDATE Transactions
          SET category_id = (
          SELECT id FROM categories 
          WHERE name = Transactions.subcategory
          AND parent_id = (
          SELECT id from categories 
          WHERE name = Transactions.category
          )
        )
""")

conn.commit()

print(f"Updated : {conn.total_changes} rows")

conn.close()
