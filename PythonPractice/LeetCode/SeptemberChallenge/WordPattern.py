def wordPattern(pattern,str):
	if(not pattern and not str):
		return True
	
	N = len(pattern)
	arr = str.split()
	M = len(arr)
	if(N != M):
		return False

	dict1 = {}
	dict2 = {}
	for i in range(N):
		if(pattern[i] in dict1):
			if(arr[i] != dict1[pattern[i]]):
				return False
		if(arr[i] in dict2):
			if(pattern[i] != dict2[arr[i]]):
				return False
		else:
			dict1[pattern[i]] = arr[i]
			dict2[arr[i]] = pattern[i]

	return True

pattern = "abc"
str = "b c a"

print(wordPattern(pattern,str))
