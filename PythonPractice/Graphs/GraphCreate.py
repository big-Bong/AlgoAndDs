class Graph:
	vertex_count = 0
	id = 0
	def __init__(self,numVertex):
		self.numVertex = numVertex
		self.vertexDict = {}
		self.vertexList = [0]*numVertex
		self.graphMatrix = [[0 for j in range(numVertex)] for i in range(numVertex)]

	def setVertex(self,val):
		if(self.vertex_count < self.numVertex):
			self.vertexList[self.id] = val
			self.vertexDict[val] = self.id
			self.vertex_count += 1
			self.id += 1
		else:
			print("Can't add more vertices")

	def getVertex(self):
		print(self.vertexList)

	def setEdges(self,vertex1,vertex2,weight):
		if(vertex1 in self.vertexDict and vertex2 in self.vertexDict):
			self.graphMatrix[self.vertexDict[vertex1]][self.vertexDict[vertex2]] = weight
			self.graphMatrix[self.vertexDict[vertex2]][self.vertexDict[vertex1]] = weight
		else:
			print("Vertex does not exist in the graph")

	def printGraph(self):
		for i in range(self.numVertex):
			print(self.graphMatrix[i])

graph = Graph(6)
graph.setVertex('a')
graph.setVertex('b')
graph.setVertex('c')
graph.setVertex('d')
graph.setVertex('e')
graph.setVertex('f')
graph.setVertex('g')
graph.setEdges('a','b',2)
graph.setEdges('a','d',3)
graph.setEdges('a','e',1)
graph.setEdges('a','b',2)
graph.setEdges('b','c',4)
graph.setEdges('b','d',3)
graph.setEdges('b','e',2)
graph.setEdges('c','d',1)
graph.setEdges('d','e',6)
graph.printGraph()
graph.getVertex()