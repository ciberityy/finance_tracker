# src/menu.py
from src.constants import MENU_WIDTH, MENU_BORDER_CHAR_PRIMARY, MENU_BORDER_CHAR_SECONDARY

def generate_transactions_menu(transactions_menu_options):
    """
    Generates the menu prompt string for managing transactions (Add, Delete, Go back).

    Args:
        transactions_menu_options (list): A list of strings representing the options in the transactions menu.

    Returns:
        str: The formatted menu prompt string.
    """
    menu_string = "\n"
    for i, option_item in enumerate(transactions_menu_options, 1):
        menu_string += f"{i}. {option_item}\n"

    menu_string += "\nYour choice : "
    return menu_string


def generate_categories_menu(categories):
    """
    Generates the menu prompt string for choosing a category.

    Args:
        categories (dict): A dictionary where keys are category names.

    Returns:
        str: The formatted menu prompt string.
    """
    menu_string = ""
    menu_string += f"\nChoose a category:\n\n"

    for index, category in enumerate(categories.keys(), 1):
        menu_string += f"{index}. {category}\n"

    menu_string += "Your choice : "
    return menu_string


def generate_main_menu(main_menu_options):
    """
    Generates the main menu prompt string.

    Args:
        main_menu_options (list): A list of strings representing the options in the main menu.

    Returns:
        str: The formatted main menu prompt string.
    """
    print(f"\n{MENU_BORDER_CHAR_SECONDARY * MENU_WIDTH}")
    print("MAIN MENU".center(MENU_WIDTH))
    print(f"{MENU_BORDER_CHAR_SECONDARY * MENU_WIDTH}\n")

    menu_string = "\nSelect an option :\n\n"
    for index, menu_item in enumerate(main_menu_options, 1):
        menu_string += f"{index}. {menu_item}\n"

    menu_string += "\nYour choice : "
    return menu_string


def display_expenses(manager, CATEGORIES, current_balance, user_income):
    """
    Displays a detailed summary of expenses by category and subcategory,
    along with total expenses, current balance, and remaining income.

    Args:
        manager (TransactionManager): The manager object responsible for transaction data.
        categories_data (dict): A dictionary containing category and subcategory information.
        current_balance (int): The user's current balance.
        user_income (int): The user's income.
    """
    print(f"{MENU_BORDER_CHAR_PRIMARY * MENU_WIDTH}")
    print("EXPENSE SUMMARY".center(MENU_WIDTH))
    print(f"{MENU_BORDER_CHAR_PRIMARY * MENU_WIDTH}")

    label_balance = "Balance"
    label_income = "Income"
    amount1 = f"{current_balance:,} dzd"
    amount2 = f"{user_income:,} dzd"

    num_dots1 = MENU_WIDTH - len(label_balance) - len(amount1) - 2
    dots1 = '.' * num_dots1
    line1 = f"{label_balance} {dots1} {amount1}"

    num_dots2 = MENU_WIDTH - len(label_income) - len(amount2) - 2
    dots2 = '.' * num_dots2
    line2 = f"{label_income} {dots2} {amount2}"

    print(line1)
    print(line2)
    print()

    for category_name in CATEGORIES:
        category_total = manager.get_category_total(category_name) ######################
        category_amount_str = f"{category_total:,} dzd"
        num_dots_category = MENU_WIDTH - len(category_name) - len(category_amount_str) - 2
        dots_category = '.' * num_dots_category
        print(f"{category_name} {dots_category} {category_amount_str}")

        for subcategory_name in CATEGORIES[category_name]:
            subcategory_total = manager.get_subcategory_total(category_name, subcategory_name) #####################
            subcategory_amount_str = f"{subcategory_total:,} dzd"
            num_dots_subcategory = MENU_WIDTH - len(subcategory_name) - len(subcategory_amount_str) - 2
            dots_subcategory = "." * num_dots_subcategory
            print(f"  {subcategory_name} {dots_subcategory} {subcategory_amount_str}")

    grand_total = manager.get_total() ####################inance_tracker_cli/src/transactions_cli.py", line 180, in handle_user_choice
    label_total_expenses = "TOTAL EXPENSES"
    amount_total = f"{grand_total:,} dzd"

    num_dots_total = MENU_WIDTH - len(label_total_expenses) - len(amount_total) - 2
    dots_total = "." * num_dots_total

    print(f"{MENU_BORDER_CHAR_SECONDARY * MENU_WIDTH}")
    print(f"{label_total_expenses} {dots_total} {amount_total}")
    print(f"{MENU_BORDER_CHAR_PRIMARY * MENU_WIDTH}")

    remaining_balance = current_balance - grand_total
    remaining_income = user_income - grand_total

    label_rem_balance = "Remaining Balance"
    amount_rem_balance = f"{remaining_balance:,} dzd"
    num_dots_rem_balance = MENU_WIDTH - len(label_rem_balance) - len(amount_rem_balance) - 2
    dots_rem_balance = "." * num_dots_rem_balance
    print(f'{label_rem_balance} {dots_rem_balance} {amount_rem_balance}')

    label_rem_income = "Remaining Income"
    amount_rem_income = f"{remaining_income:,} dzd"
    num_dots_rem_income = MENU_WIDTH - len(label_rem_income) - len(amount_rem_income) - 2
    dots_rem_income = "." * num_dots_rem_income
    print(f"{label_rem_income} {dots_rem_income} {amount_rem_income}")

    print(f"{MENU_BORDER_CHAR_SECONDARY * MENU_WIDTH}")
