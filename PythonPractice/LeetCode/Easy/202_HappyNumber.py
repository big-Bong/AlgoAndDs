def checkHappyNumber(n):
	dict = {}
	while(n != 1):
		q,r = divmod(n,10)
		temp = r**2
		while(q != 0):
			q,r = divmod(q,10)
			temp += r**2

		if(temp in dict):
			return False
		dict[temp] = 1
		n = temp

	return True

n = 34
print(checkHappyNumber(n))