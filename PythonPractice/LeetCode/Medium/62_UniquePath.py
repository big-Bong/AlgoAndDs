def uniquePaths(r, c):
	if(r==0 or c==0):
		return
        
	matrix = [[1]*c for i in range(r)]
    
	for i in range(1,r):
		for j in range(1,c):
			matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]
	return matrix[r-1][c-1]

print(uniquePaths(6,8))