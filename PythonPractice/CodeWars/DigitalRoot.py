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

print(digital_root(989891))