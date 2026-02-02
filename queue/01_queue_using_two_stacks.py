class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def print_queue(self):
        if self.is_empty():
            print("Queue is empty")
            return

        print("FRONT -> ", end="")
        for i in range(len(self.stack1) - 1, -1, -1):
            print(self.stack1[i], end=" ")
        print("<- REAR")
        
    def enqueue(self, value):
        while len(self.stack1) > 0:
            self.stack2.append(self.stack1.pop())
        self.stack1.append(value)
        while len(self.stack2) > 0:
            self.stack1.append(self.stack2.pop())
            
    def dequeue(self):
        if self.is_empty():
            return None
        else:
            return self.stack1.pop()
            


    def peek(self):
        return self.stack1[-1]

    def is_empty(self):
        return len(self.stack1) == 0
q = MyQueue()

while True:
    print("\n1. Enqueue")
    print("2. Dequeue")
    print("3. Print Queue")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        val = int(input("Enter value to enqueue: "))
        q.enqueue(val)
        print("Enqueued successfully")

    elif choice == 2:
        removed = q.dequeue()
        if removed is None:
            print("Queue is empty")
        else:
            print("Dequeued value:", removed)

    elif choice == 3:
        print("Queue elements:")
        q.print_queue()

    elif choice == 4:
        print("Exiting...")
        break

    else:
        print("Invalid choice")
