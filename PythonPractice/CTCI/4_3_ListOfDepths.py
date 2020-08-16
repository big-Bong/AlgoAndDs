class Tree:
	def __init__(self,num):
		self.val = num
		self.left = None
		self.right = None

class LL:
	def __init__(self,num):
		self.val = num
		self.next = None

def listOfDepths(root):
	if(not root):
		return []

	arr_lists = []
	head = ll_node = None
	queue = [(root,1)]
	oldDepth = 1

	while(queue):
		node, depth = queue.pop(0)

		if(node.left != None):
			queue.append((node.left,depth+1))
		if(node.right != None):
			queue.append((node.right,depth+1))

		if(depth != oldDepth):
			arr_lists.append(head)
			head = ll_node = LL(node.val)
			oldDepth = depth
		else:
			if(head == None):
				head = ll_node = LL(node.val)
			else:
				ll_node.next = LL(node.val)
				ll_node = ll_node.next

	arr_lists.append(head)

	return arr_lists


root = Tree(1)
root.left = Tree(2)
root.right = Tree(3)
root.left.left = Tree(4)
#root.left.right = Tree(5)
#root.right.left = Tree(6)
root.right.right = Tree(7)

arr_lists = listOfDepths(root)

for lists in arr_lists:
	while(lists != None):
		print(lists.val,end = " ")
		lists = lists.next
	print()