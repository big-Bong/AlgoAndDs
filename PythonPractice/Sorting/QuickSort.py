def quickSort(arr,low,high):
	if(low<high):
		arr_pt = partition(arr,low,high)
		quickSort(arr,low,arr_pt-1)
		quickSort(arr,arr_pt+1,high)

def partition(arr,low,high):
	val = arr[high]
	i = low -1
	for j in range(low,high):
		if(arr[j]<val):
			i += 1
			temp = arr[i]
			arr[i] = arr[j]
			arr[j] = temp

	arr[high] = arr[i+1]
	arr[i+1] = val
	return i+1

arr = []
quickSort(arr,0,len(arr)-1)
print(arr)