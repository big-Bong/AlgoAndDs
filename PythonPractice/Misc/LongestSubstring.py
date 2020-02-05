def longestSubstring(string):
	if(not string):
		return 0
	N = len(string)
	if(N == 1):
		return N

	i = 0
	j = 1
	longest = j - i
	longestSubstring = string[0]
	dict = {string[0]:0}

	while(j<N):
		if(string[j] in dict and dict[string[j]] >= i):
			i = dict[string[j]] + 1
		
		dict[string[j]] = j
		j += 1
		if(j - i > longest):
			longest = j - i
			longestSubstring = string[i:j]

	return longest,longestSubstring

string = "abcbacbacdbeaacdebbrrbascsrebdfadbc"
print(longestSubstring(string))
