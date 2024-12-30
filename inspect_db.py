import sqlite3

def inspect_tables():
    conn = sqlite3.connect('budget_tracker.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    print("Tables:", tables)
    conn.close()

if __name__ == "__main__":
    inspect_tables()
