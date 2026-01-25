class Node:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.prev=None
        self.next=None

class LRUCache:
    def __init__(self,capacity:int):
        self.capacity=capacity
        self.cache={}
        self.head=Node(0,0)
        self.tail=Node(0,0)
        self.head.next=self.tail
        self.tail.prev=self.head

    def remove(self,node):
        prev_node=node.prev
        next_node=node.next
        prev_node.next=next_node
        next_node.prev=prev_node

    def add_to_head(self,node):
        node.next=self.head.next
        node.prev=self.head
        self.head.next.prev=node
        self.head.next=node
    
    def get(self,key:int)->int:
        if key not in self.cache:
            return -1
        node=self.cache[key]
        self.remove(node)
        self.add_to_head(node)
        return node.value
    
    def put(self,key:int,value:int)->None:
        if key in self.cache:
            node=self.cache[key]
            node.value=value
            self.remove(node)
            self.add_to_head(node)
        else:
            new_node=Node(key,value)
            self.cache[key]=new_node
            self.add_to_head(new_node)
            if len(self.cache)>self.capacity:
                lru=self.tail.prev
                self.remove(lru)
                del self.cache[lru.key]

    def print_cache(self):
        temp=self.head.next
        print("cache state:",end=" ")
        while temp!=self.tail:
            print(f"[{temp.key}:{temp.value}]",end="<->")
            temp=temp.next
        print("TAIL")

# ---------------- DRIVER CODE ----------------

lru = LRUCache(2)

lru.put(1, 10)
lru.print_cache()

lru.put(2, 20)
lru.print_cache()

print("get(1):", lru.get(1))
lru.print_cache()

lru.put(3, 30)   # This should remove key 2
lru.print_cache()

print("get(2):", lru.get(2))  # Should return -1
print("get(3):", lru.get(3))
lru.print_cache()
