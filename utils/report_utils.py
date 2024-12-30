import pandas as pd
import matplotlib.pyplot as plt
from models.transaction import Transaction


def generate_csv_report(report_data):
    """Generate a CSV report."""
    df = pd.DataFrame(report_data).T
    df.to_csv('transactions_report.csv', index=False)

def generate_excel_report(report_data):
    """Generate an Excel report."""
    df = pd.DataFrame(report_data).T
    df.to_excel('transactions_report.xlsx', index=False)


def calculate_balance():
    """Calculate the net balance (income - expenses)."""
    transactions = Transaction.view_transactions()
    income = sum(tx[1] for tx in transactions if tx[2] == 'income')
    expenses = sum(tx[1] for tx in transactions if tx[2] == 'expense')
    return income - expenses

def plot_balance():
    """Plot the cumulative balance over time."""
    transactions = Transaction.view_transactions()
    df = pd.DataFrame(transactions, columns=['id', 'amount', 'type', 'category_id', 'description', 'date'])
    df['date'] = pd.to_datetime(df['date'])
    df = df.sort_values(by='date')

    df['balance'] = df.apply(lambda row: row['amount'] if row['type'] == 'income' else -row['amount'], axis=1).cumsum()
    
    plt.figure(figsize=(10, 6))
    plt.plot(df['date'], df['balance'], marker='o', linestyle='-', color='blue', label='Cumulative Balance')
    plt.xlabel('Date')
    plt.ylabel('Balance')
    plt.title('Balance Over Time')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig('balance_plot.png')
    plt.show()
