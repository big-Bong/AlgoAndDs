def pick_peaks(arr):
	ascCheck = False
	equalCheck = False
	pos = []
	peaks = []
	localPos = 0
	localPeak = 0

	for i in range(1,len(arr)):
		if(arr[i] < arr[i-1] and ascCheck):
			if(equalCheck):
				equalCheck = False
				pos.append(localPos)
				peaks.append(localPeak)
			else:
				pos.append(i-1)
				peaks.append(arr[i-1])
			ascCheck = False
		if(arr[i] == arr[i-1] and not equalCheck):
			equalCheck = True
			localPos = i-1
			localPeak = arr[i-1]
		if(arr[i] > arr[i-1]):
			ascCheck = True
			equalCheck = False

	return {"pos":pos,"peaks":peaks}

arr = [1,2,2,2,1,2,2,1,2,3,4,5,3]
print(pick_peaks(arr))