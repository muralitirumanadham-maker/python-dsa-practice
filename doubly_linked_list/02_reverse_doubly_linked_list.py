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
                print("<->", end="")
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
    
    def reverse(self):
        if self.length==0:
            return None
        if self.length<=1:
            return True
        current=self.head
        while current is not None:
            current.next,current.prev=current.prev,current.next
            current=current.prev
        self.head,self.tail=self.tail,self.head
    

dll = doublyll(1)
dll.append(2)
dll.append(3)
dll.append(4)
dll.append(5)
print("Before reversing the list:")
dll.print_list()
dll.reverse()
print("After reversing the list:")
dll.print_list()




        
