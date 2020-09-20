def combinationSum(candidates, target):
	N = len(candidates)
	output = []

	combinationSumHelper(candidates,target,[],output,0,N)

	return output

def combinationSumHelper(candidates,target,input,output,start,N):
	if(target < 0):
		return
	if(target == 0):
		temp = [elem for elem in input]
		output.append(temp)
		return

	for i in range(start,N):
		elem = candidates[i]
		input.append(elem)
		combinationSumHelper(candidates,target-elem,input,output,i,N)
		input.pop()

candidates = [2]
target = 8

print(combinationSum(candidates,target))