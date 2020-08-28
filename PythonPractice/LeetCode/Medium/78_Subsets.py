def subsets(nums):
	if(not nums):
		return [[]]

	output = [[]]
	for i in range(1,len(nums)+1):
		data = [0 for _ in range(i)]
		generateSubsets(nums,data,output,0,len(nums)-1,0)

	return output

def generateSubsets(nums,data,output,start,end,index):
	if(index == len(data)):
		temp = [elem for elem in data]
		output.append(temp)
		return

	i = start
	while(i <= end):
		data[index] = nums[i]
		generateSubsets(nums,data,output,i+1,end,index+1)
		i += 1

	return output

nums = [1,2,3]
print(subsets(nums))