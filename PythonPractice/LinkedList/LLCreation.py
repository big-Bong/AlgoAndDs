class Node:
	def __init__(self,data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	def traversal(self):
		node = self.head
		while(node != None):
			print(node.data)
			node = node.next


n1 = Node(1)
n2 = Node(2)
n3 = Node(3)

llist = LinkedList()
llist.head = n1
n1.next = n2
n2.next = n3


llist.traversal()