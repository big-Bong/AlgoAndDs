def oneAway(str1, str2):
	l1 = len(str1)
	l2 = len(str2)
	if(abs(l1 - l2) > 1):
		return False

	if(l1 == l2):
		return compareEqualStrings(str1,str2,l1)
	else:
		longString, shortString = getLongerString(str1, str2)
		return compareUnequalStrings(longString,shortString)

def getLongerString(str1, str2):
	if(len(str1) > len(str2)):
		return (str1,str2)
	else:
		return (str2, str1)

def compareEqualStrings(str1,str2,length):
	count = 0
	for i in range(length):
		if(str1[i] != str2[i]):
			count += 1
		if(count > 1):
			return False
	return True

def compareUnequalStrings(str1,str2):
	count = 0
	j = 0
	for i in range(len(str1)):
		if(str1[i] != str2[j]):
			count += 1
		else:
			j += 1
		if(count > 1):
			return False
		if(j >= len(str2)):
			break
	return True

str1 = "pall"
str2 = "paltl"
print(oneAway(str1,str2))