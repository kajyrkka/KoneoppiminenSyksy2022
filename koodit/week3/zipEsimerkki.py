import numpy as np
import matplotlib.pyplot as plt
import sys
import time

'''
Python’s zip() function is defined as zip(*iterables). 
The function takes in iterables as arguments and returns an iterator. 
This iterator generates a series of tuples containing elements from 
each iterable. 
zip() can accept any type of iterable, such as files, lists, 
tuples, dictionaries, sets, and so on.
'''

a = ["Kari", "Pekka"]
b = ["Jyrkka","Patka"]
c = ["lehtori","nayttelija"]
d = [1,2]

print( [(x+y+z+str(xx)) for x,y,z,xx in zip(a,b,c,d) ])
'''
foo,bar = zip(a,b)
for fool,baar in foo,bar:
    print(fool)
    print(baar)

for i,j in foo,bar:
    print(i+j)
'''