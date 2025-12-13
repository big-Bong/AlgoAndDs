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
    
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
        
        char_arr = [0]*26
        for char in s:
            position = ord(char) - ord('a')
            char_arr[position] += 1

        for char in t:
            position = ord(char) - ord('a')
            if(char_arr[position] == 0):
                return False
            char_arr[position] -= 1
        
        """
        Third loop to check if character array has a number or nor becomes unnecessary.
        In case string length is same but character mismatch is present, then in the second loop
        at least for one character the value will already be 0
        """
 
        return True


solution = Solution()
#print(solution.isValidAnagram("baa","aaa"))
print(solution.isAnagram("rat","car"))
print(solution.isAnagram("stts","tstt"))