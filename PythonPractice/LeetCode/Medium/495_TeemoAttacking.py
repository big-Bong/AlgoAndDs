def findPoisonedDuration(timeSeries,duration):
	if(not timeSeries or duration == 0):
		return 0

	totalDuration = 0
	expiration = timeSeries[0]+duration
	start_point = timeSeries[0]
	N = len(timeSeries)
	for i in range(1,N):
		if(timeSeries[i] < expiration):
			totalDuration += (timeSeries[i] - start_point)
		else:
			totalDuration += duration

		expiration = timeSeries[i]+duration
		start_point = timeSeries[i]

	return (totalDuration+duration)

timeSeries = [1,5,8,13]
duration = 5
print(findPoisonedDuration(timeSeries,duration))