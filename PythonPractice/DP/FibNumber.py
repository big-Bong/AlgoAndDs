#Find Nth Fibonacci number

def fibonacci1(n):
	if(n == 1):
		return 0
	if(n == 2):
		return 1

	return fibonacci1(n-2)+fibonacci1(n-1)

def fibonacci2(n):
	if(arr[n-1]):
		return arr[n-1]

	if(n==1):
		arr[0] = 0
		return 0
	if(n==2):
		arr[1] = 1
		return 1

	arr[n-1] = fibonacci2(n-1)+fibonacci2(n-2)
	return arr[n-1]

def fibonacci3(n):
	arr[0] = 0
	arr[1] = 1
	for i in range(3,n+1):
		arr[i-1] = arr[i-2]+arr[i-3]

	return arr[n-1]




n = 1000
arr = [None]*1000
#print("5th Fibonnaci number",fibonacci1(5))
#print("20th Fibonnaci number",fibonacci1(20))
print("50th Fibonnaci number",fibonacci3(1000))