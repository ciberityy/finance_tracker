MAX_INCOME = 1000000
MIN_BALANCE = -100000
MIN_AMOUNT = 1


def get_user_balance():
    """gets the user's current balance"""

    while True:
        balance = input("Enter your current balance : ")

        if not balance:
            print("Please enter a value.")
            continue

        try:
            balance = int(balance)
            if balance < MIN_BALANCE:
                print('Balance seems unrealistic, try again.')
                continue

            print("Balance Updated.\n")

            return balance

        except ValueError:
            print("Invalid input. Please enter a valid number")


def get_user_income():
    """gets the user's income"""

    while True:
        income = input("Type your income: ")

        if not income.isdigit():
            print("Invalid amount.")
            continue

        income = int(income)

        if not (MIN_AMOUNT < income < MAX_INCOME):
            print("Invalid amount try again.")
            continue

        print("Income Updated.\n")

        return income
