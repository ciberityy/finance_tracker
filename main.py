from lib import MENU
from lib import get_user_income, get_user_current_balance, handle_expense_category, handle_user_choice
from models import TransactionManager


def main():

    manager = TransactionManager()

    current_balance = get_user_current_balance()
    user_income = get_user_income()

    CATEGORIES = {
        "Food": ["Sandwich", "Coffee", "Water"],
        "Transport": ["Bus", "Taxi", "Vtc"],
        "Chill_day": ["Dinner", "Beach_day", "Gaming"]
    }

    while True:

        user_input = handle_user_choice(
            CATEGORIES, MENU, manager, current_balance, user_income)


if __name__ == "__main__":
    main()
