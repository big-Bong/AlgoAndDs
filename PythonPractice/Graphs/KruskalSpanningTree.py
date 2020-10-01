def find(parent,vertex):
	if(parent[vertex] == -1):
		return vertex
	if(parent[parent[vertex]] != -1):
		parent[vertex] = parent[parent[vertex]]

	return find(parent,parent[vertex])

def union(parent,rank,vertex1,vertex2):
	parent1 = find(parent,vertex1)
	parent2 = find(parent,vertex2)

	if(rank[parent1] == rank[parent2]):
		parent[vertex2] = vertex1
		rank[parent1] += 1
	elif(rank[parent1] < rank[parent2]):
		parent[vertex1] = vertex2
	else:
		parent[vertex2] = vertex1

def isCyclePresent(parent,vertex1,vertex2):
	return (find(parent,vertex1) == find(parent,vertex2))

def createGraph(edges,parent,rank):
	for s,d in edges:
		union(parent,rank,s,d)
		print(isCyclePresent(parent,s,d))

vertices = 5
edges = [[0,1],[1,2],[2,3],[1,3],[0,4]]
parent = [-1 for _ in range(vertices)]
rank = [1 for _ in range(vertices)]
createGraph(edges,parent,rank)
print(parent)
print(rank)