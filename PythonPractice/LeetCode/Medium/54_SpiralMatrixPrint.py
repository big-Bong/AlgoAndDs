def spiralMatrix(matrix):
	if(not matrix):
		return []
	R = len(matrix)
	C = len(matrix[0])
	arr = []

	i = 0
	j = 0
	bound = 0
	N = R*C

	while(N>0):
		while(j<(C-bound) and (N>0)):
			arr.append(matrix[i][j])
			N -= 1
			j += 1
		j -= 1
		i += 1

		while(i<(R-bound) and (N>0)):
			arr.append(matrix[i][j])
			N -= 1
			i += 1
		i -= 1
		j -= 1

		while(j>=bound and (N>0)):
			arr.append(matrix[i][j])
			N -= 1
			j -= 1
		j += 1
		i -= 1

		while(i >= (bound+1) and (N>0)):
			arr.append(matrix[i][j])
			N -= 1
			i -= 1
		i += 1
		j += 1
		bound += 1

	return arr

matrix = [[]
]
print(spiralMatrix(matrix))