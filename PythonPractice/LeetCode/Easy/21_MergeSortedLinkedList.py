class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def mergeTwoLists(l1, l2):
    if(not l1 and not l2):
        return l1
    
    output = head3 = ListNode(None)
    
    while(l1 and l2):
        head3.next = ListNode(None)
        
        if(l1.val <= l2.val):
            head3.val = l1.val
            l1 = l1.next
        else:
            head3.val = l2.val
            l2 = l2.next
        
        head3 = head3.next
    
    if(l2 != None):
        head3.val = l2.val
        head3.next = l2.next
    if(l1 != None):
        head3.val = l1.val
        head3.next = l1.next
    
    return output


l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

l3 = mergeTwoLists(l1,l2)
while(l3):
    print(l3.val)
    l3 = l3.next