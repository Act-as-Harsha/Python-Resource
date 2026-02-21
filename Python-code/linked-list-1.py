# Node class to store data and the next pointer
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Linked List class to manage nodes
class LinkedList:
    def __init__(self):
        self.head = None

    # Add a new node at the end of the list
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    # Display the linked list
    def display(self):
        if self.head is None:
            print("The linked list is empty.")
            return
        current = self.head
        print("Linked List:", end=" ")
        while current:
            print(current.data, end=" → ")
            current = current.next
        print("None")  # Indicates end of list


# --- Main Program ---
if __name__ == "__main__":
    linked_list = LinkedList()

    print("Enter numbers to add to the linked list.")
    print("Type 'done' when you are finished.\n")

    while True:
        user_input = input("Enter a number: ")
        if user_input.lower() == 'done':
            break
        # Check if user entered a number
        if user_input.isdigit() or (user_input.startswith('-') and user_input[1:].isdigit()):
            linked_list.append(int(user_input))
        else:
            print("Please enter a valid number or 'done' to finish.")

    print("\nYour final linked list:")
    linked_list.display()
