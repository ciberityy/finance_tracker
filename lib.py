import sys

MIN_AMOUNT = 1
MAX_AMOUNT = 60000
MAX_INCOME = 1000000


def get_user_input(CATEGORIES, MENU):
    """user chooses a category to add expenses to"""

    valid_choice = len(CATEGORIES) + len(MENU)

    while True:
        user_input = input(generate_main_menu(CATEGORIES, MENU))

        if not user_input.isdigit():
            print("Invalid input.")
            continue

        user_input = int(user_input)

        if not user_input <= valid_choice and not user_input > 0:
            print("Invalid input")
            continue

        print("-" * 50)
        return user_input


def get_user_income_input():
    """gets the user's income"""

    while True:
        user_income = input("Type your income: ")

        if not user_income.isdigit():
            print("Invalid amount.")
            continue

        user_income = int(user_income)

        if not (MIN_AMOUNT < user_income < MAX_INCOME):
            print("Invalid amount try again.")
            continue

        return user_income


def get_user_spending_input():
    """gets the amount spent by the user"""

    while True:
        spending_amout = input("Enter an amount : ")

        if not spending_amout.isdigit():
            print("Invalid amount.")
            continue

        spending_amout = int(spending_amout)

        if not (MIN_AMOUNT < spending_amout <= MAX_AMOUNT):
            print("Invalid amount.")
            continue

        print("-" * 50)
        return spending_amout


def get_user_current_balance():
    """gets the user's current balance"""

    while True:
        current_balance = input("Enter your current balance : ")

        if not current_balance:
            print("Please enter a value.")
            continue

        try:
            current_balance = int(current_balance)
            if current_balance < -100000:
                print('Balance seems unrealistic, try again.')
                continue
            print("Balance Updated")
            return current_balance

        except ValueError:
            print("Invalid input. Please enter a valid number")


def handle_expense_category(CATEGORIES, category_name, expenses):
    """adds expenses to a specific category"""

    while True:
        subcategories = CATEGORIES[category_name]

        for index, subcategory in enumerate(subcategories, 1):
            print(f"{index}. {subcategory}")

        user_choice = input("Your Choice : ")

        if not user_choice.isdigit():
            print("Invalid input.")
            continue

        user_choice = int(user_choice)

        if user_choice < 1 or user_choice > len(subcategories):
            print(f"Invalid choice : {user_choice}")
            continue

        subcategory_name = subcategories[user_choice - 1]

        spendings = get_user_spending_input()

        expenses[category_name][subcategory_name] += spendings
        expenses[category_name]["Total"] += spendings
        expenses["Grand_Total"] += spendings

        print("Value added to your expenses!")
        print("-" * 50)
        break


def handle_user_choice(CATEGORIES, MENU, expenses):

    categories = list(CATEGORIES.keys())
    num_categories = len(CATEGORIES)
    user_choice = get_user_input(CATEGORIES, MENU)

    if user_choice <= num_categories:
        category_name = categories[user_choice - 1]
        handle_expense_category(CATEGORIES, category_name, expenses)

    elif user_choice == (num_categories + 1):
        display_expenses(expenses)

    elif user_choice == (num_categories + 2):
        sys.exit()


def generate_main_menu(CATEGORIES, MENU):
    """Generate the main menu for the user"""

    number_of_categories = len(CATEGORIES)

    menu = ""
    menu += f"Choose a category:\n\n"

    for index, category in enumerate(CATEGORIES.keys(), 1):
        menu += f"{index}. {category}\n"

    for i, item in enumerate(MENU, number_of_categories + 1):
        menu += f"{i}. {item}\n"
    menu += f"Your choice : "

    return menu


def generate_expense_dict(CATEGORIES):
    expenses = {"Grand_Total": 0}
    for k, v in CATEGORIES.items():
        subcategory = {item: 0 for item in v}
        subcategory["Total"] = 0
        expenses[k] = subcategory

    return expenses


def display_expenses(expenses):
    print("\n" + "-" * 50)
    print(f"\n---Food expenses: {expenses['Food']["Total"]} dzd")
    print(f"Money spent on sandwiches: {expenses['Food']["Sandwich"]} dzd")
    print(f"Money spent on coffee: {expenses['Food']["Coffee"]} dzd")
    print(f"Money spent on water: {expenses['Food']["Water"]} dzd")
    print(f"\n---Transport expenses: {expenses['Transport']["Total"]} dzd")
    print(f"Money spent on Bus : {expenses['Transport']["Bus"]} dzd")
    print(f"Money spent on Taxi : {expenses['Transport']["Taxi"]} dzd")
    print(f"Money spent on Vtc : {expenses['Transport']["Vtc"]} dzd")
    print(f"\n---Chill day expenses: {expenses['Chill_day']["Total"]} dzd")
    print(f"Money spent on dinner : {expenses['Chill_day']["Dinner"]} dzd")
    print(
        f"Money spent on Beach day : {expenses['Chill_day']["Beach_day"]} dzd")
    print(f"Money spent on Gaming : {expenses['Chill_day']["Gaming"]} dzd")
    print("-" * 50 + "\n")


if __name__ == "__main__":
    pass
