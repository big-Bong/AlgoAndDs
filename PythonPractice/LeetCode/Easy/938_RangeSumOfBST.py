class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

def rangeSumBST(root, low, high):
	if(not root):
		return 0

	finalSum = rangeSumBSTHelper(root,low,high,0)
	return finalSum

def rangeSumBSTHelper(root,low,high,finalSum):
	if(root.val >= low and root.val <= high):
		finalSum += root.val
	if(root.left):
		finalSum = rangeSumBSTHelper(root.left,low,high,finalSum)
	if(root.right):
		finalSum = rangeSumBSTHelper(root.right,low,high,finalSum)

	return finalSum


root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right.right = TreeNode(18)

print(rangeSumBST(root,7,15))