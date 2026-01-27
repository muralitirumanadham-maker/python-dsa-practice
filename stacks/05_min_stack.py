class Minstack:
    def __init__(self):
        self.stack=[]
        self.min_stack=[]

    def push(self,val:int)->None:
        self.stack.append(val)
        if not self.min_stack or val<=self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self)->None:
        if self.stack[-1]==self.min_stack[-1]:
            self.min_stack.pop()
        self.stack.pop()

    def top(self)->int:
        return self.stack[-1]
    
    def get_min(self)->int:
        return self.min_stack[-1]
    
obj = Minstack()

print("MinStack Operations")
print("1. push")
print("2. pop")
print("3. top")
print("4. getMin")
print("5. exit")

while True:
    choice = int(input("\nEnter your choice: "))

    if choice == 1:
        value = int(input("Enter value to push: "))
        obj.push(value)
        print("Pushed:", value)

    elif choice == 2:
        obj.pop()
        print("Pop operation done")

    elif choice == 3:
        print("Top element:", obj.top())

    elif choice == 4:
        print("Minimum element:", obj.get_min())

    elif choice == 5:
        print("Exiting program")
        break

    else:
        print("Invalid choice")

    print("Stack:", obj.stack)
    print("Min Stack:", obj.min_stack)
