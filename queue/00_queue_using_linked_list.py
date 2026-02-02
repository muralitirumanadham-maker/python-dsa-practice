class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class queue:
    def __init__(self,value):
        new_node=Node(value)
        self.first=new_node
        self.second=new_node
        self.length=1

    def print_queue(self):
        if self.length == 0:
            print("Queue is empty")
            return

        temp = self.first
        print("FRONT -> ", end="")
        while temp:
            print(temp.value, end=" -> ")
            temp = temp.next
        print("REAR")

    def enqueue(self,value):
        new_node=Node(value)
        if self.length==0:
            self.first=new_node
            self.second=new_node
        else:
            self.second.next=new_node
            self.second=new_node
        self.length+=1
        return True
    
    def dequeue(self,value):
        if self.length==0:
            return None
        temp=self.first
        if self.length==1:
            self.first=None
            self.second=None
        else:
            self.first=self.first.next
            temp.next=None
        self.length-=1
        return temp
    
q = queue(int(input("Enter first value of queue: ")))

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
