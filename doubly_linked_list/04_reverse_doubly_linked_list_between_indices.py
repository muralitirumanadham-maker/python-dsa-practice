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

    def reverse_between(self, start_index, end_index):
        if self.length<=1 or start_index==end_index:
            return None
        dummy=Node(0)
        dummy.next=self.head
        self.head.prev=dummy
        prev=dummy
        for _ in range(start_index):
            prev=prev.next
        current=prev.next
        for _ in range(end_index-start_index):
            node_to_move=current.next
            current.next=node_to_move.next
            if node_to_move.next:
                node_to_move.next.prev=current
            node_to_move.next=prev.next
            prev.next.prev=node_to_move
            prev.next=node_to_move
            node_to_move.prev=prev
        self.head=dummy.next
        self.head.prev=None
    

dll = doublyll(10)
dll.append(20)
dll.append(30)
dll.append(40)
dll.append(50)

print("Before reversing the list:")
dll.print_list()

start_index=1
end_index=3
dll.reverse_between(start_index,end_index)

print(f"After partitioning the list around the indexes {start_index} and {end_index} the list is:")
dll.print_list()





        
