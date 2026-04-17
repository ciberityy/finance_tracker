from src.constants import MIN_AMOUNT, MIN_BALANCE, MAX_INCOME

def get_user_balance():
    """
    Prompts the user to enter their current balance and validates the input.
    Ensures the input is a valid integer and falls within a realistic range.

    Returns:
        int: The validated current balance.
    """
    while True:
        balance_str = input("Enter your current balance : ")

        if not balance_str:
            print("Please enter a value.")
            continue

        try:
            balance = int(balance_str)
            if balance < MIN_BALANCE:
                print(f'Balance seems unrealistic (less than {MIN_BALANCE}). Please try again.')
                continue

            print("Balance Updated.\n")

            return balance

        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_user_income():
    """
    Prompts the user to enter their income and validates the input.
    Ensures the input is a valid integer and falls within a realistic range.

    Returns:
        int: The validated income amount.
    """
    while True:
        income_str = input("Type your income: ")

        if not income_str.isdigit():
            print("Invalid amount. Please enter a number.")
            continue

        income = int(income_str)

        if not (MIN_AMOUNT < income < MAX_INCOME):
            print(f"Invalid amount. Please enter a number between {MIN_AMOUNT + 1} and {MAX_INCOME - 1}.")
            continue

        print("Income Updated.\n")

        return income
