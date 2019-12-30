def intersect(nums1, nums2):
	if(not nums1 or not nums2):
		return []

	N = len(nums1)
	M = len(nums2)

	if(N<M):
		return helperIntersect(nums1,nums2)
	return helperIntersect(nums2,nums1)


def helperIntersect(smaller,larger):
	dict = {}
	output = []

	for elem in smaller:
		if(elem in dict):
			dict[elem] += 1
		else:
			dict[elem] = 1

	for elem in larger:
		if(elem in dict and dict[elem] != 0):
			output.append(elem)
			dict[elem] -= 1

	return output

nums1 = [1,1,3,3]
nums2 = [1,1,3,4,6]

print(intersect(nums1,nums2))