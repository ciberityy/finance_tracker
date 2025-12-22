
from constants import MENU, MENU_CHOICES

def get_user_input():
    
    """gets the users input to choose a category to add expenses to,
    then checks if that input is valid 
    then it converts the input to an int

    Returns:
        str: has to be contained in MENU_CHOICES
    """
    while True:
        user_input = input(MENU)
        if user_input in MENU_CHOICES:
            return user_input    
        
        print("Invalid input, try again.")
        print("-" * 50) 

def get_user_income_input(): 
    
    """ gets the user's incomes input then checks the inputs validity by
    verifying if it's > 0 and digit

    Returns:
        int: has to be over 0 
    """
    while True:
        user_income = input("Type your income: ")
        
        if user_income.isdigit() and ( 0 < int(user_income) < 600000):
            user_income = int(user_income)
            return user_income 
        
        print("Invalid income.")


def get_user_spending_input(): 
    
    """gets the user's spendings input for a specific item(category and sub category) 
        an input is considered valid if it passes the .isdigit() method and is > 0 
        when an input is invalid it tells the user that it's wrong and asks for an input again 
    
    Returns:
        int: has to be over 0  
    """
    while True:
        spending_amout_input = input("Enter an amount : ")

        if spending_amout_input.isdigit() and (0 < int(spending_amout_input) < 60000):
            spending_amout_input = int(spending_amout_input)
            return spending_amout_input
        
        print("Invalid input. try again.")
        print("-" * 50)

def get_user_current_balance():
    
    """gets the user's input for his current balance
        checks if the input is an integer, if not it'll loop again 
    Returns:
        int: can be negative or positive 
    """

    while True:
        current_balance = input("Enter your current balance : ")
        if current_balance:
            try:
                current_balance = int(current_balance)
                print("Balance updated !")
                return current_balance
            
            except ValueError:
                print("Invalid input. Please enter a valid number")

def handle_expense_category(CATEGORIES, category_name, expense_dict):
    
    while True:
        subcategories = CATEGORIES[category_name]

        for index, subcategory in enumerate(subcategories, 1):
            print(f"{index}. {subcategory}")

        user_choice = input("Your Choose : ")

        if not user_choice.isdigit():
            print("Invalid input.")
            continue
        
        user_choice = int(user_choice)
        
        subcategory_name = subcategories[user_choice - 1]

        spendings = get_user_spending_input()
            
        expense_dict[category_name][subcategory_name] += spendings
        expense_dict[category_name]["Total"] += spendings   
        expense_dict["Grand_Total"] += spendings
 
            
        print("Value added to your expenses!")
        print("-" * 50)
        break               
            
        

if __name__ == "__main__":
    pass


    


