def mergeSort(arr,l,r):
	if(l<r):
		mid = l + ((r-l)//2)
		mergeSort(arr,l,mid)
		mergeSort(arr,mid+1,r)
		merge(arr,l,mid,r)
	return arr

def merge(arr,l,mid,r):
	i = l
	j = mid+1

	while(i < j and j <= r):
		if(arr[i] >= arr[j]):
			temp = arr[j]
			left = i
			right = j
			while(left<right):
				arr[right] = arr[right-1]
				right -= 1
			arr[i] = temp
			j += 1
		i += 1

def mergeSortOptimized(arr):
	N = len(arr)
	if(N>1):
		mid = N//2
		L = arr[:mid]
		R = arr[mid:]
		mergeSortOptimized(L)
		mergeSortOptimized(R)

		i = j = k = 0
		while(i < len(L) and j < len(R)):
			if(L[i] < R[j]):
				arr[k] = L[i]
				i += 1
			else:
				arr[k] = R[j]
				j += 1
			k += 1

		while(i < len(L)):
			arr[k] = L[i]
			i += 1
			k += 1

		while(j < len(R)):
			arr[k] = R[j]
			j += 1
			k += 1
	return arr

arr = [4,2,3,1]
print(mergeSortOptimized(arr))