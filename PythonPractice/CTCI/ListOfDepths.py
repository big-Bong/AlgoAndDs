class TreeNode:
	def __init__(self,x):
		self.val = x
		self.left = None
		self.right = None
class LinkedList:
	def __init__(self,x):
		self.val = x
		self.next = None

def levelOrder(root):
	if(not root):
		return
	
	arr = [root]
	output = []
	return levelOrderHelper(arr,1,output)

def levelOrderHelper(arr,counter,output):
	treenode = arr.pop(0)
	output.append(LinkedList(treenode.val))
	arr.append(treenode.left)
	arr.append(treenode.right)
	counter = 0
	initialCounter = 1
	start = None
	head = None
	while(len(arr) > 0):
		treenode = arr.pop(0)
		if(treenode != None):
			arr.append(treenode.left)
			arr.append(treenode.right)
			node = LinkedList(treenode.val)
			if(counter == 0):
				output.append(start)
				counter = initialCounter*2
				initialCounter = counter
				head = node
				start = head
			else:
				head.next = node
			counter -= 1
	return output