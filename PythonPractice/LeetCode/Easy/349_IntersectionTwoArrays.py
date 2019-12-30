def intersect(nums1, nums2):
	if(not nums1 or not nums2):
		return []

	N = len(nums1)
	M = len(nums2)

	if(N<M):
		return helperIntersect(nums1,nums2)
	return helperIntersect(nums2,nums1)

def intersectSorted(nums1,nums2):
	if(not nums1 or not nums2):
		return []

	N = len(nums1)
	M = len(nums2)

	i = j = 0
	output = []
	while(i < N and j < M):
		if(nums1[i]==nums2[j]):
			output.append(nums1[i])
			i += 1
			j += 1
		elif(nums1[i] > nums2[j]):
			j += 1
		else:
			i += 1

	return output


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

nums1 = [1]
nums2 = [3]

print(intersectSorted(nums1,nums2))