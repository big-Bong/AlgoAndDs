from collections import defaultdict

def findOrder(numCourses,prerequisites):
	if(numCourses == 1):
		return [0]
	graph = defaultdict(list)
	for elem in prerequisites:
		graph[elem[1]].append(elem[0])
		if(not graph[elem[0]]):
			graph[elem[0]] = []
	
	if(isCyclic(graph,numCourses)):
		return []
	
	finalResult = []
	visited = [False]*numCourses
	for elem in graph:
		if(not visited[elem]):
			DFSUtil(graph,elem,visited,finalResult)
			finalResult.append(elem)
	
	for digit in range(numCourses):
		if(digit not in graph):
			finalResult.append(digit)
	return finalResult[::-1]

def DFSUtil(graph,elem,visited,finalResult):
	if(visited[elem]):
		return

	visited[elem] = True
	for neighbour in graph[elem]:
		if(not visited[neighbour]):
			DFSUtil(graph,neighbour,visited,finalResult)
			finalResult.append(neighbour)

def isCyclic(graph,numCourses):
	recStack = [False]*numCourses
	visited = [False]*numCourses
	for elem in graph:
		if(not visited[elem]):
			if(isCyclicUtil(graph,elem,visited,recStack)):
				return True
	return False

def isCyclicUtil(graph,elem,visited,recStack):
	if(recStack[elem]):
		return True
	visited[elem] = True
	recStack[elem] = True
	for neighbour in graph[elem]:
		if(isCyclicUtil(graph,neighbour,visited,recStack)):
			return True
	
	recStack[elem] = False
	return False

numCourses = 2
prerequisites = [[1,0]]

print(findOrder(numCourses,prerequisites))