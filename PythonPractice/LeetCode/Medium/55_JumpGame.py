def canJump(nums):
	if(not nums):
		return False

	N = len(nums)
	bool_arr = [False]*N
	bool_arr[-1] = True

	for i in range(N-2,-1,-1):
		max_jump = nums[i] + i
		while(max_jump > 0):
			if(max_jump < N-1 and not bool_arr[max_jump]):
				max_jump -= 1
			else:
				bool_arr[i] = True
				break

	return bool_arr[0]

arr = [3,2,1,0,4]
print(canJump(arr))