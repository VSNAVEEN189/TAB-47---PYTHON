'''Expense Tracker with Persistence
You'll practice
JSON persistence across program runs
Build a menu-driven expense tracker that survives restarts by saving to a JSON file. Support:
• Add an expense (amount, category, note)
• View all expenses
• View expenses by category
• Show total spending
• Save & exit (write to the JSON file)

On startup, load existing expenses from the file if it exists.

Example:
> add 250 Food "lunch"
> add 1200 Travel "cab"
> total   -> Rs 1450
> exit    -> saved to expenses.json
(run the program again)
-> previous expenses are still there'''


import json

expenses = []

try:
    with open("expenses.json", "r") as file:
        expenses = json.load(file)
except:
    expenses = []


while True:
    print("\nExpense Tracker")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View By Category")
    print("4. Show Total Spending")
    print("5. Save & Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amount = float(input("Enter amount: "))
        category = input("Enter category: ")
        note = input("Enter note: ")

        expense = {
            "amount": amount,
            "category": category,
            "note": note
        }

        expenses.append(expense)

        print("Expense added.")

    elif choice == "2":
        if len(expenses) == 0:
            print("No expenses found.")
        else:
            for expense in expenses:
                print(
                    "Amount:", expense["amount"],
                    "| Category:", expense["category"],
                    "| Note:", expense["note"]
                )

    elif choice == "3":
        category = input("Enter category: ")

        found = False

        for expense in expenses:
            if expense["category"].lower() == category.lower():
                print(
                    "Amount:", expense["amount"],
                    "| Note:", expense["note"]
                )
                found = True

        if found == False:
            print("No expenses found in this category.")

    elif choice == "4":
        total = 0

        for expense in expenses:
            total = total + expense["amount"]

        print("Total spending: Rs", total)

    elif choice == "5":
        with open("expenses.json", "w") as file:
            json.dump(expenses, file, indent=4)

        print("Expenses saved.")
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")