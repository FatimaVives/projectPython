import os
from models.transaction import Transaction
from models.category import Category
from models.report import Report
from utils.report_utils import generate_csv_report, generate_excel_report, calculate_balance, plot_balance

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Welcome to Personal Budget Tracker")
    
    while True:
        print("\n1. Add Transaction")
        print("2. View Transactions")
        print("3. Add Category")
        print("4. View Categories")
        print("5. Generate Report")
        print("6. Export Report to CSV")
        print("7. Export Report to Excel")
        print("8. Calculate Balance")
        print("9. Plot Balance Over Time")
        print("10. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            amount = float(input("Enter amount: "))
            transaction_type = input("Enter transaction type (income/expense): ").lower()
            category_id = int(input("Enter category ID: "))
            description = input("Enter description: ")
            date = input("Enter date (YYYY-MM-DD): ")
            
            transaction = Transaction(amount, transaction_type, category_id, description, date)
            transaction.add_transaction()

        elif choice == '2':
            transactions = Transaction.view_transactions()
            for transaction in transactions:
                print(transaction)

        elif choice == '3':
            category_name = input("Enter category name: ")
            category = Category(category_name)
            category.add_category()

        elif choice == '4':
            categories = Category.view_categories()
            for category in categories:
                print(category)

        elif choice == '5':
            report = Report.generate_report()
            print("Report Generated:", report)

        elif choice == '6':
            report = Report.generate_report()
            generate_csv_report(report)
            print("Report exported to CSV.")

        elif choice == '7':
            report = Report.generate_report()
            generate_excel_report(report)
            print("Report exported to Excel.")


        elif choice == '8':
            balance = calculate_balance()
            print(f"\nYour current balance is: {balance:.2f}\n")


        elif choice == '9':
            plot_balance()
            print("Balance plot generated!")


        elif choice == '10':
            print("Goodbye!")
            os.system('cls' if os.name == 'nt' else 'clear')
            break

        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
