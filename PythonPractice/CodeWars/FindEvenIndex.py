"""
Find the index in the array (if it exists) where the sum to the left hand side of the index and sum to the right hand side of the index
is equal.

CODEWARS
"""
"""
def find_even_index(arr):
    n = len(arr)
    for i in range(0,n):
        left_sum = sum(arr[:i])
        right_sum = sum(arr[i+1:])
        
        if(left_sum == right_sum):
            return i
    
    return -1
"""
"""
def find_even_index(arr):
	n = len(arr)
	left_sum_arr = [0]*n
	right_sum_arr = [0]*n

	for i in range(1,n):
		left_sum_arr[i] = left_sum_arr[i-1]+arr[i-1]
		right_sum_arr[n-i-1] = right_sum_arr[n-i]+arr[n-i]

	for j in range(0,n):
		if(left_sum_arr[j] == right_sum_arr[j]):
			return j

	return -1
"""

def find_even_index(arr):
	left_sum = 0
	right_sum = sum(arr)

	for i,a in enumerate(arr):
		right_sum -= a
		if(left_sum == right_sum):
			return i

		left_sum += a

	return -1

arr = [1,2,3,4,3,2,1]
print(find_even_index(arr))