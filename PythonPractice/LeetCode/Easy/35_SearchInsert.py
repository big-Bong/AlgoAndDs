def searchInsert(nums, target):
    if(not nums):
        return 0
    
    desc = False
    N = len(nums)
    
    if(N>1 and nums[1] < nums[0]):
        desc = True
    
    for pos,num in enumerate(nums):
        if(num == target):
            return pos
        if(desc and target > num):
            return pos
        if(not desc and target < num):
            return pos
    
    return N

nums = [1,3,5,9]
target = 12

print(searchInsert(nums,target))