def largestSubarray(nums,K):
	N = len(nums)
	i = 0
	j = 1

	while(j <= N-K):
		if(nums[i] < nums[j]):
			i = j
		elif(nums[i] == nums[j]):
			x = i
			y = j
			while(nums[x] == nums[y]):
				x += 1
				y += 1
			if(nums[x] < nums[y]):
				i = j

		j += 1

	return nums[i:i+K]

nums = [1,4,3,4,5]
print(largestSubarray(nums,5))