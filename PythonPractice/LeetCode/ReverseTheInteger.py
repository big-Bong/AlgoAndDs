import math

class Solution:
    def reverse(self, x: int) -> int:
        val = x
        if(x<0):
            x = -(x)
        num_digits = 0
        if(x!=0):
            num_digits = int(math.log10(x))
        else:
            num_digits = 1
        
        multiplier = 10**num_digits
        
        reversed_num = 0
        while(multiplier>0):
            x,rem = divmod(x,10)
            reversed_num += (multiplier*rem)
            multiplier = int(multiplier/10)
        
        if((reversed_num > 2**31 - 1) or (-reversed_num < -2**31)):
            return 0
        
        return -(reversed_num) if(val<0) else reversed_num

sol = Solution()
print(sol.reverse(123189))