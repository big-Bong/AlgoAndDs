def zeroMatrix(matrix):
	N = len(matrix)
	M = len(matrix[0])
	row_flag = False
	column_flag = False

	for i in range(N):
		for j in range(M):
			if(matrix[i][j] == 0):
				if(i == 0):
					row_flag = True

				if(j == 0):
					column_flag = True
				matrix[i][0] = 0
				matrix[0][j] = 0

	for i in range(1,N):
		if(matrix[i][0] == 0):
			matrix[i] = [0]*M

	for j in range(1, M):
		if(matrix[0][j] == 0):
			for row in matrix:
				row[j] = 0

	if(matrix[0][0] == 0):
		if(row_flag):
			matrix[0] = [0]*M
		if(column_flag):
			for row in matrix:
				row[0] = 0

	return matrix

matrix = [[1,0]]
print(zeroMatrix(matrix))