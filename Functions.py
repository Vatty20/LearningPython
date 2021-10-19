''' Built-in functions
int() / float() / eval()
input()
min() / max()
abs()
type()
len()
round()
range()'''

''' A module is a file containing functions and variables defined in separate files. A module is simply 
a file that contains Python code. When we break a program into modules, each module should contain 
functions that perform related tasks.
math
random
string
'''

#import math as m 
#print(m.pi) #3.141592653589793

from math import cos, sin

print(cos(3.14)) #-0.9999987317275395
print(sin(3.14)) #0.0015926529164868282

'''User-defined functions
Syntax: def function_name(parameters):
'''

#def greet():
 #   print('Good Morning')
    
#greet()
'''
def greet(name):
    print('Good Morning,', name)
    
greet(input('Enter name: '))
'''

def greet(name, dish):
    print('Good Morning,', name)
    print('Please eat', dish)
    
greet(input('Enter name: '), input('Enter dish: '))

#def greet(name, dish="Pasta")

def sum_of_list(a):
    print('Calculating...')
    
    return sum(a)
    
marks = [45, 16, 53, 9, 36]
sum_of_marks = sum_of_list(marks)

print('Sum of marks is', sum_of_marks)

