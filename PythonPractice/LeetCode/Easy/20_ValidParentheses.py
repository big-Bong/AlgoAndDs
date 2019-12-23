def isValid(s):
	if(s.strip() == ""):
		return True
	stack = []
	dict = {"[":"]","{":"}","(":")"}
	for i in range(len(s)):
		if(peek(stack) != s[i]):
			if(s[i] in dict):
				stack.append(dict[s[i]])
			else:
				return False
		else:
			stack.pop()

	return (not stack)

def peek(stack):
	if(stack):
		return stack[-1]
	return None

s = "{{[)}}"
print(isValid(s))