from collections import defaultdict

class Node:
	def __init__(self,val):
		self.val = val
		self.next = None

class Graph:
	def __init__(self):
		self.graph = defaultdict(list)

	def addEdge(self,source,dest):
		self.graph[source].append(dest)

	def printGraph(self):
		for elem in self.graph:
			print("Vertex connected to vertex",elem)
			for e in self.graph[elem]:
				print(e,end=" ")
			print()

	def BFS(self,vertex):
		visited = [False]*len(self.graph)
		queue = [vertex]
		visited[vertex] = True

		while(queue):
			node = queue.pop(0)
			print(node,end = " ")
			for elem in self.graph[node]:
				if(not visited[elem]):
					queue.append(elem)
					visited[elem] = True
		print()



g = Graph()
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3)

g.BFS(2)