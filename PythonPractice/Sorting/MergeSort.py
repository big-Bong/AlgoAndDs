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

arr = [4,2,1,3]
print(mergeSort(arr,0,len(arr) - 1))