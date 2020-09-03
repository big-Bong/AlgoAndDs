def largestTimeFromDigits(A):
	s = ""
	A.sort()
	biggest = -1
	i = 0
	pos = -1
	while(i < 4):
		if(A[i] >= biggest and A[i] <= 2):
			biggest = A[i]
			pos = i
		i += 1

	if(biggest == -1):
		return ""
	
	if(biggest == 2):
		s += "2"
		A[pos] = -1

		if(pos+1 == 4):
			s += str(A[2])+":"+str(A[1])+str(A[0])
			return s
		elif(A[pos+1] > 3 and pos-1 < 0):
			return ""
		elif(A[pos+1] > 3):
			s += str(A[pos-1])+":"
			A[pos-1] = -1
		else:
			s += str(A[pos+1])+":"
			A[pos+1] = -1
	else:
		s += str(A[pos])
		A[pos] = -1
		if(pos+1 == 4):
			s += str(A[2])+":"+str(A[1])+str(A[0])
			return s
		else:
			s += str(A[3])+":"
			A[3] = -1

	biggest = -1
	i = 3
	while(i >= 0):
		if(A[i] != -1 and A[i] < 6 and A[i] > biggest):
			biggest = A[i]
			pos = i
		i -= 1

	if(biggest == -1):
		return ""

	s += str(A[pos])
	A[pos] = -1

	for elem in A:
		if(elem != -1):
			s += str(elem)

	return s

A = [2,0,6,6]
print(largestTimeFromDigits(A))