# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
	def checkStack(self, nodeVal,stack):
		if(not stack):
			stack.append(nodeVal)
		elif(nodeVal == stack[len(stack)-1]):
			stack.pop()
		else:
			stack.append(nodeVal)

		return stack

	def isSymmetric(self, root: TreeNode) -> bool:
		queue = [root]
		stack = []
		
		while(True):
			if(not queue):
				break

			root = queue.pop(0)

			if(root.left):
				queue.append(root.left)
				nodeVal = root.left.val
				stack = self.checkStack(nodeVal,stack)
			else:
				nodeVal = None
				stack = self.checkStack(nodeVal,stack)

			if(root.right):
				queue.append(root.right)
				nodeval = root.right.val
				stack = self.checkStack(nodeVal,stack)
			else:
				nodeval = None
				stack = self.checkStack(nodeVal,stack)

		return (not stack)


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
#root.left.left = TreeNode(3)
root.left.right = TreeNode(3)
#root.right.left = TreeNode(4)
root.right.right = TreeNode(3)

sol = Solution()
print(sol.isSymmetric(root))