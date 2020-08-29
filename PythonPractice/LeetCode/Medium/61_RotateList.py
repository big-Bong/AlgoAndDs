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

	node = head
	for _ in range(N-k-1):
		node = node.next

	new_node = node.next
	node.next = None
	arr = []
	while(new_node):
		arr.append(new_node)
		new_node = new_node.next

	for i in range(len(arr)-1,-1,-1):
		temp = arr[i]
		temp.next = head
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


head = ListNode(0,ListNode(1,ListNode(2)))
printNode(rotateRight(head,4))