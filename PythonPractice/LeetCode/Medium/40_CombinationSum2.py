def combinationSum2(candidates,target):
	N = len(candidates)
	output = []
	candidates.sort()
	combinationSum2Helper(candidates,output,[],N,target,0)
	return output

def combinationSum2Helper(candidates,output,input,N,target,i):
	if(target < 0):
		return output
	if(target == 0):
		temp = [elem for elem in input]
		output.append(temp)
		return output

	while(i < N):
		input.append(candidates[i])
		combinationSum2Helper(candidates,output,input,N,target-candidates[i],i+1)
		val = input.pop()
		i += 1
		while(i < N and val == candidates[i]):
			i += 1

#candidates = [10,1,2,7,6,1,5]
#target = 8
#candidates = [2,5,2,1,2]
candidates = [5,5,5]
target = 5
print(combinationSum2(candidates,target))


