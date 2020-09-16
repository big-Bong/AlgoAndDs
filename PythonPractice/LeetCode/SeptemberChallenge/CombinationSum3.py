def combinationSum3(k, n):
	output = []
	combinationSum3Helper(k,n,[],output,0)
	return output

def combinationSum3Helper(k,n,inner,output,val):
	if(n == 0 and len(inner) == k):
		temp = [elem for elem in inner]
		output.append(temp)
		return output
	elif(n < 0):
		return output

	for i in range(val,9):
		inner.append(i+1)
		combinationSum3Helper(k,n-i-1,inner,output,i+1)
		inner.pop()

k = 4
n = 16
print(combinationSum3(k,n))
	