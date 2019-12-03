class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if(not s):
            return 0
        if(len(s) == 1):
            return 1
        
        i = 0
        dict = {}
        maxLength = tempLength = 0
        
        for j in range(0,len(s)):
            elem = s[j]
            if((elem in dict) and i<(dict[elem]+1)):
                i = dict[elem]+1
            
            dict[elem] = j
            tempLength = j-i+1
            if(tempLength > maxLength):
                maxLength = tempLength
        
        return maxLength

sol = Solution()
print(sol.lengthOfLongestSubstring('abcbdace'))