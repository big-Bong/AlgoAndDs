class Solution:
    def romanToInt(self, s: str) -> int:
        romanDict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        otherRomanDict = {'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
        
        num = 0
        flag = False
        for i in range(len(s)):
            if(not flag):
                if((i<len(s)-1) and (s[i:i+2] in otherRomanDict)):
                    num += otherRomanDict[s[i:i+2]]
                    flag = True
                else:
                    num += romanDict[s[i]]
            else:
                flag = False
                
        
        return num

sol = Solution()
print(sol.romanToInt('XLV'))