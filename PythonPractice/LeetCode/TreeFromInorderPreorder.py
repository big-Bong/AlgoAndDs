#Definition for a binary tree node.

class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        if(not inorder):
            return
        
        elem = preorder[0]
        preorder.remove(elem)
        ind = inorder.index(elem)
        
        root = TreeNode(inorder[ind])
        root.left = self.buildTree(preorder,inorder[:ind])
        root.right = self.buildTree(preorder,inorder[ind+1:])
        
        return root

def printInorder(node):
	if(not node):
		return

	printInorder(node.left)
	print(node.val)
	printInorder(node.right)

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]

sol = Solution()
printInorder(sol.buildTree(preorder,inorder))