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

string = "baaaaaaaab"
print(longestPalindromicSubstring(string))

