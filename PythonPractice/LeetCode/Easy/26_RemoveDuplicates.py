def removeDuplicates(nums):
    if(not nums):
        return
    N = len(nums)
    i = 0
    j = 1
    while(j<N):
        if(nums[j]!=nums[i]):
            nums[i+1] = nums[j]
            i += 1
        j+=1
            
            
    return (i+1)

nums = [0,0,1,1,1,1,2,3,3,4,5,6,6]
print(removeDuplicates(nums))