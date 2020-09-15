def rob(nums):
	if(not nums):
		return 0

	N = len(nums)
	if(N == 1):
		return nums[0]
	if(N == 2):
		return max(nums[0],nums[1])

	max_arr = [0 for _ in range(N)]
	max_arr[0] = nums[0]
	max_arr[1] = nums[1]
	max_so_far = max(nums[0],nums[1])

	for i in range(2,N):
		if(i == 2):
			max_arr[i] = max_arr[i-2]+nums[i]
		else:
			max_arr[i] = max(max_so_far+nums[i],nums[i]+max_arr[i-2])
			max_so_far = max(max_so_far,max_arr[i-1])

	return max(max_arr[N-1],max_arr[N-2])

nums = [8,1,12,11,13]
print(rob(nums))