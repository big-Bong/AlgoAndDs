def removeDuplicateLetter(s):
	N = len(s)
	if(N == 1):
		return s

	dict = {}
	for c in s:
		if(c in dict):
			dict[c] += 1
		else:
			dict[c] = 1
		
	output = ""
	ch_arr = [-1]*26
	for i,c in enumerate(s):
		pos = ord(c) - ord('a')
		if(ch_arr[pos] == -1):
			start = 0
			for j in range(25,pos,-1):
				if(ch_arr[j] != -1):
					if(ch_arr[j] >= start and ch_arr[j] < i):
						char = chr(j+ord('a'))
						if(dict[char] != 0):
							output = output[:ch_arr[j]]+output[ch_arr[j]+1:]
							ch_arr[j] = -1
						else:
							start = ch_arr[j]
			output += c
			ch_arr[pos] = len(output)-1
		dict[c] -= 1


	return output

s = "bcabc"
#s = "leetcode"
#s = "abacb"
#s = "cbacdcbc"
print(removeDuplicateLetter(s))
