def majorityElement2(nums):
	if(not nums):
		return []

	N = len(nums)
	threshold = N//3
	dict = {}

	for elem in nums:
		if(elem in dict):
			dict[elem] += 1
		else:
			dict[elem] = 1

	output = []
	for key in dict:
		if(dict[key] > threshold):
			output.append(key)

	return output

nums = [1,1,1,3,3,2,2,2]
print(majorityElement2(nums))
