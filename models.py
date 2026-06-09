from datetime import datetime

from user_io import get_user_balance, get_user_income
from database.database import Database

class Transaction:
    """
    Represents a single financial transaction with an amount, category, subcategory, date, and an optional ID.
    """
    def __init__(self, amount, category, subcategory, date=None, id=None):
        self.amount = amount
        self.category = category
        self.subcategory = subcategory
        self.date = date or datetime.now()
        self.id = id

    def __repr__(self) -> str:
        """
        Returns a string representation of the Transaction object.
        """
        return (f"Transaction details :\nAmount : {self.amount}\nCategory : {self.category}\nSubcategory : {self.subcategory}\nDate : {self.date}")

    def to_dict(self):
        """
        Converts the Transaction object to a dictionary.

        Returns:
            dict: A dictionary representation of the transaction.
        """
        return {
            "amount": self.amount,
            "category": self.category,
            "subcategory": self.subcategory,
            "date": self.date,
            "id": self.id
        }


class TransactionManager:
    """
    Manages a collection of Transaction objects, handling their addition, deletion, and retrieval.
    Interacts with the Database class for persistence and user_io for initial user data.
    """
    def __init__(self):
        """
        Initializes the TransactionManager, loads existing transactions and user data from the database.
        If no user data exists, it prompts the user for income and balance.
        """
        self.db = Database("database/database.db")

        user_settings = self.db.load_user_data()

        if not user_settings:
            self.balance = get_user_balance()
            self.income = get_user_income()

        else:
            self.income = user_settings[1]
            self.balance = user_settings[2]

        self.db.save_user_data(self.income, self.balance)

    def add_transaction(self, transaction):
        """
        Adds a new transaction to the manager's list and saves it to the database.

        Args:
            transaction (Transaction): The Transaction object to add.
        """
        self.db.save_transaction(transaction)

    def delete_transaction(self, transaction):
        """
        Removes a transaction from the manager's list and deletes it from the database.

        Args:
            transaction (Transaction): The Transaction object to delete.
        """
        self.db.delete_transaction(transaction.id)

    def get_category_total(self, category):
        """Return total spending for a top-level category (including all subcategories)"""
        
        return self.db.get_category_total(category)

    def get_subcategory_total(self, category_name, subcategory_name):
        """
        Calculates the total amount spent for a specific subcategory within a category.

        Args:
            category (str): The name of the category.
            subcategory (str): The name of the subcategory.

        Returns:
            int: The total amount spent in the specified subcategory.s
        """
        return self.db.get_subcategory_total(category_name, subcategory_name)

    def get_total(self):
        """
        Calculates the grand total of all transactions.

        Returns:
            int: The sum of amounts of all transactions.
        """
        return self.db.get_total_expenses()

    def get_all(self):
        """
        Returns all transactions currently managed.

        Returns:
            list: A list of all Transaction objects.
        """
        raw_transactions = self.db.get_all_transactions()

        transactions_list = [Transaction(amount=t[3],category=t[1], subcategory=t[2], date=t[4], id=t[0]) for t in raw_transactions]

        return transactions_list 

    def save_user_info(self, income, balance):
        """
        Saves the user's income and balance to the database.

        Args:
            income (int): The user's income.
            balance (int): The user's balance.
        """
        self.db.save_user_data(income, balance)
