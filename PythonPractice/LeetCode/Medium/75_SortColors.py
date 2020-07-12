def sortColors(nums):
	N = len(nums)
	if(N<=1):
		return nums
	startptr = currptr = 0
	endptr = N - 1
	
	while(currptr <= endptr):
		if(nums[startptr] == 0):
			if(currptr == startptr):
				currptr += 1
			startptr += 1
			continue

		if(nums[endptr] == 2):
			endptr -= 1
			continue

		if(nums[currptr] == 0):
			temp = nums[startptr]
			nums[startptr] = nums[currptr]
			nums[currptr] = temp
			startptr += 1
		elif(nums[currptr] == 2):
			temp = nums[endptr]
			nums[endptr] = nums[currptr]
			nums[currptr] = temp
			endptr -= 1

			if(nums[currptr] == 0):
				temp = nums[startptr]
				nums[startptr] = nums[currptr]
				nums[currptr] = temp
				startptr += 1
		else:
			if(nums[startptr] == 0):
				startptr = currptr
		
		currptr += 1
	
	return nums

nums = [1,1,0]
print(sortColors(nums))
