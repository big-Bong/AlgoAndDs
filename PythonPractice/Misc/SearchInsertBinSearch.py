def searchInsert(nums,target):
	if(not nums):
		return 0

	N = len(nums)
	start = 0
	end = N-1
	desc = False

	if(N>1 and nums[1]<nums[0]):
		desc = True

	while(start <= end):
		mid = start + ((end-start)//2)

		if(nums[mid] == target):
			return mid

		if(mid != 0 and mid != N-1):
			if((desc and (target > nums[mid] and target < nums[mid-1])) or (target < nums[mid] and target > nums[mid-1])):
				return mid
			if((desc and (target < nums[mid] and target > nums[mid+1])) or (target > nums[mid] and target < nums[mid+1])):
				return mid + 1

		if(desc and target<nums[mid]):
			start = mid + 1
		elif(desc and target>nums[mid]):
			end = mid - 1
		elif(target < nums[mid]):
			end = mid - 1
		else:
			start = mid + 1

	if(end < 0):
		return 0
	elif(start >= N):
		return N
	else:
		return mid

nums = [-2]
target = -3
print(searchInsert(nums,target))