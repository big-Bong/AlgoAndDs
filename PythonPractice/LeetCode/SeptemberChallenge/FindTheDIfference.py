def findTheDifference(s,t):
	M = len(s)
	N = len(t)
	if(N - M != 1):
		return ""

	dict = {}
	for c in s:
		if(c in dict):
			dict[c] += 1
		else:
			dict[c] = 1

	for c in t:
		if(c in dict):
			dict[c] -= 1
			if(dict[c] == 0):
				del dict[c]
		else:
			return c
def findTheDifference2(s,t):
	xor_val = 0
	for c in s+t:
		xor_val ^= ord(c)
	return (chr(xor_val))

s = "aabbcd"
t = "aabcbad"

print(findTheDifference(s,t))
