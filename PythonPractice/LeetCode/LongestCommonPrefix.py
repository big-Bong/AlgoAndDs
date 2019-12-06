class Solution:
    def longestCommonPrefix(self, strs):
        if(not strs):
            return ""
        s1 = strs[0]
        prefix = ""
        for i in range(len(s1)):
            for elem in strs[1:]:
                if(i >= len(elem) or s1[i] != elem[i]):
                    return s1[:i]
            prefix += s1[i]

        return prefix

sol = Solution()
arr = ['flower','flow','flowered']
print(sol.longestCommonPrefix(arr))