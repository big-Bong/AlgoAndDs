"""
Remove all vowels from a string

Codewars
"""

def disemvowel(string):
    vowel_arr = ['a','e','i','o','u']
    
    for i in string:
        if(i.lower() in vowel_arr):
            ind = string.find(i)
            string = string[:ind]+string[ind+1:]
            
    return string

string = "This site is for losers...LOL!!!"
print(disemvowel(string))



"""
ALTERNATE SOLUTIONS

#1
def disemvowel(string):
	table = str.maketrans("","","aeiouAEIOU")
	return string.translate(table)

#2
def disemvowel(string):
	return ''.join(c for c in string if(c.lower() not in 'aeiou'))
"""