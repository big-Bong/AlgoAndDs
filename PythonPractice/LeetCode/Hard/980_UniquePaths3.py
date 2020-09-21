def uniquePaths3(grid):
	zero_count = 0
	N = len(grid)
	M = len(grid[0])
	start_i = 0
	start_j = 0

	for i in range(N):
		for j in range(M):
			if(grid[i][j] == 0):
				zero_count += 1
			if(grid[i][j] == 1):
				start_i = i
				start_j = j

	total_paths = 0
	visited = [[False for _ in range(M)] for _ in range(N)]
	visited[start_i][start_j] = True

	if(start_i - 1 < 0):
		total_paths = uniquePaths3Helper(grid,zero_count,visited,start_i+1,start_j,total_paths,N,M)
		if(start_j - 1 < 0):
			total_paths = uniquePaths3Helper(grid,zero_count,visited,start_i,start_j+1,total_paths,N,M)
		elif(start_j + 1 == M):
			total_paths = uniquePaths3Helper(grid,zero_count,visited,start_i,start_j-1,total_paths,N,M)
		else:
			total_paths = uniquePaths3Helper(grid,zero_count,visited,start_i,start_j+1,total_paths,N,M)
			total_paths = uniquePaths3Helper(grid,zero_count,visited,start_i,start_j-1,total_paths,N,M)
	elif(start_i + 1 == N):
		total_paths = uniquePaths3Helper(grid,zero_count,visited,start_i-1,start_j,total_paths,N,M)
		if(start_j - 1 < 0):
			total_paths = uniquePaths3Helper(grid,zero_count,visited,start_i,start_j+1,total_paths,N,M)
		elif(start_j + 1 == M):
			total_paths = uniquePaths3Helper(grid,zero_count,visited,start_i,start_j-1,total_paths,N,M)
		else:
			total_paths = uniquePaths3Helper(grid,zero_count,visited,start_i,start_j+1,total_paths,N,M)
			total_paths = uniquePaths3Helper(grid,zero_count,visited,start_i,start_j-1,total_paths,N,M)
	else:
		total_paths = uniquePaths3Helper(grid,zero_count,visited,start_i+1,start_j,total_paths,N,M)
		total_paths = uniquePaths3Helper(grid,zero_count,visited,start_i-1,start_j,total_paths,N,M)
		total_paths = uniquePaths3Helper(grid,zero_count,visited,start_i,start_j+1,total_paths,N,M)
		total_paths = uniquePaths3Helper(grid,zero_count,visited,start_i,start_j-1,total_paths,N,M)

	return total_paths

def uniquePaths3Helper(grid,zero_count,visited,i,j,total_paths,rows,columns):
	if(i >= rows or j >= columns or i < 0 or j < 0):
		return total_paths
	if(grid[i][j] == -1 or visited[i][j] == True):
		return total_paths
	if((grid[i][j] != 2 and zero_count == 0) or (grid[i][j] == 2 and zero_count != 0)):
		return total_paths
	if(grid[i][j] == 2 and zero_count == 0):
		total_paths += 1
		return total_paths

	visited[i][j] = True
	total_paths = uniquePaths3Helper(grid,zero_count-1,visited,i-1,j,total_paths,rows,columns)
	total_paths = uniquePaths3Helper(grid,zero_count-1,visited,i+1,j,total_paths,rows,columns)
	total_paths = uniquePaths3Helper(grid,zero_count-1,visited,i,j-1,total_paths,rows,columns)
	total_paths = uniquePaths3Helper(grid,zero_count-1,visited,i,j+1,total_paths,rows,columns)
	visited[i][j] = False

	return total_paths

#grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
#grid = [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
#grid = [[1,0],[-1,2]]
#grid = [[1,0,0],[0,0,0],[0,0,2]]
grid = [[1]]
print(uniquePaths3(grid))





