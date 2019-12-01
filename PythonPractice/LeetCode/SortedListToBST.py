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
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if(not head):
            return
        if(not head.next):
            return TreeNode(head.val)
        curr = head
        length = 0
        while(curr):
            curr = curr.next
            length += 1
        
        mid = int(length/2)
        curr = head.next
        trail = head
        length = 1
        while(length<mid):
            curr = curr.next
            trail = trail.next
            length += 1
        
        root = TreeNode(curr.val)
        curr = curr.next
        trail.next = None
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(curr)
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

sol = Solution()
printInorder(sol.sortedListToBST(head))
