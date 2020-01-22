def compareStrings(A,B):
	A_arr = A.split()
	B_arr = B.split()
	output = []
	
	for elem in B_arr:
		B_char_arr = [0]*26
		for c in elem:
			B_char_arr[ord(c)-ord('a')] += 1
		j = 0
		for b_c in B_char_arr:
			if(b_c != 0):
				j = b_c
				break
		count = 0
		for a_elem in A_arr:
			A_char_arr = [0]*26
			for a_c in a_elem:
				A_char_arr[ord(a_c)-ord('a')] += 1
			i = 0
			for a_c in A_char_arr:
				if(a_c != 0):
					i = a_c
					break
			if(i<j):
				count += 1
		output.append(count)

	return output

A = 'abcd aabc bd'
B = 'aaa aa'
print(compareStrings(A,B))