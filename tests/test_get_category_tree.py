import sqlite3
from database.database import Database

db = Database("database/database.db")
db.get_category_tree()