def bsearch(arr,elem):
	end = len(arr)-1
	start = 0

	while(start <= end):
		mid = start + int((end-start)/2)
		if(elem == arr[mid]):
			return True

		if(elem > arr[mid]):
			start = mid+1
		else:
			end = mid-1

	return False

arr = [1,2,6,7,8]
elem = int(input())
print("Element found in array: ",bsearch(arr,elem))