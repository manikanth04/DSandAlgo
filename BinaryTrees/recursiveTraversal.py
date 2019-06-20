#!/usr/bin/env python



class Node: 
      
    # Constructor to create a new node 
    def __init__(self, data): 
        self.data = data  
        self.left = None
        self.right = None

def recursiveTraversal(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    ls=recursiveTraversal(root.left)
    print ("ls",ls)
    rs=recursiveTraversal(root.right)
    print ("rs",rs)
    #print ls+rs+1


root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.right.left = Node(4) 
root.right.right = Node(5)
root.right.left.right=Node(6)

recursiveTraversal(root)
