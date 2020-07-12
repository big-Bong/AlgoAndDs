def addBinary(a, b):
	carry = 0
	output_str = ""
	len_a = len(a)
	len_b = len(b)
	
	if(len_a>len_b):
		b = "0"*(len_a - len_b)+b
	else:
		a = "0"*(len_b - len_a)+a

	len_a = len(a)

	for i in range(len_a-1,-1,-1):
		if(carry==0):
			if(a[i] == "1" and b[i] == "1"):
				output_str += "0"
				carry = 1
			elif((a[i] == "1" and b[i] == "0") or (a[i] == "0" and b[i] == "1")):
				output_str += "1"
			else:
				output_str += "0"
		else:
			if(a[i] == "1" and b[i] == "1"):
				output_str += "1"
				carry = 1
			elif((a[i] == "1" and b[i] == "0") or (a[i] == "0" and b[i] == "1")):
				output_str += "0"
				carry = 1
			else:
				output_str += "1"
				carry = 0

	if(carry==1):
		output_str += "1"

	return (output_str[::-1])
			

print(addBinary("110","1011"))