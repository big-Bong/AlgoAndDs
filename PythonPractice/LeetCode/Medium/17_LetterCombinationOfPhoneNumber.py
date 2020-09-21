def letterCombination(digits):
	dict = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
	if(not digits):
		return []

	N = len(digits)
	output = []
	letterCombinationHelper(digits,dict,output,"",N,0)
	return output

def letterCombinationHelper(digits,dict,output,my_str,N,digit_no):
	if(len(my_str) == N):
		output.append(my_str)
		return

	for elem in dict[digits[digit_no]]:
		my_str += elem
		letterCombinationHelper(digits,dict,output,my_str,N,digit_no+1)
		my_str = my_str[:-1]

digits = "237"
print(letterCombination(digits))

