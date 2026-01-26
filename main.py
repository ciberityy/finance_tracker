import sys
from constants import MENU

from lib import get_user_input, get_user_income_input, get_user_current_balance, handle_expense_category, generate_expense_dict, handle_user_choice


def main():
    current_balance = get_user_current_balance()
    user_income = get_user_income_input()

    CATEGORIES = {
        "Food": ["Sandwich", "Coffee", "Water"],
        "Transport": ["Bus", "Taxi", "Vtc"],
        "Chill_day": ["Dinner", "Beach_day", "Gaming"],
        "Entertainement": ["Movies", "Games", "Concert"]
    }

    expenses = generate_expense_dict(CATEGORIES)

    while True:
        print("\n" + "-" * 50)

        user_input = handle_user_choice(CATEGORIES, MENU)

        if user_input == 1:
            handle_expense_category(CATEGORIES, "Food", expenses)

        elif user_input == 2:
            handle_expense_category(CATEGORIES, "Transport", expenses)

        elif user_input == 3:
            handle_expense_category(CATEGORIES, "Chill_day", expenses)

        elif user_input == 4:

            print("\n" + "-" * 50)
            print(f"\n---Food expenses: {expenses['Food']["Total"]} dzd")
            print(
                f"Money spent on sandwiches: {expenses['Food']["Sandwich"]} dzd")
            print(f"Money spent on coffee: {expenses['Food']["Coffee"]} dzd")
            print(f"Money spent on water: {expenses['Food']["Water"]} dzd")
            print(
                f"\n---Transport expenses: {expenses['Transport']["Total"]} dzd")
            print(f"Money spent on Bus : {expenses['Transport']["Bus"]} dzd")
            print(f"Money spent on Taxi : {expenses['Transport']["Taxi"]} dzd")
            print(f"Money spent on Vtc : {expenses['Transport']["Vtc"]} dzd")
            print(
                f"\n---Chill day expenses: {expenses['Chill_day']["Total"]} dzd")
            print(
                f"Money spent on dinner : {expenses['Chill_day']["Dinner"]} dzd")
            print(
                f"Money spent on Beach day : {expenses['Chill_day']["Beach_day"]} dzd")
            print(
                f"Money spent on Gaming : {expenses['Chill_day']["Gaming"]} dzd")

            print("-" * 50 + "\n")

        elif user_input == 5:
            sys.exit()

        remaining_income = user_income - expenses["Grand_Total"]
        remaining_balance = current_balance - expenses["Grand_Total"]

        print(f'---TOTAL EXPENSES: {expenses["Grand_Total"]}')
        print(f"YOUR INITIAL BALANCE: {current_balance}")
        print(f'YOUR INITIAL INCOME : {user_income}')
        print(f'YOUR REMAINING BALANCE: {remaining_balance}')
        print(f'YOUR REMAINING INCOME: {remaining_income}')


if __name__ == "__main__":
