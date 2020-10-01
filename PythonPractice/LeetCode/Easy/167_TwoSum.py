def twoSum(numbers,target):
	N = len(numbers)
	start = 0
	end = N-1
	total = numbers[start]+numbers[end]

	while(start < end and total != target):
		if(total < target):
			start += 1
		if(total > target):
			end -= 1

		total = numbers[start] + numbers[end]

	return [start+1,end+1]

numbers = [-1]
target = -2
print(twoSum(numbers,target))
