class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

def buildTree(val):
	queue = []
	root = Node(val[0])
	queue.append(root)
	i = 1
	while i < len(val):
		currval = val[i]
		currNode = queue[0]
		queue.pop(0)
		if currNode.left == None:
			currNode.left = Node(currval)
			queue.append(currNode.left)
		i = i + 1
		if i >= len(val):
			break
		currval = val[i]
		if currNode.right == None:
			currNode.right = Node(currval)
			queue.append(currNode.right)
		i = i + 1
	return root

def inorder(root):
	if root is None:
		return
	inorder(root.left)
	print(root.data, end = ' ')
	inorder(root.right)	

def preorder(root):
	if root is None:
		return
	print(root.data, end = ' ')
	preorder(root.left)
	preorder(root.right)

def postorder(root):
	if root is None:
		return
	postorder(root.left)
	postorder(root.right)
	print(root.data, end = ' ')

if __name__ == '__main__':
	root = buildTree([1,2,3,4,5,6])
	inorder(root)
	print()
	preorder(root)
	print()
	postorder(root)