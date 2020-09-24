def canCompleteCircuit(gas,cost):
	N = len(gas)
	neg_flag = False

	for i in range(N):
		gas[i] -= cost[i]
		if(gas[i] < 0):
			neg_flag = True

	if(not neg_flag):
		return 0

	for i in range(N):
		if(gas[i] >= 0):
			if(canComplete(gas,i,N)):
				return i
	return -1

def canComplete(gas,start_pos,N):
	i = start_pos
	end_pos = i-1 if(start_pos != 0) else N - 1
	final_sum = 0
	while(i != end_pos):
		final_sum += gas[i]
		if(final_sum < 0):
			return False
		i += 1
		if(i == N):
			i = 0
	final_sum += gas[i]
	if(final_sum < 0):
		return False

	return True



#gas = [1,2,3,4,5]
#cost = [3,4,5,1,2]
#gas = [2,3,4]
#cost = [3,4,3]
gas = [6,1,4,3,5]
cost = [3,8,2,4,2]

print(canCompleteCircuit(gas,cost))