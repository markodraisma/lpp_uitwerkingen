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
    print(telop(3,4)) # verwachte waarde: 7
    print(macht(3,0)) # verwachte waarde: 1
else:
     print("module %s is geïmporteerd" % __name__)
