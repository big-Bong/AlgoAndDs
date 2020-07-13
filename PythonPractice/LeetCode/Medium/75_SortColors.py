def sortColorsUnoptimized(nums):
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

def sortColors(nums):
	startptr, currptr, endptr = 0, 0, len(nums) - 1

	while(currptr <= endptr):
		if(nums[currptr] == 0):
			nums[currptr],nums[startptr] = nums[startptr],nums[currptr]
			currptr += 1
			startptr += 1
		elif(nums[currptr] == 1):
			currptr += 1
		else:
			nums[currptr],nums[endptr] = nums[endptr],nums[currptr]
			endptr -= 1

	return nums

nums = [1,2,2,0]
print(sortColors(nums))
