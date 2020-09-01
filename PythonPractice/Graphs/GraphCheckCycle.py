from collections import defaultdict

class Graph:
	def __init__(self):
		self.graph = defaultdict(list)

	def addEdge(self,source,dest):
		self.graph[source].append(dest)
		if(not self.graph[dest]):
			self.graph[dest] = []

	def checkCycle(self):
		visited = [False]*len(self.graph)
		recStack = [False]*len(self.graph)

		for elem in self.graph:
			if(not visited[elem]):
				if(self.checkCycleUtil(elem,visited,recStack)):
					return True
		return False
			

	def checkCycleUtil(self,elem,visited,recStack):
		if(recStack[elem]):
			return True

		visited[elem] = True
		recStack[elem] = True
		
		for e in self.graph[elem]:
			if(self.checkCycleUtil(e,visited,recStack)):
				return True

		recStack[elem] = False
		return False

g = Graph()
g.addEdge(2, 1)
g.addEdge(1, 0)
g.addEdge(2, 0)
#g.addEdge(2, 0)
#g.addEdge(2, 3)
#g.addEdge(3, 3)

print(g.checkCycle())

	