class Solution:
    def isValidAnagram(self,s: str, t: str) -> bool:
        count_dict = {}
        for alph in s:
            if(alph in count_dict):
                count_dict[alph] += 1
            else:
                count_dict[alph] = 1
        for alph in t:
            if(alph in count_dict):
                count_dict[alph] -= 1
            else:
                return False
        for elem in count_dict:
            if(count_dict[elem] != 0):
                return False
        return True

solution = Solution()
print(solution.isValidAnagram("baa","aaa"))