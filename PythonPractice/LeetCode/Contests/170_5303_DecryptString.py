def freqAlphabets(s):
    arr = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    
    if(not s):
        return
    
    N = len(s)
    
    if(N==1):
        return arr[int(s[0])-1]
    
    if(N==2):
        return arr[int(s[0])-1]+arr[int(s[1])-1]
    
    output = ""
    i = 0
    
    while(i<N):
        if((i+2 < N) and s[i+2] == "#"):
            output += arr[int(s[i:i+2])-1]
            i += 3
        else:
            output += arr[int(s[i])-1]
            i += 1
    
    return output

s = "10#11#12"
print(freqAlphabets(s))