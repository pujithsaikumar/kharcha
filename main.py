expenses = []
 
def add_expense():
    amount = float(input("Enter amount: "))
    category = input("Enter category (food/transport/shopping): ")
    description = input("Enter description: ")
    expenses.append({"amount": amount, "category": category, "description": description})
    print(f"Added ₹{amount} for {category}!\n")
 
def view_expenses():
    if not expenses:
        print("No expenses yet!\n")
        return
    print("\n--- YOUR EXPENSES ---")
    for i, e in enumerate(expenses, 1):
        print(f"{i}. ₹{e['amount']} | {e['category']} | {e['description']}")
    print()
 
def total():
    grand_total = sum(e["amount"] for e in expenses)
    print(f"\nTotal spent: ₹{grand_total}\n")
 
while True:
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total")
    print("4. Exit")
 
    choice = input("Choose: ")
 
    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        total()
    elif choice == "4":
        print("Bye!")
        break
    else:
        print("Invalid choice!\n")