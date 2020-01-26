def first_non_repeating_letter(string):
    if(not string):
        return ""
    
    dict = {}
    for elem in string:
        e = elem.lower()
        if(e in dict):
            dict[e] += 1
        else:
            dict[e] = 1

    for elem in string:
        if(dict[elem.lower()] == 1):
            return elem
    
    return ""

string = "sTreSS"
print(first_non_repeating_letter(string))