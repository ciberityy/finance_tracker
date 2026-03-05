import sys

from models import Transaction

MIN_AMOUNT = 1
MAX_AMOUNT = 60000
MAX_INCOME = 1000000
MIN_BALANCE = -100000


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


def get_user_income():
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


def get_user_spending():
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
            if current_balance < MIN_BALANCE:
                print('Balance seems unrealistic, try again.')
                continue

            print("Balance Updated")
            return current_balance

        except ValueError:
            print("Invalid input. Please enter a valid number")


def handle_expense_category(manager, category_name, CATEGORIES):
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

        spendings = get_user_spending()

        t = Transaction(spendings, category_name, subcategory_name)
        manager.add_transaction(t)

        print("Value added to your expenses!")
        print("-" * 50)
        break


def handle_user_choice(CATEGORIES, MENU, manager, current_balance, user_income):

    categories = list(CATEGORIES.keys())
    num_categories = len(CATEGORIES)
    user_choice = get_user_input(CATEGORIES, MENU)

    if user_choice <= num_categories:
        category_name = categories[user_choice - 1]
        handle_expense_category(manager, category_name, CATEGORIES)

    elif user_choice == (num_categories + 1):
        display_expenses(manager, CATEGORIES, current_balance, user_income)

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


def display_expenses(manager, CATEGORIES, current_balance, user_income):

    print("=" * 47)
    print("EXPENSE SUMMARY".center(47))
    print("=" * 47)

    width = 47
    label = "Balance"
    label_2 = "Income"
    amount1 = f"{current_balance:,} dzd"
    amount2 = f"{user_income:,} dzd"

    num_dots = width - len(label) - len(amount1) - 2
    dots1 = '.' * num_dots

    num_dots = width - len(label_2) - len(amount2) - 2
    dots = '.' * num_dots

    line1 = f"{label} {dots1} {amount1}"
    line2 = f"{label_2} {dots} {amount2}"

    print(line1)
    print(line2)
    print()

    for category_name in CATEGORIES:
        category_total = manager.get_category_total(category_name)

        width = 47
        category = f"{category_name}"
        amount = f"{category_total:,} dzd"

        num_dots = width - len(category) - len(amount) - 2
        dots = '.' * num_dots
        line = f"{category} {dots} {amount}"

        print(line)

        for subcategory_name in CATEGORIES[category_name]:
            subcategory_total = manager.get_subcategory_total(
                category_name, subcategory_name)

            width = 47
            subcategory = f"{subcategory_name}"
            amount = f"{subcategory_total:,} dzd"

            num_dots = width - len(subcategory) - len(amount) - 2
            dots = "." * num_dots
            line = f"  {subcategory_name} {dots} {amount}"

            print(line)

    grand_total = manager.get_total()
    label = "TOTAL EXPENSES"
    amount = f"{grand_total:,} dzd"

    equal_signs = "=" * 47
    solo_signs = "-" * 47
    num_dots = width - len(label) - len(amount) - 2
    dots = "." * num_dots

    line = f"""{solo_signs}\n{label} {dots} {amount}\n{equal_signs}"""

    print(line)

    remaining_balance = current_balance - grand_total
    remaining_income = user_income - grand_total

    label = "Remaining Balance"
    amount = f"{remaining_balance:,} dzd"

    num_dots = width - len(label) - len(amount) - 2
    dots = "." * num_dots
    line = f'{label} {dots} {amount}'

    print(line)

    label = "Remaining Income"
    amount = f"{remaining_income:,} dzd"

    num_dots = width - len(label) - len(amount) - 2
    dots = "." * num_dots
    line = f"{label} {dots} {amount}"

    print(line)


if __name__ == "__main__":
    pass
