class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

def deleteDuplicates(head):
	if(not head):
		return None
	if(not head.next):
		return head

	node = head
	while(node):
		while(node.next and node.next.val == node.val):
			node.next = node.next.next
		node = node.next

	return head

def printList(head):
	node = head
	while(node):
		print(node.val,end=" ")
		node = node.next
	print()

head = ListNode(1,ListNode(1,ListNode(1)))
printList(head)
node = deleteDuplicates(head)
printList(node)