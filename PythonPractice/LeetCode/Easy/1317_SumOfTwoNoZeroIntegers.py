def getNoZeroIntegers(n):
	i,j = 1,n-1

	while(True):
		if(not hasZero(i) and not hasZero(j)):
			return [i,j]
		i += 1
		j -= 1

def hasZero(n):
	while (n != 0):
		if(n%10 == 0):
			return True

		n //= 10
	return False

n = 1403
print(getNoZeroIntegers(n))