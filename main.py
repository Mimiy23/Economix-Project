# main.py

from utils import add_expense, list_expenses

def main():
    print("Welcome to ECONOMIX - Your Personal Expense Tracker")

    while True:
        print("\nChoose an option:")
        print("1. Add Expense")
        print("2. List Expenses")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            amount = float(input("Enter the expense amount: "))
            description = input("Enter a brief description: ")
            add_expense(amount, description)
        
        elif choice == '2':
            list_expenses()
        
        elif choice == '3':
            print("Exiting ECONOMIX. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
