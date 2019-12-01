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
        
        dict = {}
        for ind, elem in enumerate(inorder):
            dict[elem] = ind

        return self.buildUsingDictionary(preorder,0,len(preorder)-1,inorder,0,len(inorder)-1,dict)

    def buildUsingDictionary(self,preorder,pLeft,pRight,inorder,iLeft,iRight,dict):

        if(pLeft>pRight or iLeft>iRight):
            return

        root = TreeNode(preorder[pLeft])
        ind = dict[preorder[pLeft]]

        root.left = self.buildUsingDictionary(preorder,pLeft+1,pLeft+ind-iLeft,inorder,iLeft,ind-1,dict)
        root.right = self.buildUsingDictionary(preorder,pLeft+ind-iLeft+1,pRight,inorder,ind+1,iRight,dict)

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