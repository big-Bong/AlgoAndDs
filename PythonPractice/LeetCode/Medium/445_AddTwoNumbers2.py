class ListNode:
	def __init__(self,val=0,next=None):
		self.val = val
		self.next = next

def addTwoNumbers(l1,l2):
	l1 = reverseList(l1)
	l2 = reverseList(l2)
	temp1 = None
	c = 0

	while(l1 and l2):
		val = l1.val + l2.val + c
		c,val = divmod(val,10)
		temp = ListNode(val)
		temp.next = temp1
		temp1 = temp
		l1 = l1.next
		l2 = l2.next

	(temp1,c) = append(l1,temp1,c)
	(temp1,c) = append(l2,temp1,c)

	if(c != 0):
		temp = ListNode(c)
		temp.next = temp1
		temp1 = temp

	return temp1

def append(l,temp1,c):
	while(l):
		val = l.val + c
		c,val = divmod(val,10)
		temp = ListNode(val)
		temp.next = temp1
		temp1 = temp
		l = l.next

	return (temp1,c)


def reverseList(l):
	temp2 = None
	temp1 = None
	while(l):	
		temp1 = ListNode(l.val)
		temp1.next = temp2
		l = l.next
		temp2 = temp1

	return temp1

def printList(l):
	while(l):
		print(l.val,end=" ")
		l = l.next

	print()


#l1 = ListNode(7,ListNode(2,ListNode(4,ListNode(3))))
#l2 = ListNode(5,ListNode(6,ListNode(4)))
l1 = ListNode(8,ListNode(9,ListNode(9)))
l2 = ListNode(2)
printList(addTwoNumbers(l1,l2))
