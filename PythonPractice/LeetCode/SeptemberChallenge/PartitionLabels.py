def partitionLabels(S):
	N = len(S)
	if(N == 1):
		return [1]

	dict = {}
	arr = []
	j = 0
	for i,c in enumerate(S):
		if(c in dict):
			temp = arr[dict[c]]
			arr[dict[c]] = [temp[0],i]
		else:
			dict[c] = j
			j += 1
			arr.append([i,i])

	final_result = []
	min_elem = arr[0][0]
	max_elem = arr[0][1]

	N = len(arr)
	for i in range(1,N):
		if(arr[i][0] > max_elem):
			final_result.append(max_elem - min_elem + 1)
			min_elem = arr[i][0]
			max_elem = arr[i][1]
		elif(arr[i][1] > max_elem):
			max_elem = arr[i][1]
	final_result.append(max_elem - min_elem + 1)

	return final_result

S = "ab"
print(partitionLabels(S))


