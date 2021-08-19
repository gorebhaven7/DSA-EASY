#User function Template for python3

def convert_expression(exp, i):
    #code here
    if i >= len(exp):
        return None
    
    root = Node(exp[i])
    i += 1
    if i < len(exp) and exp[i] is '?':
        root.left = convert_expression(exp,i+1)
    elif i < len(exp) and exp[i] is ':':
        root.right = convert_expression(exp,i+1)

    return root
    
#{ 
#  Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10000)

class Node: 
    def __init__(self, key): 
        self.data = key 
        self.left = None
        self.right = None
  
# Function to print the tree 
# in a pre-order traversal pattern 
def print_tree(root): 
    if not root: 
        return
    print(root.data, end=' ') 
    print_tree(root.left) 
    print_tree(root.right) 
  
# Driver Code 
if __name__ == "__main__": 

    tcs=int(input())
    for _ in range(tcs):
    	expression=input()
    	root_node=convert_expression(expression, 0) 
    	print_tree(root_node) 
    	print()
# } Driver Code Ends