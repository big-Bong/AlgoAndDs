#METHOD1
def digital_root(n):
    sum = 0
    while((n+sum)>=10):
        q,r = divmod(n,10)
        sum += r
        n = q
        if(n==0):
            n = sum
            sum = 0
    
    return (n+sum)

#METHOD2
def digital_root2(n):
	s = str(n)
	arr = []
	for elem in s:
		arr.append(int(elem))
	if(sum(arr)<10):
		return sum(arr)
	return digital_root2(sum(arr))

print(digital_root(989891))
print(digital_root2(989891))