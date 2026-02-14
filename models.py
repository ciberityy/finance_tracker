from datetime import datetime


class Transaction:
    def __init__(self, amount, category, subcategory, date=None):
        self.amount = amount
        self.category = category
        self.subcategory = subcategory
        self.date = date or datetime.now()

    def __repr__(self) -> str:
        return (f"Transaction details :\nAmount : {self.amount}\nCategory : {self.category}\nSubcategory : {self.subcategory}\nDate : {self.date}")

    def to_dict(self):
        return {
            "amount": self.amount,
            "category": self.category,
            "subcategory": self.subcategory,
            "date": self.date
        }


class TransactionManager:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction):
        """append a transaction into the list of transactions"""
        self.transactions.append(transaction)

    def get_category_total(self, category):
        """calculate total for a specific category"""
        return sum(t.amount for t in self.transactions if t.category == category
                   )

    def get_subcategory_total(self, category, subcategory):
        return sum(t.amount for t in self.transactions if t.category == category and t.subcategory == subcategory)

    def get_total(self):
        """get the total of all the transactions"""
        return sum([t.amount for t in self.transactions])

    def get_all(self):
        """returns all transactions"""
        return self.transactions
