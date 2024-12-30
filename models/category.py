import sqlite3
from database import create_connection

class Category:
    def __init__(self, name):
        self.name = name

    def add_category(self):
        """Add a new category to the database."""
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO categories (name) VALUES (?)", (self.name,))
        conn.commit()
        conn.close()

    @staticmethod
    def view_categories():
        """View all categories in the database."""
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM categories")
        categories = cursor.fetchall()
        conn.close()
        return categories
