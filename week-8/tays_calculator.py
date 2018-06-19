# Author: David Tays 
#		 Date:  06/19/2018  
#		 modified by: David Tays
#    Desc:  python functions and conditionals



def intCheck(val1, val2):
    if type(val1) == int and type(val2) == int:
        return True
    else:
        return False

def add(a, b):
    if intCheck(a, b):
        return a + b
    else:
        return "Check that your numbers are numbers please"

def subtract(a, b):
    if intCheck(a, b):
        return a - b
    else:
        return "Check that your numbers are numbers please"

def divide(a, b):
    if intCheck(a, b):
        return a / b
    else:
        return "Check that your numbers are numbers please"

print(add(1, 2))

print(subtract(4,1))

print(divide(8,2))