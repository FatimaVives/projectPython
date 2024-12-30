import pandas as pd
from models.transaction import Transaction

class Report:
    @staticmethod
    def generate_report():
        """Generate a report showing totals for each category."""
        transactions = Transaction.view_transactions()
        data = {}
        for transaction in transactions:
            category = transaction[3]  # Category name
            if category not in data:
                data[category] = {'income': 0, 'expense': 0}
            if transaction[2] == 'income':
                data[category]['income'] += transaction[1]
            else:
                data[category]['expense'] += transaction[1]

        return data

    @staticmethod
    def export_to_csv(report):
        """Export the report to a CSV file."""
        df = pd.DataFrame(report).T
        df.to_csv('budget_report.csv')

    @staticmethod
    def export_to_excel(report):
        """Export the report to an Excel file."""
        df = pd.DataFrame(report).T
        df.to_excel('budget_report.xlsx')
