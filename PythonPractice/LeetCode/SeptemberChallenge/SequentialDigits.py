def sequentialDigits(low,high):
	digit_dict = {2:(12,11),3:(123,111),4:(1234,1111),5:(12345,11111),6:(123456,111111),7:(1234567,1111111),8:(12345678,11111111),9:(123456789,111111111)}
	temp = low
	digits = 0

	while(temp > 0):
		digits += 1
		temp //= 10

	if(digits > 9):
		return []

	num,adder = digit_dict[digits]
	out = []

	while(num <= high and digits < 9):
		if(num >= low):
			out.append(num)

		num += adder
		last_dig = num%10

		if(last_dig == 9):
			if(num >= low and num <= high):
				out.append(num)
			digits += 1
			num, adder = digit_dict[digits]
	
	if(num >= low and num <= high):
		out.append(num)

	return out

low = 123456799
high = 234567890

print(sequentialDigits(low,high))