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

        raw_transactions = self.db.load_transactions()

        self.transactions = [Transaction(
            t[3], t[1], t[2], t[4], t[0]) for t in raw_transactions]

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
        self.transactions.append(transaction)

        self.db.save_transaction(transaction)

    def delete_transaction(self, transaction):
        """
        Removes a transaction from the manager's list and deletes it from the database.

        Args:
            transaction (Transaction): The Transaction object to delete.
        """
        self.transactions.remove(transaction)

        self.db.delete_transaction(transaction.id)

    def get_category_total(self, category):
        """
        Calculates the total amount spent for a specific category.

        Args:
            category (str): The name of the category.

        Returns:
            int: The total amount spent in the specified category.
        """
        return sum(t.amount for t in self.transactions if t.category == category)

    def get_subcategory_total(self, category, subcategory):
        """
        Calculates the total amount spent for a specific subcategory within a category.

        Args:
            category (str): The name of the category.
            subcategory (str): The name of the subcategory.

        Returns:
            int: The total amount spent in the specified subcategory.
        """
        return sum(t.amount for t in self.transactions if t.category == category and t.subcategory == subcategory)

    def get_total(self):
        """
        Calculates the grand total of all transactions.

        Returns:
            int: The sum of amounts of all transactions.
        """
        return sum([t.amount for t in self.transactions])

    def get_all(self):
        """
        Returns all transactions currently managed.

        Returns:
            list: A list of all Transaction objects.
        """
        return self.transactions

    def save_user_info(self, income, balance):
        """
        Saves the user's income and balance to the database.

        Args:
            income (int): The user's income.
            balance (int): The user's balance.
        """
        self.db.save_user_data(income, balance)
