from collections import defaultdict

class Graph:
	def __init__(self):
		self.graph = defaultdict(list)

	def addEdge(self,source,dest):
		self.graph[source].append(dest)

	def DFS(self,vertex):
		visited = [False]*len(self.graph)
		self.DFSHelper(vertex,visited)
		print()

	def DFSHelper(self,vertex,visited):
		if(visited[vertex]):
			return

		print(vertex,end=" ")
		visited[vertex] = True
		for elem in self.graph[vertex]:
			self.DFSHelper(elem,visited)

g = Graph()
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3)

g.DFS(2)
