from database import Database
from models import Transaction

db = Database("test_expenses.db")

transaction = Transaction(500, "Food", "Sandwich", date=None)

db.save_transaction(transaction)

print("Saved successfuly !")
print(f"check if test_database.py was created")
