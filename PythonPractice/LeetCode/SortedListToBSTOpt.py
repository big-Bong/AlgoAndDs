# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
	def __init__(self,head):
		self.__curr = head
	def sortedListToBST(self, head):
		if(not head):
			return

		if(not head.next):
			return TreeNode(head.val)

		length = 0
		while(head):
			head = head.next
			length += 1

		return self.createBST(length)

	def createBST(self,length):
		if(length <= 0):
			return

		leftNode = self.createBST(int(length/2))
		root = TreeNode(self.__curr.val)
		root.left = leftNode
		self.__curr = self.__curr.next
		root.right = self.createBST(length - int(length/2) -1)

		return root

def printInorder(node):
    if(not node):
        return

    printInorder(node.left)
    print(node.val)
    printInorder(node.right)

head = ListNode(-10)
head.next = ListNode(-3)
head.next.next = ListNode(0)
head.next.next.next = ListNode(5)
head.next.next.next.next = ListNode(9)

sol = Solution(head)
printInorder(sol.sortedListToBST(head))