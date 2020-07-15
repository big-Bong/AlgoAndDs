def findLongestWord(s, d):
	longest_word = ""
	N = len(s)
	for word in d:
		ptr = -1
		flag = True
		if(len(word) <= N):
			for l in word:
				if(l in s):
					ind = s.find(l,ptr+1,N)
					if(ind != -1):
						ptr = ind
					else:
						flag = False
						break
				else:
					flag = False
					break
			
			if(flag):
				if((len(word) > len(longest_word)) or (len(word) == len(longest_word) and word < longest_word)):
					longest_word = word

	return longest_word

print(findLongestWord("abpcplea",["ale","apple","monkey","plea"]))