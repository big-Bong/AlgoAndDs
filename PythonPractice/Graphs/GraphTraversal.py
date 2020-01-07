from collections import defaultdict

class Graph:
	def __init__(self):
		self.graph = defaultdict(list)

	def addEdge(self,vertex1,vertex2):
		self.graph[vertex1].append(vertex2)

	def BFS(self,startVertex):
		N = len(self.graph)
		visited = [False]*N
		queue = [startVertex]
		visited[startVertex] = True

		while(queue):
			v = queue.pop(0)
			print(v,end = " ")

			l = self.graph[v]
			for i in l:
				if(not visited[i]):
					visited[i] = True
					queue.append(i)

	def DFS(self,startVertex):
		N = len(self.graph)
		visited = [False]*N
		stack = []
		traversalList = []

		self.DFSUtil(startVertex,visited,stack,traversalList)
		print(traversalList)

	def DFSUtil(self,vertex,visited,stack,traversalList):
		if(not visited[vertex]):
			stack.append(vertex)
			traversalList.append(vertex)
			visited[vertex] = True

		for elem in self.graph[vertex]:
			if(not visited[elem]):
				self.DFSUtil(elem,visited,stack,traversalList)

		if(stack):
			self.DFSUtil(stack.pop(),visited,stack,traversalList)

		return None



g = Graph() 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3)
g.BFS(2)
g.DFS(2)