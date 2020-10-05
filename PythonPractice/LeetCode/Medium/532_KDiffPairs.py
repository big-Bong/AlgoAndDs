def findPairs(nums,k):
	pairs = 0
	dict = {}
	for elem in nums:
		if(elem in dict):
			dict[elem] += 1
		else:
			dict[elem] = 1

	if(k == 0):
		for elem in dict:
			if(dict[elem] > 1):
				pairs += 1
	else:
		for elem in dict:
			elem2 = k + elem
			if(elem2 in dict):
				pairs += 1

	return pairs

#nums = [3,1,4,1,5]
#k = 2

#nums = [1,2,3,4,5]
#k = 1

#nums = [1,3,1,5,4]
#k = 0

#nums = [1]
#k = 1

#nums = [-1,-2,-3]
#k = 1

nums = [3,3,5,5]
k = 2
print(findPairs(nums,k))
