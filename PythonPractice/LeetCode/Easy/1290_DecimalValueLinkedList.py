class ListNode:
	def __init__(self,val=0,next=None):
		self.val = val
		self.next = next

def getDecimalValue(head):
	if(not head):
		return None

	num = ""
	while(head):
		num += str(head.val)
		head = head.next

	return int(num,2)

#head = ListNode(1,ListNode(0,ListNode(1)))
#head = ListNode(1)
head = ListNode(1,ListNode(0,ListNode(1,ListNode(1,ListNode(1,ListNode(0))))))
print(getDecimalValue(head))