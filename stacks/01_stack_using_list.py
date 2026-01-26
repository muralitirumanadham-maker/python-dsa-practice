class Stack:
    def __init__(self):
        self.stack_list=[]

    def print_stack(self):
        for i in range(len(self.stack_list)-1,-1,-1):
            print(f"[{self.stack_list[i]}]")
            if i!=0:
                print(" ↓")

    def push(self,value):
        self.stack_list.append(value)

    def isEmpty(self):
        return len(self.stack_list)==0
    
    def peek(self):
        if self.isEmpty():
            return None
        return self.stack_list[-1]
    
    def size(self):
        return len(self.stack_list)
    
    def pop(self):
        if self.isEmpty():
            return None
        return self.stack_list.pop()

my_stack = Stack()
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
my_stack.push(4)
my_stack.push(5)

print("After pushing the elements into the stack:")
print("__________")
my_stack.print_stack()
print("__________")

print("After popping an element from the stack:")
print("__________")
print(my_stack.pop())
print("__________")

print("Checking whether the stack is empty:")
print("__________")
print(my_stack.isEmpty())
print("__________")

print("Retrieving the top element of the stack:")
print("__________")
print(my_stack.peek())
print("__________")

print("Checking the size of the stack:")
print("__________")
print(my_stack.size())
print("__________")

print("Final stack is:")
print("__________")
my_stack.print_stack()
print("__________")






