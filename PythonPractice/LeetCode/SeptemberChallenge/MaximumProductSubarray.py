def maxProduct(nums):
	if(not nums):
		return 0
	N = len(nums)
	if(N == 1):
		return nums[0]

	arrs_without_zero = []
	last_zero_pos = 0
	for i in range(N):
		if(nums[i] == 0):
			arrs_without_zero.append(nums[last_zero_pos:i])
			last_zero_pos = i + 1
	if(last_zero_pos < N):
		arrs_without_zero.append(nums[last_zero_pos:])

	maxProd = 0
	for arr in arrs_without_zero:
		if(arr):
			negs = checkNegsInArr(arr)

			if(negs == 1):
				maxProd = max(maxProd,processForOneNeg(arr))
			elif(negs%2 == 0):
				prod = 1
				for elem in arr:
					prod *= elem
				maxProd = max(maxProd,prod)
			else:
				maxProd = max(maxProd,processForMultipleNegs(arr))

	return maxProd

def processForMultipleNegs(nums):
	prod1 = nums[0] if(nums[0] < 0) else 1
	i = 1 if(nums[0] < 0) else 0

	if(i == 0):
		while(nums[i] > 0):
			prod1 *= nums[i]
			i += 1
		prod1 = prod1*nums[i]
		i += 1

	N = len(nums)
	prod2 = nums[N-1] if(nums[N-1] < 0) else 1
	j = N-2 if(nums[N-1] < 0) else N-1

	if(j == N-1):
		while(nums[j] > 0):
			prod2 *= nums[j]
			j -= 1
		prod2 = prod2*nums[j]
		j -= 1

	common = 1
	for elem in nums[i:j+1]:
		common *= elem

	return max(common*prod1,common*prod2) 	



def processForOneNeg(arr):
	N = len(arr)
	if(N == 1):
		return arr[0]

	maxProd = 0
	prod = 1
	for elem in arr:
		prod *= elem
		if(elem < 0):
			maxProd = prod//elem
			prod = 1
	return max(maxProd,prod)

def checkNegsInArr(arr):
	negs = 0
	for elem in arr:
		if(elem < 0):
			negs += 1

	return negs

def maxProductSubarray(nums):
	if(not nums):
		return 0
	N = len(nums)
	max_product = nums[0]
	min_product = nums[0]
	ans = nums[0]

	for i in range(1,N):
		curr_max = max(max_product*nums[i],min_product*nums[i],nums[i])
		curr_min = min(min_product*nums[i],max_product*nums[i],nums[i])
		ans = max(ans,curr_max)
		max_product = curr_max
		min_product = curr_min

	return ans

#arr = [-2,-3,7]
#arr = [-1,-2,-3,0]
#arr = [-2,0,-1]
#arr = [2,3,-2,4]
#arr = [-6,-1,-3,1,5,-2,4,-1,-5,3,-6,11000]
arr = [2,-5,-2,-4,3]
#arr = [0,-2,0]
print(maxProductSubarray(arr))