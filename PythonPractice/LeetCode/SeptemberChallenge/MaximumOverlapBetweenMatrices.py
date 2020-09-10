def largestOverlap(A, B):
	N = len(A)
	maxOverlap = 0
	for i in range(N):
		for j in range(N):
			maxOverlap = max(maxOverlap,calculateMaxOverlap(i,j,A,B,N))
			maxOverlap = max(maxOverlap,calculateMaxOverlap(i,j,B,A,N))

	return maxOverlap

def calculateMaxOverlap(index1,index2,A,B,N):
	maxOverlap = 0
	for b_row,a_row in enumerate(range(index2,N)):
		for b_col,a_col in enumerate(range(index1,N)):
			if(A[a_row][a_col] == 1 and A[a_row][a_col] == B[b_row][b_col]):
				maxOverlap += 1

	return maxOverlap

A = [[1,1,0],[0,1,0],[0,1,0]]
B = [[0,0,0],[0,1,1],[0,0,1]]

print(largestOverlap(A,B))