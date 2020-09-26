def largestNumber(nums):
	if(not nums):
		return ""

	if(sum(nums) == 0):
		return "0"

	N = len(nums)
	maxDigits = 0
	for i in range(N):
		digits = findNoDigits(nums[i])
		nums[i] = (nums[i],digits)
		if(digits > maxDigits):
			maxDigits = digits

	for i in range(N):
		number, digits = nums[i]
		if(digits != maxDigits):
			temp = digits
			nums [i] = (convertNumber(number,temp,maxDigits), digits)

	nums = sorted(nums,key = lambda x: x[0],reverse=True)
	output = ""

	for i in range(N):
		number1,digits1 = nums[i]
		if(i+1 < N):
			number2,digits2 = nums[i+1]
			if(number1 == number2 and digits1 != digits2):
				if(str(number2)[:digits2][-1] > str(number1)[:digits1][-1]):
					nums[i+1],nums[i] = nums[i],nums[i+1]
		number, digits = nums[i]
		output += str(number)[:digits]

	return output

def convertNumber(number,digits,maxDigits):
	temp = number
	temp_str = str(temp)
	i = 0
	while(i < maxDigits-digits):
		temp_str += temp_str[i]
		i += 1
	return int(temp_str)

def findNoDigits(number):
	digits = 1
	q, r = divmod(number,10)
	while(q > 0):
		q, r = divmod(q,10)
		digits += 1

	return digits

#nums = [3,30,34,5,9]
#nums = [10,2]
#nums = [128,12]
#nums = [121,12]
nums = [1,2,4,8,16,32,64,128,256,512]
#nums = [8308,830]

print(largestNumber(nums))