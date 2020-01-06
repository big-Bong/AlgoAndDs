class LinkedList:
	def __init__(self,val):
		self.val = val
		self.next = None

class Graph:
	def __init__(self,numVertex):
		self.numVertex = numVertex
		self.graphList = [None]*numVertex

	def addEdge(self,vertex1,vertex2):
		if(self.graphList[vertex1] == None):
			self.graphList[vertex1] = LinkedList(vertex1)
		
		node = self.graphList[vertex1]
		while(node.next != None):
			node = node.next
		node.next = LinkedList(vertex2)

		if(self.graphList[vertex2] == None):
			self.graphList[vertex2] = LinkedList(vertex2)

		node = self.graphList[vertex2]
		while(node.next != None):
			node = node.next
		node.next = LinkedList(vertex1)

	def printGraph(self):
		for elem in self.graphList:
			node = elem
			while(node):
				print(node.val,end="->")
				node = node.next
			print()


if __name__ == "__main__":
	numVertex = 5
	graph = Graph(numVertex)
	graph.addEdge(0, 1)
	graph.addEdge(0, 4)
	graph.addEdge(1, 2)
	graph.addEdge(1, 3)
	graph.addEdge(1, 4)
	graph.addEdge(2, 3)
	graph.addEdge(3, 4)

	graph.printGraph()
