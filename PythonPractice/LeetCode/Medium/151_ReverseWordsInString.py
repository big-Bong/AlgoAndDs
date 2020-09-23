def reverseWord(s):
	if(not s):
		return s
	s_arr = s.strip().split()
	s = " ".join(s_arr[::-1])

	return s.strip()

s = "  hello world!  "
print(reverseWord(s))
