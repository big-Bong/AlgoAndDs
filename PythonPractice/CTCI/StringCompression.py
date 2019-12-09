def compression(string):
	count = 1
	new_string = []

	for i in range(1,len(string)):
		if(string[i] == string[i-1]):
			count += 1
		else:
			new_string.append(string[i-1]+str(count))
			count = 1
	new_string.append(string[len(string)-1]+str(count))
	new_string = "".join(new_string)
	return min(string,new_string,key=len)

string = "abcd"
print(compression(string))
string = "aaabbaaabbbbdd"
print(compression(string))
string = "aabcccccaaa"
print(compression(string))