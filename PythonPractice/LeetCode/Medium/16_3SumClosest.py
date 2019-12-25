def threeSumClosest(nums,target):
    N = len(nums)
    output = None
    least_diff = None
    nums.sort()
    
    for i in range(N-2):
        j = i+1
        k = N-1
        
        while(j<k):
            closest = nums[i]+nums[j]+nums[k]
            diff = abs(target - closest)
            if(least_diff==None):
                least_diff = diff
                output = closest
                
            if(diff<least_diff):
                least_diff = diff
                output = closest
                
            if(closest < target ):
                j += 1
            elif(closest > target):
                k -= 1
            else:
                return closest
        
    return output

arr = [-1,2,1,-4]
target = 1
print(threeSumClosest(arr,target))
