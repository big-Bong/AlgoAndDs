def likes(names):
    if(not names):
        return "no one likes this"
    N = len(names)
    if(N == 1):
        return names[0]+" likes this"
    elif(N == 2):
        return names[0]+" and "+names[1]+" like this"
    elif(N == 3):
        return names[0]+", "+names[1]+" and "+names[2]+" like this"
    else:
        return names[0]+", "+names[1]+" and "+str(N-2)+" others like this"

names = ["he","she","her"]
print(likes(names))