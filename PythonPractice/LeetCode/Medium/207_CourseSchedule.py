from collections import defaultdict

def canFinish(numCourses,prerequisites):
	graph = defaultdict(list)
	for s,d in prerequisites:
		graph[s].append(d)

	visited = [False for _ in range(numCourses)]
	for i in range(numCourses):
		if(i in graph and not DFS(graph,i,visited)):
			return False

	return True

def DFS(graph,i,visited):
	if(visited[i] == True):
		return False

	visited[i] = True
	for j in graph[i]:
		if(not DFS(graph,j,visited)):
			return False
	visited[i] = False

	return True

numCourses = 3
prerequisites = [[0,1],[2,0],[1,2]]
print(canFinish(numCourses,prerequisites))