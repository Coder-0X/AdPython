# 💰 Expense Tracker Starter Code

expenses = []

def show_menu():
    print("\n--- EXPENSE TRACKER ---")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

def add_expense():
    # TODO: Ask user for 'item', 'amount', and 'date'
    # TODO: Store it in a dictionary and append to the 'expenses' list
    pass

def view_expenses():
    # TODO: Loop through the 'expenses' list and print each one nicely
    print("Not implemented yet!")

# Main Loop
while True:
    show_menu()
    choice = input("Choose an option (1-3): ")
    
    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again.")
