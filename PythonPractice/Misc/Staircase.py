def numberOfStairs(s):
	if(s == 0):
		return 1;
	if(s == 1):
		return 1;

	return (numberOfStairs(s-1) + numberOfStairs(s-2))


print(numberOfStairs(2))
