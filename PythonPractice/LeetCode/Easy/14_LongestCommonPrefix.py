from typing import List

def longestCommonPrefix(strs: List[str]) -> str:
	if(len(strs) == 0):
		return ""
	if(len(strs) == 1):
		return strs[0]

	lcp_main = strs[0]
	for i in range(1,len(strs)):
		lcp = ""
		word = strs[i]
		for j in range(len(lcp_main)):
			if(j<len(word) and lcp_main[j] == word[j]):
				lcp += word[j]
			else:
				break
		if(lcp == ""):
			return ""
		else:
			lcp_main = lcp
	return lcp_main

def longestCommonPrefixOptimized(strs: List[str]) -> str:
	if not strs:
		return ""
	
	prefix = strs[0]
	for word in strs[1:]:
		j = 0
		while j < min(len(prefix),len(word)) and prefix[j] == word[j]:
			j += 1
		prefix = word[:j]
		if not prefix:
			return ""

	return prefix


if __name__ == "__main__":
	strs = ["aa"]
	print(longestCommonPrefixOptimized(strs))
