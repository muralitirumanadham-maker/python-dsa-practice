class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        self.prev=None

class doublyll:
    def __init__(self,value):
        new_node=Node(value)
        self.head=new_node
        self.tail=new_node
        self.length=1

    def print_list(self):
        temp=self.head
        while temp is not None:
            print(temp.value, end="")
            if temp.next is not None:
                print("->", end="")
            temp=temp.next
        print()


    def append(self,value):
        new_node=Node(value)
        if self.length==0:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            new_node.prev=self.tail
            self.tail=new_node
        self.length+=1
        return True
    
    def palindrome(self):
        if self.length==0:
            return None
        if self.length==1:
            return True
        forward=self.head
        backward=self.tail
        while forward is not None and backward is not None:
            if forward.value!=backward.value:
                return "Not palindrome"
            if forward==backward or forward.prev==backward:
                break
            forward=forward.next
            backward=backward.prev
        return "Palindrome"
    

dll = doublyll(1)
dll.append(2)
dll.append(4)
dll.append(2)
dll.append(1)

dll.print_list()
print(f" is {dll.palindrome()}")



        

