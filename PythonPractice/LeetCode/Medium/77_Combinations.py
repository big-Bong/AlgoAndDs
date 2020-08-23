def combine(n, k):
	data = [0 for _ in range(k)]
	arr = [i+1 for i in range(n)]
	final_arr = []
	return combineHelper(arr,data,0,len(arr)-1,0,k,final_arr)

def combineHelper(arr,data,start,end,index,k,final_arr):
	if(index == k):
		temp = [elem for elem in data]
		final_arr.append(temp)
		return

	i = start

	while(i <= end and end - i + 1 >= k - index):
		data[index] = arr[i]
		combineHelper(arr,data,i+1,end,index+1,k,final_arr)
		i += 1

	return final_arr

print(combine(1,1))