from constants import MENU
from tracker_lib import get_user_income_input, get_user_current_balance, handle_expense_category, generate_expense_dict, handle_user_choice
from models import TransactionManager


def main():
    manager = TransactionManager()

    current_balance = get_user_current_balance()
    user_income = get_user_income_input()

    CATEGORIES = {
        "Food": ["Sandwich", "Coffee", "Water"],
        "Transport": ["Bus", "Taxi", "Vtc"],
        "Chill_day": ["Dinner", "Beach_day", "Gaming"]
    }

    # expenses = generate_expense_dict(CATEGORIES)

    while True:
        print("\n" + "-" * 50)

        user_input = handle_user_choice(CATEGORIES, MENU, manager)

        # remaining_income = user_income - expenses["Grand_Total"]
        # remaining_balance = current_balance - expenses["Grand_Total"]

        # print(f'---TOTAL EXPENSES: {expenses["Grand_Total"]}')
        # print(f"YOUR INITIAL BALANCE: {current_balance}")
        # print(f'YOUR INITIAL INCOME : {user_income}')
        # print(f'YOUR REMAINING BALANCE: {remaining_balance}')
        # print(f'YOUR REMAINING INCOME: {remaining_income}')


if __name__ == "__main__":
    main()
