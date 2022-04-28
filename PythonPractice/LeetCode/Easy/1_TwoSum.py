from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i in range(len(nums)):
            dict[nums[i]] = i
        for i in range(len(nums)):
            other_num = target - nums[i]
            if(other_num in dict):
                other_num_pos = dict[other_num]
                if(other_num_pos != i):
                    return ([i,other_num_pos])
        return []

s = Solution()
print(s.twoSum([3,3],6))