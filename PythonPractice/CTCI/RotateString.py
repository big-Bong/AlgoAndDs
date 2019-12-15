def rotateString(s1,s2):
	if(len(s1) != len(s2)):
		return False

	return (s1 in (s2+s2))

s1 = "anna"
s2 = "nnaa"
print(rotateString(s1,s2))