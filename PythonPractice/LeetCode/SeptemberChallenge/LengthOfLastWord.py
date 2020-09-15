def lengthOfLastWord(s):
	if(not s):
		return 0
	s = s.strip()
	len_last_word = 0
	i = len(s)

	while(i > 0 and s[i-1] != " "):
		len_last_word += 1
		i -= 1

	return len_last_word

s = "x y x"
print(lengthOfLastWord(s))
