def merge(nums1, m, nums2, n):
	while(n >= 0):
		if(m <= 0 or nums2[n-1] >= nums1[m-1]):
			nums1[m+n-1] = nums2[n-1]
			n -= 1
		else:
			nums1[m+n-1] = nums1[m-1]
			m -= 1

nums1 = [1,2,3,4,5,6,0,0,0]
m = 6
nums2 = [0,1,7]
n = 3

merge(nums1,m,nums2,n)
print(nums1)