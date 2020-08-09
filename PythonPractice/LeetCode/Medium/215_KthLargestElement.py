def findKthLargest(nums, k):
	if(not nums):
		return None
	
	N = len(nums)
	if(N <= 1):
		return nums[0]

	for i in range(N//2 - 1, -1, -1):
		heapify(nums,N,i)

	for i in range(N-1,N-k,-1):
		nums[i],nums[0] = nums[0],nums[i]
		heapify(nums,i,0)

	return nums[0]


def heapify(nums,N,i):
	largest = i
	left = 2*i + 1
	right = 2*i + 2

	if(left < N and nums[largest] < nums[left]):
		largest = left

	if(right < N and nums[largest] < nums[right]):
		largest = right

	if(largest != i):
		nums[largest],nums[i] = nums[i],nums[largest]
		heapify(nums,N,largest)


nums = [3,2,3,1,2,4,5,5,6,6]
k = 4
print(findKthLargest(nums,k))