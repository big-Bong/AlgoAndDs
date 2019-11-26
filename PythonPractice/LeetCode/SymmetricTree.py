def isSymmetric(arr):
	n = len(arr)
	l = []
	pointer = 0


	for elem in arr:
		if(len(l) == 0):
			l.append(elem)
			pointer += 1
		else:
			if(elem == l[pointer-1]):
				del l[pointer-1]
				pointer -= 1
			else:
				l.append(elem)
				pointer += 1

	return (len(l) == 1)

arr1 = [1,2,2,3,4,4,3]
print(isSymmetric(arr1))

arr2 = [1,2,2,None,3,None,3]
print(isSymmetric(arr2))