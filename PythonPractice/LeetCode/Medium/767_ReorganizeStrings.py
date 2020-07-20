def reorganizeString(S):
	dict = {}
	for c in S:
		if(c in dict):
			dict[c] += 1
		else:
			dict[c] = 1
	
	dict = {k: v for k,v in sorted(dict.items(),key = lambda item: item[1], reverse = True)}
	i = 0
	maxVal = 0
	sumVal = 0
	for elem in dict:
		if(i == 0):
			maxVal = dict[elem]
		else:
			sumVal += dict[elem]
		i += 1
	
	output_str = ""
	if((maxVal - sumVal) <= 1):
		N = len(S)
		while(N>0):
			for elem in dict:
				if(dict[elem] != 0):
					if(output_str == "" or output_str[-1] != elem):
						output_str += elem
					else:
						for i in range(1,len(output_str)-1):
							if(output_str[i] != elem and output_str[i+1] != elem):
								output_str = output_str[:i+1]+elem+output_str[i+1:]
								break
							elif(output_str[i] != elem and output_str[i-1] != elem):
								output_str = output_str[:i]+elem+output_str[i:]
								break
					dict[elem] -= 1
			N -= 1
	
	return output_str

def isSequalS1(S,S1):
	dict = {}
	for c in S:
		if(c in dict):
			dict[c] += 1
		else:
			dict[c] = 1

	for c in S1:
		if(c in dict):
			dict[c] -= 1
		else:
			dict[c] = 1

	print(dict)

S = "zqugrfbsznyiwbokwkpvpmeyvaosdkedbgjogzdpwawwl"
S1 = "wzwgbokpdsyveaqurfnimjlwzgbokpdsyveawzgbokpdw"
#print(reorganizeString(S))
isSequalS1(S,S1)