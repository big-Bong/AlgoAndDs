class TreeNode:
	def __init__(self,val=0,left=None,right=None):
		self.val = val
		self.left = left
		self.right = right

def isSameTree(p,q):
	stack1 = [p]
	stack2 = [q]

	while(stack1 and stack2):
		temp1 = stack1.pop()
		temp2 = stack2.pop()

		if(temp1 == None and temp2 == None):
			continue
		if((temp1 == None and temp2 != None) or (temp1 != None and temp2 == None)):
			return False
		if(temp1.val != temp2.val):
			return False

		stack1.append(temp1.left)
		stack1.append(temp1.right)
		stack2.append(temp2.left)
		stack2.append(temp2.right)

	if(stack1 or stack2):
		return False

	return True


root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(2)
#root1.left.left = TreeNode(4)
#root1.left.right = TreeNode(5)
#root1.right.left = TreeNode(6)
#root1.right.right = TreeNode(7)
root2 = TreeNode(1)
root2.left = TreeNode(2)
#root2.right = TreeNode(3)
root2.left.left = TreeNode(2)
#root2.left.right = TreeNode(5)
#root2.right.left = TreeNode(7)
#root2.right.right = TreeNode(6)
print(isSameTree(root1,root2))
#print(isSameTree(root1,root2))