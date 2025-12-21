
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

def handle_expense_category(category_name, sub_menu, subcategory_dict, expense_dict):
    
    """displays the correct sub menu to the user depending on his category choice,
    if the user's input is correct, it converts it to an int, then access the user sub input in the subcategory dict
    and then asks for the spending amount,
    it then increments that sub category and then the total of that category and then the whole dictionnary (Grand_Total)
    prints whether or not it worked.
    this functions avoids repeating the code each time the user chooses a category to add expenses to 

    Args:
        category_name (str): the main categories 
        sub_menu (str): sub_menus with the sub categories 
        subcategory_dict (dict): subcategory dict with numbers as keys in order to link that with the main dict
        expense_dict (dict): the whole main dictionnary
    
    Returns:
        None: This function doesn't return a value, it modifies the expense dictionary in place."""
    
    while True:
        user_sub_input = input(sub_menu)

        for key in subcategory_dict.keys():
            sub_menu_choice = str(key)
            print(key)

            if user_sub_input in sub_menu_choice:
                user_sub_input = int(user_sub_input)
                
                subcategory = subcategory_dict[user_sub_input]
                
                spendings = get_user_spending_input()
                print(spendings)
                
                expense_dict[category_name][subcategory] += spendings
                expense_dict[category_name]["Total"] += spendings
                expense_dict["Grand_Total"] += spendings
                
                print("Value added to your expenses!")
                print("-" * 50)
                break

            else:
                print("Invalid input please try again.")
            
            break
        break

                
               
            
        

if __name__ == "__main__":
    get_user_current_balance()



    


