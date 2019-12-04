def differenceTwo(arr):
	dict = {}
	for ind,elem in enumerate(arr):
		dict[elem] = ind

	k = 2
	return [(elem,elem+k) for elem in arr if(elem+k in dict)]

arr = [1,2,5,4]
print(differenceTwo(arr))