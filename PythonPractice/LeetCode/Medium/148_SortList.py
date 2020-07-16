class ListNode:
	def __init__(self,val = 0):
		self.val = val
		self.next = None

def sortList(head):
	if(not head or head.next == None):
		return head
	middle = findMiddle(head)
	nexttomiddle = middle.next
	middle.next = None

	left = sortList(head)
	right = sortList(nexttomiddle)
	return mergeList(left,right)

def findMiddle(head):
	slow = head
	fast = head
	while(fast.next != None and fast.next.next != None):
		slow = slow.next
		fast = fast.next.next

	return slow

def mergeList(left,right):
	finalList = None

	if(left == None):
		return right
	if(right == None):
		return left

	if(left.val <= right.val):
		finalList = left
		finalList.next = mergeList(left.next,right)
	else:
		finalList = right
		finalList.next = mergeList(left,right.next)

	return finalList


def printList(head):
	while(head != None):
		print(head.val)
		head = head.next

head = ListNode(4)
head.next = ListNode(2)
head.next.next = ListNode(1)
head.next.next.next = ListNode(3)
printList(head)
output = sortList(head)
print("==========================")
printList(output)