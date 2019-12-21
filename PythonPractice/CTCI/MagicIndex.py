def magicIndex(arr,start,end):
	if(end < start):
		return "Doesn't exist"
	
	mid = start + int((end-start)/2)
	if(arr[mid] == mid):
		return mid
	elif(arr[mid] > mid):
		end = mid - 1
		return magicIndex(arr,start,end)
	else:
		start = mid+1
		return magicIndex(arr,start,end)

arr = [-2,0,1,2,3,4,5,6,7,10]
print(magicIndex(arr,0,len(arr)-1))