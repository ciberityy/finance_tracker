import sys
import time

from src.constants import MIN_AMOUNT, MAX_AMOUNT, MAIN_MENU, TRANSACTIONS_MENU, \
    MANAGE_TRANSACTIONS_CHOICE, MY_EXPENSES_CHOICE, EXIT_CHOICE, \
    ADD_TRANSACTION_CHOICE, DELETE_TRANSACTION_CHOICE, GO_BACK_CHOICE, \
    MENU_BORDER_CHAR_SECONDARY, TRANSACTION_DISPLAY_WIDTH
from src.menu import generate_main_menu, generate_transactions_menu, generate_categories_menu, display_expenses
from models import Transaction

def get_and_validate_user_input(menu_prompt, num_options):
    """
    Displays a menu prompt and returns a validated, 0-indexed integer choice.
    Handles invalid input (non-digits, out of range).

    Args:
        menu_prompt (str): The string prompt to display to the user.
        num_options (int): The total number of valid options (1-indexed).

    Returns:
        int: The validated, 0-indexed integer choice from the user.
    """
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
    """
    Prompts the user to enter an amount spent and validates the input.

    Returns:
        int: The validated spending amount.
    """
    while True:
        try:
            spending_amount_str = input("Enter an amount : ")
            spending_amount = int(spending_amount_str)

            if not (MIN_AMOUNT < spending_amount <= MAX_AMOUNT):
                print(f"Invalid amount. Please enter a number between {MIN_AMOUNT + 1} and {MAX_AMOUNT}.")
                continue
            
            print(MENU_BORDER_CHAR_SECONDARY * TRANSACTION_DISPLAY_WIDTH)
            return spending_amount
        except ValueError:
            print("Invalid amount. Please enter a valid number.")
            continue


def add_expense(manager, category_name, CATEGORIES):
    """
    Guides the user through adding a new expense to a specific category and subcategory.

    Args:
        manager (TransactionManager): The manager object responsible for transaction data.
        category_name (str): The name of the chosen category.
        CATEGORIES (dict): A dictionary containing category and subcategory information.
    """
    while True:
        subcategories = CATEGORIES[category_name]

        for index, subcategory in enumerate(subcategories, 1):
            print(f"{index}. {subcategory}")

        user_choice_str = input("Your Choice : ")

        if not user_choice_str.isdigit():
            print("Invalid input.")
            continue

        user_choice = int(user_choice_str)

        if user_choice < 1 or user_choice > len(subcategories):
            print(f"Invalid choice : {user_choice}")
            continue

        subcategory_name = subcategories[user_choice - 1]

        spendings = get_user_spending()

        transaction = Transaction(spendings, category_name,
                                subcategory_name, date=None, id=None)
        manager.add_transaction(transaction)

        print("Value added to your expenses!")
        print(MENU_BORDER_CHAR_SECONDARY * TRANSACTION_DISPLAY_WIDTH)
        break

def delete_expense(manager):
    """
    Guides the user through selecting and deleting a transaction.
    Displays a numbered list of transactions and handles user input.

    Args:
        manager (TransactionManager): The manager object responsible for transaction data.
    """
    transactions_list = manager.get_all()

    if not transactions_list:
        print("No transactions recorded yet to delete.\n")
        print(MENU_BORDER_CHAR_SECONDARY * TRANSACTION_DISPLAY_WIDTH)
        return

    menu_list_prompt = "Select a transaction to delete (or type 0 to cancel):\n\n"
    
    for i, transaction in enumerate(transactions_list, 1):
        menu_list_prompt += f"{i}. {transaction.__repr__()}\n"

    menu_list_prompt += "\nYour choice :  "

    while True:
        try:   
            user_input_str = input(menu_list_prompt)
            print("USER INPUT:", user_input_str)

        except KeyboardInterrupt:
            print("Exiting program...")
            break

        if not user_input_str.isdigit():
            print("ivalid input try again.\n")
            continue

        user_input_int = int(user_input_str)
        print("USER INPUT INT:", user_input_int)

        if user_input_int == 0:
            print("\nTransaction deletion canceled...\n")
            time.sleep(0.4)
            return

        if 1 <= user_input_int <= len(transactions_list):
            user_input = user_input_int -1
            
            transaction_to_delete = transactions_list[user_input]
            manager.delete_transaction(transaction_to_delete)
            print(f"\nTRANSACTION INFO :\n-CATEGORY : {transaction_to_delete.category} \n-AMOUNT : {transaction_to_delete.amount} dzd\n-STATUS : deleted successfully!\n")
            return
        
        else:
            print(f"Deletion failed. Enter a number between 1 and {len(transactions_list)}.\n")

     
    

def handle_user_choice(CATEGORIES, manager, current_balance, user_income):
    """
    Handles the user's main menu choice and directs to appropriate sub-menus or actions.
    This function orchestrates the flow of the application based on user input.

    Args:
        CATEGORIES (dict): A dictionary containing category and subcategory information.
        manager (TransactionManager): The manager object responsible for transaction data.
        current_balance (int): The user's current balance.
        user_income (int): The user's income.

    Returns:
        int: The user's choice from the main menu (0-indexed).
    """
    categories_list = list(CATEGORIES.keys())
    
    main_menu_prompt = generate_main_menu(MAIN_MENU) 
    transactions_menu_prompt = generate_transactions_menu(TRANSACTIONS_MENU)
    categories_menu_prompt = generate_categories_menu(CATEGORIES)

    user_input = get_and_validate_user_input(main_menu_prompt, len(MAIN_MENU))

    if user_input == MANAGE_TRANSACTIONS_CHOICE:  # Manage transactions 
        transactions_menu_choice = get_and_validate_user_input(transactions_menu_prompt, len(TRANSACTIONS_MENU))

        if transactions_menu_choice == ADD_TRANSACTION_CHOICE:  # Add a transaction 
            
            categories_menu_choice = get_and_validate_user_input(categories_menu_prompt, len(CATEGORIES))

            category_name = categories_list[categories_menu_choice]
            add_expense(manager, category_name, CATEGORIES) 

        elif transactions_menu_choice == DELETE_TRANSACTION_CHOICE:  # Delete a transaction
            delete_expense(manager)

        elif transactions_menu_choice == GO_BACK_CHOICE: # Go back to the main menu
            pass # No action needed, loop continues

    elif user_input == MY_EXPENSES_CHOICE:  # User chose "My expenses"
        display_expenses(manager, CATEGORIES, current_balance, user_income)
    
    elif user_input == EXIT_CHOICE:   # User chose "Exit"
        print("Exiting program...")
        time.sleep(0.5)
        sys.exit()

    return user_input