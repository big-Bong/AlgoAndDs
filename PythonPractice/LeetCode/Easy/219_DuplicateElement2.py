from typing import List


class Solution:
	def containsNearbyDuplicate(self,nums: List[int],k: int) -> bool:
		dict = {}
		for i in range(len(nums)):
			if(nums[i] in dict and abs(i-dict[nums[i]]) <= k):
				return True
			dict[nums[i]] = i
		return False

soluton = Solution()
print(soluton.containsNearbyDuplicate([1,0,1,1],1))