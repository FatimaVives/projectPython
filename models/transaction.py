import sqlite3
from database import create_connection

class Transaction:
    def __init__(self, amount, transaction_type, category_id, description, date):
        self.amount = amount
        self.transaction_type = transaction_type
        self.category_id = category_id
        self.description = description
        self.date = date

    def add_transaction(self):
        """Add a new transaction to the database."""
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO transactions (amount, transaction_type, category_id, description, date)
            VALUES (?, ?, ?, ?, ?)
        ''', (self.amount, self.transaction_type, self.category_id, self.description, self.date))
        conn.commit()
        conn.close()

    @staticmethod
    def view_transactions():
        """View all transactions in the database."""
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT t.id, t.amount, t.transaction_type, c.name, t.description, t.date FROM transactions t JOIN categories c ON t.category_id = c.id')
        transactions = cursor.fetchall()
        conn.close()
        return transactions

    @staticmethod
    def total_balance():
        """Calculate the total balance (income - expenses)."""
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT SUM(amount) FROM transactions WHERE transaction_type = "income"')
        income = cursor.fetchone()[0] or 0
        cursor.execute('SELECT SUM(amount) FROM transactions WHERE transaction_type = "expense"')
        expenses = cursor.fetchone()[0] or 0
        conn.close()
        return income - expenses
