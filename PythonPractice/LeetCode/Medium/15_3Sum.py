def threeSumSorting(nums):
	N = len(nums)
	output_mat = []
	nums.sort()
        
	for i in range(N-2):
		j = i+1
		k = N-1
		prev_j = None
		prev_k = None
            
		if(i!=0 and nums[i] == nums[i-1]):
			continue
            
		while(j<k):
			if(prev_j != None and nums[j] == prev_j):
				j += 1
				continue
			if(prev_k != None and nums[k] == prev_k):
				k -= 1
				continue
			
			arr = []
			if(nums[i]+nums[j]+nums[k]==0):
				arr.append(nums[i])
				arr.append(nums[j])
				arr.append(nums[k])
				output_mat.append(arr)
				prev_j = nums[j]
				prev_k = nums[k]
				j += 1
				k -= 1
			elif(nums[i]+nums[j]+nums[k] < 0):
				prev_j = nums[j]
				j += 1
			else:
				prev_k = nums[k]
				k -= 1
        
	return output_mat

arr = [-1,0,1,2,-1,-4,-1,-1,2,2]
print(threeSumSorting(arr))