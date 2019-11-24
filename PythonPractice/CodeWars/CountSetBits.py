"""
Count the number of set bits in binary representation of an integer

CODEWARS
"""

"""
def countBits(n):
    if(n==0):
        return 0
    if((n&(n-1))==0):
        return 1
    
    arr = []
    while(n>0):
        arr.append(n%2)
        n = int(n/2)

    count = 0
    for i in arr:
        if(i == 1):
            count += 1
    
    return count
"""

def countBits(n):
    count = 0
    while(n > 0):
        count += (n&1)
        n >>= 1

    return count

print(countBits(1234))
print(countBits(0))
print(countBits(15))
print(countBits(2))
print(countBits(1))
print(countBits(8))