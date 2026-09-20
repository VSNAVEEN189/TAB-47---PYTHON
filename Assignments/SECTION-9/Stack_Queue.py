'''Stack & Queue Implementation
Modeling data structures with lists
Implement two classic data structures using Python lists, exposed through a menu:
• Stack (Last-In-First-Out): push, pop, peek
• Queue (First-In-First-Out): enqueue, dequeue, peek
The program should keep running and maintain its state until the user chooses to exit. Handle empty-structure cases gracefully (e.g. popping from an empty stack).'''

print("===== STACK & QUEUE =====")
stack = []
queue = []
while True:
    print("\n1. Stack")
    print("2. Queue")
    print("3. Exit")
    choice = input("Enter your choice: ")

    # STACK
    if choice == "1":
        while True:
            print("\n===== STACK MENU =====")
            print("1. Push")
            print("2. Pop")
            print("3. Peek")
            print("4. Back")
            stack_choice = input("Enter your choice: ")

            # Push
            if stack_choice == "1":
                value = input("Enter value: ")
                stack.append(value)
                print("Added:", value)

            # Pop
            elif stack_choice == "2":
                if len(stack) == 0:
                    print("Stack is empty!")
                else:
                    removed = stack.pop()
                    print("Removed:", removed)

            # Peek
            elif stack_choice == "3":
                if len(stack) == 0:
                    print("Stack is empty!")
                else:
                    print("Top:", stack[-1])

            # Back
            elif stack_choice == "4":
                break
            else:
                print("Invalid choice!")


    # QUEUE
    elif choice == "2":
        while True:
            print("\n===== QUEUE MENU =====")
            print("1. Enqueue")
            print("2. Dequeue")
            print("3. Peek")
            print("4. Back")
            queue_choice = input("Enter your choice: ")

            # Enqueue
            if queue_choice == "1":
                value = input("Enter value: ")
                queue.append(value)
                print("Added:", value)

            # Dequeue
            elif queue_choice == "2":
                if len(queue) == 0:
                    print("Queue is empty!")
                else:
                    removed = queue.pop(0)
                    print("Removed:", removed)

            # Peek
            elif queue_choice == "3":
                if len(queue) == 0:
                    print("Queue is empty!")
                else:
                    print("Front:", queue[0])

            # Back
            elif queue_choice == "4":
                break
            else:
                print("Invalid choice!")


    # Exit
    elif choice == "3":
        print("Program ended.")
        break
    else:
        print("Invalid choice!")