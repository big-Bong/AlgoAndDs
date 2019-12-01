# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        if(not nums):
            return
        
        return self.createBST(0,len(nums)-1,nums)
    
    def createBST(self,leftIndex,rightIndex,nums):
        if(leftIndex>rightIndex):
            return
        midIndex = self.mid(leftIndex,rightIndex)
        root = TreeNode(nums[midIndex])
        root.left = self.createBST(leftIndex,midIndex-1,nums)
        root.right = self.createBST(midIndex+1,rightIndex,nums)
        
        return root
    
    def mid(self,leftIndex,rightIndex):
        mid = leftIndex + (rightIndex-leftIndex)/2
        return int(mid)

def printInorder(node):
    if(not node):
        return

    printInorder(node.left)
    print(node.val)
    printInorder(node.right)

nums = [-10,-3, 0, 5, 9]

sol = Solution()
printInorder(sol.sortedArrayToBST(nums))