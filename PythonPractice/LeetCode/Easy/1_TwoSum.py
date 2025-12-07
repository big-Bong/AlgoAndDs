from typing import List, Tuple

def sorting_approach(arr: List[int], target: int) -> Tuple[int,int]:
    """
    O(nlgn) approach to two sum
    Runs two pointer from left and right, and depending on whether sum of elem > or < moves the pointers
    
    This is a wrong approach. Unless we can preserve original index positions
    """
    arr.sort()
    lp = 0
    rp = len(arr) - 1

    while(lp < rp):
        sum = arr[lp] + arr[rp]
        if(sum == target):
            return (lp,rp)
        elif(sum < target):
            lp += 1
        else:
            rp -= 1
    
    return (-1,-1)

def dict_approach(arr: List[int], target: int) -> Tuple[int,int]:
    """
    O(n) approach to two sum. O(n) auxillary space as well
    Use a dict to store arr numbers and indexes. Iterate over array
    """

    dict = {}
    for (index,value) in enumerate(arr):
        dict[value] = index
    
    for (index,elem) in enumerate(arr):
        other_elem = target - elem
        if other_elem in dict and dict[other_elem] != index:
            return(index,dict[other_elem])
    
    return (-1,-1)

def improved_dict_approach(nums: List[int], target: int) -> Tuple[int,int]:
    """
    Improved version of dict with a single loop and better variable name
    """

    lookup = {}
    for index,elem in enumerate(nums):
        other_elem = target-elem
        if(other_elem in lookup):
            return(lookup[other_elem],index)
        lookup[elem] = index
    
    return (-1,-1)

if __name__ == "__main__":
    arr = [3,2,4,2]
    target = 4

    #(index1, index2) = sorting_approach(arr=arr,target=target)
    #(index1, index2) = dict_approach(arr=arr,target=target)
    (index1, index2) = improved_dict_approach(nums=arr,target=target)
    if(index1 != -1):
        print(f"The two indexes are {index1} and {index2}")
    else:
        print("No numbers add upto target")



