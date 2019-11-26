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



root = BinaryTreeNode(1)
root.left = BinaryTreeNode(2)
root.right = BinaryTreeNode(3)
root.left.left = BinaryTreeNode(4)
root.left.right = BinaryTreeNode(5)

print("inorder")
inorder(root)
print("preorder")
preorder(root)
print("postorder")
postorder(root)