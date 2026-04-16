from src.constants import MENU_BORDER_CHAR_PRIMARY, MENU_BORDER_CHAR_SECONDARY, MENU_WIDTH

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