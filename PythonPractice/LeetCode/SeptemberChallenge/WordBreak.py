import re

def wordBreak(s,wordDict):
	pos_dict = {}
	for word in wordDict:
		for m in re.finditer('(?='+word+')',s):
			start = m.start()
			if(start in pos_dict):
				pos_dict[start].append(start+len(word)-1)
			else:
				pos_dict[start] = [start+len(word)-1]

	print(pos_dict)

	end = len(s) - 1
	return DFS(pos_dict,0,end)

def DFS(pos_dict,start,end):
	if(start not in pos_dict):
		return False
	if(start > end):
		return False
	if(start==end):
		return True

	for elem in pos_dict[start]:
		if(elem == end):
			return True
		if(DFS(pos_dict,elem+1,end)):
			return True

	return False

#s = "catsandog"
#wordDict = ["cats", "dog", "sand", "and", "cat"]

#s = "applepenapple"
#wordDict = ["apple", "pen"]

#s = "leetcode"
#wordDict = ["leet", "code"]

s = "aaaaaaa"
wordDict = ["aaaa","aaa"]
print(wordBreak(s,wordDict))