#!/usr/bin/env python

from Queue import Queue

class Node: 
      
    # Constructor to create a new node 
    def __init__(self, data): 
        self.data = data  
        self.left = None
        self.right = None

def levelOrderTraversal(root):
    q=Queue()
    q.put(root)
    
    count=0
    #abc=q.empty()
    #print not(abc)
    while not(q.empty()):
        tmp=q.get()
        #print tmp
        count+=1
        #print (count)
        if tmp.left is not None:
            q.put(tmp.left)
        if tmp.right is not None:
            q.put(tmp.right)
    print(count)


root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.right.left = Node(4) 
root.right.right = Node(5)
root.right.left.right=Node(6)

levelOrderTraversal(root)
