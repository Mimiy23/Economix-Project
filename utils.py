expenses = []

def add_expense(amount, description):
    expenses.append({"amount": amount, "description": description})
    print("Expense added successfully!")

def list_expenses():
    if not expenses:
        print("No expenses recorded yet.")
    else:
        print("List of Expenses:")
        for idx, expense in enumerate(expenses, start=1):
            print(f"{idx}. Amount: ${expense['amount']}, Description: {expense['description']}")
