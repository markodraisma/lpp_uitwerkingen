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


if __name__ == "__main__":
    print("3 tot de macht 4 is:", macht(3,4))
    print("5 plus 6 is:", telop(5,6))
else:
    print("__name__ is nu:", __name__)





