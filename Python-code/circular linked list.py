# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Circular Linked List class
class CircularLinkedList:
    def __init__(self):
        self.head = None

    # Add a new node at the end
    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            # First node points to itself
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head  # make it circular

    # Display the circular linked list
    def display(self):
        if self.head is None:
            print("The circular linked list is empty.")
            return

        print("Circular Linked List:", end=" ")
        current = self.head
        while True:
            print(current.data, end=" → ")
            current = current.next
            if current == self.head:
                break
        print("(back to head)")

# --- Main Program ---
if __name__ == "__main__":
    cll = CircularLinkedList()

    print("Enter numbers to add to the circular linked list.")
    print("Type 'done' when you are finished.\n")

    while True:
        user_input = input("Enter a number: ")
        if user_input.lower() == 'done':
            break
        # Check for valid integer input
        if user_input.isdigit() or (user_input.startswith('-') and user_input[1:].isdigit()):
            cll.append(int(user_input))
        else:
            print("Please enter a valid number or 'done' to finish.")

    print("\nYour final circular linked list:")
    cll.display()
