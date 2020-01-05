def countAndSay(n):
    out = "1"
    for _ in range(1,n):
        N = len(out)
        tempStr = ""
        count = 1
        i = 1
        while(i < N):
            if(out[i] == out[i-1]):
                count += 1
            else:
                tempStr += str(count)+out[i-1]
                count = 1
            i += 1
        tempStr += str(count)+out[N-1]
        out = tempStr
        
    
    return out

n = 10
print(countAndSay(n))