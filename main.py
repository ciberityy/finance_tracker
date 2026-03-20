from lib import MENU, handle_user_choice
from models import TransactionManager


def main():

    manager = TransactionManager()

    CATEGORIES = {
        "Food": ["Sandwich", "Coffee", "Water"],
        "Transport": ["Bus", "Taxi", "Vtc"],
        "Chill_day": ["Dinner", "Beach_day", "Gaming"]
    }

    while True:

        user_input = handle_user_choice(
            CATEGORIES, MENU, manager, manager.balance, manager.income)


if __name__ == "__main__":
    main()
