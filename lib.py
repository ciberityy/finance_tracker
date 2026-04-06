import sys
import time

from models import Transaction

MIN_AMOUNT = 1
MAX_AMOUNT = 60000

MAIN_MENU = ["Manage transactions", "My expenses", "Exit"]
TRANSACTIONS_MENU = ["Add a transaction", "Delete a transaction", "Go back to the main menu"]


def get_and_validate_user_input(menu_prompt, num_options):
    """Displays a menu prompt and returns a validated, 0-indexed integer choice.
    Handles invalid input (non-digits, out of range)."""

    while True:

        try:
            user_input_str = input(menu_prompt)
        
        except KeyboardInterrupt:
            print("\nExiting program...")
            sys.exit(0)


        if not user_input_str.isdigit():
            print("\nInvalid input. Please enter a number.\n")
            continue                        

        user_input_int = int(user_input_str)

        if not 1 <= user_input_int <= num_options:
            print(f"\nInvalid input. Please enter a number between 1 and {num_options}.\n")
            continue

        return user_input_int - 1
    


def get_user_spending():
    """gets the amount spent by the user"""

    while True:
        spending_amount = input("Enter an amount : ")

        if not spending_amount.isdigit():
            print("Invalid amount.")
            continue

        spending_amount = int(spending_amount)

        if not (MIN_AMOUNT < spending_amount <= MAX_AMOUNT):
            print("Invalid amount.")
            continue

        print("-" * 50)
        return spending_amount


def add_expense(manager, category_name, CATEGORIES):
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

        t = Transaction(spendings, category_name,
                        subcategory_name, date=None, id=None)
        manager.add_transaction(t)

        print("Value added to your expenses!")
        print("-" * 50)
        break

def delete_expense(manager):
    """Guides the user through selecting and deleting a transaction.
    Displays a numbered list of transactions and handles user input."""
    
    transactions_list = manager.get_all()

    if not transactions_list:
        print("No transactions recorded yet to delete.\n")
        print("-" * 50)
        return

    menu_list_prompt = "Select a transaction to delete (or type 0 to cancel):\n\n"
    
    for i, transaction in enumerate(transactions_list, 1):
        menu_list_prompt += f"{i}. {transaction.__repr__()}\n"

    menu_list_prompt += "\nYour choice :  "   

    user_input = get_and_validate_user_input(menu_list_prompt, len(transactions_list) + 1)

    if user_input == -1:
        print("\nTransaction deletion canceled.\n")
        return

    transaction_to_delete = transactions_list[user_input]
    manager.delete_transaction(transaction_to_delete)

    print(f"\nTransaction : 'CATEGORY : {transaction_to_delete.category} AMOUNT : {transaction_to_delete.amount} dzd' deleted successfully!\n")

    


def handle_user_choice(CATEGORIES, MAIN_MENU, TRANSACTIONS_MENU, manager, current_balance, user_income):
        """Handles the user's main menu choice and directs to appropriate sub-menus or actions.
    This function orchestrates the flow of the application based on user input."""
        
        categories = list(CATEGORIES.keys())                                                            
        
        main_menu_prompt = generate_main_menu(MAIN_MENU) 
        transactions_menu_prompt = generate_transactions_menu(TRANSACTIONS_MENU)
        categories_menu_prompt = generate_categories_menu(CATEGORIES)

        user_input = get_and_validate_user_input(main_menu_prompt, len(MAIN_MENU))

        if user_input == 0:  #  if user input = Manage transactions 
            transactions_menu_choice = get_and_validate_user_input(transactions_menu_prompt, len(TRANSACTIONS_MENU))

            if transactions_menu_choice == 0:  # if user_input = Add a transaction 
                
                categories_menu_choice = get_and_validate_user_input(categories_menu_prompt, len(CATEGORIES))

                category_name = categories[categories_menu_choice]
                add_expense(manager, category_name, CATEGORIES) 

            elif transactions_menu_choice == 1:  # if user_input = Delete a transaction
                delete_expense(manager)

            elif transactions_menu_choice == 2:
                pass

        elif user_input == 1:  # User chose "My expenses"
            display_expenses(manager, CATEGORIES, current_balance, user_income)
        
        elif user_input == 2:   # User chose "Exit"
            print("Exiting program...")
            time.sleep(0.5)
            
            sys.exit()
                                                                                            


def generate_transactions_menu(TRANSACTIONS_MENU):
    """Generates the menu prompt string for managing transactions
    (Add, Delete, Go back)."""

    menu = "\n"
    for i, option_item in enumerate(TRANSACTIONS_MENU, 1):
        menu += f"{i}. {option_item}\n"

    menu += "\nYour choice : "

    return menu


def generate_categories_menu(CATEGORIES):
    """Generate the menu of categories"""

    menu = ""
    menu += f"\nChoose a category:\n\n"

    for index, category in enumerate(CATEGORIES.keys(), 1):
        menu += f"{index}. {category}\n"

    menu += "Your choice : "
    
    return menu

def generate_main_menu(MAIN_MENU):
    """generate the main menu"""
    
    print("\n" + "-" * 47)
    print("MAIN MENU".center(47))
    print("-" * 47 + "")
    
    menu =""
    menu += "\nSelect an option :\n\n"
    

    for index, menu_item in enumerate(MAIN_MENU, 1):
        menu += f"{index}. {menu_item}\n"
    
    menu += "\nYour choice : "

    
    return menu


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

    print("-" * 47)


if __name__ == "__main__":
    pass
