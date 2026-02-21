import deque

def menu():
    print("\nQueue Operations Menu:")
    print("1. Enqueue (Add item)")
    print("2. Dequeue (Remove item)")
    print("3. Peek (Front item)")
    print("4. Check if queue is empty")
    print("5. Display queue")
    print("6. Exit")

queue = deque()

while True:
    menu()
    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        item = input("Enter item to enqueue: ")
        queue.append(item)
        print(f"'{item}' added to the queue.")

    elif choice == '2':
        if queue:
            removed = queue.popleft()
            print(f"Dequeued item: {removed}")
        else:
            print("Queue is empty, nothing to dequeue.")

    elif choice == '3':
        if queue:
            print(f"Front item: {queue[0]}")
        else:
            print("Queue is empty.")

    elif choice == '4':
        if not queue:
            print("Queue is empty.")
        else:
            print("Queue is not empty.")

    elif choice == '5':
        if queue:
            print("Current queue:", list(queue))
        else:
            print("Queue is empty.")

    elif choice == '6':
        print("Exiting program.")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 6.")
