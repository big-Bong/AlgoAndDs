def magicIndex2(arr,start,end):
	if(end<start):
		return

	mid = start + int((end-start)/2)
	found = None

	if(arr[mid] == mid):
		return mid
	elif(arr[mid] > mid):
		found = jumpCheck(arr,arr[mid],end)
		if(found == None):
			return magicIndex2(arr,start,mid-1)
	else:
		found = jumpCheck1(arr,start,arr[mid])
		if(found == None):
			return magicIndex2(arr,mid+1,end)

	return found

def jumpCheck(arr,start,end):
	if(start > end):
		return

	if(arr[start] == start):
		return start
	else:
		return jumpCheck(arr,arr[start],end)

def jumpCheck1(arr,start,end):
	if(start > end):
		return

	if(arr[end] == end):
		return end
	else:
		return jumpCheck1(arr,start,arr[end])

arr = [0,0,1,2,3,3,3,3,6,10]
print(magicIndex2(arr,0,len(arr)-1))
