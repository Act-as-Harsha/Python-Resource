def menu():
    print("\nStack Operations Menu:")
    print("1. Push (Add item)")
    print("2. Pop (Remove item)")
    print("3. Peek (Top item)")
    print("4. Check if stack is empty")
    print("5. Display stack")
    print("6. Exit")

stack = []

while True:
    menu()
    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        item = input("Enter item to push: ")
        stack.append(item)
        print(f"'{item}' pushed onto the stack.")

    elif choice == '2':
        if stack:
            removed = stack.pop()
            print(f"Popped item: {removed}")
        else:
            print("Stack is empty, nothing to pop.")

    elif choice == '3':
        if stack:
            print(f"Top item: {stack[-1]}")
        else:
            print("Stack is empty.")

    elif choice == '4':
        if not stack:
            print("Stack is empty.")
        else:
            print("Stack is not empty.")

    elif choice == '5':
        if stack:
            print("Current stack (top at right):", stack)
        else:
            print("Stack is empty.")

    elif choice == '6':
        print("Exiting program.")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 6.")