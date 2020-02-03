def pick_peaks(arr):
	ascCheck = False
	pos = []
	peaks = []

	for i in range(1,len(arr)):
		if(arr[i] < arr[i-1] and ascCheck):
			pos.append(localPos)
			peaks.append(localPeak)
			ascCheck = False
		if(arr[i] > arr[i-1]):
			ascCheck = True
			localPos = i
			localPeak = arr[i]


	return {"pos":pos,"peaks":peaks}

arr = [1,2,3,3,4,4,3,3,1,2,3,4,4,3,4,5,4]
print(pick_peaks(arr))