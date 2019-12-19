def stepClimbing(n):
	if(n<=0):
		return

	arr = [0]*(n+1)
	arr[0] = 1

	for i in range(1,n+1):
		total = 0
		for j in [1,3,5]:
			if((i-j) >= 0):
				total += arr[i-j]
		arr[i] = total

	return arr[n]

print(stepClimbing(7))