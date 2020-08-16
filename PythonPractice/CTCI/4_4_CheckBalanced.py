class Tree:
	def __init__(self,num):
		self.val = num
		self.left = None
		self.right = None

def checkBalanced(root):
	if(not root):
		return False

	val = calculateHeight(root)
	if(val == -1):
		return False
	return True

def calculateHeight(root):
	if(not root):
		return 0

	l_height = calculateHeight(root.left)
	r_height = calculateHeight(root.right)

	if(l_height == -1 or r_height == -1):
		return -1

	diff_val = abs(l_height - r_height)
	if(diff_val > 1):
		return -1
	
	return 1+max(l_height,r_height)

root = Tree(1)
root.left = Tree(2)
root.right = Tree(3)
root.left.left = Tree(4)
root.left.right = Tree(5)
#root.right.left = Tree(6)
root.right.right = Tree(7)
root.left.left.left = Tree(0)

print(checkBalanced(root))