def getHint(secret, guess):
	dict = {}
	for elem in secret:
		if(elem in dict):
			dict[elem] += 1
		else:
			dict[elem] = 1

	output_dict = {'A':0,'B':0}
	N = len(guess)
	remaining_guess = ""
	for i in range(N):
		if(guess[i] in dict and dict[guess[i]] > 0):
			if(guess[i] == secret[i]):
				output_dict['A'] += 1
				dict[guess[i]] -= 1
			else:
				remaining_guess += guess[i]

	N = len(remaining_guess)
	for i in range(N):
		if(remaining_guess[i] in dict and dict[remaining_guess[i]] > 0):
				output_dict['B'] += 1
				dict[remaining_guess[i]] -= 1


	return str(output_dict['A'])+'A'+str(output_dict['B'])+'B'

secret = "1771"
guess = "1171"
print(getHint(secret,guess))