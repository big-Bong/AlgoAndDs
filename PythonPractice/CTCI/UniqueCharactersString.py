def uniqueCharString(string):
	arr = [0]*256
	for elem in string:
		asciival = ord(elem)
		if(arr[asciival] != 0):
			return False
		arr[asciival] = 1

	return True

def uniqueCharString2(string):
	checker = 0
	for elem in string:
		asciival = ord(elem) - ord('a')
		if((checker&(1<<asciival))>0):
			return False
		checker = checker | (1<<asciival)

	return True

string = 'abcdef'
string2 = 'abcdea'
string3 = 'skj@12a'

print(uniqueCharString(string))
print(uniqueCharString2(string))
print(uniqueCharString(string2))
print(uniqueCharString2(string2))
print(uniqueCharString(string3))