def longestConsecutive(nums):
	if(not nums):
		return 0

	N = len(nums)
	dict = {}

	for elem in nums:
		dict[elem] = -1

	longestConsecutive = 1

	for elem in nums:
		if(dict[elem] == -1 and elem-1 in dict):
			count = 1
			if(dict[elem-1] > 0):
				count += dict[elem-1]
				dict[elem-1] = 0
			temp = elem
			while(temp-1 in dict and dict[temp-1] == -1):
				temp -= 1
				count += 1
				dict[temp] = 0

			if(temp-1 in dict and dict[temp-1] > 0):
				count += dict[temp-1]

			dict[elem] = count
			if(count > longestConsecutive):
				longestConsecutive = count

	return longestConsecutive


nums = [2,0,4,100,101,106,3,1,102,104,107,105,103]
print(longestConsecutive(nums))