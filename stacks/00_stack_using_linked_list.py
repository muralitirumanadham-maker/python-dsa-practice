class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class stack:
    def __init__(self,value):
        new_node=Node(value)
        self.top=new_node
        self.height=1

    def push(self,value):
        new_node=Node(value)
        if self.height==0:
            self.top=new_node
        else:
            new_node.next=self.top
            self.top=new_node
        self.height+=1

    def pop(self):
        temp=self.top
        if self.top is None:
            return self.top
        self.top=self.top.next
        temp.next=None
        self.height-=1
        return temp.value

    def print_stack(self):
        temp=self.top
        while temp is not None:
            print(f"[{temp.value}]")
            if temp.next is not None:
                print(" ↓")
            temp=temp.next
print("pushing elements into stack:")
print("_______________")
my_stack=stack(1)
my_stack.push(2)
my_stack.push(3)
my_stack.print_stack()
print("_______________")
print("popping an element in the stack:")
print("_______________")
print(my_stack.pop())
print("_______________")
print("The final stack is:")
print("_______________")
my_stack.print_stack()
print("_______________")
