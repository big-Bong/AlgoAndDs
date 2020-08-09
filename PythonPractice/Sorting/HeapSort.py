def heapSort(arr):
	if(not arr):
		return []
	if(len(arr) <= 1):
		return arr

	n = len(arr)
	for i in range(n//2 - 1,-1,-1):
		heapify(arr,n,i)
	for i in range(n-1,0,-1):
		arr[0],arr[i] = arr[i],arr[0]
		heapify(arr,i,0)

def heapify(arr,n,i):
	largest = i
	left = 2*i + 1
	right = 2*i + 2
	
	if(left < n and arr[largest] < arr[left]):
		largest = left
	if(right < n and arr[largest] < arr[right]):
		largest = right

	if(largest != i):
		arr[largest],arr[i] = arr[i],arr[largest]
		heapify(arr,n,largest)

arr = [6,3,9,2,5,1,8,3]
heapSort(arr)
print(arr)