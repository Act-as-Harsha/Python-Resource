# Define a Node class
class Node:
    def __init__(self, data):
        self.data = data      # store data
        self.next = None      # store reference to next node


# Define a LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None      # head of the list

    # Function to add a new node at the end
    def append(self, data):
        new_node = Node(data)

        # If list is empty, new node becomes head
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:  # move to the last node
                current = current.next
            current.next = new_node

    # Function to display the linked list
    def display(self):
        current = self.head
        if current is None:
            print("Linked List is empty!")
            return
        print("Linked List elements:")
        while current:
            print(current.data, end=" → ")
            current = current.next
        print("None")  # end of list indicator


# --- Main Program ---
my_list = LinkedList()

print("Create your linked list:")
while True:
    value = input("Enter a number to add (or type 'done' to finish): ")
    if value.lower() == 'done':
        break
    my_list.append(int(value))

print("\nYour final linked list:")
my_list.display()
