from collections import defaultdict

def calcEquation(equations,values,queries):
	var_list = defaultdict(list)
	N = len(equations)
	for i in range(N):
		var_list[equations[i][0]].append([equations[i][1],values[i]])
		var_list[equations[i][1]].append([equations[i][0],1/values[i]])

	M = len(queries)
	output = []
	for i in range(M):
		if(queries[i][0] not in var_list or queries[i][1] not in var_list):
			output.append(-1.0)
		elif(queries[i][0] == queries[i][1]):
			output.append(1.0)
		else:
			output.append(dfs(queries[i][0],queries[i][1],var_list,1.0,{queries[i][0]:True}))

	return output

def dfs(start,end,dict,product,visited):
	if(start == end):
		return product

	for first,second in dict[start]:
		if(first not in visited):
			visited[first] = True
			temp = dfs(first,end,dict,product*float(second),visited)
			del visited[first]
			if(temp != -1.0):
				return temp

	return -1.0

#equations = [["a","b"],["b","c"]]
#values = [2.0,3.0]
#queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"],["c","a"]]

#equations = [["a","b"],["b","c"],["bc","cd"]]
#values = [1.5,2.5,5.0]
#queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"],["b","d"]]

equations = [["a","b"],["c","d"]]
values = [2.0,3.0]
queries = [["a","d"]]

print(calcEquation(equations,values,queries))
