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
    
    def swap_pairs(self):
        if self.length<=1:
            return self.head
        dummy=Node(0)
        dummy.next=self.head
        self.head.prev=dummy
        prev=dummy
        while prev.next and prev.next.next:
            first=prev.next
            second=first.next

            first.next=second.next
            if second.next:
                second.next.prev=first

            second.next=first
            second.prev=prev
            first.prev=second
            prev.next=second
            prev=first
            self.head=dummy.next
            self.head.prev=None
    

dll = doublyll(1)
dll.append(2)
dll.append(3)
dll.append(4)
dll.append(5)

print("Before swapping the pairs:")
dll.print_list()

dll.swap_pairs()

print(f"After swapping the pairs:")
dll.print_list()





        
