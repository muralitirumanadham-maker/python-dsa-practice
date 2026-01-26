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
    

def is_balanced_paranthesis(string):
    stack=Stack()
    for ch in string:
        if ch=="(":
            stack.push(ch)
        elif ch==")":
            if stack.isEmpty():
                return False
            stack.pop()
    return stack.isEmpty()

my_string = input("Enter parentheses string: ")

result = is_balanced_paranthesis(my_string)

if result:
    print("✅ Balanced Parentheses")
else:
    print("❌ Not Balanced Parentheses")

