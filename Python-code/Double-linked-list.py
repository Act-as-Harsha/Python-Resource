# Node class for a doubly linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


# Doubly Linked List class
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Append a new node at the end
    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            # If list is empty, the new node is the head
            self.head = new_node
        else:
            current = self.head
            while current.next:  # move to last node
                current = current.next
            current.next = new_node
            new_node.prev = current

    # Display the list forward
    def display_forward(self):
        if self.head is None:
            print("The doubly linked list is empty.")
            return
        print("Doubly Linked List (Forward):", end=" ")
        current = self.head
        while current:
            print(current.data, end=" ⇄ ")
            last = current  # save last node for backward print
            current = current.next
        print("None")

    # Display the list backward
    def display_backward(self):
        if self.head is None:
            print("The doubly linked list is empty.")
            return
        print("Doubly Linked List (Backward):", end=" ")
        current = self.head
        # move to the last node
        while current.next:
            current = current.next
        # traverse backward
        while current:
            print(current.data, end=" ⇄ ")
            current = current.prev
        print("None")


# --- Main Program ---
if __name__ == "__main__":
    dll = DoublyLinkedList()

    print("Enter numbers to add to the doubly linked list.")
    print("Type 'done' when you are finished.\n")

    while True:
        user_input = input("Enter a number: ")
        if user_input.lower() == 'done':
            break
        # Check for valid integer input
        if user_input.isdigit() or (user_input.startswith('-') and user_input[1:].isdigit()):
            dll.append(int(user_input))
        else:
            print("Please enter a valid number or 'done' to finish.")

    print("\nYour final doubly linked list:")
    dll.display_forward()
    dll.display_backward()
