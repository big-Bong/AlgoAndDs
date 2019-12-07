def palindromePerm(s):
	arr = [0]*256
	for elem in s:
		if(elem.isalnum()):
			indexVal = ord(elem)
			arr[indexVal] += 1
	
	count = 0
	for val in arr:
		if(val%2 != 0):
			count += 1
	
	return (count <= 1)

def palindromePerm2(s):
	checker = 0
	for elem in s:
		if(elem.isalnum()):
			indexVal = ord(elem) - ord('a')
			checker ^= (1<<indexVal)

	return ((checker&(checker-1)==0))

s = "A man, a plan, a canal: Panama"
s1 = "bbcdbb"
print(palindromePerm(s.lower()))
print(palindromePerm2(s1.lower()))