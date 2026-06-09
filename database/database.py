import sqlite3

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
        category_id INTEGER
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

        category_id = self.get_category_id(transaction.category, transaction.subcategory)
        
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()

        query = "INSERT INTO Transactions (category_id, amount, date) VALUES (?, ?, ?)"
        values = (category_id,
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

        return

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

        return

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
        

    def get_category_id(self, category_name, subcategory_name):
        """
        Gets the id of each transaction by matching the category name and subcategory name to their correct id in the categories table
        
        Returns:
            integer: which will be the category_id 
        """
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        
        query = "SELECT id FROM categories WHERE name = ? AND parent_id = (" \
        "SELECT id FROM categories WHERE name = ?)"
        values = (subcategory_name, category_name) 
        
        c.execute(query, values)
        row = c.fetchone()
        
        conn.close()
        if row is None:
            raise ValueError(f"Category pair not found: '{category_name}' / '{subcategory_name}'")
        
        return row[0]


    def get_category_total(self, category):
        
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()

        query = "SELECT SUM(amount) \
        FROM Transactions \
        WHERE category_id IN ( \
            SELECT id from categories \
            WHERE parent_id = (SELECT id FROM categories WHERE name = ?) \
            );"
        values = (category,)

        c.execute(query, values)
        category_total = c.fetchone()

        conn.close()

        if category_total is None or category_total[0] is None:
            return 0 
        
        return category_total[0]
            
    
    def get_subcategory_total(self, subcategory_name, category_name):

        
        subcategory_id = self.get_category_id(subcategory_name, category_name)

        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()

        query = "SELECT SUM(amount) FROM Transactions WHERE category_id = ?"
        values =(subcategory_id,)

        c.execute(query, values)
        subcategory_total = c.fetchone()

        conn.close

        if subcategory_total is None or subcategory_total[0] is None:
            return 0 
        
        return subcategory_total[0]
    
    def get_category_tree(self):
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()

        query = "SELECT id, name FROM categories WHERE parent_id IS NULL"
        
        c.execute(query,)

        categories = c.fetchall()

        categories_dict = {}

        for category in categories:
            query = "SELECT name FROM categories WHERE parent_id = (?)"
            values = (category[0],)
            
            c.execute(query, values)

            subcategories_list_of_tuples = c.fetchall()

            subcategories_list = [name for (name,) in subcategories_list_of_tuples]

            categories_dict[category[1]] = subcategories_list

        conn.close()

        if not categories_dict:
            return None 
        
        return categories_dict
    
    def get_total_expenses(self):
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()            
        c.execute("SELECT SUM(amount) FROM Transactions")
        total = c.fetchone()[0]
        conn.close()
        
        return total if total is not None else 0
    
    def get_all_transactions(self):
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()

        query = "SELECT \
        Transactions.id, \
        parent.name, \
        sub.name, \
        Transactions.amount, \
        Transactions.date \
        FROM Transactions \
        JOIN categories AS sub ON category_id = sub.id \
        JOIN categories AS parent ON sub.parent_id = parent.id;"

        c.execute(query)

        raw_transactions = c.fetchall()

        return raw_transactions

           
    

