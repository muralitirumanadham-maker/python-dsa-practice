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
    
    def partition_list(self,x):
        if self.length==0:
            return None
        if self.length==1:
            return self.head
        dummy1=Node(0)
        dummy2=Node(0)
        left=dummy1
        right=dummy2
        current=self.head
        while current:
            nxt=current.next
            current.next=None
            current.prev=None
            if current.value<x:
                left.next=current
                current.prev=left
                left=current
            else:
                right.next=current
                current.prev=right
                right=current
            current=nxt
        if dummy1.next:
            self.head=dummy1.next
            self.head.prev=None
            left.next=dummy2.next
            if dummy2.next:
                dummy2.next.prev=left
        else:
            self.head=dummy2.next
            if self.head:
                self.head.prev=None
        self.tail=right if dummy2.next else left
        return self.head
    

dll = doublyll(3)
dll.append(8)
dll.append(5)
dll.append(10)
dll.append(2)
dll.append(1)

print("Before partitioning the list:")
dll.print_list()

x = 3
dll.partition_list(x)

print(f"After partitioning the list around {x}:")
dll.print_list()





        
