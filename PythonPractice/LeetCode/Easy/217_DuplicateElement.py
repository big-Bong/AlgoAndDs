from typing import Set


class Solution:
	def hasDuplicateElements(self, arr):
		dict = set()
		for elem in arr:
			if(elem in dict):
				return True
			else:
				dict.add(elem)
		return False

S = Solution()
print(S.hasDuplicateElements([1,2,3,4]))