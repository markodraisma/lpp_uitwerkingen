#!/usr/bin/env python3
'''Dit is een verzameling van nuttige functies
'''

priem = (2,3,5,7,11,13,17,19,23,29)

def telop(a,b):
    '''Deze functie telt twee variablen bijelkaar op
    '''
    return a+b

def macht(grondgetal, exponent):
    '''Deze functie doet iets nuttigs
    '''
    return grondgetal ** exponent

def myfunc(*args, **kwargs):
    '''Dit is een functie om *args en **kwargs te demonstreren
    '''
    print('positional arguments:')
    for a in args:
        print(a)
    print('keyword args:')
    for k in kwargs:
        print(k, kwargs[k])

getal = 10
