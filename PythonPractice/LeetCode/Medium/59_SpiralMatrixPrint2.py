def generateMatrix(n):
	border = 0
	arr = [[0]*n for i in range(n)]
	
	arrMinIndex = 0
	arrMaxIndex = n-1
	val =0
	while(val < n*n):
		i = arrMinIndex + border
		for j in range(arrMinIndex+border, arrMaxIndex-border+1):
			val += 1
			arr[i][j] = val
		
		j = arrMaxIndex - border
		for i in range(arrMinIndex+border+1, arrMaxIndex-border+1):
			val += 1
			arr[i][j] = val

		i = arrMaxIndex - border
		for j in range(arrMaxIndex - 1 - border, arrMinIndex+border-1,-1):
			val += 1
			arr[i][j] = val

		j = arrMinIndex + border
		for i in range(arrMaxIndex - border - 1, arrMinIndex+border, -1):
			val += 1
			arr[i][j] = val

		border += 1

	
	return arr

print(generateMatrix(1))