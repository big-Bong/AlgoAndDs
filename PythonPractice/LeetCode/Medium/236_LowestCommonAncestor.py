class Tree:
	def __init__(self,val):
		self.val = val
		self.left = None
		self.right = None

def ancestor(root,p,q):
	if(root == None or p == None or q == None or not cover(root,p) or not cover(root,q)):
		return None
	if(cover(p,q)):
		return p.val
	if(cover(q,p)):
		return q.val
	return ancestorHelper(root,p,q)

def ancestorHelper(root,node1,node2):
	if(not root or not node1 or not node2):
		return None
	pLeft = cover(root.left,node1) and cover(root.left,node2)
	pRight = cover(root.right,node1) and cover(root.right,node2)
	
	if(pLeft):
		return ancestorHelper(root.left,node1,node2)
	if(pRight):
		return ancestorHelper(root.right,node1,node2)

	return root.val

def cover(node1,node2):
	if(not node1):
		return False
	if(node1.val == node2.val):
		return True
	return (cover(node1.left,node2) or cover(node1.right,node2))

def inorder(root):
	if(root):
		inorder(root.left)
		print(root.val,end = " ")
		inorder(root.right)


root = Tree(6)
root.left = Tree(5)
root.left.left = Tree(-5)
root.left.left.right = Tree(0)
root.left.right = Tree(16)
root.left.right.left = Tree(1)
root.right = Tree(10)
root.right.left = Tree(-3)
root.right.left.left = Tree(2)
root.right.left.left.left = Tree(4)
root.right.left.right = Tree(15)
root.right.left.right.left = Tree(3)
root.right.left.right.right = Tree(9)
root.right.right = Tree(7)
root.right.right.left = Tree(11)
root.right.right.left.right = Tree(8)


print(ancestor(root,root.left.right.left,root.right))