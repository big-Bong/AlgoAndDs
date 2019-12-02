# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        curr = l3 = ListNode(0)
        carry = 0
        while(l1 or l2):
            if(not l1):
                val = carry+l2.val
                l2 = l2.next
            elif(not l2):
                val = carry+l1.val
                l1 = l1.next
            else:
                val = carry+l1.val+l2.val
                l1 = l1.next
                l2 = l2.next
            
            carry,num = divmod(val,10)
            
            curr.val = num
            if(l1 or l2 or (carry != 0)):
                curr.next = ListNode(carry)
                curr = curr.next
         
        return l3

l1 = ListNode(5)
#l1.next = ListNode(4)
#l1.next.next = ListNode(3)

l2 = ListNode(5)
#l2.next = ListNode(6)
#l2.next.next = ListNode(4)

sol = Solution()
l3 = sol.addTwoNumbers(l1,l2)

while(l3):
    print(l3.val)
    l3 = l3.next