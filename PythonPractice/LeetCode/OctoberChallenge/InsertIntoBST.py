class TreeNode:
	def __init__(self,val=0,left=None,right=None):
		self.val = val
		self.left = left
		self.right = right

def insertIntoBST(root,val):
	if(not root):
		return TreeNode(val)

	temp = root
	while(True):
		if(val <= temp.val):
			if(not temp.left):
				temp.left = TreeNode(val)
				break
			else:
				temp = temp.left
		else:
			if(not temp.right):
				temp.right = TreeNode(val)
				break
			else:
				temp = temp.right

	return root

def inorderPrint(root):
	if(root):
		inorderPrint(root.left)
		print(root.val,end=" ")
		inorderPrint(root.right)

root = TreeNode(5,TreeNode(3,TreeNode(2),TreeNode(4)),TreeNode(10,TreeNode(7)))
val = 6
root = insertIntoBST(root,val)
inorderPrint(root)
print()


