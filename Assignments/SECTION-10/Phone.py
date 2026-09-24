'''Phone Book
You'll practice
Dictionary CRUD with a menu loop
Build a contact manager backed by a dictionary (name -> phone number). Offer a menu that loops until the user exits:
• Add a contact
• Search by name
• Delete a contact
• Show all contacts

Handle the "contact not found" case cleanly instead of crashing.'''

contacts = {}

while True:
    print("\n--- PHONE BOOK ---")
    print("1. Add contact")
    print("2. Search contact")
    print("3. Delete contact")
    print("4. Show all contacts")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter contact name: ")
        phone = input("Enter phone number: ")

        contacts[name] = phone
        print("Contact added successfully.")

    elif choice == "2":
        name = input("Enter name to search: ")

        if name in contacts:
            print(f"{name}: {contacts[name]}")
        else:
            print("Contact not found.")

    elif choice == "3":
        name = input("Enter name to delete: ")

        if name in contacts:
            del contacts[name]
            print("Contact deleted successfully.")
        else:
            print("Contact not found.")

    elif choice == "4":
        if len(contacts) == 0:
            print("Phone book is empty.")
        else:
            print("\n--- All Contacts ---")

            for name, phone in contacts.items():
                print(f"{name}: {phone}")

    elif choice == "5":
        print("Exiting Phone Book...")
        break

    else:
        print("Invalid choice. Please try again.")