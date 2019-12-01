#Definition for a binary tree node.

class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def buildTree(self, inorder, postorder):
        if(not inorder):
            return
        
        dict = {}
        for ind, elem in enumerate(inorder):
            dict[elem] = ind

        return self.buildUsingDictionary(inorder,0,len(inorder)-1,postorder,0,len(postorder)-1,dict)

    def buildUsingDictionary(self,inorder,iLeft,iRight,postorder,pLeft,pRight,dict):

        if(pLeft>pRight or iLeft>iRight):
            return

        root = TreeNode(postorder[pRight])
        ind = dict[postorder[pRight]]

        root.right = self.buildUsingDictionary(inorder,ind+1,iRight,postorder,pRight-iRight+ind,pRight-1,dict)
        root.left = self.buildUsingDictionary(inorder,iLeft,ind-1,postorder,pLeft,pRight-iRight+ind-1,dict)

        return root


def printInorder(node):
	if(not node):
		return

	printInorder(node.left)
	print(node.val)
	printInorder(node.right)

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]

sol = Solution()
printInorder(sol.buildTree(inorder,postorder))