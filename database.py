from settings import DATABASE_PATH
import sqlite3

def create_connection():
    """Create a connection to the SQLite database."""
    conn = sqlite3.connect('budget_tracker.db')
    return conn

def create_tables():
    """Create the necessary tables in the database."""
    conn = create_connection()
    cursor = conn.cursor()

    # Create categories table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS categories (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL
        )
    ''')

    # Create transactions table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY,
            amount REAL NOT NULL,
            transaction_type TEXT NOT NULL,  -- "income" or "expense"
            category_id INTEGER NOT NULL,
            description TEXT,
            date TEXT NOT NULL,
            FOREIGN KEY (category_id) REFERENCES categories(id)
        )
    ''')

    conn.commit()
    conn.close()
