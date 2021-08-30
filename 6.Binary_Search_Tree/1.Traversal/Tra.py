class Node:
	def __init__(self,val):
		self.left = None
		self.val = val
		self.right = None

def buildTree(root,key):
	if root is None:
		return Node(key)

	else:
		if root.val == key:
			return root
		elif key < root.val:
			root.left = buildTree(root.left,key)
		else:
			root.right = buildTree(root.right,key)

	return root

def inorder(root):
	if root is None:
		return

	inorder(root.left)
	print(root.val,end = " ")
	inorder(root.right)

l = [5,4,1,8,3,2,10,13,7]
root = Node(l[0])
for e in l:
	root = buildTree(root,e)
inorder(root)