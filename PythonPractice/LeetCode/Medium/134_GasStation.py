def canCompleteCircuit(gas,cost):
	N = len(gas)
	neg_flag = False

	for i in range(N):
		gas[i] -= cost[i]
		if(gas[i] < 0):
			neg_flag = True

	if(not neg_flag):
		return 0

	start = running_sum = sum_so_far = 0
	for i in range(N):
		running_sum += gas[i]
		if(running_sum < 0):
			start = -1
			sum_so_far += running_sum
			running_sum = 0
		if(start == -1 and gas[i] >= 0):
			start = i

	if(running_sum + sum_so_far < 0):
		return -1
	else:
		return start



#gas = [1,2,3,4,5]
#cost = [3,4,5,1,2]
#gas = [2,3,4]
#cost = [3,4,3]
#gas = [6,1,4,3,5]
#cost = [3,8,2,4,2]
gas = [1,4,2,5]
cost = [3,2,5,1]

print(canCompleteCircuit(gas,cost))