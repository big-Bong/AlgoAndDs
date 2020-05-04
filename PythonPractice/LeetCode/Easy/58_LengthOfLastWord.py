def lengthOfLastWord(s):
	return len(s.strip().split(" ")[-1])

s = "Hello World   "
print(lengthOfLastWord(s))