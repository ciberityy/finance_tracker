# My Current Code Analysis

## What does my code do right now?
my current code gets the users current_balance through get_user_current_balance : if users enters balance, if balance > MIN_BALANCE then it returns current_balance

after that the program asks the for the user's income : get's the user icome with some verifications 

var CATEGORIES : which is the main data structure, we can generate from it the expense dict, it's a dict containng categories and subcategories 

then we generate_expense_dict : iterating through the CATEGORIES dict we generate the expenses dict 

handle_user_choice : converts the CATEGORIES keys into lists, and check for the number of categories and then gets the user_choice by calling get_user_input and then we set a variable called category name that would access an index in the list of keys 
and then we call handle_expense_category that would enumerate the subcatgories, and then uses the users input to accessa subategory and then it calls get_user_spending_input to add it to the category value and then to the total and grand total 

the program also displays informations about the expenses 

## How is my code organized?
- main.py: the main logic 
- lib.py: all the functions 
- constants.py: a single constant for now

## What data am I storing?
only the transaction amount, which is lacking to be honest, when i looked at your classes with the date and amount and category etc... that's much more detailed and better, i feel like i didn't think about the big picture from the start i just thought about writing code 

## How am I storing it?
dictionnaries 

## What's messy about my current code?
i'd improve everything, i guess i would create a class transaction as i said that would be able to have all the info about a transaction, getting all the informations from the user, i don't know how tho it just crossed my mind 

## What do I actually understand vs. what did I copy?
i think i understand a lot of the code the hard part is thinking about it, i feel like ai helps me in a way where it sees the big picture and thinks about the next step whereas i stuggle to think about the next step