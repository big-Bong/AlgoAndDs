def mergeInterval(intervals):
	if(not intervals):
		return []
	if(not intervals[0]):
		return [[]]
	intervals.sort()
	output = [intervals[0]]
	N = len(intervals)
	for i in range(1,N):
		if(intervals[i][0] <= output[-1][1]):
			if(output[-1][1]<=intervals[i][1]):
				val = output.pop()
				output.append([val[0],intervals[i][1]])
		else:
			output.append(intervals[i])

	return output

#intervals = [[3,6],[1,7],[4,9],[2,4],[1,5]]
intervals = [[]]
print(mergeInterval(intervals))