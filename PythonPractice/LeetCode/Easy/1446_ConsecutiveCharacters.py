def maxPower(s):
	if(not s):
		return 0

	maxP = 1
	N = len(s)
	counter = 1

	for i in range(N-1):
		if(s[i] == s[i+1]):
			counter += 1
			if(counter > maxP):
				maxP = counter
		else:
			counter = 1

	return maxP

s = "leetcode"
#s = "ee"
#s = "e"
#s = "eelleee"
#s = "elle"
#s = "abcc"
#s = "abcd"
#s = "aabbbcccc"
print(maxPower(s))
