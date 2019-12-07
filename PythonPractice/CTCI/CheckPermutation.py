def isAnagram(s, t):
    dict = {}
    for elem in s:
        if(elem not in dict):
            dict[elem] = 1
        else:
            dict[elem] += 1

    for elem in t:
        if(elem not in dict):
            return False
        else:
            dict[elem] -= 1

    for key,value in dict.items():
        if(value != 0):
            return False

    return True

s = 'anagram'
t = 'nagaram'
print(isAnagram(s,t))