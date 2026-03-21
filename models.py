from datetime import datetime

from database import Database
from user_io import get_user_balance, get_user_income


class Transaction:
    def __init__(self, amount, category, subcategory, date=None, id=None):
        self.amount = amount
        self.category = category
        self.subcategory = subcategory
        self.date = date or datetime.now()
        self.id = id

    def __repr__(self) -> str:
        return (f"Transaction details :\nAmount : {self.amount}\nCategory : {self.category}\nSubcategory : {self.subcategory}\nDate : {self.date}")

    def to_dict(self):
        return {
            "amount": self.amount,
            "category": self.category,
            "subcategory": self.subcategory,
            "date": self.date,
            "id": self.id
        }


class TransactionManager:

    def __init__(self):
        """intitate an empty transactions list"""

        self.db = Database("database.db")

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
        """append a transaction into the list of transactions and save it into the db"""

        self.transactions.append(transaction)

        self.db.save_transaction(transaction)

    def delete_transaction(self, transaction):
        """remove a transaction from the list of transactions and delete it from the db"""

        self.transactions.remove(transaction)

        self.db.delete_transaction(transaction.id)

    def get_category_total(self, category):
        """calculate total for a specific category"""
        return sum(t.amount for t in self.transactions if t.category == category)

    def get_subcategory_total(self, category, subcategory):
        """get the total of all the transactions matching the category and subcategory args"""
        return sum(t.amount for t in self.transactions if t.category == category and t.subcategory == subcategory)

    def get_total(self):
        """get the total of all the transactions"""
        return sum([t.amount for t in self.transactions])

    def get_all(self):
        """returns all transactions"""
        return self.transactions

    def save_user_info(self, income, balance):
        """saves the users related info"""

        self.db.save_user_data(income, balance)
