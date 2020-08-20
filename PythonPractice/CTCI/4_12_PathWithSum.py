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

def pathSumOpt(root,currentSum):
	new_dict = {}
	return pathSumOptHelper(root,currentSum,0,new_dict)

def pathSumOptHelper(node,currentSum,runningSum,new_dict):
	if(not node):
		return 0

	runningSum += node.val
	totalPaths = 0
	diff_sum = runningSum - currentSum
	if(diff_sum in new_dict):
		totalPaths += new_dict[diff_sum]

	if(runningSum == currentSum):
		totalPaths += 1

	updateDictionary(new_dict,runningSum,1)
	totalPaths += pathSumOptHelper(node.left,currentSum,runningSum,new_dict)
	totalPaths += pathSumOptHelper(node.right,currentSum,runningSum,new_dict)
	updateDictionary(new_dict,runningSum,-1)

	return totalPaths

def updateDictionary(new_dict,runningSum,delta):
	new_count = 0
	if(runningSum in new_dict):
		new_count = new_dict[runningSum]

	new_count += delta
	if(new_count == 0):
		del new_dict[runningSum]
	else:
		new_dict[runningSum] = new_count



root = Tree(10)
root.left = Tree(5)
root.left.left = Tree(3)
root.left.left.left = Tree(3)
root.left.left.right = Tree(-2)
root.left.right = Tree(2)
root.left.right.right = Tree(1)
root.right = Tree(-3)
root.right.right = Tree(11)

print(pathSumOpt(root,8))