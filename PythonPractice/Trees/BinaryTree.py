class BinaryTreeNode:
	def __init__(self,value):
		self.value = value
		self.left = None
		self.right = None
		

def inorder(root):
	if(root):
		inorder(root.left)
		print(root.value)
		inorder(root.right)

def preorder(root):
	if(root):
		print(root.value)
		preorder(root.left)
		preorder(root.right)

def postorder(root):
	if(root):
		postorder(root.left)
		postorder(root.right)
		print(root.value)

def levelOrderTraversal(root):
	queue = [root]

	while(True):
		if(not queue):
			break
		
		current = queue.pop(0)
		print(current.value)
		
		if(current.left):
			queue.append(current.left)
		if(current.right):
			queue.append(current.right)

def height(root):
	if(root == None):
		return 0

	lheight = height(root.left)
	rheight = height(root.right)

	if(lheight > rheight):
		return lheight+1
	else:
		return rheight+1



root = BinaryTreeNode(25)
root.left = BinaryTreeNode(15)
root.right = BinaryTreeNode(50)
root.left.left = BinaryTreeNode(10)
root.left.right = BinaryTreeNode(22)
root.left.left.left = BinaryTreeNode(4)
root.left.left.right = BinaryTreeNode(12)
root.left.right.left = BinaryTreeNode(18)
root.left.right.right = BinaryTreeNode(24)
root.right.left = BinaryTreeNode(35)
root.right.right = BinaryTreeNode(70)
root.right.left.left = BinaryTreeNode(31)
root.right.left.right = BinaryTreeNode(44)
root.right.right.left = BinaryTreeNode(66)
root.right.right.right = BinaryTreeNode(90)

print("Height of tree")
print(height(root))
"""
print("inorder")
inorder(root)
print("preorder")
preorder(root)
print("postorder")
postorder(root)
print("Level order")
levelOrderTraversal(root)
"""