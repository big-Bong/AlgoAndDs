#Union-Find Algorithm. Assuming Graph vertices are labeled as 0, 1, 2 etc.

#Find - Find's whether two vertices belong to same subset or not
def find(arr,v1,v2):
	start_v1 = arr[v1]
	while(start_v1 != -1):
		v1 = start_v1
		start_v1 = arr[v1]

	start_v2 = arr[v2]
	while(start_v2 != -1):
		v2 = start_v2
		start_v2 = arr[v2]

	return [v1==v2,v1,v2]

#Union - Unites two subsets into single set
def union(arr,v1,v2):
	v1 = find(arr,v1,v2)[1]
	v2 = find(arr,v1,v2)[2]

	arr[v1] = v2

	return arr

N = 5
arr = [-1]*N
arr = union(arr,0,1)
print(arr)
arr = union(arr,1,2)
print(arr)
arr = union(arr,2,3)
arr = union(arr,1,4)
print(arr)
print(find(arr,3,4)[0])



