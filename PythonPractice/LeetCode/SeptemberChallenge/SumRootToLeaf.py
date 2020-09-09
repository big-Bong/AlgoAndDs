class Tree:
	def __init__(self,val):
		self.val = val
		self.left = None
		self.right = None

def sumRootToLeaf(root):
	num = ""
	sum = 0
	return preorderSum(root,num,sum)

def preorderSum(root,num,sum):
	if(not root):
		return sum
	if(not root.left and not root.right):
		num += str(root.val)
		sum += int(num,2)
		return sum

	num += str(root.val)
	sum = preorderSum(root.left,num,sum)
	sum = preorderSum(root.right,num,sum)

	return sum

root = Tree(0)
root.left = Tree(0)
root.left.left = Tree(0)
root.left.right = Tree(1)
root.right = Tree(1)
root.right.left = Tree(0)
root.right.right = Tree(1)

print(sumRootToLeaf(root))