import math

def sum_for_list(lst):
	if(not lst):
		return []

	output = []

	for elem in lst:
		temp = elem
		if(elem < 0):
			temp = -elem
		if(isPrime(temp) and temp not in output):
			output.append(temp)
		else:
			for i in range(2,int(math.sqrt(temp))+1):
				if(elem%i == 0):
					insertInOutputHelper(i,elem,output)

	output.sort()
	for i in range(len(output)):
		sum_val = 0
		val = output[i]
		for elem in lst:
			if(elem%val == 0):
				sum_val += elem
		output[i] = [val,sum_val]	

	return output


def insertInOutputHelper(num,elem,output):
	if(isPrime(num)):
		insertInOutput(num,output)
	otherFact = elem // num
	if(otherFact < 0):
		otherFact = -otherFact
	if(isPrime(otherFact)):
		insertInOutput(otherFact,output)

def insertInOutput(factor,output):
	if(factor not in output):
		output.append(factor)

def isPrime(n):
	if(n<=1):
		return False
	if(n==2 or n==3):
		return True

	if(n%2 == 0 or n%3 == 0):
		return False

	i = 5
	while(i*i <= n):
		if(n%i == 0 or n%(i+2) == 0):
			return False
		i += 6

	return True

arr = [106, -186, -29, -51, -124, 122, -73, -50, -17, -144, 188, -40, -25, -135]
print(sum_for_list(arr))