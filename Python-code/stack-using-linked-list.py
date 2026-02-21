# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Stack class using Linked List
class Stack:
    def __init__(self):
        self.top = None  # top of the stack

    # Push: add element to the top
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        print(f"{data} pushed onto the stack.")

    # Pop: remove element from the top
    def pop(self):
        if self.top is None:
            print("Stack is empty! Cannot pop.")
            return
        removed_data = self.top.data
        self.top = self.top.next
        print(f"{removed_data} popped from the stack.")

    # Peek: view top element
    def peek(self):
        if self.top is None:
            print("Stack is empty.")
        else:
            print(f"Top element: {self.top.data}")

    # Display stack elements
    def display(self):
        if self.top is None:
            print("The stack is empty.")
            return
        print("Stack elements (top → bottom):", end=" ")
        current = self.top
        while current:
            print(current.data, end=" → ")
            current = current.next
        print("None")


# --- Main Program ---
if __name__ == "__main__":
    stack = Stack()

    print("Stack using Linked List")
    print("Choose an operation:")
    print("1. Push (Add element)")
    print("2. Pop (Remove element)")
    print("3. Peek (View top element)")
    print("4. Display Stack")
    print("5. Exit")

    while True:
        choice = input("\nEnter your choice (1-5): ")

        if choice == '1':
            value = input("Enter value to push: ")
            if value.isdigit() or (value.startswith('-') and value[1:].isdigit()):
                stack.push(int(value))
            else:
                print("Please enter a valid number.")

        elif choice == '2':
            stack.pop()

        elif choice == '3':
            stack.peek()

        elif choice == '4':
            stack.display()

        elif choice == '5':
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")
