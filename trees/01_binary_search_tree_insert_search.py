class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

class BST:
    def __init__(self):
        self.root=None

    def insert(self,value):
        new_node=Node(value)
        if self.root==None:
            self.root=new_node
            return True
        temp=self.root
        while(True):
            if new_node.value==temp.value:
                return False
            if new_node.value<temp.value:
                if temp.left is None:
                    temp.left=new_node
                    return True
                temp=temp.left
            else:
                if temp.right is None:
                    temp.right=new_node
                    return True
                temp=temp.right

    def contains(self,value):
        temp=self.root
        while temp is not None:
            if value<temp.value:
                temp=temp.left
            elif value>temp.value:
                temp=temp.right
            else:
                return True
        return False
    
    def print_tree(self):
        self._print_tree(self.root, 0)

    def _print_tree(self, node, level):
        if node is not None:
            self._print_tree(node.right, level + 1)
            print("    " * level + str(node.value))
            self._print_tree(node.left, level + 1)


bst = BST()

n = int(input("Enter number of nodes: "))

print("Enter values:")
for _ in range(n):
    value = int(input())
    bst.insert(value)

print("\nBST Tree Structure:\n")
bst.print_tree()
