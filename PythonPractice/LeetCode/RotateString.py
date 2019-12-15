def rotateString(A: str, B: str) -> bool:
    if(len(A) != len(B)):
        return False
    
    i = j = start = 0
    flag = False

    while(i<len(A)):
        if(A[i] != B[j]):
            if(flag):
                i = start + 1
                j = 0
                flag = False
            else:
                i += 1
        else:
            if(not flag):
                start = i
            i += 1
            j += 1
            flag = True
        
    return(B[j:]==A[:start])

A = "anna"
B = "nnaa"
print(rotateString(A,B))