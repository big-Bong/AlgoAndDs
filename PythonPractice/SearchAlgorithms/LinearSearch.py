def lsearch(arr, elem):
	i = 0
	n = len(arr)

	for i in range(0,n):
		if(arr[i] == elem):
			return True

	return False

arr = [3]
elem = int(input())

print("Element is present in the array: ",lsearch(arr,elem))