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
    

def stack_sort(stac):
    temp_stack=Stack()
    while not stack.isEmpty():
        temp=stack.pop()
        while(not temp_stack.isEmpty() and temp_stack.peek()>temp):
            stack.push(temp_stack.pop())
        temp_stack.push(temp)
    while not temp_stack.isEmpty():
        stack.push(temp_stack.pop())

stack = Stack()
stack.push(3)
stack.push(1)
stack.push(5)
stack.push(4)
stack.push(2)

print("Stack before sorting:")
stack.print_stack()

stack_sort(stack)

print("\nStack after sorting:")
stack.print_stack()




