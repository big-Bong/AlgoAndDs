from typing import List


def reverse_traversal(arr):
    for i in range(len(arr)-1,-1,-1):
        print(arr[i])

def insert(arr,val,option="b"):
    if(option=="b"):
        arr.insert(0,val)
    if(option=="a"):
        pos = int(input("Enter position to insert: "))
        arr.insert(pos,val)
    if(option=="e"):
        arr.append(val)
    
    print(arr)

def insert_at_pos(arr,val,pos):
    arr.append(0)
    for i in range(len(arr)-1,pos-1,-1):
        arr[i] = arr[i-1]
    
    arr[pos] = val
    print(arr)

def linear_search(arr: List[int],elem: int) -> int:
    for index,value in enumerate(arr):
        if(elem == value):
            return index
    return -1

def binary_search(arr: List[int], elem: int) -> int:
    start = 0
    end = len(arr)-1
    
    while(start<=end):
        mid = start + (end-start)//2
        if(arr[mid] == elem):
            return mid
        elif(elem < arr[mid]):
            end = mid-1
        else:
            start = mid+1
    
    return -1

def binary_search_recursive(arr: List[int], elem: int, start: int, end: int) -> int:
    if(start > end):
        return -1
    
    mid = start + (end-start)//2
    if(arr[mid] == elem):
        return mid
    elif(elem < arr[mid]):
        return binary_search_recursive(arr,elem,start,mid-1)
    else:
        return binary_search_recursive(arr,elem,mid+1,end)



if __name__ == "__main__":
    arr = [0,1,2,3,4]
    #reverse_traversal(arr)

    #insert(arr,5,"e")
    #insert(arr,6,"b")
    #insert(arr,7,"a")

    #insert_at_pos(arr,7,2)
    #arr.pop()
    #print(arr,end=" ")
    #arr.remove(0)
    #print(arr, end=" ")
    #arr.clear()
    #print(arr, end=" ")

    #position = binary_search(arr,5)
    position = binary_search_recursive(arr=arr,elem=15,start=0,end=len(arr)-1)
    if(position==-1):
        print("Number not present")
    else:
        print(f"Number present at {position}")