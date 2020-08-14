class Tree:
	def __init__(self,num):
		self.val = num
		self.left = None
		self.right = None

def minimalTree(arr):
	if(not arr or len(arr) == 0):
		return None
	N = len(arr)
	if(N == 1):
		return Tree(arr[0])
	
	return minimalTreeHelper(arr,0,N-1)

def minimalTreeHelper(arr,start,end):
	root = None
	if(start<=end):
		mid = start + ((end-start)//2)
		root = Tree(arr[mid])
		root.left = minimalTreeHelper(arr,start,mid-1)
		root.right = minimalTreeHelper(arr,mid+1,end)
	return root

def printTree(root):
	if(root):
		printTree(root.left)
		print(root.val)
		printTree(root.right)

arr = [1,3,4,6,12,13,15,20]
root = minimalTree(arr)
printTree(root)

