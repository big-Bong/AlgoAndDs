def removeElement(nums, val):
    if(not nums):
        return
    N = len(nums)
    if(val not in nums):
        return N
    i = 0
    j = N-1
    
    while(i<j):
        if(nums[i]==val):
            while(j>i and nums[j]==val):
                j -= 1
            if(j==i):
                return i
            temp = nums[j]
            nums[j] = nums[i]
            nums[i] = temp
        i += 1
    
    return i

nums = [3,2,3,4]
val = 3
print(removeElement(nums,val))