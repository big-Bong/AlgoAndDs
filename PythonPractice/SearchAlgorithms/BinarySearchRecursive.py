def recursiveBSearch(arr,elem, start, end):
	if(start <= end):
		mid = int(start + (end-start)/2)

		if(arr[mid] == elem):
			return True

		if(elem > arr[mid]):
			return recursiveBSearch(arr,elem,mid+1,end)
		else:
			return recursiveBSearch(arr,elem,start,mid-1)

	return False

arr = [1,2,6,7,8]
elem = int(input())
start = 0
end = len(arr)-1
print("Presence of element is: ",recursiveBSearch(arr,elem,start,end))