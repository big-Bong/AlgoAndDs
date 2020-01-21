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
	return n if (n<10) else digital_root2(sum(map(int,str(n))))

print(digital_root(989891))
print(digital_root2(989891))