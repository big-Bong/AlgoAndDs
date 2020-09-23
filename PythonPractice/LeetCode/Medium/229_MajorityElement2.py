import collections
def majorityElement(nums):
    ctr = collections.Counter()
    for n in nums:
        ctr[n] += 1
        print(ctr)
        if len(ctr) == 3:
            ctr -= collections.Counter(set(ctr))
        print(ctr)
    return [n for n in ctr if nums.count(n) > len(nums)/3]

nums = [1,1,1,3,3,2,2,2]
print(majorityElement(nums))