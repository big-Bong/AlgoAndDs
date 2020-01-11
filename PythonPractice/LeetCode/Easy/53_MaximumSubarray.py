def maxSubarray(arr):
	if(not arr):
		return None

	maxSum = arr[0]
	total = arr[0]
	N = len(arr)

	for j in range(1,N):
		total += arr[j]
		if(total <= arr[j]):
			total = arr[j]
		if(total > maxSum):
			maxSum = total
	return maxSum

nums = [-1]
print(maxSubarray(nums))