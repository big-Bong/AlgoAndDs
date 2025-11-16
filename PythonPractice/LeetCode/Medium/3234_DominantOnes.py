class Solution:
    def numberOfSubstrings(self, s:str) -> int:
        count = 0
        n = len(s)

        for i in range(n):
            num_zero = 0
            num_one = 0
            for j in range(i,n):
                if(s[j] == "0"):
                    num_zero += 1
                else:
                    num_one += 1
                
                if(num_one >= (num_zero**2)):
                    count += 1
        
        return count
    
if __name__ == "__main__":
    input = "0"
    sol = Solution()
    print(sol.numberOfSubstrings(s=input))