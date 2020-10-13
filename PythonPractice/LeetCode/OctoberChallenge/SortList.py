class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

def sortList(head):
	if(not head or not head.next):
		return head

	temp_arr = []
	N = 0
	while(head):
		temp_arr.append(head.val)
		N += 1
		head = head.next

	temp_arr.sort()
	head = ListNode(temp_arr[0])
	temp = head
	for i in range(1,N):
		temp.next = ListNode(temp_arr[i])
		temp = temp.next

	return head

head = ListNode(-1,ListNode(5,ListNode(3,ListNode(4,ListNode(0)))))
head = sortList(head)
while(head):
	print(head.val,end=" ")
	head = head.next
print()