#Union By Rank and Path Compression. Detect cycle in a graph.

#Find operation with path compression
def findParent(parent,vertex):
	parent_vertex = parent[vertex]
	while(parent[parent_vertex] != -1):
		parent[vertex] = parent[parent_vertex]
		vertex = parent_vertex
		parent_vertex = parent[parent_vertex]

	return vertex if(parent_vertex == -1) else parent_vertex


def unionByRank(parent,rank,vertex1,vertex2):
	parent_vertex1 = findParent(parent,vertex1)
	parent_vertex2 = findParent(parent,vertex2)

	if(rank[parent_vertex1] > rank[parent_vertex2]):
		parent[parent_vertex2] = parent_vertex1 
	elif(rank[parent_vertex1] < rank[parent_vertex2]):
		parent[parent_vertex1] = parent_vertex2
	else:
		parent[parent_vertex1] = parent_vertex2
		rank[parent_vertex2] += 1 

def detectCycle(parent,rank,vertex1,vertex2):
	if(findParent(parent,vertex1) == findParent(parent,vertex2)):
		return True

	unionByRank(parent,rank,vertex1,vertex2)

	return False

V = 5
parent = [-1 for _ in range(V)]
rank = [0 for _ in range(V)]

detectCycle(parent,rank,0,1)
detectCycle(parent,rank,0,2)
detectCycle(parent,rank,3,4)
print(parent)
print(rank)
input("Press Enter to continue...")
print("Adding edge between 1 and 3. Cycle detected = ",detectCycle(parent,rank,1,3))
print(parent)
print(rank)
input("Press Enter to continue...")
print("Adding edge between 4 and 2. Cycle detected = ",detectCycle(parent,rank,4,2))
print(parent)
print(rank)
