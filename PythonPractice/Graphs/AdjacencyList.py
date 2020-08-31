class Node:
	def __init__(self,val):
		self.val = val
		self.next = None

class Graph:
	def __init__(self,V):
		self.vertices = V
		self.edge_list = [None]*V

	def addEdge(self,source,dest):
		s_node = Node(source)
		d_node = Node(dest)

		#Undirected graph. Hence both will go in each others list
		d_node.next = self.edge_list[source]
		self.edge_list[source] = d_node

		s_node.next = self.edge_list[dest]
		self.edge_list[dest] = s_node

	def addVertex(self):
		self.vertices += 1
		self.edge_list.append(None)

	def printGraph(self):
		for i in range(self.vertices):
			print("List for vertex ",i)
			temp = self.edge_list[i]
			while(temp):
				print(temp.val,end=" ")
				temp = temp.next
			print()

graph = Graph(5)
graph.addEdge(0, 1) 
graph.addEdge(0, 4) 
graph.addEdge(1, 2) 
graph.addEdge(1, 3) 
graph.addEdge(1, 4) 
graph.addEdge(2, 3) 
graph.addEdge(3, 4) 

graph.printGraph()

#graph.addVertex()
#graph.addEdge(1,5)
#graph.addEdge(5,2)

#raph.printGraph()