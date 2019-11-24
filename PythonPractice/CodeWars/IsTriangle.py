"""
Given 3 numbers, check whether they can form a triangle or not

Codewars
"""
"""
def is_triangle(a, b, c):
    return True if ((a+b>c) and (a+c>b) and (b+c>a)) else False
"""

def is_triangle(a, b, c):
    return True if ((a+b>c) and (a+c>b) and (b+c>a)) else False

print("Is triangle: ",is_triangle(2,3,4))



"""
ALTERNATE SOLUTIONS

#1
def is_triangle(a, b, c):
	return ((a+b)>c and (a+c)>b and (b+c)>a)

#2
def is_triangle(a, b, c):
	a, b, c = sorted([a,b,c])
	return (a+b)>c

#3
def is_triangle(a, b, c):
	return abs(a-b) < c < a+b
"""