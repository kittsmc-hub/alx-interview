#!/usr/bin/python3
"""a function that returns a list of lists of integers representing the pascalstriangle"""

def pascal_triangle(n):
    r = [1]

    for i in range(n):
        print(r)
        tr = [0] + r
        r = r + [0]
        r = [x+y for x,y in zip(r,tr)]

pascal(6)
