import numpy as np

def minPathSum(grid):
	m = len(grid)
	n = len(grid[0])

	for j in range(1,n):
		grid[0][j] += grid[0][j-1]
	for i in range(1,m):
		grid[i][0] += grid[i-1][0]

	for i in range(1,m):
		for j in range(1,n):
			grid[i][j] = min(grid[i-1][j], grid[i][j-1])+grid[i][j]
	return grid[m-1][n-1]


grid = np.random.randint(0,20,(4,1))
print(grid)
print(minPathSum(grid))