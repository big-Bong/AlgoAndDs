def majorityElement(nums):
	dict = {}
	for elem in nums:
		if(elem in dict):
			dict[elem] += 1
		elif(len(dict) == 0):
			dict[elem] = 1
		else:
			(k,v), = dict.items()
			if(v == 1):
				del dict[k]
				dict[elem] = 1
			else:
				dict[k] -= 1

	(k,v), = dict.items()
	return k

nums = [2,2,1,1,1,2,2]
print(majorityElement(nums))

