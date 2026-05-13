import sqlite3

CATEGORIES = {
        "Food": ["Sandwich", "Coffee", "Water"],
        "Transport": ["Bus", "Taxi", "Vtc"],
        "Chill_day": ["Dinner", "Beach_day", "Gaming"]}

def seed_categories_table(categories):
    conn = sqlite3.connect("database.db")

    c = conn.cursor()

    categories_list = list(categories.keys())

    for category in categories_list:

        sub_categories_list = categories[category]
        
        query = ("INSERT INTO categories (name, parent_id) VALUES (?,?)")
        values = (category, None)
        
        c.execute(query, values)

        categories_id = c.lastrowid
        
        for sub_category in sub_categories_list:
            
            query = ("INSERT INTO categories (name, parent_id) VALUES (?,?)")
            values = (sub_category, categories_id)

            c.execute(query,values) 

    conn.commit()

    conn.close()

seed_categories_table(categories=CATEGORIES)


  


