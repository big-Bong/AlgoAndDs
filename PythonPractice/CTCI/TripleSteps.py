def tripleSteps(n):
	if(n==1 or n==2):
		return n
	if(n==3):
		return n+1

	a = 1
	b = 2
	c = 4
	d = 0

	for i in range(3,n):
		d = a+b+c
		a = b
		b = c
		c = d

	return d

n = 5
print(tripleSteps(n))
