from src.transactions_cli import handle_user_choice
from models import TransactionManager
from src.constants import MAIN_MENU, TRANSACTIONS_MENU
from database.database import Database


def main():
    """
    Main function to run the Personal Finance Tracker CLI application.
    Initializes the TransactionManager, defines categories, and enters the main application loop.
    """
    manager = TransactionManager()

    CATEGORIES = manager.db.get_category_tree()

    while True:

        user_input = handle_user_choice(
            CATEGORIES, manager, manager.balance, manager.income)


if __name__ == "__main__":
    main()
