# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
	def isSymmetric(self, root: TreeNode) -> bool:

		if(root == None):
			return False

		queue = []
		queue.append(root)
		queue.append(root)

		while(queue):
			leftTree = queue.pop(0)
			rightTree = queue.pop(0)

			if(leftTree.val != rightTree.val):
				return False

			if((leftTree.left == None and rightTree.right == None)):
				pass
			elif(leftTree.left == None or rightTree.right == None):
				return False
			else:
				queue.append(leftTree.left)
				queue.append(rightTree.right)

			if((leftTree.right == None and rightTree.left == None)):
				pass
			elif(leftTree.right == None or rightTree.left == None):
				return False
			else:
				queue.append(leftTree.right)
				queue.append(rightTree.left)

		return True

		


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)

sol = Solution()
print(sol.isSymmetric(root))