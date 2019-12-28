def strStr(haystack, needle):
    N = len(haystack)
    M = len(needle)
    
    if(M==0):
        return 0

    i = 0
    while(i<N):
        if(haystack[i] == needle[0] and i+M <= N):
            tempHay = haystack[i:i+M]
            if(tempHay==needle):
                return i
        i += 1
    
    return -1

str1 = "hello"
str2 = "ll"
print(strStr(str1,str2))