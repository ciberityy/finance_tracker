from src.transactions_cli import handle_user_choice
from models import TransactionManager
from src.constants import MAIN_MENU, TRANSACTIONS_MENU


def main():
    """
    Main function to run the Personal Finance Tracker CLI application.
    Initializes the TransactionManager, defines categories, and enters the main application loop.
    """
    manager = TransactionManager()

    CATEGORIES = {
        "Food": ["Sandwich", "Coffee", "Water"],
        "Transport": ["Bus", "Taxi", "Vtc"],
        "Chill_day": ["Dinner", "Beach_day", "Gaming"]
    }

    while True:

        user_input = handle_user_choice(
            CATEGORIES, manager, manager.balance, manager.income)


if __name__ == "__main__":
    main()
