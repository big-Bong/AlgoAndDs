def spliceString(s):
	n = len(s)
	if(n%2 != 0):
		s += "_"
	return [s[i:i+2] for i in range(0,n,2)]

s = 'abcde'
print(spliceString(s))