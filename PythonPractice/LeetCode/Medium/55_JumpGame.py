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

def canJump1(nums):
	if(not nums):
		return False
	N = len(nums)
	if(N==1):
		return True
	max_jump = 0
	max_jump_pos = N-1
	for i in range(N-2,-1,-1):
		curr = i+nums[i]
		if(curr >= max_jump_pos):
			max_jump_pos = i
			val = max(curr,max_jump)
			if(val>max_jump):
				max_jump = val
	return (max_jump_pos == 0 and max_jump >= N-1)


arr = [2,0,1,0,0]
print(canJump1(arr))