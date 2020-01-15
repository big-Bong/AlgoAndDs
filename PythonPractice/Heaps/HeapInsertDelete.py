class TreeNode:
	def __init__(self,val):
		self.left = None
		self.right = None
		self.val = val


def insert(root,val):
	queue = [root]
	parent = []
	node = None
	while(True):
		node = queue.pop(0)
		if(not node.left):
			node.left = TreeNode(val)
			break

		if(not node.right):
			node.right = TreeNode(val)
			break

		queue.append(node.left)
		queue.append(node.right)
		parent.append(node)

	
	child = node.right if(node.right) else node.left
	bubble_up(root,node,parent,child)

def bubble_up(root,node,parent,child):
	if(node.val <= child.val):
		return

	node_pos = -1
	for i,elem in enumerate(parent):
		if(elem.val == node.val):
			node_pos = i

	temp = node
	node = child
	child = temp

	parent_pos = (node_pos - 2)//2
	if(parent_pos <= 0):
		return
	elif(parent[parent_pos].right == temp):
		bubble_up(root,parent[parent_pos],parent,parent[parent_pos].right)
	else:
		parent_pos = (node_pos - 1)//2
		bubble_up(root,parent[parent_pos],parent,parent[parent_pos].left)

def printHeap(root):
	queue = [root]
	
	while(queue):
		node = queue.pop(0)
		print(node.val,end=" ")

		if(node.left):
			queue.append(node.left)
		if(node.right):
			queue.append(node.right)


root = TreeNode(5)
insert(root,6)
insert(root,8)
insert(root,7)
insert(root,9)
insert(root,10)
printHeap(root)









