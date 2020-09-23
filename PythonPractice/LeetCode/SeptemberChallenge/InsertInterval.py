def insert(intervals, newInterval):
	if(not intervals):
		intervals.append(newInterval)
		return intervals

	N = len(intervals)
	i = 0
	while(i < N):
		if(intervals[i][0] >= newInterval[0]):
			break
		i += 1

	if(i == N):
		if(newInterval[0] <= intervals[i-1][1]):
			if(newInterval[1]>intervals[i-1][1]):
				intervals[i-1] = [intervals[i-1][0],newInterval[1]]
		else:
			intervals.append(newInterval)

		return intervals
	if(i == 0):
		if(newInterval[1] >= intervals[i][0] and newInterval[1] <= intervals[i][1]):
			intervals[i] = [newInterval[0],intervals[i][1]]
			return intervals
		elif(newInterval[1] < intervals[i][0]):
			intervals = [newInterval]+intervals
			return intervals

	
	smaller = newInterval[0]
	if(i != 0 and newInterval[0] <= intervals[i-1][1]):
		smaller = intervals[i-1][0]
		i -= 1

	while(i < N):
		if(newInterval[1] >= intervals[i][1]):
			del intervals[i]
			N -= 1
		else:
			break

	if(i==N):
		intervals.append([smaller,newInterval[1]])
		return intervals

	if(newInterval[1] < intervals[i][0]):
		intervals = intervals[:i]+[[smaller,newInterval[1]]]+intervals[i:]
	else:
		intervals[i] = [smaller,intervals[i][1]]

	return intervals

#intervals = [[1,3],[6,9]]
#newInterval = [2,5]

#intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
#newInterval = [4,8]
#newInterval = [0,1]
#newInterval = [13,15]
#newInterval = [5,8]
#newInterval = [2,3]

#intervals = [[1,5]]
#newInterval = [6,8]

#intervals = [[0,5],[9,12]]
#newInterval = [7,16]

#intervals = [[1,5],[6,8]]
#newInterval = [0,9]

intervals = [[1,4],[5,14]]
newInterval = [-1,0]
print(insert(intervals,newInterval))
			

