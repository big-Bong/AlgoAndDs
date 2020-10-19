def rob(nums):
	N = len(nums)
	if(N == 1):
		return nums[0]
	if(N == 2 or N == 3):
		return max(nums)

	return max(houseRob(nums[:N-1],N),houseRob(nums[1:],N))

def houseRob(nums,N):
	print(nums)
	max_so_far = nums[0]
	temp_arr = [0]*(N-1)
	temp_arr[0] = nums[0]
	temp_arr[1] = nums[1]

	for i in range(2,N-1):
		temp_arr[i] = max(temp_arr[i-2]+nums[i],max_so_far+nums[i])
		max_so_far = max(max_so_far,temp_arr[i-1])

	print(temp_arr)
	return max(temp_arr[N-2],temp_arr[N-3])

#nums = [1,4,2,1,0,2,3,1,4,2,5,3,1,2]
#nums = [200,3,140,20,10]
nums = [1,2,3,4,5,1,2,3,4,5]
print(rob(nums))


