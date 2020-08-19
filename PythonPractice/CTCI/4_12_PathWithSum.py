class Tree:
	def __init__(self,val):
		self.val = val
		self.left = None
		self.right = None

def pathSumBF(node,sum):
	if(not node):
		return 0

	totalPath_root = pathSumBFHelper(node,sum,0)

	totalPath_root_left = pathSumBF(node.left,sum)
	totalPath_root_right = pathSumBF(node.right,sum)

	return totalPath_root+totalPath_root_left+totalPath_root_right

def pathSumBFHelper(node,sum,currentSum):
	if(not node):
		return 0

	totalPaths = 0
	currentSum += node.val
	if(currentSum == sum):
		totalPaths += 1

	totalPaths += pathSumBFHelper(node.left,sum,currentSum)
	totalPaths += pathSumBFHelper(node.right,sum,currentSum)

	return totalPaths


root = Tree(10)
root.left = Tree(5)
root.left.left = Tree(3)
root.left.left.left = Tree(3)
root.left.left.right = Tree(-2)
root.left.right = Tree(2)
root.left.right.right = Tree(1)
root.right = Tree(-3)
root.right.right = Tree(11)

print(pathSumBF(root,7))