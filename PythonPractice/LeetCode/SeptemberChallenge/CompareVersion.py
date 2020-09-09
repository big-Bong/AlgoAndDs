def compareVersion(version1,version2):
	if(version1 == version2):
		return 0

	version1_arr = version1.split(".")
	version2_arr = version2.split(".")

	N = len(version1_arr)
	M = len(version2_arr)

	i = 0
	j = 0

	while(i < N and j < M):
		if(int(version1_arr[i]) < int(version2_arr[j])):
			return -1
		if(int(version1_arr[i]) > int(version2_arr[j])):
			return 1
		
		i += 1
		j += 1

	while(i < N):
		if(int(version1_arr[i]) != 0):
			return 1
		i += 1

	while(j < M):
		if(int(version2_arr[j]) != 0):
			return -1
		j += 1

	return 0


version1 = "1.0"
version2 = "1.0.0"

print(compareVersion(version1,version2))