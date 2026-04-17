class Database:
    """
    Handles all database interactions for transactions and user data using SQLite.
    """
    def __init__(self, db_path):
        """
        Initializes the Database connection and creates necessary tables if they don't exist.

        Args:
            db_path (str): The path to the SQLite database file.
        """
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
        """
        Deletes a transaction from the database based on its primary key (ID).

        Args:
            primary_key (int): The ID of the transaction to delete.
        """
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()

        query = "DELETE FROM Transactions WHERE id = (?)"
        values = (primary_key,)

        c.execute(query, values)

        conn.commit()
        conn.close()

    def load_transactions(self):
        """
        Loads all transactions from the database.

        Returns:
            list: A list of tuples, where each tuple represents a transaction record.
        """
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()

        query = 'SELECT * FROM Transactions'
        c.execute(query)

        transactions = c.fetchall()

        conn.close()
        return transactions

    def save_user_data(self, income, balance):
        """
        Saves or updates the user's income and balance in the database.
        It uses INSERT OR REPLACE to ensure only one user data entry exists.

        Args:
            income (int): The user's income.
            balance (int): The user's current balance.
        """
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()

        query = "INSERT OR REPLACE INTO User_data (id, income, balance) VALUES (?, ?, ?)"
        values = (1, income, balance)

        c.execute(query, values)

        conn.commit()
        conn.close()

    def load_user_data(self):
        """
        Loads the user's income and balance from the database.

        Returns:
            tuple or None: A tuple containing (id, income, balance) if data exists,
                           otherwise None.
        """
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()

        query = "SELECT * FROM User_data"
        c.execute(query)

        user_data = c.fetchone()

        conn.close()

        if not user_data:
            return None

        else:
            return user_data
