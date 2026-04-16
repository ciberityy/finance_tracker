import sqlite3


class Database:
    def __init__(self, db_path):
        self.db_path = db_path

        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()

        c.execute("""
CREATE TABLE IF NOT EXISTS Transactions(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        category TEXT,
        subcategory TEXT,
        amount INTEGER,
        date TEXT
        )
""")
        c.execute("""
CREATE TABLE IF NOT EXISTS User_data(
                  id INTEGER PRIMARY KEY, 
                  income INTEGER,
                  balance INTEGER
                  )
""")

        conn.commit()

        conn.close()

    def save_transaction(self, transaction):
        """
        Saves a new transaction to the database.

        Args:
            transaction (Transaction): The Transaction object to save.
        """
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

    def delete_transaction(self, primary_key):

        conn = sqlite3.connect(self.db_path)

        c = conn.cursor()

        query = "DELETE FROM Transactions WHERE id = (?)"
        values = (primary_key,)

        c.execute(query, values)

        conn.commit()

        conn.close()

    def load_transactions(self):

        conn = sqlite3.connect(self.db_path)

        c = conn.cursor()

        query = 'SELECT * FROM Transactions'

        c.execute(query)

        transactions = c.fetchall()

        conn.close()

        return transactions

    def save_user_data(self, income, balance):

        conn = sqlite3.connect(self.db_path)

        c = conn.cursor()

        query = "INSERT OR REPLACE INTO User_data (id, income, balance) VALUES (?, ?, ?)"
        values = (1, income, balance)

        c.execute(query, values)

        conn.commit()

        conn.close()

    def load_user_data(self):

        conn = sqlite3.connect(self.db_path)

        c = conn.cursor()

        query = "SELECT * FROM User_data"

        c.execute(query)

        user_data = c.fetchone()

        conn.close()

        if user_data:
            return user_data

        else:
            return None

