'''
Inventory Management System

Nested dicts and grouped reporting
Manage a product inventory where each product has a name, quantity, price, and category. Support:
• Add a product
• Update a product's stock quantity
• Search by category
• Total inventory value (sum of quantity × price across all products)
• Low-stock alerts (quantity below a threshold)
• A summary report grouped by category'''


inventory = {}
while True:
    print("\n1. Add Product")
    print("2. Update Stock")
    print("3. Search by Category")
    print("4. Total Inventory Value")
    print("5. Low Stock Alert")
    print("6. Summary Report")
    print("7. Exit")
    choice = input("Enter your choice: ")
    
    if choice == "1":
        name = input("Enter product name: ")
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price: "))
        category = input("Enter category: ")
        inventory[name] = {
            "quantity": quantity,
            "price": price,
            "category": category
        }
        print("Product added successfully.")

    # Update stock
    elif choice == "2":
        name = input("Enter product name: ")
        if name in inventory:
            quantity = int(input("Enter new quantity: "))
            inventory[name]["quantity"] = quantity
            print("Stock updated successfully.")
        else:
            print("Product not found.")

    # Search by category
    elif choice == "3":
        category = input("Enter category: ")
        found = False
        for name, product in inventory.items():
            if product["category"].lower() == category.lower():
                print(name, product)
                found = True
        if not found:
            print("No products found in this category.")

    # Total inventory value
    elif choice == "4":
        total = 0
        for product in inventory.values():
            total += product["quantity"] * product["price"]

        print("Total inventory value:", total)

    # Low stock alert
    elif choice == "5":
        threshold = int(input("Enter stock threshold: "))
        for name, product in inventory.items():
            if product["quantity"] < threshold:
                print(
                    "Low Stock:",
                    name,
                    "- Quantity:",
                    product["quantity"]
                )

    # Summary report grouped by category
    elif choice == "6":
        summary = {}
        for name, product in inventory.items():
            category = product["category"]
            if category not in summary:
                summary[category] = {
                    "products": 0,
                    "quantity": 0,
                    "value": 0
                }

            summary[category]["products"] += 1
            summary[category]["quantity"] += product["quantity"]
            summary[category]["value"] += (
                product["quantity"] * product["price"]
            )

        for category, data in summary.items():
            print("\nCategory:", category)
            print("Products:", data["products"])
            print("Total Quantity:", data["quantity"])
            print("Total Value:", data["value"])

    # Exit
    elif choice == "7":
        print("Exiting...")
        break

    else:
        print("Invalid choice.")