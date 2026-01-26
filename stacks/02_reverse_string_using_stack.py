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
    

def reversed_string(string):
    stack=Stack()
    for ch in string:
        stack.push(ch)
    reverse_string=""
    while not stack.isEmpty():
        reverse_string+=stack.pop()
    return reverse_string


my_string =input("Enter the word to be reverse:")

print ( reversed_string(my_string) )
