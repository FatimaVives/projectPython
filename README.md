# Personal Budget Tracker

## Overview
The Personal Budget Tracker is a command-line application designed to help users manage their finances effectively. It allows users to record transactions, categorize them, generate reports, and visualize their financial trends over time. This project is developed using Python and employs SQLite for data storage.

---

## Features
1. **Add Transactions**: Record financial transactions as either income or expenses.
2. **View Transactions**: Display all recorded transactions.
3. **Add Categories**: Define categories to organize transactions (e.g., Salary, Groceries, Utilities).
4. **View Categories**: List all existing categories.
5. **Generate Reports**: Create summarized reports showing income and expenses by category.
6. **Export Reports**:
   - CSV format
   - Excel format
7. **Calculate Balance**: Calculate the net balance (total income minus total expenses).
8. **Visualize Balance Over Time**: Generate a graph showing the cumulative balance trend.

---

## Installation

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Steps
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Create a virtual environment:
   ```bash
   python -m venv project_env
   source project_env/bin/activate  # On Windows: project_env\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Initialize the database:
   ```bash
   python database.py
   ```

---

## Usage

### Run the Application
```bash
python app.py
```

### Menu Options
1. **Add Transaction**:
   - Enter the transaction amount, type (income or expense), category ID, description, and date (YYYY-MM-DD).
2. **View Transactions**:
   - Displays all recorded transactions.
3. **Add Category**:
   - Provide a category name (e.g., "Salary").
4. **View Categories**:
   - Lists all available categories with their IDs.
5. **Generate Report**:
   - Shows income and expenses summarized by category.
6. **Export Report to CSV**:
   - Exports the generated report to a `transactions_report.csv` file.
7. **Export Report to Excel**:
   - Exports the generated report to a `transactions_report.xlsx` file.
8. **Calculate Balance**:
   - Displays the net balance (total income minus total expenses).
9. **Plot Balance Over Time**:
   - Displays a graph of the cumulative balance trend over time.
10. **Exit**:
   - Exits the application.

---

## Project Structure
```
project-folder/
├── app.py               # Main application file
├── database.py          # Database initialization script
├── requirements.txt     # List of required Python packages
├── README.md            # Project documentation
├── models/              # Data model definitions
│   ├── transaction.py   # Transaction model
│   ├── category.py      # Category model
│   └── report.py        # Report generation logic
├── utils/               # Utility functions
│   └── report_utils.py  # Functions for reports and plots
└── budget_tracker.db    # SQLite database (auto-generated)
```

---

## Sample Usage
1. **Add Category**:
   - Input: `Entertainment`
2. **Add Transaction**:
   - Input: `400, income, 1 (Salary), "Paycheck", 2024-12-30`
3. **View Transactions**:
   - Output:
     ```
     (1, 400, 'income', 'Salary', 'Paycheck', '2024-12-30')
     ```
4. **Calculate Balance**:
   - Output:
     ```
     Current Balance: $400
     ```
5. **Plot Balance Over Time**:
   - Generates a `balance_plot.png` file and displays the graph.

---




