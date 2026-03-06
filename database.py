import sqlite3


class Database:
    def __init__(self, db_path):
        self.db_path = db_path

        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()

        c.execute("""
CREATE TABLE IF NOT EXISTS Transactions(
        id INTEGER PRIMARY KEY AUTOINCREMENT
        category TEXT,
        subcategory TEXT,
          amount INTEGER,
          date TEXT,
          )
""")
        conn.commit()
        conn.close()

    def save_transaction(self, transaction):

        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()

        query = "INSERT INTO Transactions (category, subcategory, amount, date) VALUES (?, ?, ?, ?)"
        values = (transaction.category,
                  transaction.subcategory,
                  transaction.amount,
                  transaction.date)

        c.execute(query, values)

        conn.commit()
        conn.close()
