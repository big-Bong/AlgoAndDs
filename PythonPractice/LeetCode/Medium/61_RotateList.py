class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

def rotateRight(head, k):
	if(not head):
		return None

	N = calculateLength(head)
	k = k%N
	if(k==0):
		return head

	fast_node = head
	slow_node = head
	for _ in range(k):
		fast_node = fast_node.next

	while(fast_node.next):
		slow_node = slow_node.next
		fast_node = fast_node.next

	temp = slow_node.next
	slow_node.next = None
	fast_node.next = head
	head = temp

	return head

def calculateLength(head):
	node = head
	N = 0
	while(node):
		node = node.next
		N += 1
	return N

def printNode(head):
	node = head
	while(node):
		print(node.val,end=" ")
		node = node.next
	print()


head = ListNode(0,ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5,ListNode(6,ListNode(7,ListNode(8,ListNode(9,ListNode(10,ListNode(11))))))))))))
printNode(rotateRight(head,4))