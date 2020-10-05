def bitwiseComplement(N):
	if(N == 0):
		return 1
	for i in range(32):
		val = 2**i
		if(N < val):
			return (val-1-N)
		elif(N == val):
			return (2**(i+1)-1-N)

N = 999999999
print(bitwiseComplement(N))