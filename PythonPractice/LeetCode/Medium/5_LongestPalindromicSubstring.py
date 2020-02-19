def longestPalindromicSubstring(string):
	if(not string):
		return
	N = len(string)
	print(N)
	if(N == 1):
		return string

	longestString = ""
	for i in range(1,N):
		start = 0
		end = i
		while(end < N):
			if(isPalindrome(string[start:end+1])):
				longestString = string[start:end+1]
				break

			start += 1
			end += 1

	return longestString

def isPalindrome(string):
	start = 0
	end = len(string) - 1

	while(start <= end):
		if(string[start] != string[end]):
			return False

		start += 1
		end -= 1

	return True

def longestPalindromicSubstringDP(string):
	if(not string):
		return ""

	N = len(string)
	table = [[0 for j in range(N)] for i in range(N)]

	for i in range(N):
		table[i][i] = 1

	maxLength = 1
	output = string[0]

	for i in range(N-1):
		if(string[i] == string[i+1]):
			table[i][i+1] = 1
			maxLength = 2
			output = string[i:i+maxLength]

	for j in range(2,N):
		for i in range(N-1):
			if(table[i+1][j-1] and string[i]==string[j]):
				table[i][j] = 1
				length = j - i + 1
				if(length > maxLength):
					maxLength = length
					output = string[i:i+maxLength]

	return output

string = "bdaac"
print(longestPalindromicSubstringDP(string))

