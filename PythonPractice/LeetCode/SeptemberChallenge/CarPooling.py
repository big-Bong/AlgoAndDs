def carPooling(trips,capacity):
	N = len(trips)
	if(N == 0):
		return True

	trips_e = [elem for elem in trips]
	trips = sorted(trips,key=lambda x: x[1])
	trips_e = sorted(trips_e,key=lambda x: x[2])
	total_capacity = trips[0][0]
	end_time = trips_e[0][2]
	j = 0

	for i in range(1,N):
		if(trips[i][1] >= end_time):
			while(j < N and trips_e[j][2] <= trips[i][1]):
				total_capacity -= trips_e[j][0]
				j += 1
			end_time = trips_e[j][2]

		total_capacity += trips[i][0]
		if(total_capacity > capacity):
			return False

	return True

def carPooling2(trips,capacity):
	timestamp = []
	for trip in trips:
		timestamp.append([trip[1], trip[0]])
		timestamp.append([trip[2], -trip[0]])

	timestamp.sort()

	total_capacity = 0
	for time,time_capacity in timestamp:
		total_capacity += time_capacity
		if(total_capacity > capacity):
			return False
	return True


#trips = [[3,2,7],[3,7,9],[8,3,9]]
trips = [[2,1,8],[3,5,6],[1,1,3],[4,6,10]]
#trips = []
capacity = 6

print(carPooling2(trips,capacity))

