class Tree:
	def __init__(self,val,parent):
		self.val = val
		self.left = None
		self.right = None
		self.parent = parent

def inorder(root):
	if(root):
		inorder(root.left)
		print(root.val)
		inorder(root.right)

def inorderSuccessor(node):
	if(not node):
		return None
	if(node.right):
		return inorderSuccessorHelper(node.right).val
	if(node.parent and node.val < node.parent.val):
		return node.parent.val
	if(node.parent and node.val > node.parent.val):
		while(node.parent):
			node = node.parent
			if(node.parent and node.val < node.parent.val):
				return node.parent.val

	return None


def inorderSuccessorHelper(node):
	if(node.left):
		return inorderSuccessorHelper(node.left)
	else:
		return node


root = Tree(8,None)
root.left = Tree(2,root)
root.right = Tree(17,root)
root.left.left = Tree(-1,root.left)
root.left.left.right = Tree(1,root.left.left)
root.left.right = Tree(5,root.left)
root.left.right.left = Tree(3,root.left.right)
root.left.right.right = Tree(7,root.left.right)
root.left.right.left.right = Tree(4,root.left.right.left)
root.right.left = Tree(12,root.right)
root.right.right = Tree(18,root.right)

print(inorderSuccessor(root.right.left))