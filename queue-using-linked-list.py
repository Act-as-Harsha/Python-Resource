# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Queue class using Linked List
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    # Enqueue: Add element to the rear
    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            # If queue is empty, both front and rear are the new node
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        print(f"{data} added to the queue.")

    # Dequeue: Remove element from the front
    def dequeue(self):
        if self.front is None:
            print("Queue is empty! Cannot dequeue.")
            return
        removed_data = self.front.data
        self.front = self.front.next
        if self.front is None:  # If queue becomes empty
            self.rear = None
        print(f"{removed_data} removed from the queue.")

    # Display the queue
    def display(self):
        if self.front is None:
            print("The queue is empty.")
            return
        print("Queue elements (front → rear):", end=" ")
        current = self.front
        while current:
            print(current.data, end=" → ")
            current = current.next
        print("None")


# --- Main Program ---
if __name__ == "__main__":
    queue = Queue()

    print("Queue using Linked List")
    print("Choose an operation:")
    print("1. Enqueue (Add element)")
    print("2. Dequeue (Remove element)")
    print("3. Display Queue")
    print("4. Exit")

    while True:
        choice = input("\nEnter your choice (1-4): ")

        if choice == '1':
            value = input("Enter value to enqueue: ")
            if value.isdigit() or (value.startswith('-') and value[1:].isdigit()):
                queue.enqueue(int(value))
            else:
                print("Please enter a valid number.")

        elif choice == '2':
            queue.dequeue()

        elif choice == '3':
            queue.display()

        elif choice == '4':
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")
