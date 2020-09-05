def repeatedSubstringPattern(s):
	N = len(s)
	if(N == 1):
		return False

	i = N//2
	while(i > 0):
		flag = False
		if(N%i == 0):
			j = i
			while(j < N):
				if(s[:i] == s[j:j+i]):
					flag = True
				else:
					flag = False
					break
				j = j + i
			if(flag):
				return flag
		i -= 1
	return flag


s = "abcdaabcd"
print(repeatedSubstringPattern(s))
