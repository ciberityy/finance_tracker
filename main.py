import sys


from constants import SUB_MENU, SUB_MENU_2, SUB_MENU_3
from lib import get_user_input, get_user_income_input, get_user_current_balance, handle_expense_category


def main():
    current_balance = get_user_current_balance()
    user_income = get_user_income_input()

    CATEGORIES = {
                    "Food": ["Sandwich", "Coffee" , "Water"],
                    "Transport": ["Bus", "Taxi", "Vtc" ],
                    "Chill_day": ["Dinner", "Beach_day", "Gaming"],
                    }
    
    d = {"Grand_Total": 0,
    
    "Food": {
        "Total": 0,
        "Sandwich": 0,
        "Coffee": 0,
        "Water": 0,
    },
    "Transport": {
        "Total": 0,
        "Bus": 0,
        "Taxi": 0,
        "Vtc": 0,
    },
    "Chill_day": {
        "Total": 0,
        "Dinner": 0,
        "Beach_day": 0,
        "Gaming": 0,
    }
    }

    while True:
        print("\n" + "-" * 50)
        user_input = get_user_input()
        
        if user_input == "1":
            handle_expense_category(CATEGORIES=CATEGORIES, category_name="Food", expense_dict=d)
        
              
        elif user_input == "2":
            handle_expense_category(CATEGORIES=CATEGORIES,category_name="Transport", expense_dict=d)
       
        
        elif user_input == "3":
           handle_expense_category(CATEGORIES=CATEGORIES, category_name="Chill_day", expense_dict=d)
      
    
        
        elif user_input == "4":
            
            print("\n" + "-" * 50)
            print(f"\n---Food expenses: {d['Food']["Total"]} dzd")
            print(f"Money spent on sandwiches: {d['Food']["Sandwich"]} dzd")
            print(f"Money spent on coffee: {d['Food']["Coffee"]} dzd")
            print(f"Money spent on water: {d['Food']["Water"]} dzd")
            print(f"\n---Transport expenses: {d['Transport']["Total"]} dzd")
            print(f"Money spent on Bus : {d['Transport']["Bus"]} dzd")
            print(f"Money spent on Taxi : {d['Transport']["Taxi"]} dzd")
            print(f"Money spent on Vtc : {d['Transport']["Vtc"]} dzd")
            print(f"\n---Chill Day expenses: {d['Chill_day']["Total"]} dzd")
            print(f"Money spent on Dinner : {d['Chill_day']["Dinner"]} dzd")   
            print(f"Money spent on Beach Day : {d['Chill_day']["Beach_day"]} dzd")
            print(f"Money spent on Gaming : {d['Chill_day']["Gaming"]} dzd")
            
            
            print("-" * 50 + "\n" )

         
        
        elif user_input == "5":
            sys.exit()

        remaining_income = user_income - d["Grand_Total"]
        remaining_balance = current_balance - d["Grand_Total"]

        print(f'---TOTAL EXPENSES: {d["Grand_Total"]}')
        print(f"YOUR INITIAL BALANCE: {current_balance}")
        print(f'YOUR INITIAL INCOME : {user_income}')
        print(f'YOUR REMAINING BALANCE: {remaining_balance}')
        print(f'YOUR REMAINING INCOME: {remaining_income}')
           
        


if __name__ == "__main__":
    main()
    
    
            


            
